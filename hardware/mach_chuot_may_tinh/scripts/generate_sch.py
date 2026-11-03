import os, re, uuid, json

sym_root = r'C:\Program Files\KiCad\10.0\share\kicad\symbols'
out_dir = r'C:\Users\TBC\.gemini\antigravity\brain\c6debe5b-52f6-4b1c-8582-d3fe068b534a\scratch\mach_chuot_may_tinh'
os.makedirs(out_dir, exist_ok=True)

PROJECT_NAME = "mach_chuot_may_tinh"
ROOT_UUID = str(uuid.uuid5(uuid.NAMESPACE_DNS, "mach_chuot_may_tinh_root_sch"))

def det_uuid(seed):
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, f"mcm_{seed}"))

def load_symbol_def(lib_name, sym_file_name, target_lib_id):
    p = os.path.join(sym_root, f"{lib_name}.kicad_symdir", f"{sym_file_name}.kicad_sym")
    txt = open(p, encoding="utf-8").read()
    lines = txt.strip().splitlines()
    start_idx = None
    for i, l in enumerate(lines):
        if l.startswith('\t(symbol "'):
            start_idx = i
            break
    inner_lines = lines[start_idx:-1]
    old_name = re.search(r'^\t\(symbol\s+"([^"]+)"', inner_lines[0]).group(1)
    inner_lines[0] = f'\t\t(symbol "{target_lib_id}"'
    body = "\n".join(inner_lines)
    short_new = target_lib_id.split(":")[-1]
    body = re.sub(r'\(symbol\s+"' + re.escape(old_name) + r'_(\d+_\d+)"', f'(symbol "{short_new}_\\1"', body)
    indented = "\n".join("\t" + l if not l.startswith("\t\t(symbol \"" + target_lib_id) else l for l in body.splitlines())
    return indented, body

