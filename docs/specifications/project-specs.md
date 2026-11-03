# Đặc Tả Kỹ Thuật Dự Kiến (Project Specifications)

## 1. Thông số điện sinh học (Microcurrent Subsystem)
- **Cường độ dòng ra:** $50\,\mu\text{A} - 400\,\mu\text{A}$ (có thể tinh chỉnh qua phần mềm).
- **Điện áp nguồn kích thích:** Tối đa $\approx 24\text{V} - 30\text{V}$ (nguồn nâng áp nội bộ dòng siêu nhỏ) để đảm bảo duy trì vi dòng qua điện trở da khô.
- **Tần số xung (Frequency):** $0.5\,\text{Hz} - 100\,\text{Hz}$.
  - $0.5\,\text{Hz} - 3\,\text{Hz}$: Thư giãn sâu, hỗ trợ giảm căng cứng cơ.
  - $10\,\text{Hz} - 40\,\text{Hz}$: Tăng tuần hoàn vi mạch, hỗ trợ giảm mỏi.
- **Dạng sóng:** Biphasic square pulse (xung vuông 2 pha đối xứng).
- **Chu kỳ kích thích:** 15 phút kích thích, nghỉ 45 phút (chu kỳ thông minh bảo vệ da).

## 2. Phần cứng chuột máy tính (Mouse Core)
- **Cảm biến quang học:** PixArt PAW3395 / PMW3360 hoặc tương đương.
- **Vi điều khiển chính (MCU):** ESP32-S3 / nRF52840 (Bluetooth BLE + 2.4GHz + USB HID) hoặc STM32.
- **Kiểu dáng:** Chuột công thái học (Ergonomic / Vertical Mouse).
- **Vật liệu điện cực tiếp xúc:** Thép không gỉ y tế 316L hoặc Silicone dẫn điện (Conductive Silicone Rubber).
- **Nguồn cấp:** Pin sạc Li-ion tích hợp (sạc qua USB-C) kèm mạch quản lý pin an toàn (BMS).
