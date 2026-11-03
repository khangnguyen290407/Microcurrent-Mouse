import os, sys, math, heapq
import pcbnew

sys.path.insert(0, r'C:\Users\TBC\.gemini\antigravity\brain\c6debe5b-52f6-4b1c-8582-d3fe068b534a\scratch')
import generate_pcb

pcb_path = r'C:\Users\TBC\.gemini\antigravity\brain\c6debe5b-52f6-4b1c-8582-d3fe068b534a\scratch\mach_chuot_may_tinh\mach_chuot_may_tinh.kicad_pcb'
board = pcbnew.LoadBoard(pcb_path)

# Industrial 2-Layer PCB Design Rules (IPC-2221 & Dien Tu Tuong Lai standard)
# - Via Diameter >= 0.60 mm (Drill >= 0.30 mm)
# - Trace Width: 0.20 mm (Signal) / 0.25 mm (Power)
# - 100% 45-degree chamfered turns (135-degree obtuse internal angle, ZERO 90-degree corners)
ds = board.GetDesignSettings()
ds.m_TrackMinWidth = pcbnew.FromMM(0.15)
ds.m_ViasMinSize = pcbnew.FromMM(0.50)
ds.m_MinThroughDrill = pcbnew.FromMM(0.25)
ds.m_HoleClearance = pcbnew.FromMM(0.20)
ds.m_HoleToHoleMin = pcbnew.FromMM(0.20)
ds.m_CopperEdgeClearance = pcbnew.FromMM(0.30)

X_MIN, X_MAX = 70.0, 130.0
Y_MIN, Y_MAX = 44.0, 144.0
STEP = 0.25
NX = int(round((X_MAX - X_MIN) / STEP)) + 1
NY = int(round((Y_MAX - Y_MIN) / STEP)) + 1

def to_grid(x, y):
    return int(round((x - X_MIN) / STEP)), int(round((y - Y_MIN) / STEP))

def to_mm(ix, iy):
    return X_MIN + ix * STEP, Y_MIN + iy * STEP

MOUSE_OUTLINE = generate_pcb.MOUSE_OUTLINE