CUSTOM_PAW3395_INNER = """\t(symbol "PAW3395_Optical"
\t\t(pin_names
\t\t\t(offset 1.016)
\t\t)
\t\t(exclude_from_sim no)
\t\t(in_bom yes)
\t\t(on_board yes)
\t\t(in_pos_files yes)
\t\t(duplicate_pin_numbers_are_jumpers no)
\t\t(property "Reference" "U"
\t\t\t(at -7.62 11.43 0)
\t\t\t(show_name no)
\t\t\t(do_not_autoplace no)
\t\t\t(effects
\t\t\t\t(font
\t\t\t\t\t(size 1.27 1.27)
\t\t\t\t)
\t\t\t\t(justify left)
\t\t\t)
\t\t)
\t\t(property "Value" "PAW3395_Optical"
\t\t\t(at -7.62 -11.43 0)
\t\t\t(show_name no)
\t\t\t(do_not_autoplace no)
\t\t\t(effects
\t\t\t\t(font
\t\t\t\t\t(size 1.27 1.27)
\t\t\t\t)
\t\t\t\t(justify left)
\t\t\t)
\t\t)
\t\t(property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm"
\t\t\t(at 0 0 0)
\t\t\t(show_name no)
\t\t\t(do_not_autoplace no)
\t\t\t(hide yes)
\t\t\t(effects
\t\t\t\t(font
\t\t\t\t\t(size 1.27 1.27)
\t\t\t\t)
\t\t\t)
\t\t)
\t\t(property "Datasheet" ""
\t\t\t(at 0 0 0)
\t\t\t(show_name no)
\t\t\t(do_not_autoplace no)
\t\t\t(hide yes)
\t\t\t(effects
\t\t\t\t(font
\t\t\t\t\t(size 1.27 1.27)
\t\t\t\t)
\t\t\t)
\t\t)
\t\t(property "Description" "PixArt PAW3395 Optical Mouse Sensor SPI"
\t\t\t(at 0 0 0)
\t\t\t(show_name no)
\t\t\t(do_not_autoplace no)
\t\t\t(hide yes)
\t\t\t(effects
\t\t\t\t(font
\t\t\t\t\t(size 1.27 1.27)
\t\t\t\t)
\t\t\t)
\t\t)
\t\t(symbol "PAW3395_Optical_0_1"
\t\t\t(rectangle
\t\t\t\t(start -10.16 10.16)
\t\t\t\t(end 10.16 -10.16)
\t\t\t\t(stroke
\t\t\t\t\t(width 0.254)
\t\t\t\t\t(type default)
\t\t\t\t)
\t\t\t\t(fill
\t\t\t\t\t(type background)
\t\t\t\t)
\t\t\t)
\t\t)
\t\t(symbol "PAW3395_Optical_1_1"
\t\t\t(pin power_in line
\t\t\t\t(at -12.7 7.62 0)
\t\t\t\t(length 2.54)
\t\t\t\t(name "VDD"
\t\t\t\t\t(effects
\t\t\t\t\t\t(font
\t\t\t\t\t\t\t(size 1.27 1.27)
\t\t\t\t\t\t)
\t\t\t\t\t)
\t\t\t\t)
\t\t\t\t(number "1"
\t\t\t\t\t(effects
\t\t\t\t\t\t(font
\t\t\t\t\t\t\t(size 1.27 1.27)
\t\t\t\t\t\t)
\t\t\t\t\t)
\t\t\t\t)
\t\t\t)
\t\t\t(pin power_in line
\t\t\t\t(at -12.7 -7.62 0)
\t\t\t\t(length 2.54)
\t\t\t\t(name "GND"
\t\t\t\t\t(effects
\t\t\t\t\t\t(font
\t\t\t\t\t\t\t(size 1.27 1.27)
\t\t\t\t\t\t)
\t\t\t\t\t)
\t\t\t\t)
\t\t\t\t(number "2"
\t\t\t\t\t(effects
\t\t\t\t\t\t(font
\t\t\t\t\t\t\t(size 1.27 1.27)
\t\t\t\t\t\t)
\t\t\t\t\t)
\t\t\t\t)
\t\t\t)
\t\t\t(pin input line
\t\t\t\t(at 12.7 7.62 180)
\t\t\t\t(length 2.54)
\t\t\t\t(name "SCLK"
\t\t\t\t\t(effects
\t\t\t\t\t\t(font
\t\t\t\t\t\t\t(size 1.27 1.27)
\t\t\t\t\t\t)
\t\t\t\t\t)
\t\t\t\t)
\t\t\t\t(number "3"
\t\t\t\t\t(effects
\t\t\t\t\t\t(font
\t\t\t\t\t\t\t(size 1.27 1.27)
\t\t\t\t\t\t)
\t\t\t\t\t)
\t\t\t\t)
\t\t\t)
\t\t\t(pin input line
\t\t\t\t(at 12.7 2.54 180)
\t\t\t\t(length 2.54)
\t\t\t\t(name "MOSI"
\t\t\t\t\t(effects
\t\t\t\t\t\t(font
\t\t\t\t\t\t\t(size 1.27 1.27)
\t\t\t\t\t\t)
\t\t\t\t\t)
\t\t\t\t)
\t\t\t\t(number "4"
\t\t\t\t\t(effects
\t\t\t\t\t\t(font
\t\t\t\t\t\t\t(size 1.27 1.27)
\t\t\t\t\t\t)
\t\t\t\t\t)
\t\t\t\t)
\t\t\t)
\t\t\t(pin output line
\t\t\t\t(at 12.7 -2.54 180)
\t\t\t\t(length 2.54)
\t\t\t\t(name "MISO"
\t\t\t\t\t(effects
\t\t\t\t\t\t(font
\t\t\t\t\t\t\t(size 1.27 1.27)
\t\t\t\t\t\t)
\t\t\t\t\t)
\t\t\t\t)
\t\t\t\t(number "5"
\t\t\t\t\t(effects
\t\t\t\t\t\t(font
\t\t\t\t\t\t\t(size 1.27 1.27)
\t\t\t\t\t\t)
\t\t\t\t\t)
\t\t\t\t)
\t\t\t)
\t\t\t(pin input line
\t\t\t\t(at 12.7 -7.62 180)
\t\t\t\t(length 2.54)
\t\t\t\t(name "NCS"
\t\t\t\t\t(effects
\t\t\t\t\t\t(font
\t\t\t\t\t\t\t(size 1.27 1.27)
\t\t\t\t\t\t)
\t\t\t\t\t)
\t\t\t\t)
\t\t\t\t(number "6"
\t\t\t\t\t(effects
\t\t\t\t\t\t(font
\t\t\t\t\t\t\t(size 1.27 1.27)
\t\t\t\t\t\t)
\t\t\t\t\t)
\t\t\t\t)
\t\t\t)
\t\t\t(pin output line
\t\t\t\t(at -12.7 2.54 0)
\t\t\t\t(length 2.54)
\t\t\t\t(name "MOTION"
\t\t\t\t\t(effects
\t\t\t\t\t\t(font
\t\t\t\t\t\t\t(size 1.27 1.27)
\t\t\t\t\t\t)
\t\t\t\t\t)
\t\t\t\t)
\t\t\t\t(number "7"
\t\t\t\t\t(effects
\t\t\t\t\t\t(font
\t\t\t\t\t\t\t(size 1.27 1.27)
\t\t\t\t\t\t)
\t\t\t\t\t)
\t\t\t\t)
\t\t\t)
\t\t\t(pin input line
\t\t\t\t(at -12.7 -2.54 0)
\t\t\t\t(length 2.54)
\t\t\t\t(name "NRESET"
\t\t\t\t\t(effects
\t\t\t\t\t\t(font
\t\t\t\t\t\t\t(size 1.27 1.27)
\t\t\t\t\t\t)
\t\t\t\t\t)
\t\t\t\t)
\t\t\t\t(number "8"
\t\t\t\t\t(effects
\t\t\t\t\t\t(font
\t\t\t\t\t\t\t(size 1.27 1.27)
\t\t\t\t\t\t)
\t\t\t\t\t)
\t\t\t\t)
\t\t\t)
\t\t)
\t\t(embedded_fonts no)
\t)"""

# Save local custom symbol library and sym-lib-table so ERC finds Mouse_Custom:PAW3395_Optical
custom_lib_path = os.path.join(out_dir, "Mouse_Custom.kicad_sym")
with open(custom_lib_path, "w", encoding="utf-8") as f:
    f.write(f'(kicad_symbol_lib\n\t(version 20251024)\n\t(generator "kicad_symbol_editor")\n\t(generator_version "10.0")\n{CUSTOM_PAW3395_INNER}\n)\n')

sym_lib_table_path = os.path.join(out_dir, "sym-lib-table")
with open(sym_lib_table_path, "w", encoding="utf-8") as f:
    f.write('(sym_lib_table\n  (version 7)\n  (lib (name "Mouse_Custom")(type "KiCad")(uri "${KIPRJMOD}/Mouse_Custom.kicad_sym")(options "")(descr "Custom Mouse Symbols"))\n)\n')

