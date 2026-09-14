# 08 — BẢO HIỂM & QUẢN TRỊ RỦI RO CHO ĐỘI MÁY CHO THUÊ
**Dự án:** Website cho thuê laptop đi thi — khu vực ĐH FPT Đà Nẵng (P. Hoà Hải, Ngũ Hành Sơn)
**Quy mô giả định:** 15–40 máy (mô hình hoá ở mức **25 máy**)
**Ngày lập:** 14/09/2026
**Người thực hiện:** Nhóm nghiên cứu — module Rủi ro & Bảo hiểm

> ### ⚠️ CẢNH BÁO VỀ ĐỘ TIN CẬY CỦA TÀI LIỆU NÀY
> 1. **Toàn bộ dữ liệu bên dưới lấy từ TIÊU ĐỀ + ĐOẠN TRÍCH (snippet) của WebSearch.** Công cụ mở trang (WebFetch/curl) bị chặn hoàn toàn trong phiên làm việc (EGRESS_BLOCKED) → **KHÔNG trang nào được mở và đọc trực tiếp**. Mọi con số phải được nhóm tự mở URL kiểm chứng trước khi đưa vào proposal.
> 2. **Ngân sách tìm kiếm của phiên đã hết (200/200 lượt WebSearch)** trước khi kịp tra 4 nhóm chủ đề: (a) bảo hiểm tài sản/trách nhiệm cho hộ kinh doanh VN, (b) mô hình damage waiver ngành cho thuê xe/thiết bị, (c) loss rate ngành equipment rental & annual failure rate laptop, (d) bảng giá sửa laptop tại Đà Nẵng 2025–2026. → Các phần này được trình bày dưới dạng **KHUNG PHƯƠNG PHÁP + BẢNG TRỐNG ĐỂ NHÓM TỰ KHẢO SÁT**, KHÔNG bịa số.
> 3. Mọi con số trong mô hình tài chính ở Phần 5–7 là **THAM SỐ GIẢ ĐỊNH (GĐ)**, được gắn nhãn rõ ràng. Công thức là chuẩn actuarial (đúng về mặt phương pháp); **đầu vào phải thay bằng số thật của nhóm.**

---

