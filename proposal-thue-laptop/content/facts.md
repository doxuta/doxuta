# HỒ SƠ DỮ KIỆN CHUẨN — ExamLap
> Mọi người viết phần đều PHẢI dùng đúng các con số, tên gọi và cách diễn đạt trong file này.
> Không được tự chế số mới. Nếu cần một con số chưa có ở đây, hãy ghi rõ là ước lượng và nêu giả định.

## 0. QUY ƯỚC ĐỘ TIN CẬY (bắt buộc dùng)
Toàn bộ nghiên cứu được thực hiện trong môi trường **chỉ truy cập được công cụ tìm kiếm web**, không mở
được trực tiếp từng trang (mọi yêu cầu tải trang đều bị chặn ở tầng mạng). Vì vậy:
- **[Đã xác minh]** — thông tin xuất hiện nhất quán trong nhiều kết quả tìm kiếm, kèm URL thật.
- **[Cần kiểm chứng]** — lấy từ đoạn trích kết quả tìm kiếm, chưa mở được trang gốc để đối chiếu.
- **[Ước lượng của nhóm]** — nhóm tự suy ra, kèm giả định. Không được trình bày như dữ liệu thật.
Khi viết, đặt nhãn này ngay sau con số hoặc trong ghi chú bảng. Đây là điểm mạnh của bản proposal chứ
không phải điểm yếu: giám khảo đánh giá cao việc phân biệt rõ dữ liệu và giả định.

## 1. THƯƠNG HIỆU & ĐỊNH VỊ
- Tên dự án: **ExamLap**. Đọc là "ếch-xam-láp". Không viết EXAMLAP hay Examlap.
- Một câu định vị: *"Không sinh viên nào phải bỏ một buổi thi vì cái máy tính."*
- Sản phẩm bán ra không phải "cái laptop" mà là **"máy sẵn sàng thi" (exam-ready machine)**:
  máy Windows đã cài sẵn EOS Client + Safe Exam Browser, đã chạy thử, kèm tai nghe có dây 3.5mm,
  sạc đầy, dữ liệu người dùng trước đã xoá sạch.
- Địa bàn giai đoạn đầu: **Đại học FPT Đà Nẵng, phường Hoà Hải, quận Ngũ Hành Sơn** (Khu đô thị FPT City).
- Ba cam kết công khai: **giao trước giờ thi 30 phút** · **đổi máy trong 15 phút nếu máy lỗi giữa ca thi**
  · **hoàn cọc tự động trong 5 phút sau khi trả máy nguyên vẹn**.

## 2. DỮ KIỆN NỀN — VÌ SAO CÓ VẤN ĐỀ (dùng cho Phần I)
| # | Dữ kiện | Nhãn |
|---|---|---|
| F1 | Sinh viên ĐH FPT thi cuối kỳ trên **phần mềm EOS (Exam Online System)** chạy trên **máy tính cá nhân của chính sinh viên**; trường không cấp máy cho kỳ thi | [Đã xác minh] |
| F2 | EOS **bắt buộc hệ điều hành Windows**; máy Mac phải cài Windows qua Bootcamp | [Đã xác minh] |
| F3 | **MacBook chip M1/M2/M3 không cài được Bootcamp → không thi được EOS** | [Đã xác minh] |
| F4 | Kỳ thi dùng kèm **Safe Exam Browser (SEB)**, tải từ `exam.fpt.edu.vn`, phải cài đúng phiên bản | [Đã xác minh] |
| F5 | File `EOSClient.exe` **chỉ chạy khi nằm đúng thư mục giải nén ban đầu**; copy ra ngoài là không khởi động được | [Cần kiểm chứng] |
| F6 | Bài làm được lưu thành file trên **ổ cứng máy sinh viên** rồi mới nộp lên máy chủ → máy hỏng giữa chừng là rủi ro mất bài | [Cần kiểm chứng] |
| F7 | Phần thi nghe cần **tai nghe có dây**; nhiều laptop đời mới đã bỏ jack 3.5mm | [Đã xác minh] |
| F8 | Học phí giai đoạn chuyên ngành, campus Đà Nẵng: **22.120.000đ/học kỳ** (2025–2026 và 2026–2027) | [Đã xác minh] |
| F9 | Một học kỳ 4 tháng, khoảng 5 môn thi → **giá trị kinh tế một môn thi ≈ 4.424.000đ** | [Ước lượng của nhóm] |
| F10 | Một năm học có **3 học kỳ**: Fall (9→12), Spring (1→5), Summer (5→9) → **3 đỉnh thi cuối kỳ + 3 đợt progress test** mỗi năm | [Đã xác minh] |
| F11 | Sinh viên ĐH FPT Đà Nẵng: **khoảng 4.500 – 6.000 người** (ba cách ước lượng độc lập cho kết quả nhất quán) | [Ước lượng của nhóm] |
| F12 | ĐH FPT toàn hệ thống khoảng **30.000 sinh viên** (2024); chỉ tiêu tuyển sinh 2025 là **13.677** | [Cần kiểm chứng] |
| F13 | Tổng sinh viên đại học và cao đẳng tại Đà Nẵng: **khoảng 90.000 – 120.000** | [Ước lượng của nhóm] |