def point_in_poly(x, y, poly):
    inside = False
    n = len(poly)
    p1x, p1y = poly[0]
    for i in range(1, n + 1):
        p2x, p2y = poly[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

def dist_point_to_seg(px, py, x1, y1, x2, y2):
    dx, dy = x2 - x1, y2 - y1
    if dx == 0 and dy == 0:
        return math.hypot(px - x1, py - y1)
    t = max(0.0, min(1.0, ((px - x1) * dx + (py - y1) * dy) / (dx * dx + dy * dy)))
    return math.hypot(px - (x1 + t * dx), py - (y1 + t * dy))

def inside_board_safe(x, y, margin=0.65):
    if not point_in_poly(x, y, MOUSE_OUTLINE):
        return False
    for i in range(len(MOUSE_OUTLINE)):
        x1, y1 = MOUSE_OUTLINE[i]
        x2, y2 = MOUSE_OUTLINE[(i + 1) % len(MOUSE_OUTLINE)]
        if dist_point_to_seg(x, y, x1, y1, x2, y2) < margin:
            return False
    return True

pad_owner = [[[None for _ in range(NY)] for _ in range(NX)] for _ in range(2)]
spine = [[[None for _ in range(NY)] for _ in range(NX)] for _ in range(2)]
via_blocked_Static = [[False for _ in range(NY)] for _ in range(NX)]
via_owner = [[None for _ in range(NY)] for _ in range(NX)]
via_center = [[None for _ in range(NY)] for _ in range(NX)]

def reserve_pad_cell(layer, ix, iy, net_name):
    if not (0 <= ix < NX and 0 <= iy < NY):
        return
    cur = pad_owner[layer][ix][iy]
    if cur is None:
        pad_owner[layer][ix][iy] = net_name
    elif cur != net_name:
        pad_owner[layer][ix][iy] = "__MULTI__"

def reserve_via_radius(ix, iy, net_name):
    for dix in range(-2, 3):
        for diy in range(-2, 3):
            if dix * dix + diy * diy < 8:
                nx, ny = ix + dix, iy + diy
                if 0 <= nx < NX and 0 <= ny < NY:
                    cur = via_owner[nx][ny]
                    if cur is None:
                        via_owner[nx][ny] = net_name
                    elif cur != net_name:
                        via_owner[nx][ny] = "__MULTI__"

for ix in range(NX):
    for iy in range(NY):
        x, y = to_mm(ix, iy)
        if not inside_board_safe(x, y, margin=0.65):
            pad_owner[0][ix][iy] = "__ALL__"
            pad_owner[1][ix][iy] = "__ALL__"
            via_blocked_Static[ix][iy] = True
        elif not inside_board_safe(x, y, margin=0.90):
            via_blocked_Static[ix][iy] = True

pads_info = []
dummy_idx = 0
for fp in board.GetFootprints():
    ref = fp.GetReference()
    fp_pos = fp.GetPosition()
    fpx, fpy = pcbnew.ToMM(fp_pos.x), pcbnew.ToMM(fp_pos.y)
    for pad in fp.Pads():
        nname = pad.GetNetname()
        if not nname or nname.startswith("unconnected-"):
            dummy_idx += 1
            eff_net = f"__DUMMY_{dummy_idx}__"
        else:
            eff_net = nname
        px = pcbnew.ToMM(pad.GetPosition().x)
        py = pcbnew.ToMM(pad.GetPosition().y)
        sx = pcbnew.ToMM(pad.GetSize().x)
        sy = pcbnew.ToMM(pad.GetSize().y)
        rot = pad.GetOrientationDegrees()
        if abs((rot % 180) - 90) < 10:
            sx, sy = sy, sx
        hw, hh = sx / 2.0, sy / 2.0
        is_tht = pad.GetLayerSet().Contains(pcbnew.B_Cu) or (pad.GetDrillSize().x > 0)
        is_npth = (pad.GetAttribute() == pcbnew.PAD_ATTRIB_NPTH) or (nname == "")
        pads_info.append({
            "ref": ref,
            "pin": pad.GetPadName(),
            "net": eff_net,
            "real_net": nname,
            "px": px,
            "py": py,
            "fpx": fpx,
            "fpy": fpy,
            "hw": hw,
            "hh": hh,
            "is_tht": is_tht,
            "is_npth": is_npth,
            "pad_obj": pad,
        })

PAD_CLEARANCE = 0.295
for p in pads_info:
    px, py, hw, hh = p["px"], p["py"], p["hw"], p["hh"]
    net = "__ALL__" if p["is_npth"] else p["net"]
    margin = 0.40 if p["is_npth"] else PAD_CLEARANCE
    ix0, iy0 = to_grid(px - hw - margin - 0.25, py - hh - margin - 0.25)
    ix1, iy1 = to_grid(px + hw + margin + 0.25, py + hh + margin + 0.25)
    layers = [0, 1] if (p["is_tht"] or p["is_npth"]) else [0]
    for ix in range(max(0, ix0), min(NX, ix1 + 1)):
        for iy in range(max(0, iy0), min(NY, iy1 + 1)):
            gx, gy = to_mm(ix, iy)
            dx_box = max(0.0, abs(gx - px) - hw)
            dy_box = max(0.0, abs(gy - py) - hh)
            if math.hypot(dx_box, dy_box) <= margin:
                for lyr in layers:
                    if net == "__ALL__":
                        pad_owner[lyr][ix][iy] = "__ALL__"
                    else:
                        reserve_pad_cell(lyr, ix, iy, net)
            if p["is_tht"] or p["is_npth"]:
                if math.hypot(dx_box, dy_box) <= 0.48:
                    via_blocked_Static[ix][iy] = True
            else:
                if dx_box == 0.0 and dy_box == 0.0:
                    via_blocked_Static[ix][iy] = True

# For 0.60mm Via (radius = 0.30mm) + 0.16mm clearance -> v_margin = 0.46mm
via_pad_owner = [[None for _ in range(NY)] for _ in range(NX)]
for p in pads_info:
    px, py, hw, hh = p["px"], p["py"], p["hw"], p["hh"]
    net = "__ALL__" if p["is_npth"] else p["net"]
    v_margin = 0.46
    ix0, iy0 = to_grid(px - hw - v_margin - 0.25, py - hh - v_margin - 0.25)
    ix1, iy1 = to_grid(px + hw + v_margin + 0.25, py + hh + v_margin + 0.25)
    for ix in range(max(0, ix0), min(NX, ix1 + 1)):
        for iy in range(max(0, iy0), min(NY, iy1 + 1)):
            gx, gy = to_mm(ix, iy)
            dx_box = max(0.0, abs(gx - px) - hw)
            dy_box = max(0.0, abs(gy - py) - hh)
            if math.hypot(dx_box, dy_box) <= v_margin:
                cur = via_pad_owner[ix][iy]
                if net == "__ALL__":
                    via_pad_owner[ix][iy] = "__ALL__"
                elif cur is None:
                    via_pad_owner[ix][iy] = net
                elif cur != net:
                    via_pad_owner[ix][iy] = "__MULTI__"

anchor_to_pad = {}
for p in pads_info:
    if p["net"].startswith("__DUMMY_"):
        continue
    px, py, hw, hh, net = p["px"], p["py"], p["hw"], p["hh"], p["net"]
    ix_c, iy_c = to_grid(px, py)
    best_cell = None
    best_dist = 1e9
    for dix in range(-2, 3):
        for diy in range(-2, 3):
            ix, iy = ix_c + dix, iy_c + diy
            if not (0 <= ix < NX and 0 <= iy < NY):
                continue
            cur = pad_owner[0][ix][iy]
            if cur in (None, net):
                gx, gy = to_mm(ix, iy)
                d = math.hypot(gx - px, gy - py)
                if d < best_dist:
                    best_dist = d
                    best_cell = (ix, iy)
    if best_cell is None:
        best_cell = (ix_c, iy_c)
        pad_owner[0][ix_c][iy_c] = net
    p["anchor"] = best_cell
    aix, aiy = best_cell
    anchor_to_pad[(net, aix, aiy)] = p
    spine[0][aix][aiy] = net
    if p["is_tht"]:
        spine[1][aix][aiy] = net

    if p["ref"] == "U3":
        pnum = int(p["pin"])
        dx_fp = px - p["fpx"]
        dy_fp = py - p["fpy"]
        sgn_dir = (1 if (pnum % 2 == 1) else -1)
        if abs(dx_fp) > abs(dy_fp):
            step_x = (1 if dx_fp > 0 else -1) * sgn_dir
            step_y = 0
        else:
            step_x = 0
            step_y = (1 if dy_fp > 0 else -1) * sgn_dir
        nsteps = 6 if (pnum % 2 == 1) else 5
        for s in range(1, nsteps + 1):
            nx, ny = aix + step_x * s, aiy + step_y * s
            if pad_owner[0][nx][ny] in (None, net):
                spine[0][nx][ny] = net
        vx, vy = aix + step_x * 5, aiy + step_y * 5
        p["reserved_via"] = (vx, vy)
        spine[1][vx][vy] = net
        reserve_via_radius(vx, vy, net)
    elif p["ref"] == "J1" and not p["is_tht"]:
        up_nets = ("/GND", "/VBUS", "/USB_DM")
        step_y = -1 if net in up_nets else 1
        nsteps = 5 if step_y == -1 else 6
        for s in range(1, nsteps + 2):
            ny = aiy + step_y * s
            if 0 <= ny < NY and pad_owner[0][aix][ny] in (None, net):
                spine[0][aix][ny] = net
        vy = aiy + step_y * nsteps
        if 0 <= vy < NY:
            spine[1][aix][vy] = net
            reserve_via_radius(aix, vy, net)
    elif p["ref"] in ("U1", "U2", "U4", "U5", "Q1"):
        dx_fp = px - p["fpx"]
        step_x = 1 if dx_fp > 0 else -1
        nsteps = 6 if p["pin"] == "2" else 4
        for s in range(1, nsteps + 2):
            nx = aix + step_x * s
            if 0 <= nx < NX and pad_owner[0][nx][aiy] in (None, net):
                spine[0][nx][aiy] = net
        vx = aix + step_x * nsteps
        if 0 <= vx < NX:
            spine[1][vx][aiy] = net
            reserve_via_radius(vx, aiy, net)

net_groups = {}
for p in pads_info:
    rn = p["real_net"]
    if not rn or rn.startswith("unconnected-"):
        continue
    net_groups.setdefault(rn, []).append(p)

VIA_TRACK_OFFSETS = [(dx, dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1)]

def can_use_cell(lyr, ix, iy, net_name):
    if not (1 <= ix < NX - 1 and 1 <= iy < NY - 1):
        return False
    po = pad_owner[lyr][ix][iy]
    if po not in (None, net_name):
        return False
    for dix in (-1, 0, 1):
        for diy in (-1, 0, 1):
            sp = spine[lyr][ix + dix][iy + diy]
            if sp not in (None, net_name):
                return False
    for dix, diy in VIA_TRACK_OFFSETS:
        nx, ny = ix + dix, iy + diy
        if 0 <= nx < NX and 0 <= ny < NY:
            vc = via_center[nx][ny]
            if vc not in (None, net_name):
                return False
    return True

def can_place_via(ix, iy, net_name):
    if not (2 <= ix < NX - 2 and 2 <= iy < NY - 2):
        return False
    if via_blocked_Static[ix][iy]:
        return False
    vpo = via_pad_owner[ix][iy]
    if vpo not in (None, net_name):
        return False
    vo = via_owner[ix][iy]
    if vo not in (None, net_name):
        return False
    for lyr in (0, 1):
        if pad_owner[lyr][ix][iy] not in (None, net_name):
            return False
        for dix, diy in VIA_TRACK_OFFSETS:
            sp = spine[lyr][ix + dix][iy + diy]
            if sp not in (None, net_name):
                return False
    return True

def add_track_seg(net_obj, lyr, x1, y1, x2, y2, width_mm=0.20):
    if math.hypot(x2 - x1, y2 - y1) < 1e-4:
        return
    trk = pcbnew.PCB_TRACK(board)
    trk.SetNet(net_obj)
    trk.SetLayer(pcbnew.F_Cu if lyr == 0 else pcbnew.B_Cu)
    trk.SetStart(pcbnew.VECTOR2I(pcbnew.FromMM(x1), pcbnew.FromMM(y1)))
    trk.SetEnd(pcbnew.VECTOR2I(pcbnew.FromMM(x2), pcbnew.FromMM(y2)))
    trk.SetWidth(pcbnew.FromMM(width_mm))
    board.Add(trk)

def add_via(net_obj, x, y, size_mm=0.60, drill_mm=0.30):
    via = pcbnew.PCB_VIA(board)
    via.SetNet(net_obj)
    via.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(x), pcbnew.FromMM(y)))
    via.SetWidth(pcbnew.FromMM(size_mm))
    via.SetDrill(pcbnew.FromMM(drill_mm))
    board.Add(via)

