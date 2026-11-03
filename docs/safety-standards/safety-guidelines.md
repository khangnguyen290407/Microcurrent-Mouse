# Hướng Dẫn & Tiêu Chuẩn An Toàn Điện Sinh Học (Safety Guidelines)

Dự án tiếp xúc trực tiếp dòng điện với cơ thể người, do đó **An toàn phần cứng phải là ưu tiên số 1** trước bất kỳ tính năng nào khác.

## 1. Ngưỡng dòng điện y sinh
- **Microcurrent (MENS):** Định nghĩa chuẩn trong y sinh thường nằm trong khoảng **$10\,\mu\text{A}$ đến $600\,\mu\text{A}$** (dưới $1\,\text{mA}$).
- Ở mức dòng điện này: Người dùng hầu như **không cảm nhận thấy cảm giác điện giật hay co thắt cơ**, mà chỉ tác động ở cấp độ tế bào (kích thích màng tế bào, tăng chuyển hóa dưỡng chất và sản sinh ATP).
- **Ngưỡng cảm nhận (Perception Threshold):** Thường từ $1\,\text{mA}$ trở lên đối với dòng AC tần số thấp. Không được để dòng vượt quá ngưỡng này để tránh gây giật mình, đau hoặc bỏng da.

## 2. Các nguyên tắc kỹ thuật bắt buộc
1. **Triệt tiêu thành phần một chiều (Zero DC Offset):**
   - Khi dòng điện 1 chiều (DC) chạy qua da người trong thời gian dài, hiện tượng điện phân (electrolysis) sẽ xảy ra, làm phân cực da và gây bỏng hóa học.
   - Bắt buộc dùng dạng sóng **Biphasic Alternating (Xung 2 pha đảo cực đối xứng)** hoặc tụ chống DC (DC blocking capacitor).
2. **Nguồn dòng cố định (Constant Current), không dùng nguồn áp (Constant Voltage):**
   - Trở kháng da người thay đổi rất lớn (từ $1\,\text{k}\Omega$ khi có mồ hôi đến $> 100\,\text{k}\Omega$ khi da khô).
   - Nếu dùng nguồn áp cố định, khi tay ra mồ hôi, dòng điện có thể tăng vọt đột ngột gây nguy hiểm. Nguồn dòng tự động điều chỉnh điện áp để duy trì dòng an toàn.
3. **Cách ly & Bảo vệ quá dòng phần cứng (Hardware Clamping):**
   - Không chỉ dựa vào phần mềm (firmware có thể bị crash/treo).
   - Phải có cầu chì tự phục hồi (PTC) hoặc diode Zener/mạch ngắt giới hạn cứng dòng điện ở mức an toàn tuyệt đối.
4. **Cơ chế phát hiện tiếp xúc (Contact Detection):**
   - Chỉ phát xung khi da bàn tay tiếp xúc ổn định cả 2 cực.
   - Tự động ngắt xung ngay khi nhấc tay khỏi chuột.
