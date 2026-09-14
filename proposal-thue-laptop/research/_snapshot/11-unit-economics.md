# 11 — UNIT ECONOMICS & SỐ LIỆU TÀI CHÍNH THẬT
## Dịch vụ cho thuê laptop đi thi — quy mô 15–40 máy — khu vực ĐH FPT Đà Nẵng (P. Hoà Hải, Ngũ Hành Sơn)

- **Ngày tổng hợp:** 14/09/2026
- **Người dùng tài liệu:** nhóm sinh viên môn Khởi nghiệp, ĐH FPT Đà Nẵng
- **Mục đích:** nguyên liệu thô để dựng bảng P&L 12 tháng, tính CAPEX, điểm hoà vốn, thời gian hoàn vốn/máy

---

## 0. CẢNH BÁO PHƯƠNG PHÁP — ĐỌC TRƯỚC KHI DÙNG SỐ

> **RẤT QUAN TRỌNG.** Môi trường nghiên cứu này **bị chặn WebFetch/curl** (mọi domain trả `EGRESS_BLOCKED`). Toàn bộ số liệu dưới đây được rút ra từ **tiêu đề + đoạn trích (snippet) do công cụ WebSearch trả về**, **KHÔNG mở được trang gốc để đọc bảng giá đầy đủ**.

Hệ quả bắt buộc nhóm phải xử lý:

| Rủi ro | Biểu hiện | Việc nhóm phải làm |
|---|---|---|
| Giá web ≠ giá thực tế | Shop laptop cũ VN thường niêm yết "giá từ", giá thật phụ thuộc cấu hình/tình trạng pin/màn | Gọi điện hoặc đến trực tiếp shop, xin **báo giá có văn bản** cho lô 15–40 máy |
| Snippet không ghi rõ shop nào | Một vài con số trong file này nằm trong nhóm 8–9 kết quả, chưa xác định chính xác URL nguồn | Mục nào bị đánh dấu `[SNIPPET-MƠ-HỒ]` phải mở lại từng URL trong "nhóm ứng viên" để đối chiếu |
| Giá thay đổi theo tháng | Thị trường laptop cũ VN biến động 5–15%/quý | Chốt lại giá trong vòng **≤ 2 tuần** trước khi nộp proposal |
| Chưa có giá lô sỉ | Mọi giá dưới đây là **giá bán lẻ 1 máy** | Hỏi chiết khấu mua 15–40 máy (thị trường thường giảm thêm) |

**Ký hiệu dùng trong file:**
- `[XÁC MINH-SNIPPET]` = số có trong snippet, nguồn rõ, nhưng chưa mở được trang → nhóm phải kiểm chứng lại.
- `[SNIPPET-MƠ-HỒ]` = số có trong snippet nhưng **không xác định được chính xác URL nào trong nhóm kết quả** → độ tin cậy thấp nhất, bắt buộc kiểm chứng.
- `[GIẢ ĐỊNH]` = con số do nhóm/người viết đặt ra để dựng mô hình, **KHÔNG phải dữ liệu thật**.
- `[KHÔNG TÌM ĐƯỢC]` = đã tìm nhưng ngân sách WebSearch của phiên đã hết / không có kết quả.

---

# PHẦN A — CAPEX: GIÁ MUA LAPTOP

## A.1. Laptop CŨ dòng business (trục xương sống của mô hình)

Đây là nhóm máy phù hợp nhất với bài toán: thi EOS + Safe Exam Browser bắt buộc Windows, cấu hình chỉ cần chạy được trình duyệt khoá và phần mềm thi, nhưng **độ bền và tỉ lệ hỏng thấp là ưu tiên số 1** (máy hỏng giữa ca thi = mất khách vĩnh viễn).

### Bảng A.1 — Giá laptop cũ business tại VN (tổng hợp 09/2026)

| # | Model | Cấu hình theo snippet | Giá (VND) | Nguồn (URL thật) | Độ tin cậy |
|---|---|---|---|---|---|
| 1 | **Lenovo ThinkPad T480** | i5-8250U / 8GB DDR4 / SSD 256GB / 14" FHD chống chói | **từ 6.200.000** | https://laptops.vn/san-pham/thinkpad-t480/ | `[XÁC MINH-SNIPPET]` — snippet ghi rõ "Giá Tháng 12 \| 2025" |
| 2 | ThinkPad T480 (shop khác) | i5-8250U / 8GB / SSD 256GB / 14" FHD | chưa hiện giá trong snippet | https://laptoptcc.com/laptop-cu-lenovo-thinkpad-t480-core-i5-8250u-8-gb-ram-ssd-256-gb-14-fhd | cần mở trang |
| 3 | ThinkPad T480 Like New | i5 Gen 8, BH 12 tháng | chưa hiện giá | https://nhatminhlaptop.com/thinkpad-t480-i5-8250u | cần mở trang |
| 4 | ThinkPad T480s | i5-8250U / 8GB / 256GB / cũ 99% | chưa hiện giá | https://2tmobile.com/thinkpad-t480s-cu-99 (trang: https://2tmobile.com/thinkpad-t480s-core-i5-8250u-ram-8gb-ssd-256gb-cu-99) | cần mở trang |
| 5 | **ThinkPad T490** | i7-10510 / 16GB / SSD 512GB / 14" FHD cảm ứng / 98–99% | **8.500.000** | `[SNIPPET-MƠ-HỒ]` — nhóm ứng viên: https://nhatminhlaptop.com/thinkpad-t490 · https://2tmobile.com/thinkpad-t490-i5-8265u-16gb-256gb-99/ · https://laptopsieuben.com/product/lenovo-thinkpad-t490-core-i5-8265u | thấp — phải đối chiếu 3 URL |
| 6 | **Dell Latitude 5410** | i5-10310U / 8GB / SSD 256GB / 14" FHD, BH 6 tháng | **7.280.000** | https://laptoptv.vn/laptop-cu-dell-latitude-5410-core-i5-10310u-8gb-256gb-man-hinh-14-inch-fhd | `[XÁC MINH-SNIPPET]` |
| 7 | Dell Latitude 5410 | i5-10310U / **16GB** / SSD 256GB / 14" FHD, BH 6 tháng | **8.380.000** | https://laptoptv.vn/laptop-cu-dell-latitude-5410-core-i5-10310u-16gb-256gb-man-hinh-14-inch-fhd | `[XÁC MINH-SNIPPET]` |
| 8 | Dell Latitude 5410 | i5-10310U / 8GB / 256GB / 14" FHD (shop khác) | **7.490.000** | `[SNIPPET-MƠ-HỒ]` — ứng viên: https://hacom.vn/laptop-dell-latitude-5410-i5-10310u-8gb-ram-256gb-ssd-man-14.0-inch-fhd-kem-sac-hang-cu-dep · https://anhduongstore.vn/laptop-cu-dell-latitude-5410-core-i5-10310u-ram-8gb-ssd-256gb-14-inch-fhd · https://topcomputer.vn/laptop-cu-dell-5410-i5-10310u-8gb-256gb-fhd-14 | trung bình |
| 9 | **Dell Latitude 5400** | i5-8365U / 8GB DDR4 / SSD 256GB / 14" FHD IPS | **từ 5.000.000** | https://laptop15.vn/dell-latitude-5400/ (title ghi rõ "Giá Chỉ Từ 5 Triệu") | `[XÁC MINH-SNIPPET]` |
| 10 | Dell Latitude 5400 | i5-8365U / 8GB / 256GB / 14" FHD | **6.500.000** | `[SNIPPET-MƠ-HỒ]` — ứng viên: https://hoangsonstore.com/dell-latitude-5400 · https://laptoptld.com/sp/dell-latitude-5400/ · https://www.shopcongngheso.vn/dell-latitude-5400-i5-8365u | trung bình |
| 11 | Dell Latitude 5400 | i5-8365U / 8GB / 256GB | **6.990.000** | `[SNIPPET-MƠ-HỒ]` — cùng nhóm ứng viên #10 | trung bình |
| 12 | Dell Latitude 5400 | bản cảm ứng / Win10 | **~9.000.000** | https://laptopcubinhduong.vn/dell-latitude-5400/ (shop Laptop Cũ Bình Dương — đúng shop đề bài yêu cầu) | `[SNIPPET-MƠ-HỒ]` về mức giá, URL thì chắc chắn |
| 13 | **HP EliteBook 840 G6** | laptop văn phòng mỏng nhẹ | **từ ~10.000.000** | https://techcare.vn/hp-elitebook-840-g6/ — **shop tại Đà Nẵng** | `[XÁC MINH-SNIPPET]` |
| 14 | HP EliteBook 840 G6 | i5-8350U / 8GB / SSD 256GB, like new 99% | chưa hiện giá | https://ttcenter.com.vn/hp-elitebook-840-g6-core-i5-8350u-ram-8gb-ssd-256gb | cần mở trang |
| 15 | HP EliteBook 840 G5 | i5-8350U / 8GB / SSD 256GB, like new 99% | chưa hiện giá | https://ttcenter.com.vn/hp-elitebook-840-g5-core-i5-8350u-ram-8gb-ssd-256gb | cần mở trang |
| 16 | **ThinkPad T14s Gen 2 (2021)** | i5 / 16GB / SSD 512GB / 99% | **10.200.000 – 10.600.000** | https://ttcenter.com.vn/thinkpad-t14s-gen-2-core-i5-16gb-512gb-99 | `[XÁC MINH-SNIPPET]` |
| 17 | ThinkPad dòng T cũ (mặt bằng chung) | nhiều cấu hình i5/i7 | **5.310.000 – 6.490.000** (số liệu ngày 03/06/2026) | https://2tmobile.com/thinkpad-t-cu/ | `[XÁC MINH-SNIPPET]` |
| 18 | ThinkPad cũ (mặt bằng thấp nhất) | các đời cũ hơn | **từ 3.000.000** | https://laptops.vn/review/laptop-thinkpad-cu-gia-re/ (bài "Top 8 Laptop Thinkpad Cũ Giá Rẻ 2026") | `[XÁC MINH-SNIPPET]` |
| 19 | ThinkPad T490 | i7-8565U / 16GB / 256GB | chưa hiện giá | https://nhatminhlaptop.com/thinkpad-t490 | cần mở trang |

### ⚠ Cảnh báo riêng về HP EliteBook 840 G5
Snippet trả về câu *"giá máy cũ đã giảm xuống còn khoảng 22 triệu; lúc mới ra mắt khoảng 40 triệu"* từ bài tư vấn https://no1computer.vn/hp-elitebook-840-g5-san-xuat-nam-nao-n60.html — **con số 22 triệu này gần như chắc chắn là bài viết cũ chưa cập nhật**, mâu thuẫn với mặt bằng EliteBook 840 G6 "từ 10 triệu" và mâu thuẫn với dải niêm yết trên Chợ Tốt. **KHÔNG dùng số 22 triệu.** Tham chiếu Chợ Tốt (dải rất rộng, gồm cả tin rác):
- https://www.chotot.com/tags/mua-ban-laptop/hp-elitebook-840-g5 → dải "dưới 5 triệu đến trên 25 triệu" `[XÁC MINH-SNIPPET]`
- https://www.chotot.com/tags/mua-ban-laptop/hp-840-g5
- https://www.chotot.com/tags/mua-ban-laptop/hp-elitebook-840

### Bảng A.1b — Khoảng giá đề xuất để dựng CAPEX (tổng hợp từ bảng trên)

| Phân khúc | Model đại diện | Khoảng giá quan sát được (VND/máy) | Ghi chú cho mô hình |
|---|---|---|---|
| **Tiết kiệm** | Dell Latitude 5400 i5-8365U/8/256 · ThinkPad T480 | **5.000.000 – 6.990.000** | Đủ chạy Windows + SEB. Rủi ro: pin chai, đời CPU Gen 8 (2018) |
| **Cân bằng (khuyến nghị)** | Dell Latitude 5410 i5-10310U/8/256 · ThinkPad T480 8GB | **6.200.000 – 7.490.000** | Điểm ngọt giữa giá và tuổi đời máy |
| **Cao cấp** | ThinkPad T490 · T14s Gen 2 · EliteBook 840 G6 | **8.500.000 – 10.600.000** | Chỉ nên mua vài máy làm "máy dự phòng VIP" |

---

## A.2. Laptop MỚI phân khúc dưới 12 triệu (2026)

FPT Shop, GEARVN, MemoryZone đều có bài tổng hợp 2026. **Snippet KHÔNG trả về giá cụ thể từng model** — chỉ trả về cấu hình. Đây là khoảng trống dữ liệu quan trọng.

| Model | Cấu hình (theo snippet) | Giá | Nguồn |
|---|---|---|---|
| **Acer Aspire Lite 14 AL14-52M-32KV** | Intel Core i3-1305U (Gen 13), RAM 8GB DDR5, SSD 256GB NVMe, 14" WUXGA 1920×1200 | `[KHÔNG TÌM ĐƯỢC]` | https://fptshop.com.vn/tin-tuc/danh-gia/laptop-sinh-vien-duoi-12-trieu-2026-205902 |
| **Lenovo V14 G4 IRU 83A000S4VN** | Intel Core i3-1315U (Gen 13), RAM 8GB (nâng cấp được), SSD 512GB NVMe | `[KHÔNG TÌM ĐƯỢC]` | https://fptshop.com.vn/tin-tuc/danh-gia/laptop-sinh-vien-duoi-12-trieu-2026-205902 |
| **Colorful Rimbook L1** | Intel Core i3-1220P (10 nhân / 12 luồng), mỏng nhẹ | `[KHÔNG TÌM ĐƯỢC]` | https://fptshop.com.vn/tin-tuc/danh-gia/laptop-sinh-vien-duoi-12-trieu-2026-205902 |

