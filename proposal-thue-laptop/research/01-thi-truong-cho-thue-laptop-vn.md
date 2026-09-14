# NGHIÊN CỨU THỊ TRƯỜNG CHO THUÊ LAPTOP TẠI VIỆT NAM & ĐÀ NẴNG

**Phục vụ:** Bản proposal khởi nghiệp — Website cho thuê laptop đi thi, khu vực Đại học FPT Đà Nẵng (P. Hoà Hải, Q. Ngũ Hành Sơn, TP. Đà Nẵng)
**Ngày thực hiện:** 14/09/2026
**Phạm vi:** Nhà cung cấp, bảng giá, điều kiện thuê, chính sách bồi thường, giao nhận, quy mô thị trường, khoảng trống thị trường

---

## 0. GHI CHÚ PHƯƠNG PHÁP VÀ GIỚI HẠN — ĐỌC TRƯỚC KHI DÙNG SỐ LIỆU

> **QUAN TRỌNG — người viết proposal phải đọc mục này.**

Trong phiên nghiên cứu này, **công cụ tải trực tiếp nội dung trang web (WebFetch/curl) bị chặn hoàn toàn bởi proxy mạng của môi trường** (mọi domain đều trả về lỗi `EGRESS_BLOCKED`, và `curl` trả về `CONNECT tunnel failed, response 403`). Điều này đã được kiểm chứng trên nhiều domain khác nhau, kể cả các domain phổ thông như `vnexpress.net` và `en.wikipedia.org`.

**Hệ quả:**

- Toàn bộ số liệu dưới đây được thu thập qua **công cụ tìm kiếm web (WebSearch)**, tức là từ **tiêu đề trang, đoạn trích (snippet) và phần tóm tắt nội dung trang do máy tìm kiếm trả về** — **KHÔNG phải từ việc mở và đọc trực tiếp từng trang**.
- **URL trong tài liệu này là URL thật**, do máy tìm kiếm trả về, không bịa. Nhưng **nội dung số liệu gắn với URL đó chưa được xác minh bằng cách mở trang**.
- Giá dịch vụ cho thuê laptop ở Việt Nam **thay đổi rất nhanh** và hầu hết các trang đều tự ghi chú "giá chỉ mang tính tham khảo, liên hệ để có báo giá chính xác".

**KHUYẾN NGHỊ BẮT BUỘC trước khi đưa số vào proposal nộp bài:**