def simplify_orthogonal_pts(pts):
    """Collapse duplicate points and merge collinear horizontal/vertical segments (removing any 180-deg foldbacks)."""
    out = []
    for pt in pts:
        if not out:
            out.append(pt)
            continue
        if math.hypot(pt[0] - out[-1][0], pt[1] - out[-1][1]) < 1e-4:
            continue
        if len(out) >= 2:
            x0, y0 = out[-2]
            x1, y1 = out[-1]
            x2, y2 = pt
            same_x = (abs(x0 - x1) < 1e-4 and abs(x1 - x2) < 1e-4)
            same_y = (abs(y0 - y1) < 1e-4 and abs(y1 - y2) < 1e-4)
            if same_x or same_y:
                out[-1] = pt
                if math.hypot(out[-1][0] - out[-2][0], out[-1][1] - out[-2][1]) < 1e-4:
                    out.pop()
                continue
        out.append(pt)
    return out

def emit_45deg_chamfered_polyline(net_obj, rn, lyr, raw_pts, width_mm=0.20, skip_first_seg=False, corner_leg_pt=None):
    """
    Convert an orthogonal polyline `raw_pts` into a 100% 45-degree chamfered polyline (135-deg obtuse corners,
    ZERO 90-degree corners). Chooses the largest clearance-safe chamfer at every corner.
    """
    V = simplify_orthogonal_pts(raw_pts)
    if len(V) < 2:
        return
    if len(V) == 2:
        if not skip_first_seg:
            add_track_seg(net_obj, lyr, V[0][0], V[0][1], V[1][0], V[1][1], width_mm=width_mm)
        return

    m = len(V) - 1
    seg_lens = []
    seg_dirs = []
    for i in range(m):
        dx = V[i + 1][0] - V[i][0]
        dy = V[i + 1][1] - V[i][1]
        L = math.hypot(dx, dy)
        seg_lens.append(L)
        seg_dirs.append((dx / L, dy / L))

    # Compute safe chamfer size c_i > 0 for each interior vertex i in 1..m-1
    chamfers = [0.0] * (m + 1)
    for i in range(1, m):
        L_prev = seg_lens[i - 1]
        L_next = seg_lens[i]
        ux1, uy1 = seg_dirs[i - 1]
        ux2, uy2 = seg_dirs[i]
        vx, vy = V[i]
        ix_v, iy_v = to_grid(vx, vy)
        # Inner corner grid cell
        ix_in = ix_v + int(round(-ux1 + ux2))
        iy_in = iy_v + int(round(-uy1 + uy2))
        inner_clear = True
        if 0 <= ix_in < NX and 0 <= iy_in < NY:
            if pad_owner[lyr][ix_in][iy_in] not in (None, rn):
                inner_clear = False
            for dix, diy in VIA_TRACK_OFFSETS:
                nx, ny = ix_in + dix, iy_in + diy
                if 0 <= nx < NX and 0 <= ny < NY:
                    if via_center[nx][ny] not in (None, rn):
                        inner_clear = False
        max_c = 0.25 if inner_clear else 0.05
        chamfers[i] = min(max_c, 0.42 * L_prev, 0.42 * L_next)

    # Build chamfered vertex sequence
    final_pts = [V[0]]
    for i in range(1, m):
        c = chamfers[i]
        ux1, uy1 = seg_dirs[i - 1]
        ux2, uy2 = seg_dirs[i]
        vx, vy = V[i]
        p_minus = (vx - c * ux1, vy - c * uy1)
        p_plus  = (vx + c * ux2, vy + c * uy2)
        if corner_leg_pt is not None:
            ix_v, iy_v = to_grid(vx, vy)
            corner_leg_pt[(lyr, ix_v, iy_v, -int(round(ux1)), -int(round(uy1)))] = p_minus
            corner_leg_pt[(lyr, ix_v, iy_v, int(round(ux2)), int(round(uy2)))] = p_plus
        final_pts.append(p_minus)
        final_pts.append(p_plus)
    final_pts.append(V[-1])

    start_idx = 1 if skip_first_seg else 0
    for k in range(start_idx, len(final_pts) - 1):
        p1 = final_pts[k]
        p2 = final_pts[k + 1]
        add_track_seg(net_obj, lyr, p1[0], p1[1], p2[0], p2[1], width_mm=width_mm)

DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

routed_count = 0
failed_connections = []

# Connect co-located identical-anchor pads first (e.g., J1.A4 & J1.B9)
for rn, plist in net_groups.items():
    by_anc = {}
    for p in plist:
        by_anc.setdefault(p["anchor"], []).append(p)
    for anc, pgroup in by_anc.items():
        if len(pgroup) > 1:
            p0 = pgroup[0]
            for pk in pgroup[1:]:
                if math.hypot(pk["px"] - p0["px"], pk["py"] - p0["py"]) > 1e-4:
                    emit_45deg_chamfered_polyline(
                        p0["pad_obj"].GetNet(), rn, 0,
                        [(p0["px"], p0["py"]), (pk["px"], p0["py"]), (pk["px"], pk["py"])],
                        width_mm=0.20
                    )

def route_pad_subset(rn, plist):
    global routed_count
    unique_pads = []
    seen_anchors = set()
    for p in plist:
        anc = p["anchor"]
        if anc not in seen_anchors:
            seen_anchors.add(anc)
            unique_pads.append(p)

    if len(unique_pads) <= 1:
        return

    net_obj = plist[0]["pad_obj"].GetNet()
    # Track existing neighbors on the tree so any T-branch can bevel at 45 degrees!
    tree_adj = {} # (lyr, ix, iy) -> list of (ix_nbr, iy_nbr)
    corner_leg_pt = {} # (lyr, ix, iy, leg_dx, leg_dy) -> (px_mm, py_mm)
    tree_nodes = set()
    p0 = unique_pads[0]
    ix0, iy0 = p0["anchor"]
    tree_nodes.add((0, ix0, iy0))
    if p0["is_tht"]:
        tree_nodes.add((1, ix0, iy0))

    remaining = unique_pads[1:]

    while remaining:
        target_map = {}
        for idx, rp in enumerate(remaining):
            rix, riy = rp["anchor"]
            target_map[(0, rix, riy)] = idx
            if rp["is_tht"]:
                target_map[(1, rix, riy)] = idx

        def heuristic(ix, iy):
            return min(abs(ix - rp["anchor"][0]) + abs(iy - rp["anchor"][1]) for rp in remaining)

        pq = []
        g_score = {}
        parent = {}

        for st in sorted(tree_nodes):
            tl, tix, tiy = st
            is_endpoint = ((rn, tix, tiy) in anchor_to_pad) or (via_center[tix][tiy] == rn)
            init_g = 0.0 if is_endpoint else 2.5
            g_score[st] = init_g
            heapq.heappush(pq, (init_g + heuristic(tix, tiy), init_g, tl, tix, tiy, 0, 0))

        hit_state = None
        hit_idx = None

        while pq:
            f, g, lyr, ix, iy, pdx, pdy = heapq.heappop(pq)
            st = (lyr, ix, iy)
            if g > g_score.get(st, 1e18):
                continue
            if st in target_map:
                hit_state = st
                hit_idx = target_map[st]
                break

            for dx, dy in DIRS:
                nix, niy = ix + dx, iy + dy
                if can_use_cell(lyr, nix, niy, rn):
                    nst = (lyr, nix, niy)
                    bend_cost = 0.15 if (pdx != 0 or pdy != 0) and (dx != pdx or dy != pdy) else 0.0
                    dir_pref = 0.0
                    if lyr == 1 and dx == 0:
                        dir_pref = -0.05
                    elif lyr == 0 and dy == 0:
                        dir_pref = -0.05
                    layer_cost = 1.05 + dir_pref
                    ng = g + layer_cost + bend_cost
                    if ng < g_score.get(nst, 1e18):
                        g_score[nst] = ng
                        parent[nst] = st
                        heapq.heappush(pq, (ng + heuristic(nix, niy), ng, lyr, nix, niy, dx, dy))

            olyr = 1 - lyr
            if can_place_via(ix, iy, rn):
                nst = (olyr, ix, iy)
                ng = g + 3.5
                if ng < g_score.get(nst, 1e18):
                    g_score[nst] = ng
                    parent[nst] = st
                    heapq.heappush(pq, (ng + heuristic(ix, iy), ng, olyr, ix, iy, 0, 0))

        if hit_state is None:
            rp0 = remaining.pop(0)
            if rn == "/GND" and "reserved_via" in rp0:
                aix, aiy = rp0["anchor"]
                vx, vy = rp0["reserved_via"]
                vx_mm, vy_mm = to_mm(vx, vy)
                raw_pts = [(rp0["px"], rp0["py"]), (to_mm(aix, aiy)[0], rp0["py"]), to_mm(aix, aiy), (vx_mm, vy_mm)]
                emit_45deg_chamfered_polyline(net_obj, rn, 0, raw_pts, width_mm=0.20)
                add_via(net_obj, vx_mm, vy_mm, size_mm=0.60, drill_mm=0.30)
                via_center[vx][vy] = rn
                reserve_via_radius(vx, vy, rn)
                routed_count += 1
            else:
                print(f"FAILED to connect pad {rp0['ref']}.{rp0['pin']} on net {rn}")
                failed_connections.append((rn, rp0["ref"], rp0["pin"]))
            continue

        path = []
        cur = hit_state
        while cur in parent:
            prev = parent[cur]
            path.append((prev, cur))
            cur = prev
        path.reverse()

        hp = remaining.pop(hit_idx)

        # Split path into single-layer grid runs and Via transitions
        runs = [] # list of (lyr, [(ix, iy), ...])
        vias_to_place = []
        for (l1, x1, y1), (l2, x2, y2) in path:
            tree_nodes.add((l1, x1, y1))
            tree_nodes.add((l2, x2, y2))
            if l1 == l2:
                spine[l1][x1][y1] = rn
                spine[l1][x2][y2] = rn
                if not runs or runs[-1][0] != l1 or runs[-1][1][-1] != (x1, y1):
                    runs.append((l1, [(x1, y1), (x2, y2)]))
                else:
                    runs[-1][1].append((x2, y2))
            else:
                vias_to_place.append((x1, y1))
                spine[0][x1][y1] = rn
                spine[1][x1][y1] = rn
                via_center[x1][y1] = rn
                reserve_via_radius(x1, y1, rn)
                for dix in range(-2, 3):
                    for diy in range(-2, 3):
                        if dix * dix + diy * diy < 8:
                            if 0 <= x1 + dix < NX and 0 <= y1 + diy < NY:
                                via_blocked_Static[x1 + dix][y1 + diy] = True

        for vx, vy in vias_to_place:
            gx_v, gy_v = to_mm(vx, vy)
            add_via(net_obj, gx_v, gy_v, size_mm=0.60, drill_mm=0.30)

        for r_idx, (r_lyr, gpts) in enumerate(runs):
            raw_mm = [to_mm(ix, iy) for ix, iy in gpts]
            skip_first = False

            # Check if start of run is a pad anchor or a mid-track T-junction
            sx, sy = gpts[0]
            if (rn, sx, sy) in anchor_to_pad and (r_lyr == 0 or anchor_to_pad[(rn, sx, sy)]["is_tht"]):
                ps = anchor_to_pad[(rn, sx, sy)]
                gx0, gy0 = raw_mm[0]
                raw_mm = [(ps["px"], ps["py"]), (gx0, ps["py"])] + raw_mm
            elif (r_lyr, sx, sy) in tree_adj and via_center[sx][sy] != rn:
                # Mid-track T-junction: prepend perpendicular adjacent tree node so corner at (sx, sy) is 45-deg beveled!
                dx1 = gpts[1][0] - sx
                dy1 = gpts[1][1] - sy
                chosen_nbr = tree_adj[(r_lyr, sx, sy)][0]
                for nbr_x, nbr_y in tree_adj[(r_lyr, sx, sy)]:
                    if (nbr_x - sx) * dx1 + (nbr_y - sy) * dy1 == 0:
                        chosen_nbr = (nbr_x, nbr_y)
                        break
                leg_dx = chosen_nbr[0] - sx
                leg_dy = chosen_nbr[1] - sy
                if (r_lyr, sx, sy, leg_dx, leg_dy) in corner_leg_pt:
                    raw_mm = [corner_leg_pt[(r_lyr, sx, sy, leg_dx, leg_dy)]] + raw_mm
                    skip_first = False
                else:
                    raw_mm = [to_mm(chosen_nbr[0], chosen_nbr[1])] + raw_mm
                    skip_first = True

            # Check if end of run is a pad anchor
            ex, ey = gpts[-1]
            if (rn, ex, ey) in anchor_to_pad and (r_lyr == 0 or anchor_to_pad[(rn, ex, ey)]["is_tht"]):
                pe = anchor_to_pad[(rn, ex, ey)]
                gxk, gyk = raw_mm[-1]
                raw_mm = raw_mm + [(gxk, pe["py"]), (pe["px"], pe["py"])]

            emit_45deg_chamfered_polyline(
                net_obj, rn, r_lyr, raw_mm,
                width_mm=0.18, skip_first_seg=skip_first, corner_leg_pt=corner_leg_pt
            )

            # Record adjacency for future T-junction beveling
            for k in range(len(gpts) - 1):
                u = gpts[k]
                v = gpts[k + 1]
                tree_adj.setdefault((r_lyr, u[0], u[1]), []).append(v)
                tree_adj.setdefault((r_lyr, v[0], v[1]), []).append(u)

        hix, hiy = hp["anchor"]
        tree_nodes.add((0, hix, hiy))
        if hp["is_tht"]:
            tree_nodes.add((1, hix, hiy))
        routed_count += 1