CUSTOM_PAW3395_SCH = "\n".join(
    '\t\t(symbol "Mouse_Custom:PAW3395_Optical"' if i == 0 else "\t" + l
    for i, l in enumerate(CUSTOM_PAW3395_INNER.splitlines())
)

LIB_MAP = [
    ("Device", "R", "Device:R"),
    ("Device", "C", "Device:C"),
    ("Device", "L", "Device:L"),
    ("Device", "LED", "Device:LED"),
    ("Device", "Polyfuse", "Device:Polyfuse"),
    ("Device", "D_Schottky", "Device:D_Schottky"),
    ("Device", "RotaryEncoder_Switch_MP", "Device:RotaryEncoder_Switch_MP"),
    ("Switch", "SW_Push", "Switch:SW_Push"),
    ("Connector", "USB_C_Receptacle_USB2.0_16P", "Connector:USB_C_Receptacle_USB2.0_16P"),
    ("Connector_Generic", "Conn_01x02", "Connector_Generic:Conn_01x02"),
    ("Connector_Generic", "Conn_01x04", "Connector_Generic:Conn_01x04"),
    ("Battery_Management", "MCP73831-2-OT", "Battery_Management:MCP73831-2-OT"),
    ("Regulator_Linear", "AP2204K-1.5", "Regulator_Linear:AP2204K-1.5"),
    ("Regulator_Switching", "LMR10510XMF", "Regulator_Switching:LMR10510XMF"),
    ("Amplifier_Operational", "MCP6L91T-EOT", "Amplifier_Operational:MCP6L91T-EOT"),
    ("Transistor_BJT", "Q_NPN_BEC", "Transistor_BJT:Q_NPN_BEC"),
    ("MCU_ST_STM32F1", "STM32F103C_8-B_Tx", "MCU_ST_STM32F1:STM32F103C_8-B_Tx"),
    ("power", "PWR_FLAG", "power:PWR_FLAG"),
]

lib_symbols_strs = []
pin_table = {}

for lib_name, sym_file, target_id in LIB_MAP:
    indented, raw_body = load_symbol_def(lib_name, sym_file, target_id)
    lib_symbols_strs.append(indented)
    pins = re.findall(
        r'\(pin\s+\w+\s+\w+\s+\(at\s+([-\d\.]+)\s+([-\d\.]+)\s+([-\d\.]+)\).*?\(name\s+"([^"]*)".*?\(number\s+"([^"]*)"',
        raw_body, re.S
    )
    pin_table[target_id] = [(num, nm, float(x), float(y), int(float(a))) for x, y, a, nm, num in pins]

lib_symbols_strs.append(CUSTOM_PAW3395_SCH)
pins_paw = re.findall(
    r'\(pin\s+\w+\s+\w+\s+\(at\s+([-\d\.]+)\s+([-\d\.]+)\s+([-\d\.]+)\).*?\(name\s+"([^"]*)".*?\(number\s+"([^"]*)"',
    CUSTOM_PAW3395_SCH, re.S
)
pin_table["Mouse_Custom:PAW3395_Optical"] = [(num, nm, float(x), float(y), int(float(a))) for x, y, a, nm, num in pins_paw]