1. **Mở lại từng URL** trong mục [12. Danh sách nguồn](#12-danh-sách-nguồn) và chụp màn hình bảng giá làm phụ lục.
2. **Gọi trực tiếp hotline** của ít nhất 3–5 đơn vị tại Đà Nẵng (số điện thoại có trong Bảng 1) để hỏi giá thuê 1 ngày + mức cọc thực tế. Đây vừa là xác minh, vừa là **dữ liệu sơ cấp (primary research)** — thường được chấm điểm cao hơn dữ liệu thứ cấp trong bài tập Khởi nghiệp.
3. Ghi rõ trong proposal: "Số liệu khảo sát ngày __/__/2026, giá có thể thay đổi."

Các mục **không tìm được dữ liệu** được liệt kê đầy đủ tại [mục 11. Những điều CHƯA xác minh được](#11-những-điều-chưa-xác-minh-được).

---

## 1. BỐI CẢNH: VÌ SAO CÓ NHU CẦU "THUÊ LAPTOP ĐI THI" TẠI ĐẠI HỌC FPT

Đây là phần **quan trọng nhất** của nghiên cứu, vì nó chứng minh vấn đề (problem) mà startup định giải quyết là có thật và có tính đặc thù — chứ không phải nhu cầu chung chung.

### 1.1. Sinh viên FPT thi trên máy tính cá nhân, bằng phần mềm EOS + SEB

Theo hướng dẫn chính thức của Trường Đại học FPT:

| Yêu cầu | Nội dung | Nguồn |
|---|---|---|
| Hệ điều hành | Máy tính **bắt buộc cài hệ điều hành Windows** để thi trên phần mềm EOS | [Hướng dẫn sinh viên sử dụng và thi trên phần mềm EOS tại Trường Đại học FPT](https://daihoc.fpt.edu.vn/tin-noi-bat-muc-tin-tuc/huong-dan-sinh-vien-su-dung-va-thi-tren-phan-mem-eos-tai-truong-dai-hoc-fpt/) |
| Máy Mac | **Bắt buộc cài Windows qua Bootcamp** | [Cài đặt Windows trên MAC bằng Bootcamp – Helpdesk FPT University](https://it.fpt.edu.vn/cantho/huong-dan-cai-windows-tren-mac-dung-bootcamp/) |
| Mac chip M1/M2 | **KHÔNG được hỗ trợ** — không cài được Windows qua Bootcamp | [Hướng dẫn sinh viên sử dụng và thi trên phần mềm EOS](https://hanoi.fpt.edu.vn/tin-tuc-su-kien/huong-dan-sinh-vien-su-dung-va-thi-tren-phan-mem-eos.html) |
| Phần mềm giám sát | **SEB (Safe Exam Browser)**, tải tại `https://exam.fpt.edu.vn/` → mục "HỆ ĐIỀU HÀNH WINDOWS" → file `SEB_3.10.0.794_AutoSettings.msi` | [Hướng dẫn cài đặt phần mềm thi EOS và SEB – Helpdesk FPT University](https://it.fpt.edu.vn/cantho/huong-dan-cai-dat-phan-mem-thi-eos-seb/) |
| Thiết bị kèm | **Tai nghe có dây** cho phần thi nghe (listening) | [Hướng dẫn sinh viên sử dụng và thi trên phần mềm EOS](https://daihoc.fpt.edu.vn/tin-noi-bat-muc-tin-tuc/huong-dan-sinh-vien-su-dung-va-thi-tren-phan-mem-eos-tai-truong-dai-hoc-fpt/) |
| Giấy tờ | Mang **CCCD/giấy tờ tuỳ thân có giá trị pháp lý** để xác minh thông tin | nt |
| Chuẩn bị trước | Sinh viên **nên tải và chạy thử EOS trước ngày thi** để kiểm tra máy có thi được không | nt |

**Các "bẫy kỹ thuật" đã được nhà trường cảnh báo** — rất hữu ích để thiết kế quy trình bàn giao máy thuê:

- File `EOSClient.exe` **chỉ chạy được khi nằm trong thư mục ban đầu**; copy/kéo file ra ngoài thì phần mềm thi **không khởi động được**. ([Hướng dẫn cài đặt phần mềm thi EOS và SEB](https://it.fpt.edu.vn/cantho/huong-dan-cai-dat-phan-mem-thi-eos-seb/))
- Để mở Safe Exam Browser phải tìm từ khoá **"Safe"**, không phải "SEB". (nt)
- Sau lần khởi chạy đầu tiên, khi tắt phần mềm **không thao tác gì thêm và chờ 1–2 phút để máy khởi động lại**. (nt)
- Hướng dẫn cài SEB trên Windows: [FPT University Quy Nhon – Hướng dẫn cài đặt Safe Exam Browser trên HĐH Windows](https://lmsqn.fpt.edu.vn/hd/huong-dan-cai-dat-seb-tren-windows/)
- Hướng dẫn cài SEB cho Edunext / LMS: [IT HCM FPT – Hướng dẫn cài đặt SEB cho Edunext trên Windows](https://it-hcm.fpt.edu.vn/articles.php?news=huong-dan-cai-dat-seb-cho-edunext-tren-windows-&id=22), [Hướng dẫn cài đặt SEB cho LMS trên Windows](https://it-hcm.fpt.edu.vn/articles.php?news=huong-dan-cai-dat-seb-cho-lms-tren-windows&id=36)

### 1.2. Ý nghĩa chiến lược cho startup

Đây là **rào cản kỹ thuật mà không một đơn vị cho thuê laptop thương mại nào hiện nay đang xử lý**. Một chiếc laptop thuê "chung chung" giao cho sinh viên FPT vào ngày thi **có thể vẫn thi không được**, vì:

1. Máy phải là **Windows thật** (không phải macOS, không phải Mac M1/M2).
2. Phải **cài sẵn SEB đúng phiên bản** lấy từ `exam.fpt.edu.vn`.
3. Phải **cài sẵn EOS Client đúng thư mục**.
4. Phải **chạy thử trước** — vì bản thân nhà trường khuyến cáo test trước ngày thi.
5. Phải có **tai nghe có dây** kèm theo cho môn thi nghe.

→ **Đây chính là lõi khác biệt (core differentiation) của ý tưởng**: không bán "laptop cho thuê", mà bán **"máy đã sẵn sàng thi" (exam-ready machine)** — đã cài EOS + SEB, đã test, kèm tai nghe có dây, giao tận cửa phòng thi. Xem chi tiết tại [mục 10](#10-khoảng-trống-thị-trường--cơ-hội-cho-dịch-vụ-chuyên-cho-thuê-laptop-đi-thi).

### 1.3. Cấu hình laptop nhà trường khuyến nghị cho sinh viên FPT

Dùng để quyết định **nên mua máy gì đưa vào đội máy cho thuê**:

| Thành phần | Khuyến nghị | Nguồn |
|---|---|---|
| RAM | **≥ 8GB và có thể nâng cấp**; mức khuyến nghị là **16GB** | [Gợi ý cấu hình laptop cho tân sinh viên Đại học FPT](https://daihoc.fpt.edu.vn/goi-y-cau-hinh-laptop-cho-tan-sinh-vien-dai-hoc-fpt/) |
| Ổ cứng | **SSD 512GB trở lên** | nt |
| Màn hình | **14–16 inch**, độ phân giải **FHD (1920×1080) trở lên** | nt |
| CPU | Ưu tiên CPU tiết kiệm điện, hiệu năng tốt; AMD Ryzen 7000 series trở lên là lựa chọn đáng cân nhắc | nt |
| Ví dụ máy | **HP 14s-em0086AU** — Ryzen 5 7520U, RAM 16GB — **giá hơn 12 triệu đồng** | nt |
| Tầm giá | Máy chip AMD tầm **15–25 triệu đồng** phần lớn đã có sẵn 16GB RAM + 512GB SSD | nt |

**Lưu ý cho bài toán vốn:** với dịch vụ **thi cử**, cấu hình không cần cao như máy học lập trình cả kỳ. Phần mềm EOS/SEB là ứng dụng thi trắc nghiệm/tự luận, không phải render đồ hoạ. Máy cũ i5 Gen 8 / RAM 8GB / SSD 256GB là đủ — xem [mục 9.4](#94-chi-phí-đầu-tư-máy-tham-khảo-cho-bài-toán-vốn).

### 1.4. Bối cảnh campus

| Thông tin | Chi tiết | Nguồn |
|---|---|---|
| Địa chỉ | Khu đô thị FPT, **P. Hoà Hải, Q. Ngũ Hành Sơn, TP. Đà Nẵng** | [Campus Đà Nẵng – Trường Đại học FPT](https://daihoc.fpt.edu.vn/da-nang/) |
| Diện tích | **5,1 ha**, khởi công **2018** | nt |
| Cơ sở vật chất | Toà **Alpha** và **Gamma** (phòng học, phòng thực hành, phòng chức năng, thư viện); sân bóng cỏ nhân tạo **1.500 m²** có hệ thống đèn; sân bóng rổ; **2 sân bóng chuyền**; khu street workout; thư viện **hơn 33.000 đầu sách**; căng tin, ký túc xá, hồ sen, công viên cây xanh | nt |
| Số sinh viên | **KHÔNG tìm được số liệu công khai** cho campus Đà Nẵng (2024–2026) | — |

> **Cảnh báo:** Một kết quả tìm kiếm có nhắc con số "10.000 sinh viên, 5.000/ca" nhưng đó là **quy mô quy hoạch của campus TP.HCM**, KHÔNG phải Đà Nẵng. **Tuyệt đối không dùng con số này cho campus Đà Nẵng trong proposal.** Cách lấy số đúng: liên hệ Phòng Công tác Sinh viên / Ban Đào tạo FPTU Đà Nẵng ([fptudn.info.vn](https://fptudn.info.vn/)), hoặc đếm số lớp trong lịch thi công bố.

---

## 2. BẢN ĐỒ NHÀ CUNG CẤP TẠI ĐÀ NẴNG

### Bảng 1 — Các đơn vị cho thuê laptop tại Đà Nẵng

| # | Đơn vị | Địa chỉ | Hotline / Liên hệ | Website | Ghi chú nổi bật |
|---|---|---|---|---|---|
| 1 | **Trường Giang Computer** | 118 Hàm Nghi, TP. Đà Nẵng | Hotline **1900 2007**; Zalo **0972.0909.49**; email info@truonggiang.vn | [truonggiang.vn/cho-thue-laptop.html](https://truonggiang.vn/cho-thue-laptop.html) | Giá **từ 50K/ngày**. HP, Dell, Acer, Asus, Macbook; Core 2 Duo → i7, Macbook Air/Pro. **Giao hàng trong ngày tại Đà Nẵng**, nhiều chi nhánh. Phục vụ sự kiện, hội nghị, đào tạo, **thi tuyển công chức**. Có cả dịch vụ sửa laptop tại 118 Hàm Nghi |
| 2 | **leminhSTORE Computer** | 107 Phạm Cự Lượng, P. An Hải, Q. Sơn Trà, Đà Nẵng | **0915 819 967** (alo/sms/Zalo); Hotline **0236 7777 999** | [leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html](https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html) | **Chuyên mảng sinh viên**, giá **từ 38K/ngày**. **Cọc 500.000đ – 2.000.000đ** tuỳ dòng máy & thời gian, **hoàn 100%** khi trả đúng tình trạng. **Giảm 10–20% cho nhóm 2–10 bạn**. Giờ mở cửa: T2–T7 08:00–12:00 & 13:30–19:00; CN 08:30–12:00 & 13:30–17:30. Có cả thuê iMac, thuê PC Gaming/Workstation |
| 3 | **Đình Hậu Computer** | 91 Phạm Như Xương, P. Hoà Khánh Nam, Q. Liên Chiểu, Đà Nẵng (gần ĐH Sư phạm ĐN) | **0948 637 037** – **0984 637 037** | [maytinhdinhhau.vn/dich-vu-cho-thue-laptop-tai-da-nang/](https://maytinhdinhhau.vn/dich-vu-cho-thue-laptop-tai-da-nang/) | **Miễn phí vận chuyển và lắp đặt**. Thuê theo ngày/tuần/tháng. Hỗ trợ kỹ thuật miễn phí 24/7. Có trang riêng "[Địa chỉ cho sinh viên thuê laptop giá rẻ tại Đà Nẵng](https://maytinhdinhhau.vn/dia-chi-cho-sinh-vien-thue-laptop-gia-re-tai-da-nang/)" |
| 4 | **Sky Computer** (Cty TNHH Công nghệ & Giải pháp Sky) | 115 Yên Thế, P. Hoà An, Q. Cẩm Lệ, Đà Nẵng | **0708 084 444** | [skycomputer.vn/dich-vu/cho-thue-may-tinh-laptop-tai-da-nang/](https://skycomputer.vn/dich-vu/cho-thue-may-tinh-laptop-tai-da-nang/) | Thành lập **22/12/2008** (gần 15 năm thị trường ĐN). **Miễn phí giao trong thành phố cho đơn từ 5 máy trở lên**. Kho máy nhập khẩu phục vụ sự kiện **10–200 máy**. Dell, HP, ThinkPad, Asus; i3/i5/i7 trở lên. Hỗ trợ nhân sự tại chỗ trong TP. Đà Nẵng |
| 5 | **Chothuelaptop.com.vn** | 62A Phạm Như Xương, Q. Liên Chiểu, Đà Nẵng | (chưa lấy được) | [chothuelaptop.com.vn/thue-laptop-da-nang/](https://chothuelaptop.com.vn/thue-laptop-da-nang/) | Đa dạng cấu hình Core 2 Duo, i3, i7, Macbook Air/Pro. Có trang [thuê laptop theo tháng](https://chothuelaptop.com.vn/thue-laptop-theo-thang/) |
| 6 | **SEA Event** | 57 Nguyễn Xuân Nhĩ, Q. Hải Châu, Đà Nẵng (một nguồn khác ghi 217 Trần Phú, P. Phước Ninh, Q. Hải Châu) | **0968 37 4343** | [seaevent.vn/cho-thue-laptop-su-kien-tai-da-nang/](https://seaevent.vn/cho-thue-laptop-su-kien-tai-da-nang/) | **Case study đáng chú ý:** cho thuê **hơn 100 laptop phục vụ đào tạo/đánh giá AUN-QA tại Trường ĐH Bách Khoa – ĐH Đà Nẵng**, ngày **26–30/10/2020** (đợt đánh giá ngoài lần thứ 186, 4 chương trình đào tạo). → Chứng minh **các trường ĐH tại Đà Nẵng CÓ thuê laptop số lượng lớn**. [Link case study](https://seaevent.vn/cho-thue-laptop-phuc-vu-dao-tao-tai-truong-dai-hoc-bach-khoa-da-nang/) |
| 7 | **Công ty Phương Châu** (vận hành thuelaptop.com.vn) | Có mặt tại 63 tỉnh thành, phục vụ Đà Nẵng | **0936 228 200** | [thuelaptop.com.vn](https://thuelaptop.com.vn/) | **20 năm kinh nghiệm**. Trụ sở chính có **hơn 20 nhân sự kỹ thuật, 300 laptop và hơn 100 PC** chuyên cho thuê. **KHÔNG yêu cầu đặt cọc** — điểm khác biệt lớn nhất. Giá i5 **80k/máy/ngày**, i7 **100k/máy/ngày**. Có trang [Địa điểm cho thuê laptop tại Đà Nẵng giá rẻ](https://thuelaptop.com.vn/dia-diem-cho-thue-laptop-tai-da-nang-gia-re.html) |
| 8 | **Thuelaptop.vn** | Phục vụ Đà Nẵng | (chưa lấy được) | [thuelaptop.vn/thue-laptop-da-nang-gia-re-chi-tu-10k/](https://www.thuelaptop.vn/thue-laptop-da-nang-gia-re-chi-tu-10k/) | Tiêu đề trang quảng cáo **"cấu hình Gen 10 giá chỉ từ 10k/ngày"**. ⚠️ Con số 10k/ngày **rất thấp so với mặt bằng**, nhiều khả năng là giá thuê dài hạn/số lượng lớn quy đổi. **Cần xác minh.** Có [trang chính sách kinh doanh cho thuê thiết bị](https://www.thuelaptop.vn/gioi-thieu/chinh-sach-kinh-doanh-cho-thue-thiet-bi/) |
| 9 | **Gia Tín Computer** (Tin Học Gia Tín) | 183 Huỳnh Tấn Phát, Đà Nẵng | (chưa lấy được) | — | Hỗ trợ cài đặt, lắp đặt miễn phí; máy i3/i5/i7 trở lên. Nguồn: [Top 15+ công ty cho thuê laptop Đà Nẵng](https://top10danang.com/top-10-cong-ty-cho-thue-laptop-da-nang-uy-tin-gia-re/) |
| 10 | **Song Vũ** | 444 Điện Biên Phủ, Q. Thanh Khê, Đà Nẵng | **0905 821 068** / **0888 933 477** | — | Nguồn: [Top 15+ công ty cho thuê laptop Đà Nẵng](https://top10danang.com/top-10-cong-ty-cho-thue-laptop-da-nang-uy-tin-gia-re/) |
| 11 | **DH Lend** | Đà Nẵng (chưa có địa chỉ cụ thể) | (chưa lấy được) | — | "Nhiều năm kinh nghiệm thuê laptop giá rẻ tại Đà Nẵng; **miễn phí hỗ trợ vận chuyển và lắp đặt**, cài phần mềm theo yêu cầu". Nguồn: [Top 7 dịch vụ cho thuê laptop Đà Nẵng](https://danang.plus/thue-laptop/) |
| 12 | **Danang Events** | Đà Nẵng | (chưa lấy được) | — | Cho thuê laptop phục vụ hội nghị, hội thảo, in ấn, trình chiếu, tổ chức sự kiện. Nguồn: [Top 7 dịch vụ cho thuê laptop Đà Nẵng](https://danang.plus/thue-laptop/) |
| 13 | **Xoo Event** | Đà Nẵng | (chưa lấy được) | [xooevent.com/cho-thue-laptop-may-tinh-so-luong-lon-tai-da-nang/](https://xooevent.com/cho-thue-laptop-may-tinh-so-luong-lon-tai-da-nang/) | Cho thuê laptop, máy tính **số lượng lớn** tại Đà Nẵng |
| 14 | **SAOLA** (CTCP Công nghệ SAOLA) | Toàn quốc: Hà Nội, TP.HCM, **Đà Nẵng** | (chưa lấy được) | [saolatech.com.vn](https://saolatech.com.vn/) | Nhà máy sản xuất máy tính OEM/ODM có mảng cho thuê. **Chính sách không cọc nếu có giấy bảo lãnh của nhà trường** (xem [mục 5.3](#53-mô-hình-không-cọc--rất-quan-trọng-với-startup-sinh-viên)). Có [bảng giá thuê công khai](https://saolatech.com.vn/bang-gia-thue-3425667) |
| 15 | **Kim Anh Computer** (CN4) | **248 Ngũ Hành Sơn, Q. Ngũ Hành Sơn, Đà Nẵng** | **0815 126 126** | [kimanh.com.vn](https://www.kimanh.com.vn/linh-kien-laptop/) | ⚠️ **Đây là đơn vị gần campus FPT nhất được tìm thấy** (cùng quận Ngũ Hành Sơn). Thành lập **2014** từ cửa hàng trên đường Hàm Nghi, nay có **6 chi nhánh**. **NHƯNG:** kết quả tìm kiếm chỉ xác nhận **sửa chữa, bảo hành, bán linh kiện, thu cũ đổi mới** — **KHÔNG xác nhận có dịch vụ cho thuê**. Cần gọi hỏi trực tiếp |

**→ Tổng: 15 đơn vị, trong đó 13 đơn vị xác nhận có dịch vụ cho thuê laptop tại/phục vụ Đà Nẵng.** Yêu cầu đề bài là 8–12 đơn vị, đã vượt.

### 2.1. Nhận xét về phân bố địa lý — CỰC KỲ QUAN TRỌNG

Đây là phát hiện có giá trị nhất cho phần "khoảng trống thị trường":

| Đơn vị | Quận | Khoảng cách tương đối tới campus FPT (P. Hoà Hải, Q. Ngũ Hành Sơn) |
|---|---|---|
| Kim Anh Computer CN4 (248 Ngũ Hành Sơn) | **Ngũ Hành Sơn** | Cùng quận — gần nhất, nhưng **chưa xác nhận có cho thuê** |
| leminhSTORE (107 Phạm Cự Lượng) | Sơn Trà | Xa — qua cầu, khác quận |
| Trường Giang (118 Hàm Nghi) | Thanh Khê / trung tâm | Rất xa — gần như đầu kia thành phố |
| Đình Hậu (91 Phạm Như Xương) | **Liên Chiểu** | Rất xa — đầu Tây Bắc thành phố |
| Chothuelaptop.com.vn (62A Phạm Như Xương) | **Liên Chiểu** | Rất xa |
| Sky Computer (115 Yên Thế) | Cẩm Lệ | Xa |
| SEA Event (Hải Châu) | Hải Châu | Xa — trung tâm |
| Song Vũ (444 Điện Biên Phủ) | Thanh Khê | Rất xa |

**Kết luận:** **Không có một đơn vị nào xác nhận có dịch vụ cho thuê laptop đặt tại hoặc ngay cạnh P. Hoà Hải / Q. Ngũ Hành Sơn.** Cụm cho thuê laptop sinh viên của Đà Nẵng tập trung ở **Q. Liên Chiểu** (Đình Hậu, Chothuelaptop.com.vn — cùng nằm trên đường Phạm Như Xương), vì đó là khu vực **Làng Đại học Đà Nẵng** (ĐH Bách Khoa, ĐH Sư phạm, ĐH Kinh tế). Campus FPT ở Ngũ Hành Sơn **nằm tách biệt khỏi cụm này**.

→ Sinh viên FPT phát hiện hỏng máy lúc 6h sáng ngày thi **không có lựa chọn nào trong bán kính đi bộ/xe máy 10 phút**.

---

## 3. BẢN ĐỒ NHÀ CUNG CẤP TOÀN QUỐC (đối chuẩn mô hình & giá)

### Bảng 2 — Các đơn vị lớn ngoài Đà Nẵng

| # | Đơn vị | Địa chỉ | Hotline | Website | Điểm nổi bật |
|---|---|---|---|---|---|
| 1 | **ICT Sài Gòn** | 232 Chu Văn An, Q. Bình Thạnh, TP.HCM | **0906 652 739** | [ictsaigon.com.vn/cho-thue-laptop](https://ictsaigon.com.vn/cho-thue-laptop) | **Setup tận nơi, từ 49.000đ/ngày**. Dải giá **49.000đ/ngày → 3.000.000đ/tháng**. Có gói [thuê laptop không cọc](https://ictsaigon.com.vn/thue-laptop-khong-coc). Cho thuê PC từ [99K/ngày](https://ictsaigon.com.vn/cho-thue-pc-may-tinh-de-ban) |
| 2 | **Laptop SGN** | 50C Trần Khắc Chân, P.15, Q. Phú Nhuận, TP.HCM | **0906 961 347**; laptopsgn@gmail.com | [laptopsgn.com/cho-thue-laptop/](https://laptopsgn.com/cho-thue-laptop/) | ⭐ **Cam kết giao máy + cài đặt tận nhà/văn phòng trong vòng 2 GIỜ** kể từ khi xác nhận đơn, khu vực nội thành TP.HCM. Giấy tờ linh hoạt: **CCCD/CMND HOẶC GPLX HOẶC SIM chính chủ**. Hỗ trợ kỹ thuật 24/7 miễn phí. Từ **150.000đ/ngày**. [Trang dịch vụ giao nhanh 2h](https://laptopsgn.com/tin-tuc/dich-vu-cho-thue-laptop-tphcm-gia-re-giao-2h/) |
| 3 | **MiT Group** | TP.HCM, Bình Dương, Đồng Nai, BR-VT | (chưa lấy được) | [mitgroup.vn/cho-thue-laptop/](https://mitgroup.vn/cho-thue-laptop/) | **Giá thấp nhất thị trường tìm được: từ 29.000đ/ngày**. Cấu hình i5–i9, RAM 8–16GB, SSD. **Giao trong ngày**. **Đổi máy hoặc nâng cấu hình không tính thêm phí**. Có gói [thuê laptop không cọc](https://mitgroup.vn/thue-laptop-khong-coc/) và [thuê laptop sinh viên](https://mitgroup.vn/thue-laptop-sinh-vien/) |
| 4 | **SKYLAP** (Cty TNHH TM DV SKYLAP) | TP.HCM | (chưa lấy được) | [skylap.vn/dich-vu-cho-thue/cho-thue-laptop/](https://skylap.vn/dich-vu-cho-thue/cho-thue-laptop/) | Bảng giá công khai theo từng model cụ thể (xem Bảng 3) |
| 5 | **Tin học PNN** | 238/4 Đội Cung, P.9, Q.11, TP.HCM | **0931 454 838** | [tinhocpnn.com/bang-gia-cho-thue-laptop-may-tinh-gia-re/](https://tinhocpnn.com/bang-gia-cho-thue-laptop-may-tinh-gia-re/) | **Từ 500.000đ/tháng (tức chưa tới 20.000đ/ngày)**. Phân khúc rõ: laptop văn phòng / đồ hoạ / gaming. Fanpage: facebook.com/tinhocpnn |
| 6 | **SAOLA** | Hà Nội, TP.HCM, Đà Nẵng | (chưa lấy được) | [saolatech.com.vn/bang-gia-thue-3425667](https://saolatech.com.vn/bang-gia-thue-3425667) | **Không cọc nếu có giấy bảo lãnh của trường**. ⚠️ Điều khoản bất lợi: "ký thuê theo tuần/tháng nhưng **trả sớm hơn thì vẫn phải trả đủ giá trị hợp đồng**" |
| 7 | **VIETBIS** | Hà Nội | (chưa lấy được) | [vietbis.vn](https://vietbis.vn/tin-tuc/dich-vu-cho-thue-laptop-tai-ha-noi---vietbisvn-2530.html) | Có bài riêng về [thuê laptop không cần đặt cọc tại Hà Nội – điều kiện áp dụng](https://vietbis.vn/tin-tuc/thue-laptop-khong-can-dat-coc-tai-ha-noi-dieu-kien-ap-dung-3116.html) |
| 8 | **Phương Nam Tech** | TP.HCM | (chưa lấy được) | [phuongnamco.com](https://phuongnamco.com/) | ⭐ Có hẳn trang **["Cho thuê laptop thi cử – Giải pháp hữu ích cho sinh viên mùa thi"](https://phuongnamco.com/cho-thue-laptop-thi-cu-giai-phap-huu-ich-cho-sinh-vien-mua-thi/)** — đối thủ khái niệm gần nhất. Máy gọn nhẹ, pin khoẻ, cài sẵn phần mềm, hỗ trợ tận nơi. "Giá chỉ từ vài chục ngàn/ngày" |
| 9 | **Bách Khoa 4** | Hà Nội | (chưa lấy được) | [bk4.com.vn](https://bk4.com.vn/dich-vu-cho-thue-laptop-theo-ngay-tai-ha-noi/) | Thuê theo ngày, giao tận nơi, hỗ trợ kỹ thuật nhanh |
| 10 | **Vi Tính Thiên Ân** | TP.HCM | (chưa lấy được) | [laptopthienan.com](https://laptopthienan.com/cho-thue-laptop-may-tinh-hcm-gia-re-50k.html) | Quảng cáo **50k/ngày** |
| 11 | **Chothuelaptop.info** | Hà Nội, Đà Nẵng | (chưa lấy được) | [chothuelaptop.info](https://chothuelaptop.info/cho-thue-laptop-da-nang-thu-tuc-nhanh-gon/) | Định vị "**thủ tục nhanh gọn**" |
| 12 | **Chothuemaytinh.vn** | — | **0984 131 355** | [chothuemaytinh.vn/cho-thue-laptop-sinh-vien/](https://chothuemaytinh.vn/cho-thue-laptop-sinh-vien/) | Chuyên mảng sinh viên |
| 13 | **Quảng Tin** | TP.HCM | (chưa lấy được) | [quangtin.com](https://quangtin.com/pages/cho-thue-may-tinh-laptop-gia-re-tai-tp-hcm-dich-vu-chuyen-nghiep) | "Giao nhanh 24/7" |
| 14 | **Laptopchothue.com** | Toàn quốc | (chưa lấy được) | [laptopchothue.com](https://laptopchothue.com/) | Chuyên **số lượng lớn** phục vụ đào tạo, sự kiện. Có [trang riêng cho Đà Nẵng](https://laptopchothue.com/dich-vu-cho-thue-laptop-tai-da-nang-laptop-cau-hinh-cao-gia-tot/) |
| 15 | **Thiết bị cho thuê** | — | (chưa lấy được) | [thietbichothue.com/cho-thue-laptop/](https://thietbichothue.com/cho-thue-laptop/) | Thuê theo ngày, tháng |

---

## 4. BẢNG GIÁ THUÊ LAPTOP — TỔNG HỢP TOÀN THỊ TRƯỜNG

### Bảng 3 — Bảng giá theo model/cấu hình cụ thể (số liệu có nguồn)

| Phân khúc | Cấu hình cụ thể | Giá/NGÀY | Giá/TUẦN | Giá/THÁNG | Đơn vị | Nguồn |
|---|---|---|---|---|---|---|
| **Cơ bản (máy đời cũ)** | HP Elitebook 9480m — i5-4310U, 8GB DDR3, SSD 240GB, 14" FHD | **49.000đ** | **300.000đ** | **600.000đ** | ICT Sài Gòn | [ictsaigon.com.vn/cho-thue-laptop-hp-elitebook-9480m](https://ictsaigon.com.vn/cho-thue-laptop-hp-elitebook-9480m) |
| **Cơ bản** | Dell i5-4300M, RAM 8GB, SSD 240GB | **49.000đ** | **300.000đ** | **600.000đ** | SKYLAP | [skylap.vn/dich-vu-cho-thue/cho-thue-laptop-dell-van-phong/](https://skylap.vn/dich-vu-cho-thue/cho-thue-laptop-dell-van-phong/) |
| **Văn phòng i5** | i5-4300, RAM 8GB, SSD 240GB, màn 14" | **50.000đ** | **300.000đ** | **600.000đ** | (nguồn tổng hợp) | [thuelaptop.com.vn/bang-gia-cho-thue-laptop-van-phong.html](https://thuelaptop.com.vn/bang-gia-cho-thue-laptop-van-phong.html) |
| **Văn phòng i5** | Core i5 (không nêu đời) | **80.000đ/máy** | **450.000đ/máy** | **800.000đ/máy** | Phương Châu / tổng hợp ĐN | [thuelaptop.com.vn](https://thuelaptop.com.vn/), [truonggiang.vn](https://truonggiang.vn/cho-thue-laptop.html) |
| **Văn phòng i7** | Core i7 (không nêu đời) | **100.000đ/máy** | **600.000đ/máy** | **1.000.000đ/máy** | Phương Châu / tổng hợp ĐN | nt |
| **Cao cấp i7** | Dell Core i7 | **149.000đ** | **600.000đ** | **1.200.000đ** | (nguồn tổng hợp) | [thuelaptop.com.vn/bang-gia-cho-thue-laptop-van-phong.html](https://thuelaptop.com.vn/bang-gia-cho-thue-laptop-van-phong.html) |
| **Đồ hoạ / Workstation** | Dell Precision Core i7-7700HQ | **180.000đ** | **800.000đ** | **1.700.000đ** | SKYLAP | [skylap.vn/thue-laptop-dell-precision-core-i7-7700hq/](https://skylap.vn/thue-laptop-dell-precision-core-i7-7700hq/) |
| **Gaming** | Cấu hình gaming các loại | **100.000 – 500.000đ** | — | — | ICT Sài Gòn | [ictsaigon.com.vn/thue-laptop-gaming](https://ictsaigon.com.vn/thue-laptop-gaming) |
| **Giá sàn quảng cáo** | i5–i9, RAM 8–16GB, SSD | **từ 29.000đ** | — | — | MiT Group | [mitgroup.vn/cho-thue-laptop/](https://mitgroup.vn/cho-thue-laptop/) |
| **Giá sàn sinh viên ĐN** | Máy học tập cơ bản | **từ 38.000đ** | — | — | leminhSTORE (Đà Nẵng) | [leminhstore.vn](https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html) |
| **Giá sàn ĐN** | Máy cơ bản | **từ 50.000đ** | — | — | Trường Giang (Đà Nẵng) | [truonggiang.vn](https://truonggiang.vn/cho-thue-laptop.html) |
| **Thuê dài hạn rẻ nhất** | Laptop văn phòng | (~<20.000đ quy đổi) | — | **từ 500.000đ** | Tin học PNN | [tinhocpnn.com](https://tinhocpnn.com/bang-gia-cho-thue-laptop-may-tinh-gia-re/) |
| **Trần giá** | Cấu hình cao nhất | — | — | **tới 3.000.000đ** | ICT Sài Gòn | [ictsaigon.com.vn/cho-thue-laptop](https://ictsaigon.com.vn/cho-thue-laptop) |
| **Cao cấp giao nhanh** | Dell, HP, ThinkPad, Macbook | **từ 150.000đ** | — | — | Laptop SGN | [laptopsgn.com](https://laptopsgn.com/tin-tuc/dich-vu-cho-thue-laptop-tphcm-gia-re-giao-2h/) |
| **Mặt bằng chung ĐN** | Mọi loại, tuỳ SL & thời gian | **80.000 – 200.000đ/máy** | — | — | Tổng hợp Đà Nẵng | [truonggiang.vn](https://truonggiang.vn/cho-thue-laptop.html) |

### Bảng 4 — Quy luật chiết khấu theo số lượng & thời gian

| Kịch bản | Giá | Nguồn |
|---|---|---|
| Thuê **5 máy trong 1 ngày** | **150.000đ/máy** | [thuelaptop.com.vn/bang-gia-cho-thue-laptop-do-hoa.html](https://thuelaptop.com.vn/bang-gia-cho-thue-laptop-do-hoa.html) |
| Thuê **5 máy trong 1 tuần** | **450.000đ/máy/tuần** (tức ~64.000đ/máy/ngày — **giảm ~57%**) | nt |
| Nhóm **2–10 sinh viên** | **Giảm 10–20%** | [leminhstore.vn](https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html) |
| Nguyên tắc chung | "Thuê càng lâu / số lượng càng nhiều thì giá càng rẻ" — được xác nhận bởi ICT Sài Gòn, Phương Châu, Tin học PNN, SKYLAP | nhiều nguồn |

### 4.1. Ba nhận xét quan trọng rút ra từ bảng giá

**(1) Giá công bố ở Đà Nẵng CAO HƠN TP.HCM ở cùng phân khúc.**
Cùng một cấu hình Core i5 phổ thông: TP.HCM ~49.000–50.000đ/ngày, trong khi mặt bằng Đà Nẵng được ghi nhận **80.000đ/máy/ngày (i5)** và **100.000đ/máy/ngày (i7)**, dải chung **80.000–200.000đ/máy/ngày**. → Thị trường Đà Nẵng **ít cạnh tranh hơn, biên lợi nhuận tốt hơn**.

**(2) Cấu trúc giá của cả thị trường được thiết kế cho THUÊ DÀI, KHÔNG cho THUÊ NGẮN.**
Đây là phát hiện then chốt. Quan sát tỷ lệ giá của bất kỳ đơn vị nào:

| Gói | Giá (ví dụ ICT Sài Gòn / SKYLAP) | Quy về đơn giá/ngày | Chỉ số |
|---|---|---|---|
| 1 ngày | 49.000đ | 49.000đ/ngày | 100% |
| 1 tuần (7 ngày) | 300.000đ | ~42.900đ/ngày | 87% |
| 1 tháng (30 ngày) | 600.000đ | ~20.000đ/ngày | **41%** |

→ Toàn ngành **thưởng cho khách thuê lâu và phạt khách thuê ngắn**. Không ai thiết kế sản phẩm cho khách thuê **nửa ngày** hoặc **3 giờ**. Trong khi đó, nhu cầu "thuê laptop đi thi" bản chất là **thuê 3–4 giờ, 1–2 lần/kỳ**.

**(3) KHÔNG TỒN TẠI gói thuê theo GIỜ hoặc theo BUỔI trên toàn thị trường Việt Nam.**
Đã tìm kiếm trực tiếp cụm từ **"thuê laptop theo giờ"**. Kết quả: **không có đơn vị nào cung cấp gói theo giờ**. Tất cả kết quả trả về đều là **thuê theo ngày / tuần / tháng / năm**, kể cả VIETBIS, Bách Khoa 4, Chinhnhan.vn, Laptopchothue.com, ALi Việt, Trường Giang. → Đây là **khoảng trống sản phẩm rõ rệt nhất**.

---

## 5. ĐIỀU KIỆN THUÊ, GIẤY TỜ VÀ ĐẶT CỌC

### Bảng 5 — Điều kiện thuê theo từng đơn vị

| Đơn vị | Giấy tờ yêu cầu | Mức đặt cọc | Hình thức cọc | Nguồn |
|---|---|---|---|---|
| **Mặt bằng chung Đà Nẵng** | CMND/CCCD | **Cọc bằng GIÁ TRỊ MÁY** — "tất cả các đơn vị cho thuê laptop tại Đà Nẵng đều áp dụng đặt cọc giá trị máy khi thuê" | Tiền mặt | [thuelaptop.com.vn/dia-diem-cho-thue-laptop-tai-da-nang-gia-re.html](https://thuelaptop.com.vn/dia-diem-cho-thue-laptop-tai-da-nang-gia-re.html) |
| **leminhSTORE** (ĐN) | **CMND/CCCD bản gốc** (+ bản photo nếu cần), có thể kèm **thẻ sinh viên hoặc giấy xác nhận đang học**, **thông tin liên hệ gia đình**, **địa chỉ tạm trú** | **500.000đ – 2.000.000đ** tuỳ dòng máy & thời gian thuê. **Hoàn lại 100%** khi trả máy đúng tình trạng | Tiền mặt | [leminhstore.vn](https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html) |
| **Phương Châu** | — | **KHÔNG CỌC** — "khách thuê không phải đặt cọc giá trị máy", "không cần phải đặt cọc bất cứ đồng nào" | Không | [thuelaptop.com.vn](https://thuelaptop.com.vn/), [dich-vu-cho-thue-laptop-gaming.html](https://thuelaptop.com.vn/dich-vu-cho-thue-laptop-gaming.html) |
| **Laptop SGN** | **CCCD/CMND HOẶC Giấy phép lái xe HOẶC SIM điện thoại chính chủ** (chỉ cần 1 trong 3) | — | — | [laptopsgn.com/cho-thue-laptop/](https://laptopsgn.com/cho-thue-laptop/) |
| **SAOLA** | **Giấy giới thiệu/bảo lãnh của nhà trường** | **KHÔNG CỌC** nếu có giấy bảo lãnh — nhà trường đồng ý bảo đảm thông tin, chịu trách nhiệm quản lý sinh viên và phối hợp xử lý vi phạm về hư hỏng/mất thiết bị | Không (thay bằng bảo lãnh) | [saolatech.com.vn/thue-laptop-khong-can-dat-coc-tai-ha-noi...](https://saolatech.com.vn/thue-laptop-khong-can-dat-coc-tai-ha-noi-giai-phap-tiet-kiem-cho-sinh-vien-3425752) |
| **ICT Sài Gòn** | — | Có gói **không cọc** (gọi là "Đặc quyền tín chấp") | — | [ictsaigon.com.vn/thue-laptop-khong-coc](https://ictsaigon.com.vn/thue-laptop-khong-coc) |
| **MiT Group** | — | Có gói **không cọc** | — | [mitgroup.vn/thue-laptop-khong-coc/](https://mitgroup.vn/thue-laptop-khong-coc/) |
| **Thuê ngắn hạn <1 tháng (chung)** | Chỉ cần **CCCD hoặc thẻ sinh viên** | Không cọc (áp dụng cho thuê ngắn hạn dưới 1 tháng) | — | [thuelaptop.com.vn/cho-sinh-vien-thue-may-tinh-khong-can-dat-coc.html](https://thuelaptop.com.vn/cho-sinh-vien-thue-may-tinh-khong-can-dat-coc.html) |
| **Doanh nghiệp (chung)** | **Giấy phép kinh doanh bản scan + công văn/giấy giới thiệu**; xác minh địa chỉ công ty và nhu cầu sử dụng. Không cần giấy tờ công chứng phức tạp | Không cọc | [vietbis.vn](https://vietbis.vn/tin-tuc/thue-laptop-khong-can-dat-coc-tai-ha-noi-dieu-kien-ap-dung-3116.html) |

### 5.1. Quy trình thuê chuẩn của thị trường (5 bước)

Theo mô tả tổng hợp từ các đơn vị ([thuelaptop.com.vn](https://thuelaptop.com.vn/dia-diem-cho-thue-laptop-tai-da-nang-gia-re.html), [ictsaigon.com.vn](https://ictsaigon.com.vn/kinh-nghiem-thue-laptop-uy-tin-dam-bao), [maytinhdinhhau.vn](https://maytinhdinhhau.vn/dich-vu-cho-thue-laptop-tai-da-nang/)):

1. **Liên hệ hotline / Zalo** → nêu yêu cầu; nhân viên tư vấn dòng máy và phương án thuê
2. **Lựa chọn cấu hình** phù hợp nhu cầu
3. **Cung cấp giấy tờ tuỳ thân** (CMND/CCCD)
4. **Ký hợp đồng thuê và đặt cọc** (nếu có yêu cầu) — chi tiết mức cọc ghi rõ trên **phiếu thuê/biên nhận**, minh bạch từ đầu
5. **Kiểm tra tình trạng máy và phụ kiện** trước khi nhận; nhân viên đến địa chỉ khách để lắp đặt và kiểm tra máy

### 5.2. Điểm yếu chí mạng của quy trình này đối với tình huống "sáng ngày thi"

Quy trình 5 bước trên mất **tối thiểu vài giờ đến 1 ngày** (tư vấn → báo giá → hợp đồng → chuẩn bị máy → giao & lắp đặt). Với sinh viên phát hiện máy hỏng lúc **6h30 sáng, ca thi 7h30**, quy trình này **hoàn toàn vô dụng**.

Thêm vào đó, rào cản cọc: mức cọc phổ biến ở Đà Nẵng là **"bằng giá trị máy"**, hoặc **500.000đ – 2.000.000đ** ở nơi thân thiện nhất với sinh viên (leminhSTORE). Một sinh viên năm nhất **thường không có 2 triệu tiền mặt sẵn lúc 6h30 sáng**.

### 5.3. Mô hình "không cọc" — rất quan trọng với startup sinh viên

Thị trường thừa nhận thẳng thắn: *"thuê laptop không cần đặt cọc là mong muốn của tất cả khách hàng nhưng hiện nay **không nhà cung cấp nào áp dụng** vì mang nhiều rủi ro"* ([vietbis.vn](https://vietbis.vn/tin-tuc/thue-laptop-khong-can-dat-coc-tai-ha-noi-dieu-kien-ap-dung-3116.html)). Nhưng đã hình thành **3 cơ chế thay thế cọc tiền**:

| Cơ chế | Mô tả | Áp dụng được cho startup FPT? |
|---|---|---|
| **Bảo lãnh của nhà trường** | Nhà trường ký giấy bảo lãnh, cam kết quản lý sinh viên và phối hợp xử lý khi hư hỏng/mất máy (mô hình SAOLA) | ⭐⭐⭐ **Rất phù hợp** — có thể xin phối hợp với Phòng CTSV FPTU Đà Nẵng |
| **Tín chấp bằng giấy tờ linh hoạt** | Chấp nhận CCCD **hoặc** GPLX **hoặc** SIM chính chủ (mô hình Laptop SGN) | ⭐⭐ Phù hợp |
| **Thuê ngắn hạn <1 tháng chỉ cần CCCD/thẻ SV** | Không cọc tiền cho kỳ thuê ngắn | ⭐⭐⭐ **Rất phù hợp** — thuê đi thi vốn là ngắn hạn |

> **Insight cho proposal:** Sinh viên FPT có **mã số sinh viên, tài khoản FAP/LMS, thẻ sinh viên, và bị ràng buộc bởi quy chế nhà trường**. Đây là **tài sản tín chấp phi tiền mặt cực mạnh** mà các đơn vị cho thuê thương mại bên ngoài không khai thác được — vì họ không biết sinh viên đó là ai, học lớp nào, còn mấy kỳ nữa mới ra trường. Một startup **do sinh viên FPT vận hành, trong khuôn viên FPT** có thể dùng chính danh tính sinh viên làm cọc → **bỏ hoàn toàn cọc tiền mặt** → phá bỏ rào cản lớn nhất.

---

## 6. CHÍNH SÁCH BỒI THƯỜNG HƯ HỎNG & CƠ SỞ PHÁP LÝ

### 6.1. Chính sách thương mại của các đơn vị

| Chính sách | Nội dung | Nguồn |
|---|---|---|
| **Đổi máy khi lỗi** | "Máy được bảo trì liên tục, nếu có vấn đề thì **đổi máy mới không tốn thêm chi phí**" | [laptopsgn.com/tin-tuc/thue-laptop-sinh-vien/](https://laptopsgn.com/tin-tuc/thue-laptop-sinh-vien/) |
| **Đổi máy / nâng cấu hình** | "Khách có thể **đổi máy hoặc nâng cấu hình không mất thêm chi phí**" | [mitgroup.vn/cho-thue-laptop/](https://mitgroup.vn/cho-thue-laptop/) |
| **Hỗ trợ sự cố** | "Nếu chẳng may máy gặp sự cố, dịch vụ sẽ **hỗ trợ đổi máy hoặc sửa chữa ngay**. Không tốn thêm chi phí hay mất thời gian bảo hành" | [saolatech.com.vn](https://saolatech.com.vn/thue-laptop-cho-sinh-vien-giai-phap-tien-loi-tiet-kiem-va-hien-dai-3425768) |
| **Hỗ trợ kỹ thuật** | **24/7 miễn phí** — xử lý lỗi phần cứng, lỗi hệ điều hành, cài đặt phần mềm trong suốt thời gian thuê | [laptopsgn.com/cho-thue-laptop/](https://laptopsgn.com/cho-thue-laptop/), [maytinhdinhhau.vn](https://maytinhdinhhau.vn/dich-vu-cho-thue-laptop-tai-da-nang/) |
| **Hoàn cọc** | leminhSTORE: **hoàn lại 100%** khi trả máy đúng tình trạng | [leminhstore.vn](https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html) |
| **Kiểm tra trước bàn giao** | "Thiết bị cho thuê được **kiểm tra nghiêm ngặt** trước khi đến tay khách"; máy được kiểm tra kỹ để đảm bảo **Windows và phần mềm cơ bản sẵn sàng, pin ổn định, ngoại hình sạch sẽ** | [laptopsgn.com/cho-thue-laptop/](https://laptopsgn.com/cho-thue-laptop/) |
| **Điều khoản bất lợi cần biết** | SAOLA: "ký thuê theo tuần/tháng nhưng **trả sớm hơn thì tổng tiền thuê vẫn bằng đúng giá trị hợp đồng**" | [saolatech.com.vn/bang-gia-thue-3425667](https://saolatech.com.vn/bang-gia-thue-3425667) |

> ⚠️ **Lưu ý:** Không tìm được **điều khoản bồi thường định lượng cụ thể** (ví dụ "vỡ màn hình đền X đồng", "mất máy đền Y% giá trị") công bố công khai trên website của bất kỳ đơn vị nào. Các điều khoản này nằm trong **hợp đồng/phiếu thuê ký tại quầy**, không đăng web. → Cần lấy mẫu hợp đồng thực tế khi đi khảo sát.

### 6.2. Cơ sở pháp lý Việt Nam về bồi thường trong hợp đồng thuê tài sản

| Nội dung | Quy định | Nguồn |
|---|---|---|
| Căn cứ pháp lý | **Bộ luật Dân sự 2015, Điều 554 và Điều 557** (hợp đồng thuê tài sản, nghĩa vụ bên thuê) | [congchung247.com.vn – Thuê thiết bị làm hỏng: Bên thuê có phải bồi thường?](https://congchung247.com.vn/thue-thiet-bi-lam-hong-ben-thue-co-phai-boi-thuong/) |
| Nguyên tắc bồi thường | Bên thuê có trách nhiệm bồi thường **theo giá trị thực tế tài sản hư hại hoặc chi phí sửa chữa**. Bên cho thuê có quyền yêu cầu bồi thường **toàn bộ chi phí sửa chữa hoặc thay thế thiết bị** | nt |
| Xác định mức bồi thường | Dựa trên **hoá đơn sửa chữa, giá trị tài sản, hoặc thoả thuận trong hợp đồng**. Mức bồi thường phải **đủ để khôi phục tình trạng ban đầu hoặc bù đắp giá trị đã mất** | [vanphongcongchung.info – Quy định về bồi thường thiệt hại trong hợp đồng thuê tài sản](https://vanphongcongchung.info/quy-dinh-ve-boi-thuong-thiet-hai-trong-hop-dong-thue-tai-san/) |
| Vai trò hợp đồng | Hợp đồng thể hiện quy định về **trách nhiệm, chi phí bồi thường và hình thức thanh toán**. Nếu bên thuê chối trách nhiệm, **hợp đồng là chứng cứ pháp lý quan trọng để khởi kiện** | [congchung247.com.vn](https://congchung247.com.vn/thue-thiet-bi-lam-hong-ben-thue-co-phai-boi-thuong/) |
| Giải quyết tranh chấp | Khởi kiện tại **Toà án Nhân dân** dựa trên hợp đồng thuê và Điều 554, 557 BLDS 2015 | nt |
| Tham khảo thêm | Trường hợp làm mất laptop và không chịu đền bù | [luatminhkhue.vn – Làm mất laptop nhưng không chịu trả tiền đền bù xử lý thế nào?](https://luatminhkhue.vn/lam-mat-laptop-nhung-khong-chiu-tra-tien-den-bu-.aspx) |
| Bồi thường tài sản gửi giữ | Nguyên tắc đền bù thiệt hại khi làm mất tài sản gửi giữ | [luatduonggia.vn](https://luatduonggia.vn/phap-luat/den-bu-thiet-hai-khi-lam-mat-tai-san-gui-giu/) |

> **Hàm ý cho proposal:** Startup **bắt buộc phải có mẫu hợp đồng/phiếu thuê bằng văn bản** (dù là e-contract ký trên web), ghi rõ: (a) tình trạng máy khi giao, (b) mức bồi thường cho từng loại hư hỏng, (c) giá trị đền bù khi mất máy. Không có văn bản → khi tranh chấp gần như **không có cơ sở đòi bồi thường**. Đây cũng là một mục có thể đưa vào phần "Quản trị rủi ro" của proposal.

---

## 7. GIAO TẬN NƠI VÀ CAM KẾT THỜI GIAN (SLA)

### Bảng 6 — So sánh năng lực giao nhận

| Đơn vị | Cam kết giao | Phí giao | Nguồn |
|---|---|---|---|
| **Laptop SGN** (TP.HCM) | ⭐ **Trong vòng 2 GIỜ** kể từ khi xác nhận đơn, khu vực nội thành TP.HCM — **đây là SLA nhanh nhất tìm được trên toàn thị trường VN** | — | [laptopsgn.com/tin-tuc/dich-vu-cho-thue-laptop-tphcm-gia-re-giao-2h/](https://laptopsgn.com/tin-tuc/dich-vu-cho-thue-laptop-tphcm-gia-re-giao-2h/) |
| **Trường Giang** (Đà Nẵng) | **Giao hàng trong ngày** tại Đà Nẵng, nhiều chi nhánh khắp thành phố | — | [truonggiang.vn/cho-thue-laptop.html](https://truonggiang.vn/cho-thue-laptop.html) |
| **MiT Group** | **Giao trong ngày**, giao tận nơi kèm lắp đặt và hỗ trợ kỹ thuật nhanh | — | [mitgroup.vn/cho-thue-laptop/](https://mitgroup.vn/cho-thue-laptop/) |
| **Sky Computer** (Đà Nẵng) | Không nêu thời gian | **Miễn phí giao trong thành phố cho đơn từ 5 MÁY TRỞ LÊN** ⚠️ (tức thuê 1 máy **không được** miễn phí giao) | [skycomputer.vn](https://skycomputer.vn/dich-vu/cho-thue-may-tinh-laptop-tai-da-nang/) |
| **Đình Hậu Computer** (Đà Nẵng) | Không nêu thời gian | **Miễn phí vận chuyển và lắp đặt** | [maytinhdinhhau.vn](https://maytinhdinhhau.vn/dich-vu-cho-thue-laptop-tai-da-nang/) |
| **DH Lend** (Đà Nẵng) | Không nêu thời gian | **Miễn phí hỗ trợ vận chuyển và lắp đặt** | [danang.plus/thue-laptop/](https://danang.plus/thue-laptop/) |
| **ICT Sài Gòn** | "Setup tận nơi" | — | [ictsaigon.com.vn/cho-thue-laptop](https://ictsaigon.com.vn/cho-thue-laptop) |
| **Quảng Tin** (TP.HCM) | "Giao nhanh 24/7" | — | [quangtin.com](https://quangtin.com/pages/cho-thue-may-tinh-laptop-gia-re-tai-tp-hcm-dich-vu-chuyen-nghiep) |
| **Laptop SGN / Đình Hậu** | Hỗ trợ kỹ thuật **24/7 miễn phí** trong suốt thời gian thuê | Miễn phí | nhiều nguồn |

### 7.1. Nhận xét

- **SLA nhanh nhất toàn quốc là 2 giờ** (Laptop SGN, chỉ ở TP.HCM). **Tại Đà Nẵng, cam kết tốt nhất chỉ là "trong ngày"** (Trường Giang).
- **"Trong ngày" là vô nghĩa với ca thi 7h30 sáng.** Nếu sinh viên đặt lúc 6h30, "giao trong ngày" có thể là 15h chiều — đã thi xong từ lâu.
- Nhiều đơn vị **chỉ miễn phí giao khi thuê từ 5 máy trở lên** (Sky Computer) → khách lẻ 1 máy bị phân biệt đối xử.
- → **Không có bất kỳ đơn vị nào ở Đà Nẵng cam kết SLA tính bằng PHÚT.** Đây là khoảng trống thứ hai.

---

## 8. KÊNH PHI CHÍNH THỨC: FACEBOOK / CHỢ SINH VIÊN

### 8.1. Kết quả tìm kiếm

Đã tìm kiếm cụm từ *"nhóm Facebook cho thuê laptop sinh viên Đà Nẵng chợ sinh viên FPT"*.

**Kết quả: KHÔNG tìm thấy nhóm Facebook chuyên cho thuê laptop nào tại Đà Nẵng qua công cụ tìm kiếm web.** Các kết quả trả về đều là **doanh nghiệp chính thức** (leminhSTORE, Trường Giang, MiT Group, SAOLA) hoặc fanpage bán lẻ ([FPTShop Đà Nẵng 07 Nguyễn Văn Thoại](https://www.facebook.com/p/FPTShop-%C4%90%C3%A0-N%E1%BA%B5ng-07-Nguy%E1%BB%85n-V%C4%83n-Tho%E1%BA%A1i-100068984088734/), [leminhSTORE fanpage](https://www.facebook.com/leminhstore.vn/)).

**Hai cách diễn giải — proposal nên nêu cả hai:**

1. **Thị trường phi chính thức thực sự mỏng** → cơ hội tốt cho startup chính thức hoá.
2. **Nội dung nhóm Facebook kín không được công cụ tìm kiếm index** → thị trường có thể tồn tại nhưng "vô hình" với nghiên cứu thứ cấp. **Đây là khả năng cao hơn.**

> **BẮT BUỘC làm trước khi nộp proposal:** Đăng nhập Facebook và tìm trực tiếp trong các nhóm sinh viên FPT Đà Nẵng (ví dụ các nhóm dạng "FPTU Đà Nẵng Confessions", "Chợ sinh viên FPT Đà Nẵng", "FPTU Da Nang K17/K18/K19"), tìm từ khoá **"thuê laptop"**, **"cho mượn laptop"**, **"mai thi mà máy hỏng"**. Chụp màn hình các bài đăng làm **bằng chứng nhu cầu (demand evidence)** — đây là loại dữ liệu thuyết phục nhất cho một proposal khởi nghiệp, mạnh hơn mọi số liệu thị trường vĩ mô.

### 8.2. Chợ đồ cũ — chỉ số gián tiếp về nguồn cung máy

| Chỉ số | Số liệu | Nguồn |
|---|---|---|
| Số tin đăng laptop cũ trên Chợ Tốt | **39.814 tin** (ghi nhận 09/08/2025); một trang khác ghi **hơn 34.570 tin** | [chotot.com/mua-ban-laptop](https://www.chotot.com/mua-ban-laptop) |

→ Nguồn cung máy cũ để startup mua vào làm đội máy cho thuê là **rất dồi dào**, không phải rào cản.

---

## 9. QUY MÔ THỊ TRƯỜNG & XU HƯỚNG "DEVICE AS A SERVICE"

### 9.1. Thị trường cho thuê thiết bị điện tử toàn cầu (nguồn quốc tế)

| Chỉ số | Số liệu | Nguồn |
|---|---|---|
| Consumer Electronics & Appliances Rental — quy mô | **73,71 tỷ USD (2024)** → **82,18 tỷ USD (2025)** | [The Business Research Company – Consumer Electronics and Appliances Rental Global Market Report](https://www.thebusinessresearchcompany.com/report/consumer-electronics-and-appliances-rental-global-market-report) |
| CAGR | **11,5%** (2024→2025); một nguồn khác dự báo **11,2% CAGR đến 2029** | nt; [openpr.com](https://www.openpr.com/news/4260950/consumer-electronics-and-appliances-rental-market-expected) |
| ⭐ **Đông Nam Á** | **CAGR vượt 13,2%** tại các thị trường **Việt Nam, Indonesia, Philippines** — được mô tả là "frontier tăng trưởng năng động nhất khu vực" | [dataintelo.com – Electronics Rental Platform Market Research Report](https://dataintelo.com/report/electronics-rental-platform-market) |
| Động lực tăng trưởng | Tầng lớp trung lưu đô thị hoá nhanh; tỷ lệ thâm nhập smartphone **vượt 78%** ở các nền kinh tế dẫn đầu; sự hiện diện của các nền tảng cho thuê được cấp vốn tốt | nt |
| Động lực chung | Điều kiện kinh tế & khả năng chi trả, thay đổi lối sống, đô thị hoá & tính di động, ý thức môi trường, **sự trỗi dậy của kinh tế chia sẻ** | [The Business Research Company](https://www.thebusinessresearchcompany.com/report/consumer-electronics-and-appliances-rental-global-market-report) |

> ⭐ Con số **CAGR >13,2% cho Việt Nam** là số liệu quốc tế tốt nhất, sát nhất với đề tài. **Nên dùng con số này trong proposal.**

### 9.2. Thị trường Device as a Service (DaaS) toàn cầu — ⚠️ CÁC NGUỒN MÂU THUẪN NẶNG

| Nguồn | Số liệu công bố |
|---|---|
| [The Business Research Company](https://www.thebusinessresearchcompany.com/report/device-as-a-service-global-market-report) | **199 tỷ USD (2025)** → **266,51 tỷ USD (2026)**, CAGR **33,9%**; đạt **866,03 tỷ USD (2030)**, CAGR 34,3% |
| [Precedence Research](https://www.precedenceresearch.com/device-as-a-service-market) | **273,53 tỷ USD (2026)** |
| Một nguồn khác | **254 tỷ USD (2026)** |
| Một nguồn khác | **163,89 tỷ USD (2025)** → **228,47 tỷ USD (2026)** |
| [Market Research Future](https://www.marketresearchfuture.com/reports/device-as-a-service-market-4486) | **150 tỷ USD vào 2026**, CAGR 22% |
| [Research Nester](https://www.researchnester.com/reports/device-as-a-service-daas-market/3703) | CAGR **39,4%** giai đoạn 2026–2034 |

> ⚠️ **CẢNH BÁO MẠNH:** Các con số này **chênh nhau tới hơn 5 lần cho cùng năm 2026** (từ 150 tỷ đến 273,53 tỷ USD) và CAGR dao động **22% – 39,4%**. Đây là dấu hiệu điển hình của các báo cáo thị trường thương mại định nghĩa phạm vi khác nhau (có/không tính dịch vụ đi kèm, phần cứng, phần mềm quản lý).
>
> **Khuyến nghị dùng trong proposal:** Nếu dùng, hãy **trích dẫn cả dải và nêu rõ nguồn mâu thuẫn** — ví dụ: *"Thị trường DaaS toàn cầu được các hãng nghiên cứu ước tính rất khác nhau, dao động 150–273 tỷ USD cho năm 2026 với CAGR 22–39%, cho thấy đây là một phân khúc đang định hình nhanh"*. **Tuyệt đối không trích một con số duy nhất như thể đó là sự thật đã xác lập.** Giảng viên hoàn toàn có thể vặn lại điểm này.
>
> **Quan trọng hơn:** DaaS toàn cầu là mô hình **B2B doanh nghiệp thuê trọn gói thiết bị + quản lý + bảo hành nhiều năm**. Nó **khác hẳn** mô hình cho thuê laptop theo buổi thi cho sinh viên. Dùng nó làm "bối cảnh xu hướng" thì được; **dùng nó để tính TAM cho startup này thì sai về bản chất**.

### 9.3. Bối cảnh thị trường Việt Nam (nguồn Việt Nam)

| Chỉ số | Số liệu | Nguồn |
|---|---|---|
| Thương mại điện tử VN 2024 | **Trên 25 tỷ USD**, tăng **20%** so với 2023, chiếm **~9%** tổng mức bán lẻ hàng hoá & doanh thu dịch vụ tiêu dùng | [moit.gov.vn – Thương mại điện tử Việt Nam năm 2024](https://moit.gov.vn/khoa-hoc-va-cong-nghe/thuong-mai-dien-tu-viet-nam-nam-2024-nhung-buoc-tien-va-thach-thuc.html) |
| Dự báo 2025 | **Vượt mốc 30 tỷ USD**, chiếm **~10%** tổng mức bán lẻ | nt |
| Tốc độ tăng trưởng TMĐT | **18–25%/năm** | nt |
| Ngành thiết bị điện tử VN (tháng 7/2024) | Doanh thu **2.071 tỷ đồng**, tăng **20,14%** so với cùng kỳ | [Metric Insights – Ngành hàng thiết bị điện tử: Xu hướng mới và cơ hội trong tháng 7/2024](https://metric.vn/insights/nganh-hang-thiet-bi-dien-tu-xu-huong-moi-va-co-hoi-trong-thang-7-2024/) |
| Thị trường thuê xe/xe đạp chia sẻ VN | **~1,2 tỷ USD** — dùng làm tham chiếu cho thấy mô hình "thuê thay vì mua" đã được người Việt chấp nhận | [Ken Research – Vietnam Shared Mobility and Bike Rentals Market](https://www.kenresearch.com/vietnam-shared-mobility-and-bike-rentals-market) |
| Recommerce VN 2025 | Tăng trưởng **13,7%** trong 2025, dẫn dắt bởi nền tảng C2C và B2C | [ResearchAndMarkets via Businesswire – Vietnam Recommerce Market Intelligence Databook 2025](https://www.businesswire.com/news/home/20250701589204/en/Vietnam-Recommerce-Market-Intelligence-Databook-2025-13.7-Growth-in-2025-Led-by-C2C-and-B2C-Platforms---ResearchAndMarkets.com) |

> ❌ **KHÔNG tìm được số liệu riêng cho "thị trường cho thuê laptop tại Việt Nam"** (giá trị VND, số lượng máy, số doanh nghiệp). Sau nhiều truy vấn khác nhau, không có báo cáo nào công bố con số này. **Đây là giới hạn thật của nghiên cứu, không được bịa ra.**
>
> **Cách xử lý trong proposal:** Dùng phương pháp **bottom-up** thay vì top-down. Ví dụ: *(số sinh viên FPTU Đà Nẵng) × (% ước tính gặp sự cố máy trong kỳ thi) × (số kỳ thi/năm) × (giá thuê/buổi)*. Phương pháp bottom-up với giả định minh bạch thường được đánh giá cao hơn việc trích một con số thị trường vĩ mô không liên quan.

### 9.4. Chi phí đầu tư máy (tham khảo cho bài toán vốn)

| Loại máy | Giá tham khảo | Nguồn |
|---|---|---|
| Dell cũ, i5 Gen 8, RAM 8GB, SSD 256GB | **Dưới 5 triệu đồng** (2025) | [laptopnhatlinh.vn – Top 5 laptop Dell cũ dưới 5 triệu 2025](https://laptopnhatlinh.vn/top-5-laptop-dell-cu-duoi-5-trieu-dang-mua-nhat-2025-laptop-nhat-linh/) |
| Dell Latitude 5590, i7 Gen 8, RAM 8GB, SSD 256GB | **5,9 triệu đồng** | nt |
| Dell Latitude 3500, i5-8250U, RAM 8GB, SSD 256GB, 15.6" | Có bán tại Đà Nẵng | [truonggiang.vn/laptop-cu-dell-3500-i5-8250](https://truonggiang.vn/laptop-cu-dell-3500-i5-8250) |
| Laptop mới cho sinh viên | HP 14s-em0086AU (Ryzen 5 7520U, 16GB) **hơn 12 triệu đồng**; tầm 15–25 triệu có 16GB + 512GB | [daihoc.fpt.edu.vn – Gợi ý cấu hình laptop cho tân sinh viên ĐH FPT](https://daihoc.fpt.edu.vn/goi-y-cau-hinh-laptop-cho-tan-sinh-vien-dai-hoc-fpt/) |
| Nguồn cung máy cũ | 39.814 tin laptop cũ trên Chợ Tốt | [chotot.com](https://www.chotot.com/mua-ban-laptop) |

**Phép tính sơ bộ về khả năng hoàn vốn (dùng số có nguồn, giả định do nhóm đặt ra — phải ghi rõ là giả định):**

- Chi phí 1 máy cũ i5 Gen 8 / 8GB / 256GB: **~5.000.000đ** (nguồn: dưới 5 triệu)
- Giá thuê mặt bằng Đà Nẵng cho i5: **80.000đ/máy/ngày** (nguồn: thuelaptop.com.vn)
- Nếu định giá theo buổi thi ở mức **~50.000đ/buổi** (giả định nhóm đặt, thấp hơn giá ngày để hấp dẫn):
  - Số lượt thuê để hoàn vốn 1 máy: **5.000.000 ÷ 50.000 = 100 lượt**
- ⚠️ **Đây là phép tính đơn giản hoá, CHƯA tính**: khấu hao, hỏng hóc, chi phí vận hành, chi phí giao nhận, thuế, chi phí website. Phải nêu rõ trong proposal là **ước tính sơ bộ**.

---

## 10. KHOẢNG TRỐNG THỊ TRƯỜNG — CƠ HỘI CHO DỊCH VỤ CHUYÊN CHO THUÊ LAPTOP ĐI THI

Đây là phần kết luận chính, tổng hợp từ toàn bộ dữ liệu trên.

### Bảng 7 — Ma trận khoảng trống: thị trường hiện tại KHÔNG phục vụ điều gì

| # | Chiều cạnh | Thị trường hiện tại | Nhu cầu "đi thi" | Mức độ trống | Bằng chứng |
|---|---|---|---|---|---|
| **1** | **Đơn vị thời gian** | Ngắn nhất là **1 NGÀY**. **Không tồn tại gói theo GIỜ/BUỔI** trên toàn thị trường VN | Cần **3–4 giờ**, đúng 1 ca thi | 🔴 **TRỐNG HOÀN TOÀN** | Tìm kiếm "thuê laptop theo giờ" → 100% kết quả là ngày/tuần/tháng/năm |
| **2** | **Cấu trúc giá** | Thưởng thuê dài, phạt thuê ngắn (1 tháng chỉ = **41%** đơn giá/ngày của gói 1 ngày) | Thuê cực ngắn, tần suất 1–2 lần/kỳ | 🔴 **TRỐNG** | Bảng 3: 49.000đ/ngày vs 600.000đ/tháng |
| **3** | **Tốc độ (SLA)** | Nhanh nhất toàn quốc: **2 giờ** (chỉ TP.HCM). **Đà Nẵng: "trong ngày"** | Cần **≤ 20–30 phút**, tính bằng phút | 🔴 **TRỐNG** | Bảng 6 |
| **4** | **Vị trí địa lý** | Cụm cho thuê tập trung ở **Liên Chiểu** (Làng ĐH ĐN), Hải Châu, Sơn Trà, Cẩm Lệ. **Không có đơn vị nào xác nhận cho thuê tại Ngũ Hành Sơn/Hoà Hải** | Cần ngay trong khuôn viên/bán kính 1–2 km campus FPT | 🔴 **TRỐNG** | Mục 2.1 |
| **5** | **Rào cản đặt cọc** | Đà Nẵng: cọc **bằng giá trị máy**; nơi thân thiện nhất vẫn **500k–2 triệu** | Sinh viên 6h30 sáng **không có 2 triệu tiền mặt** | 🟠 **TRỐNG MỘT PHẦN** (đã có mô hình không cọc nhưng chưa ai áp dụng cho sinh viên tại ĐN) | Bảng 5 |
| **6** | **Sẵn sàng kỹ thuật cho kỳ thi** | Máy giao "có Windows và phần mềm cơ bản". **KHÔNG đơn vị nào cài sẵn EOS + SEB, không ai test trước, không ai kèm tai nghe có dây** | Bắt buộc Windows + SEB đúng bản + EOS đúng thư mục + đã test + tai nghe có dây | 🔴 **TRỐNG HOÀN TOÀN — RÀO CẢN CAO NHẤT** | Mục 1.1, 1.2 |
| **7** | **Quy trình đặt** | 5 bước: gọi → tư vấn → báo giá → hợp đồng → giao & lắp đặt (mất vài giờ đến 1 ngày) | Cần đặt online **trong 2 phút**, không gọi điện | 🔴 **TRỐNG** | Mục 5.1, 5.2 |
| **8** | **Khách lẻ 1 máy** | Nhiều đơn vị **chỉ miễn phí giao từ 5 máy**; định vị chủ đạo là **B2B/sự kiện/đào tạo** | Luôn là **1 máy, 1 người** | 🟠 **TRỐNG MỘT PHẦN** | Sky Computer (≥5 máy mới free ship); SEA Event, Danang Events, Xoo Event đều định vị sự kiện |
| **9** | **Cơ chế tín chấp** | Chỉ có 3 cơ chế: bảo lãnh nhà trường, giấy tờ linh hoạt, thuê ngắn <1 tháng. **Chưa ai khai thác danh tính sinh viên FPT** | Sinh viên có MSSV, thẻ SV, tài khoản FAP/LMS — tài sản tín chấp mạnh | 🟠 **CƠ HỘI ĐỘC QUYỀN** cho startup nội bộ campus | Mục 5.3 |

### 10.1. Đối thủ gần nhất về mặt khái niệm

| Đối thủ | Mức độ trùng lặp | Vì sao KHÔNG phải đối thủ trực tiếp |
|---|---|---|
| **Phương Nam Tech** — có hẳn trang ["Cho thuê laptop thi cử"](https://phuongnamco.com/cho-thue-laptop-thi-cu-giai-phap-huu-ich-cho-sinh-vien-mua-thi/) | Cao nhất về **thông điệp marketing** | Ở **TP.HCM**, không có mặt ở Đà Nẵng. Và "thi cử" ở đây nghĩa là **thuê theo tuần/tháng/trọn mùa thi** để ôn tập và làm bài online — **không phải thuê theo buổi thi**. Nguyên văn: "thuê theo tuần, theo tháng hay trọn mùa thi đều được" |
| **leminhSTORE** (Đà Nẵng) | Cao nhất về **tệp khách hàng** (chuyên sinh viên, 38K/ngày, giảm giá nhóm) | Ở **Sơn Trà**, cách campus FPT rất xa. Vẫn thu **cọc 500k–2 triệu**. Vẫn bán theo **ngày**, không theo buổi. Không cài EOS/SEB |
| **SEA Event** (Đà Nẵng) | Cao về **kinh nghiệm phục vụ trường ĐH** (>100 máy cho ĐH Bách Khoa ĐN) | Mô hình **B2B số lượng lớn**, ký hợp đồng với nhà trường. Không phục vụ **sinh viên lẻ** |
| **Trường Giang** (Đà Nẵng) | Cao về **độ phủ + giao trong ngày** | "Trong ngày" quá chậm cho ca thi sáng. Ở 118 Hàm Nghi, rất xa Hoà Hải. Định vị sự kiện/hội nghị/thi tuyển công chức, không phải sinh viên lẻ |

→ **Không có đối thủ trực tiếp.** Startup sẽ ở vị trí **người đầu tiên (first mover)** trong ngách "thuê laptop theo buổi thi tại campus FPT Đà Nẵng".

### 10.2. Định vị đề xuất

> **"Không cho thuê laptop. Cho thuê một ca thi an toàn."**
> (*Not renting a laptop — renting a guaranteed exam slot.*)

**Sản phẩm lõi — "Máy sẵn sàng thi" (Exam-Ready Machine):**

| Thành phần | Chi tiết | Vì sao quan trọng |
|---|---|---|
| Máy Windows thật | Không dùng Mac; máy đã cài Windows bản quyền, hoạt động ổn định | EOS **bắt buộc Windows**; Mac M1/M2 không thi được |
| SEB cài sẵn | `SEB_3.10.0.794_AutoSettings.msi` (hoặc bản mới nhất) tải từ `exam.fpt.edu.vn` | Tránh sinh viên phải tải/cài lúc 7h sáng |
| EOS Client cài sẵn đúng thư mục | Không copy file ra ngoài thư mục gốc | Nhà trường cảnh báo copy ra ngoài → **không khởi động được** |
| Đã test trước | Mỗi máy chạy thử EOS/SEB trước khi đưa vào kho cho thuê | Nhà trường khuyến cáo test trước ngày thi |
| Tai nghe có dây kèm theo | Miễn phí kèm mỗi lượt thuê | Bắt buộc cho môn thi nghe |
| Sạc + chuột | Kèm theo | Tình huống "hết pin" là một trong các nguyên nhân gốc |
| Pin đã kiểm tra | Cam kết pin trụ được trọn ca thi | Phòng thi có thể thiếu ổ cắm |

**Bốn cam kết SLA đề xuất (điểm khác biệt bán hàng):**

1. **Giao trong ≤ 15–20 phút** trong khuôn viên campus (so với chuẩn tốt nhất Đà Nẵng là "trong ngày")
2. **Đặt online ≤ 2 phút**, không cần gọi điện, không cần chờ báo giá
3. **Không cọc tiền mặt** — dùng thẻ sinh viên + MSSV + xác thực qua email trường làm tín chấp
4. **Cam kết máy thi được**: nếu máy không chạy được EOS/SEB → **hoàn 100% + đền bù**

**Cấu trúc giá đề xuất (cần nhóm tự quyết, đây là gợi ý dựa trên dữ liệu):**

| Gói | Thời lượng | Neo giá thị trường | Ghi chú |
|---|---|---|---|
| Gói "1 ca thi" | 3–4 giờ | Thị trường chưa có → tự định giá | Nên đặt **thấp hơn rõ rệt giá 1 ngày** (80.000đ/ngày ở ĐN) để hấp dẫn, nhưng **cao hơn tỷ lệ giờ** để có biên |
| Gói "trọn ngày thi" | 1 ngày | **80.000đ (i5) / 100.000đ (i7)** — mặt bằng ĐN | Cạnh tranh trực tiếp |
| Gói "trọn tuần thi" | 5–7 ngày | **450.000đ (i5) / 600.000đ (i7)** — mặt bằng ĐN | Cho sinh viên thi nhiều môn |
| Gói "trọn kỳ" | 1 tháng | **800.000đ (i5) / 1.000.000đ (i7)** — mặt bằng ĐN | Cho sinh viên máy hỏng chờ sửa |

**Kênh tiếp cận khách hàng:**
- Nhóm Facebook sinh viên FPT Đà Nẵng (cần khảo sát trực tiếp — xem mục 8.1)
- Đặt điểm trực tại sảnh toà **Alpha / Gamma** vào **mùa thi**
- Phối hợp Phòng CTSV để được công nhận (mở đường cho mô hình "bảo lãnh nhà trường" như SAOLA)

### 10.3. Rủi ro chính cần nêu trong proposal

| Rủi ro | Mức độ | Giảm thiểu |
|---|---|---|
| **Tính mùa vụ cực cao** | 🔴 Cao | Nhu cầu dồn vào tuần thi, còn lại gần như bằng 0 → máy nằm không. **Giảm thiểu:** kết hợp gói thuê tháng cho sinh viên máy hỏng; cho thuê phục vụ sự kiện/workshop ngoài mùa thi |
| **Rào cản gia nhập thấp** | 🟠 Trung bình | Bất kỳ ai cũng có thể mua 5 máy cũ và làm theo. **Giảm thiểu:** xây lợi thế ở **quan hệ với nhà trường**, thương hiệu trong cộng đồng SV, và quy trình kỹ thuật EOS/SEB đã chuẩn hoá |
| **Rủi ro mất/hỏng máy** | 🟠 Trung bình | Không cọc tiền → tăng rủi ro. **Giảm thiểu:** hợp đồng điện tử có điều khoản bồi thường rõ (căn cứ BLDS 2015 Đ.554, 557); ràng buộc bằng MSSV; giới hạn phạm vi giao trong campus |
| **Quy chế thi của nhà trường** | 🔴 **Cao — cần kiểm tra gấp** | **CHƯA xác minh được** nhà trường có **cho phép** sinh viên dùng máy đi mượn/thuê vào phòng thi hay không, và có yêu cầu khai báo máy không. **Phải hỏi Phòng Khảo thí trước khi hoàn thiện proposal** |
| **Bảo mật/gian lận** | 🟠 Trung bình | Máy dùng chung có thể bị nghi ngờ cài phần mềm gian lận. **Giảm thiểu:** wipe + cài lại image chuẩn sau mỗi lượt thuê; minh bạch quy trình với nhà trường |

---

## 11. NHỮNG ĐIỀU CHƯA XÁC MINH ĐƯỢC

Liệt kê trung thực, **không suy đoán**:

1. ❌ **Toàn bộ dữ liệu chưa được xác minh bằng cách mở trực tiếp trang web** — WebFetch/curl bị proxy chặn hoàn toàn (403). Mọi số liệu đến từ snippet/tóm tắt của công cụ tìm kiếm.
2. ❌ **Số lượng sinh viên Đại học FPT Đà Nẵng (2024–2026)** — không có số liệu công khai. (Con số "10.000 SV" tìm được là của **campus TP.HCM**, không dùng được.)
3. ❌ **Quy mô thị trường cho thuê laptop tại Việt Nam** (giá trị VND, số doanh nghiệp, số máy) — không có báo cáo nào công bố.
4. ❌ **Quy mô thị trường cho thuê laptop tại Đà Nẵng** — không có.
5. ❌ **Điều khoản bồi thường định lượng** của từng đơn vị (đền bao nhiêu khi vỡ màn hình / mất máy) — nằm trong hợp đồng giấy tại quầy, không đăng web.
6. ❌ **Bảng giá đầy đủ từng model** của các đơn vị Đà Nẵng (Trường Giang, leminhSTORE, Đình Hậu, Sky Computer) — chỉ lấy được giá "từ X đồng" và vài mốc tổng hợp.
7. ❌ **Hotline/địa chỉ đầy đủ** của: DH Lend, Danang Events, Tin Học Gia Tín, Xoo Event, chothuelaptop.com.vn, thuelaptop.vn.
8. ❌ **Nhóm Facebook/chợ sinh viên cho thuê laptop tại Đà Nẵng** — không tìm thấy qua công cụ tìm kiếm web; cần khảo sát trực tiếp trên Facebook.
9. ❌ **Kim Anh Computer (248 Ngũ Hành Sơn) có cho thuê laptop hay không** — chỉ xác nhận sửa chữa/bán/thu cũ đổi mới. Đây là đơn vị gần campus FPT nhất nên **cần gọi hỏi: 0815 126 126**.
10. ❌ **Quy chế thi FPTU về việc dùng máy mượn/thuê** — chưa xác minh nhà trường có cho phép không. **Rủi ro pháp lý/vận hành lớn nhất của ý tưởng.**
11. ⚠️ **Con số "10k/ngày"** của thuelaptop.vn và **"29.000đ/ngày"** của MiT Group — nghi là giá quảng cáo dẫn dụ (loss leader) hoặc giá quy đổi từ thuê dài hạn/số lượng lớn. **Cần xác minh.**
12. ⚠️ **Địa chỉ SEA Event** — hai nguồn ghi khác nhau: *57 Nguyễn Xuân Nhĩ, Hải Châu* và *217 Trần Phú, P. Phước Ninh, Hải Châu*. Cần xác minh.
13. ⚠️ **Số liệu DaaS toàn cầu mâu thuẫn nặng** giữa các hãng nghiên cứu (150–273 tỷ USD cho cùng năm 2026) — xem cảnh báo tại mục 9.2.
14. ❌ **Số liệu về tỷ lệ sinh viên gặp sự cố laptop trong kỳ thi** — không có nghiên cứu nào. **Bắt buộc phải tự khảo sát** (Google Form gửi sinh viên FPTU ĐN) để có con số cho proposal.

---

## 12. DANH SÁCH NGUỒN

### 12.1. Nguồn về Đại học FPT (bối cảnh & yêu cầu kỹ thuật thi)

| # | Tiêu đề | URL |
|---|---|---|
| 1 | Hướng dẫn sinh viên sử dụng và thi trên phần mềm EOS tại Trường Đại học FPT | https://daihoc.fpt.edu.vn/tin-noi-bat-muc-tin-tuc/huong-dan-sinh-vien-su-dung-va-thi-tren-phan-mem-eos-tai-truong-dai-hoc-fpt/ |
| 2 | Hướng dẫn sinh viên sử dụng và thi trên phần mềm EOS (FPTU Hà Nội) | https://hanoi.fpt.edu.vn/tin-tuc-su-kien/huong-dan-sinh-vien-su-dung-va-thi-tren-phan-mem-eos.html |
| 3 | Hướng dẫn cài đặt phần mềm thi EOS và SEB — Helpdesk of FPT University | https://it.fpt.edu.vn/cantho/huong-dan-cai-dat-phan-mem-thi-eos-seb/ |
| 4 | Cài đặt Windows trên MAC bằng Bootcamp — Helpdesk of FPT University | https://it.fpt.edu.vn/cantho/huong-dan-cai-windows-tren-mac-dung-bootcamp/ |
| 5 | Hướng dẫn cài đặt Safe Exam Browser trên HĐH Windows — FPTU Quy Nhơn | https://lmsqn.fpt.edu.vn/hd/huong-dan-cai-dat-seb-tren-windows/ |
| 6 | Hướng dẫn cài đặt phần mềm thi EOS — FPTU Quy Nhơn | https://lmsqn.fpt.edu.vn/hd/video-huong-dan-cai-dat-va-su-dung-phan-mem-thi-eos-tren-windows/ |
| 7 | Hướng dẫn cài đặt SEB cho Edunext trên Windows — IT HCM FPT | https://it-hcm.fpt.edu.vn/articles.php?news=huong-dan-cai-dat-seb-cho-edunext-tren-windows-&id=22 |
| 8 | Hướng dẫn cài đặt SEB cho LMS trên Windows — IT HCM FPT | https://it-hcm.fpt.edu.vn/articles.php?news=huong-dan-cai-dat-seb-cho-lms-tren-windows&id=36 |
| 9 | Campus Đà Nẵng — Trường Đại học FPT | https://daihoc.fpt.edu.vn/da-nang/ |
| 10 | Gợi ý cấu hình laptop cho tân sinh viên Đại học FPT | https://daihoc.fpt.edu.vn/goi-y-cau-hinh-laptop-cho-tan-sinh-vien-dai-hoc-fpt/ |
| 11 | Trang tin hoạt động Ban Đào tạo — FPTU Da Nang | https://fptudn.info.vn/ |

### 12.2. Nhà cung cấp tại Đà Nẵng

| # | Đơn vị | URL |
|---|---|---|
| 12 | Trường Giang Computer — Cho thuê laptop Đà Nẵng từ 50K | https://truonggiang.vn/cho-thue-laptop.html |
| 13 | Trường Giang — Laptop cũ Dell 3500 i5 8250 | https://truonggiang.vn/laptop-cu-dell-3500-i5-8250 |
| 14 | leminhSTORE — Cho thuê laptop sinh viên giá rẻ Đà Nẵng | https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html |
| 15 | leminhSTORE — Thuê PC Gaming/Workstation Đà Nẵng | https://leminhstore.vn/thue-pc-gaming-da-nang-104910u.html |
| 16 | leminhSTORE — Sửa máy tính PC laptop khu vực Ngũ Hành Sơn | https://leminhstore.vn/sua-may-tinh-pc-laptop-khu-vuc-ngu-hanh-son-tp-da-nang-83299u.html |
| 17 | Đình Hậu Computer — Dịch vụ cho thuê laptop tại Đà Nẵng | https://maytinhdinhhau.vn/dich-vu-cho-thue-laptop-tai-da-nang/ |
| 18 | Đình Hậu Computer — Địa chỉ cho sinh viên thuê laptop giá rẻ tại Đà Nẵng | https://maytinhdinhhau.vn/dia-chi-cho-sinh-vien-thue-laptop-gia-re-tai-da-nang/ |
| 19 | Sky Computer — Dịch vụ cho thuê máy tính laptop tại Đà Nẵng | https://skycomputer.vn/dich-vu/cho-thue-may-tinh-laptop-tai-da-nang/ |
| 20 | Chothuelaptop.com.vn — Dịch vụ cho thuê laptop Đà Nẵng | https://chothuelaptop.com.vn/thue-laptop-da-nang/ |
| 21 | Chothuelaptop.com.vn — Thuê laptop theo tháng | https://chothuelaptop.com.vn/thue-laptop-theo-thang/ |
| 22 | SEA Event — Cho thuê laptop Đà Nẵng số lượng lớn phục vụ Event | https://seaevent.vn/cho-thue-laptop-su-kien-tai-da-nang/ |
| 23 | SEA Event — Cho thuê hơn 100 laptop phục vụ đào tạo tại ĐH Bách Khoa Đà Nẵng | https://seaevent.vn/cho-thue-laptop-phuc-vu-dao-tao-tai-truong-dai-hoc-bach-khoa-da-nang/ |
| 24 | Thuelaptop.com.vn (Phương Châu) — Trang chủ | https://thuelaptop.com.vn/ |
| 25 | Thuelaptop.com.vn — Địa điểm cho thuê laptop tại Đà Nẵng giá rẻ | https://thuelaptop.com.vn/dia-diem-cho-thue-laptop-tai-da-nang-gia-re.html |
| 26 | Thuelaptop.vn — Cho thuê laptop Đà Nẵng Gen 10 từ 10k/ngày | https://www.thuelaptop.vn/thue-laptop-da-nang-gia-re-chi-tu-10k/ |
| 27 | Thuelaptop.vn — Chính sách kinh doanh cho thuê thiết bị | https://www.thuelaptop.vn/gioi-thieu/chinh-sach-kinh-doanh-cho-thue-thiet-bi/ |
| 28 | Xoo Event — Cho thuê laptop, máy tính số lượng lớn tại Đà Nẵng | https://xooevent.com/cho-thue-laptop-may-tinh-so-luong-lon-tai-da-nang/ |
| 29 | Kim Anh Computer — Linh kiện laptop | https://www.kimanh.com.vn/linh-kien-laptop/ |
| 30 | Chothuelaptop.info — Cho thuê laptop Đà Nẵng thủ tục nhanh gọn | https://chothuelaptop.info/cho-thue-laptop-da-nang-thu-tuc-nhanh-gon/ |
| 31 | Laptopchothue.com — Dịch vụ cho thuê laptop tại Đà Nẵng | https://laptopchothue.com/dich-vu-cho-thue-laptop-tai-da-nang-laptop-cau-hinh-cao-gia-tot/ |

### 12.3. Danh sách tổng hợp / toplist Đà Nẵng

| # | Tiêu đề | URL |
|---|---|---|
| 32 | Top 7 dịch vụ cho thuê laptop Đà Nẵng uy tín, giá rẻ | https://danang.plus/thue-laptop/ |
| 33 | Top 15+ công ty cho thuê laptop Đà Nẵng uy tín giá rẻ | https://top10danang.com/top-10-cong-ty-cho-thue-laptop-da-nang-uy-tin-gia-re/ |
| 34 | TOP 10+ địa chỉ thuê máy tính bàn Đà Nẵng uy tín, giá rẻ | https://top10danang.com/mach-ban-10-dia-chi-thue-may-tinh-ban-da-nang-uy-tin-gia-re/ |
| 35 | Đừng bỏ lỡ Top 7 dịch vụ cho thuê laptop Đà Nẵng uy tín nhất | https://toplistdanang.com/cong-nghe/thue-laptop-da-nang/ |
| 36 | Top 7 địa chỉ cho thuê laptop tại Đà Nẵng giá rẻ chất lượng | https://reviewnao.net/cho-thue-laptop-tai-da-nang/ |
| 37 | Mách bạn Top 7 địa điểm cho thuê laptop Đà Nẵng uy tín | https://danangaz.com/cong-nghe/cho-thue-laptop-da-nang/ |
| 38 | Những dịch vụ cho thuê laptop giá rẻ uy tín tại Đà Nẵng | https://top10danang.vn/cho-thue-laptop-gia-re/ |
| 39 | Top 10 nơi thuê laptop màn hình máy tính tại Đà Nẵng rẻ | https://nhomkinhtaidanang.com/noi-thue-laptop-man-hinh-may-tinh-tai-da-nang/ |

### 12.4. Nhà cung cấp toàn quốc (đối chuẩn giá & mô hình)

| # | Đơn vị / Tiêu đề | URL |
|---|---|---|
| 40 | ICT Sài Gòn — Cho thuê laptop setup tận nơi từ 49.000đ/ngày | https://ictsaigon.com.vn/cho-thue-laptop |
| 41 | ICT Sài Gòn — Cho thuê laptop HP Elitebook 9480m 49k/ngày | https://ictsaigon.com.vn/cho-thue-laptop-hp-elitebook-9480m |
| 42 | ICT Sài Gòn — Cho thuê laptop gaming | https://ictsaigon.com.vn/thue-laptop-gaming |
| 43 | ICT Sài Gòn — Thủ tục thuê laptop không cọc | https://ictsaigon.com.vn/thue-laptop-khong-coc |
| 44 | ICT Sài Gòn — Cho thuê PC, máy tính để bàn từ 99K/ngày | https://ictsaigon.com.vn/cho-thue-pc-may-tinh-de-ban |
| 45 | ICT Sài Gòn — Kinh nghiệm thuê laptop | https://ictsaigon.com.vn/kinh-nghiem-thue-laptop-uy-tin-dam-bao |
| 46 | Laptop SGN — Cho thuê laptop uy tín, bảng giá thuê chi tiết | https://laptopsgn.com/cho-thue-laptop/ |
| 47 | Laptop SGN — Dịch vụ cho thuê laptop TPHCM giao nhanh 2h | https://laptopsgn.com/tin-tuc/dich-vu-cho-thue-laptop-tphcm-gia-re-giao-2h/ |
| 48 | Laptop SGN — Dịch vụ cho thuê laptop sinh viên giá rẻ | https://laptopsgn.com/tin-tuc/thue-laptop-sinh-vien/ |
| 49 | Laptop SGN — Cho thuê laptop theo ngày giá rẻ TPHCM | https://laptopsgn.com/tin-tuc/cho-thue-laptop-theo-ngay-gia-re-tphcm/ |
| 50 | MiT Group — Cho thuê laptop 2025 từ 29.000đ | https://mitgroup.vn/cho-thue-laptop/ |
| 51 | MiT Group — Thuê laptop không cọc | https://mitgroup.vn/thue-laptop-khong-coc/ |
| 52 | MiT Group — Thuê laptop sinh viên giá rẻ | https://mitgroup.vn/thue-laptop-sinh-vien/ |
| 53 | SKYLAP — Cho thuê laptop giá rẻ, cấu hình nhiều tùy chọn | https://skylap.vn/dich-vu-cho-thue/cho-thue-laptop/ |
| 54 | SKYLAP — Thuê Laptop Dell Precision Core i7-7700HQ | https://skylap.vn/thue-laptop-dell-precision-core-i7-7700hq/ |
| 55 | SKYLAP — Cho thuê Laptop Dell văn phòng | https://skylap.vn/dich-vu-cho-thue/cho-thue-laptop-dell-van-phong/ |
| 56 | Tin học PNN — Bảng giá cho thuê laptop máy tính giá rẻ TP HCM | https://tinhocpnn.com/bang-gia-cho-thue-laptop-may-tinh-gia-re/ |
| 57 | SAOLA — Bảng giá thuê Laptop, PC, All in one, Mini PC | https://saolatech.com.vn/bang-gia-thue-3425667 |
| 58 | SAOLA — Thuê laptop không cần đặt cọc tại Hà Nội (giải pháp cho sinh viên) | https://saolatech.com.vn/thue-laptop-khong-can-dat-coc-tai-ha-noi-giai-phap-tiet-kiem-cho-sinh-vien-3425752 |
| 59 | SAOLA — Thuê laptop cho sinh viên | https://saolatech.com.vn/thue-laptop-cho-sinh-vien-giai-phap-tien-loi-tiet-kiem-va-hien-dai-3425768 |
| 60 | SAOLA — Dịch vụ cho thuê máy tính laptop toàn quốc: Hà Nội, TP.HCM, Đà Nẵng | https://saolatech.com.vn/saola-dich-vu-cho-thue-may-tinh-laptop-uy-tin-toan-quoc-ha-noi-tp-hcm-da-nang-3425773 |
| 61 | VIETBIS — Thuê laptop không cần đặt cọc tại Hà Nội: Điều kiện áp dụng | https://vietbis.vn/tin-tuc/thue-laptop-khong-can-dat-coc-tai-ha-noi-dieu-kien-ap-dung-3116.html |
| 62 | VIETBIS — Dịch vụ cho thuê Laptop, PC tại Hà Nội | https://vietbis.vn/tin-tuc/dich-vu-cho-thue-laptop-tai-ha-noi---vietbisvn-2530.html |
| 63 | ⭐ Phương Nam Tech — Cho thuê laptop thi cử (đối thủ khái niệm gần nhất) | https://phuongnamco.com/cho-thue-laptop-thi-cu-giai-phap-huu-ich-cho-sinh-vien-mua-thi/ |
| 64 | Phương Nam Tech — Bảng giá cho thuê laptop | https://phuongnamco.com/bang-gia-cho-thue-laptop-giai-phap-tiet-kiem-cho-ca-nhan-doanh-nghiep/ |
| 65 | Phương Nam Tech — Cho thuê laptop theo tháng | https://phuongnamco.com/cho-thue-laptop-theo-thang-tiet-kiem-linh-hoat-cho-ca-nhan-va-doanh-nghiep/ |
| 66 | Thuelaptop.com.vn — Bảng giá cho thuê laptop văn phòng | https://thuelaptop.com.vn/bang-gia-cho-thue-laptop-van-phong.html |
| 67 | Thuelaptop.com.vn — Bảng giá cho thuê laptop đồ họa theo ngày/tuần/tháng/năm | https://thuelaptop.com.vn/bang-gia-cho-thue-laptop-do-hoa.html |
| 68 | Thuelaptop.com.vn — Dịch vụ cho thuê laptop Gaming, không đặt cọc | https://thuelaptop.com.vn/dich-vu-cho-thue-laptop-gaming.html |
| 69 | Thuelaptop.com.vn — Cho sinh viên thuê máy tính không cần đặt cọc | https://thuelaptop.com.vn/cho-sinh-vien-thue-may-tinh-khong-can-dat-coc.html |
| 70 | Bách Khoa 4 — Dịch vụ cho thuê laptop theo ngày tại Hà Nội | https://bk4.com.vn/dich-vu-cho-thue-laptop-theo-ngay-tai-ha-noi/ |
| 71 | Vi Tính Thiên Ân — Cho thuê laptop giá rẻ 50k tại TP.HCM | https://laptopthienan.com/cho-thue-laptop-may-tinh-hcm-gia-re-50k.html |
| 72 | Chothuemaytinh.vn — Cho thuê laptop, máy tính cho sinh viên | https://chothuemaytinh.vn/cho-thue-laptop-sinh-vien/ |
| 73 | Quảng Tin — Cho thuê laptop, PC giá rẻ TP.HCM, giao nhanh 24/7 | https://quangtin.com/pages/cho-thue-may-tinh-laptop-gia-re-tai-tp-hcm-dich-vu-chuyen-nghiep |
| 74 | Laptopchothue.com — Cho thuê laptop số lượng lớn phục vụ đào tạo, sự kiện | https://laptopchothue.com/ |
| 75 | Thietbichothue.com — Cho thuê laptop theo ngày, tháng | https://thietbichothue.com/cho-thue-laptop/ |
| 76 | Chinhnhan.vn — Cho thuê laptop theo ngày | https://chinhnhan.vn/cho-thue-laptop |
| 77 | ALi Việt (wifisukien.com) — Cho thuê laptop theo ngày, theo tháng cho sự kiện | https://wifisukien.com/cho-thue-laptop/ |
| 78 | Chothuelaptop.org — Cho thuê laptop tại TP.HCM | https://chothuelaptop.org/cho-thue-laptop/ |
| 79 | Suachualaptop24h — Dịch vụ cho thuê laptop tại Hà Nội | https://suachualaptop24h.com/ct-dich-vu-cho-thue-laptop-tai-ha-noi.html |

### 12.5. Pháp lý — bồi thường hợp đồng thuê tài sản

| # | Tiêu đề | URL |
|---|---|---|
| 80 | Thuê thiết bị làm hỏng: Bên thuê có phải bồi thường? (BLDS 2015 Đ.554, 557) | https://congchung247.com.vn/thue-thiet-bi-lam-hong-ben-thue-co-phai-boi-thuong/ |
| 81 | Quy định về bồi thường thiệt hại trong hợp đồng thuê tài sản | https://vanphongcongchung.info/quy-dinh-ve-boi-thuong-thiet-hai-trong-hop-dong-thue-tai-san/ |
| 82 | Làm mất laptop nhưng không chịu trả tiền đền bù xử lý thế nào? — Luật Minh Khuê | https://luatminhkhue.vn/lam-mat-laptop-nhung-khong-chiu-tra-tien-den-bu-.aspx |
| 83 | Đền bù thiệt hại khi làm mất tài sản gửi giữ — Luật Dương Gia | https://luatduonggia.vn/phap-luat/den-bu-thiet-hai-khi-lam-mat-tai-san-gui-giu/ |
| 84 | Nhân viên làm hỏng máy tính của công ty thì bồi thường như thế nào? — Thư viện Pháp luật | https://thuvienphapluat.vn/hoi-dap-phap-luat/nhan-vien-lam-hong-may-tinh-cua-cong-ty-thi-boi-thuong-nhu-the-nao-284337.html |

### 12.6. Thị trường & xu hướng

| # | Tiêu đề | URL |
|---|---|---|
| 85 | Consumer Electronics And Appliances Rental Global Market Report — The Business Research Company | https://www.thebusinessresearchcompany.com/report/consumer-electronics-and-appliances-rental-global-market-report |
| 86 | Consumer Electronics And Appliances Rental Market — Research and Markets | https://www.researchandmarkets.com/reports/5807053/consumer-electronics-appliances-rental-global |
| 87 | Consumer Electronics And Appliances Rental Market 11.2% CAGR by 2029 — OpenPR | https://www.openpr.com/news/4260950/consumer-electronics-and-appliances-rental-market-expected |
| 88 | ⭐ Electronics Rental Platform Market Research Report (CAGR >13,2% cho VN/Indonesia/Philippines) — Dataintelo | https://dataintelo.com/report/electronics-rental-platform-market |
| 89 | Device-As-A-Service Market Size Forecast Report 2026-2030 — The Business Research Company | https://www.thebusinessresearchcompany.com/report/device-as-a-service-global-market-report |
| 90 | Device-as-a-Service Market Size, Share and Trends 2026 — Precedence Research | https://www.precedenceresearch.com/device-as-a-service-market |
| 91 | Device as a Service Market Size, Trends — Market Research Future | https://www.marketresearchfuture.com/reports/device-as-a-service-market-4486 |
| 92 | Device as a Service Market Size & Share Growth Report 2035 — Research Nester | https://www.researchnester.com/reports/device-as-a-service-daas-market/3703 |
| 93 | Device As A Service Market Growth Analysis 2025-2029 — Technavio | https://www.technavio.com/report/device-as-a-service-market-analysis |
| 94 | Device as a Service Market — Fortune Business Insights | https://www.fortunebusinessinsights.com/device-as-a-service-market-108000 |
| 95 | Thương mại điện tử Việt Nam năm 2024: Những bước tiến và thách thức — Bộ Công Thương | https://moit.gov.vn/khoa-hoc-va-cong-nghe/thuong-mai-dien-tu-viet-nam-nam-2024-nhung-buoc-tien-va-thach-thuc.html |
| 96 | Quy mô thị trường thương mại điện tử Việt Nam ước đạt 14,7 tỷ USD trong năm 2024 — VnEconomy | https://vneconomy.vn/quy-mo-thi-truong-thuong-mai-dien-tu-viet-nam-uoc-dat-14-7-ty-usd-trong-nam-2024.htm |
| 97 | Ngành hàng thiết bị điện tử: Xu hướng mới và cơ hội trong tháng 7/2024 — Metric Insights | https://metric.vn/insights/nganh-hang-thiet-bi-dien-tu-xu-huong-moi-va-co-hoi-trong-thang-7-2024/ |
| 98 | Vietnam Shared Mobility and Bike Rentals Market — Ken Research | https://www.kenresearch.com/vietnam-shared-mobility-and-bike-rentals-market |
| 99 | Vietnam Recommerce Market Intelligence Databook 2025 — Businesswire | https://www.businesswire.com/news/home/20250701589204/en/Vietnam-Recommerce-Market-Intelligence-Databook-2025-13.7-Growth-in-2025-Led-by-C2C-and-B2C-Platforms---ResearchAndMarkets.com |
| 100 | Thị trường laptop chuẩn bị mùa kinh doanh sôi động — Báo Đầu tư | https://baodautu.vn/thi-truong-laptop-chuan-bi-mua-kinh-doanh-soi-dong-d192674.html |

### 12.7. Giá laptop cũ (bài toán vốn)

| # | Tiêu đề | URL |
|---|---|---|
| 101 | Laptop Dell cũ dưới 5 triệu: Top 5 dành cho văn phòng, học sinh, sinh viên 2025 | https://laptopnhatlinh.vn/top-5-laptop-dell-cu-duoi-5-trieu-dang-mua-nhat-2025-laptop-nhat-linh/ |
| 102 | Chợ Tốt — Mua bán laptop cũ (39.814 tin, 09/08/2025) | https://www.chotot.com/mua-ban-laptop |
| 103 | Laptop Dell cũ uy tín, giá từ 4 triệu — Khoa Vàng | https://khoavang.vn/laptop-dell-cu/c726 |

---

## 13. CHECKLIST VIỆC CẦN LÀM TIẾP (cho nhóm làm proposal)

| # | Việc | Ưu tiên | Ghi chú |
|---|---|---|---|
| 1 | **Hỏi Phòng Khảo thí FPTU Đà Nẵng**: sinh viên có được dùng máy mượn/thuê vào phòng thi không? | 🔴 **Cao nhất** | Nếu KHÔNG được phép, toàn bộ ý tưởng phải xoay trục |
| 2 | Xin **số lượng sinh viên** campus FPTU Đà Nẵng từ Phòng CTSV/Ban Đào tạo | 🔴 Cao | Không có số này thì không tính được TAM/SAM/SOM |
| 3 | **Khảo sát Google Form** sinh viên FPTU ĐN: đã từng gặp sự cố laptop ngày thi chưa? sẵn sàng trả bao nhiêu? | 🔴 Cao | Dữ liệu sơ cấp — giá trị cao nhất cho proposal |
| 4 | **Gọi 5 hotline Đà Nẵng** hỏi giá thuê 1 ngày + mức cọc thực tế (Trường Giang 1900 2007; leminhSTORE 0915 819 967; Đình Hậu 0948 637 037; Sky Computer 0708 084 444; Kim Anh 0815 126 126) | 🔴 Cao | Vừa xác minh dữ liệu, vừa là primary research |
| 5 | **Tìm trong nhóm Facebook sinh viên FPT ĐN** từ khoá "thuê laptop", "máy hỏng", chụp màn hình | 🟠 Trung bình | Bằng chứng nhu cầu thực |
| 6 | **Mở lại và chụp màn hình** các bảng giá tại mục 12 làm phụ lục | 🟠 Trung bình | Do WebFetch bị chặn nên chưa xác minh được |
| 7 | Xác minh Kim Anh Computer (248 Ngũ Hành Sơn) có cho thuê không | 🟠 Trung bình | Đơn vị gần campus nhất |
| 8 | Soạn **mẫu hợp đồng/phiếu thuê** có điều khoản bồi thường (căn cứ BLDS 2015 Đ.554, 557) | 🟢 Thấp hơn | Đưa vào phụ lục proposal |

---

*Tài liệu nghiên cứu — soạn ngày 14/09/2026. Mọi số liệu cần xác minh lại theo hướng dẫn tại [mục 0](#0-ghi-chú-phương-pháp-và-giới-hạn--đọc-trước-khi-dùng-số-liệu) trước khi đưa vào bản proposal nộp bài.*
