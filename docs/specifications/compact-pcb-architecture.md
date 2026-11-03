# Kiến Trúc Thiết Kế Bo Mạch PCB Siêu Thu Nhỏ (Compact SMD Hardware Architecture)

Tài liệu này hướng dẫn cách thiết kế một bo mạch PCB tùy biến (Custom PCB) kích thước siêu nhỏ, tích hợp toàn bộ tính năng của chuột không dây và bộ tạo vi dòng điện mà không cần dùng các module phát triển cồng kềnh ngoài thị trường.

---

## 1. Kiến Trúc Phân Tầng Bo Mạch (2-Board Stacking)

Để tận dụng tối đa thể tích bên trong vỏ chuột công thái học, hệ thống phần cứng được chia làm 2 tầng:

```text
[ Vỏ trên: 2 Điện cực tiếp xúc (Thép 316L / Silicone dẫn điện) ]
             │ (Tiếp xúc bằng Pogo Pins mạ vàng)
             ▼
[ Top Board (Daughterboard) ]: Microswitch Click Trái/Phải, Con lăn (Encoder)
             │ (Cáp dẹt FPC / JST SH 1.0mm)
             ▼
[ Main Board (Bo mạch đáy) ]: Mắt đọc PAW3395, MCU nRF52840, Khối Boost 24V,
                              Khối Nguồn dòng Op-Amp + Cầu H, Mạch sạc Type-C & BMS
```

- **Kết nối điện cực bằng chân Pogo Pin:** Trên bo mạch hàn 2 chân lò xo mạ vàng hướng lên trên. Khi úp vỏ chuột lại, 2 chân Pogo Pin tự động tì chặt vào mặt sau của điện cực kim loại trên vỏ chuột mà không cần hàn dây điện thủ công.

---

## 2. Lựa Chọn Vi Điều Khiển (SoC Chip Rời)

Không dùng board cắm dây (Dev Kit). Sử dụng trực tiếp chip IC dán bề mặt (SMD):

### nRF52840 (Nordic Semiconductor) — Lựa chọn hàng đầu
- **Đóng gói:** QFN73 ($7 \times 7\,\text{mm}$) hoặc WLCSP ($3.5 \times 3.6\,\text{mm}$).
- **Nhân xử lý:** ARM Cortex-M4 32-bit @ 64 MHz, 1 MB Flash, 256 KB RAM.
- **Tích hợp phần cứng:**
  - Native USB 2.0 Full Speed (12 Mbps).
  - 2.4 GHz Transceiver hỗ trợ Bluetooth 5.3 Low Energy (BLE) và chế độ không dây độc quyền 2.4GHz độ trễ 1ms.
  - Bộ chuyển đổi ADC 12-bit (8 kênh) để đo đạc trở kháng da.
  - Các khối PWM phần cứng điều chế xung vi dòng không tiêu tốn tài nguyên CPU.

---

## 3. Thiết Kế Khối Nâng Áp Siêu Nhỏ (Micro Boost Converter 24V)

Thay vì module MT3608 to tướng ($36 \times 17\,\text{mm}$), cụm Boost được thiết kế bằng IC chuyên dụng cho thiết bị đeo y tế:

- **IC điều khiển:** **TPS61040DBVR** (Texas Instruments) đóng gói **SOT-23-5** ($2.9 \times 1.6\,\text{mm}$).
- **Điện áp vào:** $3.0\text{V} - 4.2\text{V}$ (từ pin sạc Li-Po).
- **Điện áp ra:** Cố định ở $24\text{V}$ (điều chỉnh qua cầu phân áp $R_1, R_2$).
- **Cuộn cảm SMD:** Chuẩn kích thước 2520 ($2.5 \times 2.0 \times 1.2\,\text{mm}$), giá trị $10\,\mu\text{H}$, dòng bão hòa $I_{\text{sat}} = 350\,\text{mA}$.
- **Diode Schottky:** **BAT54W** hoặc **MBR0540** (gói SOD-123).
- **Tụ lọc đầu ra:** Tụ gốm MLCC 0805 $1\,\mu\text{F} / 50\text{V}$.
- **Diện tích chiếm dụng trên PCB:** **$\approx 6 \times 8\,\text{mm}$**.

---

## 4. Khối Tạo Nguồn Dòng & Cầu H Đảo Cực (Howland Pump + H-Bridge)

### 4.1. Nguồn dòng không đổi (Constant Current Generator)
- **IC khuếch đại thuật toán (Op-Amp):** **OPA2333** hoặc **MCP6002** (gói siêu nhỏ DFN-8 $2 \times 2\,\text{mm}$ hoặc MSOP-8).
- **Nguyên lý:** Mạch Howland Current Pump hoặc mạch Op-Amp hồi tiếp âm qua cảm biến dòng điện shunt ($R_{\text{sense}} = 1\,\text{k}\Omega$).
- **Điều khiển biên độ:** MCU xuất điện áp analog qua DAC (hoặc PWM lọc thông thấp qua mạch RC) vào chân tham chiếu của Op-Amp để điều chỉnh dòng ra từ $50\,\mu\text{A}$ đến $400\,\mu\text{A}$.

### 4.2. Cầu H đảo chiều xung 2 pha (Biphasic H-Bridge)
- **IC chuyển mạch:** **Dual Complementary MOSFET** (tích hợp 2 kênh N và 2 kênh P trong 1 chip duy nhất, ví dụ **DMC3028LSD** hoặc **FDMC8015**) đóng gói SO-8 hoặc DFN ($3 \times 3\,\text{mm}$).
- **Điều khiển:** 2 chân GPIO của MCU kích hoạt luân phiên cặp chéo để đảo chiều dòng điện qua da tay với tần số $10\,\text{Hz} - 100\,\text{Hz}$, triệt tiêu 100% thành phần một chiều (Zero DC).

---

## 5. Bảng Dự Toán Không Gian Linh Kiện Trên Main PCB

| Khối chức năng | Kích thước dự kiến | Linh kiện chính |
| :--- | :--- | :--- |
| **SoC MCU & Mạch RF Antenna** | $10 \times 10\,\text{mm}$ | nRF52840, Thạch anh 32MHz, Ceramic Antenna |
| **Mắt đọc quang học** | $15 \times 15\,\text{mm}$ | PixArt PAW3395 + Thấu kính |
| **Khối Nguồn Boost 24V** | $6 \times 8\,\text{mm}$ | TPS61040, Cuộn cảm 2520, Diode MBR0540 |
| **Khối Tạo Vi Dòng & Cầu H** | $10 \times 12\,\text{mm}$ | OPA2333, Dual MOSFET DMC3028LSD |
| **Mạch Sạc Pin & Type-C** | $8 \times 10\,\text{mm}$ | BQ24040, Cổng USB Type-C 16-pin chân SMD |
| **Tổng diện tích cụm vi dòng** | **$\approx 2\,\text{cm}^2$** | Hoàn toàn nằm gọn ở một góc bo mạch chuột. |