# Define all components on the A3 sheet (420 x 297 mm) with generous spacing and custom label offsets
COMPONENTS = [
    # --- BLOCK 1: USB-C, LIPO CHARGER & 3.3V LDO (Top-Left: X=20..155, Y=25..140) ---
    {
        "ref": "J1", "lib_id": "Connector:USB_C_Receptacle_USB2.0_16P", "val": "USB_C_2.0",
        "fp": "Connector_USB:USB_C_Receptacle_HRO_TYPE-C-31-M-12", "at": (43.18, 66.04),
        "ref_off": (-7.62, -21.59), "val_off": (-7.62, -19.05),
        "nets": {
            "A1": "GND", "A12": "GND", "B1": "GND", "B12": "GND", "SH": "GND",
            "A4": "VBUS", "A9": "VBUS", "B4": "VBUS", "B9": "VBUS",
            "A5": "USB_CC1", "B5": "USB_CC2",
            "A6": "USB_DP", "B6": "USB_DP",
            "A7": "USB_DM", "B7": "USB_DM",
            "A8": None, "B8": None,
        }
    },
    {
        "ref": "R1", "lib_id": "Device:R", "val": "5.1k",
        "fp": "Resistor_SMD:R_0603_1608Metric", "at": (83.82, 55.88),
        "nets": {"1": "USB_CC1", "2": "GND"}
    },
    {
        "ref": "R2", "lib_id": "Device:R", "val": "5.1k",
        "fp": "Resistor_SMD:R_0603_1608Metric", "at": (101.60, 55.88),
        "nets": {"1": "USB_CC2", "2": "GND"}
    },
    {
        "ref": "J2", "lib_id": "Connector_Generic:Conn_01x02", "val": "LiPo_3.7V_400mAh",
        "fp": "Connector_JST:JST_PH_B2B-PH-K_1x02_P2.00mm_Vertical", "at": (132.08, 55.88),
        "ref_off": (-2.54, -6.35), "val_off": (-2.54, -3.81),
        "nets": {"1": "+BATT", "2": "GND"}
    },
    {
        "ref": "U1", "lib_id": "Battery_Management:MCP73831-2-OT", "val": "MCP73831_LiPo_Chg",
        "fp": "Package_TO_SOT_SMD:SOT-23-5", "at": (53.34, 114.30),
        "ref_off": (-7.62, -10.16), "val_off": (-7.62, -7.62),
        "nets": {"4": "VBUS", "2": "GND", "3": "+BATT", "5": "CHG_PROG", "1": "CHG_STAT"}
    },
    {
        "ref": "R3", "lib_id": "Device:R", "val": "2k_500mA",
        "fp": "Resistor_SMD:R_0603_1608Metric", "at": (27.94, 114.30),
        "nets": {"1": "CHG_PROG", "2": "GND"}
    },
    {
        "ref": "D1", "lib_id": "Device:LED", "val": "CHG_LED",
        "fp": "LED_SMD:LED_0603_1608Metric", "at": (81.28, 101.60),
        "ref_off": (-2.54, -5.08), "val_off": (-2.54, -2.54),
        "nets": {"2": "VBUS", "1": "CHG_LED_K"}
    },
    {
        "ref": "R4", "lib_id": "Device:R", "val": "1k",
        "fp": "Resistor_SMD:R_0603_1608Metric", "at": (81.28, 121.92),
        "nets": {"1": "CHG_LED_K", "2": "CHG_STAT"}
    },
    {
        "ref": "C1", "lib_id": "Device:C", "val": "4.7uF",
        "fp": "Capacitor_SMD:C_0603_1608Metric", "at": (99.06, 114.30),
        "nets": {"1": "+BATT", "2": "GND"}
    },
    {
        "ref": "U2", "lib_id": "Regulator_Linear:AP2204K-1.5", "val": "AP2112K-3.3_LDO",
        "fp": "Package_TO_SOT_SMD:SOT-23-5", "at": (121.92, 114.30),
        "ref_off": (-5.08, -10.16), "val_off": (-5.08, -7.62),
        "nets": {"1": "+BATT", "3": "+BATT", "2": "GND", "4": None, "5": "+3V3"}
    },
    {
        "ref": "C2", "lib_id": "Device:C", "val": "10uF",
        "fp": "Capacitor_SMD:C_0603_1608Metric", "at": (144.78, 114.30),
        "nets": {"1": "+3V3", "2": "GND"}
    },

    # --- BLOCK 2: STM32F103C8T6 MCU CORE & DEBUG (Center: X=160..274, Y=25..162) ---
    {
        "ref": "U3", "lib_id": "MCU_ST_STM32F1:STM32F103C_8-B_Tx", "val": "STM32F103C8T6",
        "fp": "Package_QFP:LQFP-48_7x7mm_P0.5mm", "at": (210.82, 99.06),
        "ref_off": (-15.24, -49.53), "val_off": (-15.24, -46.99),
        "nets": {
            "1": "+3V3", "9": "+3V3", "24": "+3V3", "36": "+3V3", "48": "+3V3",
            "8": "GND", "23": "GND", "35": "GND", "47": "GND",
            "7": "NRST", "44": "GND",
            "2": "STATUS_LED",
            "10": "ADC_SKIN",
            "11": "ISENSE_FB",
            "13": "OPT_MOTION",
            "14": "SPI_CS",
            "15": "SPI_SCK",
            "16": "SPI_MISO",
            "17": "SPI_MOSI",
            "18": "BOOST_EN",
            "25": "HBRIDGE_PHA",
            "26": "HBRIDGE_PHB",
            "29": "PWM_DAC",
            "32": "USB_DM",
            "33": "USB_DP",
            "34": "SWDIO",
            "37": "SWCLK",
            "39": "BTN_LEFT",
            "40": "BTN_RIGHT",
            "41": "BTN_MIDDLE",
            "42": "BTN_MENS_MODE",
            "45": "ENC_A",
            "46": "ENC_B",
        }
    },
    {
        "ref": "C3", "lib_id": "Device:C", "val": "100nF",
        "fp": "Capacitor_SMD:C_0603_1608Metric", "at": (167.64, 48.26),
        "nets": {"1": "+3V3", "2": "GND"}
    },
    {
        "ref": "C4", "lib_id": "Device:C", "val": "100nF",
        "fp": "Capacitor_SMD:C_0603_1608Metric", "at": (182.88, 48.26),
        "nets": {"1": "+3V3", "2": "GND"}
    },
    {
        "ref": "R15", "lib_id": "Device:R", "val": "1.5k_USB_PU",
        "fp": "Resistor_SMD:R_0603_1608Metric", "at": (251.46, 48.26),
        "nets": {"1": "+3V3", "2": "USB_DP"}
    },
    {
        "ref": "R16", "lib_id": "Device:R", "val": "10k_NRST",
        "fp": "Resistor_SMD:R_0603_1608Metric", "at": (167.64, 144.78),
        "nets": {"1": "+3V3", "2": "NRST"}
    },
    {
        "ref": "J5", "lib_id": "Connector_Generic:Conn_01x04", "val": "SWD_Header",
        "fp": "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical", "at": (256.54, 142.24),
        "ref_off": (-2.54, -7.62), "val_off": (-2.54, -5.08),
        "nets": {"1": "+3V3", "2": "SWDIO", "3": "SWCLK", "4": "GND"}
    },
    {
        "ref": "D3", "lib_id": "Device:LED", "val": "MENS_LED",
        "fp": "LED_SMD:LED_0603_1608Metric", "at": (261.62, 73.66),
        "ref_off": (-2.54, -5.08), "val_off": (-2.54, -2.54),
        "nets": {"2": "+3V3", "1": "MENS_LED_K"}
    },
    {
        "ref": "R14", "lib_id": "Device:R", "val": "1k",
        "fp": "Resistor_SMD:R_0603_1608Metric", "at": (261.62, 91.44),
        "nets": {"1": "MENS_LED_K", "2": "STATUS_LED"}
    },

    # --- BLOCK 3: OPTICAL SENSOR PAW3395 & MOUSE SWITCHES (Bottom-Left: X=20..165, Y=167..274) ---
    {
        "ref": "U6", "lib_id": "Mouse_Custom:PAW3395_Optical", "val": "PAW3395_Optical_Sensor",
        "fp": "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm", "at": (58.42, 205.74),
        "ref_off": (-10.16, -15.24), "val_off": (-10.16, -12.70),
        "nets": {
            "1": "+3V3", "2": "GND", "3": "SPI_SCK", "4": "SPI_MOSI",
            "5": "SPI_MISO", "6": "SPI_CS", "7": "OPT_MOTION", "8": "+3V3"
        }
    },
    {
        "ref": "C5", "lib_id": "Device:C", "val": "100nF",
        "fp": "Capacitor_SMD:C_0603_1608Metric", "at": (33.02, 243.84),
        "nets": {"1": "+3V3", "2": "GND"}
    },
    {
        "ref": "SW1", "lib_id": "Switch:SW_Push", "val": "LEFT_CLICK",
        "fp": "Button_Switch_THT:SW_PUSH_6mm", "at": (109.22, 190.50),
        "ref_off": (-5.08, -6.35), "val_off": (-5.08, -3.81),
        "nets": {"1": "BTN_LEFT", "2": "GND"}
    },
    {
        "ref": "SW2", "lib_id": "Switch:SW_Push", "val": "RIGHT_CLICK",
        "fp": "Button_Switch_THT:SW_PUSH_6mm", "at": (109.22, 215.90),
        "ref_off": (-5.08, -6.35), "val_off": (-5.08, -3.81),
        "nets": {"1": "BTN_RIGHT", "2": "GND"}
    },
    {
        "ref": "SW3", "lib_id": "Switch:SW_Push", "val": "MENS_MODE_BTN",
        "fp": "Button_Switch_THT:SW_PUSH_6mm", "at": (109.22, 241.30),
        "ref_off": (-5.08, -6.35), "val_off": (-5.08, -3.81),
        "nets": {"1": "BTN_MENS_MODE", "2": "GND"}
    },
    {
        "ref": "SW4", "lib_id": "Device:RotaryEncoder_Switch_MP", "val": "SCROLL_WHEEL_ENC",
        "fp": "Rotary_Encoder:RotaryEncoder_Alps_EC11E-Switch_Vertical_H20mm", "at": (147.32, 205.74),
        "ref_off": (-5.08, -10.16), "val_off": (-5.08, -7.62),
        "nets": {"A": "ENC_A", "B": "ENC_B", "C": "GND", "S1": "BTN_MIDDLE", "S2": "GND", "MP": "GND"}
    },

    # --- BLOCK 4: 24V MICRO-BOOST CONVERTER (Top-Right: X=279..403, Y=25..116) ---
    {
        "ref": "U4", "lib_id": "Regulator_Switching:LMR10510XMF", "val": "TPS61040DBVR_24V",
        "fp": "Package_TO_SOT_SMD:SOT-23-5", "at": (307.34, 68.58),
        "ref_off": (-5.08, -10.16), "val_off": (-5.08, -7.62),
        "nets": {"5": "+BATT", "4": "BOOST_EN", "2": "GND", "1": "BOOST_SW", "3": "BOOST_FB"}
    },
    {
        "ref": "L1", "lib_id": "Device:L", "val": "10uH_SMD",
        "fp": "Inductor_SMD:L_0805_2012Metric", "at": (335.28, 48.26),
        "nets": {"1": "+BATT", "2": "BOOST_SW"}
    },
    {
        "ref": "D2", "lib_id": "Device:D_Schottky", "val": "MBR0540_40V",
        "fp": "Diode_SMD:D_SOD-123", "at": (360.68, 48.26),
        "ref_off": (-2.54, -5.08), "val_off": (-2.54, -2.54),
        "nets": {"2": "BOOST_SW", "1": "+24V"}
    },
    {
        "ref": "R5", "lib_id": "Device:R", "val": "180k_1%",
        "fp": "Resistor_SMD:R_0603_1608Metric", "at": (342.90, 81.28),
        "nets": {"1": "+24V", "2": "BOOST_FB"}
    },
    {
        "ref": "R6", "lib_id": "Device:R", "val": "10k_1%",
        "fp": "Resistor_SMD:R_0603_1608Metric", "at": (363.22, 81.28),
        "nets": {"1": "BOOST_FB", "2": "GND"}
    },
    {
        "ref": "C6", "lib_id": "Device:C", "val": "1uF_50V",
        "fp": "Capacitor_SMD:C_0805_2012Metric", "at": (383.54, 81.28),
        "nets": {"1": "+24V", "2": "GND"}
    },

    # --- BLOCK 5: CONSTANT CURRENT SOURCE 50-400uA (Middle-Right: X=279..403, Y=121..198) ---
    {
        "ref": "R7", "lib_id": "Device:R", "val": "10k_DAC_LPF",
        "fp": "Resistor_SMD:R_0603_1608Metric", "at": (289.56, 154.94),
        "ref_off": (-3.81, -8.89), "val_off": (-3.81, -6.35),
        "nets": {"1": "PWM_DAC", "2": "V_DAC_REF"}
    },
    {
        "ref": "C7", "lib_id": "Device:C", "val": "100nF_LPF",
        "fp": "Capacitor_SMD:C_0603_1608Metric", "at": (307.34, 154.94),
        "ref_off": (-3.81, -8.89), "val_off": (-3.81, -6.35),
        "nets": {"1": "V_DAC_REF", "2": "GND"}
    },
    {
        "ref": "U5", "lib_id": "Amplifier_Operational:MCP6L91T-EOT", "val": "OPA333_CCS_Ctrl",
        "fp": "Package_TO_SOT_SMD:SOT-23-5", "at": (337.82, 154.94),
        "ref_off": (-5.08, -11.43), "val_off": (-5.08, -8.89),
        "nets": {"5": "+3V3", "2": "GND", "3": "V_DAC_REF", "4": "ISENSE_FB", "1": "OPAMP_OUT"}
    },
    {
        "ref": "R9", "lib_id": "Device:R", "val": "1k",
        "fp": "Resistor_SMD:R_0603_1608Metric", "at": (360.68, 154.94),
        "nets": {"1": "OPAMP_OUT", "2": "Q1_BASE"}
    },
    {
        "ref": "Q1", "lib_id": "Transistor_BJT:Q_NPN_BEC", "val": "BC847_CCS",
        "fp": "Package_TO_SOT_SMD:SOT-23", "at": (381.00, 154.94),
        "ref_off": (-2.54, -8.89), "val_off": (-2.54, -6.35),
        "nets": {"1": "Q1_BASE", "2": "ISENSE_FB", "3": "I_STIM_SINK"}
    },
    {
        "ref": "R8", "lib_id": "Device:R", "val": "8.2k_Rsense",
        "fp": "Resistor_SMD:R_0603_1608Metric", "at": (396.24, 154.94),
        "ref_off": (-3.81, -8.89), "val_off": (-3.81, -6.35),
        "nets": {"1": "ISENSE_FB", "2": "GND"}
    },

    # --- BLOCK 6: BIPHASIC ELECTRODE STAGE, SAFETY CLAMP & SKIN SENSING (Bottom-Right: X=175..403, Y=203..274) ---
    {
        "ref": "F1", "lib_id": "Device:Polyfuse", "val": "PTC_50mA_Safety",
        "fp": "Fuse:Fuse_0805_2012Metric", "at": (193.04, 233.68),
        "nets": {"1": "+24V", "2": "HV_SAFE"}
    },
    {
        "ref": "R10", "lib_id": "Device:R", "val": "39k_HW_Limit",
        "fp": "Resistor_SMD:R_0603_1608Metric", "at": (215.90, 233.68),
        "nets": {"1": "HV_SAFE", "2": "STIM_POS_RAW"}
    },
    {
        "ref": "R11", "lib_id": "Device:R", "val": "10k_PhaseA",
        "fp": "Resistor_SMD:R_0603_1608Metric", "at": (238.76, 233.68),
        "nets": {"1": "HBRIDGE_PHA", "2": "STIM_POS_RAW"}
    },
    {
        "ref": "R12", "lib_id": "Device:R", "val": "100k_Skin_Sense",
        "fp": "Resistor_SMD:R_0603_1608Metric", "at": (261.62, 233.68),
        "nets": {"1": "STIM_POS_RAW", "2": "ADC_SKIN"}
    },
    {
        "ref": "R13", "lib_id": "Device:R", "val": "15k_Skin_Sense",
        "fp": "Resistor_SMD:R_0603_1608Metric", "at": (284.48, 233.68),
        "nets": {"1": "ADC_SKIN", "2": "GND"}
    },
    {
        "ref": "C8", "lib_id": "Device:C", "val": "1uF_50V_ZeroDC",
        "fp": "Capacitor_SMD:C_0805_2012Metric", "at": (307.34, 233.68),
        "nets": {"1": "STIM_POS_RAW", "2": "ELEC_PALM_OUT"}
    },
    {
        "ref": "R17", "lib_id": "Device:R", "val": "10k_PhaseB",
        "fp": "Resistor_SMD:R_0603_1608Metric", "at": (330.20, 233.68),
        "nets": {"1": "HBRIDGE_PHB", "2": "I_STIM_SINK"}
    },
    {
        "ref": "J3", "lib_id": "Connector_Generic:Conn_01x02", "val": "PALM_ELECTRODE_POGO",
        "fp": "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical", "at": (365.76, 226.06),
        "ref_off": (-2.54, -6.35), "val_off": (-2.54, -3.81),
        "nets": {"1": "ELEC_PALM_OUT", "2": "ELEC_PALM_OUT"}
    },
    {
        "ref": "J4", "lib_id": "Connector_Generic:Conn_01x02", "val": "THUMB_ELECTRODE_POGO",
        "fp": "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical", "at": (365.76, 251.46),
        "ref_off": (-2.54, -6.35), "val_off": (-2.54, -3.81),
        "nets": {"1": "I_STIM_SINK", "2": "I_STIM_SINK"}
    },

    # --- PWR_FLAG SYMBOLS FOR ERC POWER RAIL DRIVING ---
    {
        "ref": "#FLG01", "lib_id": "power:PWR_FLAG", "val": "PWR_FLAG",
        "fp": "", "at": (30.48, 86.36), "is_power": True,
        "nets": {"1": "VBUS"}
    },
    {
        "ref": "#FLG02", "lib_id": "power:PWR_FLAG", "val": "PWR_FLAG",
        "fp": "", "at": (30.48, 96.52), "is_power": True,
        "nets": {"1": "GND"}
    },
]