**Trần phân khúc đã được xác nhận: < 12.000.000 VND/máy** (tiêu đề bài của cả 4 nguồn dưới).

Nguồn bổ sung cần mở lại để lấy giá từng model:
- https://gearvn.com/blogs/danh-gia-tu-van/top-laptop-cho-sinh-vien-duoi-12-trieu
- https://memoryzone.com.vn/laptop-gia-re-duoi-12-trieu-dong-cho-sinh-vien
- https://www.phucanh.vn/top-6-laptop-van-phong-gia-re-ban-nen-tham-khao.html
- https://hoanghamobile.com/tin-tuc/top-10-laptop-van-phong-gia-re-duoi-15-trieu-dang-mua-2026/
- https://thailongcomputer.com/laptop-cho-sinh-vien-van-phong.html
- https://cellphones.com.vn/sforum/top-5-laptop-cho-tan-sinh-vien-gia-re

### Khuyến nghị chiến lược mua (cho phần "Vận hành" của proposal)

> Dữ liệu cho thấy **1 máy MỚI dưới 12 triệu ≈ giá của 2 máy CŨ business Latitude 5400 (5–7 triệu)**. Với mô hình cho thuê, **số lượng máy sẵn sàng quan trọng hơn cấu hình**, vì nhu cầu chỉ là chạy Windows + EOS + Safe Exam Browser. Đề xuất tỉ trọng: **~85% máy cũ business + ~15% máy mới/cao cấp** làm máy dự phòng và máy demo. → Đây là `[GIẢ ĐỊNH]` của nhóm, cần lập luận trong proposal.

---

## A.3. Kênh mua tại ĐÀ NẴNG (gần địa bàn vận hành)

Ưu thế lớn: mua tại Đà Nẵng thì **bảo hành và sửa chữa nằm trong bán kính xe máy**, giảm downtime máy — yếu tố sống còn khi khách thuê để đi thi.

| Shop | Địa chỉ / Thông tin | URL |
|---|---|---|
| **T&T Center (Trường Giang Computer)** | CN1: 133 Hàm Nghi, Thanh Khê, ĐN · **CN2: 101 Nguyễn Văn Thoại, Ngũ Hành Sơn, ĐN** · ĐT: 0905 677 427 – 0969 539 381 | https://ttcenter.com.vn/laptop-cu |
| **Kim Anh Computer** | **248 Ngũ Hành Sơn, Ngũ Hành Sơn, ĐN** · ĐT: 0777 126 126 | https://laptopkimanh.vn/14-inch |
| **TechCare Đà Nẵng** | chuyên EliteBook 840 G6 "từ 10 triệu" | https://techcare.vn/hp-elitebook-840-g6/ |
| **Ngọc Vũ PC** | chuyên ThinkPad & Dell like new 99% nhập khẩu Nhật | https://ngocvupc.com/ |
| **Laptopre.vn (Thanh Hương Technology)** | laptop cũ Đà Nẵng | https://laptopre.vn/laptop-cu |
| **T&T Laptop** | 484 Núi Thành, Hoà Cường Nam, Hải Châu, ĐN | (xem top10danang bên dưới) |
| **Chợ Tốt Đà Nẵng** | **2.399 tin laptop cũ Đà Nẵng** (số liệu 25/08/2026) — nguồn mua rẻ nhất nhưng rủi ro cao nhất | https://www.chotot.com/mua-ban-laptop-da-nang |
| Danh sách tổng hợp | "15+ địa chỉ bán laptop cũ Đà Nẵng" | https://top10danang.com/diem-danh-15-dia-chi-ban-laptop-cu-da-nang-gia-re-uy-tin/ |
| Danh sách tổng hợp | "Top 10 địa chỉ mua bán laptop cũ Đà Nẵng" | https://www.taidanang.com/laptop-cu-da-nang/ |
| Rao vặt | Laptop cũ/mới Đà Nẵng | https://raovat.vnexpress.net/da-nang/laptop |

Shop ngoài Đà Nẵng (đề bài yêu cầu) đã tìm được URL:
- **Laptop Cũ Bình Dương** — https://laptopcubinhduong.vn/dell-latitude-5400/
- **ThinkPro** — https://thinkpro.vn/laptop/hp-elitebook-840-g5 (trang niêm yết 08/2026, chưa mở được giá)
- LaptopTV — https://laptoptv.vn/ (có giá Latitude 5410 rõ nhất)
- Nhật Minh Laptop — https://nhatminhlaptop.com/
- 2T Mobile — https://2tmobile.com/thinkpad-cu-99/
- Cường Phát — https://laptopcuongphat.com/laptop-cu-lenovo-thinkpad/
- Next Gold — https://nextgold.vn/danh-sach-laptop-cu-2025/
- `[KHÔNG TÌM ĐƯỢC]`: LaptopWorld, Hoàng Hà, Nam Phương — hết ngân sách WebSearch của phiên, nhóm tự tra thêm.

---

## A.4. Các khoản CAPEX khác chưa có số liệu

| Khoản | Trạng thái |
|---|---|
| Túi chống sốc / balo đựng laptop (×N máy) | `[KHÔNG TÌM ĐƯỢC]` |
| Sạc dự phòng / cục sạc thay thế | `[KHÔNG TÌM ĐƯỢC]` |
| Tem niêm phong, tem tài sản, khoá số | `[KHÔNG TÌM ĐƯỢC]` |
| Kệ/tủ sắt lưu trữ máy | `[KHÔNG TÌM ĐƯỢC]` |
| Bản quyền Windows (nếu mua máy không kèm bản quyền) | `[KHÔNG TÌM ĐƯỢC]` — **quan trọng**, vì thi EOS bắt buộc Windows; máy cũ nhập khẩu thường kèm Win bản quyền OEM, cần xác minh với shop |
| Bảo hiểm thiết bị / quỹ dự phòng mất máy | `[KHÔNG TÌM ĐƯỢC]` |

---

# PHẦN B — KHẤU HAO & GIÁ TRỊ THU HỒI

## B.1. Khung pháp lý (Thông tư 45/2013/TT-BTC)

| Nội dung | Số liệu | Nguồn |
|---|---|---|
| Điều kiện ghi nhận TSCĐ | **Nguyên giá ≥ 30.000.000 VND**, thời gian sử dụng **> 1 năm**, phục vụ trực tiếp hoạt động kinh doanh (Điều 4) | https://docs.kreston.vn/vbpl/chi-phi-tai-chinh/tai-san-co-dinh/thong-tu-45-2013-tt-btc/ |
| Hệ quả trực tiếp cho dự án | **Laptop 5–11 triệu/máy KHÔNG đủ điều kiện là TSCĐ** → hạch toán thẳng vào chi phí (công cụ dụng cụ), không trích khấu hao TSCĐ. Snippet nêu ví dụ: *"một chiếc laptop giá 25 triệu đồng dù sử dụng lâu dài vẫn không được khấu hao mà phải hạch toán trực tiếp vào chi phí"* | https://accnet.vn/cach-tinh-khau-hao-tai-san-co-dinh-cu-the-chi-tiet-chinh-xac |
| Khung thời gian khấu hao nhóm "máy móc thiết bị" | **3 – 15 năm** (Phụ lục 1) | https://ketoanthienung.org/tin-tuc/khung-thoi-gian-trich-khau-hao-cac-loai-tai-san-co-dinh.htm |
| Laptop có mã riêng trong Phụ lục 1? | **Không được liệt kê cụ thể**; thường xếp vào nhóm thiết bị văn phòng / máy móc thiết bị | https://acccantho.vn/khau-hao-tai-san-co-dinh-theo-thong-tu-45/ |

Văn bản gốc:
- https://vcci.com.vn/legal-document/thong-tu-452013tt-btc-cua-bo-tai-chinh-ve-viec-huong-dan-che-do-quan-ly-su-dung-va-trich-khau-hao-tai-san-co-dinh
- https://ketoanthienung.net/khung-thoi-gian-trich-khau-hao-cac-loai-tai-san-co-dinh.htm
- https://kiemtoancalico.com/ghi-nhan-tscd-va-trich-khau-hao-doi-voi-laptop-moi-mua-cua-cong-ty.html
- https://khanhhungpc.vn/khau-hao-may-tinh-van-phong/ (bài "Khấu Hao Máy Tính Văn Phòng – Cách Thẩm Định Giá")

> **Ghi chú cho proposal:** vì máy < 30 triệu, về mặt kế toán thuế đây là **công cụ dụng cụ**, không phải TSCĐ. Nhưng để dựng **mô hình tài chính nội bộ** (tính hoàn vốn/máy), nhóm **vẫn nên trích khấu hao kinh tế** theo tuổi thọ kỳ vọng. Hai cách trình bày khác nhau — nêu rõ trong proposal để tránh bị phản biện.

## B.2. Tỉ lệ mất giá thực tế trên thị trường

| Phát hiện | Số liệu | Nguồn |
|---|---|---|
| Chênh lệch máy cũ vs máy mới | **Laptop cũ rẻ hơn 30–50% so với máy mới** (cùng phân khúc) | https://laptops.vn/review/laptop-thinkpad-cu-gia-re/ |
| Hình dạng đường mất giá | *"Một chiếc máy tính sẽ mất giá trị nhanh nhất trong năm đầu tiên và ổn định dần ở các năm tiếp theo nếu được giữ gìn cẩn thận"* → đường cong lồi, không tuyến tính | https://macvn.com.vn/dinh-gia-laptop-cu/ |
| Yếu tố quyết định giá bán lại | (1) thời gian sử dụng — **thông số quan trọng nhất**; (2) model & năm sản xuất; (3) cấu hình CPU/RAM/ổ cứng; (4) **tình trạng pin và màn hình** — hai linh kiện thay thế đắt nhất, lỗi là giá tụt mạnh | https://macvn.com.vn/dinh-gia-laptop-cu/ |
| Thảo luận cộng đồng | "Laptop cũ bán được bao nhiêu là hợp lý?" | https://tinhte.vn/thread/laptop-cu-ban-duoc-bao-nhieu-la-hop-ly.4115236/ |

### ❌ `[KHÔNG TÌM ĐƯỢC]`: con số %/năm cụ thể
Không nguồn nào trong kết quả tìm kiếm đưa ra tỉ lệ mất giá **%/năm** định lượng cho laptop tại VN. Đây là **lỗ hổng dữ liệu lớn nhất của phần B**.

### Cách nhóm tự tạo số liệu thật thay thế (khuyến nghị mạnh)
Không cần chờ nguồn thứ cấp — làm khảo sát giá sơ cấp, rất hợp với bài tập khởi nghiệp:
1. Vào https://www.chotot.com/mua-ban-laptop-da-nang (2.399 tin) và https://www.chotot.com/tags/mua-ban-laptop/thinkpad-t490
2. Lấy 20–30 tin **cùng 1 model** (ví dụ ThinkPad T480, ra mắt 2018) và ghi giá rao.
3. So với giá shop bán ra hôm nay và giá gốc khi ra mắt → suy ra đường mất giá thực nghiệm.
4. Bảng ví dụ tự lập: model ra mắt 2018, giá gốc ~X, hôm nay bán ~6,2 triệu → tính CAGR mất giá.

### `[GIẢ ĐỊNH]` để dựng mô hình khi chưa có số thật
Chỉ dùng tạm và **phải ghi rõ là giả định trong proposal**:

| Kịch bản | Tuổi thọ vận hành | Giá trị thu hồi cuối kỳ | Khấu hao kinh tế |
|---|---|---|---|
| Thận trọng `[GIẢ ĐỊNH]` | 24 tháng | 30% nguyên giá | ~2,9%/tháng |
| Cơ sở `[GIẢ ĐỊNH]` | 36 tháng | 35% nguyên giá | ~1,8%/tháng |
| Lạc quan `[GIẢ ĐỊNH]` | 48 tháng | 30% nguyên giá | ~1,5%/tháng |

Lập luận hỗ trợ cho tuổi thọ dài: dòng **business (ThinkPad T / Latitude / EliteBook) vốn được thiết kế chu kỳ doanh nghiệp 3–5 năm**, và thực tế thị trường VN vẫn giao dịch sôi động máy đời 2018 (T480) ở mức 6,2 triệu vào 2025–2026 — tức sau ~7 năm vẫn còn thanh khoản. Đây là **luận điểm mạnh cho proposal**: tài sản của mô hình này mất giá chậm và luôn có thị trường thứ cấp để thanh lý.

---

# PHẦN C — DOANH THU THAM CHIẾU: GIÁ THUÊ LAPTOP TRÊN THỊ TRƯỜNG

## C.1. Bảng giá thuê — thị trường toàn quốc

