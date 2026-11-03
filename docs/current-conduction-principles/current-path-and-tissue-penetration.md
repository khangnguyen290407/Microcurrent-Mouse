# Nguyên Lý Truyền Dẫn Dòng Điện Trong Mô Sinh Học & Độ Sâu Thâm Nhập

## 1. Dòng điện di chuyển như thế nào khi cầm chuột?

Để dòng điện có thể chạy, **bắt buộc phải có một mạch kín (Closed Loop)** gồm ít nhất 2 điện cực:
- **Cực phát (Anode / Phase A)**
- **Cực thu (Cathode / Phase B)**

Khi người dùng cầm chuột, dòng điện di chuyển qua các lớp mô cơ thể theo **con đường có trở kháng thấp nhất (Path of Least Impedance)**.

```
       [ Cực Dương (Anode) ]                     [ Cực Âm (Cathode) ]
                 │                                         │
        ┌────────▼─────────────────────────────────────────▼────────┐
        │ Lớp sừng (Stratum Corneum) - Trở kháng R_skin rất cao      │
        ├───────────────────────────────────────────────────────────┤
        │ Biểu bì & Hạ bì (Epidermis/Dermis) - R trung bình          │
        ├───────────────────────────────────────────────────────────┤
        │ Mô mỡ & Dưới da - R khá cao                              │
        ├───────────────────────────────────────────────────────────┤
        │ Mạch máu, Cơ, Dịch ngoại bào - R rất thấp (dẫn điện tốt)   │
        └───────────────────────────────────────────────────────────┘
```

---

## 2. Thách thức lớn nhất: "Hiện tượng đoản mạch bề mặt" (Surface Shunting)

Nếu bạn bố trí **cả hai điện cực đều nằm trên thân chuột** (ví dụ: một cực ở ngón tay, một cực ở lòng bàn tay):

1. **Khoảng cách điện cực $d$ quyết định độ sâu thâm nhập:**
   - Theo định luật phân bố điện trường trong mô sinh học, độ sâu xâm nhập hiệu dụng của dòng điện tỷ lệ thuận với khoảng cách giữa 2 điện cực ($d$).
   - Nếu 2 điện cực nằm quá gần nhau (vài cm trên thân chuột), đa số dòng điện sẽ chọn con đường ngắn nhất chạy lướt trên bề mặt biểu bì và mồ hôi của da (**Surface Shunting**).
2. **Dòng điện có đi tới cổ tay được không?**
   - **KHÔNG THỂ tự nhiên đi tới cổ tay** nếu cả 2 cực đều nằm ở bàn tay trên chuột. Dòng điện không bao giờ tự "chạy vòng lên cổ tay rồi quay ngược lại chuột" nếu ở cổ tay không có điện cực kéo dòng điện về.
   - Khi đó, tác dụng sinh học **chỉ giới hạn ở các mô bàn tay và ngón tay**, không giải quyết được trực tiếp bó gân hay dây thần kinh giữa (Median Nerve) nằm trong ống cổ tay.

---

## 3. Các kịch bản bố trí điện cực để dòng điện thực sự có tác dụng

### Kịch bản 1: Hai cực đều nằm trên chuột (Tác dụng cục bộ bàn tay)
- **Vị trí cực 1:** Lòng bàn tay (Thenar / Hypothenar eminence).
- **Vị trí cực 2:** Các ngón tay (nút bấm trái/phải) hoặc ngón cái.
- **Đường đi dòng điện:** Chạy qua các cơ nội tại của bàn tay (cơ liên cốt, cơ giun, cơ mô cái).
- **Tác dụng thực tế:**
  - Giảm căng mỏi các khớp ngón tay do click chuột nhiều.
  - Tăng vi tuần hoàn máu tại các đầu ngón tay (chống lạnh tay khi ngồi máy lạnh).
- **Hạn chế:** Không tác động sâu đến vùng cổ tay (Carpal Tunnel).

### Kịch bản 2: Hệ thống Chuột + Đệm kê cổ tay (Tác dụng toàn diện đến Ống Cổ Tay)
- **Cực 1 (Trên chuột):** Tiếp xúc lòng bàn tay hoặc các ngón tay.
- **Cực 2 (Trên miếng đệm kê tay Mousepad):** Tiếp xúc mặt dưới của cổ tay.
- **Đường đi dòng điện:** Bắt buộc phải đi từ lòng bàn tay **xuyên qua toàn bộ ống cổ tay** để xuống miếng đệm.
- **Tác dụng thực tế:**
  - Dòng điện đi thẳng qua dây thần kinh giữa (Median Nerve) và các gân gấp ngón tay.
  - Đây chính là vị trí điều trị chuẩn trong vật lý trị liệu hội chứng ống cổ tay.

---

## 4. Tóm tắt kết luận & Khuyến nghị kỹ thuật
- **Nếu mục tiêu chỉ là giảm mỏi ngón tay và lòng bàn tay:** Thiết kế 2 cực trên chuột là khả thi, nhưng cần đặt khoảng cách 2 cực xa nhất có thể trên thân chuột để tăng độ sâu thâm nhập vào cơ bàn tay.
- **Nếu mục tiêu là điều trị mỏi cổ tay / hội chứng ống cổ tay:** Cần cân nhắc nghiêm túc giải pháp **Chuột kết hợp Bàn di chuột (hoặc Đệm kê cổ tay dẫn điện)** để dòng điện thực sự khép kín vòng qua khớp cổ tay.