sym_instances = []
wires = []
labels = []
no_connects = []
graphics = []

BLOCKS = [
    (20.32, 25.40, 154.94, 142.24, "KHOI 1: NGUON USB-C, SAC PIN LIPO & LDO 3.3V (POWER MANAGEMENT)"),
    (160.02, 25.40, 274.32, 162.56, "KHOI 2: VI DIEU KHIEN STM32F103C8T6 & GIAO TIEP USB/SWD"),
    (20.32, 167.64, 167.64, 274.32, "KHOI 3: CAM BIEN QUANG PAW3395, NUT CLICK & CON LAN CHUOT"),
    (279.40, 25.40, 403.86, 116.84, "KHOI 4: MACH NANG AP SIEU NHO 24V (MICRO-BOOST CONVERTER)"),
    (279.40, 121.92, 403.86, 198.12, "KHOI 5: NGUON DONG VI DONG DIEN KHONG DOI 50-400uA (CCS)"),
    (175.26, 203.20, 403.86, 274.32, "KHOI 6: DAO CUC BIPHASIC, BAO VE AN TOAN & DIEN CUC POGO"),
]

for idx, (x1, y1, x2, y2, title) in enumerate(BLOCKS):
    graphics.append(f"""\t(rectangle
\t\t(start {x1:.2f} {y1:.2f})
\t\t(end {x2:.2f} {y2:.2f})
\t\t(stroke
\t\t\t(width 0.254)
\t\t\t(type dash)
\t\t\t(color 0 100 180 1)
\t\t)
\t\t(fill
\t\t\t(type none)
\t\t)
\t\t(uuid "{det_uuid(f'rect_{idx}')}")
\t)""")
    graphics.append(f"""\t(text "{title}"
\t\t(exclude_from_sim no)
\t\t(at {x1 + 2.54:.2f} {y1 + 5.08:.2f} 0)
\t\t(effects
\t\t\t(font
\t\t\t\t(size 1.778 1.778)
\t\t\t\t(bold yes)
\t\t\t)
\t\t\t(justify left bottom)
\t\t)
\t\t(uuid "{det_uuid(f'title_{idx}')}")
\t)""")