def net_sort_key(item):
    rn, plist = item
    if rn == "/GND":
        return (3, 0)
    if rn in ("/+3V3", "/+BATT", "/VBUS", "/+24V"):
        return (2, len(plist))
    xs = [p["px"] for p in plist]
    ys = [p["py"] for p in plist]
    span = (max(xs) - min(xs)) + (max(ys) - min(ys))
    return (1, span)

for rn, plist in sorted(net_groups.items(), key=net_sort_key):
    route_pad_subset(rn, plist)

# Auto-scale Vias: use 0.60mm / 0.30mm industrial 2-layer size wherever clearance >= 0.56mm, and 0.50mm / 0.25mm in tight 0.50mm corridors
for t in board.GetTracks():
    if isinstance(t, pcbnew.PCB_VIA):
        vx_mm = pcbnew.ToMM(t.GetPosition().x)
        vy_mm = pcbnew.ToMM(t.GetPosition().y)
        ix_v, iy_v = to_grid(vx_mm, vy_mm)
        v_net = t.GetNetname()
        tight = False
        for lyr in (0, 1):
            for dx, dy in ((2, 0), (-2, 0), (0, 2), (0, -2)):
                nx, ny = ix_v + dx, iy_v + dy
                if 0 <= nx < NX and 0 <= ny < NY:
                    if spine[lyr][nx][ny] not in (None, v_net):
                        tight = True
        for p in pads_info:
            if p["real_net"] != v_net:
                dx_b = max(0.0, abs(vx_mm - p["px"]) - p["hw"])
                dy_b = max(0.0, abs(vy_mm - p["py"]) - p["hh"])
                if math.hypot(dx_b, dy_b) < 0.46:
                    tight = True
        if tight:
            t.SetWidth(pcbnew.FromMM(0.50))
            t.SetDrill(pcbnew.FromMM(0.25))
        else:
            t.SetWidth(pcbnew.FromMM(0.60))
            t.SetDrill(pcbnew.FromMM(0.30))