| Đơn vị | Giá theo NGÀY | Giá theo THÁNG | Ghi chú | Nguồn |
|---|---|---|---|---|
| **MIT Group** | **từ 29.000 VND/ngày**; **ưu đãi sinh viên từ 20.000 VND/ngày** | — | Mức giá thấp nhất tìm được toàn thị trường | https://mitgroup.vn/cho-thue-laptop/ |
| Thị trường chung (nhiều đơn vị) | **từ 50.000 VND/máy/ngày** | — | mặt bằng phổ biến | `[SNIPPET-MƠ-HỒ]` — ứng viên: https://thietbichothue.com/cho-thue-laptop/ · https://wifisukien.com/cho-thue-laptop/ · https://skylap.vn/dich-vu-cho-thue/cho-thue-laptop/ |
| Thuê theo tháng (thị trường chung) | — | **từ 600.000 VND/tháng** | `[SNIPPET-MƠ-HỒ]` — ứng viên: https://chothuelaptop.com.vn/thue-laptop-theo-thang/ · https://phuongnamco.com/cho-thue-laptop-theo-thang-tiet-kiem-linh-hoat-cho-ca-nhan-va-doanh-nghiep/ | |
| Laptop đồ hoạ (phân khúc cao) | có bảng giá theo ngày/tuần/tháng/năm | — | tham chiếu trần giá | https://thuelaptop.com.vn/bang-gia-cho-thue-laptop-do-hoa.html |
| Vietbis (Hà Nội) | — | — | dịch vụ cho thuê laptop/PC | https://vietbis.vn/tin-tuc/dich-vu-cho-thue-laptop-tai-ha-noi---vietbisvn-2530.html |

## C.2. Bảng giá thuê — **TẠI ĐÀ NẴNG** (đối thủ trực tiếp)

| Đơn vị | Giá theo NGÀY | Giá theo THÁNG | Dịch vụ kèm | Nguồn |
|---|---|---|---|---|
| **DH Lend** | **50.000 VND/ngày** | **1.000.000 VND/tháng** | Giao & nhận tận nơi trong khu vực Đà Nẵng; **đổi máy nếu hư hỏng trong lúc sử dụng**; có kỹ thuật hướng dẫn | https://dhlend.com/cho-thue-may-tinh-laptop-pc-may-in-da-nang.html |
| **Trường Giang Computer** | **từ 50.000 VND/ngày** | có, chưa rõ giá | HP, Dell, Acer, Asus, MacBook Air/Pro | https://truonggiang.vn/cho-thue-laptop.html |
| **leminhSTORE** | **từ 38.000 VND/ngày** | có, chưa rõ giá | gói riêng "thuê laptop sinh viên Đà Nẵng" | https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html |
| Sky Computer | chưa rõ | chưa rõ | cho thuê máy tính/laptop Đà Nẵng | https://skycomputer.vn/dich-vu/cho-thue-may-tinh-laptop-tai-da-nang/ |
| Chothuelaptop.com.vn (CN Đà Nẵng) | chưa rõ | chưa rõ | — | https://chothuelaptop.com.vn/thue-laptop-da-nang/ |
| Chothuelaptop.info | chưa rõ | chưa rõ | "thủ tục nhanh gọn" | https://chothuelaptop.info/cho-thue-laptop-da-nang-thu-tuc-nhanh-gon/ |
| leminhSTORE (dịch vụ đủ) | — | — | Thuê Laptop / MacBook / iMac / PC văn phòng, thi công dự án & sự kiện | https://leminhstore.vn/thue-laptop-thue-macbook-thue-imac-thue-pc-van-phong-thi-cong-du-an-su-kien-tai-da-nang-76867u.html |
| Danh sách tổng hợp | — | — | "Top 7 dịch vụ cho thuê laptop Đà Nẵng uy tín" | https://danang.plus/thue-laptop/ |
| Danh sách tổng hợp | — | — | "Địa điểm cho thuê laptop tại Đà Nẵng giá rẻ" | https://thuelaptop.com.vn/dia-diem-cho-thue-laptop-tai-da-nang-gia-re.html |

## C.3. Cơ chế thương mại chuẩn của ngành (dùng để thiết kế chính sách giá)

| Cơ chế | Số liệu | Nguồn |
|---|---|---|
| **Đặt cọc** | Bắt buộc trong hầu hết dịch vụ; **mức cọc tuỳ cấu hình máy**, hoàn trả khi kết thúc hợp đồng | `[XÁC MINH-SNIPPET]` — tổng hợp từ nhóm kết quả C.1 |
| **Chiết khấu số lượng** | Thuê số lượng lớn **giảm 10–20%** tuỳ số lượng | `[XÁC MINH-SNIPPET]` — tổng hợp từ nhóm kết quả C.1 |
| Kỳ hạn thuê | Đa số cho thuê **theo ngày / theo tuần / theo tháng**; điều khoản điều chỉnh theo nhu cầu khách | `[XÁC MINH-SNIPPET]` |
| Mục đích thuê phổ biến | học tập, văn phòng, **sự kiện, hội nghị, và THI TUYỂN** — snippet nêu đích danh "thi tuyển" | https://danang.plus/thue-laptop/ + nhóm kết quả C.2 |

> **Phát hiện quan trọng cho proposal:** các đối thủ Đà Nẵng đã bán được cả "thi tuyển" nhưng **không ai định vị chuyên biệt cho SINH VIÊN ĐI THI EOS + Safe Exam Browser**. Đây là khoảng trống định vị. Đồng thời, việc DH Lend cam kết **"đổi máy nếu hư hỏng trong lúc sử dụng"** cho thấy **SLA đổi máy là kỳ vọng mặc định của thị trường** — mô hình của nhóm bắt buộc phải có, và nên nâng lên thành **SLA đổi máy trong X phút trong ngày thi** để tạo khác biệt.

## C.4. Khoảng giá đề xuất cho mô hình (suy ra từ dữ liệu trên)

| Gói | Neo thị trường | Đề xuất `[GIẢ ĐỊNH]` | Lập luận |
|---|---|---|---|
| Thuê 1 ngày (ca thi) | ĐN: 38.000–50.000 VND/ngày | 50.000–80.000 VND/ngày | Có thể neo cao hơn 50K vì bán **sự chắc chắn trong ngày thi**, không bán "cái máy" |
| Gói "ca thi khẩn cấp" (giao <60 phút) | không ai bán | 100.000–150.000 VND/ca | Đây là sản phẩm lõi — giá trị = tránh trượt môn |
| Thuê theo tuần (mùa thi) | — | ~200.000–300.000 VND/tuần | — |
| Thuê theo tháng | ĐN: 1.000.000 VND/tháng; toàn quốc từ 600.000 | 600.000–900.000 VND/tháng | Bám sàn thị trường để lấp công suất ngoài mùa thi |

---

# PHẦN D — OPEX: CHI PHÍ VẬN HÀNH TẠI ĐÀ NẴNG

## D.1. Mặt bằng / kho tại Hoà Hải – Ngũ Hành Sơn – FPT City

### D.1a — Phòng trọ (phương án rẻ nhất: dùng phòng trọ làm kho + điểm giao nhận)

| Loại | Giá (VND/tháng) | Chi tiết | Nguồn |
|---|---|---|---|
| **Dải chung Q. Ngũ Hành Sơn** | **1.100.000 – 6.800.000** | Toàn quận, 01/2026 | https://phongtro123.com/tinh-thanh/da-nang/quan-ngu-hanh-son |
| **FPT City, Hoà Hải** | **3.200.000** | Full nội thất hiện đại | https://troplus.vn/phong-tro/cho-thue-phong-tro-full-noi-that-gan-fpt-city-hoa-hai-ngu-hanh-son-da-nang-gia-chi-32-trieuthang |
| **Gần ĐH FPT** | **3.800.000** | Có gác lửng | `[SNIPPET-MƠ-HỒ]` — ứng viên: https://www.nhatot.com/thue-phong-tro-gan-truong-dai-hoc-fpt-da-nang-quan-ngu-hanh-son-sdse344300 |
| **Võ Văn Đồng, P. Hoà Hải** | **4.500.000** | Full nội thất, **40 m²** | `[SNIPPET-MƠ-HỒ]` — cùng nhóm ứng viên trên |
| **Khoảng tập trung gần ĐH FPT** | **3.200.000 – 4.500.000** | Kết luận tổng hợp của snippet cho 01/2026 | tổng hợp |

Nguồn tra thêm:
- https://phongtro123.com/tinh-thanh/da-nang/quan-ngu-hanh-son/phuong-hoa-hai (lọc đúng P. Hoà Hải)
- https://www.nhatot.com/thue-phong-tro-phuong-hoa-hai-quan-ngu-hanh-son-da-nang (35 tin, 09/2025)
- https://www.nhatot.com/thue-phong-tro-quan-ngu-hanh-son-da-nang
- https://homedy.com/cho-thue-nha-tro-phong-tro-quan-ngu-hanh-son-da-nang/gia-re-phuong-hoa-hai-es1569907
- https://chothuephongtro.me/da-nang/quan-ngu-hanh-son.html
- https://sosanhnha.com/cho-thuê-nhà-trọ-phòng-trọ-fpt-city-đà-nẵng-tại-phường-hòa-hải-quận-ngũ-hành-sơn-đà-nẵng

Snippet ghi rõ khu quanh ĐH FPT có nhiều loại hình: *phòng trọ khép kín, phòng có gác lửng, nhà trọ không chung chủ, phòng trọ dịch vụ, phòng ở ghép*.

### D.1b — Mặt bằng kinh doanh / kiot (phương án có mặt tiền)

| Loại | Giá (VND/tháng) | Chi tiết | Nguồn |
|---|---|---|---|
| Mặt bằng 30 m² Ngũ Hành Sơn | **15.000.000** | Phù hợp nail/văn phòng/spa/shop — **quá đắt cho mô hình này** | `[SNIPPET-MƠ-HỒ]` — ứng viên: https://mogi.vn/da-nang/quan-ngu-hanh-son/thue-mat-bang-cua-hang-shop · https://alonhadat.com.vn/nha-dat/cho-thue/mat-bang/da-nang/587/quan-ngu-hanh-son.html |
| Mặt bằng 95 m² (5×19 m) Ngũ Hành Sơn | **6.500.000** | Cọc 1 tháng, thanh toán 6 tháng/lần, WC riêng — **giá/m² rẻ hơn hẳn** | `[SNIPPET-MƠ-HỒ]` — cùng nhóm ứng viên |
| Mặt bằng **< 30 m² trong ngõ/hẻm** | **3.000.000 – 5.000.000** | Kiot/cửa hàng nhỏ khu dân cư — **phù hợp nhất với mô hình 15–40 máy** | `[XÁC MINH-SNIPPET]` |

Nguồn tra thêm:
- https://phongtro123.com/cho-thue-mat-bang-quan-ngu-hanh-son-da-nang
- https://muaban.net/bat-dong-san/cho-thue-mat-bang-kinh-doanh-quan-ngu-hanh-son-da-nang
- https://batdongsan.com.vn/cho-thue-sang-nhuong-cua-hang-ki-ot-da-nang
- https://nhadat.cafeland.vn/cho-thue/mat-bang-tai-da-nang/
- https://alonhadat.com.vn/nha-dat/cho-thue/mat-bang/3/da-nang.html

### D.1c — Kết luận mặt bằng cho mô hình

| Phương án | Chi phí (VND/tháng) | Nhận xét |
|---|---|---|
| **A. Phòng trọ kiêm kho** (khuyến nghị giai đoạn 0) | **3.200.000 – 4.500.000** | 40 m² ở Võ Văn Đồng thừa sức chứa 40 laptop + bàn kiểm máy. Nếu thành viên nhóm đã thuê trọ sẵn → **chi phí biên ≈ 0**, đây là lợi thế lớn nên nêu trong proposal |
| B. Kiot nhỏ trong hẻm | 3.000.000 – 5.000.000 | Có mặt tiền, tăng niềm tin, nhưng chưa cần ở giai đoạn đầu |
| C. Mặt bằng mặt tiền 30 m² | 15.000.000 | **Loại bỏ** — không khả thi với doanh thu dự kiến |
| D. 100% mô hình giao tận nơi, không mặt bằng | 0 | Đáng cân nhắc nhất: dùng phòng trọ + ship |

> **Chưa có số:** điện, nước, internet, phí gửi xe, phí vệ sinh của phòng trọ → `[KHÔNG TÌM ĐƯỢC]`, nhóm hỏi trực tiếp chủ trọ.

## D.2. Nhân sự

### D.2a — Lương tối thiểu vùng 2026 (căn cứ pháp lý — Nghị định 293/2025/NĐ-CP, hiệu lực 01/01/2026)

| Vùng | Lương tối thiểu THÁNG (VND) | Lương tối thiểu GIỜ (VND) |
|---|---|---|
| **Vùng II** | **4.730.000** | **22.700** |
| **Vùng III** | **4.140.000** | **20.000** |
| **Vùng IV** | **3.700.000** | **17.000** |

- Mức tăng chung: **+7,2%** so với trước 01/01/2026
- **Đà Nẵng được phân vào cả 3 vùng: II, III và IV** (tuỳ địa bàn cấp xã/phường)
- Nguồn:
  - https://luatvietnam.vn/lao-dong-tien-luong/muc-luong-toi-thieu-vung-tai-thanh-pho-da-nang-nam-2026-562-105277-article.html
  - https://thuvienphapluat.vn/phap-luat-doanh-nghiep/bai-viet/muc-luong-toi-thieu-vung-thanh-pho-da-nang-tu-01-01-2026-15957.html
  - https://nhansu.vn/phap-luat-lao-dong/muc-luong-toi-thieu-vung-2026-da-nang-la-bao-nhieu-41233.html
  - https://thuvienphapluat.vn/phap-luat-doanh-nghiep/bai-viet/muc-luong-toi-thieu-vung-2026-muc-luong-co-so-2026-va-mot-so-luu-y-quan-trong-18204.html
  - https://xaydungchinhsach.chinhphu.vn/de-xuat-muc-luong-toi-thieu-vung-tu-1-1-2026-119250718084713755.htm
  - https://baoangiang.com.vn/muc-luong-toi-thieu-vung-2026-tang-bao-nhieu-phan-tram-a472794.html
  - https://thuvienphapluat.vn/lao-dong-tien-luong/muc-luong-toi-thieu-vung-hien-nay-tai-thanh-pho-da-nang-la-bao-nhieu-53981.html