for comp in COMPONENTS:
    ref = comp["ref"]
    lib_id = comp["lib_id"]
    val = comp["val"]
    fp = comp["fp"]
    sx, sy = comp["at"]
    is_pwr = comp.get("is_power", False)
    comp_uuid = det_uuid(f"comp_{ref}")
    pins_info = pin_table[lib_id]

    pin_entries = []
    seen_coords = set()

    for pnum, pname, px, py, pang in pins_info:
        p_uuid = det_uuid(f"pin_{ref}_{pnum}")
        pin_entries.append(f'\t\t(pin "{pnum}"\n\t\t\t(uuid "{p_uuid}")\n\t\t)')

        x_sheet = round(sx + px, 2)
        y_sheet = round(sy - py, 2)
        coord_key = (x_sheet, y_sheet)
        if coord_key in seen_coords:
            continue
        seen_coords.add(coord_key)

        net_name = comp["nets"].get(pnum, None)
        if net_name is None:
            nc_uuid = det_uuid(f"nc_{ref}_{pnum}")
            no_connects.append(f'\t(no_connect\n\t\t(at {x_sheet:.2f} {y_sheet:.2f})\n\t\t(uuid "{nc_uuid}")\n\t)')
        else:
            if pang == 0:
                x_end, y_end = round(x_sheet - 5.08, 2), y_sheet
                lbl_ang, just = 180, "right bottom"
            elif pang == 180:
                x_end, y_end = round(x_sheet + 5.08, 2), y_sheet
                lbl_ang, just = 0, "left bottom"
            elif pang == 270:
                x_end, y_end = x_sheet, round(y_sheet - 3.81, 2)
                lbl_ang, just = 90, "left bottom"
            else:
                x_end, y_end = x_sheet, round(y_sheet + 3.81, 2)
                lbl_ang, just = 270, "right bottom"

            w_uuid = det_uuid(f"wire_{ref}_{pnum}")
            wires.append(f"""\t(wire
\t\t(pts
\t\t\t(xy {x_sheet:.2f} {y_sheet:.2f}) (xy {x_end:.2f} {y_end:.2f})
\t\t)
\t\t(stroke
\t\t\t(width 0)
\t\t\t(type default)
\t\t)
\t\t(uuid "{w_uuid}")
\t)""")
            l_uuid = det_uuid(f"lbl_{ref}_{pnum}")
            labels.append(f"""\t(label "{net_name}"
\t\t(at {x_end:.2f} {y_end:.2f} {lbl_ang})
\t\t(effects
\t\t\t(font
\t\t\t\t(size 1.143 1.143)
\t\t\t)
\t\t\t(justify {just})
\t\t)
\t\t(uuid "{l_uuid}")
\t)""")

    rx_off, ry_off = comp.get("ref_off", (1.905, -1.27))
    vx_off, vy_off = comp.get("val_off", (1.905, 1.27))
    ref_hide = "\n\t\t\t(hide yes)" if is_pwr else ""
    val_hide = "\n\t\t\t(hide yes)" if is_pwr else ""

    pins_block = "\n".join(pin_entries)
    sym_instances.append(f"""\t(symbol
\t\t(lib_id "{lib_id}")
\t\t(at {sx:.2f} {sy:.2f} 0)
\t\t(unit 1)
\t\t(body_style 1)
\t\t(exclude_from_sim no)
\t\t(in_bom {"no" if is_pwr else "yes"})
\t\t(on_board {"no" if is_pwr else "yes"})
\t\t(in_pos_files {"no" if is_pwr else "yes"})
\t\t(dnp no)
\t\t(fields_autoplaced yes)
\t\t(uuid "{comp_uuid}")
\t\t(property "Reference" "{ref}"
\t\t\t(at {sx + rx_off:.2f} {sy + ry_off:.2f} 0){ref_hide}
\t\t\t(show_name no)
\t\t\t(do_not_autoplace yes)
\t\t\t(effects
\t\t\t\t(font
\t\t\t\t\t(size 1.143 1.143)
\t\t\t\t\t(bold yes)
\t\t\t\t)
\t\t\t\t(justify left)
\t\t\t)
\t\t)
\t\t(property "Value" "{val}"
\t\t\t(at {sx + vx_off:.2f} {sy + vy_off:.2f} 0){val_hide}
\t\t\t(show_name no)
\t\t\t(do_not_autoplace yes)
\t\t\t(effects
\t\t\t\t(font
\t\t\t\t\t(size 1.016 1.016)
\t\t\t\t)
\t\t\t\t(justify left)
\t\t\t)
\t\t)
\t\t(property "Footprint" "{fp}"
\t\t\t(at {sx:.2f} {sy:.2f} 0)
\t\t\t(hide yes)
\t\t\t(show_name no)
\t\t\t(do_not_autoplace no)
\t\t\t(effects
\t\t\t\t(font
\t\t\t\t\t(size 1.27 1.27)
\t\t\t\t)
\t\t\t)
\t\t)
\t\t(property "Datasheet" ""
\t\t\t(at {sx:.2f} {sy:.2f} 0)
\t\t\t(hide yes)
\t\t\t(show_name no)
\t\t\t(do_not_autoplace no)
\t\t\t(effects
\t\t\t\t(font
\t\t\t\t\t(size 1.27 1.27)
\t\t\t\t)
\t\t\t)
\t\t)
\t\t(property "Description" ""
\t\t\t(at {sx:.2f} {sy:.2f} 0)
\t\t\t(hide yes)
\t\t\t(show_name no)
\t\t\t(do_not_autoplace no)
\t\t\t(effects
\t\t\t\t(font
\t\t\t\t\t(size 1.27 1.27)
\t\t\t\t)
\t\t\t)
\t\t)
{pins_block}
\t\t(instances
\t\t\t(project "{PROJECT_NAME}"
\t\t\t\t(path "/{ROOT_UUID}"
\t\t\t\t\t(reference "{ref}")
\t\t\t\t\t(unit 1)
\t\t\t\t)
\t\t\t)
\t\t)
\t)""")