**Tỉ số quyết định dùng để bán hàng:** thuê máy một ca thi tốn **79.000–179.000đ**; trượt một môn vì hỏng máy
mất khoảng **4.424.000đ** học phí cộng một học kỳ chậm tiến độ → **tỉ lệ chi phí trên rủi ro khoảng 1 : 25 đến 1 : 56**.

## 3. ĐỐI THỦ (dùng cho Phần I)
| Đơn vị | Giá công bố | Ghi chú |
|---|---|---|
| MIT Group | từ 29.000đ/ngày (ưu đãi sinh viên từ 20.000đ/ngày) | mức thấp nhất tìm được |
| leminhSTORE (Đà Nẵng) | từ 38.000đ/ngày | có gói "thuê laptop sinh viên Đà Nẵng" |
| DH Lend (Đà Nẵng) | 50.000đ/ngày · 1.000.000đ/tháng | giao nhận tận nơi, **cam kết đổi máy nếu hỏng** |
| Trường Giang Computer (Đà Nẵng) | từ 50.000đ/ngày | |
| Đình Hậu, Sky Computer (Đà Nẵng) | không công bố giá | |
Thị trường Đà Nẵng đã có **ít nhất 7 đơn vị** cho thuê laptop. **Không đơn vị nào** định vị chuyên cho
sinh viên đi thi EOS/SEB, và không đơn vị nào đặt tại khu Hoà Hải (đều cách 8–15 km).

## 4. ĐỘI MÁY VÀ GIÁ (khớp tuyệt đối với mô hình tài chính)
Đội máy năm 1: **10 máy**. Năm 2: **16 máy**.
| Nhóm | Số máy | Máy đại diện | Đơn giá mua | Giá thuê một ca thi 4 giờ |
|---|---|---|---|---|
| A — Máy thi tiêu chuẩn | 5 | Dell Latitude 5400 · ThinkPad T480, i5 gen 8, 8GB, SSD 256GB, có jack 3.5mm | 6.500.000đ | **79.000đ** |
| B — Máy lập trình | 4 | Dell Latitude 5410 · ThinkPad T480 16GB, i5 gen 10, 16GB | 7.500.000đ | **99.000đ** |
| C — Máy cấu hình cao | 1 | ThinkPad T490 · T14s Gen 2, 16GB, SSD 512GB | 10.000.000đ | **129.000đ** |

Bảng giá theo gói (giá của nhóm A; nhóm B cộng 20.000đ, nhóm C cộng 50.000đ):
- Ca thi 4 giờ: **79.000đ** · Ngày thi 2 ca: **129.000đ** · Ca thi khẩn cấp (đặt dưới 3 giờ, giao tận cổng): **179.000đ**
- Tuần thi 7 ngày: **449.000đ** · Tháng (đồ án, thực tập): **849.000đ**
- Phí miễn trừ thiệt hại tự chọn: **15.000đ/lượt** hoặc **69.000đ/tháng**
- Tiền cọc: **300.000đ** chuẩn · **150.000đ** hạng B (từ lượt thứ 3) · **0đ** hạng A (từ lượt thứ 6, không vi phạm)
- Phí trả trễ: **20.000đ mỗi 30 phút**, tối đa 200.000đ/ngày
- Doanh thu bình quân mỗi lượt thuê (đã trộn các gói): **144.100đ**

## 5. SỐ TÀI CHÍNH CHỐT (không được viết khác)
- Tổng vốn đầu tư ban đầu: **93.250.000đ** (trong đó 72.500.000đ là 10 máy)
- Định phí hằng tháng: **2.800.000đ** · Khấu hao hằng tháng: **1.571.000đ**
- Năm 1: **382 lượt thuê ca/ngày/tuần** + **30 máy-tháng**; doanh thu **81.758.200đ**; EBITDA **33.294.672đ**;
  lợi nhuận sau thuế **14.442.672đ** (biên **17,7%**); tỉ lệ khai thác bình quân **42%**
- Năm 2 (16 máy, nhu cầu ×1,6): doanh thu **159.718.200đ**; LNST **56.115.472đ**; đầu tư thêm **45.180.000đ**
- Hoà vốn: **25 lượt/tháng** (tiền mặt) · **39 lượt/tháng** (kế toán)
- Điểm hoàn vốn toàn bộ vốn đầu tư: **tháng thứ 27**
- Ba kịch bản: Thận trọng LNST **−14.565.301đ**; Cơ sở **+14.442.672đ**; Thuận lợi **+43.737.949đ**
- Toàn bộ bảng số nằm sẵn ở `content/fin_tables.md`, dán nguyên vào bài bằng chỉ dấu:
  `{{T-CAPEX}}`, `{{T-OPEX}}`, `{{T-GIA}}`, `{{T-PNL}}`, `{{T-HOAVON}}`, `{{T-KICHBAN}}`, `{{T-NAM2}}`