> ⚠ **CHƯA XÁC MINH ĐƯỢC:** P. Hoà Hải / Ngũ Hành Sơn thuộc **vùng nào** trong 3 vùng trên. Snippet chỉ liệt kê "Hải Châu, Thanh Khê, Sơn Trà..." thuộc Vùng II. Hoà Hải là phường nội thành nên **nhiều khả năng thuộc Vùng II (22.700 VND/giờ)** nhưng **phải kiểm tra danh mục địa bàn cấp xã kèm Nghị định 293/2025/NĐ-CP**. Trong mô hình, dùng **22.700 VND/giờ** làm sàn pháp lý là an toàn.

### D.2b — Lương part-time thực tế tại Đà Nẵng (mức thị trường, cao hơn sàn)

| Công việc | Mức lương | Nguồn |
|---|---|---|
| Nhân viên phục vụ, bán hàng | **20.000 – 35.000 VND/giờ** | https://vn.joboko.com/blog/luong-part-time-nwi5750 |
| Telesale, chăm sóc khách hàng | **25.000 – 50.000 VND/giờ** | https://vn.joboko.com/blog/luong-part-time-nwi5750 |
| Gia sư dạy kèm | **80.000 – 200.000 VND/buổi** | https://vn.joboko.com/blog/luong-part-time-nwi5750 |
| Cộng tác viên sự kiện | **150.000 – 500.000 VND/ngày** | https://vn.joboko.com/blog/luong-part-time-nwi5750 |

Nguồn tra thêm:
- https://thuvienphapluat.vn/phap-luat/nam-2026-sinh-vien-di-lam-them-lam-parttime-o-tphcm-ha-noi-duoc-tra-luong-theo-gio-toi-thieu-la-bao-263082.html
- https://vn.indeed.com/career/nhân-viên-part-time/salaries
- https://careerviet.vn/viec-lam/parttime-tai-da-nang-kl511-vi.html
- https://careerviet.vn/viec-lam/part-time-ke1-vi.html

### D.2c — Mức lương nên dùng trong mô hình

| Vai trò | Mức đề xuất `[GIẢ ĐỊNH]` | Căn cứ |
|---|---|---|
| CTV giao/nhận máy + kiểm máy (sinh viên) | **25.000 – 30.000 VND/giờ** | Nằm giữa dải phục vụ/bán hàng ĐN (20–35K) và **trên** sàn pháp lý Vùng II (22,7K) |
| CTV trực mùa thi cao điểm (theo ca/ngày) | **150.000 – 250.000 VND/ngày** | Neo theo dải CTV sự kiện ĐN (150–500K/ngày), lấy nửa dưới |
| Kỹ thuật cài đặt/xử lý sự cố | **30.000 – 50.000 VND/giờ** | Neo theo dải telesale/CSKH (25–50K), lấy nửa trên vì cần kỹ năng |
| Founder/thành viên nhóm | 0 (không tính lương giai đoạn đầu) | Chuẩn mực proposal sinh viên — **nhưng nên tính "chi phí cơ hội" ở một dòng riêng để bảng P&L trung thực** |

## D.3. Chi phí giao nhận (ship nội thành Đà Nẵng)

### Ahamove — bảng giá tham khảo

| Dịch vụ | Giá | Nguồn |
|---|---|---|
| **Giao tiêu chuẩn nội tỉnh** | **10.000 – 20.000 VND/km** | https://ahamove.com/giao-hang-tieu-chuan-la-gi |
| **Siêu tốc – Đồ ăn** | 3 km đầu: **18.000 VND**; trên 3 km: **5.000 VND/km** | https://topkinhdoanh.net/bang-gia-ahamove/ |
| **Siêu tốc** | 4 km đầu: **23.000 VND**; trên 4 km: **5.000 VND/km** | https://topkinhdoanh.net/bang-gia-ahamove/ |
| **Siêu rẻ** | 4 km đầu: **18.000 VND**; trên 4 km: **4.000 VND/km** | https://topkinhdoanh.net/bang-gia-ahamove/ |

Nguồn tra thêm:
- https://ahamove.com/service/aha-delivery/price (bảng giá chính thức dịch vụ xe máy)
- https://ahamove.com/tinh-tien-ship-theo-km
- https://ahamove.com/giao-hang-nhanh-trong-1-ngay
- https://hellodanang.vn/danh-gia/ahamove-dich-vu-ship-hang-hoa-toc-tai-da-nang (review Ahamove tại Đà Nẵng)
- https://topkinhdoanh.com/bang-gia-ahamove/

> ⚠ Bảng giá trên là **bảng giá tham khảo chung của Ahamove, KHÔNG xác nhận là bảng giá riêng Đà Nẵng 2026**. Trang gốc cảnh báo *"bảng giá có thể thay đổi theo thời gian và địa điểm cụ thể"*. **Nhóm bắt buộc mở app Ahamove, nhập điểm đi ĐH FPT Đà Nẵng → điểm đến vài KTX/trọ quanh Hoà Hải và chụp màn hình giá thật.** Đây là số liệu sơ cấp rất dễ lấy.

### `[KHÔNG TÌM ĐƯỢC]`: Grab Express Đà Nẵng, Be Giao hàng Đà Nẵng
Hết ngân sách WebSearch của phiên. Nhóm tự mở app.

### Ước tính chi phí giao nhận cho mô hình
Bán kính phục vụ chính = quanh ĐH FPT Đà Nẵng (Hoà Hải, FPT City, Nam Việt Á, làng ĐH) → **ước tính 2–5 km** `[GIẢ ĐỊNH]`.

| Kịch bản | Chi phí 1 chiều | Chi phí khứ hồi (giao + thu hồi) |
|---|---|---|
| Tự giao bằng xe máy của nhóm | chỉ tốn xăng, ~5.000–10.000 VND `[GIẢ ĐỊNH]` | 10.000 – 20.000 VND |
| Ahamove Siêu rẻ (≤4 km) | 18.000 VND | **36.000 VND** |
| Ahamove Siêu tốc (≤4 km) | 23.000 VND | **46.000 VND** |

> **Phát hiện chí mạng cho unit economics:** nếu giá thuê 1 ngày là **50.000 VND** mà ship khứ hồi qua Ahamove Siêu tốc đã là **46.000 VND**, thì **biên lợi nhuận gần như bằng 0**. → Hai hàm ý bắt buộc cho proposal: (1) **tự giao bằng xe máy** trong giai đoạn đầu, hoặc (2) **thu phí giao nhận riêng** / bắt buộc khách tự đến lấy với gói giá rẻ. Đây là một trong những insight quan trọng nhất của file này.

## D.4. Hạ tầng website

### D.4a — Hosting / VPS Việt Nam

| Nhà cung cấp | Sản phẩm | Giá (VND/tháng) | Nguồn |
|---|---|---|---|
| **Vietnix** | **VPS** (cấu hình từ 2 CPU / SSD) | **từ 157.000** | https://vietnix.vn/vps/ |
| Vietnix | Hosting | **từ 20.000** | https://azdigi.com/blog/kien-thuc-hosting/top-5-hosting-gia-re-tot-nhat-viet-nam-2026 |
| **AZDIGI** | AZDIGI Pro (gói thấp) | **từ 29.000** | https://azdigi.com/blog/kien-thuc-hosting/top-5-hosting-gia-re-tot-nhat-viet-nam-2026 |
| AZDIGI | Pro Platinum (NVMe, Platinum CPU) — *"cân bằng giá/chất lượng tốt"* | **từ 55.000** | https://azdigi.com/blog/kien-thuc-hosting/top-5-hosting-gia-re-tot-nhat-viet-nam-2026 |
| **TinoHost** | Cloud Hosting gói thấp nhất | **từ 9.000** | https://azdigi.com/blog/kien-thuc-hosting/top-5-hosting-gia-re-tot-nhat-viet-nam-2026 |
| TinoHost | Gói **dùng được thực tế cho WordPress** | **~43.000** | https://azdigi.com/blog/kien-thuc-hosting/top-5-hosting-gia-re-tot-nhat-viet-nam-2026 |

> ⚠ Lưu ý nguồn: 5/6 con số trên đến từ **blog của AZDIGI** — tức **nguồn có xung đột lợi ích** (nhà cung cấp tự so sánh với đối thủ). Nhóm nên mở trực tiếp trang bảng giá của từng bên. Con số Vietnix 157.000 VND/tháng là từ **chính trang Vietnix**, đáng tin hơn.

Nguồn tra thêm:
- https://azdigi.com/blog/kien-thuc-vps/bang-gia-thue-vps-viet-nam ("Bảng giá thuê VPS Việt Nam 2026")
- https://azdigi.com/blog/kien-thuc-vps/top-nha-cung-cap-vps-viet-nam
- https://azdigi.com/blog/kien-thuc-hosting/bang-gia-hosting-viet-nam-2026
- https://azdigi.com/blog/kien-thuc-hosting/bang-gia-hosting-viet-nam-so-sanh (so sánh 10 nhà cung cấp)
- https://azdigi.com/blog/kien-thuc-hosting/top-10-nha-cung-cap-hosting-tot-nhat-viet-nam-2026
- https://azdigi.com/blog/kien-thuc-hosting/so-sanh-5-nha-cung-cap-hosting-viet-nam-2026

### `[KHÔNG TÌM ĐƯỢC]`: Vercel, Railway, Viettel IDC
Hết ngân sách WebSearch. **Gợi ý cho proposal:** Vercel và Railway đều có **free tier** đủ dùng cho một website đặt thuê quy mô 15–40 máy → nhóm nên **đặt chi phí hosting năm 1 = 0 VND** và ghi rõ lý do (free tier), rồi dự phòng **150.000–200.000 VND/tháng** khi phải nâng cấp lên VPS Việt Nam. Số 0 này phải kiểm chứng lại trên trang pricing chính thức.

### D.4b — Tên miền

| Loại | Chi phí | Chi tiết | Nguồn |
|---|---|---|---|
| **.vn cấp 2 — NĂM ĐẦU** | **770.000 VND** | = Lệ phí đăng ký **200.000** + Phí duy trì **350.000** + Dịch vụ tài khoản quản trị **200.000** | https://helpdesk.inet.vn/knowledgebase/bang-gia-ten-mien-va-cac-loai-phi |
| **.vn cấp 2 — NĂM SAU** | **460.000 VND/năm** | phí duy trì | https://helpdesk.inet.vn/knowledgebase/bang-gia-ten-mien-va-cac-loai-phi |
| .vn (dải chung theo nhà đăng ký) | **40.000 – 450.000 VND/năm** | tuỳ loại tên miền và nhà đăng ký | https://vinahost.vn/phi-duy-tri-ten-mien/ |
| **Thuế** | **.vn KHÔNG chịu VAT**; **tên miền quốc tế (.com/.net/.org) chịu VAT 10%** | quan trọng khi lập dự toán | https://helpdesk.inet.vn/knowledgebase/bang-gia-ten-mien-va-cac-loai-phi |
| .org (tham chiếu quốc tế) | đăng ký năm đầu **319.000 VND**, duy trì **329.000 VND/năm** | năm đầu thường KM rẻ hơn năm sau | https://helpdesk.inet.vn/knowledgebase/bang-gia-ten-mien-va-cac-loai-phi |

### `[KHÔNG TÌM ĐƯỢC]`: giá cụ thể tên miền **.com**
Snippet chỉ đưa ví dụ .org. **Ước lượng an toàn để dựng mô hình: dùng chính con số .org (≈ 320.000 – 330.000 VND/năm + VAT 10%) làm proxy cho .com** `[GIẢ ĐỊNH]`, và kiểm chứng lại tại:
- https://www.bkns.vn/ten-mien/bang-gia-ten-mien.html
- https://vinahost.vn/bang-gia-ten-mien/
- https://vietnix.vn/bang-gia-ten-mien/
- https://www.matbao.net/ten-mien/bang-gia-ten-mien.html

### D.4c — Tổng OPEX hạ tầng website (năm 1)

| Khoản | Thấp (VND/năm) | Cao (VND/năm) |
|---|---|---|
| Hosting/VPS | 0 (free tier Vercel/Railway `[GIẢ ĐỊNH]`) | 157.000 × 12 = **1.884.000** (VPS Vietnix) |
| Tên miền .vn năm đầu | — | **770.000** |
| Tên miền .com năm đầu (proxy .org + VAT) | ~**352.000** | — |
| **Tổng** | **~352.000** | **~2.654.000** |

> **Đây là chi phí gần như không đáng kể so với CAPEX laptop.** Trong proposal, không nên phóng đại phần công nghệ; giá trị nằm ở vận hành và tài sản máy.

## D.5. Các khoản OPEX chưa có số liệu