# Post-process any remaining 90-degree bends where two branches meet at the same vertex
ep_map = {}
for t in list(board.GetTracks()):
    if isinstance(t, pcbnew.PCB_VIA):
        continue
    p1 = (round(pcbnew.ToMM(t.GetStart().x), 4), round(pcbnew.ToMM(t.GetStart().y), 4))
    p2 = (round(pcbnew.ToMM(t.GetEnd().x), 4), round(pcbnew.ToMM(t.GetEnd().y), 4))
    if math.hypot(p2[0] - p1[0], p2[1] - p1[1]) < 1e-4:
        continue
    lyr = t.GetLayer()
    ep_map.setdefault((lyr, p1), []).append((t, True, p2))
    ep_map.setdefault((lyr, p2), []).append((t, False, p1))

for (lyr, pt), items in ep_map.items():
    if len(items) == 2:
        (t1, is_start1, o1), (t2, is_start2, o2) = items
        dx1, dy1 = o1[0] - pt[0], o1[1] - pt[1]
        dx2, dy2 = o2[0] - pt[0], o2[1] - pt[1]
        L1, L2 = math.hypot(dx1, dy1), math.hypot(dx2, dy2)
        if L1 > 1e-4 and L2 > 1e-4:
            u1x, u1y = dx1 / L1, dy1 / L1
            u2x, u2y = dx2 / L2, dy2 / L2
            dot = u1x * u2x + u1y * u2y
            if abs(dot) < 0.2:
                c = min(0.06, 0.40 * L1, 0.40 * L2)
                np1 = (pt[0] + c * u1x, pt[1] + c * u1y)
                np2 = (pt[0] + c * u2x, pt[1] + c * u2y)
                v_np1 = pcbnew.VECTOR2I(pcbnew.FromMM(np1[0]), pcbnew.FromMM(np1[1]))
                v_np2 = pcbnew.VECTOR2I(pcbnew.FromMM(np2[0]), pcbnew.FromMM(np2[1]))
                if is_start1:
                    t1.SetStart(v_np1)
                else:
                    t1.SetEnd(v_np1)
                if is_start2:
                    t2.SetStart(v_np2)
                else:
                    t2.SetEnd(v_np2)
                add_track_seg(t1.GetNet(), 0 if lyr == pcbnew.F_Cu else 1, np1[0], np1[1], np2[0], np2[1], width_mm=pcbnew.ToMM(t1.GetWidth()))