## MỤC LỤC
1. [Kết luận điều hành (đọc trước)](#1-kết-luận-điều-hành)
2. [Sản phẩm bảo hiểm thiết bị điện tử tại Việt Nam](#2-sản-phẩm-bảo-hiểm-thiết-bị-điện-tử-tại-việt-nam)
3. [Gói bảo hành mở rộng / bảo hiểm rơi vỡ của chuỗi bán lẻ](#3-gói-bảo-hành-mở-rộng--bảo-hiểm-rơi-vỡ-của-chuỗi-bán-lẻ)
4. [Bảo hiểm tài sản & trách nhiệm cho hộ kinh doanh — CHƯA XÁC MINH](#4-bảo-hiểm-tài-sản--trách-nhiệm-cho-hộ-kinh-doanh)
5. [Mô hình Damage Waiver (Phí miễn trừ thiệt hại)](#5-mô-hình-damage-waiver-phí-miễn-trừ-thiệt-hại)
6. [Tự bảo hiểm (Self-insurance) — công thức tính quỹ dự phòng](#6-tự-bảo-hiểm--công-thức-tính-quỹ-dự-phòng)
7. [Bảng tham số rủi ro & kết quả tính toán](#7-bảng-tham-số-rủi-ro--kết-quả-tính-toán)
8. [Chi phí sửa chữa laptop — KHUNG KHẢO SÁT (chưa có dữ liệu)](#8-chi-phí-sửa-chữa-laptop--khung-khảo-sát)
9. [Rủi ro vận hành đặc thù: EOS + Safe Exam Browser + mùa thi](#9-rủi-ro-vận-hành-đặc-thù)
10. [Rủi ro pháp lý & thiết kế hợp đồng](#10-rủi-ro-pháp-lý--thiết-kế-hợp-đồng)
11. [Ma trận rủi ro tổng hợp](#11-ma-trận-rủi-ro-tổng-hợp)
12. [Việc cần làm tiếp — checklist kiểm chứng](#12-việc-cần-làm-tiếp)
13. [Danh mục nguồn](#13-danh-mục-nguồn)

---

## 1. KẾT LUẬN ĐIỀU HÀNH

### 1.1. Ba kết luận quan trọng nhất

**KL-1 — KHÔNG thể dựa vào bảo hiểm rơi vỡ bán lẻ (FPT Shop / TGDĐ / CellphoneS / Điện Máy Xanh / Viettel Store).**
Lý do (suy ra từ các snippet đã tra, cần kiểm chứng quy tắc điều khoản gốc):
- Các gói này **gắn với máy MUA MỚI tại chính chuỗi đó**. Gói MIC × Viettel Store ghi rõ áp dụng cho "điện thoại, máy tính bảng và laptop có giá trị không vượt quá 40.000.000đ, **mua mới tại hệ thống Viettel Store**" ([viettelstore.vn](https://viettelstore.vn/tin-tuc/viettel-store-hop-tac-cung-bao-hiem-mic-mo-ban-bao-hiem-thiet-bi-di-dong-tren-toan-quoc), [micdongsaigon.com.vn](https://micdongsaigon.com.vn/khach-hang/bao-hiem-thiet-bi-di-dong/)). Mô hình của nhóm nhiều khả năng mua **máy cũ/refurb** → không đủ điều kiện.
- Gói gắn với **người mua ban đầu**, mục đích **sử dụng cá nhân**. Việc **cho thuê thương mại** gần như chắc chắn nằm trong điều khoản loại trừ. ⚠️ *Phải mở Quy tắc điều khoản (QTĐK) để xác nhận — chưa xác minh được.*
- **Giới hạn số lần**: gói S-Diamond của CellphoneS (do AIG cấp) chỉ bảo vệ rơi vỡ/vào nước **1 lần**; sau đó máy quay về điều khoản Bảo hành Vàng cho phần thời hạn còn lại ([cellphones.com.vn](https://cellphones.com.vn/chinh-sach-bao-hanh-from-11052019)). Với đội máy quay vòng 400+ lượt thuê/năm, giới hạn 1 lần/máy là vô nghĩa.
- **Thời gian xử lý quá dài**: CellphoneS ghi thời gian xử lý bảo hành **14–30 ngày** ([cellphones.com.vn](https://cellphones.com.vn/chinh-sach-bao-hanh-from-11052019)). Trong mô hình cho thuê theo mùa thi, máy nằm xưởng 14–30 ngày = mất trọn một mùa doanh thu.

**KL-2 — Dòng sản phẩm ĐÚNG cho doanh nghiệp là "Bảo hiểm Thiết bị điện tử" (Electronic Equipment Insurance – EEI), bán cho tổ chức, không bán lẻ.**
- PVI xếp sản phẩm này trong nhóm **"products/business"** (khách hàng doanh nghiệp): bồi thường thiệt hại vật chất đối với thiết bị điện tử do **"các nguyên nhân bất ngờ và không lường trước được"**; **"phí bảo hiểm được tính theo một tỷ lệ % trên số tiền bảo hiểm, tỷ lệ phí thay đổi căn cứ vào đặc điểm, tính chất của đối tượng được bảo hiểm và ngành nghề hoạt động sản xuất kinh doanh"** ([pvi.com.vn](https://www.pvi.com.vn/vi/products/business/electronic-equipment)).
- PJICO cũng có dòng tương đương ([pjico.com.vn](https://www.pjico.com.vn/san-pham/bao-hiem-thiet-bi-dien-tu)).
- ⚠️ **Rào cản thực tế**: (a) tỷ lệ phí do doanh nghiệp bảo hiểm chào riêng, **không công bố** → bắt buộc phải xin báo giá; (b) ngành nghề "cho thuê thiết bị cho người dùng cuối, thiết bị di chuyển ngoài trụ sở" là nhóm rủi ro cao, phí sẽ cao hoặc bị từ chối; (c) tổng giá trị đội máy ~200–400 triệu là **quá nhỏ so với mức tối thiểu** thường thấy của hợp đồng EEI. → **Khả năng cao KHÔNG mua được với giá hợp lý.**

**KL-3 — Chiến lược đề xuất: TỰ BẢO HIỂM 3 LỚP (không mua bảo hiểm thương mại ở năm 1).**

```
┌─────────────────────────────────────────────────────────────────┐
│ LỚP 3 — QUỸ DỰ PHÒNG RỦI RO (Self-insurance fund)               │
│   Mục tiêu ≈ 27–30 triệu đ (≈ 9–10% giá trị đội máy)            │
│   Nguồn nạp: 10% doanh thu thuê + 100% phí gói An Tâm           │
│   → Hấp thụ: mất máy, hỏng nặng, phần khách không đền được      │
├─────────────────────────────────────────────────────────────────┤
│ LỚP 2 — GÓI "AN TÂM" (Damage Waiver, khách TỰ CHỌN)             │
│   15.000đ/ngày hoặc 40.000đ/trọn đợt thi (≤4 ngày)              │
│   Hạ trách nhiệm của khách: từ "chi phí sửa thực tế"            │
│   xuống "mức miễn thường 500.000đ/vụ"                            │
│   → Biến rủi ro thành DOANH THU + xoá xung đột với khách        │
├─────────────────────────────────────────────────────────────────┤
│ LỚP 1 — KIỂM SOÁT GỐC (quan trọng nhất, chi phí gần bằng 0)     │
│   Đặt cọc • Xác minh MSSV/CCCD • Biên bản ảnh-video bàn giao    │
│   • Ghi serial • Định vị thiết bị • Máy dự phòng 15%            │
└─────────────────────────────────────────────────────────────────┘
```

### 1.2. Hai con số cần nhớ (kết quả mô hình, tham số giả định)

| Chỉ tiêu | Giá trị mô hình (kịch bản Cơ sở) | Ghi chú |
|---|---|---|
| **Quỹ dự phòng rủi ro mục tiêu** | **≈ 27 triệu đ** (≈ 9% giá trị đội máy 300 tr) | = Tổn thất kỳ vọng 13,2 tr + 1,645 × σ 8,4 tr |
| **Phí miễn trừ thiệt hại nên thu** | **15.000đ/ngày** hoặc **40.000đ/lượt** (miễn thường 500.000đ/vụ) | = Phí thuần 23.350đ/lượt × hệ số tải 1,725 ≈ 40.279đ |

> ⚠️ Hai con số này **chỉ đúng nếu bộ tham số tần suất/mức độ tổn thất ở Phần 7 đúng**. Bộ tham số đó hiện là **GIẢ ĐỊNH của nhóm, chưa có nguồn**. Xem Phần 12 để biết cách hiệu chỉnh bằng dữ liệu pilot.

---

## 2. SẢN PHẨM BẢO HIỂM THIẾT BỊ ĐIỆN TỬ TẠI VIỆT NAM

### 2.1. Bảng tổng hợp (dữ liệu từ snippet — CHƯA mở trang)

| Nhà BH | Sản phẩm | Đối tượng | Phạm vi (theo snippet) | Phí | Bảo hiểm MẤT CẮP? | Nguồn |
|---|---|---|---|---|---|---|
| **PVI** | Bảo hiểm Thiết bị điện tử (EEI) | **Doanh nghiệp** — thiết bị điện tử ngành tin học, viễn thông, phát thanh truyền hình, hàng không, khí tượng, KHKT | Thiệt hại vật chất do "nguyên nhân bất ngờ và không lường trước được" | **% trên số tiền bảo hiểm**; tỷ lệ thay đổi theo đặc điểm tài sản & ngành nghề. **Không công bố số cụ thể** | ❓ Không nêu trong snippet | [pvi.com.vn](https://www.pvi.com.vn/vi/products/business/electronic-equipment) |
| **PJICO** | Bảo hiểm Thiết bị điện tử | Doanh nghiệp | Chưa đọc được nội dung | ❓ | ❓ | [pjico.com.vn](https://www.pjico.com.vn/san-pham/bao-hiem-thiet-bi-dien-tu) |
| **MIC (Bảo hiểm Quân đội)** | Bảo hiểm Thiết bị Di động (hợp tác Viettel Store, tái BH: **Chubb Việt Nam**) | **Cá nhân** — điện thoại, máy tính bảng, **laptop** giá trị **≤ 40.000.000đ**, **mua mới tại Viettel Store** | Vỡ màn hình, vào nước/chất lỏng, và các hư hỏng khác không thuộc loại trừ. Đổi máy mới **tối đa 2 lần** nếu không sửa được. Thời hạn **6 hoặc 12 tháng** từ ngày kế tiếp ngày mua. Phạm vi địa lý toàn cầu trừ Cuba, giới hạn 1 chuyến đi liên tục ≤ 60 ngày | Snippet nêu 2 mốc: **"từ 255.000đ"** và **"giảm tới 35%, còn từ 165.000đ"** — ⚠️ **không rõ tương ứng giá trị máy nào** | ❓ Snippet **không khẳng định**. Có **"mức khấu trừ"** (deductible) khách phải trả mỗi lần sửa/đổi | [viettelstore.vn](https://viettelstore.vn/tin-tuc/viettel-store-hop-tac-cung-bao-hiem-mic-mo-ban-bao-hiem-thiet-bi-di-dong-tren-toan-quoc), [viettelstore.vn (165k)](https://viettelstore.vn/tin-tuc/bao-hiem-thiet-bi-di-dong-bao-ve-suc-khoe-de-yeu-cua-ban-gia-chi-tu-165-000d), [micdongsaigon.com.vn](https://micdongsaigon.com.vn/khach-hang/bao-hiem-thiet-bi-di-dong/) |
| **OPES** | Bảo hiểm **vỡ màn hình điện thoại** (có QTĐK công bố) | Cá nhân — **điện thoại**, không thấy laptop | Vỡ màn hình | ❓ | ❓ | [opes.com.vn QTĐK](https://opes.com.vn/congbo/sanpham/qtdk-phonescreen-V1) |
| **OPES** | Danh mục sản phẩm số | Cá nhân | "bảo hiểm chậm chuyến bay, **bảo hiểm vỡ màn hình thiết bị điện tử**, bảo hiểm chuyến đi xe công nghệ — cách mua đơn giản, chi phí thấp, bồi thường nhanh" | ❓ | ❓ | [dantri.com.vn](https://dantri.com.vn/kinh-doanh/bao-hiem-opes-tien-phong-trai-nghiem-so-danh-cho-khach-hang-20240104092308426.htm) |
| **Papaya Insurtech** | — | — | Kết quả tra cứu cho thấy **tập trung vào bảo hiểm xe máy**; **không tìm thấy sản phẩm laptop** | — | — | [ppaya.vn](https://ppaya.vn/) |
| **Bảo Việt** | — | — | ❌ **KHÔNG tra được** (hết ngân sách search) | — | — | — |
| **Bảo Minh** | — | — | ❌ **KHÔNG tra được** | — | — | — |
| **PTI** | — | — | ❌ **KHÔNG tra được** | — | — | — |
| **Liberty** | — | — | ❌ **KHÔNG tra được** | — | — | — |

### 2.2. Vấn đề "BẢO HIỂM MẤT CẮP" — câu trả lời thận trọng

Đây là câu hỏi **quan trọng nhất** với mô hình cho thuê, vì mất máy / khách không trả máy là tổn thất tuyệt đối (100% giá trị tài sản).

**Những gì tra được:**
- Một snippet tổng hợp có nêu: *"Sản phẩm bảo hiểm cho thiết bị di động và laptop thường bảo hiểm mất mát/trộm cắp, trộm đột nhập, trộm có dấu hiệu phá khoá, hoặc cướp giật."*
- ⚠️ **CẢNH BÁO**: snippet này có khả năng cao bị **trộn từ nguồn bảo hiểm HÀNH LÝ DU LỊCH** ([baohiemvui.vn — "Quyền lợi bảo hiểm hành lý mất cắp"](https://baohiemvui.vn/quyen-loi-bao-hiem-hanh-ly-mat-cap-duoc-boi-thuong-bao-nhieu/)), **không phải** từ sản phẩm bảo hiểm laptop. **KHÔNG được trích dẫn câu này trong proposal.**

**Nhận định của nhóm (cần kiểm chứng):**
- Các gói bán lẻ tại VN thường được đặt tên **"bảo hiểm/bảo hành RƠI VỠ, VÀO NƯỚC"** — tên gọi này tự nó cho thấy phạm vi là **hư hỏng do tai nạn (accidental damage)**, **không phải trộm cắp**.
- Trộm cắp thường chỉ nằm trong: bảo hiểm hành lý (du lịch), bảo hiểm tài sản/trộm cắp cho doanh nghiệp (dòng riêng), hoặc gói cao cấp có phụ lục.
- **Trộm cắp do chính người thuê gây ra (fraud/misappropriation)** thì **hầu như không có sản phẩm bảo hiểm nào tại VN nhận** — đây là rủi ro tín dụng/gian lận, không phải rủi ro tai nạn. → **Phải xử lý bằng đặt cọc + xác minh danh tính, không phải bằng bảo hiểm.**

> 📌 **Hệ quả cho proposal**: Rủi ro mất máy **PHẢI được tự gánh** (Lớp 1 + Lớp 3). Đừng viết trong proposal rằng "sẽ mua bảo hiểm mất cắp" nếu chưa có báo giá thực tế.

### 2.3. Nền pháp lý về điều khoản loại trừ
Điều khoản loại trừ trách nhiệm bảo hiểm là quy định về các trường hợp doanh nghiệp bảo hiểm **không phải bồi thường** khi sự kiện bảo hiểm xảy ra. Khi mua bất kỳ gói nào, phải đọc kỹ mục này.
- [VKSND Tối cao — "Thực hiện điều khoản loại trừ trách nhiệm bảo hiểm trong hợp đồng bảo hiểm"](https://vksndtc.gov.vn/tin-tuc/cong-tac-kiem-sat/thuc-hien-dieu-khoan-loai-tru-trach-nhiem-bao-hiem-d10-t11857.html)
- [Công ty Luật ACC — "Công ty bảo hiểm từ chối chi trả do điều khoản loại trừ xử lý sao?"](https://congtyluatacc.vn/cong-ty-bao-hiem-tu-choi-chi-tra-do-dieu-khoan-loai-tru-xu-ly-sao/)
- [Manulife — Các điều khoản loại trừ (tham khảo khái niệm)](https://www.manulife.com.vn/vi/kien-thuc/cac-dieu-khoan-loai-tru-trong-bao-hiem-nhan-tho.html)

---

## 3. GÓI BẢO HÀNH MỞ RỘNG / BẢO HIỂM RƠI VỠ CỦA CHUỖI BÁN LẺ

### 3.1. Bảng so sánh (dữ liệu snippet — CHƯA mở trang)

| Chuỗi | Tên gói | Giá | Phạm vi | Điểm chặn với mô hình cho thuê | Nguồn |
|---|---|---|---|---|---|
| **FPT Shop** | Bảo hành rơi vỡ, vào nước (điện thoại & **laptop**) | **Từ 79.000đ** | Rơi vỡ, vào nước. Nhân viên đến **tận nơi lấy máy, mang đi sửa, trả lại — miễn phí thủ tục** | Gắn với máy mua tại FPT Shop; mức 79.000đ nhiều khả năng là bậc **thấp nhất cho điện thoại**, không phải laptop | [fptshop.com.vn 137045](https://fptshop.com.vn/tin-tuc/tin-khuyen-mai/goi-bao-hanh-roi-vo-dien-thoai-laptop-tai-fpt-shop-gia-chi-tu-79000-dong-137045), [fptshop.com.vn 140490](https://fptshop.com.vn/tin-tuc/tin-khuyen-mai/bao-hanh-roi-vo-vao-nuoc-tai-fpt-shop-gia-chi-tu-79000-dong-140490), [znews.vn](https://znews.vn/bao-hanh-roi-vo-vao-nuoc-tai-fpt-shop-voi-gia-tu-79000-dong-post1290215.html) |
| **FPT Shop** | Chính sách đổi máy khi hỏng nặng do lỗi khách hàng | **Phí = 25% giá trị máy cũ** | Nếu hỏng nặng trong thời hạn bảo hành **do lỗi khách hàng** và **không sửa được**, FPT Shop hỗ trợ **đổi máy tương đương** với phí bằng **25% giá trị máy cũ** | 🔑 **Đây là benchmark rất hữu ích** — xem 3.3 | [fptshop.com.vn 154419](https://fptshop.com.vn/tin-tuc/tin-moi/chinh-sach-bao-hanh-fpt-shop-154419) + snippet 137045 |
| **FPT Shop** | SLA thời gian xử lý | — | **24h tại HN & TP.HCM; 48h tại ĐÀ NẴNG & Cần Thơ; tối đa 5 ngày các tỉnh khác** | 🔑 **48h ở Đà Nẵng** — dùng làm mốc lập kế hoạch máy dự phòng | snippet 137045 |
| **CellphoneS** | **S-Diamond** (do **AIG** cấp) | ❓ | Rơi vỡ, vào nước — **CHỈ 1 LẦN**; sau đó máy chuyển sang điều khoản Bảo hành Vàng cho thời hạn còn lại. **Thời gian xử lý 14–30 ngày** | ❌ 1 lần/máy + 14–30 ngày = không dùng được | [cellphones.com.vn](https://cellphones.com.vn/chinh-sach-bao-hanh-from-11052019) |
| **CellphoneS + AIG** | (Bài báo phản ánh) | — | Bài *"Thượng đế khóc thét vì gói bảo hành mở rộng của CellphoneS và AIG"* | ⚠️ Có tranh chấp thực tế về gói này → **đọc trước khi tham chiếu** | [phapluatplus.baophapluat.vn](https://phapluatplus.baophapluat.vn/thuong-de-khoc-thet-vi-goi-bao-hanh-mo-rong-cua-cellphones-va-aig-111448.html) |
| **Thế Giới Di Động** | Bảo hiểm rơi vỡ / BH mở rộng / BH 1 đổi 1 | ⚠️ Snippet trả về: *"máy tính bảng: tháng đầu 20% giá trị hoá đơn, tháng 2–12 là 10% giá trị hoá đơn/tháng"* — **CON SỐ NÀY RẤT ĐÁNG NGỜ** (giống biểu phí thu hồi/khấu hao hơn là phí bảo hành). **KHÔNG dùng cho đến khi mở trang xác minh** | ❓ | — | [tgdd 1567763](https://www.thegioididong.com/tin-tuc/tat-tan-tat-ve-chinh-sach-bao-hiem-roi-vo-bao-hanh-mo-rong-bao-hanh-1-doi-1-tai-tgdd-1567763), [tgdd 1460444](https://www.thegioididong.com/hoi-dap/tong-hop-csbh-the-gioi-di-dong-toan-nganh-hang-1460444), [tgdd 1324313](https://www.thegioididong.com/tin-tuc/dien-thoai-laptop--tu-nay-roi-vo-da-co-bao-hiem-do-1324313) |
| **Điện Máy Xanh** | Bảo hiểm rơi vỡ / Bảo hành mở rộng | ❓ Snippet chỉ có: laptop & hàng công nghệ *"giảm 5%–15% kèm phụ kiện hoặc gói bảo hành mở rộng"*; và *"trừ 5% giá trị hoá đơn"* khi không đủ điều kiện — **cả hai đều mơ hồ, không phải biểu phí** | ❓ | — | [dmx 1574741](https://www.dienmayxanh.com/kinh-nghiem-hay/chinh-sach-bao-hiem-roi-vo-bao-hanh-mo-rong-bao-1574741), [dmx dịch vụ BHMR](https://www.dienmayxanh.com/dich-vu-bao-hanh-mo-rong), [dmx 773940](https://www.dienmayxanh.com/kinh-nghiem-hay/chinh-sach-bao-hanh-nhom-hang-dien-thoai-laptop-sm-773940) |
| **Viettel Store** | Bảo hiểm Thiết bị Di động (MIC) + gia hạn bảo hành | **Từ 255.000đ** (list) / **từ 165.000đ** (sau giảm 35%) | Xem mục 2.1 | Máy phải **mua mới tại Viettel Store** | [viettelstore.vn tổng hợp](https://viettelstore.vn/tin-tuc/tong-hop-cac-goi-bao-hiem-thiet-bi-di-dong-gia-han-bao-hanh-tai-viettel-store) |

### 3.2. Ước lượng tỷ lệ phí từ dữ liệu bán lẻ (tính toán của nhóm, có điều kiện)

Đây là phép chia trên **số liệu đã xác minh qua snippet**, nhưng mẫu số (giá trị máy tương ứng mốc giá đó) **chưa xác minh** → chỉ dùng làm **khoảng tham chiếu**, không dùng làm kết luận.

| Giả định giá trị máy được bảo hiểm | Phí 255.000đ tương đương | Phí 165.000đ tương đương |
|---|---|---|
| 10.000.000đ | **2,55%** giá trị/kỳ | **1,65%** |
| 15.000.000đ | **1,70%** | **1,10%** |
| 20.000.000đ | **1,28%** | **0,83%** |
| 40.000.000đ (trần sản phẩm MIC) | **0,64%** | **0,41%** |

**Đọc bảng này thế nào:** thị trường bán lẻ VN đang định giá bảo hiểm rơi vỡ cho **người dùng cá nhân** ở khoảng **≈0,6%–2,6% giá trị máy cho 6–12 tháng**, và vẫn còn **mức khấu trừ** khách phải trả mỗi lần sửa.
→ **Rủi ro cho thuê cao hơn rủi ro cá nhân NHIỀU LẦN** (máy đổi tay 15–20 lần/năm, người dùng không sở hữu nên ít giữ gìn, luôn phải di chuyển). Phí tự bảo hiểm của nhóm **phải cao hơn hẳn** khoảng này — mô hình ở Phần 7 cho ra ~9,3%/năm giá trị đội máy, tức **cao gấp 4–14 lần** mức bán lẻ cá nhân. Đây là kiểm tra tính hợp lý (sanity check) cho thấy con số của nhóm **không vô lý**.

### 3.3. Benchmark quan trọng: quy tắc "25%" của FPT Shop

> *"Nếu sản phẩm phát sinh hư hỏng nặng trong thời gian bảo hành **do lỗi khách hàng** và không thể sửa chữa được, FPT Shop hỗ trợ **đổi máy tương đương với phí bằng 25% giá trị máy cũ**."* — snippet [fptshop.com.vn 137045](https://fptshop.com.vn/tin-tuc/tin-khuyen-mai/goi-bao-hanh-roi-vo-dien-thoai-laptop-tai-fpt-shop-gia-chi-tu-79000-dong-137045)

**Ứng dụng trực tiếp:** nhóm có thể sao chép cấu trúc này cho điều khoản "máy hỏng không sửa được" trong hợp đồng thuê:
- Khách **CÓ** gói An Tâm → chỉ trả **25% giá trị còn lại của máy** (trần tổn thất, dễ chấp nhận, có tiền lệ thị trường để viện dẫn).
- Khách **KHÔNG** có gói An Tâm → trả **100% giá trị thay thế**, trừ đi tiền cọc.
→ Chênh lệch 25% vs 100% chính là **lý do bán được gói An Tâm**.

---

## 4. BẢO HIỂM TÀI SẢN & TRÁCH NHIỆM CHO HỘ KINH DOANH

> ### ❌ PHẦN NÀY CHƯA CÓ DỮ LIỆU XÁC MINH
> Ngân sách WebSearch của phiên đã hết trước khi kịp tra chủ đề này. **Không có bất kỳ con số phí nào được xác minh.** Dưới đây chỉ là **khung để nhóm tự đi khảo sát**.

### 4.1. Các dòng sản phẩm cần hỏi báo giá (khi liên hệ đại lý)

| Dòng sản phẩm | Tên gọi tiếng Việt thường dùng | Bảo vệ điều gì | Có phù hợp dự án? |
|---|---|---|---|
| Property / Fire & Special Perils | **Bảo hiểm hoả hoạn và các rủi ro đặc biệt** | Cháy, nổ, sét, giông bão, ngập lụt tại **địa điểm kho/văn phòng** | ✅ Phù hợp — bảo vệ đội máy **khi đang ở kho**. Rẻ nhất trong các lựa chọn. **Không** bảo vệ khi máy ở ngoài |
| Burglary / Theft | **Bảo hiểm trộm cắp** | Trộm đột nhập có dấu vết phá khoá tại địa điểm được bảo hiểm | ⚠️ Chỉ bảo vệ **trộm tại kho**, KHÔNG bảo vệ khách không trả máy |
| Electronic Equipment Insurance | **Bảo hiểm thiết bị điện tử** (PVI, PJICO) | Thiệt hại vật chất bất ngờ, kể cả khi di chuyển (tuỳ phạm vi mở rộng) | ✅ Đúng dòng nhất — nhưng xem rào cản ở KL-2 |
| Public Liability | **Bảo hiểm trách nhiệm công cộng** | Thiệt hại gây ra cho bên thứ ba | ⚠️ Ưu tiên thấp với mô hình này |
| — | **Bảo hiểm gián đoạn kinh doanh** | Mất doanh thu do tài sản hư hỏng | ❌ Không cần ở quy mô 25 máy |

### 4.2. Kịch bản gọi điện xin báo giá (dùng luôn được)

> "Chào anh/chị, em là chủ một hộ kinh doanh nhỏ tại Đà Nẵng, ngành **cho thuê laptop ngắn hạn cho sinh viên**. Em có **25 máy tính xách tay**, tổng giá trị khoảng **300 triệu đồng**, để tại một địa điểm ở P. Hoà Hải, Ngũ Hành Sơn. Máy được khách thuê mang ra ngoài **2–5 ngày/lượt**, khoảng **450 lượt/năm**.
> Em muốn hỏi báo giá cho:
> 1. **Bảo hiểm thiết bị điện tử** — phạm vi: hư hỏng vật chất bất ngờ, **bao gồm cả khi thiết bị ở ngoài trụ sở trong tay người thuê**. Tỷ lệ phí bao nhiêu %/năm? Mức khấu trừ (deductible) bao nhiêu/vụ?
> 2. **Bảo hiểm hoả hoạn & rủi ro đặc biệt** cho tài sản tại kho. Phí bao nhiêu?
> 3. **Bảo hiểm trộm cắp** tại kho.
> Cho em hỏi thêm: **mất mát do người thuê không trả lại máy** có thuộc phạm vi bảo hiểm nào không ạ? Và **số tiền bảo hiểm tối thiểu** để anh/chị nhận đơn là bao nhiêu?"

**Đối tượng cần gọi (ít nhất 4, để có 4 báo giá so sánh):** PVI, PJICO, Bảo Việt, Bảo Minh, PTI, MIC — chi nhánh/đại lý tại Đà Nẵng.

### 4.3. Bảng trống để điền kết quả khảo sát

| Nhà BH | Sản phẩm chào | Số tiền BH | Tỷ lệ phí (%/năm) | Phí (đ/năm) | Mức khấu trừ | Có nhận ngành cho thuê? | Có BH mất cắp/không trả máy? | Ngày liên hệ |
|---|---|---|---|---|---|---|---|---|
| PVI | | | | | | | | |
| PJICO | | | | | | | | |
| Bảo Việt | | | | | | | | |
| Bảo Minh | | | | | | | | |
| PTI | | | | | | | | |
| MIC | | | | | | | | |

**Ngưỡng quyết định (đề xuất):** nếu tổng phí bảo hiểm thương mại **> 15 triệu đ/năm** (≈ tổn thất kỳ vọng 13,2 tr) thì **không mua** — tự bảo hiểm rẻ hơn. Nếu **< 8 triệu đ/năm** và phạm vi có bao gồm hư hỏng ngoài trụ sở thì **nên mua** và giảm quỹ dự phòng tương ứng.

---

## 5. MÔ HÌNH DAMAGE WAIVER (PHÍ MIỄN TRỪ THIỆT HẠI)

> ### ⚠️ Dữ liệu ngành CHƯA tra được
> Không tra được số liệu thực tế về **cách định giá CDW/LDW của ngành cho thuê xe**, **mức miễn thường phổ biến**, và **tỉ lệ khách mua (take-up rate)**. Các con số ngành bị bỏ trống, **không bịa**. Phần dưới trình bày **bản chất mô hình + công thức định giá + số của riêng dự án**.

### 5.1. Damage Waiver là gì — và tại sao KHÔNG phải bảo hiểm

**Damage Waiver (DW) / Collision Damage Waiver (CDW) / Loss Damage Waiver (LDW)** là một **điều khoản trong hợp đồng thuê**, theo đó bên cho thuê **từ bỏ (waive) quyền đòi bồi thường** đối với bên thuê khi tài sản bị hư hỏng, đổi lại bên thuê trả một khoản phí.

| | Bảo hiểm | Damage Waiver |
|---|---|---|
| Bản chất pháp lý | Hợp đồng bảo hiểm — chịu quản lý của Luật Kinh doanh bảo hiểm | **Điều khoản dân sự trong hợp đồng thuê tài sản** |
| Ai cấp | Doanh nghiệp bảo hiểm có giấy phép | **Chính bên cho thuê** |
| Cần giấy phép? | Có | **Không** |
| Ai gánh rủi ro | Doanh nghiệp bảo hiểm | **Bên cho thuê tự gánh** |
| Bồi thường cho ai | Bên được bảo hiểm | Không bồi thường — chỉ **miễn trừ nghĩa vụ đền** của khách |

> 🔑 **Điểm mấu chốt cho proposal**: vì DW **không phải bảo hiểm**, một hộ kinh doanh/startup sinh viên **được phép** áp dụng ngay mà **không cần giấy phép kinh doanh bảo hiểm**. Đây chính là lý do mô hình này khả thi. ⚠️ *Cần luật sư/giảng viên xác nhận về mặt pháp lý VN trước khi khẳng định trong proposal.*
> 🔒 **Quy tắc câu chữ bắt buộc**: **TUYỆT ĐỐI KHÔNG** gọi gói này là "bảo hiểm" trên website, hợp đồng hay tài liệu marketing. Gọi là **"Gói Miễn trừ thiệt hại"**, **"Gói An Tâm"**, hoặc **"Gói giới hạn trách nhiệm"**. Dùng từ "bảo hiểm" khi không có giấy phép là rủi ro pháp lý.

### 5.2. Công thức định giá Damage Waiver

```
                 E[L_có_thể_miễn_trừ]  −  E[min(L, D)]
  PHÍ DW  =  ─────────────────────────────────────────────  × (1+e) × (1+a) × (1+m)
                              1

  Trong đó:
    E[L]          = tổn thất kỳ vọng/lượt thuê của các hiểm hoạ được miễn trừ
    E[min(L, D)]  = phần khách vẫn giữ lại = mức miễn thường D (deductible)
    e             = hệ số chi phí xử lý & hành chính     (đề xuất 0,15)
    a             = hệ số phản chọn lựa (adverse selection) (đề xuất 0,25)
    m             = biên an toàn & lợi nhuận             (đề xuất 0,20)
```

**Giải thích 3 hệ số tải:**
- **e = 15%** — chi phí giám định, chụp ảnh, liên hệ xưởng, xử lý tranh chấp, thời gian nhân sự.
- **a = 25% (Phản chọn lựa)** — đây là hệ số **quan trọng nhất và hay bị quên**. Người tự thấy mình **hậu đậu, hay để máy trong balo chật, hay đi mưa** là người có xác suất mua gói DW cao nhất. Nhóm khách mua DW **rủi ro cao hơn** nhóm trung bình. Nếu định giá bằng tần suất trung bình toàn tập khách, **gói DW chắc chắn lỗ**. Hệ số 1,25 là mức bù thận trọng, có thể phải nâng lên 1,4–1,5 nếu dữ liệu pilot cho thấy chênh lệch lớn.
- **m = 20%** — biên lợi nhuận + đệm sai số tham số.

**Tổng hệ số tải = 1,15 × 1,25 × 1,20 = 1,725** (tức phí niêm yết ≈ 1,7 lần phí thuần).

### 5.3. Vai trò của mức miễn thường (Deductible / Mức khấu trừ)

Mức miễn thường **D** là số tiền khách **vẫn phải trả** cho mỗi vụ dù đã mua gói. Nó phục vụ 3 mục đích:

1. **Chống rủi ro đạo đức (moral hazard)** — nếu D = 0, khách mua gói rồi sẽ dùng máy cẩu thả hơn hẳn. D > 0 giữ cho khách "có phần da thịt trong cuộc chơi".
2. **Loại bỏ các vụ nhỏ, chi phí xử lý cao hơn giá trị bồi thường** — ví dụ mất cục sạc 350.000đ: nếu D = 500.000đ thì khách tự trả, doanh nghiệp không tốn công xử lý.
3. **Hạ giá gói xuống mức bán được** — xem bảng độ nhạy bên dưới.

**Độ nhạy của phí DW theo mức miễn thường** (tính trên bộ tham số Cơ sở ở Phần 7, 450 lượt/năm):

| Mức miễn thường D | Phí thuần (đ/lượt) | Phí niêm yết ×1,725 (đ/lượt) | Quy ra đ/ngày (lượt TB 3 ngày) | Đánh giá |
|---|---|---|---|---|
| **0đ** (miễn trừ toàn bộ) | 46.850 | **80.816** | ~27.000 | ❌ Quá đắt so với giá thuê; moral hazard cao |
| **300.000đ** | 30.050 | **51.836** | ~17.300 | ⚠️ Chấp nhận được |
| **500.000đ** ✅ | 23.350 | **40.279** | ~13.400 | ✅ **ĐỀ XUẤT** — cân bằng tốt nhất |
| **1.000.000đ** | ~14.500 (ước) | ~25.000 | ~8.300 | ⚠️ Rẻ nhưng giá trị cảm nhận thấp, khó bán |

### 5.4. Cấu trúc gói đề xuất cho dự án

| | **GÓI CƠ BẢN** (mặc định, 0đ) | **GÓI AN TÂM** (tự chọn) |
|---|---|---|
| **Giá** | Đã nằm trong giá thuê | **15.000đ/ngày** hoặc **40.000đ/trọn đợt thi (≤4 ngày)** |
| **Trách nhiệm của khách khi máy hư hỏng** | **100% chi phí sửa chữa thực tế**, tối đa bằng giá trị thay thế máy | **Tối đa 500.000đ/vụ** (mức miễn thường) |
| **Nếu máy hỏng không sửa được** | Đền **100% giá trị còn lại** của máy | Đền **25% giá trị còn lại** (áp dụng chuẩn tương tự FPT Shop) |
| **Vỡ màn hình** | Khách trả toàn bộ (~2,5 tr) | Khách trả 500.000đ |
| **Đổ nước, hỏng bàn phím** | Khách trả toàn bộ (~800k) | Khách trả 500.000đ |
| **Gãy bản lề, nứt vỏ** | Khách trả toàn bộ (~1,2 tr) | Khách trả 500.000đ |
| **Mất/hỏng sạc & phụ kiện** | Khách trả toàn bộ (~350k) | Khách trả toàn bộ (vì < 500k) |
| **Hao mòn tự nhiên, chai pin** | ❌ **Không tính tiền khách** (chi phí vận hành của doanh nghiệp) | ❌ Không tính tiền khách |
| **🚫 MẤT MÁY / KHÔNG TRẢ MÁY / TRỘM CẮP** | **LOẠI TRỪ** — khách đền 100% giá trị thay thế | **LOẠI TRỪ — gói An Tâm KHÔNG bảo vệ trường hợp này** |
| **🚫 Cố ý phá hoại, cho người khác thuê lại, tháo linh kiện** | Loại trừ | **Loại trừ** |

> 📢 **Câu bán hàng (dùng cho website)**: *"Chỉ 40.000đ cho cả đợt thi — nếu lỡ tay làm vỡ màn hình (sửa khoảng 2,5 triệu), bạn chỉ trả tối đa 500.000đ."*
> Tỷ lệ đòn bẩy giá trị cảm nhận: **2.500.000 / 40.000 = 62,5 lần**. Đây là lý do gói này bán được.

### 5.5. Tỉ lệ khách mua (Take-up rate) — CHƯA CÓ DỮ LIỆU

❌ **Không tra được** số liệu take-up rate của ngành cho thuê xe/thiết bị. Mô hình dưới đây chạy 3 kịch bản:

| Kịch bản | Take-up | Doanh thu gói An Tâm/năm (450 lượt × 40.000đ) | Chi phí bồi thường (450 × take-up × 23.350đ) | Lãi gộp gói |
|---|---|---|---|---|
| Thấp | 20% | 3.600.000đ | 2.101.500đ | **+1.498.500đ** |
| **Cơ sở** | **35%** | **6.300.000đ** | **3.677.625đ** | **+2.622.375đ** |
| Cao | 60% | 10.800.000đ | 6.304.500đ | **+4.495.500đ** |

> 💡 **Lưu ý về phản chọn lựa**: take-up càng cao thì thành phần phản chọn lựa càng **loãng** (tiệm cận tần suất trung bình toàn tập). Take-up thấp (20%) là trường hợp **phản chọn lựa nặng nhất** — chỉ những người tự biết mình rủi ro cao mới mua. Nếu take-up thực tế ở mức 15–25%, phải **nâng hệ số a lên 1,4–1,5** và tăng giá gói.
>
> 💡 **Mẹo tăng take-up**: đặt gói An Tâm là lựa chọn **được chọn sẵn (pre-checked)** trên form đặt thuê, khách phải chủ động bỏ chọn. Kỹ thuật này nâng take-up rất mạnh. ⚠️ *Cần cân nhắc khía cạnh đạo đức & quy định bảo vệ người tiêu dùng — nên hiển thị rõ ràng, không giấu.*

---

## 6. TỰ BẢO HIỂM — CÔNG THỨC TÍNH QUỸ DỰ PHÒNG

### 6.1. Bộ công thức chuẩn (đây là PHƯƠNG PHÁP, không phải dữ liệu — dùng được ngay)

#### Bước 1 — Phí thuần (Pure Premium)
```
  P  =  Σ ( f_i × s_i )
```
- `f_i` = tần suất xảy ra hiểm hoạ loại *i* (số vụ trên một lượt thuê)
- `s_i` = mức độ tổn thất trung bình của hiểm hoạ loại *i* (đồng/vụ)

#### Bước 2 — Tổn thất kỳ vọng năm (mô hình Poisson gộp / Compound Poisson)
```
  λ_i   =  n × f_i                    (n = tổng số lượt thuê/năm)

  E[L]  =  Σ ( λ_i × s_i )            ← Tổn thất KỲ VỌNG
  Var(L)=  Σ ( λ_i × s_i² )           ← Phương sai
  σ(L)  =  √ Var(L)                   ← Độ lệch chuẩn (mức độ biến động)
```
> 📐 Công thức `Var = Σ λ_i s_i²` đúng khi mỗi loại hiểm hoạ có mức tổn thất cố định `s_i` và số vụ tuân theo phân phối Poisson độc lập. Nếu mức tổn thất trong một loại cũng biến thiên, dùng `Var = Σ λ_i (σ_i² + s_i²)`.

#### Bước 3 — Quy mô quỹ dự phòng (Nguyên tắc độ lệch chuẩn)
```
  QUỸ  =  E[L]  +  z × σ(L)
```
| Mức tin cậy mong muốn | z | Ý nghĩa |
|---|---|---|
| 90% | 1,282 | Quỹ đủ trong 9/10 năm |
| **95%** ✅ | **1,645** | **Quỹ đủ trong 19/20 năm — ĐỀ XUẤT cho dự án sinh viên** |
| 99% | 2,326 | Rất thận trọng, đọng vốn nhiều |
| 99,5% | 2,576 | Chuẩn Solvency II của ngành BH — quá mức cho quy mô này |

> ⚠️ **Hạn chế của công thức**: dùng xấp xỉ phân phối chuẩn. Với đội máy nhỏ (25 máy) và một hiểm hoạ tổn thất lớn (mất máy 12 triệu), phân phối thực tế **lệch phải mạnh (right-skewed)** → công thức này có xu hướng **ĐÁNH GIÁ THẤP** phần đuôi. **Khuyến nghị nhân thêm hệ số an toàn 1,15–1,25** hoặc chạy mô phỏng Monte Carlo bằng Excel (hàm `POISSON.INV(RAND(); λ)`).

#### Bước 4 — Tỷ lệ trích lập từ doanh thu
```
                   E[L_ròng_doanh_nghiệp_gánh]
  Tỷ lệ trích  =  ─────────────────────────────  × 100%
                      Doanh thu thuê năm
```
Trích đến khi quỹ đạt mức mục tiêu, sau đó **giảm xuống mức duy trì** = mức chi thực tế bình quân. **Nạp lại đầy sau mỗi lần chi.**

#### Bước 5 — Hiệu chỉnh tham số bằng dữ liệu thật (Lý thuyết Tín nhiệm — Limited Fluctuation Credibility)
Sau mùa thi đầu tiên, nhóm có dữ liệu thật nhưng số vụ còn ít → **không nên vứt bỏ giả định ban đầu**, mà pha trộn:
```
  f_mới  =  Z × f_quan_sát  +  (1 − Z) × f_giả_định

              ┌─────────
  Z  =  min ⎜ √ (n / 1082) ,  1 ⎟
              └─────────
       n = số vụ tổn thất THỰC TẾ đã quan sát
       1082 = (1,645 / 0,05)² — chuẩn tín nhiệm đầy đủ cho tần suất Poisson (P=90%, k=5%)
```
**Ví dụ thực tế:** sau mùa thi đầu tiên nhóm ghi nhận **12 vụ tổn thất**.
`Z = √(12/1082) = √0,01109 = 0,105` → chỉ **10,5%** trọng số cho số liệu quan sát, **89,5%** vẫn theo giả định.
→ **Bài học:** đừng vội sửa mạnh mô hình sau 1 mùa. Cần **~100 vụ** (`Z = √(100/1082) = 0,30`) mới đủ tin cậy 30%.

### 6.2. So sánh 3 chiến lược xử lý rủi ro

| Tiêu chí | (A) Không làm gì | (B) Mua bảo hiểm thương mại | (C) Tự bảo hiểm + DW ✅ |
|---|---|---|---|
| Chi phí năm | 0đ danh nghĩa | Phí BH (chưa biết, ước > 15 tr/năm nếu mua được) | ~13,2 tr tổn thất kỳ vọng, bù một phần bằng doanh thu DW |
| Vốn cần đọng | 0 | Thấp | **~27 tr** (quỹ) |
| Khả năng chịu cú sốc lớn | ❌ Một vụ mất 2 máy là phá sản | ✅ Tốt | ⚠️ Trung bình — cần hạn mức dừng (xem 6.3) |
| Rào cản triển khai | Không | ⚠️ **Cao** — có thể không nhà BH nào nhận | ✅ Thấp |
| Có tạo doanh thu? | Không | Không | ✅ **Có** — gói An Tâm lãi ~2,6 tr/năm |
| Thời gian xử lý sự cố | — | ⚠️ 14–30 ngày (tham chiếu CellphoneS) → mất mùa thi | ✅ **Tự quyết, sửa ngay trong 48h** |
| **Khuyến nghị** | ❌ | ⚠️ Chỉ mua BH hoả hoạn cho kho nếu rẻ | ✅ **CHỌN** |

### 6.3. Hạn mức dừng (Stop-loss) — điều kiện an toàn bắt buộc

Tự bảo hiểm chỉ an toàn khi tổn thất **không quá tập trung**. Đặt các ngưỡng cảnh báo:

| Ngưỡng | Điều kiện kích hoạt | Hành động bắt buộc |
|---|---|---|
| 🟡 **Vàng** | Quỹ tụt xuống **< 50%** mức mục tiêu (< 13,5 tr) | Tăng tỷ lệ trích từ 10% → 18% doanh thu; rà soát lại quy trình bàn giao |
| 🟠 **Cam** | Quỹ tụt **< 25%** (< 6,75 tr) HOẶC có **≥ 2 vụ mất máy trong 1 quý** | Nâng tiền cọc lên 3 tr; tạm ngừng cho thuê khách chưa xác minh được MSSV; xem lại giá |
| 🔴 **Đỏ** | Quỹ cạn HOẶC tổn thất luỹ kế **> 60 triệu** (20% giá trị đội máy) trong 12 tháng | **Dừng mở rộng đội máy**; bắt buộc gói An Tâm cho mọi lượt thuê; xem xét thanh lý bớt máy |

---

## 7. BẢNG THAM SỐ RỦI RO & KẾT QUẢ TÍNH TOÁN

### 7.1. Tham số nền (GIẢ ĐỊNH — phải thay bằng số thật của nhóm)

| Ký hiệu | Tham số | Giá trị dùng trong mô hình | Nguồn |
|---|---|---|---|
| N | Số máy trong đội | **25 máy** | GĐ — giữa khoảng 15–40 |
| V | Giá trị thay thế mỗi máy | **12.000.000đ** | 🔴 **GĐ — LẤY TỪ FILE NGHIÊN CỨU PHẦN CỨNG CỦA NHÓM** |
| A | Tổng giá trị đội máy | **300.000.000đ** | = N × V |
| R | Số lượt thuê/máy/năm | **18 lượt** | 🔴 **GĐ — lấy từ file nghiên cứu nhu cầu/lịch thi FPT** |
| n | Tổng lượt thuê/năm | **450 lượt** | = N × R |
| d | Số ngày TB mỗi lượt | **3 ngày** | GĐ — đợt thi thường 2–5 ngày |
| — | Tổng ngày-máy/năm | **1.350 ngày-máy** | = n × d |
| C | Tiền cọc | **2.000.000đ/lượt** | GĐ — đề xuất |
| D | Mức miễn thường gói An Tâm | **500.000đ/vụ** | Đề xuất (xem 5.3) |
| r | Tỷ lệ thu hồi được từ khách (không có gói) | **80%** | GĐ — 20% không đòi được/tranh chấp |
| p | Giá thuê | **50.000đ/ngày** → 150.000đ/lượt | 🔴 **GĐ — lấy từ file nghiên cứu giá của nhóm** |
| — | Doanh thu thuê/năm | **67.500.000đ** | = n × 150.000 |

### 7.2. Bảng tần suất & mức độ tổn thất (🔴 TOÀN BỘ LÀ GIẢ ĐỊNH — KHÔNG CÓ NGUỒN)

**Tần suất tính trên 100 lượt thuê:**

| # | Hiểm hoạ | Thấp | **Cơ sở** | Cao | Tổn thất TB (đ/vụ) | Nhóm |
|---|---|---|---|---|---|---|
| 1 | Vỡ / nứt màn hình | 0,20 | **0,45** | 0,90 | 2.500.000 | B — Khách gây ra |
| 2 | Đổ nước / hỏng bàn phím | 0,60 | **1,20** | 2,40 | 800.000 | B |
| 3 | Gãy bản lề, nứt vỏ | 0,25 | **0,50** | 1,00 | 1.200.000 | B |
| 4 | Hỏng SSD do va đập | 0,10 | **0,25** | 0,50 | 1.000.000 | B |
| 5 | Hỏng mainboard / mạch nguồn | 0,10 | **0,20** | 0,40 | 3.500.000 | B |
| 6 | Mất / hỏng sạc & phụ kiện | 1,50 | **3,00** | 6,00 | 350.000 | B |
| 7 | **Mất máy / khách không trả** | 0,05 | **0,15** | 0,40 | 12.000.000 | **C — Thảm hoạ** |
| 8 | Chai pin (hao mòn) | — | **3,00** | — | 900.000 | **W — Vận hành, KHÔNG tính khách** |
| 9 | Trầy xước, hao mòn nhẹ | — | ~20 | — | 0 | W — Bỏ qua |

> 🔴 **BẮT BUỘC ĐỌC:** bảng này là **ước lượng chuyên gia của nhóm**, KHÔNG dựa trên bất kỳ nguồn nào. Ngân sách tìm kiếm hết trước khi tra được: (a) loss rate / shrinkage của ngành equipment rental, (b) annual failure rate của laptop. Xem Phần 12 để biết cách kiểm chứng.

**Đọc lại bằng ngôn ngữ thường (kịch bản Cơ sở, 450 lượt/năm, 25 máy):**
- 0,45/100 vỡ màn hình → **≈ 2 màn hình vỡ mỗi năm** trên 25 máy (8% đội máy/năm)
- 1,20/100 đổ nước/bàn phím → **≈ 5,4 vụ/năm**
- 3,00/100 mất sạc → **≈ 13,5 cục sạc/năm** (nhiều nhất về số vụ, ít nhất về tiền)
- 0,15/100 mất máy → **≈ 0,68 máy/năm**, tức **cứ ~1,5 năm mất 1 máy**
👉 Nhóm hãy tự hỏi: những con số này có **hợp lý** với thực tế sinh viên FPT không? Nếu thấy quá cao/thấp, sửa lại rồi tính lại.

### 7.3. Tính toán — Kịch bản CƠ SỞ

**Bước 1 — Tần suất năm (λ = n × f), n = 450 lượt**

| # | Hiểm hoạ | f (/lượt) | λ (vụ/năm) | s (đ) | λ×s (đ/năm) | λ×s² |
|---|---|---|---|---|---|---|
| 1 | Vỡ màn hình | 0,0045 | 2,025 | 2.500.000 | **5.062.500** | 1,2656 × 10¹³ |
| 2 | Nước / bàn phím | 0,0120 | 5,400 | 800.000 | **4.320.000** | 3,456 × 10¹² |
| 3 | Bản lề / vỏ | 0,0050 | 2,250 | 1.200.000 | **2.700.000** | 3,240 × 10¹² |
| 4 | SSD | 0,0025 | 1,125 | 1.000.000 | **1.125.000** | 1,125 × 10¹² |
| 5 | Mainboard | 0,0020 | 0,900 | 3.500.000 | **3.150.000** | 1,1025 × 10¹³ |
| 6 | Sạc / phụ kiện | 0,0300 | 13,500 | 350.000 | **4.725.000** | 1,654 × 10¹² |
| | **Cộng nhóm B** | | **25,20** | | **21.082.500** | 3,3156 × 10¹³ |
| 7 | **Mất máy (gộp)** | 0,0015 | 0,675 | 12.000.000 | **8.100.000** | 9,720 × 10¹³ |
| | **TỔNG GỘP** | | **25,875** | | **29.182.500** | **1,30356 × 10¹⁴** |

**Bước 2 — Tổn thất kỳ vọng & độ biến động (trước mọi thu hồi)**
```
  E[L]  = 29.182.500 đ/năm                    ← 9,7% giá trị đội máy
  Var(L)= 1,30356 × 10¹⁴
  σ(L)  = √(1,30356 × 10¹⁴) = 11.417.000 đ    ← Hệ số biến thiên CV = 0,39
```
> 📌 **Quan sát quan trọng**: hiểm hoạ **mất máy** chỉ chiếm **28%** tổn thất kỳ vọng (8,1/29,2 tr) nhưng chiếm tới **75% phương sai** (9,72/13,04 × 10¹³). → **Mất máy là nguồn rủi ro đuôi lớn nhất**. Giảm rủi ro này (bằng cọc + xác minh danh tính) có tác dụng ổn định tài chính **lớn hơn nhiều** so với giảm rủi ro vỡ màn hình.

**Bước 3 — Tổn thất RÒNG doanh nghiệp thực gánh (sau thu hồi từ khách)**

| Nguồn tổn thất | Cách tính | Số tiền (đ/năm) |
|---|---|---|
| (a) Bồi thường cho khách **CÓ** gói An Tâm (35%) | 450 × 35% × 23.350đ | **3.677.625** |
| (b) Phần **không đòi được** từ khách KHÔNG có gói (65%, thất thu 20%) | 450 × 65% × 46.850đ × 20% | **2.740.725** |
| (c) Mất máy — **ròng sau trừ cọc 2 tr** | 0,675 vụ × (12.000.000 − 2.000.000) | **6.750.000** |
| | **TỔNG TỔN THẤT RÒNG E[L_ròng]** | **13.168.350** |
| | *(Ghi nhớ: chai pin 13,5 × 900.000 = 12.150.000đ/năm đi vào CHI PHÍ BẢO TRÌ, không vào quỹ rủi ro)* | |

**Bước 4 — Độ biến động của tổn thất ròng**
```
  Phương sai phần thảm hoạ (mất máy, ròng 10 tr/vụ):
      0,675 × (10.000.000)²  =  6,750 × 10¹³

  Phương sai phần thường (nhóm B), sau khi nhân hệ số chuyển giao hiệu dụng
      k = 0,35 × 0,50  +  0,65 × 0,20  =  0,305
      → nhân phương sai với k² = 0,093
      0,093 × 3,3156 × 10¹³  =  0,308 × 10¹³

  Var(L_ròng) ≈ 7,058 × 10¹³
  σ(L_ròng)   ≈ 8.401.000 đ
```

**Bước 5 — 🎯 QUY MÔ QUỸ DỰ PHÒNG**
```
  QUỸ(95%) = E[L_ròng] + 1,645 × σ(L_ròng)
           = 13.168.350 + 1,645 × 8.401.000
           = 13.168.350 + 13.819.645
           = 26.987.995 đ   ≈  27 TRIỆU ĐỒNG
```
| Mức tin cậy | z | Quy mô quỹ | % giá trị đội máy |
|---|---|---|---|
| 90% | 1,282 | 23.938.000đ | 8,0% |
| **95%** ✅ | **1,645** | **26.988.000đ** | **9,0%** |
| 99% | 2,326 | 32.709.000đ | 10,9% |
| 95% + hệ số lệch đuôi ×1,2 | — | 32.386.000đ | 10,8% |

> ✅ **KHUYẾN NGHỊ: Quỹ dự phòng rủi ro mục tiêu = 27.000.000đ (làm tròn 30.000.000đ cho an toàn) ≈ 9–10% giá trị đội máy.**

### 7.4. 🎯 Phí miễn trừ thiệt hại nên thu

**Phí thuần (D = 500.000đ), tính trên 100 lượt:**

| # | Hiểm hoạ | f/100 | Tổn thất gộp (đ) | Khách giữ lại min(s, D) (đ) | **DN gánh (đ)** |
|---|---|---|---|---|---|
| 1 | Vỡ màn hình | 0,45 | 1.125.000 | 0,45 × 500.000 = 225.000 | **900.000** |
| 2 | Nước / bàn phím | 1,20 | 960.000 | 1,20 × 500.000 = 600.000 | **360.000** |
| 3 | Bản lề / vỏ | 0,50 | 600.000 | 0,50 × 500.000 = 250.000 | **350.000** |
| 4 | SSD | 0,25 | 250.000 | 0,25 × 500.000 = 125.000 | **125.000** |
| 5 | Mainboard | 0,20 | 700.000 | 0,20 × 500.000 = 100.000 | **600.000** |
| 6 | Sạc / phụ kiện (350k < 500k) | 3,00 | 1.050.000 | 3,00 × 350.000 = 1.050.000 | **0** |
| | **CỘNG** | **5,60** | **4.685.000** | **2.350.000** | **2.335.000** |

```
  Phí thuần    = 2.335.000 / 100 lượt  =  23.350 đ/lượt

  Phí niêm yết = 23.350 × 1,15 × 1,25 × 1,20
               = 23.350 × 1,725
               = 40.279 đ/lượt      →  làm tròn 40.000 đ/lượt
               = 13.426 đ/ngày      →  làm tròn 15.000 đ/ngày
```

> ✅ **KHUYẾN NGHỊ NIÊM YẾT:**
> | Hình thức bán | Giá | Điều kiện |
> |---|---|---|
> | Theo ngày | **15.000đ/ngày** | Mức miễn thường 500.000đ/vụ |
> | **Trọn gói đợt thi** ⭐ | **40.000đ** | Cho lượt thuê ≤ 4 ngày. Nên làm mặc định — dễ hiểu, dễ bán |
> | Gói dài (5–10 ngày) | **80.000đ** | |

**Kiểm tra tính hợp lý:**
- Phí gói = 40.000đ / giá thuê 150.000đ = **26,7% giá thuê cơ bản** → nằm trong khoảng thông thường của ngành cho thuê xe (⚠️ *khoảng này là kiến thức nền, CHƯA có nguồn xác minh trong phiên — cần tra lại*).
- Phí gói = 40.000đ / giá trị máy 12.000.000đ = **0,33% giá trị máy cho 3 ngày**. Quy năm (×18 lượt) = **6,0%/năm** — cao hơn 4–9 lần mức bán lẻ cá nhân 0,6–2,6% (mục 3.2). Hợp lý, vì rủi ro cho thuê cao hơn hẳn.

### 7.5. Độ nhạy theo 3 kịch bản tần suất

| Chỉ tiêu | Thấp | **Cơ sở** | Cao |
|---|---|---|---|
| Tổn thất gộp E[L] (đ/năm) | ~13.900.000 | **29.182.500** | ~58.400.000 |
| % giá trị đội máy | 4,6% | **9,7%** | 19,5% |
| Tổn thất ròng E[L_ròng] (đ/năm) | ~6.200.000 | **13.168.350** | ~28.900.000 |
| σ(L_ròng) (đ) | ~5.000.000 | **8.401.000** | ~13.700.000 |
| **Quỹ dự phòng (95%)** | **~14.400.000đ** | **~27.000.000đ** | **~51.500.000đ** |
| Phí thuần DW (đ/lượt) | ~11.100 | **23.350** | ~48.900 |
| **Phí DW niêm yết (đ/lượt)** | **~19.000đ** | **~40.000đ** | **~84.000đ** |
| Số máy mất/năm | 0,23 | **0,68** | 1,80 |

> ⚠️ **Kịch bản Cao là kịch bản đáng lo**: tổn thất 19,5% giá trị đội máy/năm và cần quỹ 51,5 triệu (17% giá trị đội máy). Nếu proposal có phần phân tích hoà vốn, **PHẢI chạy cả kịch bản này** — nó có thể xoá sạch lợi nhuận.

### 7.6. Kế hoạch nạp quỹ

| Nguồn | Tỷ lệ | Số tiền/năm | Ghi chú |
|---|---|---|---|
| Vốn mồi từ vốn đầu tư ban đầu | — | **11.000.000đ** | ≈ 40% quỹ mục tiêu, nạp ngay ngày khai trương. **Không được bỏ qua** — mùa thi đầu tiên đã có rủi ro |
| Trích từ doanh thu thuê | **10%** | 6.750.000đ | 10% × 67.500.000đ |
| 100% phí gói An Tâm | 100% | 6.300.000đ | Ở take-up 35% |
| **Tổng nạp/năm** | | **13.050.000đ** | ≈ **bằng tổn thất ròng kỳ vọng 13.168.350đ** ✅ |

**Diễn giải:** dòng tiền vào quỹ (13,05 tr) ≈ dòng tiền ra kỳ vọng (13,17 tr) → quỹ **ở trạng thái cân bằng ổn định**. Vốn mồi 11 triệu đóng vai trò **đệm chống biến động năm đầu**. Sau 2–3 năm không có sự cố lớn, quỹ sẽ tự tích tụ lên mức mục tiêu 27 triệu và có thể giảm tỷ lệ trích xuống 6–7%.

**Quy tắc vận hành quỹ:**
1. Mở **tài khoản ngân hàng riêng**, không dùng chung tài khoản vận hành.
2. Ghi sổ mọi khoản vào/ra, đối chiếu hằng tháng.
3. **Chỉ được chi** cho: sửa chữa do hư hỏng, mua máy thay thế khi mất máy, phần bồi thường cho gói An Tâm. **Không được chi** cho marketing, lương, mở rộng.
4. Nạp lại đầy trong **60 ngày** sau mỗi lần chi lớn.
5. Báo cáo số dư quỹ trong họp nhóm hằng tháng.

---

## 8. CHI PHÍ SỬA CHỮA LAPTOP — KHUNG KHẢO SÁT

> ### ❌ PHẦN NÀY HOÀN TOÀN CHƯA CÓ DỮ LIỆU THỊ TRƯỜNG
> Ngân sách WebSearch hết trước khi tra được bảng giá sửa laptop tại Đà Nẵng/VN 2025–2026. **Các con số dùng ở Phần 7 (2.500.000đ màn hình, 800.000đ bàn phím, v.v.) là GIẢ ĐỊNH của nhóm, KHÔNG có nguồn.** Đây là **rủi ro lớn nhất về độ chính xác của toàn bộ mô hình** — vì `s_i` vào thẳng công thức tổn thất kỳ vọng.

### 8.1. Bảng khảo sát cần điền (in ra, mang đi hỏi giá)

**Dòng máy cần hỏi:** chọn đúng 2–3 dòng nhóm dự định mua (điền vào cột "Dòng máy").

| Hạng mục sửa | Dòng máy 1: ______ | Dòng máy 2: ______ | Dòng máy 3: ______ | Thời gian sửa | Có bảo hành sửa? |
|---|---|---|---|---|---|
| Thay **màn hình** (LCD 14"/15,6" HD) | | | | | |
| Thay **màn hình** (LCD FHD IPS) | | | | | |
| Thay **bàn phím** (nguyên bộ) | | | | | |
| Vệ sinh **đổ nước** (không thay linh kiện) | | | | | |
| Thay **pin** (pin zin / pin thay thế) | | | | | |
| Thay/hàn **bản lề** | | | | | |
| Thay **vỏ A / vỏ C** | | | | | |
| Sửa **mainboard** (lỗi nguồn) | | | | | |
| **Thay mainboard** | | | | | |
| Thay **SSD 256GB / 512GB** | | | | | |
| Thay **RAM 8GB / 16GB** | | | | | |
| Thay **sạc** (adapter chính hãng / thay thế) | | | | | |
| Thay **bản lề + vỏ** (combo) | | | | | |
| **Vệ sinh + tra keo tản nhiệt** (bảo trì định kỳ) | | | | | |

### 8.2. Kênh khảo sát (theo thứ tự ưu tiên)

| # | Kênh | Cách tiếp cận | Ưu | Nhược |
|---|---|---|---|---|
| 1 | **Cửa hàng sửa laptop tư nhân khu Hoà Hải / Ngũ Hành Sơn / Hải Châu (ĐN)** | Đi trực tiếp hoặc gọi. Tìm Google Maps: *"sửa laptop Ngũ Hành Sơn Đà Nẵng"*, *"thay màn hình laptop Đà Nẵng"* | Rẻ nhất, nhanh nhất, gần trường, **có thể đàm phán hợp đồng đối tác giá sỉ** | Chất lượng linh kiện không đồng đều |
| 2 | **Trung tâm bảo hành uỷ quyền hãng tại ĐN** (Dell/HP/Lenovo/Asus/Acer) | Hỏi giá thay linh kiện ngoài bảo hành | Linh kiện zin, có hoá đơn | Đắt, chậm |
| 3 | **FPT Services / FPT Shop ĐN** | Đã xác minh: **SLA 48h tại Đà Nẵng** ([nguồn](https://fptshop.com.vn/tin-tuc/tin-khuyen-mai/goi-bao-hanh-roi-vo-dien-thoai-laptop-tai-fpt-shop-gia-chi-tu-79000-dong-137045)) | Có mạng lưới, minh bạch | Đắt hơn tư nhân |
| 4 | **TGDĐ / Điện Máy Xanh / CellphoneS ĐN** | Xem chính sách bảo hành công bố ([dmx](https://www.dienmayxanh.com/kinh-nghiem-hay/chinh-sach-bao-hanh-nhom-hang-dien-thoai-laptop-sm-773940)) | Chuẩn hoá | Chỉ nhận máy mua tại chuỗi |
| 5 | **Cửa hàng máy tính chuyên laptop cũ** (tham khảo chính sách bảo hành: [no1computer.vn](https://no1computer.vn/bao-hanh.html)) | Xem điều khoản bảo hành máy cũ | Hiểu được mức bảo hành khi mua máy | — |
| 6 | **Shopee / Lazada / Tiki** | Tra giá **linh kiện rời** (màn hình, bàn phím, pin) để biết giá sàn | Biết giá vật tư → đàm phán công thợ | Không tính công |

### 8.3. 🔑 Khuyến nghị chiến lược quan trọng: KÝ HỢP ĐỒNG XƯỞNG SỬA ĐỐI TÁC

Đây là biện pháp **giảm chi phí rủi ro hiệu quả nhất**, nên đưa vào proposal:

**Nội dung đàm phán với 1 cửa hàng sửa laptop gần trường:**
| Điều khoản | Mục tiêu |
|---|---|
| **Bảng giá cố định** cho 10 hạng mục sửa phổ biến, cam kết 12 tháng | Loại bỏ rủi ro biến động giá → tham số `s_i` trở nên chắc chắn |
| **Chiết khấu sỉ 15–25%** đổi lấy cam kết đưa toàn bộ máy hỏng | Giảm trực tiếp tổn thất kỳ vọng E[L] |
| **SLA sửa ưu tiên ≤ 24h trong mùa thi** | Quan trọng hơn cả giá — xem Phần 9 |
| **Công nợ 30 ngày** | Giảm áp lực dòng tiền lên quỹ |
| **Báo giá trước khi sửa**, không tự ý phát sinh | Chống phát sinh chi phí |

> 💡 **Tác động lên mô hình**: nếu đàm phán được chiết khấu 20%, tổn thất kỳ vọng nhóm B giảm từ 21,08 tr → **16,87 tr/năm**, quỹ dự phòng giảm khoảng **2,5–3 triệu**, và phí gói An Tâm có thể hạ xuống ~33.000đ/lượt (dễ bán hơn).

### 8.4. Tỉ lệ hư hỏng laptop (Annual Failure Rate) — CHƯA XÁC MINH

> 🔴 **KHÔNG CÓ SỐ LIỆU XÁC MINH.** Các nguồn thường được ngành trích dẫn mà nhóm **cần tự tra**:
> - **SquareTrade** — nghiên cứu về tỷ lệ hỏng laptop theo hãng trong 2–3 năm sử dụng (nghiên cứu cũ, cần tìm bản cập nhật).
> - **Rescuecom Computer Reliability Report** — xếp hạng độ tin cậy theo hãng, cập nhật hằng năm.
> - **Laptop Mag Tech Support Showdown** — đánh giá hỗ trợ & độ bền.
> - **Gartner / IDC** — báo cáo TCO (tổng chi phí sở hữu) thiết bị đầu cuối, có mục failure rate & chi phí sửa chữa.
> - Từ khoá tra cứu: `laptop annual failure rate 2025`, `notebook AFR statistics`, `equipment rental loss rate shrinkage percentage`, `tool rental industry loss ratio`.
>
> ⚠️ **Cảnh báo quan trọng khi dùng các số này**: AFR của laptop công bố là cho **1 người dùng sở hữu, dùng tại nhà/văn phòng**. Mô hình cho thuê có **hồ sơ rủi ro hoàn toàn khác**: máy đổi tay 15–20 lần/năm, luôn phải di chuyển, người dùng không sở hữu. **Không được lấy AFR tiêu dùng áp thẳng vào mô hình cho thuê.** Dùng nó làm **cận dưới (lower bound)**, rồi nhân hệ số điều chỉnh.

---

## 9. RỦI RO VẬN HÀNH ĐẶC THÙ

### 9.1. 🔴 Rủi ro #1: TẬP TRUNG THEO MÙA (Peak Concentration Risk) — nghiêm trọng nhất

**Vấn đề:** toàn bộ nhu cầu dồn vào 1–2 tuần thi mỗi kỳ. Trong tuần đó:
- **100% đội máy được thuê cùng lúc** → **KHÔNG CÒN MÁY DỰ PHÒNG**
- Một máy hỏng giữa tuần thi = **không có máy thay** = sinh viên **không thi được** = thảm hoạ về danh tiếng (và mạng lưới sinh viên FPT lan tin cực nhanh)
- Đưa máy đi sửa: **SLA nhanh nhất đo được tại Đà Nẵng là 48h** ([FPT Shop](https://fptshop.com.vn/tin-tuc/tin-khuyen-mai/goi-bao-hanh-roi-vo-dien-thoai-laptop-tai-fpt-shop-gia-chi-tu-79000-dong-137045)) → **quá chậm**, kỳ thi đã kết thúc

**Đây là rủi ro mà TIỀN KHÔNG GIẢI QUYẾT ĐƯỢC — nó là rủi ro dịch vụ, không phải rủi ro tài sản.**

**Biện pháp bắt buộc:**

| Biện pháp | Chi tiết | Chi phí |
|---|---|---|
| **Đệm máy dự phòng 15%** | Với 25 máy cho thuê → giữ thêm **4 máy KHÔNG BAO GIỜ cho thuê** trong mùa thi | 4 × 12 tr = **48 triệu vốn** (⚠️ khoản này phải vào bảng vốn đầu tư của proposal) |
| **Cam kết "Đổi máy trong 60 phút"** | Biến điểm yếu thành **USP marketing mạnh nhất** của dự án | Gần 0đ — chỉ cần có máy dự phòng + người trực |
| **Trực 24/7 trong tuần thi** | Hotline/Zalo, có người ở gần trường | Lương/phụ cấp mùa vụ |
| **Sửa chữa hoãn sang sau mùa thi** | Máy hỏng nhẹ vẫn chạy được → dồn sửa vào kỳ nghỉ | Giảm chi phí sửa gấp |
| **Kiểm tra kỹ trước khi giao** | Chạy thử EOS + SEB, test pin, test bàn phím, test mạng ngay tại quầy | Thời gian |

> 💡 **Gợi ý cho proposal**: Cam kết "Đổi máy trong 60 phút, miễn phí" là điều **không đối thủ cho thuê chung chung nào làm được**, và nó trực tiếp giải quyết nỗi sợ lớn nhất của khách hàng (trượt môn vì hỏng máy). Đây nên là dòng đầu tiên trên trang chủ.

### 9.2. 🔴 Rủi ro #2: LỖI PHẦN MỀM EOS + SAFE EXAM BROWSER

Đây là rủi ro **đặc thù duy nhất có của mô hình này** — và cũng là rào cản gia nhập ngành (nếu làm tốt).

| Rủi ro | Hậu quả | Biện pháp phòng ngừa |
|---|---|---|
| **Windows Update tự chạy giữa giờ thi** | Máy restart → mất bài thi | **Tắt/hoãn Windows Update**; đặt Active Hours; dùng Group Policy hoặc `sc config wuauserv start=disabled` trên bản Pro |
| **SEB không khởi động / báo lỗi cấu hình** | Không vào được phòng thi | **Cài sẵn & test SEB trước mỗi lượt giao**; lưu file cấu hình chuẩn |
| **Phần mềm diệt virus chặn SEB** | SEB bị kill | Gỡ AV bên thứ ba, chỉ dùng Windows Defender với ngoại lệ cho SEB |
| **Máy ngủ đông / sleep giữa giờ thi** | Mất kết nối, SEB thoát | Đặt Power Plan = **High Performance, không bao giờ sleep**; tắt Fast Startup |
| **Máy hết pin giữa giờ thi** | Mất bài | **Bắt buộc giao kèm sạc**; test dung lượng pin (>70% health) trước khi giao; dán nhãn "CẮM SẠC KHI THI" |
| **Wi-Fi/driver mạng lỗi** | Không nộp được bài | Test kết nối Wi-Fi trường trước khi giao |
| **Khách cài phần mềm lạ / đổi cấu hình** | Máy hỏng, mất chuẩn | **Tài khoản khách KHÔNG có quyền admin**; dùng tài khoản local standard |
| **Dữ liệu cá nhân khách còn lại trên máy** | Rủi ro quyền riêng tư | **Ghi đè lại image chuẩn sau MỖI lượt trả máy** |

**Giải pháp kỹ thuật xương sống — "GOLDEN IMAGE":**
```
  1. Cấu hình 1 máy chuẩn hoàn hảo: Windows + EOS + SEB + driver + tắt update + power plan
  2. Tạo bản sao ổ đĩa (disk image) bằng Macrium Reflect Free / Clonezilla
  3. Lưu image lên ổ cứng ngoài
  4. Sau MỖI lượt trả máy → ghi đè image (15–25 phút/máy)

  Lợi ích:
    ✅ Mọi máy giao ra đều ở trạng thái ĐÃ KIỂM CHỨNG chạy được EOS+SEB
    ✅ Xoá sạch dữ liệu cá nhân khách trước  → an toàn quyền riêng tư
    ✅ Loại bỏ gần như toàn bộ sự cố phần mềm  → giảm mạnh chi phí hỗ trợ
    ✅ Máy "hỏng phần mềm" khôi phục trong 20 phút thay vì mang đi sửa
```
> 📌 Chi phí: 1 ổ cứng ngoài 1TB + phần mềm miễn phí. **Đây là khoản đầu tư có ROI cao nhất trong toàn bộ dự án về mặt quản trị rủi ro.**

### 9.3. Rủi ro #3: MẤT MÁY / KHÁCH KHÔNG TRẢ (rủi ro đuôi lớn nhất về tài chính)

Như đã tính ở 7.3: chiếm **75% phương sai** dù chỉ 28% tổn thất kỳ vọng.

| Lớp kiểm soát | Biện pháp | Hiệu quả ước tính |
|---|---|---|
| **Sàng lọc trước** | Xác minh **MSSV còn hiệu lực** (yêu cầu ảnh chụp thẻ SV + đăng nhập tài khoản trường trước mặt nhân viên); đối chiếu **CCCD** (chụp ảnh, **KHÔNG giữ bản gốc** — xem 10.2); lưu **SĐT + Zalo + Facebook** | Cao — sinh viên có danh tính xác minh được rất khó "biến mất" |
| **Đặt cọc** | **2.000.000đ** tiền mặt/chuyển khoản | Giảm tổn thất ròng mỗi vụ từ 12 tr → 10 tr (17%) |
| **Cọc bậc thang** | Khách lần đầu: cọc 2 tr. Khách đã thuê ≥2 lần trả tốt: cọc 1 tr. Khách được bạn giới thiệu: cọc 1,5 tr | Tăng chuyển đổi mà không tăng rủi ro |
| **Định vị thiết bị** | Bật **Windows Find My Device**; cài **Prey Project** (miễn phí tới 3 thiết bị) | Trung bình — hỗ trợ thu hồi |
| **Ghi serial** | Ghi **Service Tag / Serial Number** vào hợp đồng; dán **tem niêm phong** có số | Cao — chống tráo máy, hỗ trợ trình báo công an |
| **Mã hoá ổ đĩa** | BitLocker | Bảo vệ dữ liệu, không chống mất máy |
| **Hạn mức** | Mỗi khách tối đa **1 máy/lượt** | Chặn rủi ro mất nhiều máy cùng lúc |
| **Cảnh báo quá hạn** | Nhắc Zalo tự động tại T-1 ngày, T+0, T+1; liên hệ trực tiếp từ T+2 | Giảm quá hạn do quên |

> 📊 **Định lượng tác động của tiền cọc**: nâng cọc từ 2 tr → 3 tr làm giảm tổn thất ròng mất máy từ 6,75 tr → **6,075 tr/năm** (−10%) và giảm quỹ dự phòng khoảng **1,5 triệu**. **Nhưng** cọc cao làm giảm tỷ lệ chuyển đổi khách sinh viên (nhóm có sẵn ít tiền mặt). ⚠️ **Cần khảo sát mức cọc chấp nhận được với sinh viên FPT** — đây là câu hỏi nên có trong bảng hỏi khảo sát của nhóm.

### 9.4. Rủi ro #4: Biên bản bàn giao — chống tranh chấp

**Quy trình bàn giao chuẩn (bắt buộc, cả 2 chiều):**
```
  GIAO MÁY                                  NHẬN MÁY
  ─────────────────────────────             ─────────────────────────────
  1. Chụp 6 ảnh: mặt A, B, C, D,            1. Chụp lại đúng 6 góc đó
     màn hình đang bật, 4 góc cạnh          2. So sánh trực tiếp với ảnh giao
  2. Quay video 30 giây: mở/gập máy,        3. Bật máy, test bàn phím
     gõ thử bàn phím, chụp màn hình         4. Kiểm tra đủ phụ kiện
  3. Ghi: Serial, % pin, tình trạng          5. Ký biên bản nhận
     trầy xước hiện có                      6. Xử lý cọc:
  4. Kiểm đủ phụ kiện (sạc, túi)               - Không hư hỏng → hoàn 100%
  5. Chạy thử EOS + SEB TRƯỚC MẶT KHÁCH        - Có hư hỏng → lập biên bản,
  6. Khách ký biên bản + ký xác nhận              báo giá, trừ cọc
     ĐÃ XEM ảnh/video                       7. Ghi đè Golden Image
  7. Lưu tất cả vào Google Drive theo
     mã đơn hàng
```
> 🔑 **Ảnh/video bàn giao là bằng chứng quyết định trong mọi tranh chấp.** Không có nó, doanh nghiệp sẽ thua mọi lần khách nói "máy đã trầy sẵn rồi". Đây là biện pháp **chi phí 0đ nhưng giá trị cao nhất** trong toàn bộ danh mục kiểm soát rủi ro.

---

## 10. RỦI RO PHÁP LÝ & THIẾT KẾ HỢP ĐỒNG

> ⚠️ **Phần này CHƯA được kiểm chứng bằng nguồn trong phiên** (hết ngân sách search). Các viện dẫn điều luật là **theo trí nhớ, PHẢI tra cứu lại** trên [thuvienphapluat.vn](https://thuvienphapluat.vn) hoặc hỏi giảng viên môn Luật.

### 10.1. Khung pháp lý cần tra cứu

| Chủ đề | Văn bản cần tra | Trạng thái |
|---|---|---|
| Hợp đồng thuê tài sản | **Bộ luật Dân sự 2015** — mục về hợp đồng thuê tài sản (nghĩa vụ bảo quản, trả lại tài sản, bồi thường hư hỏng) | 🔴 Cần tra số điều chính xác |
| Đặt cọc | **Bộ luật Dân sự 2015** — điều về đặt cọc (quyền xử lý cọc khi bên đặt cọc vi phạm) | 🔴 Cần tra số điều chính xác |
| Đăng ký hộ kinh doanh | Nghị định về đăng ký doanh nghiệp; mã ngành **cho thuê máy móc, thiết bị** (VSIC 7730) | 🔴 Cần tra |
| Thuế hộ kinh doanh | Ngưỡng doanh thu chịu thuế GTGT/TNCN đối với hộ kinh doanh (mốc mới nhất 2026) | 🔴 Cần tra — **quan trọng cho bảng tài chính** |
| Bảo vệ dữ liệu cá nhân | Nghị định về bảo vệ dữ liệu cá nhân — nghĩa vụ khi thu thập ảnh CCCD | 🔴 Cần tra |
| Kinh doanh bảo hiểm | **Luật Kinh doanh bảo hiểm** — để xác nhận gói "Miễn trừ thiệt hại" KHÔNG bị coi là kinh doanh bảo hiểm | 🔴 **QUAN TRỌNG NHẤT — phải xác nhận** |

### 10.2. ⚠️ CẢNH BÁO: KHÔNG GIỮ BẢN GỐC CCCD/CMND CỦA KHÁCH

Nhiều mô hình cho thuê tại VN có thói quen **giữ CCCD gốc làm tin**. Đây là thực hành **có rủi ro pháp lý**:
- Giấy tờ tuỳ thân do Nhà nước cấp, việc cá nhân/tổ chức không có thẩm quyền **giữ lại** có thể bị xem là hành vi vi phạm.
- Khách mất CCCD trong lúc doanh nghiệp giữ → trách nhiệm thuộc doanh nghiệp.
- Khách có thể khiếu nại, ảnh hưởng danh tiếng trong cộng đồng sinh viên.

✅ **Thay thế an toàn:** **chụp ảnh CCCD** (2 mặt) + **xác minh MSSV trực tiếp** + **đặt cọc tiền** + **lưu số Zalo/Facebook**. Có thông báo rõ ràng về mục đích thu thập & thời hạn lưu trữ ảnh CCCD, và **xoá sau khi kết thúc hợp đồng**.
🔴 *Cần xác nhận lại với giảng viên Luật — chưa tra được văn bản.*

### 10.3. Các điều khoản BẮT BUỘC có trong hợp đồng thuê

| # | Điều khoản | Nội dung tối thiểu |
|---|---|---|
| 1 | **Nhận dạng tài sản** | Hãng, model, **Serial/Service Tag**, cấu hình, tình trạng khi giao (kèm phụ lục ảnh) |
| 2 | **Thời hạn thuê** | Ngày giờ giao — ngày giờ trả cụ thể; **phí quá hạn** (đề xuất 150% giá thuê ngày) |
| 3 | **Giá & thanh toán** | Giá thuê, phí gói An Tâm (nếu có), tiền cọc, phương thức, thời điểm hoàn cọc |
| 4 | **Nghĩa vụ bảo quản của bên thuê** | Không cho thuê lại, không tháo linh kiện, không cài phần mềm bẻ khoá, giữ nguyên tem niêm phong |
| 5 | **Trách nhiệm khi hư hỏng** | Nêu rõ 2 mức: có gói An Tâm (tối đa 500.000đ/vụ) vs không có gói (100% chi phí sửa thực tế) |
| 6 | **Trách nhiệm khi mất máy** | **100% giá trị thay thế**, trừ cọc. **Ghi rõ gói An Tâm KHÔNG áp dụng cho mất máy** |
| 7 | **Loại trừ của gói An Tâm** | Mất máy, trộm cắp, cố ý phá hoại, cho người khác thuê lại, tháo linh kiện, ngâm nước hoàn toàn, cháy nổ |
| 8 | **Hao mòn tự nhiên** | Doanh nghiệp chịu — **không tính tiền khách** (điều này tạo thiện chí & giảm tranh chấp) |
| 9 | **Quy trình giám định & báo giá** | Phải báo giá trước khi sửa, khách được xem hoá đơn sửa chữa |
| 10 | **Dữ liệu cá nhân** | Máy sẽ được **xoá sạch và cài lại** sau khi trả — khách tự sao lưu dữ liệu, doanh nghiệp không chịu trách nhiệm mất dữ liệu |
| 11 | **Giới hạn trách nhiệm của bên cho thuê** | Bên cho thuê **không chịu trách nhiệm về kết quả thi** của khách; trách nhiệm tối đa = hoàn tiền thuê + cung cấp máy thay thế |
| 12 | **Giải quyết tranh chấp** | Thương lượng trước; căn cứ là biên bản bàn giao có ảnh/video |

> ⚠️ **Điều khoản #11 rất quan trọng**: nếu máy hỏng khiến sinh viên trượt môn, khách có thể đòi bồi thường học phí học lại (vài triệu đồng). **Phải giới hạn rõ trách nhiệm** trong hợp đồng.

---

## 11. MA TRẬN RỦI RO TỔNG HỢP

**Thang: Khả năng 1 (rất thấp) – 5 (rất cao); Tác động 1 (không đáng kể) – 5 (thảm hoạ). Điểm = KN × TĐ.**

| # | Rủi ro | KN | TĐ | Điểm | Mức | Biện pháp chính | Rủi ro còn lại |
|---|---|---|---|---|---|---|---|
| R1 | **Máy hỏng giữa mùa thi, không có máy thay** | 4 | 5 | **20** | 🔴 Rất cao | Đệm 4 máy dự phòng (15%); cam kết đổi máy 60 phút; trực 24/7 mùa thi | 🟡 Trung bình |
| R2 | **Lỗi EOS/SEB không chạy được khi thi** | 4 | 5 | **20** | 🔴 Rất cao | Golden Image; test EOS+SEB trước mặt khách khi giao; tắt Windows Update; tài khoản không admin | 🟢 Thấp |
| R3 | **Khách không trả máy / mất máy** | 2 | 5 | **10** | 🟠 Cao | Cọc 2 tr; xác minh MSSV; ghi serial; Prey/Find My Device; quỹ dự phòng | 🟡 Trung bình |
| R4 | **Tham số mô hình sai → quỹ thiếu** | 4 | 4 | **16** | 🔴 Rất cao | Chạy 3 kịch bản; hiệu chỉnh bằng lý thuyết tín nhiệm sau mỗi mùa; ngưỡng stop-loss | 🟡 Trung bình |
| R5 | **Chi phí sửa cao hơn giả định** | 4 | 3 | **12** | 🟠 Cao | **Khảo sát giá thật (Phần 8)**; ký hợp đồng xưởng đối tác giá cố định | 🟢 Thấp |
| R6 | **Vỡ màn hình** | 3 | 3 | **9** | 🟡 Trung bình | Tặng/cho mượn túi chống sốc; hướng dẫn bảo quản; gói An Tâm | 🟢 Thấp |
| R7 | **Đổ nước / hỏng bàn phím** | 3 | 3 | **9** | 🟡 Trung bình | Cảnh báo khi giao; gói An Tâm; vệ sinh ngay khi nhận báo | 🟢 Thấp |
| R8 | **Tranh chấp "máy trầy sẵn rồi"** | 4 | 2 | **8** | 🟡 Trung bình | Biên bản ảnh/video 2 chiều; khách ký xác nhận đã xem | 🟢 Rất thấp |
| R9 | **Gói An Tâm lỗ do phản chọn lựa** | 3 | 2 | **6** | 🟡 Trung bình | Hệ số tải a = 1,25 (nâng lên 1,5 nếu cần); mức miễn thường 500k | 🟢 Thấp |
| R10 | **Mất sạc/phụ kiện** | 4 | 1 | **4** | 🟢 Thấp | Mua sạc dự phòng rẻ; tính vào miễn thường (khách tự trả) | 🟢 Rất thấp |
| R11 | **Nhu cầu thấp hơn dự kiến (450 lượt)** | 3 | 4 | **12** | 🟠 Cao | (Ngoài phạm vi file này — xem nghiên cứu nhu cầu) | — |
| R12 | **Rủi ro pháp lý: bị coi là kinh doanh BH** | 2 | 4 | **8** | 🟡 Trung bình | **Không dùng từ "bảo hiểm"**; gọi là "Gói Miễn trừ thiệt hại"; xác nhận với giảng viên Luật | 🟢 Thấp |
| R13 | **Rủi ro giữ CCCD gốc** | 3 | 3 | **9** | 🟡 Trung bình | **Không giữ bản gốc**, chỉ chụp ảnh + xác minh MSSV | 🟢 Rất thấp |
| R14 | **Cháy/trộm tại kho (mất nhiều máy cùng lúc)** | 1 | 5 | **5** | 🟡 Trung bình | Xin báo giá BH hoả hoạn (Phần 4.2) — nếu rẻ thì mua; không để toàn bộ máy 1 chỗ trong mùa thấp điểm | 🟡 Trung bình |
| R15 | **Rò rỉ dữ liệu cá nhân khách còn trên máy** | 3 | 3 | **9** | 🟡 Trung bình | Ghi đè Golden Image sau MỖI lượt; BitLocker; điều khoản #10 hợp đồng | 🟢 Thấp |

**Tổng kết:** 2 rủi ro nghiêm trọng nhất (R1, R2) **KHÔNG phải rủi ro tài chính** — chúng là rủi ro **vận hành/dịch vụ**, và được xử lý bằng **máy dự phòng + Golden Image**, không phải bằng bảo hiểm hay quỹ tiền.

---

## 12. VIỆC CẦN LÀM TIẾP

### 12.1. 🔴 Ưu tiên 1 — Bắt buộc trước khi nộp proposal

| # | Việc | Cách làm | Ảnh hưởng nếu bỏ qua |
|---|---|---|---|
| 1 | **Khảo sát giá sửa laptop tại Đà Nẵng** | Điền bảng 8.1 — gọi/đi ít nhất **5 cửa hàng** khu Ngũ Hành Sơn/Hải Châu | 🔴 Toàn bộ tham số `s_i` sai → quỹ & phí DW sai |
| 2 | **Xác nhận giá trị máy V và số lượt thuê R** | Lấy từ file nghiên cứu phần cứng & nghiên cứu nhu cầu của nhóm | 🔴 Sai quy mô toàn mô hình |
| 3 | **Xin ≥3 báo giá bảo hiểm** | Dùng kịch bản 4.2; điền bảng 4.3 | 🟠 Không chứng minh được lựa chọn tự bảo hiểm là tối ưu |
| 4 | **Mở & xác minh 5 URL then chốt** | FPT Shop 137045 · CellphoneS · Viettel Store 165k · PVI EEI · TGDĐ 1567763 | 🔴 Các con số trong file này chưa được xác minh |
| 5 | **Xác nhận pháp lý gói "Miễn trừ thiệt hại"** | Hỏi giảng viên môn Luật / Khởi nghiệp | 🟠 Rủi ro pháp lý cho mô hình kinh doanh |

### 12.2. 🟠 Ưu tiên 2 — Nên có

| # | Việc | Ghi chú |
|---|---|---|
| 6 | Tra AFR laptop & loss rate ngành equipment rental | Từ khoá ở 8.4 |
| 7 | Tra take-up rate & cách định giá CDW ngành cho thuê xe | Từ khoá: `car rental CDW take-up rate`, `collision damage waiver pricing percentage of base rate`, `equipment rental damage waiver 10 percent` |
| 8 | **Thêm câu hỏi vào bảng khảo sát sinh viên**: "Bạn sẵn sàng đặt cọc tối đa bao nhiêu?" và "Bạn có sẵn sàng trả thêm 40.000đ để không phải đền khi lỡ làm hỏng máy?" | Cho ra **take-up rate thật** thay vì giả định 35% |
| 9 | Đàm phán thử với 1 xưởng sửa → có bảng giá cố định bằng văn bản | Biến giả định thành cam kết |
| 10 | Dựng mô hình Excel với các tham số ở 7.1 là ô nhập liệu | Để chạy độ nhạy trong buổi bảo vệ |

### 12.3. Quy trình hiệu chỉnh sau mùa thi đầu tiên

```
  Sau mỗi mùa thi:
  ┌─ 1. Ghi lại MỌI sự cố: loại, chi phí thực tế, ai gây ra, có mua gói An Tâm không
  ├─ 2. Tính tần suất quan sát  f_qs = (số vụ) / (số lượt thuê)
  ├─ 3. Tính hệ số tín nhiệm    Z = √(n / 1082)      [n = tổng số vụ]
  ├─ 4. Cập nhật                f_mới = Z × f_qs + (1−Z) × f_cũ
  ├─ 5. Tính lại E[L], σ, Quỹ, Phí DW
  ├─ 6. So sánh take-up thực tế với giả định 35% → điều chỉnh hệ số a
  └─ 7. Kiểm tra ngưỡng stop-loss (mục 6.3) → hành động nếu chạm ngưỡng
```

---

## 13. DANH MỤC NGUỒN

> **Tất cả URL dưới đây là URL THẬT do WebSearch trả về. KHÔNG có URL nào do mô hình tự tạo.**
> **KHÔNG trang nào được mở và đọc trực tiếp (WebFetch/curl bị chặn).** Nhóm PHẢI tự mở kiểm chứng.

### Bảo hiểm thiết bị điện tử (doanh nghiệp)
| Nguồn | URL | Thông tin rút được |
|---|---|---|
| PVI — Bảo hiểm Thiết bị điện tử | https://www.pvi.com.vn/vi/products/business/electronic-equipment | Dòng sản phẩm cho doanh nghiệp; phí = % số tiền BH, tỷ lệ thay đổi theo ngành nghề |
| PVI — trang chủ | https://www.pvi.com.vn/vi | Vị thế dẫn đầu phi nhân thọ VN |
| PJICO — Bảo hiểm Thiết bị điện tử | https://www.pjico.com.vn/san-pham/bao-hiem-thiet-bi-dien-tu | Có dòng sản phẩm tương đương (chưa đọc nội dung) |
| TOPI — giới thiệu gói BH PVI | https://topi.vn/bao-hiem-pvi-la-gi.html | Tham khảo |

### Bảo hiểm thiết bị di động/laptop (cá nhân)
| Nguồn | URL | Thông tin rút được |
|---|---|---|
| Viettel Store × MIC — ra mắt sản phẩm | https://viettelstore.vn/tin-tuc/viettel-store-hop-tac-cung-bao-hiem-mic-mo-ban-bao-hiem-thiet-bi-di-dong-tren-toan-quoc | Laptop ≤40 tr, mua mới tại Viettel Store; từ 1/5/2021; tái BH Chubb VN; đổi máy tối đa 2 lần |
| Viettel Store — giá từ 165.000đ | https://viettelstore.vn/tin-tuc/bao-hiem-thiet-bi-di-dong-bao-ve-suc-khoe-de-yeu-cua-ban-gia-chi-tu-165-000d | Giảm tới 35%, giá còn từ 165.000đ |
| Viettel Store — tổng hợp các gói | https://viettelstore.vn/tin-tuc/tong-hop-cac-goi-bao-hiem-thiet-bi-di-dong-gia-han-bao-hanh-tai-viettel-store | Phí từ 255.000đ |
| MIC Đông Sài Gòn — BH thiết bị di động & laptop | https://micdongsaigon.com.vn/khach-hang/bao-hiem-thiet-bi-di-dong/ | Phạm vi: vỡ MH, vào nước; có "mức khấu trừ"; thời hạn 6/12 tháng; phạm vi toàn cầu trừ Cuba |
| MIC Đông Sài Gòn — thông cáo ra mắt | https://micdongsaigon.com.vn/bao-hiem-mic-va-viettel-store-ra-mat-bao-hiem-thiet-bi-di-dong/ | Xác nhận hợp tác |
| OPES — QTĐK BH vỡ màn hình điện thoại | https://opes.com.vn/congbo/sanpham/qtdk-phonescreen-V1 | Sản phẩm chỉ cho **điện thoại**, không thấy laptop |
| Dân trí — OPES trải nghiệm số | https://dantri.com.vn/kinh-doanh/bao-hiem-opes-tien-phong-trai-nghiem-so-danh-cho-khach-hang-20240104092308426.htm | Danh mục: chậm chuyến bay, vỡ MH thiết bị điện tử, chuyến xe công nghệ |
| Papaya Insurtech | https://ppaya.vn/ | Không tìm thấy sản phẩm laptop |
| eBaohiem — giới thiệu OPES | https://ebaohiem.com/bao-hiem/gioi-thieu-cong-ty-bao-hiem-opes.html | Tham khảo |
| Papaya — danh mục SP | https://mailevision.com.vn/chi-tiet-bao-hiem | Tham khảo |

### Bảo hành mở rộng / bảo hiểm rơi vỡ chuỗi bán lẻ
| Nguồn | URL | Thông tin rút được |
|---|---|---|
| FPT Shop — gói BH rơi vỡ ĐT & laptop | https://fptshop.com.vn/tin-tuc/tin-khuyen-mai/goi-bao-hanh-roi-vo-dien-thoai-laptop-tai-fpt-shop-gia-chi-tu-79000-dong-137045 | **Từ 79.000đ**; **phí đổi máy 25% giá trị máy cũ**; **SLA 24h HN/HCM, 48h ĐÀ NẴNG/Cần Thơ, tối đa 5 ngày tỉnh khác**; nhân viên đến tận nơi lấy máy |
| FPT Shop — bản tin khác | https://fptshop.com.vn/tin-tuc/tin-khuyen-mai/bao-hanh-roi-vo-vao-nuoc-tai-fpt-shop-gia-chi-tu-79000-dong-140490 | Xác nhận mốc 79.000đ |
| ZNews | https://znews.vn/bao-hanh-roi-vo-vao-nuoc-tai-fpt-shop-voi-gia-tu-79000-dong-post1290215.html | Nguồn báo độc lập xác nhận 79.000đ |
| FPT Shop — chính sách bảo hành | https://fptshop.com.vn/tin-tuc/tin-moi/chinh-sach-bao-hanh-fpt-shop-154419 | Chính sách tổng thể |
| Dân trí — FPT Shop ưu đãi gói BH rơi vỡ | https://dantri.com.vn/cong-nghe/fpt-shop-tang-them-uu-dai-khi-mua-goi-bao-hanh-roi-vo-vao-nuoc-20220118064250199.htm | Nguồn báo |
| FPT — bài "Bảo hành vàng" | https://fpt.com/vi/tin-tuc/tin-fpt/khach-hang-fpt-shop-nhan-duoc-may-moi-tu-bao-hanh-vang | Cơ chế đổi máy mới |
| CellphoneS — chính sách bảo hành từ 11/05/2019 | https://cellphones.com.vn/chinh-sach-bao-hanh-from-11052019 | **S-Diamond do AIG cấp**; rơi vỡ/vào nước **chỉ 1 lần**; **xử lý 14–30 ngày** |
| CellphoneS — Samsung Care+ | https://cellphones.com.vn/bao-hiem-samsung | Gói rơi vỡ/vào nước của hãng |
| Pháp luật Plus — phản ánh về gói CellphoneS × AIG | https://phapluatplus.baophapluat.vn/thuong-de-khoc-thet-vi-goi-bao-hanh-mo-rong-cua-cellphones-va-aig-111448.html | ⚠️ Có tranh chấp thực tế — nên đọc |
| TGDĐ — tất tần tật BH rơi vỡ/BHMR/1 đổi 1 | https://www.thegioididong.com/tin-tuc/tat-tan-tat-ve-chinh-sach-bao-hiem-roi-vo-bao-hanh-mo-rong-bao-hanh-1-doi-1-tai-tgdd-1567763 | 🔴 **Trang quan trọng nhất cần mở** — chứa biểu phí |
| TGDĐ — tổng hợp CSBH toàn ngành hàng | https://www.thegioididong.com/hoi-dap/tong-hop-csbh-the-gioi-di-dong-toan-nganh-hang-1460444 | ⚠️ Snippet "20% tháng đầu, 10%/tháng từ tháng 2–12" — **đáng ngờ, phải xác minh** |
| TGDĐ — bài giới thiệu BH rơi vỡ | https://www.thegioididong.com/tin-tuc/dien-thoai-laptop--tu-nay-roi-vo-da-co-bao-hiem-do-1324313 | Tham khảo |
| ĐMX — chính sách BH rơi vỡ/BHMR | https://www.dienmayxanh.com/kinh-nghiem-hay/chinh-sach-bao-hiem-roi-vo-bao-hanh-mo-rong-bao-1574741 | 🔴 Cần mở để lấy biểu phí |
| ĐMX — dịch vụ bảo hành mở rộng | https://www.dienmayxanh.com/dich-vu-bao-hanh-mo-rong | 🔴 Cần mở |
| ĐMX — CSBH nhóm ĐT/laptop/máy tính bảng | https://www.dienmayxanh.com/kinh-nghiem-hay/chinh-sach-bao-hanh-nhom-hang-dien-thoai-laptop-sm-773940 | Chính sách bảo hành |
| Viettel Store — BH rơi vỡ thiết bị di động | https://viettelstore.vn/tin-tuc/bao-hiem-thiet-bi-di-dong-bao-ve-suc-khoe-de-yeu-cua-ban-gia-chi-tu-165-000d | Xem trên |
| No1Computer — chính sách bảo hành | https://no1computer.vn/bao-hanh.html | Tham khảo mức bảo hành máy cũ |

### Pháp lý & điều khoản loại trừ
| Nguồn | URL | Thông tin rút được |
|---|---|---|
| VKSND Tối cao | https://vksndtc.gov.vn/tin-tuc/cong-tac-kiem-sat/thuc-hien-dieu-khoan-loai-tru-trach-nhiem-bao-hiem-d10-t11857.html | Thực hiện điều khoản loại trừ trách nhiệm BH |
| Công ty Luật ACC | https://congtyluatacc.vn/cong-ty-bao-hiem-tu-choi-chi-tra-do-dieu-khoan-loai-tru-xu-ly-sao/ | Xử lý khi BH từ chối chi trả |
| Manulife | https://www.manulife.com.vn/vi/kien-thuc/cac-dieu-khoan-loai-tru-trong-bao-hiem-nhan-tho.html | Khái niệm điều khoản loại trừ |
| Bảo Hiểm Vui | https://baohiemvui.vn/quyen-loi-bao-hiem-hanh-ly-mat-cap-duoc-boi-thuong-bao-nhieu/ | ⚠️ BH hành lý du lịch — **KHÔNG phải BH laptop**, đừng trích nhầm |

---

## PHỤ LỤC A — BẢNG TÓM TẮT SỐ LIỆU CHO SLIDE THUYẾT TRÌNH

| Chỉ tiêu | Giá trị | Độ tin cậy |
|---|---|---|
| Quy mô đội máy mô hình hoá | 25 máy + 4 máy dự phòng | GĐ |
| Tổng giá trị đội máy | 300.000.000đ (+48 tr dự phòng) | GĐ |
| Số lượt thuê/năm | 450 lượt | GĐ |
| **Tổn thất gộp kỳ vọng** | **29.182.500đ/năm (9,7% giá trị đội máy)** | Tính từ GĐ |
| Độ lệch chuẩn σ | 11.417.000đ | Tính từ GĐ |
| **Tổn thất ròng doanh nghiệp gánh** | **13.168.350đ/năm** | Tính từ GĐ |
| **🎯 QUỸ DỰ PHÒNG RỦI RO (95%)** | **≈ 27.000.000đ (9% giá trị đội máy)** | Tính từ GĐ |
| Vốn mồi quỹ ngày khai trương | 11.000.000đ | Đề xuất |
| Tỷ lệ trích quỹ từ doanh thu | 10% | Đề xuất |
| **🎯 PHÍ MIỄN TRỪ THIỆT HẠI** | **40.000đ/lượt (≤4 ngày) hoặc 15.000đ/ngày** | Tính từ GĐ |
| Mức miễn thường (deductible) | 500.000đ/vụ | Đề xuất |
| Tiền cọc | 2.000.000đ/lượt | Đề xuất |
| Take-up rate giả định | 35% | 🔴 GĐ — chưa có nguồn |
| Lãi gộp từ gói An Tâm | +2.622.375đ/năm | Tính từ GĐ |
| Số máy mất kỳ vọng/năm | 0,68 máy (≈1 máy mỗi 1,5 năm) | GĐ |
| Benchmark phí BH rơi vỡ bán lẻ VN | ≈0,6%–2,6% giá trị máy / 6–12 tháng | Tính từ snippet đã xác minh |
| Benchmark phí đổi máy khi hỏng nặng | **25% giá trị máy cũ** (FPT Shop) | ✅ Snippet |
| SLA sửa chữa nhanh nhất tại Đà Nẵng | **48 giờ** (FPT Shop) | ✅ Snippet |
| Thời gian xử lý BH rơi vỡ bán lẻ | **14–30 ngày** (CellphoneS) | ✅ Snippet |

---

## PHỤ LỤC B — CÔNG THỨC EXCEL SẴN DÙNG

```excel
' Ô nhập liệu (đổi số ở đây, mọi thứ tự tính lại)
B2  = 25           ' N - số máy
B3  = 12000000     ' V - giá trị máy
B4  = 18           ' R - lượt thuê/máy/năm
B5  = 450          ' n = B2*B4
B6  = 500000       ' D - mức miễn thường
B7  = 2000000      ' C - tiền cọc
B8  = 0.35         ' take-up rate
B9  = 0.20         ' tỷ lệ không đòi được

' Bảng hiểm hoạ: cột E = tần suất/lượt, cột F = tổn thất TB
' λ_i:
G2  = $B$5 * E2
' Tổn thất kỳ vọng:
H2  = G2 * F2
' Đóng góp phương sai:
I2  = G2 * F2^2

' Tổng hợp:
E_L    = SUM(H2:H8)
Var_L  = SUM(I2:I8)
Sigma  = SQRT(Var_L)
Quy95  = E_L + 1.645 * Sigma
Quy99  = E_L + 2.326 * Sigma

' Phí DW:
KhachGiuLai = SUMPRODUCT(E2:E7, MIN(F2:F7, $B$6))   ' nhập mảng Ctrl+Shift+Enter
PhiThuan    = SUMPRODUCT(E2:E7, F2:F7) - KhachGiuLai
PhiNiemYet  = PhiThuan * 1.15 * 1.25 * 1.20

' Mô phỏng Monte Carlo (kéo xuống 10.000 dòng):
SoVu_i    = POISSON.INV(RAND(), λ_i)
TonThat_n = SUMPRODUCT(SoVu_range, F2:F8)
' Rồi: Quỹ_MonteCarlo = PERCENTILE(TonThat_range, 0.95)
' → So sánh với Quy95 từ công thức chuẩn. Nếu chênh >20%, dùng số Monte Carlo (chính xác hơn với đuôi lệch)
```

---

*Tài liệu lập ngày 14/09/2026 — module 08 của bộ nghiên cứu proposal khởi nghiệp. Mọi con số gắn nhãn 🔴 hoặc "GĐ" PHẢI được thay bằng dữ liệu khảo sát thực tế trước khi đưa vào bản nộp.*