| Khoản | Trạng thái | Gợi ý cách lấy |
|---|---|---|
| Điện, nước, internet tại kho/trọ | `[KHÔNG TÌM ĐƯỢC]` | Hỏi chủ trọ; thường điện 3.500–4.000đ/kWh giá trọ, nhưng **chưa xác minh** |
| Marketing (chạy ads Facebook nhóm sinh viên FPT ĐN) | `[KHÔNG TÌM ĐƯỢC]` | Meta Ads Manager, đặt ngân sách thử |
| In ấn poster/standee, tem tài sản | `[KHÔNG TÌM ĐƯỢC]` | Xin báo giá tiệm in ĐN |
| Bảo hiểm thiết bị / rủi ro mất máy | `[KHÔNG TÌM ĐƯỢC]` | Thường không có sản phẩm phù hợp ở quy mô này → thay bằng **chính sách đặt cọc + CMND/CCCD + thẻ SV** |
| Chi phí thu hồi nợ / máy không trả | `[KHÔNG TÌM ĐƯỢC]` | Dùng tỉ lệ dự phòng `[GIẢ ĐỊNH]` |
| Thuế hộ kinh doanh / đăng ký kinh doanh | `[KHÔNG TÌM ĐƯỢC]` | Tra Nghị định về hộ kinh doanh; ngưỡng doanh thu chịu thuế |

---

# PHẦN E — CHI PHÍ SỬA CHỮA & BẢO TRÌ

Đây là dòng chi phí quyết định sự sống còn: **40 máy cũ chạy liên tục sẽ hỏng**. Bảng dưới dùng để đặt tỉ lệ dự phòng bảo trì trong P&L.

## Bảng E.1 — Giá linh kiện & công thay thế (VN, 2025–2026)

| Hạng mục | Giá (VND) | Chi tiết | Nguồn | Độ tin cậy |
|---|---|---|---|---|
| **Màn hình laptop HP 14"** | **686.000 – 1.025.000** | Tuỳ model và chất lượng màn | `[SNIPPET-MƠ-HỒ]` — ứng viên: https://laptop911.vn/man-hinh-hp-14-inch-gia-bao-nhieu · https://benhvienlaptop.com/man-hinh-laptop-hp/ | trung bình |
| **Màn hình 11–14" (mặt bằng chung)** | **1.500.000 – 3.000.000** | Dải cao hơn hẳn dải HP ở trên — nhiều khả năng đã gồm công + màn chính hãng | https://bcavn.com/tin-tuc/thay-man-hinh-laptop-bao-nhieu-tien-30474.html | `[XÁC MINH-SNIPPET]` |
| Màn hình Dell 14" FHD | chưa hiện giá | — | https://linhkienlaptopthaiha.com/thay-man-hinh-laptop-dell-14-inch-full-hd-1-2-257013.html | cần mở trang |
| Bảng giá màn hình tổng hợp | — | Bảng giá HCM/HN cập nhật 24/8/2026 | https://dienthoaivui.com.vn/sua-chua-laptop/thay-man-hinh-laptop | cần mở trang |
| **Pin laptop (mặt bằng chung)** | **250.000 – >2.000.000** | Dải rất rộng | `[SNIPPET-MƠ-HỒ]` — ứng viên: https://tritienlaptop.com/thay-pin-laptop-het-bao-nhieu-tien/ · https://www.hoangvucenter.vn/vi-vn/bang-gia-thay-pin-laptop.html | trung bình |
| **Pin Dell Vostro/Inspiron** | **350.000 – 1.800.000** | dòng phổ thông | https://lacviet.vn/en/thay-pin-laptop-dell/ | `[XÁC MINH-SNIPPET]` |
| **Pin Dell Latitude / XPS / Precision / Alienware** | **1.200.000 – 2.500.000** | ⚠ **Latitude nằm ở nhóm ĐẮT** — ảnh hưởng trực tiếp nếu nhóm chọn Latitude 5400/5410 | https://lacviet.vn/en/thay-pin-laptop-dell/ | `[XÁC MINH-SNIPPET]` |
| Pin Dell (giá khuyến mại) | **từ 850.000** | ngày 11/8/2026, pin chính hãng mới 100% | https://dienthoaivui.com.vn/sua-chua-laptop/thay-pin-laptop/thay-pin-laptop-dell | `[XÁC MINH-SNIPPET]` |
| Bảng giá pin Dell Latitude riêng | chưa hiện giá | — | https://linhkienlaptopthaiha.com/pin-laptop-dell-latitude-2-1-533473.html | cần mở trang |
| **Bàn phím (mặt bằng chung)** | **250.000 – 3.000.000** | tuỳ thương hiệu và đời máy | https://phongvu.vn/cong-nghe/thay-ban-phim-laptop-bao-nhieu-tien/ | `[XÁC MINH-SNIPPET]` |
| **Bàn phím loại OEM** | **200.000 – 300.000** | lựa chọn tiết kiệm cho máy cho thuê | `[SNIPPET-MƠ-HỒ]` — ứng viên: https://khoavang.vn/blog/sua-ban-phim-laptop-het-bao-nhieu-tien-p3099.html · https://tanphatad.com/sua-va-thay-ban-phim-laptop-gia-bao-nhieu-tien/ | trung bình |
| **Bàn phím chính hãng** | **400.000 – 1.000.000** | tuỳ dòng máy | cùng nhóm trên | trung bình |
| Bàn phím (FastCare) | **từ 350.000**, lấy sau 1 giờ | thời gian sửa nhanh — quan trọng với mô hình | https://fastcare.vn/thay-ban-phim-laptop | `[XÁC MINH-SNIPPET]` |
| Bàn phím (Thành Trang) | lấy ngay 45 phút | bảng giá T7/2025 | https://thanhtrangmobile.com/thay-ban-phim-laptop/ | cần mở trang |
| **SSD 256GB** | **từ 550.000** (Patriot) | chênh lệch tuỳ thương hiệu | https://dienthoaivui.com.vn/linh-kien-laptop/o-cung | `[XÁC MINH-SNIPPET]` |
| SSD 512GB | `[KHÔNG TÌM ĐƯỢC]` | — | https://dienthoaivui.com.vn/linh-kien-laptop/o-cung | — |
| **Mainboard (main)** | `[KHÔNG TÌM ĐƯỢC]` | Hết ngân sách WebSearch | — | — |

Nguồn tra thêm:
- https://fastcare.vn/blog/gia-thay-ban-phim-laptop.html
- https://benhvienlaptop.com/pin-laptop/
- https://benhvienlaptop.com/pin-laptop-dell/
- https://doctorlaptop.com.vn/pin-laptop-dell-13429.html
- https://linhkienlaptopthaiha.com/pin-laptop-dell-2-1-305193.html
- https://lacviet.vn/en/mua-o-cung-ssd-cho-laptop-dell/
- https://dienthoaivui.com.vn/sua-chua-laptop/thay-pin-laptop/

## E.2. Hàm ý cho mô hình tài chính

### Chi phí sửa trung bình cho 1 sự cố `[GIẢ ĐỊNH dựa trên dải thật ở trên]`

| Loại sự cố | Tần suất kỳ vọng | Chi phí/lần |
|---|---|---|
| Pin chai (phải thay) | Cao — máy cũ 2018–2020, pin đã 6–8 năm | **850.000 – 2.500.000** (Latitude ở nhóm đắt) |
| Bàn phím liệt phím (dùng nhiều) | Trung bình | **200.000 – 400.000** (dùng OEM) |
| Màn hình vỡ/sọc (rơi khi vận chuyển) | Thấp nhưng đắt | **686.000 – 3.000.000** |
| SSD hỏng | Thấp | **550.000+** |
| Mainboard | Rất thấp, nhưng có thể **= giá 1 máy mới** → thường thanh lý máy | `[KHÔNG TÌM ĐƯỢC]` |

### ⚠ Cảnh báo lớn nhất phần E: **PIN**
- Máy cũ Gen 8 (2018) đến 2026 đã **8 năm tuổi pin**. Pin chai gần như chắc chắn.
- Với **ThinkPad T480**: có pin ngoài tháo rời (hot-swap) → **lợi thế vận hành rất lớn**, có thể mua pin rời dự phòng, đổi trong 30 giây thay vì tháo máy.
- Với **Dell Latitude 5400/5410**: pin liền, và snippet cho thấy Latitude thuộc **nhóm pin đắt 1,2–2,5 triệu**.
- **Khuyến nghị mạnh cho proposal:** ưu tiên **ThinkPad T480** không chỉ vì giá 6,2 triệu mà vì **kiến trúc pin đôi/tháo rời làm giảm chi phí bảo trì và downtime** — đây là một lập luận kỹ thuật sắc, dễ ghi điểm. (Cần nhóm tự xác minh lại đặc điểm pin T480 vì file này chưa có nguồn trích dẫn cho chi tiết đó.)

### Tỉ lệ dự phòng bảo trì đề xuất
`[GIẢ ĐỊNH]` — đặt **8–12% doanh thu**, hoặc **150.000 – 250.000 VND/máy/năm** cho bảo trì thường xuyên, **cộng riêng** một quỹ sự cố lớn. Nhóm nên tính lại khi có số tần suất hỏng thực tế sau 1–2 tháng vận hành thử.

---

# PHẦN F — NGUỒN VỐN CHO SINH VIÊN KHỞI NGHIỆP

## Bảng F.1 — Các cuộc thi / giải thưởng

| Cuộc thi | Đơn vị tổ chức | Giải thưởng | Đối tượng | Nguồn |
|---|---|---|---|---|
| **FPT Biz Talent 2025** ⭐ | **Trường ĐH FPT** | **Tổng giải thưởng 260.000.000 VND tiền mặt** + **chuyến trải nghiệm Singapore** cho quán quân mỗi bảng | **Bảng A: SV ĐH/CĐ/Trung cấp/Học viện** · Bảng B: HS THPT · Toàn quốc | https://daihoc.fpt.edu.vn/tin-noi-bat-muc-tin-tuc/fpt-biz-talent-2025-truong-dh-fpt-kien-tao-the-he-doanh-nhan-tre/ |
| **Startup Wheel 2026** | BSSC | **Giải Nhất: tổng 400.000.000 VND** (trong đó **hiện kim 150.000.000 VND**, còn lại hiện vật/dịch vụ). **Top 5:** pitch trước NĐT tại Đêm chung kết + đào tạo chuyên sâu miễn phí + **trưng bày miễn phí 2 ngày tại InnoEx 2026 (trị giá 2.000 USD)**. **Top 30:** pitch bán kết + đào tạo miễn phí | Có **bảng riêng "Vietnam Youth Startup"** | https://startupwheel.vn/vi/giai-thuong/ · https://startupwheel.vn/vi/top-100-startup-wheel-2026/ |
| **SV-STARTUP lần VIII (2026)** | **Bộ GD&ĐT** | Cơ cấu 2026: **15 giải Nhất, 30 giải Nhì, 55 giải Ba, 34 giải Khuyến khích**. ⚠ **Tiền thưởng 2026 chưa công bố trong snippet.** Tham chiếu **SV Startup 2025: giải Nhất 15.000.000 VND/lĩnh vực; giải Nhì 10.000.000 VND/bảng** | HS & SV toàn quốc | https://tuoitre.vn/15-du-an-khoi-nghiep-cua-hoc-sinh-sinh-vien-gianh-giai-nhat-sv-startup-2026-20260419203319353.htm |
| Tuổi Trẻ Startup Award 2026 | Báo Tuổi Trẻ | `[KHÔNG TÌM ĐƯỢC]` — mới khởi động | — | https://daidoanket.vn/khoi-dong-giai-thuong-tuoi-tre-startup-award-2026.html |
| QVIC 2026 (Qualcomm Vietnam Innovation Challenge) | Qualcomm | `[KHÔNG TÌM ĐƯỢC]` — thiên về deep-tech, **có thể không phù hợp** với mô hình cho thuê laptop | — | https://www.techsignin.com/010426-startup-viet-giai-bai-toan-toan-cau-qvic/ |

## F.2. SV-STARTUP 2026 — chi tiết bổ sung

- Tổ chức trong khuôn khổ **Ngày hội khởi nghiệp quốc gia của học sinh, sinh viên lần thứ 8**.
- **Lĩnh vực khuyến khích:** công nghiệp/chế tạo/AI/STEM; nông nghiệp/môi trường/năng lượng; **giáo dục**, văn hoá, du lịch, tài chính; y tế/sức khoẻ/đời sống; **kinh doanh tạo tác động xã hội**.
  - 👉 **Dự án cho thuê laptop đi thi hoàn toàn có thể xếp vào "giáo dục" và "kinh doanh tạo tác động xã hội"** (bảo đảm quyền được thi công bằng cho SV không đủ điều kiện thiết bị). Nên dùng framing này khi nộp.