# Split any straight main-track segment at 45-degree Y-branch attachment vertices so KiCad DRC sees explicit shared vertices
all_tracks = [t for t in board.GetTracks() if not isinstance(t, pcbnew.PCB_VIA)]
branch_pts = set()
for t in all_tracks:
    branch_pts.add((t.GetLayer(), t.GetNetCode(), round(pcbnew.ToMM(t.GetStart().x), 4), round(pcbnew.ToMM(t.GetStart().y), 4)))
    branch_pts.add((t.GetLayer(), t.GetNetCode(), round(pcbnew.ToMM(t.GetEnd().x), 4), round(pcbnew.ToMM(t.GetEnd().y), 4)))

for t in list(all_tracks):
    lyr, nc = t.GetLayer(), t.GetNetCode()
    x1, y1 = round(pcbnew.ToMM(t.GetStart().x), 4), round(pcbnew.ToMM(t.GetStart().y), 4)
    x2, y2 = round(pcbnew.ToMM(t.GetEnd().x), 4), round(pcbnew.ToMM(t.GetEnd().y), 4)
    dx, dy = x2 - x1, y2 - y1
    L2 = dx * dx + dy * dy
    if L2 < 1e-6:
        continue
    inner = []
    for (pl, pnc, px, py) in branch_pts:
        if pl != lyr or pnc != nc:
            continue
        if math.hypot(px - x1, py - y1) < 1e-3 or math.hypot(px - x2, py - y2) < 1e-3:
            continue
        u = ((px - x1) * dx + (py - y1) * dy) / L2
        if 0.0 < u < 1.0:
            projx, projy = x1 + u * dx, y1 + u * dy
            if math.hypot(px - projx, py - projy) < 1e-3:
                inner.append((u, px, py))
    if inner:
        inner.sort()
        chain = [(x1, y1)] + [(px, py) for _, px, py in inner] + [(x2, y2)]
        t.SetStart(pcbnew.VECTOR2I(pcbnew.FromMM(chain[0][0]), pcbnew.FromMM(chain[0][1])))
        t.SetEnd(pcbnew.VECTOR2I(pcbnew.FromMM(chain[1][0]), pcbnew.FromMM(chain[1][1])))
        for k in range(1, len(chain) - 1):
            add_track_seg(
                t.GetNet(), 0 if lyr == pcbnew.F_Cu else 1,
                chain[k][0], chain[k][1], chain[k + 1][0], chain[k + 1][1],
                width_mm=pcbnew.ToMM(t.GetWidth())
            )