sch_content = f"""(kicad_sch
\t(version 20260306)
\t(generator "eeschema")
\t(generator_version "10.0")
\t(uuid "{ROOT_UUID}")
\t(paper "A3")
\t(title_block
\t\t(title "MACH CHUOT MAY TINH TICH HOP VI DONG DIEN (MICROCURRENT ERGONOMIC MOUSE)")
\t\t(date "2026-11-03")
\t\t(rev "v1.0")
\t\t(company "Nguyen Doan Duy Khang - Biomedical & Embedded Hardware Project")
\t\t(comment 1 "MCU: STM32F103C8T6 | Optical: PAW3395 | Boost: TPS61040 (24V) | CCS: OPA333 (50-400uA)")
\t\t(comment 2 "Safety: Zero DC Offset (1uF Blocking Cap) + 50mA Polyfuse + 39k Hardware Current Limiter")
\t)
\t(lib_symbols
{chr(10).join(lib_symbols_strs)}
\t)
{chr(10).join(graphics)}
{chr(10).join(wires)}
{chr(10).join(labels)}
{chr(10).join(no_connects)}
{chr(10).join(sym_instances)}
\t(sheet_instances
\t\t(path "/"
\t\t\t(page "1")
\t\t)
\t)
\t(embedded_fonts no)
)
"""