- Định hướng 2026: **"Làm thật – Thi thật"**, chuyển từ "ý tưởng" sang "sản phẩm", từ "phong trào" sang "hiệu quả thực chất" → **ban giám khảo 2026 ưu tiên đội đã có doanh thu thật/khách hàng thật**. Hàm ý: nhóm nên **chạy thử 5–10 máy trước khi nộp** và đưa số liệu thật vào proposal.
- Nguồn:
  - https://vjst.vn/sv-startup-2026-chuyen-bien-ro-net-tu-y-tuong-sang-san-pham-tu-phong-trao-sang-hieu-qua-thuc-chat-86335.html
  - https://doanhnhan.congly.vn/sv-startup-2026-lam-that-thi-that-hieu-qua-thuc-chat.html
  - https://diendandoanhnghiep.vn/sv_startup-2026-y-tuong-khoi-nghiep-hom-nay-la-su-truong-thanh-doanh-nghiep-tuong-lai-10177463.html
  - https://www.vista.gov.vn/vi/news/cac-linh-vuc-khoa-hoc-va-cong-nghe/khoi-nguon-sang-tao-tre-tai-sv-startup-2025-11260.html (giải 2025)
  - Thông báo cấp trường (mẫu tham khảo): https://smia.iuh.edu.vn/news.html@detail@221@1111@Thong-bao-dang-ky-tham-gia-Cuoc-thi-%E2%80%9CHoc-sinh,-Sinh-vien-Khoi-nghiep-lan-thu-8-%E2%80%93-Nam-2026-(SV.STARTUP-2026) · https://usth.edu.vn/khoi-dong-cuoc-thi-hoc-sinh-sinh-vien-voi-y-tuong-khoi-nghiep-lan-thu-viii-nam-2026-29630/ · https://fbe.ftu.edu.vn/cuoc-thi-hoc-sinh-sinh-vien-voi-y-tuong-khoi-nghiep-lan-thu-viii-sv-startup-2026-2/

## F.3. FPT Biz Talent — chi tiết bổ sung (⭐ SÂN NHÀ, ƯU TIÊN CAO NHẤT)

- **Cấu trúc 4 vòng:** Khởi động → Phóng thử nghiệm → Tham vấn chuyên gia → Cất cánh.
- **Chủ đề:** kế hoạch khởi nghiệp **kết hợp ứng dụng khoa học công nghệ** vào mô hình kinh doanh — Giáo dục, Y tế, Nông nghiệp, Công nghiệp...
  - 👉 Mô hình **website đặt thuê laptop** khớp trực tiếp: có yếu tố công nghệ (nền tảng đặt thuê) + lĩnh vực giáo dục.
- **Quán quân 2025:** liên quân ĐH FPT (FPTU) + ĐH Kinh tế Quốc dân (NEU) với dự án ứng dụng AI cá nhân hoá lộ trình học tập.
- Nguồn:
  - https://www.vista.gov.vn/vi/news/khoi-nghiep-doi-moi-sang-tao/khoi-dong-cuoc-thi-khoi-nghiep-quy-mo-toan-quoc-fpt-biz-talent-2025-uom-mam-tai-nang-doanh-nhan-doi-moi-sang-tao-tuong-lai-11452.html
  - https://mst.gov.vn/fpt-biz-talent-2025-tim-kiem-va-uom-mam-the-he-doanh-nhan-doi-moi-sang-tao-viet-nam-197250616201306032.htm
  - https://vnexpress.net/sinh-vien-fptu-neu-thang-giai-khoi-nghiep-nho-ung-dung-ai-vao-giao-duc-4939846.html
  - https://chungta.vn/cong-nghe/du-an-giao-duc-ung-dung-tri-tue-nhan-tao-dang-quang-tai-fpt-biz-talent-2025-1140285.html
  - https://feexp.space/fpt-biz-talent-2025
  - https://daihoc.fpt.edu.vn/tin-noi-bat-muc-tin-tuc/tu-lop-hoc-den-thuong-truong-3-du-an-cua-sinh-vien-fptu-tien-thang-chung-ket-fpt-biz-talent-2025/
  - https://fschool.fpt.edu.vn/vong-ban-ket-fpt-biz-talent-2025/

## F.4. ❌ DEADLINE — DỮ LIỆU THIẾU NGHIÊM TRỌNG

**Không tìm được deadline đăng ký cụ thể của bất kỳ cuộc thi nào.** Mọi snippet đều là tin đưa sau khi trao giải. Nhóm **phải** tự tra:
- SV-STARTUP: theo công văn Bộ GD&ĐT gửi các trường; hỏi phòng CTSV ĐH FPT ĐN.
- FPT Biz Talent: hỏi trực tiếp phòng ban tổ chức của Trường ĐH FPT — **lợi thế sân nhà, nhóm là SV FPT**.
- Startup Wheel: mở https://startupwheel.vn/ (snippet ghi "đơn đăng ký được mở tại startupwheel.vn").

## F.5. ❌ `[KHÔNG TÌM ĐƯỢC]`: quỹ / vườn ươm
- **DNES (Vườn ươm doanh nghiệp Đà Nẵng)** — hết ngân sách WebSearch, chưa tra được. **Đây là nguồn vốn địa phương quan trọng nhất cần bổ sung**, vì dự án đặt tại Đà Nẵng.
- Các quỹ đầu tư thiên thần, chương trình hỗ trợ khởi nghiệp của TP Đà Nẵng — chưa tra.
- Vay vốn sinh viên / vay tín chấp — chưa tra.

## F.6. So sánh quy mô giải thưởng vs nhu cầu vốn của dự án

| Nguồn | Số tiền có thể nhận | Mua được bao nhiêu máy (giá 6.200.000 VND/máy — T480) |
|---|---|---|
| SV Startup — giải Nhất (tham chiếu 2025) | 15.000.000 VND | ~2 máy |
| SV Startup — giải Nhì (tham chiếu 2025) | 10.000.000 VND | ~1–2 máy |
| Startup Wheel — giải Nhất (hiện kim) | 150.000.000 VND | **~24 máy** |
| FPT Biz Talent — tổng giải thưởng toàn cuộc thi | 260.000.000 VND (chia nhiều giải) | — (không thể nhận toàn bộ) |

> **Kết luận cho proposal:** giải thưởng cuộc thi **không đủ** để tự tài trợ toàn bộ CAPEX 15–40 máy, nhưng **giải Nhất Startup Wheel (hiện kim 150 triệu) đủ tài trợ ~24 máy** — tức gần trọn kịch bản quy mô trung bình. Nên trình bày cơ cấu vốn nhiều nguồn: vốn góp thành viên + giải thưởng + tái đầu tư lợi nhuận + (nếu có) vườn ươm ĐN.

---

# PHẦN G — KHUNG DỰNG P&L 12 THÁNG (công thức + số đầu vào)

> ⚠ **Toàn bộ phần này là KHUNG TÍNH, không phải dữ liệu.** Các con số đánh dấu `[GIẢ ĐỊNH]` là do người viết đặt ra để nhóm có điểm khởi đầu. Mọi con số THẬT đã nêu ở Phần A–F.

## G.1. CAPEX — 3 kịch bản quy mô

Dùng giá **6.200.000 VND/máy** (ThinkPad T480, nguồn laptops.vn) làm giá cơ sở:

| Kịch bản | Số máy | CAPEX laptop (VND) | CAPEX khác `[GIẢ ĐỊNH]` | Tổng CAPEX ước tính |
|---|---|---|---|---|
| Tối thiểu (MVP) | 15 | 93.000.000 | ~7.000.000 | **~100.000.000** |
| Cơ sở | 25 | 155.000.000 | ~10.000.000 | **~165.000.000** |
| Mở rộng | 40 | 248.000.000 | ~15.000.000 | **~263.000.000** |

Với kịch bản rẻ hơn (Dell Latitude 5400 @ 5.000.000 VND/máy — laptop15.vn):

| Kịch bản | Số máy | CAPEX laptop (VND) |
|---|---|---|
| Tối thiểu | 15 | **75.000.000** |
| Cơ sở | 25 | **125.000.000** |
| Mở rộng | 40 | **200.000.000** |

## G.2. Các dòng chi phí cố định hàng tháng (dùng số thật ở Phần D)

| Khoản | Thấp (VND/tháng) | Cao (VND/tháng) | Nguồn số |
|---|---|---|---|
| Mặt bằng/kho | 0 (dùng trọ sẵn có) – 3.200.000 | 4.500.000 | D.1 |
| Hosting/VPS | 0 (free tier) | 157.000 | D.4a |
| Tên miền (quy về tháng) | ~29.000 (.com) | ~64.000 (.vn năm đầu) | D.4b |
| Nhân sự CTV | `[GIẢ ĐỊNH]` — tính theo giờ thực tế × 25.000–30.000 VND/giờ | | D.2 |
| Điện/nước/internet | `[KHÔNG TÌM ĐƯỢC]` | | — |
| Marketing | `[KHÔNG TÌM ĐƯỢC]` | | — |

## G.3. Công thức unit economics — mỗi máy

```
Doanh thu/máy/tháng   = Giá thuê/ngày × Số ngày thuê được/tháng
Số ngày thuê được     = 30 × Tỉ lệ lấp đầy (utilization)
Chi phí biến đổi/lượt = Ship khứ hồi + Chi phí vệ sinh/cài lại máy
Biên góp/máy/tháng    = Doanh thu/máy/tháng − Chi phí biến đổi − Dự phòng bảo trì
Hoàn vốn/máy (tháng)  = Giá mua máy ÷ Biên góp/máy/tháng
Điểm hoà vốn (số máy) = Tổng chi phí cố định/tháng ÷ Biên góp/máy/tháng
```

### Bảng G.3 — Độ nhạy: doanh thu/máy/tháng theo giá thuê × tỉ lệ lấp đầy `[GIẢ ĐỊNH]`

Giá thuê theo ngày lấy từ dải THẬT của thị trường Đà Nẵng (38K–50K) và dải đề xuất (80K):

| Giá thuê/ngày | Lấp đầy 20% (6 ngày) | Lấp đầy 40% (12 ngày) | Lấp đầy 60% (18 ngày) |
|---|---|---|---|
| **38.000 VND** (leminhSTORE) | 228.000 | 456.000 | 684.000 |
| **50.000 VND** (DH Lend, Trường Giang) | 300.000 | 600.000 | 900.000 |
| **80.000 VND** (định vị chuyên ngày thi) | 480.000 | 960.000 | 1.440.000 |

### Bảng G.3b — Thời gian hoàn vốn thô/máy (chưa trừ chi phí, máy 6.200.000 VND)

| Giá thuê/ngày | Lấp đầy 20% | Lấp đầy 40% | Lấp đầy 60% |
|---|---|---|---|
| 38.000 VND | 27,2 tháng | 13,6 tháng | 9,1 tháng |
| 50.000 VND | 20,7 tháng | 10,3 tháng | 6,9 tháng |
| 80.000 VND | 12,9 tháng | 6,5 tháng | 4,3 tháng |

> ⚠ **Đây là hoàn vốn THÔ (gross), chưa trừ ship, bảo trì, nhân sự, mặt bằng.** Sau khi trừ, thời gian thực có thể dài hơn **1,5–2,5 lần**. Nhóm phải tự tính lại đầy đủ.

### Đối chiếu với gói thuê THÁNG (số thật)
- DH Lend Đà Nẵng: **1.000.000 VND/tháng** → nếu 1 máy được thuê tháng liên tục, hoàn vốn thô = 6.200.000 ÷ 1.000.000 = **6,2 tháng**.
- Thị trường chung: **600.000 VND/tháng** → hoàn vốn thô = **10,3 tháng**.
- 👉 **Gói thuê tháng cho doanh thu/máy ổn định hơn hẳn gói ngày ở tỉ lệ lấp đầy thấp.** Chiến lược hợp lý: **gói tháng làm nền tảng doanh thu, gói ngày/ca thi làm biên lợi nhuận cao trong mùa thi.**

## G.4. ⚠ Yếu tố MÙA VỤ — rủi ro lớn nhất của mô hình

Nhu cầu "thuê laptop đi thi" **tập trung cực độ vào các đợt thi**. Ngoài mùa thi, tỉ lệ lấp đầy có thể gần 0. Vì vậy:

1. **Tỉ lệ lấp đầy trung bình năm nhiều khả năng THẤP hơn nhiều so với 40–60%** trong bảng G.3.
2. Nhóm **phải** lấy **lịch thi của ĐH FPT Đà Nẵng** (số đợt thi/năm, số ngày/đợt, số môn) để mô hình hoá đúng — đây là dữ liệu **nội bộ trường, nhóm có sẵn**, và là số liệu thuyết phục nhất trong proposal.
3. Cần sản phẩm lấp chỗ trống ngoài mùa thi: thuê tháng cho SV chưa mua máy, thuê cho sự kiện/hội thảo, thuê cho nhóm làm đồ án.

## G.5. Checklist các con số nhóm PHẢI tự bổ sung để P&L hoàn chỉnh

- [ ] Số đợt thi/năm của ĐH FPT ĐN và số ngày mỗi đợt
- [ ] Tổng số SV ĐH FPT ĐN (để ước TAM/SAM/SOM)
- [ ] Tỉ lệ SV dùng MacBook chip M1/M2 (không thi được) — từ khảo sát
- [ ] Tỉ lệ SV từng gặp sự cố máy vào ngày thi — từ khảo sát
- [ ] Mức giá SV sẵn sàng trả (WTP) — từ khảo sát
- [ ] Giá lô sỉ 15–40 máy từ ít nhất 3 shop (2 shop ĐN + 1 shop ngoài)
- [ ] Giá ship thật trên app Ahamove/Grab/Be cho tuyến thật
- [ ] Điện/nước/internet tại kho
- [ ] Tỉ lệ hỏng máy thực tế sau 1–2 tháng chạy thử

---

# PHẦN H — TỔNG HỢP KHOẢNG TRỐNG DỮ LIỆU