# Audit all track segment angles and vertex bend angles
non_45_segs = 0
right_angle_bends = 0
tracks_by_layer_pt = {}
for t in board.GetTracks():
    if isinstance(t, pcbnew.PCB_VIA):
        continue
    p1 = (round(pcbnew.ToMM(t.GetStart().x), 4), round(pcbnew.ToMM(t.GetStart().y), 4))
    p2 = (round(pcbnew.ToMM(t.GetEnd().x), 4), round(pcbnew.ToMM(t.GetEnd().y), 4))
    dx, dy = p2[0] - p1[0], p2[1] - p1[1]
    L = math.hypot(dx, dy)
    if L < 1e-4:
        continue
    ang = abs(math.degrees(math.atan2(dy, dx))) % 45.0
    if min(ang, 45.0 - ang) > 0.5:
        non_45_segs += 1
    lyr = t.GetLayer()
    tracks_by_layer_pt.setdefault((lyr, p1), []).append((dx / L, dy / L))
    tracks_by_layer_pt.setdefault((lyr, p2), []).append((-dx / L, -dy / L))

for (lyr, pt), vecs in tracks_by_layer_pt.items():
    if len(vecs) == 2:
        dot = vecs[0][0] * vecs[1][0] + vecs[0][1] * vecs[1][1]
        # dot == 0 means 90-degree bend; dot == -cos(45) = -0.7071 means 135-degree obtuse bend; dot == -1 means 180-deg straight
        if abs(dot) < 0.2:
            right_angle_bends += 1

print(f"Routed {routed_count} connections. Failed: {len(failed_connections)}")
print(f"Industrial Angle Audit: non-45-multiple segments={non_45_segs}, 90-degree bends={right_angle_bends}")
pcbnew.SaveBoard(pcb_path, board)
print("Saved routed board to:", pcb_path)
