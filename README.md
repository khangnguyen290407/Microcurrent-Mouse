# Dự Án: Chuột Máy Tính Tích Hợp Vi Dòng Điện (Microcurrent Mouse)

## 1. Giới thiệu tổng quan
Dự án phát triển một thiết bị ngoại vi máy tính (chuột công thái học - Ergonomic Mouse) tích hợp công nghệ **vi dòng điện (Microcurrent Therapy - MENS)** nhằm mục tiêu:
- **Tăng tuần hoàn máu & kích thích sản sinh ATP:** Giúp phục hồi mô, giảm căng cứng cơ bàn tay và cổ tay khi làm việc văn phòng liên tục.
- **Giảm nguy cơ hội chứng ống cổ tay (Carpal Tunnel Syndrome):** Hỗ trợ xoa dịu các bó cơ và dây thần kinh vùng bàn tay.
- **Nâng cao khả năng tập trung:** Nghiên cứu cơ chế kích thích thần kinh nhẹ nhàng (tương tự vi kích thích Cranial/Peripheral) kết hợp các chu kỳ làm việc (như Pomodoro).

---

## 2. Cấu trúc thư mục dự án

```text
microcurrent-mouse/
├── docs/                      # Tài liệu nghiên cứu, pháp lý và đặc tả kỹ thuật
│   ├── current-conduction-principles/ # Nguyên lý truyền dẫn dòng điện trong mô & giải phẫu học
│   │   ├── current-path-and-tissue-penetration.md  # Phân tích đường đi dòng điện, độ sâu & vị trí điện cực
│   │   ├── local-vs-systemic-effects.md            # Đánh giá tác dụng cục bộ bàn tay vs. toàn thân
│   │   └── skin-impedance-and-efficacy.md          # Cơ chế sinh học tăng ATP & mô hình trở kháng da
│   ├── research/              # Tài liệu y sinh, cơ chế vi dòng điện, tác động ATP
│   │   ├── core-keywords.md   # Từ khóa trọng tâm (DOMS, Sub-sensory, Lipolysis, Muscle Thickness)
│   │   ├── hand-nerve-anatomy-and-mouse-correlation.md # Giải phẫu 3 dây thần kinh tay & ứng dụng vào chuột
│   │   └── PMC9941239-summary.md # Tóm tắt bài báo nghiên cứu nền tảng (Eur J Appl Physiol 2023)
│   ├── safety-standards/      # Tiêu chuẩn an toàn điện sinh học (IEC 60601-1, ngưỡng vi dòng)
│   └── specifications/        # Thông số kỹ thuật của thiết bị (Specs)
├── hardware/                  # Thiết kế phần cứng & điện tử
│   ├── schematics/            # Sơ đồ mạch nguyên lý (KiCad / Proteus / EasyEDA)
│   ├── pcb/                   # Bản vẽ mạch in & Gerber files
│   ├── bom/                   # Bảng danh mục linh kiện & chi phí (BOM)
│   └── datasheets/            # Datasheet các linh kiện chính (MCU, Op-Amp, DAC,...)
├── mechanical-cad/            # Thiết kế cơ khí & vỏ ngoài (3D Modeling)
│   ├── 3d-models/             # File CAD (.step, .stl, file gốc Fusion360/SolidWorks)
│   ├── electrodes/            # Thiết kế & vị trí các điện cực tiếp xúc da
│   └── renders/               # Hình ảnh 3D mô phỏng
├── firmware/                  # Lập trình nhúng cho vi điều khiển
│   ├── src/                   # Source code C/C++ điều khiển xung, đọc cảm biến, USB/BLE HID
│   ├── include/               # Header files
│   └── tests/                 # Code test phần cứng, hiệu chuẩn dòng điện
├── software/                  # Phần mềm ứng dụng đi kèm (Desktop / Web Companion)
│   └── companion-app/         # Ứng dụng điều chỉnh thông số, hẹn giờ, theo dõi sức khỏe
├── tests-and-logs/            # Kết quả đo kiểm & nhật ký thử nghiệm
│   ├── oscilloscope-captures/ # Ảnh chụp dạng sóng thực tế trên dao động ký
│   └── test-reports/          # Báo cáo đo kiểm tải giả & thử nghiệm thực tế
└── assets/                    # Hình ảnh, sơ đồ minh họa
```

---

## 3. Các giai đoạn phát triển (Roadmap)

### Giai đoạn 1: Nghiên cứu khả thi & An toàn (Feasibility & Safety)
- [ ] Xác định dải dòng điện an toàn ($10\,\mu\text{A} - 500\,\mu\text{A}$) và dải tần số kích thích ($0.5\,\text{Hz} - 100\,\text{Hz}$).
- [ ] Chọn dạng sóng: Xung vuông 2 pha đối xứng (Biphasic Square Wave) nhằm triệt tiêu thành phần DC, tránh ăn mòn điện phân hoặc kích ứng da.
- [ ] Chọn vật liệu điện cực tiếp xúc (Thép không gỉ 316L, Silicone dẫn điện hoặc Mạ vàng y tế).

### Giai đoạn 2: Thiết kế mạch tạo dòng (Proof-of-Concept Hardware)
- [ ] Thiết kế mạch nguồn dòng không đổi (Constant Current Source) điều khiển bằng DAC/PWM (ví dụ mạch Howland Current Pump hoặc mạch Op-Amp + BJT).
- [ ] Tích hợp bảo vệ phần cứng: Giới hạn dòng điện tối đa tuyệt đối (Hardware Current Limiter) ở mức an toàn tối đa $< 1\,\text{mA}$.
- [ ] Đo kiểm dạng sóng trên tải trở tương đương trở kháng da người ($500\,\Omega - 10\,\text{k}\Omega$).

### Giai đoạn 3: Tích hợp cơ khí & Thiết kế vỏ chuột
- [ ] Chọn phom dáng chuột công thái học (chuột đứng Vertical hoặc chuột Ergonomic ôm lòng bàn tay).
- [ ] Bố trí 2 cực tiếp xúc (Anode / Cathode): Một cực ở lòng bàn tay, một cực ở cạnh ngón cái hoặc vị trí tiếp xúc tự nhiên.
- [ ] In thử nghiệm mẫu 3D prototype đầu tiên.

### Giai đoạn 4: Firmware & Tính năng thông minh
- [ ] Phát hiện có người cầm chuột (Capacitive Touch hoặc trở kháng tiếp xúc) mới kích hoạt xung điện.
- [ ] Chế độ tự ngắt: Kích thích theo chu kỳ (ví dụ: 15-20 phút hoạt động, nghỉ 40 phút).
- [ ] Kết nối chuột: Chuột quang HID chuẩn qua USB/Bluetooth song song với mạch vi dòng.