sch_path = os.path.join(out_dir, f"{PROJECT_NAME}.kicad_sch")
with open(sch_path, "w", encoding="utf-8") as f:
    f.write(sch_content)

pro_template = json.load(open(r"G:\kicad\khang\khang.kicad_pro", encoding="utf-8"))
pro_template["meta"]["filename"] = f"{PROJECT_NAME}.kicad_pro"
if "net_settings" in pro_template and "classes" in pro_template["net_settings"]:
    for cls in pro_template["net_settings"]["classes"]:
        cls["clearance"] = 0.15
        cls["track_width"] = 0.20
        cls["via_diameter"] = 0.60
        cls["via_drill"] = 0.30
if "board" in pro_template and "design_settings" in pro_template["board"]:
    rules = pro_template["board"]["design_settings"]["rules"]
    rules["min_track_width"] = 0.15
    rules["min_via_diameter"] = 0.50
    rules["min_through_hole_diameter"] = 0.25
    rules["min_hole_clearance"] = 0.20
    rules["min_hole_to_hole"] = 0.20
    rules["min_text_height"] = 0.80
    rules["min_text_thickness"] = 0.15
pro_path = os.path.join(out_dir, f"{PROJECT_NAME}.kicad_pro")
with open(pro_path, "w", encoding="utf-8") as f:
    json.dump(pro_template, f, indent=2)

print("Updated schematic and project.")