| # | Dữ liệu thiếu | Mức độ nghiêm trọng | Cách lấy nhanh nhất |
|---|---|---|---|
| 1 | Tỉ lệ mất giá laptop **%/năm** tại VN | 🔴 Cao — ảnh hưởng trực tiếp giá trị thu hồi và hoàn vốn | Khảo sát giá 20–30 tin cùng model trên Chợ Tốt |
| 2 | **Giá cụ thể** laptop mới dưới 12 triệu (Acer Aspire Lite 14, Lenovo V14 G4, Colorful Rimbook L1) | 🟠 Trung bình | Mở fptshop.com.vn / gearvn.com |
| 3 | Giá **lô sỉ** 15–40 máy | 🔴 Cao — quyết định CAPEX | Gọi T&T Center (0905 677 427), Kim Anh (0777 126 126) |
| 4 | Giá ship **thật** Đà Nẵng (Ahamove/Grab/Be) tuyến ĐH FPT → khu trọ | 🔴 Cao — có thể ăn hết biên lợi nhuận gói ngày | Mở app, chụp màn hình |
| 5 | Hoà Hải/Ngũ Hành Sơn thuộc **Vùng II hay III** lương tối thiểu | 🟠 Trung bình | Danh mục địa bàn cấp xã kèm NĐ 293/2025/NĐ-CP |
| 6 | Giá tên miền **.com** cụ thể | 🟢 Thấp (số nhỏ) | bkns.vn / matbao.net / vietnix.vn |
| 7 | Giá **Vercel / Railway / Viettel IDC** | 🟢 Thấp | Trang pricing chính thức |
| 8 | Giá **thay mainboard** laptop | 🟠 Trung bình — quyết định ngưỡng "sửa hay thanh lý" | Hỏi tiệm sửa laptop Đà Nẵng |
| 9 | Giá SSD 512GB | 🟢 Thấp | dienthoaivui.com.vn |
| 10 | **Deadline** SV-STARTUP / FPT Biz Talent / Startup Wheel 2026–2027 | 🔴 Cao — lỡ deadline là mất cơ hội | Phòng CTSV ĐH FPT ĐN; startupwheel.vn |
| 11 | **Tiền thưởng SV-STARTUP 2026** (chỉ có số 2025) | 🟠 Trung bình | Công văn Bộ GD&ĐT |
| 12 | **DNES** và các quỹ hỗ trợ khởi nghiệp Đà Nẵng | 🔴 Cao — nguồn vốn địa phương | dnes.vn; Sở KH&CN Đà Nẵng |
| 13 | Điện/nước/internet tại kho/trọ Hoà Hải | 🟠 Trung bình | Hỏi chủ trọ |
| 14 | Bản quyền Windows kèm máy cũ nhập khẩu | 🔴 Cao — **liên quan trực tiếp đến khả năng thi EOS/SEB** | Hỏi shop, yêu cầu cam kết bằng văn bản |
| 15 | Chi phí/thủ tục đăng ký hộ kinh doanh & thuế | 🟠 Trung bình | thuvienphapluat.vn |
| 16 | Giá **LaptopWorld, Hoàng Hà, Nam Phương** | 🟢 Thấp (đã có 10+ shop khác) | Tra thêm |

---

# PHẦN I — DANH MỤC NGUỒN ĐẦY ĐỦ (URL thật do WebSearch trả về)

### Laptop cũ — giá & shop
1. https://laptops.vn/san-pham/thinkpad-t480/ — ThinkPad T480 i5-8250U/8GB/256GB từ 6.200.000đ
2. https://laptops.vn/review/laptop-thinkpad-cu-gia-re/ — ThinkPad cũ từ 3 triệu; cũ rẻ hơn mới 30–50%
3. https://laptoptv.vn/laptop-cu-dell-latitude-5410-core-i5-10310u-8gb-256gb-man-hinh-14-inch-fhd — 7.280.000đ
4. https://laptoptv.vn/laptop-cu-dell-latitude-5410-core-i5-10310u-16gb-256gb-man-hinh-14-inch-fhd — 8.380.000đ
5. https://laptop15.vn/dell-latitude-5400/ — Latitude 5400 từ 5 triệu
6. https://laptopcubinhduong.vn/dell-latitude-5400/ — Laptop Cũ Bình Dương
7. https://techcare.vn/hp-elitebook-840-g6/ — EliteBook 840 G6 từ 10 triệu (shop Đà Nẵng)
8. https://ttcenter.com.vn/thinkpad-t14s-gen-2-core-i5-16gb-512gb-99 — 10,2–10,6 triệu
9. https://2tmobile.com/thinkpad-t-cu/ — ThinkPad T cũ 5,31–6,49 triệu (03/06/2026)
10. https://thinkpro.vn/laptop/hp-elitebook-840-g5 — ThinkPro (08/2026)
11. https://hacom.vn/laptop-dell-latitude-5410-i5-10310u-8gb-ram-256gb-ssd-man-14.0-inch-fhd-kem-sac-hang-cu-dep
12. https://anhduongstore.vn/laptop-cu-dell-latitude-5410-core-i5-10310u-ram-8gb-ssd-256gb-14-inch-fhd
13. https://topcomputer.vn/laptop-cu-dell-5410-i5-10310u-8gb-256gb-fhd-14
14. https://hoangsonstore.com/dell-latitude-5400
15. https://laptoptld.com/sp/dell-latitude-5400/
16. https://www.shopcongngheso.vn/dell-latitude-5400-i5-8365u
17. https://laptoptaithinh.vn/dell-latitude-5400-intel-core-i5-8365u
18. https://www.itlap.vn/san-pham/364/Laptop-Dell-Latitude-5400--Core-I5-8365U.html
19. https://vitinhtranphu.com/laptop-dell-latitude-5400-i5-8365u-16gb-ssd-512gb
20. https://hunganh.vn/laptop-doanh-nhan/laptop-cu-dell-latitude-5400-core-i5-8365u.html
21. https://nhatminhlaptop.com/thinkpad-t480-i5-8250u
22. https://nhatminhlaptop.com/thinkpad-t490
23. https://laptopsieuben.com/product/lenovo-thinkpad-t490-core-i5-8265u
24. https://2tmobile.com/thinkpad-t490-i5-8265u-16gb-256gb-99/
25. https://2tmobile.com/thinkpad-cu-99/
26. https://2tmobile.com/thinkpad-t480s-core-i5-8250u-ram-8gb-ssd-256gb-cu-99
27. https://laptoptcc.com/laptop-cu-lenovo-thinkpad-t480-core-i5-8250u-8-gb-ram-ssd-256-gb-14-fhd
28. https://maytinhtram.vn/lenovo-thinkpad-t480s.html
29. https://laptopsgn.com/lenovo-thinkpad-t14-gen-1-cu/
30. https://2tmobile.com/thinkpad-t14/
31. https://newtechshop.vn/thinkpad-t14
32. https://ttcenter.com.vn/hp-elitebook-840-g5-core-i5-8350u-ram-8gb-ssd-256gb
33. https://ttcenter.com.vn/hp-elitebook-840-g6-core-i5-8350u-ram-8gb-ssd-256gb
34. https://cellphones.com.vn/laptop-hp-elitebook-840-g5.html
35. https://no1computer.vn/hp-elitebook-840-g5-san-xuat-nam-nao-n60.html — ⚠ số 22 triệu nghi ngờ lỗi thời
36. https://laptoptld.com/sp/hp-elitebook-840-g5/
37. https://laptopcuongphat.com/laptop-cu-lenovo-thinkpad/
38. https://nextgold.vn/danh-sach-laptop-cu-2025/
39. https://www.thanhlytot.vn/thanh-ly-laptop-lenovo-thinkpad-t490s-cu-gia-re
40. https://www.chotot.com/tags/mua-ban-laptop/thinkpad-t490
41. https://www.chotot.com/tags/mua-ban-laptop/thinkpad-t490s
42. https://www.chotot.com/tags/mua-ban-laptop/hp-elitebook-840-g5
43. https://www.chotot.com/tags/mua-ban-laptop/hp-840-g5
44. https://www.chotot.com/tags/mua-ban-laptop/hp-elitebook-840
45. https://www.chotot.com/mua-ban-laptop-lenovo-thinkpad-sdpb7pm32
46. https://www.otofun.net.vn/threads/laptop-minh-dat-san-kho-laptop-thinkpad-dell-hp-xach-tay-my-truc-tiep-nguyen-ban-bao-hanh-dai.1964832/

### Shop Đà Nẵng
47. https://ttcenter.com.vn/laptop-cu — T&T Center (CN2: 101 Nguyễn Văn Thoại, Ngũ Hành Sơn)
48. https://laptopkimanh.vn/14-inch — Kim Anh (248 Ngũ Hành Sơn)
49. https://ngocvupc.com/ — Ngọc Vũ PC
50. https://laptopre.vn/laptop-cu
51. https://www.chotot.com/mua-ban-laptop-da-nang — 2.399 tin (25/08/2026)
52. https://top10danang.com/diem-danh-15-dia-chi-ban-laptop-cu-da-nang-gia-re-uy-tin/
53. https://www.taidanang.com/laptop-cu-da-nang/
54. https://raovat.vnexpress.net/da-nang/laptop

### Laptop mới dưới 12 triệu 2026
55. https://fptshop.com.vn/tin-tuc/danh-gia/laptop-sinh-vien-duoi-12-trieu-2026-205902
56. https://gearvn.com/blogs/danh-gia-tu-van/top-laptop-cho-sinh-vien-duoi-12-trieu
57. https://memoryzone.com.vn/laptop-gia-re-duoi-12-trieu-dong-cho-sinh-vien
58. https://www.phucanh.vn/top-6-laptop-van-phong-gia-re-ban-nen-tham-khao.html
59. https://hoanghamobile.com/tin-tuc/top-10-laptop-van-phong-gia-re-duoi-15-trieu-dang-mua-2026/
60. https://thailongcomputer.com/laptop-cho-sinh-vien-van-phong.html
61. https://cellphones.com.vn/sforum/top-5-laptop-cho-tan-sinh-vien-gia-re

### Giá thuê laptop (doanh thu tham chiếu)
62. https://mitgroup.vn/cho-thue-laptop/ — từ 29.000đ/ngày; SV từ 20.000đ/ngày
63. https://dhlend.com/cho-thue-may-tinh-laptop-pc-may-in-da-nang.html — **50.000đ/ngày, 1.000.000đ/tháng (Đà Nẵng)**
64. https://truonggiang.vn/cho-thue-laptop.html — từ 50K/ngày (Đà Nẵng)
65. https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html — từ 38.000đ/ngày (Đà Nẵng)
66. https://leminhstore.vn/thue-laptop-thue-macbook-thue-imac-thue-pc-van-phong-thi-cong-du-an-su-kien-tai-da-nang-76867u.html
67. https://skycomputer.vn/dich-vu/cho-thue-may-tinh-laptop-tai-da-nang/
68. https://chothuelaptop.com.vn/thue-laptop-da-nang/
69. https://chothuelaptop.com.vn/thue-laptop-theo-thang/
70. https://chothuelaptop.info/cho-thue-laptop-da-nang-thu-tuc-nhanh-gon/
71. https://danang.plus/thue-laptop/ — Top 7 dịch vụ cho thuê laptop Đà Nẵng
72. https://thuelaptop.com.vn/dia-diem-cho-thue-laptop-tai-da-nang-gia-re.html
73. https://thuelaptop.com.vn/bang-gia-cho-thue-laptop-do-hoa.html
74. https://phuongnamco.com/cho-thue-laptop-theo-thang-tiet-kiem-linh-hoat-cho-ca-nhan-va-doanh-nghiep/
75. https://thietbichothue.com/cho-thue-laptop/
76. https://skylap.vn/dich-vu-cho-thue/cho-thue-laptop/
77. https://wifisukien.com/cho-thue-laptop/
78. https://vietbis.vn/tin-tuc/dich-vu-cho-thue-laptop-tai-ha-noi---vietbisvn-2530.html

### Mặt bằng / phòng trọ Đà Nẵng
79. https://phongtro123.com/tinh-thanh/da-nang/quan-ngu-hanh-son — dải 1,1–6,8 triệu/tháng
80. https://phongtro123.com/tinh-thanh/da-nang/quan-ngu-hanh-son/phuong-hoa-hai
81. https://troplus.vn/phong-tro/cho-thue-phong-tro-full-noi-that-gan-fpt-city-hoa-hai-ngu-hanh-son-da-nang-gia-chi-32-trieuthang — 3,2 triệu/tháng
82. https://www.nhatot.com/thue-phong-tro-gan-truong-dai-hoc-fpt-da-nang-quan-ngu-hanh-son-sdse344300
83. https://www.nhatot.com/thue-phong-tro-phuong-hoa-hai-quan-ngu-hanh-son-da-nang
84. https://www.nhatot.com/thue-phong-tro-quan-ngu-hanh-son-da-nang
85. https://homedy.com/cho-thue-nha-tro-phong-tro-quan-ngu-hanh-son-da-nang/gia-re-phuong-hoa-hai-es1569907
86. https://chothuephongtro.me/da-nang/quan-ngu-hanh-son.html
87. https://phongtro123.com/cho-thue-mat-bang-quan-ngu-hanh-son-da-nang
88. https://mogi.vn/da-nang/quan-ngu-hanh-son/thue-mat-bang-cua-hang-shop
89. https://alonhadat.com.vn/nha-dat/cho-thue/mat-bang/da-nang/587/quan-ngu-hanh-son.html
90. https://muaban.net/bat-dong-san/cho-thue-mat-bang-kinh-doanh-quan-ngu-hanh-son-da-nang
91. https://batdongsan.com.vn/cho-thue-sang-nhuong-cua-hang-ki-ot-da-nang
92. https://nhadat.cafeland.vn/cho-thue/mat-bang-tai-da-nang/
93. https://alonhadat.com.vn/nha-dat/cho-thue/mat-bang/3/da-nang.html