## 6. NGUYÊN TẮC AN TOÀN TÀI SẢN (dùng cho Phần II)
Khẩu quyết: **cọc thấp + danh tính mạnh**, ngược với cách làm phổ biến là *cọc cao + danh tính yếu*.
Năm lớp phòng thủ, theo đúng thứ tự này:
1. **Sàng lọc đầu vào** — eKYC đối chiếu CCCD với khuôn mặt sống, bắt buộc email `@fpt.edu.vn` và mã số sinh viên, danh sách chặn nội bộ.
2. **Ràng buộc kinh tế** — cọc 300.000đ, phí miễn trừ thiệt hại, và quan trọng hơn: mất quyền dùng dịch vụ cả kỳ thi, mất điểm tín nhiệm.
3. **Bằng chứng** — hợp đồng điện tử có chữ ký, biên bản bàn giao kèm 6 ảnh có mã băm SHA-256, nhật ký hệ thống chỉ ghi thêm.
4. **Kiểm soát kỹ thuật** — MDM check-in mỗi 15 phút, khoá màn hình từ xa (cần hai người duyệt), BitLocker, mật khẩu BIOS, chặn khởi động USB, khắc laser mã tài sản, tem niêm phong vỡ.
5. **Pháp lý** — nhắc nợ bằng văn bản, rồi trình báo theo **Điều 175 Bộ luật Hình sự 2015** (lạm dụng tín nhiệm chiếm đoạt tài sản).

**KHÔNG giữ CCCD, thẻ sinh viên hay bất kỳ giấy tờ tuỳ thân nào của khách.** Đây vừa là điểm khác biệt
thương mại vừa là yêu cầu pháp lý — phải nêu rõ căn cứ trong phần pháp lý.

## 7. VAI TRÒ TRONG HỆ THỐNG
- **Khách thuê** (sinh viên): đặt máy, xác minh eKYC một lần, thanh toán, nhận và trả máy, khiếu nại.
- **Nhân viên giao nhận** (cộng tác viên sinh viên, trả theo giờ): chuẩn bị máy, bàn giao, thu hồi, lập biên bản.
- **Quản trị viên** (thành viên nhóm sáng lập): duyệt hồ sơ eKYC khó, cấu hình giá, xử lý sự cố, khoá máy từ xa, xem báo cáo.
- **Đối tác cung ứng và sửa chữa**: cửa hàng laptop cũ tại Đà Nẵng cấp nguồn máy và bảo hành; tiệm sửa cam kết 24 giờ.
Nguyên tắc phân quyền: **không một người nào tự mình khoá được máy của khách** — lệnh khoá cần hai người duyệt và luôn ghi nhật ký.

## 8. KHO HÌNH ẢNH ĐÃ CÓ SẴN (dùng đúng đường dẫn này)
### Sơ đồ — đặt trên TRANG NGANG (đánh dấu `<<<landscape>>>` trước và `<<<portrait>>>` sau)
- `assets/diagrams/04-kien-truc.png` — kiến trúc hệ thống
- `assets/diagrams/05-seq-dat-thue.png` — trình tự đặt thuê và thanh toán
- `assets/diagrams/06-seq-ekyc.png` — trình tự xác minh eKYC
- `assets/diagrams/07a-seq-ban-giao.png` — trình tự chuẩn bị và bàn giao máy
- `assets/diagrams/07b-seq-tra-may.png` — trình tự trả máy và hoàn cọc
- `assets/diagrams/08-seq-qua-han.png` — trình tự xử lý quá hạn
- `assets/diagrams/09a-erd-dat-thue.png` — lược đồ dữ liệu: đặt thuê
- `assets/diagrams/09c-erd-tien-kiem-toan.png` — lược đồ dữ liệu: tiền và kiểm toán
- `assets/diagrams/10-ranh-gioi-tin-cay.png` — ranh giới tin cậy và dữ liệu nhạy cảm
### Sơ đồ — đặt trên TRANG DỌC bình thường
- `assets/diagrams/02-trang-thai-don.png` — máy trạng thái đơn thuê
- `assets/diagrams/03-vong-doi-thiet-bi.png` — vòng đời thiết bị
- `assets/diagrams/09b-erd-tai-san.png` — lược đồ dữ liệu: tài sản và vận hành
### Biểu đồ tài chính — trang dọc
- `assets/diagrams/c1-doanh-thu-thang.png` · `c2-dong-tien.png` · `c3-cong-suat.png` · `c4-co-cau-chi-phi.png`
### Ảnh giao diện nguyên mẫu — trang dọc, rộng 16 cm
- `assets/screenshots/01-landing.png` `02-catalog.png` `03-ekyc.png` `04-payment.png` `05-pass.png`
  `06-staff.png` `07-dashboard.png` `08-inventory.png` `09-order.png` `10-report.png`
> Các ảnh giao diện là **bản dựng nguyên mẫu do nhóm thiết kế**, không phải ảnh chụp một hệ thống đang chạy.
> Phải nói rõ điều đó ở chú thích hình đầu tiên của chương giao diện.