### Lương & nhân sự
94. https://luatvietnam.vn/lao-dong-tien-luong/muc-luong-toi-thieu-vung-tai-thanh-pho-da-nang-nam-2026-562-105277-article.html
95. https://thuvienphapluat.vn/phap-luat-doanh-nghiep/bai-viet/muc-luong-toi-thieu-vung-thanh-pho-da-nang-tu-01-01-2026-15957.html
96. https://nhansu.vn/phap-luat-lao-dong/muc-luong-toi-thieu-vung-2026-da-nang-la-bao-nhieu-41233.html
97. https://thuvienphapluat.vn/phap-luat-doanh-nghiep/bai-viet/muc-luong-toi-thieu-vung-2026-muc-luong-co-so-2026-va-mot-so-luu-y-quan-trong-18204.html
98. https://xaydungchinhsach.chinhphu.vn/de-xuat-muc-luong-toi-thieu-vung-tu-1-1-2026-119250718084713755.htm
99. https://baoangiang.com.vn/muc-luong-toi-thieu-vung-2026-tang-bao-nhieu-phan-tram-a472794.html
100. https://thuvienphapluat.vn/lao-dong-tien-luong/muc-luong-toi-thieu-vung-hien-nay-tai-thanh-pho-da-nang-la-bao-nhieu-53981.html
101. https://vn.joboko.com/blog/luong-part-time-nwi5750 — mức lương part-time Đà Nẵng
102. https://thuvienphapluat.vn/phap-luat/nam-2026-sinh-vien-di-lam-them-lam-parttime-o-tphcm-ha-noi-duoc-tra-luong-theo-gio-toi-thieu-la-bao-263082.html
103. https://vn.indeed.com/career/nhân-viên-part-time/salaries
104. https://careerviet.vn/viec-lam/parttime-tai-da-nang-kl511-vi.html
105. https://careerviet.vn/viec-lam/part-time-ke1-vi.html

### Giao hàng
106. https://ahamove.com/service/aha-delivery/price
107. https://ahamove.com/giao-hang-tieu-chuan-la-gi — 10.000–20.000đ/km nội tỉnh
108. https://ahamove.com/tinh-tien-ship-theo-km
109. https://ahamove.com/giao-hang-nhanh-trong-1-ngay
110. https://topkinhdoanh.net/bang-gia-ahamove/ — bảng giá Siêu tốc/Siêu rẻ
111. https://topkinhdoanh.com/bang-gia-ahamove/
112. https://hellodanang.vn/danh-gia/ahamove-dich-vu-ship-hang-hoa-toc-tai-da-nang

### Hosting / tên miền
113. https://vietnix.vn/vps/ — VPS từ 157.000đ/tháng
114. https://azdigi.com/blog/kien-thuc-hosting/top-5-hosting-gia-re-tot-nhat-viet-nam-2026
115. https://azdigi.com/blog/kien-thuc-vps/bang-gia-thue-vps-viet-nam
116. https://azdigi.com/blog/kien-thuc-vps/top-nha-cung-cap-vps-viet-nam
117. https://azdigi.com/blog/kien-thuc-hosting/bang-gia-hosting-viet-nam-2026
118. https://azdigi.com/blog/kien-thuc-hosting/bang-gia-hosting-viet-nam-so-sanh
119. https://azdigi.com/blog/kien-thuc-hosting/top-10-nha-cung-cap-hosting-tot-nhat-viet-nam-2026
120. https://azdigi.com/blog/kien-thuc-hosting/so-sanh-5-nha-cung-cap-hosting-viet-nam-2026
121. https://helpdesk.inet.vn/knowledgebase/bang-gia-ten-mien-va-cac-loai-phi — .vn năm đầu 770.000đ, năm sau 460.000đ
122. https://vinahost.vn/phi-duy-tri-ten-mien/
123. https://vinahost.vn/bang-gia-ten-mien/
124. https://www.bkns.vn/ten-mien/bang-gia-ten-mien.html
125. https://vietnix.vn/bang-gia-ten-mien/
126. https://www.matbao.net/ten-mien/bang-gia-ten-mien.html

### Sửa chữa
127. https://dienthoaivui.com.vn/sua-chua-laptop/thay-man-hinh-laptop
128. https://benhvienlaptop.com/man-hinh-laptop-hp/
129. https://laptop911.vn/man-hinh-hp-14-inch-gia-bao-nhieu
130. https://bcavn.com/tin-tuc/thay-man-hinh-laptop-bao-nhieu-tien-30474.html
131. https://bcavn.com/tin-tuc/thay-man-hinh-laptop-hp-bao-nhieu-tien-30475.html
132. https://linhkienlaptopthaiha.com/thay-man-hinh-laptop-dell-14-inch-full-hd-1-2-257013.html
133. https://fastcare.vn/thay-ban-phim-laptop — từ 350.000đ, lấy sau 1 giờ
134. https://fastcare.vn/blog/gia-thay-ban-phim-laptop.html
135. https://khoavang.vn/blog/sua-ban-phim-laptop-het-bao-nhieu-tien-p3099.html
136. https://phongvu.vn/cong-nghe/thay-ban-phim-laptop-bao-nhieu-tien/
137. https://thanhtrangmobile.com/thay-ban-phim-laptop/
138. https://tanphatad.com/sua-va-thay-ban-phim-laptop-gia-bao-nhieu-tien/
139. https://lacviet.vn/en/thay-pin-laptop-dell/ — Latitude 1,2–2,5 triệu
140. https://dienthoaivui.com.vn/sua-chua-laptop/thay-pin-laptop/thay-pin-laptop-dell — từ 850K
141. https://dienthoaivui.com.vn/sua-chua-laptop/thay-pin-laptop/
142. https://benhvienlaptop.com/pin-laptop/
143. https://benhvienlaptop.com/pin-laptop-dell/
144. https://doctorlaptop.com.vn/pin-laptop-dell-13429.html
145. https://linhkienlaptopthaiha.com/pin-laptop-dell-2-1-305193.html
146. https://linhkienlaptopthaiha.com/pin-laptop-dell-latitude-2-1-533473.html
147. https://tritienlaptop.com/thay-pin-laptop-het-bao-nhieu-tien/
148. https://www.hoangvucenter.vn/vi-vn/bang-gia-thay-pin-laptop.html
149. https://dienthoaivui.com.vn/linh-kien-laptop/o-cung — SSD 256GB từ 550.000đ
150. https://lacviet.vn/en/mua-o-cung-ssd-cho-laptop-dell/

### Khấu hao / kế toán
151. https://docs.kreston.vn/vbpl/chi-phi-tai-chinh/tai-san-co-dinh/thong-tu-45-2013-tt-btc/
152. https://vcci.com.vn/legal-document/thong-tu-452013tt-btc-cua-bo-tai-chinh-ve-viec-huong-dan-che-do-quan-ly-su-dung-va-trich-khau-hao-tai-san-co-dinh
153. https://ketoanthienung.org/tin-tuc/khung-thoi-gian-trich-khau-hao-cac-loai-tai-san-co-dinh.htm
154. https://ketoanthienung.net/khung-thoi-gian-trich-khau-hao-cac-loai-tai-san-co-dinh.htm
155. https://acccantho.vn/khau-hao-tai-san-co-dinh-theo-thong-tu-45/
156. https://accnet.vn/cach-tinh-khau-hao-tai-san-co-dinh-cu-the-chi-tiet-chinh-xac
157. https://khanhhungpc.vn/khau-hao-may-tinh-van-phong/
158. https://kiemtoancalico.com/ghi-nhan-tscd-va-trich-khau-hao-doi-voi-laptop-moi-mua-cua-cong-ty.html
159. https://danketoan.com/threads/co-bat-buoc-khau-hao-may-laptop-khong.158659/
160. https://macvn.com.vn/dinh-gia-laptop-cu/ — cách định giá laptop cũ
161. https://tinhte.vn/thread/laptop-cu-ban-duoc-bao-nhieu-la-hop-ly.4115236/

### Nguồn vốn / cuộc thi
162. https://daihoc.fpt.edu.vn/tin-noi-bat-muc-tin-tuc/fpt-biz-talent-2025-truong-dh-fpt-kien-tao-the-he-doanh-nhan-tre/ — **tổng giải thưởng 260 triệu**
163. https://www.vista.gov.vn/vi/news/khoi-nghiep-doi-moi-sang-tao/khoi-dong-cuoc-thi-khoi-nghiep-quy-mo-toan-quoc-fpt-biz-talent-2025-uom-mam-tai-nang-doanh-nhan-doi-moi-sang-tao-tuong-lai-11452.html
164. https://mst.gov.vn/fpt-biz-talent-2025-tim-kiem-va-uom-mam-the-he-doanh-nhan-doi-moi-sang-tao-viet-nam-197250616201306032.htm
165. https://vnexpress.net/sinh-vien-fptu-neu-thang-giai-khoi-nghiep-nho-ung-dung-ai-vao-giao-duc-4939846.html
166. https://chungta.vn/cong-nghe/du-an-giao-duc-ung-dung-tri-tue-nhan-tao-dang-quang-tai-fpt-biz-talent-2025-1140285.html
167. https://feexp.space/fpt-biz-talent-2025
168. https://daihoc.fpt.edu.vn/tin-noi-bat-muc-tin-tuc/tu-lop-hoc-den-thuong-truong-3-du-an-cua-sinh-vien-fptu-tien-thang-chung-ket-fpt-biz-talent-2025/
169. https://fschool.fpt.edu.vn/vong-ban-ket-fpt-biz-talent-2025/
170. https://startupwheel.vn/vi/giai-thuong/ — **giải Nhất 400 triệu (hiện kim 150 triệu)**
171. https://startupwheel.vn/vi/top-100-startup-wheel-2026/
172. https://vneconomy.vn/chilica-va-kinava-gianh-vi-tri-quan-quan-startup-wheel-2025.htm
173. https://www.chinhsachphapluat.vn/startup-wheel-2025-hanh-trinh-13-nam-nang-tam-khoi-nghiep-viet-nam-ra-the-gioi/
174. https://tuoitre.vn/15-du-an-khoi-nghiep-cua-hoc-sinh-sinh-vien-gianh-giai-nhat-sv-startup-2026-20260419203319353.htm — cơ cấu giải SV-STARTUP 2026
175. https://vjst.vn/sv-startup-2026-chuyen-bien-ro-net-tu-y-tuong-sang-san-pham-tu-phong-trao-sang-hieu-qua-thuc-chat-86335.html
176. https://doanhnhan.congly.vn/sv-startup-2026-lam-that-thi-that-hieu-qua-thuc-chat.html
177. https://diendandoanhnghiep.vn/sv_startup-2026-y-tuong-khoi-nghiep-hom-nay-la-su-truong-thanh-doanh-nghiep-tuong-lai-10177463.html
178. https://www.vista.gov.vn/vi/news/cac-linh-vuc-khoa-hoc-va-cong-nghe/khoi-nguon-sang-tao-tre-tai-sv-startup-2025-11260.html — giải thưởng SV Startup 2025
179. https://usth.edu.vn/khoi-dong-cuoc-thi-hoc-sinh-sinh-vien-voi-y-tuong-khoi-nghiep-lan-thu-viii-nam-2026-29630/
180. https://fbe.ftu.edu.vn/cuoc-thi-hoc-sinh-sinh-vien-voi-y-tuong-khoi-nghiep-lan-thu-viii-sv-startup-2026-2/
181. https://fbe.ftu.edu.vn/chinh-thuc-khoi-dong-cuoc-thi-hoc-sinh-sinh-vien-voi-y-tuong-khoi-nghiep-lan-thu-viii-sv-startup-2026-cap-co-so-truong-dai-hoc-ngoai-thuong/
182. https://www.hutech.edu.vn/homepage/hoat-dong-sinh-vien/14632755-sinh-vien-hutech-gianh-giai-nhi-sv-startup-2026-voi-du-an-duoc-lieu-giau-tiem-nang
183. https://tlu.edu.vn/truong-dai-hoc-thuy-loi-khang-dinh-dau-an-tai-sv_startup-2026-noi-dai-chuoi-thanh-tich-6-nam-lien-tiep-54494
184. https://thieunien.vn/hai-truo-ng-thcs-ha-no-i-gia-nh-gia-i-nha-t-sv-startup-2026-tbd67231.html
185. https://daidoanket.vn/khoi-dong-giai-thuong-tuoi-tre-startup-award-2026.html
186. https://www.techsignin.com/010426-startup-viet-giai-bai-toan-toan-cau-qvic/

---

*Hết tài liệu. Ghi chú cuối: ngân sách WebSearch của phiên đã hết (200/200 lượt) trước khi tra xong Vercel/Railway/Viettel IDC, Grab/Be Đà Nẵng, giá thay mainboard, và DNES. Bốn nhóm dữ liệu này còn thiếu — xem Phần H.*
