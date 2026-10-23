# 03 — BỐI CẢNH ĐẠI HỌC FPT ĐÀ NẴNG & QUY MÔ THỊ TRƯỜNG (TAM/SAM/SOM)

> **Tài liệu nghiên cứu thô** phục vụ proposal khởi nghiệp "Website cho thuê laptop đi thi" — Đại học FPT Đà Nẵng, phường Hoà Hải / Ngũ Hành Sơn, Đà Nẵng.
> Ngày lập: **14/09/2026**. Ưu tiên dữ liệu 2024–2026.

---

## ⚠️ CẢNH BÁO PHƯƠNG PHÁP — ĐỌC TRƯỚC KHI DÙNG SỐ LIỆU

**Trong phiên nghiên cứu này, công cụ tải trang web trực tiếp (WebFetch/curl) bị CHẶN HOÀN TOÀN bởi chính sách egress của tổ chức** (lỗi `EGRESS_BLOCKED`, `CONNECT tunnel failed, response 403`). Các domain đã thử và bị chặn: `daihoc.fpt.edu.vn`, `it.fpt.edu.vn`, `it-hcm.fpt.edu.vn`, `bctn2025.fpt.com`, `vi.wikipedia.org`, `en.wikipedia.org`, `vnexpress.net`, `studocu.vn`, `trangedu.com`, `fptudn.info.vn`, `fptcity.vn`.

**Hệ quả:** toàn bộ số liệu dưới đây đến từ **kết quả công cụ tìm kiếm web (WebSearch)** — tức là nội dung trích xuất từ các trang thật, kèm URL thật — **nhưng tôi KHÔNG tự mở và đọc được trang gốc để xác minh từng con số**.

**Khuyến nghị cho người viết proposal:** mọi con số gắn nhãn 🟡 hoặc 🔴 dưới đây **phải được người viết mở URL gốc kiểm chứng lại** trước khi đưa vào bản nộp. Số gắn nhãn 🟢 là số xuất hiện nhất quán ở nhiều nguồn độc lập.

| Nhãn | Ý nghĩa |
|---|---|
| 🟢 | Số xuất hiện ở ≥2 nguồn độc lập, nhất quán — dùng được |
| 🟡 | Số từ 1 nguồn, cần kiểm chứng lại |
| 🔴 | **Ước lượng của người nghiên cứu**, KHÔNG phải số liệu công bố — phải ghi rõ "ước tính" trong proposal |

---

## PHẦN 1 — HỒ SƠ CAMPUS ĐẠI HỌC FPT ĐÀ NẴNG

### 1.1. Vị trí & địa giới hành chính

| Hạng mục | Thông tin | Nhãn | Nguồn |
|---|---|---|---|
| Địa chỉ | Đường Nam Kỳ Khởi Nghĩa, Khu đô thị công nghệ FPT City, phường Hoà Hải, quận Ngũ Hành Sơn, TP. Đà Nẵng | 🟢 | [FPT City Đà Nẵng — Vị trí & tiện ích](https://fptcity.vn/vi-tri/), [Campus Đà Nẵng — Trường ĐH FPT](https://daihoc.fpt.edu.vn/da-nang/) |
| Diện tích khuôn viên | **5,1 ha** | 🟢 | [Campus Đà Nẵng — Trường ĐH FPT](https://daihoc.fpt.edu.vn/da-nang/), [Bản đồ Trường ĐH FPT](https://daihoc.fpt.edu.vn/tat-tan-tat-ve-fptu/ban-do-truong-dai-hoc-fpt/) |
| Năm khởi công | **2018** | 🟢 | [Campus Đà Nẵng — Trường ĐH FPT](https://daihoc.fpt.edu.vn/da-nang/) |
| Điện thoại | (0236) 730 0999 | 🟡 | [Thông tin tuyển sinh ĐH FPT Đà Nẵng](https://trangedu.com/truong/dai-hoc-fpt-da-nang/) |

#### ⚠️ THAY ĐỔI ĐỊA GIỚI HÀNH CHÍNH — RẤT QUAN TRỌNG CHO PROPOSAL

Từ **01/07/2025**, theo **Nghị quyết 1659/NQ-UBTVQH15 ngày 16/06/2025** của Uỷ ban Thường vụ Quốc hội:

- **4 phường Mỹ An, Khuê Mỹ, Hoà Hải, Hoà Quý** (quận Ngũ Hành Sơn cũ) đã được **sáp nhập thành 01 phường mới tên là "phường Ngũ Hành Sơn"**. 🟢
- Trụ sở phường mới: **486 Lê Văn Hiến, phường Ngũ Hành Sơn**. 🟡
- Cấp quận bị bỏ; TP. Đà Nẵng (sau hợp nhất với Quảng Nam) còn **94 đơn vị hành chính cấp xã: 23 phường, 70 xã, 1 đặc khu**. 🟢

> **Nguồn:** [Phường Hòa Hải quận Ngũ Hành Sơn cũ đổi tên thành gì sau sáp nhập? — Thư Viện Pháp Luật](https://thuvienphapluat.vn/phap-luat/phuong-hoa-hai-quan-ngu-hanh-son-cu-doi-ten-thanh-gi-sau-sap-nhap-phuong-hoa-hai-da-nang-cu-sap-nha-532300-234324.html) · [Đà Nẵng: Còn 16 đơn vị hành chính cấp xã sau sắp xếp — Báo Chính phủ](https://baochinhphu.vn/da-nang-con-16-don-vi-hanh-chinh-cap-xa-sau-sap-xep-102250423101211946.htm) · [Cổng TTĐT TP Đà Nẵng](https://danang.gov.vn/en/w/thanh-pho-da-nang-sau-sap-xep-co-16-on-vi-hanh-chinh-cap-xa)

**👉 Hàm ý cho proposal:** Khi đăng ký hộ kinh doanh / ghi địa chỉ pháp lý, **phải dùng tên mới "phường Ngũ Hành Sơn, TP. Đà Nẵng"**, không dùng "phường Hoà Hải, quận Ngũ Hành Sơn" (đã hết hiệu lực từ 01/07/2025). Đây là chi tiết dễ bị chấm điểm trừ nếu ghi sai.

> **Lưu ý mâu thuẫn nguồn:** Cổng TTĐT Đà Nẵng ghi "16 đơn vị hành chính cấp xã" (đây là số của TP Đà Nẵng cũ trước hợp nhất Quảng Nam), còn nguồn khác ghi 94 đơn vị (sau hợp nhất). Cần kiểm chứng lại mốc thời gian của từng con số.

### 1.2. Cơ sở vật chất campus Đà Nẵng

| Hạng mục | Chi tiết | Nhãn |
|---|---|---|
| Toà nhà Alpha | Thiết kế "những cuốn sách chồng lên nhau"; đoạt giải **"Designed Award Winning Architecture Projects"** của World Architecture | 🟡 |
| Thư viện | **>33.000 đầu sách**, giáo trình quốc tế, Ebook, tài liệu chuyên ngành | 🟢 |
| Sân bóng đá | Cỏ nhân tạo **1.500 m²**, sân 5–7 người, có hệ thống chiếu sáng, khung lưới, khu nghỉ, bãi xe | 🟢 |
| Thể thao khác | Sân bóng rổ, **2 sân bóng chuyền**, khu street workout | 🟢 |
| Ký túc xá | Nằm **trong khuôn viên**, cách toà học chính vài bước chân; phòng **4 người** và **6 người** (bố trí 3–6 SV/phòng); có điều hoà, nước nóng, bình lọc nước, PCCC, camera, bảo vệ 24/24; có phòng gym; căng-tin 3 tầng | 🟢 |
| Số slot KTX | **500 slot đợt 1** mở đăng ký cho tân SV K19 | 🟡 |

> **Nguồn:** [Campus Đà Nẵng — Trường ĐH FPT](https://daihoc.fpt.edu.vn/da-nang/) · [Ký túc xá tại ĐH FPT Đà Nẵng dành cho tân sinh viên K19](https://daihoc.fpt.edu.vn/chua-phan-loai/ky-tuc-xa-tai-dh-fpt-da-nang-danh-cho-tan-sinh-vien-k19/) · [Tổng hợp thông tin KTX, nhà ở cho tân SV ĐH FPT 3 miền](https://daihoc.fpt.edu.vn/chua-phan-loai/tong-hop-thong-tin-ky-tuc-xa-nha-o-danh-cho-tan-sinh-vien-dh-fpt-3-mien/) · [FPT Dormitory](https://ocd.fpt.edu.vn/)

**👉 Hàm ý kinh doanh:** KTX chỉ ~500 slot đợt 1 → **phần lớn sinh viên FPT ĐN ở trọ bên ngoài**, rải rác quanh khu Hoà Hải / Ngũ Hành Sơn / Hoà Quý. Đây vừa là cơ hội (bán kính giao hàng tập trung 1–3 km) vừa là rủi ro (phải giao tận nơi sáng sớm ngày thi).

---

## PHẦN 2 — ⭐ HÌNH THỨC THI CỦA ĐẠI HỌC FPT (PHẦN QUAN TRỌNG NHẤT CỦA PROPOSAL)

> Đây là **phần chứng minh "pain point" có thật**. Toàn bộ luận điểm kinh doanh nằm ở đây.

### 2.1. Hệ thống thi EOS — Exam Online System

**Sinh viên ĐH FPT thi cuối kỳ trên phần mềm EOS, chạy trên LAPTOP CÁ NHÂN của chính sinh viên.**

| Yêu cầu | Nội dung | Nhãn | Nguồn |
|---|---|---|---|
| Hệ điều hành | **BẮT BUỘC Windows**. Khuyến cáo **Windows 10** để tương thích tốt với phần mềm thi | 🟢 | [Hướng dẫn cài đặt phần mềm thi EOS và SEB — Helpdesk FPTU](https://it.fpt.edu.vn/cantho/huong-dan-cai-dat-phan-mem-thi-eos-seb/) |
| MacBook | **Bắt buộc cài Windows qua Bootcamp**. **KHÔNG hỗ trợ Mac chip M1, M2** | 🟢 | [Hướng dẫn cài đặt phần mềm thi EOS và SEB](https://it.fpt.edu.vn/cantho/huong-dan-cai-dat-phan-mem-thi-eos-seb/) · [Hướng dẫn SV sử dụng và thi trên phần mềm EOS tại Trường ĐH FPT](https://daihoc.fpt.edu.vn/tin-noi-bat-muc-tin-tuc/huong-dan-sinh-vien-su-dung-va-thi-tren-phan-mem-eos-tai-truong-dai-hoc-fpt/) |
| Mạng | Kết nối internet **ổn định** là "cực kỳ quan trọng" | 🟢 | [Hướng dẫn SV sử dụng và thi trên phần mềm EOS](https://daihoc.fpt.edu.vn/tin-noi-bat-muc-tin-tuc/huong-dan-sinh-vien-su-dung-va-thi-tren-phan-mem-eos-tai-truong-dai-hoc-fpt/) |
| Tai nghe | **Tai nghe CÓ DÂY** bắt buộc cho phần thi Listening | 🟢 | [Hướng dẫn SV K18 thi EOS kỳ thi Kiểm tra Tiếng Anh](https://daihoc.fpt.edu.vn/tin-tuc-chung-2/huong-dan-sinh-vien-k18-su-dung-va-thi-tren-phan-mem-eos-ky-thi-kiem-tra-tieng-anh/) |
| Giấy tờ | Thẻ sinh viên / CCCD / giấy tờ tuỳ thân hợp lệ để xác minh | 🟢 | [Hướng dẫn SV sử dụng và thi tiếng Anh xếp lớp trên EOS](https://daihoc.fpt.edu.vn/tin-tuc-chung-2/su-kien-tin-tuc-chung-2/huong-dan-sinh-vien-su-dung-va-thi-tieng-anh-xep-lop-tren-phan-mem-eos/) |
| Màn hình | **Chỉ được dùng 01 màn hình** khi thi | 🟡 | [Hướng dẫn SV sử dụng và thi trên phần mềm EOS](https://daihoc.fpt.edu.vn/tin-noi-bat-muc-tin-tuc/huong-dan-sinh-vien-su-dung-va-thi-tren-phan-mem-eos-tai-truong-dai-hoc-fpt/) |
| Thi từ xa | Camera phải thấy rõ mặt và không gian xung quanh; Phòng Khảo thí gửi link Google Meet trước ngày thi | 🟡 | [HD làm bài thi cuối kỳ môn học trên EOS Client — Studocu](https://www.studocu.vn/vn/document/truong-dai-hoc-fpt/quan-tri-kinh-doanh/huong-dan-lam-bai-thi-cuoi-ky-tren-eos-client/27055728) |
| Phần mềm phụ trợ | **SEB (Safe Exam Browser)** cài kèm EOS | 🟢 | [Hướng dẫn cài đặt phần mềm thi EOS và SEB](https://it.fpt.edu.vn/cantho/huong-dan-cai-dat-phan-mem-thi-eos-seb/) |

### 2.2. Hai biến thể phần mềm thi

| Phần mềm | Dùng cho môn nào | Nhãn |
|---|---|---|
| **EOS Client** | Business English (BE) và các môn trắc nghiệm chung | 🟡 |
| **IT Client** | Java, C#, C/C++, Computer Network, Operating System (OS), Introduction to Database | 🟡 |

> **Nguồn:** [HD sử dụng phần mềm thi EOS — Studocu](https://studocu.com/vn/document/fpt-university/trs601/huong-dan-sinh-vien-su-dung-phan-mem-thi-eos/23377167) · [HD sử dụng phần mềm thi EOS Client — Studocu](https://www.studocu.vn/vn/document/truong-dai-hoc-fpt/working-in-groups/huong-dan-su-dung-eos-client/58823637) · [HD sử dụng phần mềm thi EOS học kỳ SUMMER 2025 — Studocu](https://www.studocu.vn/vn/document/dai-hoc-fpt-ha-noi/english-trs3/huong-dan-su-dung-phan-mem-thi-eos-hoc-ky-summer-2025/134096866)

### 2.3. ⭐ CƠ CHẾ KỸ THUẬT — LÝ DO LAPTOP LÀ "ĐIỂM CHẾT ĐƠN LẺ"

Luồng hoạt động của EOS:

```
Server trường  ──(tải đề)──►  Máy tính CÁ NHÂN của sinh viên
                                        │
                                  (làm bài offline)
                                        │
                              Lưu bài thành file .dat
                              TRÊN Ổ CỨNG MÁY SINH VIÊN
                                        │
                                 (nộp bài lên server)
                                        ▼
                                  Server trường
```

**Các rủi ro được chính tài liệu hướng dẫn của trường cảnh báo:**

1. **Bài thi chỉ tồn tại trong thư mục đã giải nén trên máy sinh viên.** Nếu sinh viên **không giải nén đúng phần mềm thi trước khi thi → gặp lỗi và MẤT BÀI THI**. 🟡
2. Khi máy tính gặp lỗi trong lúc thi, sinh viên **phải báo ngay giám thị** để được hướng dẫn. 🟢
3. Quy trình xử lý sự cố phổ biến: **giữ nút nguồn 10 giây** để tắt hẳn máy rồi khởi động lại. 🟡

> **Nguồn:** [Hướng dẫn SV sử dụng và thi trên phần mềm EOS tại FPTU Hà Nội](https://daihoc.fpt.edu.vn/tin-tuc-chung-2/huong-dan-sinh-vien-su-dung-va-thi-tren-phan-mem-eos-tai-fptu-ha-noi/) · [HDSV sử dụng và thi trên phần mềm EOS — hanoi.fpt.edu.vn](https://hanoi.fpt.edu.vn/huong-dan-sinh-vien-su-dung-va-thi-tren-phan-mem-eos.html) · [Hỗ trợ Khảo thí: 02462597749](https://daihoc.fpt.edu.vn/huong-dan-sinh-vien-su-dung-va-thi-tren-phan-mem-eos-tai-fptu-ha-noi/)

### 2.4. 🎯 TỔNG HỢP LUẬN ĐIỂM "PAIN POINT" CHO PROPOSAL

> **Tại ĐH FPT, laptop cá nhân KHÔNG phải là công cụ học tập tuỳ chọn — nó là THIẾT BỊ DỰ THI BẮT BUỘC.**
>
> Trường **không cấp máy** cho kỳ thi cuối kỳ. Bài thi nằm vật lý trên ổ cứng máy sinh viên. Không có laptop Windows chạy được EOS vào đúng buổi thi = **không thể dự thi**.
>
> Các kịch bản hỏng làm sinh viên mất kỳ thi:
> - Laptop hỏng đột ngột (màn hình, bàn phím, ổ cứng, main) trước/trong ngày thi
> - Pin chai + hỏng sạc, phòng thi không đủ ổ cắm
> - Máy MacBook chip **M1/M2/M3** — **không cài được Bootcamp**, không chạy được EOS
> - Máy Windows cấu hình quá yếu / lỗi hệ điều hành, không cài được SEB
> - Quên mang máy / mang nhầm sạc
> - Máy đang bảo hành/sửa chữa đúng tuần thi
>
> **→ Đây chính là thị trường của dịch vụ cho thuê laptop đi thi.**

**Điểm bán hàng đặc thù (USP) rút ra từ dữ liệu kỹ thuật trên — máy cho thuê phải:**
- Cài sẵn **Windows 10/11 bản quyền**
- **Cài sẵn EOS Client + IT Client + SEB**, đã test giải nén đúng thư mục
- Có **cổng 3.5mm cho tai nghe có dây** (nhiều laptop mới bỏ jack → sinh viên không thi Listening được)
- Có **webcam** (cho ca thi từ xa)
- **Pin còn tốt + kèm sạc**
- Đã gỡ sạch dữ liệu, tài khoản sạch để không vướng quy chế thi

---

## PHẦN 3 — LỊCH HỌC & LỊCH THI (XÁC ĐỊNH "MÙA VỤ" KINH DOANH)

### 3.1. Hệ 3 học kỳ/năm

| Học kỳ | Thời gian | Nhãn |
|---|---|---|
| **Spring** | Tháng 1 → tháng 5 | 🟢 |
| **Summer** | Tháng 5 → tháng 9 | 🟢 |
| **Fall** | Tháng 9 → hết tháng 12 | 🟢 |

- Một năm học có **3 học kỳ** (Fall – Spring – Summer), bắt đầu vào **tháng 9 – tháng 1 – tháng 5**. 🟢
- Mỗi học kỳ kéo dài **04 tháng**, tương đương **15–16 tuần**. 🟢
- Mô tả khác: mỗi kỳ **học 3 tháng, nghỉ 1 tháng** → sinh viên FPT **chỉ học 9 tháng/năm**. 🟡
- Toàn khoá: **4 năm – 9 kỳ – 4 giai đoạn**. 🟡

> **Nguồn:** [Ở FPTU, một năm học có 3 học kỳ — Fanpage Trường ĐH FPT](https://www.facebook.com/university.fpt.edu.vn/posts/1183525043803905/) · [Thời gian học Đại học FPT: 4 năm – 9 kỳ – 4 giai đoạn](https://hanoi.fpt.edu.vn/tu-van/thoi-gian-hoc-dai-hoc-fpt.html) · [Lộ trình đào tạo của Trường ĐH FPT](https://daihoc.fpt.edu.vn/lo-trinh-dao-tao-cua-truong-dai-hoc-fpt/) · ["Mùa học thêm" tại ĐH FPT](https://daihoc.fpt.edu.vn/tin-tuc-chung-2/mua-hoc-them-tai-dai-hoc-fpt/)

### 3.2. Quy chế thi

| Quy định | Nội dung | Nhãn | Nguồn |
|---|---|---|---|
| Số lần thi | Sinh viên được thi **tối đa 2 lần** theo lịch của trường. Điểm lần 1 là điểm chính thức; nếu không đạt thì dùng điểm lần 2 | 🟡 | [Sổ tay sinh viên Trường ĐH FPT](https://daihoc.fpt.edu.vn/en/wp-content/uploads/2017/06/So-tay-sinh-vien-FUG-2016.doc) |
| Đăng ký thi lại cải thiện | Phải nộp đơn **trước 12 giờ** so với giờ thi lại | 🟡 | [FAP Mobile App Guide — Studocu](https://www.studocu.vn/vn/document/truong-dai-hoc-fpt/code-vhdl/fap-mobile-app-guide-procedures-important-notices/156254239) |
| Tra cứu lịch thi | Qua mục **"Xem lịch thi"** trên **FAP – FPT Academic Portal** (`fap.fpt.edu.vn`); có icon "New" khi có lịch mới | 🟢 | [Truy cập cổng học thuật Academic Portal (FAP) — Helpdesk FPTU](https://it.fpt.edu.vn/cantho/huong-dan-he-thong-academic-portal-fap/) |
| Đào tạo | Theo **chế độ tín chỉ**; có học phần tự chọn và học phần điều kiện | 🟢 | [Quy chế đào tạo đại học chính quy — ĐH FPT](https://daihoc.fpt.edu.vn/quy-che-dao-tao-dai-hoc-chinh-quy/) |

### 3.3. 📅 LỊCH MÙA VỤ KINH DOANH SUY RA (cho mô hình tài chính)

> ⚠️ 🔴 **Đây là SUY LUẬN của người nghiên cứu**, không phải lịch thi công bố. Tôi **không tìm được** lịch thi cuối kỳ chính thức (ngày cụ thể, số ngày thi) của ĐH FPT Đà Nẵng. **Người viết proposal phải xin lịch thi thật từ FAP hoặc Phòng Khảo thí.**

Dựa trên cấu trúc 3 kỳ × 4 tháng, suy ra **3 đỉnh cầu/năm**:

| Đỉnh cầu | Thời điểm ước tính | Loại thi |
|---|---|---|
| Đỉnh 1 | **Cuối tháng 4 – đầu tháng 5** | Final Exam kỳ Spring |
| Đỉnh 2 | **Cuối tháng 8 – đầu tháng 9** | Final Exam kỳ Summer |
| Đỉnh 3 | **Cuối tháng 12** | Final Exam kỳ Fall |
| Đỉnh phụ (×3) | Giữa mỗi kỳ | **Progress Test** |

**👉 Hàm ý tài chính:** doanh thu **không đều** — tập trung ~6 đợt/năm, mỗi đợt 1–2 tuần. Mô hình tài chính trong proposal **phải mô hình hoá theo mùa vụ**, không chia đều 12 tháng. Giữa các đợt thi, đội laptop nên chuyển sang cho thuê theo tháng (thực tập, đồ án, OJT) để tránh nằm không.

---

## PHẦN 4 — QUY MÔ SINH VIÊN (CƠ SỞ TÍNH TAM/SAM/SOM)

### 4.1. Hệ thống Giáo dục FPT (FPT Education) — cấp tập đoàn

| Chỉ số | Giá trị | Thời điểm | Nhãn | Nguồn |
|---|---|---|---|---|
| Mục tiêu quy mô HSSV | **150.000** HSSV | Mục tiêu năm 2025 | 🟡 | [FPT đẩy mạnh phát triển hệ thống giáo dục phổ thông — fpt.com](https://fpt.com/vi/tin-tuc/tin-fpt/fpt-day-manh-phat-trien-he-thong-giao-duc-pho-thong) |
| Bậc đại học | Giữ ổn định **~50.000 sinh viên** | 2025 | 🟡 | [Anh Lê Trường Tùng: 2026 sẽ là năm nâng tầm toàn diện Giáo dục FPT — chungta.vn](https://chungta.vn/longform/b-anh-le-truong-tung-2026-se-la-nam-nang-tam-toan-dien-giao-duc-fpt-b-1140961.html) |
| Khối giáo dục nghề nghiệp | Quy mô **tương đương** bậc đại học (~50.000) | 2025 | 🟡 | [chungta.vn](https://chungta.vn/longform/b-anh-le-truong-tung-2026-se-la-nam-nang-tam-toan-dien-giao-duc-fpt-b-1140961.html) |
| FPT Schools (phổ thông) | **>18.000 học sinh** | Năm học 2026–2027 | 🟢 | [Lễ khai giảng năm học 2026–2027 toàn hệ thống FPT Schools](https://fschool.fpt.edu.vn/tung-bung-le-khai-giang-nam-hoc-2026-2027-toan-he-thong-fpt-schools-hon-18-000-hoc-sinh-cung-buoc-vao-hanh-trinh-moi/) |
| Doanh thu mảng Giáo dục, đầu tư và khác | **6.132 tỷ VND**; LNTT **2.792 tỷ VND**; biên LN **45,5%** | Năm 2025 | 🟡 | [Lĩnh vực giáo dục — Báo cáo thường niên FPT 2025](https://bctn2025.fpt.com/vi/phan-tich-hoat-dong-kinh-doanh/linh-vuc-giao-duc/) |

> **⚠️ Mâu thuẫn nguồn cần lưu ý:** một kết quả tìm kiếm còn nêu "Tổ chức Giáo dục FPT đang đào tạo hơn 130 học sinh cấp tiểu học, gần 1.000 học sinh THPT và gần 25.000 sinh viên, học viên" — con số này **mâu thuẫn rõ** với các số khác và có vẻ là dữ liệu cũ (nhiều năm trước). **Không dùng con số 25.000 này.**

### 4.2. Trường Đại học FPT — toàn hệ thống

| Chỉ số | Giá trị | Nhãn | Nguồn |
|---|---|---|---|
| Số campus | **5**: Hà Nội, TP.HCM, Đà Nẵng, Cần Thơ, Quy Nhơn | 🟢 | [Campus — Trường ĐH FPT](https://daihoc.fpt.edu.vn/campus/), [Phân hiệu — Trường ĐH FPT](https://daihoc.fpt.edu.vn/truong-thanh-vien/) |
| Tổng sinh viên ĐH & sau ĐH | **~30.000** (tính đến 2024) | 🟡 | [FPT University — Wikipedia](https://en.wikipedia.org/wiki/FPT_University) |
| Tổng chỉ tiêu tuyển sinh 2025 | **13.677 sinh viên** toàn quốc | 🟢 | [Quy chế tuyển sinh hệ ĐH chính quy 2025 — ĐH FPT](https://daihoc.fpt.edu.vn/quy-che-tuyen-sinh-2025/), [Đề án và chỉ tiêu tuyển sinh ĐH FPT 2025 — situ.edu.vn](https://situ.edu.vn/de-an-va-chi-tieu-tuyen-sinh-dai-hoc-fpt/) |
| Số ngành/chuyên ngành | **41 ngành** (2025); **6 nhóm ngành / 39 chuyên ngành** (2026) | 🟡 | [Đề án tuyển sinh 2025 — HOCMAI](https://huongnghiep.hocmai.vn/tuyen-sinh-2025-dai-hoc-fpt-fpt-university-cong-bo-de-an-tuyen-sinh-2025-41-nganh-4-phuong-thuc), [Các ngành đào tạo Trường ĐH FPT 2026](https://daihoc.fpt.edu.vn/tat-tan-tat-ve-fptu/cac-nganh-dai-hoc-fpt/) |
| Điểm chuẩn 2025 | **18,5 điểm** (17 điểm với thí sinh "thế hệ 1") — Toán + 2 môn bất kỳ + điểm ưu tiên | 🟢 | [Trường ĐH FPT công bố điểm chuẩn xét tuyển 2025 — VnExpress](https://vnexpress.net/truong-dai-hoc-fpt-cong-bo-diem-chuan-xet-tuyen-2025-4915009.html) |
| Năm thành lập | 2006 | 🟢 | [uniRank — FPT University](https://www.unirank.org/vn/uni/fpt-university/) |
| Tỷ lệ trúng tuyển | 40–49% | 🟡 | [uniRank](https://www.unirank.org/vn/uni/fpt-university/) |
| Tỷ lệ SV có việc làm | **98% trong 6 tháng** sau tốt nghiệp | 🟡 | [Standyou — FPT University](https://www.standyou.com/study-abroad/fpt-university-vietnam/) |
| Học bổng 2025 | **2.800 suất**; **100 suất Global Expert** (100% học phí + **30 triệu VND/năm** sinh hoạt phí) | 🟡 | [vietnam.vn — FPT University 'Learn Now – Pay Later'](https://www.vietnam.vn/en/truong-dai-hoc-fpt-ho-tro-1-000-tan-sinh-vien-nam-2025-theo-chinh-sach-hoc-truoc-tra-sau) |
| Chính sách "Học trước – Trả sau" | Hỗ trợ **1.000 tân sinh viên** năm 2025; trả góp 30% / 50% / 70% tổng học phí | 🟡 | [vietnam.vn](https://www.vietnam.vn/en/truong-dai-hoc-fpt-ho-tro-1-000-tan-sinh-vien-nam-2025-theo-chinh-sach-hoc-truoc-tra-sau) |

> **⚠️ Mâu thuẫn nghiêm trọng:** [uniRank](https://www.unirank.org/vn/uni/fpt-university/) xếp ĐH FPT vào nhóm **8.000–8.999 sinh viên**, trong khi Wikipedia ghi **~30.000**. uniRank là dữ liệu tự khai/thu thập, thường lỗi thời với trường tăng trưởng nhanh. **Khuyến nghị dùng ~30.000 và ghi rõ nguồn + năm.**

### 4.3. ⭐ SINH VIÊN ĐẠI HỌC FPT ĐÀ NẴNG — SỐ LIỆU & ƯỚC LƯỢNG

#### Dữ liệu thật tìm được

| Dữ liệu | Giá trị | Thời điểm | Nhãn | Nguồn |
|---|---|---|---|---|
| Tân sinh viên khoá 16 khai giảng | **gần 1.000** | 26/09/2020 | 🟢 | [1.000 tân sinh viên ĐH FPT Đà Nẵng khai giảng năm học mới — FPT City](https://fptcity.vn/1-000-tan-sinh-vien-dai-hoc-fpt-da-nang-khai-giang-nam-hoc-moi/) |
| Sinh viên quốc tế đón hằng năm | **gần 1.000** SV quốc tế/năm (Nhật, Thái Lan, Lào, Myanmar, Brunei, Indonesia) | ~2025 | 🟡 | [FPT University, Da Nang Campus — International Office Universitas Indonesia](https://international.ui.ac.id/shortcourse-fpt/) |
| Khai giảng toàn trường K21 | 05/09/2025 | 2025 | 🟢 | [Lễ khai giảng ĐH FPT 2025-2026 — K21](https://daihoc.fpt.edu.vn/hcm/tung-bung-le-khai-giang-truong-dai-hoc-fpt-2025-2026-khoi-dau-hanh-trinh-ruc-ro-cua-the-he-tan-sinh-vien-k21/) |

#### 🔴 ƯỚC LƯỢNG CÓ CƠ SỞ — Sinh viên ĐH FPT Đà Nẵng hiện tại

> **KHÔNG tìm được số chính thức.** Dưới đây là ước lượng tam giác hoá, **phải ghi rõ "ước tính của nhóm" trong proposal.**

**Cách 1 — Suy từ chỉ tiêu toàn quốc 2025 (13.677):**

Giả định phân bổ campus (🔴 giả định của người nghiên cứu, KHÔNG có nguồn):
| Campus | Tỷ trọng giả định | Chỉ tiêu suy ra |
|---|---|---|
| Hà Nội | ~45–50% | 6.150 – 6.840 |
| TP.HCM | ~25–30% | 3.420 – 4.100 |
| **Đà Nẵng** | **~10–12%** | **1.370 – 1.640** |
| Cần Thơ + Quy Nhơn | ~10–15% | 1.370 – 2.050 |

→ Tân SV Đà Nẵng/năm ≈ **1.300 – 1.600**.
Nhân với 4 khoá đang học, trừ ~15% rơi rớt/OJT/học kỳ nước ngoài:
→ **Tổng SV ĐH FPT Đà Nẵng ≈ 4.500 – 6.000 sinh viên** 🔴

**Cách 2 — Suy từ tăng trưởng lịch sử:**
2020 (K16): gần 1.000 tân SV → giả định tăng 8–12%/năm trong 5 năm → 2025 (K21): **1.470 – 1.760** tân SV/năm
→ Tổng 4 khoá ≈ **5.000 – 6.500 sinh viên** 🔴

**Cách 3 — Kiểm tra chéo bằng sức chứa KTX:** 500 slot KTX đợt 1 cho K19. Nếu KTX phục vụ ~10% tổng sinh viên → ~5.000 SV. Nếu phục vụ 30% tân SV → tân SV ~1.600. **Nhất quán với cách 1 và 2.** ✓

> ### 🎯 **CON SỐ ĐỀ XUẤT DÙNG TRONG PROPOSAL**
> **Sinh viên ĐH FPT Đà Nẵng ≈ 5.000 (khoảng 4.500 – 6.000) sinh viên** 🔴
> **BẮT BUỘC ghi chú:** *"Ước tính của nhóm dựa trên chỉ tiêu tuyển sinh toàn quốc 2025 là 13.677 SV và số tân sinh viên khoá 16 tại Đà Nẵng năm 2020 là gần 1.000; trường không công bố số sinh viên theo từng campus."*
>
> **Cách kiểm chứng thật (khuyến nghị mạnh):** Vì nhóm là sinh viên FPT ĐN, **hãy xin số liệu trực tiếp từ Phòng Công tác Sinh viên / Phòng Đào tạo campus Đà Nẵng**. Một email/đơn xin số liệu kèm vào phụ lục proposal sẽ nâng điểm hơn hẳn mọi ước lượng.

### 4.4. Hệ sinh thái FPT khác tại Đà Nẵng (mở rộng SAM)

| Đơn vị | Quy mô | Ghi chú vị trí | Nhãn | Nguồn |
|---|---|---|---|---|
| **Cao đẳng FPT Polytechnic** (toàn quốc) | **40.000+** sinh viên đã theo học | Có cơ sở tại Đà Nẵng; tuyển sinh quanh năm, nhiều đợt nhập học từ T1–T11 | 🟡 | [Thông tin tuyển sinh CĐ FPT Polytechnic](https://tuyensinhso.vn/school/cao-dang-fpt-polytechnic.html), [Đà Nẵng — CĐ FPT Polytechnic](https://caodang.fpt.edu.vn/category/tin-tuc-poly/tin-da-nang) |
| **Greenwich Việt Nam** (toàn quốc) | **gần 20.000** sinh viên trên 4 campus (HN, ĐN, HCM, CT) | Cơ sở Đà Nẵng: **658 Ngô Quyền, phường An Hải** — **KHÔNG nằm ở Hoà Hải** | 🟡 | [Greenwich Việt Nam — Wikipedia](https://vi.wikipedia.org/wiki/Greenwich_Vi%E1%BB%87t_Nam), [Greenwich Việt Nam](https://greenwich.edu.vn/) |
| **FPT Schools Đà Nẵng** | Đón **>700 học sinh** nhập học (lễ tại Nhà hát lớn TP) | Campus hoàn thiện đầu tiên toàn quốc | 🟡 | [Lễ nhập học FSchools Đà Nẵng](https://danang12-school.fpt.edu.vn/le-nhap-hoc-fschools-da-nang/), [FPT Schools Đà Nẵng là đơn vị đầu tiên hoàn thiện campus — chungta.vn](https://chungta.vn/nguoi-fpt/fpt-schools-da-nang-la-don-vi-dau-tien-hoan-thien-campus-tren-ca-nuoc-1136593.html) |

> **⚠️ Lưu ý chiến lược:** Greenwich ĐN ở **An Hải (quận Sơn Trà cũ)**, cách Hoà Hải ~8–10 km. **Không nằm trong bán kính phục vụ ban đầu.** Chỉ đưa vào giai đoạn mở rộng, và cần tính lại chi phí giao hàng.

---

## PHẦN 5 — NGÀNH ĐÀO TẠO & HỌC PHÍ (CHÂN DUNG KHÁCH HÀNG & KHẢ NĂNG CHI TRẢ)

### 5.1. Ngành đào tạo tại campus Đà Nẵng

Năm 2026, campus Đà Nẵng tuyển sinh **3 nhóm ngành**: 🟡

| Nhóm ngành | Chuyên ngành |
|---|---|
| **Công nghệ thông tin** | An toàn & Bảo mật thông tin · Thiết kế Mỹ thuật số · **Kỹ thuật phần mềm** · **Trí tuệ nhân tạo** |
| **Quản trị kinh doanh** | Quản trị khách sạn · QTKD · Kinh doanh quốc tế · Truyền thông đa phương tiện · Quản trị Du lịch & Lữ hành |
| **Ngôn ngữ** | Tiếng Anh · Tiếng Trung · Tiếng Hàn · Tiếng Nhật |

> **Nguồn:** [Thông tin tuyển sinh 2026 — Trường ĐH FPT](https://daihoc.fpt.edu.vn/tuyen-sinh/) · [Các ngành đào tạo Trường ĐH FPT 2026](https://daihoc.fpt.edu.vn/tat-tan-tat-ve-fptu/cac-nganh-dai-hoc-fpt/) · [Tuyển sinh Trường ĐH FPT Đà Nẵng](https://daihoc.fpt.edu.vn/tuyen-sinh-dn/) · [Kỹ thuật phần mềm — ĐH FPT](https://daihoc.fpt.edu.vn/chuyen-nganh/ky-thuat-phan-mem/)

**👉 Hàm ý:** Nhóm CNTT (Kỹ thuật phần mềm, AI, ATTT) thi bằng **IT Client** với các môn Java, C#, C/C++, Computer Network, OS, Database → **nhóm khách hàng ưu tiên số 1**, vì họ vừa thi trên máy nhiều nhất vừa cần cấu hình máy cao nhất (dễ hỏng/quá tải nhất).

### 5.2. Học phí — Campus Đà Nẵng

| Khoản | Mức | Năm áp dụng | Nhãn | Nguồn |
|---|---|---|---|---|
| **Học phí giai đoạn chuyên ngành (Đà Nẵng)** | **22.120.000 VNĐ/học kỳ** | 2025–2026 và 2026–2027 | 🟢 | [Học phí Trường ĐH FPT 2025-2026 tại các cơ sở trên cả nước — Báo Đà Nẵng](https://baodanang.vn/hoc-phi-truong-dai-hoc-fpt-2025-2026-tai-cac-co-so-tren-ca-nuoc-3151966.html), [Học phí ĐH FPT 2026–2027 — jobtest.vn](https://jobtest.vn/hrblog/hoc-phi-dai-hoc-fpt) |
| Dải học phí Đà Nẵng | **15.480.000 – 25.060.000 VNĐ/học kỳ** (tuỳ chương trình) | 2025–2026 | 🟡 | [Học phí ĐH FPT 2025 chính thức — Phongvu.vn](https://phongvu.vn/cong-nghe/hoc-phi-dai-hoc-fpt-2025-chinh-thuc/) |
| Giai đoạn định hướng (tân SV K22) | **6.420.000 VNĐ** (KV ưu tiên 1) / **9.170.000 VNĐ** (khu vực khác) | 2026 | 🟡 | [jobtest.vn](https://jobtest.vn/hrblog/hoc-phi-dai-hoc-fpt) |
| Ưu đãi vùng | Đà Nẵng & Cần Thơ được **giảm 30%** so với chuẩn | 2026 | 🟡 | [jobtest.vn](https://jobtest.vn/hrblog/hoc-phi-dai-hoc-fpt) |
| Mức tăng 2025→2026 | **+2% đến +5%** tuỳ ngành và khu vực; HN/HCM tăng **2.000.000 – 3.500.000 VNĐ/kỳ** | | 🟡 | [Học phí FPT 2026 — dienthoaivui.com.vn](https://dienthoaivui.com.vn/back-to-school-hoc-phi-fpt), [Phongvu.vn](https://phongvu.vn/cong-nghe/hoc-phi-dai-hoc-fpt-2025-chinh-thuc/) |
| Dải toàn hệ thống 2026–2027 | **15.480.000 – 31.600.000 VNĐ/học kỳ** | 2026–2027 | 🟡 | [Học phí chính thức ĐH FPT 2026–2027 — VietJack](https://khoahoc.vietjack.com/tuyen-sinh/1392/hoc-phi-chinh-thuc-truong-dai-hoc-fpt-nam-2026-2027) |
| So sánh: campus TP.HCM | **46,44 – 94,8 triệu VNĐ/năm** | 2026 | 🟡 | [dienthoaivui.com.vn](https://dienthoaivui.com.vn/back-to-school-hoc-phi-fpt) |
| Bao gồm | Giáo trình, học liệu, trang thiết bị học tập | | 🟢 | [Phongvu.vn](https://phongvu.vn/cong-nghe/hoc-phi-dai-hoc-fpt-2025-chinh-thuc/) |
| Cam kết | Kế hoạch học phí **không đổi suốt khoá học** | | 🟡 | [Báo Đà Nẵng](https://baodanang.vn/hoc-phi-truong-dai-hoc-fpt-2025-2026-tai-cac-co-so-tren-ca-nuoc-3151966.html) |

### 5.3. 💰 SỨC CHI TRẢ CỦA KHÁCH HÀNG — LUẬN ĐIỂM ĐỊNH GIÁ

Tính toán 🔴 (suy luận từ số liệu ở trên):

```
Học phí chuyên ngành 1 kỳ (Đà Nẵng)   = 22.120.000 VNĐ
Một kỳ = 4 tháng ≈ 15–16 tuần
→ Chi phí học tập mỗi TUẦN            ≈ 1.383.000 VNĐ
→ Chi phí học tập mỗi NGÀY (7 ngày/tuần) ≈ 198.000 VNĐ

Giả sử 1 kỳ có ~5 môn thi cuối kỳ:
→ "Giá trị kinh tế" của 1 môn thi     ≈ 4.424.000 VNĐ
```

> **🎯 LUẬN ĐIỂM ĐỊNH GIÁ MẠNH NHẤT CHO PROPOSAL:**
>
> **Trượt 1 môn vì hỏng laptop = mất ~4,4 triệu VNĐ học phí + 1 học kỳ chậm tiến độ.**
> **Thuê laptop 1 ngày thi = 100.000 – 200.000 VNĐ.**
> **→ Tỷ lệ chi phí/rủi ro ≈ 1 : 22 đến 1 : 44.**
>
> Đây là "no-brainer purchase" — sinh viên FPT trả 22 triệu/kỳ **chắc chắn** sẵn sàng trả 150k để không mất 4,4 triệu. Đưa phép tính này vào slide định giá.

---

## PHẦN 6 — YÊU CẦU CẤU HÌNH LAPTOP

### 6.1. Yêu cầu chính thức từ trường (cho thi EOS)

| Yêu cầu | Nội dung | Nhãn |
|---|---|---|
| Hệ điều hành | **Windows** (bắt buộc); khuyến cáo **Windows 10** | 🟢 |
| MacBook | Bootcamp Windows; **KHÔNG hỗ trợ M1/M2** | 🟢 |
| Tai nghe | Có dây (jack 3.5mm) | 🟢 |
| Webcam | Cần cho ca thi từ xa | 🟡 |
| Mạng | Internet ổn định | 🟢 |
| RAM tối thiểu | **KHÔNG CÔNG BỐ** — tài liệu FPT không nêu cấu hình tối thiểu | 🔴 |

> **Nguồn:** [Hướng dẫn cài đặt phần mềm thi EOS và SEB — Helpdesk FPTU](https://it.fpt.edu.vn/cantho/huong-dan-cai-dat-phan-mem-thi-eos-seb/) · [Hướng dẫn sử dụng phần mềm thi EOS_Client — IT HCM FPT](https://it-hcm.fpt.edu.vn/articles.php?id=18) · [Video hướng dẫn sử dụng phần mềm thi](https://it-hcm.fpt.edu.vn/articles.php?news=video-huong-dan-su-dung-phan-mem-thi&id=19)

### 6.2. Cấu hình khuyến nghị chung cho SV CNTT (2025–2026)

| Thành phần | Khuyến nghị |
|---|---|
| CPU | Intel Core i5 / AMD Ryzen 5 trở lên |
| RAM | Tối thiểu **8 GB**; **16 GB** nếu đa nhiệm / lập trình chuyên sâu |
| Ổ cứng | **SSD từ 512 GB** |

> **Nguồn:** [Top laptop cho sinh viên CNTT 2025 — FPT Shop](https://fptshop.com.vn/tin-tuc/for-gamers/laptop-cho-sinh-vien-cong-nghe-thong-tin-2025-176337) · [11 laptop cho SV CNTT 2025 giá rẻ nhất — Điện Thoại Vui](https://dienthoaivui.com.vn/laptop-cho-sinh-vien-cong-nghe-thong-tin) · [Top 25 laptop cho SV CNTT — An Khang](https://www.ankhang.vn/laptop-cho-sinh-vien-cong-nghe-thong-tin.html)

> ⚠️ Đây là **khuyến nghị thị trường**, **KHÔNG phải yêu cầu chính thức của ĐH FPT**. ĐH FPT không công bố bảng cấu hình bắt buộc.

### 6.3. 🔧 SPEC ĐỀ XUẤT CHO ĐỘI LAPTOP CHO THUÊ (🔴 khuyến nghị của người nghiên cứu)

| Hạng | Cấu hình | Dùng cho | Ghi chú |
|---|---|---|---|
| **Hạng A — "Thi chuẩn"** | i5 gen 8–10 / Ryzen 5, 8GB RAM, SSD 256GB, Win 10/11, **có jack 3.5mm**, webcam, pin ≥3h | Thi EOS Client (BE, trắc nghiệm), thi tiếng Anh | Máy cũ/refurb — **vốn thấp**, đủ chạy EOS |
| **Hạng B — "Thi IT"** | i5/i7 gen 11+, 16GB RAM, SSD 512GB | Thi IT Client (Java, C#, C/C++, DB, OS), đồ án | Giá thuê cao hơn |

**Checklist bắt buộc trước khi giao máy:**
- [ ] Windows 10/11 bản quyền, đã update
- [ ] **Cài sẵn EOS Client + IT Client + SEB, đã test giải nén đúng thư mục**
- [ ] Test jack tai nghe 3.5mm hoạt động
- [ ] Test webcam + micro
- [ ] Pin sạc đầy + kèm củ sạc + dây
- [ ] Wipe sạch dữ liệu, tài khoản Windows trống (tránh vi phạm quy chế thi)
- [ ] Dán nhãn mã máy + hotline hỗ trợ

---

## PHẦN 7 — CÁC KỲ THI CHỨNG CHỈ TRÊN MÁY TÍNH TẠI ĐÀ NẴNG (MỞ RỘNG NHU CẦU)

| Chứng chỉ | Hình thức | Địa điểm tại Đà Nẵng | Lệ phí | Nhãn | Nguồn |
|---|---|---|---|---|---|
| **TOEIC (IIG Việt Nam)** | **Thi trên máy tính (CBT)** có kết nối internet tại trung tâm được uỷ quyền; **báo điểm ngay sau khi thi** | VP IIG: **19 Hoàng Văn Thụ, Hải Châu, Đà Nẵng** | **L&R:** 1.590.000 VNĐ (người đi làm) / **1.430.000 VNĐ (HSSV)**; **S&W:** 2.270.000 VNĐ. Từ **09/06/2025** có gói ưu đãi 4 kỹ năng cho SV **giảm 450.000 VNĐ** | 🟡 | [Địa điểm & thông tin đăng ký thi TOEIC tại IIG — MS Hoa](https://www.anhngumshoa.com/tin-tuc/dia-diem-thong-tin-dang-ky-thi-toeic-tai-iig-vietnam-34944.html), [Lệ phí thi TOEIC 2026 — ZIM](https://zim.vn/le-phi-thi-toeic), [IIG ra mắt gói ưu đãi TOEIC 4 kỹ năng cho sinh viên](https://iigvietnam.com/announcement-iig-vietnam-launches-special-discount-package-for-toeic-4-skill-test-only-for-students/), [Lịch thi tiếng Anh IIG](https://online.iigvietnam.com/lich-thi-tieng-anh) |
| **AWS Certified / Microsoft (Pearson VUE)** | **Thi trên máy tính tại phòng lab đạt chuẩn**, hoặc thi online tại nhà | **Có trung tâm Pearson VUE tại Đà Nẵng** (Pearson VUE có mặt ở HN, ĐN, HCM — tổng ~20 trung tâm toàn quốc) | Không tìm được giá cụ thể tại ĐN | 🟡 | [Thi chứng chỉ AWS ở đâu — CodeGym](https://codegym.vn/blog/thi-chung-chi-aws-o-dau-cach-toi-uu-hoa-chi-phi-thi-chung-chi-aws/), [Cập nhật danh sách trung tâm khảo thí Pearson VUE ở Việt Nam — Atoha](https://www.atoha.com/blogs/tin-tuc/cap-nhat-dia-diem-thi-pearson-vue), [AWS Certification Testing](https://aws.amazon.com/vi/certification/certification-prep/testing/) |
| **JLPT (tiếng Nhật)** | **Thi trên giấy** (paper-based) — ❌ **KHÔNG phải thị trường mục tiêu** | Khoa Ngôn ngữ & Văn hoá Nhật Bản, **ĐH Ngoại ngữ – ĐH Đà Nẵng, 131 Lương Nhữ Học, Cẩm Lệ, Đà Nẵng** | — | 🟡 | [Thông báo kỳ thi JLPT đợt II tháng 12/2025 — Japan Foundation](https://hn.jpf.go.jp/posts/jlpt1225-vn), [JLPT — Khoa NN&VH Nhật Bản, ĐH Đà Nẵng](https://nnvhnhatban.ufl.udn.vn/category/thong-bao/jlpt/) |
| Lịch JLPT 2025 | 2 đợt/năm: **06/07/2025** và **07/12/2025** | | | 🟢 | [Japan Foundation](https://hn.jpf.go.jp/posts/jlpt1225-vn) |
| **TOPIK (tiếng Hàn)** | ❓ **KHÔNG tìm được** thông tin địa điểm thi TOPIK tại Đà Nẵng | — | — | 🔴 | — |

### 7.1. Thi TOEIC nội bộ tại ĐH FPT
- ĐH FPT Hà Nội tổ chức **thi TOEIC định kỳ từ thứ 2 đến thứ 7 hàng tuần, trong giờ hành chính, tại 3 cơ sở**. 🟡
- Sinh viên đạt **TOEIC ≥800** được **miễn thi tiếng Anh đầu vào** FPT. 🟡
- Kỳ thi tiếng Anh đầu vào / xếp lớp của FPT **cũng thi trên phần mềm EOS**. 🟢

> **Nguồn:** [Chứng chỉ nào phù hợp để được miễn thi Tiếng Anh đầu vào FPT — PTE Magic](https://ptemagic.com.vn/chung-chi-nao-phu-hop-de-duoc-mien-thi-tieng-anh-dau-vao-fpt/) · [Hướng dẫn SV sử dụng và thi tiếng Anh xếp lớp trên EOS](https://daihoc.fpt.edu.vn/tin-tuc-chung-2/su-kien-tin-tuc-chung-2/huong-dan-sinh-vien-su-dung-va-thi-tieng-anh-xep-lop-tren-phan-mem-eos/) · [Tra cứu lịch thi tiếng Anh đầu vào khoá 20 ĐH FPT Hà Nội](https://daihoc.fpt.edu.vn/tra-cuu-lich-thi-tieng-anh-dau-vao-khoa-20-dh-fpt-ha-noi/)

**👉 Hàm ý:** Thi tiếng Anh đầu vào/xếp lớp diễn ra **ngay đầu mỗi khoá (tháng 9)** cho hàng nghìn tân sinh viên — **và cũng thi trên EOS bằng laptop cá nhân**. Tân sinh viên là nhóm rủi ro cao nhất: vừa nhập học, nhiều em chưa kịp mua laptop, hoặc mua nhầm MacBook M-series. **→ Đây là đợt cao điểm thứ 4, và là cơ hội "acquisition" khách hàng tốt nhất trong năm.**

---

## PHẦN 8 — CÁC TRƯỜNG ĐẠI HỌC KHÁC TẠI ĐÀ NẴNG (TIỀM NĂNG MỞ RỘNG)

### 8.1. Bảng tổng hợp

| Trường | Quy mô sinh viên | Chỉ tiêu 2025 | Vị trí so với Hoà Hải | Nhãn | Nguồn |
|---|---|---|---|---|---|
| **Đại học Đà Nẵng** (ĐH vùng, đa trường thành viên) | **~50.000 SV** (Wikipedia) / **60.839** (US News) | **>17.000** (tăng ~2.000 so 2024) | Đa cơ sở, chủ yếu Hải Châu/Liên Chiểu/Cẩm Lệ | 🟡 | [University of Da Nang — Wikipedia](https://en.wikipedia.org/wiki/University_of_Da_Nang), [US News — University of Danang](https://www.usnews.com/education/best-global-universities/university-of-danang-530596), [Điểm chuẩn ĐH Đà Nẵng 2025 — VnExpress](https://vnexpress.net/diem-chuan-dai-hoc-da-nang-2025-chinh-xac-nhat-4929604.html) |
| ├ **ĐH Bách khoa – ĐH Đà Nẵng (DUT)** | — | **3.900** SV | 54 Nguyễn Lương Bằng, Liên Chiểu (~15 km) | 🟢 | [Điểm chuẩn ĐH Bách khoa Đà Nẵng 2025 — VnExpress](https://vnexpress.net/diem-chuan-dai-hoc-bach-khoa-da-nang-2025-moi-nhat-4929639.html), [Tuyển sinh DUT](https://tuyensinh.dut.udn.vn/) |
| ├ **ĐH CNTT&TT Việt – Hàn (VKU)** | ~450 SV tốt nghiệp khoá 2021–2026 | **1.500** SV | Ngũ Hành Sơn (**gần Hoà Hải nhất trong nhóm UDN**) | 🟢 | [VKU thông báo tuyển sinh ĐH chính quy 2025](https://vku.udn.vn/vi/truong-dai-hoc-cong-nghe-thong-tin-va-truyen-thong-viet-han-thong-bao-tuyen-sinh-dai-hoc-chinh-quy-nam-2025-du-kien/), [VKU công bố điểm trúng tuyển 2025](https://vku.udn.vn/vi/vku-cong-bo-diem-trung-tuyen-tuyen-sinh-dai-hoc-nam-2025/) |
| ├ ĐH Kinh tế – ĐH Đà Nẵng | — | — | 71 Ngũ Hành Sơn, gần cầu Trần Thị Lý | 🟡 | [Thông tin tuyển sinh ĐH Kinh tế — ĐH Đà Nẵng](https://tuyensinhso.vn/school/dai-hoc-kinh-te-dai-hoc-da-nang.html) |
| ├ ĐH Ngoại ngữ – ĐH Đà Nẵng | 18 chuyên ngành (7 ngành CLC) | — | 131 Lương Nhữ Học, Cẩm Lệ | 🟡 | [Các trường ĐH ở Đà Nẵng — IELTS Fighter](https://ielts-fighter.com/tin-tuc/cac-truong-dai-hoc-o-da-nang_mt1641797220.html) |
| **Đại học Duy Tân** | **>20.000 SV** (ĐH, thạc sĩ, NCS); **>90 chuyên ngành** | — | Đa cơ sở, chủ yếu Hải Châu / Ngũ Hành Sơn | 🟢 | [Tổng quan về Đại học Duy Tân](https://duytan.edu.vn/gioi-thieu), [Tuyển sinh 2025 ĐH Duy Tân](https://tuyensinh2025.duytan.edu.vn) |
| **Đại học Đông Á** | — | **6.179** SV; 41 ngành tại ĐN + 16 ngành tại phân hiệu Đắk Lắk | 33 Xô Viết Nghệ Tĩnh, Hải Châu | 🟢 | [ĐH Đông Á công bố phương thức tuyển sinh 2025](https://donga.edu.vn/tuyensinh/ts-chi-tiet/dai-hoc-dong-a-cong-bo-06-phuong-thuc-tuyen-sinh-he-chinh-quy-nam-2025-37366), [Thông tin tuyển sinh ĐH Đông Á](https://tuyensinhso.vn/school/dai-hoc-dong-a.html) |
| **Greenwich Việt Nam – cơ sở Đà Nẵng** | Toàn hệ thống gần 20.000 SV (4 campus) | — | **658 Ngô Quyền, phường An Hải** (~8–10 km) | 🟡 | [Greenwich Việt Nam](https://greenwich.edu.vn/), [Greenwich Việt Nam — Wikipedia](https://vi.wikipedia.org/wiki/Greenwich_Vi%E1%BB%87t_Nam) |
| **CĐ Đại Việt Đà Nẵng** | — | **2.000** SV | Hải Châu | 🟡 | [Thông báo tuyển sinh CĐ chính quy 2025 — Đại Việt Đà Nẵng](https://daivietdanang.edu.vn/dao-tao/bai-viet/thong-bao-tuyen-sinh-cao-dang-chinh-quy-nam-2025-1037.html) |
| **Tổng số trường ĐH tại Đà Nẵng** | **17 trường đại học / cơ sở đào tạo** | — | — | 🟡 | [Full danh sách 17 trường Đại học tại Đà Nẵng — trangedu.com](https://trangedu.com/blog/dai-hoc-hoc-vien-tai-da-nang/), [Danh sách 11+ các trường ĐH ở Đà Nẵng 2025 — Tuyển Sinh Số](https://tuyensinhso.vn/khu-vuc/khu-vuc-da-nang-c11808.html) |

### 8.2. Bối cảnh cả nước
- Quy mô giáo dục đại học Việt Nam **tăng hơn 300.000 sinh viên** trong năm học 2023–2024. 🟡
  > [Quy mô giáo dục ĐH tăng hơn 300.000 sinh viên trong năm học 2023-2024 — Thanh Niên](https://thanhnien.vn/quy-mo-giao-duc-dh-tang-hon-300000-sinh-vien-trong-nam-hoc-2023-2024-185250522162830238.htm)

### 8.3. ⚠️ RÀO CẢN QUAN TRỌNG KHI MỞ RỘNG

> **Các trường công lập KHÔNG thi bằng laptop cá nhân.** Không có bằng chứng nào cho thấy ĐH Đà Nẵng, Duy Tân, Đông Á, VKU… yêu cầu sinh viên mang laptop riêng đi thi cuối kỳ. Họ chủ yếu thi giấy hoặc thi tại **phòng lab của trường**.
>
> **→ "Pain point ngày thi" là ĐẶC THÙ CỦA HỆ THỐNG FPT**, không tự động mở rộng sang trường khác.
>
> **Với các trường khác, sản phẩm phải đổi:** từ "thuê laptop đi thi" → **"thuê laptop cho đồ án / thực tập / học online / khi máy đang sửa"**. Đây là thị trường khác, cạnh tranh trực tiếp với các cửa hàng cho thuê laptop hiện hữu ở Đà Nẵng (xem Phần 9), **biên lợi nhuận thấp hơn và không có yếu tố "khẩn cấp"**.
>
> **Khuyến nghị chiến lược cho proposal:** Không vẽ TAM = toàn bộ sinh viên Đà Nẵng. Thay vào đó dùng cấu trúc TAM/SAM/SOM ở Phần 10 — trung thực và thuyết phục hơn nhiều.

---

## PHẦN 9 — ĐỐI THỦ CHO THUÊ LAPTOP TẠI ĐÀ NẴNG (BENCHMARK GIÁ)

| Nhà cung cấp | Giá công bố | Ghi chú | Nguồn |
|---|---|---|---|
| **leminhSTORE Computer** | **Từ 38.000 VNĐ/ngày** | ⭐ Nêu rõ phục vụ **"học tập, THI CỬ, thực tập"**; hỗ trợ tận nơi; thuê theo ngày/tuần/tháng | [Cho thuê laptop sinh viên giá rẻ Đà Nẵng — leminhSTORE](https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html) |
| **MIT Group** | **Từ 29.000 VNĐ/ngày** | "Cấu hình mạnh" | [Cho thuê laptop 2025 — MIT Group](https://mitgroup.vn/cho-thue-laptop/) |
| **Trương Giang** | **Từ 50.000 VNĐ/ngày** | Cho thuê laptop Đà Nẵng theo ngày | [Cho thuê laptop Đà Nẵng — Trương Giang](https://truonggiang.vn/cho-thue-laptop.html) |
| **Đình Hậu Computer** | Không công bố giá | Ưu đãi SV, **miễn phí vận chuyển + lắp đặt**; thuê theo ngày/tuần/tháng | [Dịch vụ cho thuê laptop tại Đà Nẵng — Đình Hậu](https://maytinhdinhhau.vn/dich-vu-cho-thue-laptop-tai-da-nang/) |
| **Sky Computer** | Không công bố giá | Thuê theo ngày/tháng, **có nhân viên IT hỗ trợ** | [Cho thuê máy tính laptop tại Đà Nẵng — Sky Computer](https://skycomputer.vn/dich-vu/cho-thue-may-tinh-laptop-tai-da-nang/) |
| Tổng hợp | — | Có bài "Top 7 dịch vụ cho thuê laptop Đà Nẵng uy tín, giá rẻ" → **thị trường đã có ≥7 đối thủ** | [danang.plus](https://danang.plus/thue-laptop/) |

### 9.1. 🎯 KHOẢNG TRỐNG THỊ TRƯỜNG (điểm khác biệt của ý tưởng)

Đối thủ hiện tại là **cửa hàng máy tính truyền thống ở nội thành**, bán "thuê laptop chung chung". **Không ai** trong số họ:

| Yếu tố | Đối thủ hiện tại | Ý tưởng của nhóm |
|---|---|---|
| Vị trí | Nội thành (Hải Châu, Thanh Khê) — cách Hoà Hải 8–15 km | **Ngay trong/cạnh campus** |
| Chuẩn bị máy | Máy trắng, tự cài | **Cài sẵn EOS + IT Client + SEB, đã test** |
| Thời gian giao | Giờ hành chính | **Giao trước ca thi sáng (6–7h) và ca chiều** |
| Đặt máy | Gọi điện / inbox | **Website đặt online, xem máy còn trống theo lịch thi** |
| Hiểu ngữ cảnh | Không | **Hiểu quy chế thi FPT, biết Mac M-series không thi được** |
| Giá | 29.000 – 50.000 VNĐ/ngày | Có thể định giá cao hơn (**100.000 – 200.000 VNĐ/ngày thi**) vì bán "sự chắc chắn dự thi", không bán "cái máy" |

> **⚠️ Lưu ý phản biện (giám khảo sẽ hỏi):** Giá đối thủ chỉ 29–50k/ngày. Phải giải thích được **vì sao thu 100–200k**. Câu trả lời: **không bán thời gian sử dụng máy, mà bán "bảo hiểm dự thi"** — máy đã cài sẵn phần mềm thi, giao tận phòng thi, có máy dự phòng, hỗ trợ trong giờ thi. Đối chiếu với thiệt hại 4,4 triệu VNĐ khi trượt môn (Phần 5.3).

---

## PHẦN 10 — 🎯 KHUNG TAM / SAM / SOM ĐỀ XUẤT

> **🔴 CẢNH BÁO: Toàn bộ phần này là MÔ HÌNH ƯỚC LƯỢNG của người nghiên cứu**, xây trên các số liệu nguồn ở Phần 4 và 8. Phải ghi rõ giả định trong proposal.

### 10.1. Ba tầng thị trường

```
┌──────────────────────────────────────────────────────────────┐
│ TAM — Toàn bộ SV ĐH/CĐ tại TP. Đà Nẵng                        │
│ ≈ 90.000 – 120.000 sinh viên (17 trường ĐH + các trường CĐ)   │
│ Nhu cầu: thuê laptop cho học tập/đồ án/thực tập nói chung     │
│ Cơ sở: ĐH Đà Nẵng ~50.000 + Duy Tân >20.000 + Đông Á +        │
│        FPT + Greenwich + 12 trường khác + khối CĐ             │
├──────────────────────────────────────────────────────────────┤
│ SAM — SV thi trên máy tính bằng LAPTOP CÁ NHÂN                │
│      tại cụm giáo dục FPT khu Hoà Hải / Ngũ Hành Sơn          │
│ ≈ 7.000 – 10.000 người                                        │
│ = ĐH FPT ĐN (~5.000) + FPT Polytechnic ĐN + FPT Schools ĐN    │
│   (>700 HS, cũng thi phần mềm trực tuyến)                     │
├──────────────────────────────────────────────────────────────┤
│ SOM — Thị phần thực tế đạt được trong 12–18 tháng đầu         │
│ ≈ 250 – 500 lượt thuê/năm                                     │
│ = 5–10% SV ĐH FPT ĐN, mỗi người thuê ~1 lần/năm               │
└──────────────────────────────────────────────────────────────┘
```

### 10.2. Bảng chi tiết & giả định

| Tầng | Số người | Tần suất/năm | Giá TB/lượt | Doanh thu tiềm năng/năm |
|---|---|---|---|---|
| **TAM** | 90.000 – 120.000 | — | — | Không tính (không phải thị trường phục vụ được) |
| **SAM** | 7.000 – 10.000 | 3–6 đợt thi/năm | 150.000 VNĐ | *Lý thuyết rất lớn — không dùng làm mục tiêu* |
| **SOM năm 1** | **250 – 500 lượt thuê** | — | **150.000 VNĐ/lượt** | **37,5 – 75 triệu VNĐ** 🔴 |
| **SOM năm 2** | 600 – 1.000 lượt | — | 150.000 VNĐ | 90 – 150 triệu VNĐ 🔴 |

**Các giả định phải nêu rõ trong proposal:**
1. SV ĐH FPT ĐN ≈ 5.000 (ước tính, xem 4.3)
2. Tỷ lệ SV gặp sự cố laptop trong 1 năm: **🔴 KHÔNG CÓ SỐ LIỆU** — đây là giả định thuần tuý. Đề xuất **khảo sát 100–200 SV FPT ĐN** để có số thật (xem Phần 11)
3. Giá thuê 150.000 VNĐ/ngày thi: dựa trên benchmark đối thủ 29–50k + phần bù dịch vụ chuyên biệt
4. Mỗi khách thuê trung bình 1–1,5 ngày/lượt

### 10.3. ✅ CÁCH TRÌNH BÀY TRUNG THỰC & THUYẾT PHỤC NHẤT

> Thay vì cố vẽ TAM to, hãy dùng luận điểm này:
>
> **"Chúng tôi không nhắm 120.000 sinh viên Đà Nẵng. Chúng tôi nhắm đúng ~5.000 sinh viên ĐH FPT Đà Nẵng — nhóm duy nhất ở thành phố này BẮT BUỘC phải có laptop Windows chạy được để dự thi cuối kỳ. Chỉ cần 5% trong số đó gặp sự cố một lần mỗi năm là đã có 250 lượt thuê. Đó là điểm khởi đầu đủ nhỏ để chúng tôi làm thật, và đủ rõ để chứng minh nhu cầu."**
>
> Giám khảo môn Khởi nghiệp đánh giá cao **thị trường ngách được định nghĩa sắc nét** hơn là TAM khổng lồ không có cơ sở.

---

## PHẦN 11 — 🔍 NHỮNG GÌ KHÔNG TÌM ĐƯỢC & CÁCH TỰ THU THẬP

### 11.1. Các dữ liệu KHÔNG có (không được bịa trong proposal)

| Dữ liệu thiếu | Mức độ quan trọng | Cách khắc phục |
|---|---|---|
| **Số sinh viên chính xác của ĐH FPT Đà Nẵng** | 🔴🔴🔴 Rất cao | Xin Phòng CTSV / Phòng Đào tạo campus ĐN; hoặc đếm qua số lớp × sĩ số trên FAP |
| **Lịch thi cuối kỳ cụ thể** (ngày, số ngày, số ca) của ĐH FPT ĐN | 🔴🔴🔴 Rất cao | Chụp màn hình lịch thi trên **FAP** của chính thành viên nhóm |
| **Tỷ lệ sinh viên gặp sự cố laptop ngày thi** | 🔴🔴🔴 Rất cao (là giả định cốt lõi) | **Khảo sát Google Form 100–200 SV** — đây là dữ liệu sơ cấp, giá trị hơn mọi nguồn thứ cấp |
| **Số môn thi trung bình mỗi kỳ** của SV FPT | 🔴🔴 Cao | Đếm từ lộ trình học của chính nhóm |
| Quy chế thi bằng văn bản: trường có cho mượn máy dự phòng không? | 🔴🔴 Cao | Hỏi Phòng Khảo thí campus ĐN — **nếu trường đã có máy dự phòng thì đây là rủi ro lớn cho mô hình** |
| Cấu hình tối thiểu chính thức để chạy EOS | 🔴 Trung bình | Hỏi Helpdesk IT campus ĐN |
| Chỉ tiêu tuyển sinh riêng campus Đà Nẵng | 🔴 Trung bình | Đề án tuyển sinh PDF trên website trường |
| Số SV FPT Polytechnic Đà Nẵng | 🔴 Trung bình | Liên hệ cơ sở FPT Polytechnic ĐN |
| Địa điểm thi TOPIK tại Đà Nẵng | 🟡 Thấp | Website TOPIK Việt Nam / Trung tâm Văn hoá Hàn Quốc |
| Trung tâm Pearson VUE cụ thể tại Đà Nẵng (tên, địa chỉ) | 🟡 Thấp | Tra trực tiếp trên pearsonvue.com |

### 11.2. 📋 ĐỀ XUẤT BẢNG KHẢO SÁT SƠ CẤP (nên đưa vào proposal)

Nhóm là sinh viên FPT ĐN → **lợi thế cực lớn**: có thể thu dữ liệu sơ cấp mà không tốn chi phí. Đề xuất khảo sát:

1. Bạn dùng laptop gì để thi EOS? (Windows / MacBook Intel + Bootcamp / MacBook M-series / khác)
2. Trong 12 tháng qua, laptop của bạn có gặp sự cố (hỏng, hết pin, lỗi phần mềm) **vào đúng ngày thi hoặc sát ngày thi** không? (Có/Không — **đây là con số quan trọng nhất của cả proposal**)
3. Nếu có, bạn xử lý thế nào? (mượn bạn / hoãn thi / thi lại / đi thuê / khác)
4. Nếu có dịch vụ cho thuê laptop đã cài sẵn EOS, giao tận campus, bạn sẵn sàng trả bao nhiêu cho 1 ngày thi? (dưới 100k / 100–150k / 150–200k / trên 200k)
5. Bạn biết đến dịch vụ cho thuê laptop nào ở Đà Nẵng chưa?

> Mẫu tối thiểu **n = 100**; lý tưởng **n = 200** (≈4% dân số SV ĐH FPT ĐN ước tính) → sai số ~±7% ở độ tin cậy 95%.

### 11.3. ⚠️ RỦI RO LỚN NHẤT CỦA MÔ HÌNH (phải nêu thẳng trong proposal)

1. **Trường có thể đã có máy dự phòng.** Nếu Phòng Khảo thí FPT ĐN cho mượn máy khi SV gặp sự cố → nhu cầu gần như biến mất. **PHẢI xác minh trước.**
2. **Sinh viên mượn bạn bè miễn phí** — đối thủ cạnh tranh thực sự là "bạn cùng phòng", không phải cửa hàng.
3. **Nhu cầu cực kỳ mùa vụ** — 6 đợt/năm, máy nằm không 10 tháng.
4. **Rủi ro quy chế thi** — máy lạ mang vào phòng thi có thể bị nghi gian lận. Cần xin xác nhận từ Phòng Khảo thí rằng laptop thuê được phép dùng.
5. **Vốn đọng** — mỗi laptop 6–12 triệu VNĐ; 10 máy = 60–120 triệu vốn đầu tư ban đầu.
6. **Thị trường đã có ≥7 đối thủ** tại Đà Nẵng (Phần 9), giá thấp 29–50k/ngày.

---

## PHỤ LỤC A — DANH MỤC NGUỒN ĐÃ THAM CHIẾU

### Nguồn chính thức FPT
- [Campus Đà Nẵng — Trường Đại học FPT](https://daihoc.fpt.edu.vn/da-nang/)
- [Trường Đại học FPT – Đà Nẵng (trang phân hiệu)](https://daihoc.fpt.edu.vn/truong-thanh-vien/truong-dai-hoc-fpt-da-nang/)
- [Tuyển sinh Trường Đại học FPT Đà Nẵng](https://daihoc.fpt.edu.vn/tuyen-sinh-dn/)
- [Thông tin tuyển sinh năm 2025 — Trường ĐH FPT](https://daihoc.fpt.edu.vn/thong-tin-tuyen-sinh-nam-2025/)
- [Thông tin tuyển sinh 2026 — Trường ĐH FPT](https://daihoc.fpt.edu.vn/tuyen-sinh/)
- [Quy chế tuyển sinh hệ đại học chính quy 2025](https://daihoc.fpt.edu.vn/quy-che-tuyen-sinh-2025/)
- [Quy chế đào tạo đại học chính quy](https://daihoc.fpt.edu.vn/quy-che-dao-tao-dai-hoc-chinh-quy/)
- [Lộ trình đào tạo của Trường ĐH FPT](https://daihoc.fpt.edu.vn/lo-trinh-dao-tao-cua-truong-dai-hoc-fpt/)
- [Các ngành đào tạo Trường ĐH FPT 2026](https://daihoc.fpt.edu.vn/tat-tan-tat-ve-fptu/cac-nganh-dai-hoc-fpt/)
- [Học phí đại học FPT năm 2025 — Campus Đà Nẵng](https://daihoc.fpt.edu.vn/hoc-phi-dai-hoc-fpt-nam-2025-campus-da-nang/)
- [Bản đồ Trường ĐH FPT: Toàn cảnh 5 Campus](https://daihoc.fpt.edu.vn/tat-tan-tat-ve-fptu/ban-do-truong-dai-hoc-fpt/)
- [Ký túc xá tại ĐH FPT Đà Nẵng cho tân sinh viên K19](https://daihoc.fpt.edu.vn/chua-phan-loai/ky-tuc-xa-tai-dh-fpt-da-nang-danh-cho-tan-sinh-vien-k19/)
- [Sổ tay sinh viên Trường ĐH FPT (.doc)](https://daihoc.fpt.edu.vn/en/wp-content/uploads/2017/06/So-tay-sinh-vien-FUG-2016.doc)
- [Học phí ĐH FPT Đà Nẵng và Bình Định 2023 (PDF)](https://daihoc.fpt.edu.vn/wp-content/uploads/2022/12/Hoc_phi_dai_hoc_FPT_da_nang_binh_dinh_2023.pdf)

### Nguồn về hệ thống thi EOS/SEB/FAP
- [Hướng dẫn cài đặt phần mềm thi EOS và SEB — Helpdesk FPTU](https://it.fpt.edu.vn/cantho/huong-dan-cai-dat-phan-mem-thi-eos-seb/)
- [Truy cập cổng học thuật Academic Portal (FAP)](https://it.fpt.edu.vn/cantho/huong-dan-he-thong-academic-portal-fap/)
- [Hướng dẫn sử dụng phần mềm thi EOS_Client — IT HCM](https://it-hcm.fpt.edu.vn/articles.php?id=18)
- [Video hướng dẫn sử dụng phần mềm thi](https://it-hcm.fpt.edu.vn/articles.php?news=video-huong-dan-su-dung-phan-mem-thi&id=19)
- [HD SV sử dụng và thi trên phần mềm EOS tại Trường ĐH FPT](https://daihoc.fpt.edu.vn/tin-noi-bat-muc-tin-tuc/huong-dan-sinh-vien-su-dung-va-thi-tren-phan-mem-eos-tai-truong-dai-hoc-fpt/)
- [HD SV sử dụng và thi trên phần mềm EOS tại FPTU Hà Nội](https://daihoc.fpt.edu.vn/tin-tuc-chung-2/huong-dan-sinh-vien-su-dung-va-thi-tren-phan-mem-eos-tai-fptu-ha-noi/)
- [HD SV K18 sử dụng và thi trên EOS — kỳ thi Kiểm tra Tiếng Anh](https://daihoc.fpt.edu.vn/tin-tuc-chung-2/huong-dan-sinh-vien-k18-su-dung-va-thi-tren-phan-mem-eos-ky-thi-kiem-tra-tieng-anh/)
- [HD SV sử dụng và thi tiếng Anh xếp lớp trên EOS](https://daihoc.fpt.edu.vn/tin-tuc-chung-2/su-kien-tin-tuc-chung-2/huong-dan-sinh-vien-su-dung-va-thi-tieng-anh-xep-lop-tren-phan-mem-eos/)
- [HDSV sử dụng và thi trên phần mềm EOS — hanoi.fpt.edu.vn](https://hanoi.fpt.edu.vn/huong-dan-sinh-vien-su-dung-va-thi-tren-phan-mem-eos.html)
- [HD SV cài đặt và sử dụng phần mềm thi trực tuyến — FPT PolySchool](https://polyschool.fpt.edu.vn/huong-dan-sinh-vien-cai-dat-va-su-dung-phan-mem-thi-truc-tuyen/)
- [HD làm bài thi cuối kỳ môn học trên EOS Client — Studocu](https://www.studocu.vn/vn/document/truong-dai-hoc-fpt/quan-tri-kinh-doanh/huong-dan-lam-bai-thi-cuoi-ky-tren-eos-client/27055728)
- [HD sử dụng phần mềm thi EOS Client — Studocu](https://www.studocu.vn/vn/document/truong-dai-hoc-fpt/working-in-groups/huong-dan-su-dung-eos-client/58823637)
- [HD sử dụng phần mềm thi EOS học kỳ Summer 2025 — Studocu](https://www.studocu.vn/vn/document/dai-hoc-fpt-ha-noi/english-trs3/huong-dan-su-dung-phan-mem-thi-eos-hoc-ky-summer-2025/134096866)
- [HD sử dụng phần mềm thi EOS — Studocu (bản 04/17)](https://studocu.com/vn/document/fpt-university/trs601/huong-dan-sinh-vien-su-dung-phan-mem-thi-eos/23377167)

### Nguồn về học phí & tuyển sinh
- [Học phí Trường ĐH FPT 2025-2026 tại các cơ sở trên cả nước — Báo Đà Nẵng](https://baodanang.vn/hoc-phi-truong-dai-hoc-fpt-2025-2026-tai-cac-co-so-tren-ca-nuoc-3151966.html)
- [Học phí Đại học FPT 2026–2027: Bảng giá chuẩn & Học bổng — jobtest.vn](https://jobtest.vn/hrblog/hoc-phi-dai-hoc-fpt)
- [Học phí Đại học FPT 2025 chính thức — Phongvu.vn](https://phongvu.vn/cong-nghe/hoc-phi-dai-hoc-fpt-2025-chinh-thuc/)
- [Học phí FPT 2026 — dienthoaivui.com.vn](https://dienthoaivui.com.vn/back-to-school-hoc-phi-fpt)
- [Học phí chính thức ĐH FPT 2026–2027 — VietJack](https://khoahoc.vietjack.com/tuyen-sinh/1392/hoc-phi-chinh-thuc-truong-dai-hoc-fpt-nam-2026-2027)
- [Học phí Trường ĐH FPT (Đà Nẵng) năm 2026 — VietJack](https://vietjack.com/thong-tin-tuyen-sinh/hoc-phi-truong-dai-hoc-fpt-da-nang.jsp)
- [Đề án và chỉ tiêu tuyển sinh ĐH FPT 2025 — situ.edu.vn](https://situ.edu.vn/de-an-va-chi-tieu-tuyen-sinh-dai-hoc-fpt/)
- [Tuyển sinh 2025: ĐH FPT công bố đề án 41 ngành, 4 phương thức — HOCMAI](https://huongnghiep.hocmai.vn/tuyen-sinh-2025-dai-hoc-fpt-fpt-university-cong-bo-de-an-tuyen-sinh-2025-41-nganh-4-phuong-thuc)
- [Trường ĐH FPT công bố điểm chuẩn xét tuyển 2025 — VnExpress](https://vnexpress.net/truong-dai-hoc-fpt-cong-bo-diem-chuan-xet-tuyen-2025-4915009.html)
- [Trường ĐH FPT công bố điểm chuẩn 2026 và tuyển sinh bổ sung — Nhân Dân](https://nhandan.vn/truong-dai-hoc-fpt-cong-bo-diem-chuan-nam-2026-post980791.html)
- [Điểm chuẩn tuyển sinh 2024 của Trường ĐH FPT — Cổng Xây dựng Chính sách Chính phủ](https://xaydungchinhsach.chinhphu.vn/diem-chuan-tuyen-sinh-nam-2024-cua-truong-dai-hoc-fpt-119240719124601174.htm)
- [Đề án tuyển sinh Trường ĐH FPT 2026 — tuyensinh247](https://diemthi.tuyensinh247.com/de-an-tuyen-sinh/dai-hoc-fpt-FPT.html)
- [Thông tin tuyển sinh trường ĐH FPT Đà Nẵng — tuyensinhso.vn](https://tuyensinhso.vn/school/dai-hoc-fpt-da-nang.html)

### Nguồn về quy mô FPT Education
- [Lĩnh vực giáo dục — Báo cáo thường niên FPT 2025](https://bctn2025.fpt.com/vi/phan-tich-hoat-dong-kinh-doanh/linh-vuc-giao-duc/)
- [Báo cáo thường niên FPT 2024 (PDF)](https://fpt.com/-/media/project/fpt-corporation/fpt/ir/information-disclosures/year-report/2025/april/20250402---fpt---bao-cao-thuong-nien-nam-2024.pdf)
- [Anh Lê Trường Tùng: 2026 sẽ là năm nâng tầm toàn diện Giáo dục FPT — chungta.vn](https://chungta.vn/longform/b-anh-le-truong-tung-2026-se-la-nam-nang-tam-toan-dien-giao-duc-fpt-b-1140961.html)
- [FPT đẩy mạnh phát triển hệ thống giáo dục phổ thông — fpt.com](https://fpt.com/vi/tin-tuc/tin-fpt/fpt-day-manh-phat-trien-he-thong-giao-duc-pho-thong)
- [Giáo dục — Hệ sinh thái FPT](https://fpt.com/vi/he-sinh-thai-fpt/giao-duc)
- [Lễ khai giảng 2026–2027 toàn hệ thống FPT Schools — hơn 18.000 học sinh](https://fschool.fpt.edu.vn/tung-bung-le-khai-giang-nam-hoc-2026-2027-toan-he-thong-fpt-schools-hon-18-000-hoc-sinh-cung-buoc-vao-hanh-trinh-moi/)
- [1.000 tân sinh viên ĐH FPT Đà Nẵng khai giảng năm học mới — FPT City](https://fptcity.vn/1-000-tan-sinh-vien-dai-hoc-fpt-da-nang-khai-giang-nam-hoc-moi/)
- [Lễ nhập học FSchools Đà Nẵng — hơn 700 học sinh](https://danang12-school.fpt.edu.vn/le-nhap-hoc-fschools-da-nang/)
- [FPT Schools Đà Nẵng hoàn thiện campus đầu tiên toàn quốc — chungta.vn](https://chungta.vn/nguoi-fpt/fpt-schools-da-nang-la-don-vi-dau-tien-hoan-thien-campus-tren-ca-nuoc-1136593.html)
- [FPT University — Wikipedia (EN)](https://en.wikipedia.org/wiki/FPT_University)
- [Trường Đại học FPT — Wikipedia (VI)](https://vi.wikipedia.org/wiki/Tr%C6%B0%E1%BB%9Dng_%C4%90%E1%BA%A1i_h%E1%BB%8Dc_FPT)
- [uniRank — FPT University 2026](https://www.unirank.org/vn/uni/fpt-university/)
- [FPT University, Da Nang Campus — Universitas Indonesia International Office](https://international.ui.ac.id/shortcourse-fpt/)
- [FPT University hỗ trợ 1.000 tân sinh viên 2025 "Học trước – Trả sau" — vietnam.vn](https://www.vietnam.vn/en/truong-dai-hoc-fpt-ho-tro-1-000-tan-sinh-vien-nam-2025-theo-chinh-sach-hoc-truoc-tra-sau)

### Nguồn về các trường khác tại Đà Nẵng
- [University of Da Nang — Wikipedia](https://en.wikipedia.org/wiki/University_of_Da_Nang)
- [US News — University of Danang](https://www.usnews.com/education/best-global-universities/university-of-danang-530596)
- [Điểm chuẩn Đại học Đà Nẵng 2025 — VnExpress](https://vnexpress.net/diem-chuan-dai-hoc-da-nang-2025-chinh-xac-nhat-4929604.html)
- [Điểm chuẩn ĐH Bách khoa Đà Nẵng 2025 — VnExpress](https://vnexpress.net/diem-chuan-dai-hoc-bach-khoa-da-nang-2025-moi-nhat-4929639.html)
- [Thông tin tuyển sinh 2025 các cơ sở thành viên ĐH Đà Nẵng](https://ts.udn.vn/DHCD/Chinhquy/DHTbao/13946)
- [Tổng quan về Đại học Duy Tân](https://duytan.edu.vn/gioi-thieu)
- [Tuyển sinh 2025 — Đại học Duy Tân](https://tuyensinh2025.duytan.edu.vn)
- [ĐH Đông Á công bố phương thức tuyển sinh 2025](https://donga.edu.vn/tuyensinh/ts-chi-tiet/dai-hoc-dong-a-cong-bo-06-phuong-thuc-tuyen-sinh-he-chinh-quy-nam-2025-37366)
- [VKU thông báo tuyển sinh đại học chính quy 2025](https://vku.udn.vn/vi/truong-dai-hoc-cong-nghe-thong-tin-va-truyen-thong-viet-han-thong-bao-tuyen-sinh-dai-hoc-chinh-quy-nam-2025-du-kien/)
- [VKU công bố điểm trúng tuyển tuyển sinh đại học 2025](https://vku.udn.vn/vi/vku-cong-bo-diem-trung-tuyen-tuyen-sinh-dai-hoc-nam-2025/)
- [Greenwich Việt Nam](https://greenwich.edu.vn/)
- [Greenwich Việt Nam — Wikipedia](https://vi.wikipedia.org/wiki/Greenwich_Vi%E1%BB%87t_Nam)
- [Full danh sách 17 trường Đại học tại Đà Nẵng — trangedu.com](https://trangedu.com/blog/dai-hoc-hoc-vien-tai-da-nang/)
- [Danh sách 11+ các trường Đại học ở Đà Nẵng 2025 — Tuyển Sinh Số](https://tuyensinhso.vn/khu-vuc/khu-vuc-da-nang-c11808.html)
- [Điểm chuẩn 2025 của các trường đại học ở Đà Nẵng — Dân trí](https://dantri.com.vn/giao-duc/diem-chuan-2025-cua-cac-truong-dai-hoc-o-da-nang-20250820105000026.htm)
- [Thông báo tuyển sinh Cao đẳng chính quy 2025 — CĐ Đại Việt Đà Nẵng](https://daivietdanang.edu.vn/dao-tao/bai-viet/thong-bao-tuyen-sinh-cao-dang-chinh-quy-nam-2025-1037.html)
- [Quy mô giáo dục ĐH tăng hơn 300.000 SV năm học 2023-2024 — Thanh Niên](https://thanhnien.vn/quy-mo-giao-duc-dh-tang-hon-300000-sinh-vien-trong-nam-hoc-2023-2024-185250522162830238.htm)

### Nguồn về thi chứng chỉ
- [Địa điểm & thông tin đăng ký thi TOEIC tại IIG Vietnam — MS Hoa](https://www.anhngumshoa.com/tin-tuc/dia-diem-thong-tin-dang-ky-thi-toeic-tai-iig-vietnam-34944.html)
- [Lệ phí thi TOEIC và các khoản phụ phí mới nhất 2026 — ZIM](https://zim.vn/le-phi-thi-toeic)
- [IIG Việt Nam ra mắt gói ưu đãi lệ phí thi TOEIC 4 kỹ năng cho sinh viên](https://iigvietnam.com/announcement-iig-vietnam-launches-special-discount-package-for-toeic-4-skill-test-only-for-students/)
- [Quy định ưu đãi lệ phí dự thi tiếng Anh tại IIG cho HSSV](https://iigvietnam.com/quy-dinh-ve-uu-dai-le-phi-du-thi-tieng-anh-tai-iig-viet-nam-danh-cho-hoc-sinh-sinh-vien/)
- [Lịch thi tiếng Anh — IIG Việt Nam](https://online.iigvietnam.com/lich-thi-tieng-anh)
- [Thi chứng chỉ AWS ở đâu — CodeGym](https://codegym.vn/blog/thi-chung-chi-aws-o-dau-cach-toi-uu-hoa-chi-phi-thi-chung-chi-aws/)
- [Cập nhật danh sách trung tâm khảo thí Pearson VUE ở Việt Nam — Atoha](https://www.atoha.com/blogs/tin-tuc/cap-nhat-dia-diem-thi-pearson-vue)
- [AWS Certification Testing](https://aws.amazon.com/vi/certification/certification-prep/testing/)
- [Thông báo kỳ thi JLPT đợt II tháng 12/2025 — Japan Foundation](https://hn.jpf.go.jp/posts/jlpt1225-vn)
- [JLPT — Khoa Ngôn ngữ & Văn hoá Nhật Bản, ĐH Đà Nẵng](https://nnvhnhatban.ufl.udn.vn/category/thong-bao/jlpt/)
- [Chứng chỉ nào phù hợp để được miễn thi Tiếng Anh đầu vào FPT — PTE Magic](https://ptemagic.com.vn/chung-chi-nao-phu-hop-de-duoc-mien-thi-tieng-anh-dau-vao-fpt/)

### Nguồn về cấu hình laptop & đối thủ cho thuê
- [Top laptop cho sinh viên CNTT 2025 — FPT Shop](https://fptshop.com.vn/tin-tuc/for-gamers/laptop-cho-sinh-vien-cong-nghe-thong-tin-2025-176337)
- [11 laptop cho SV CNTT 2025 giá rẻ nhất — Điện Thoại Vui](https://dienthoaivui.com.vn/laptop-cho-sinh-vien-cong-nghe-thong-tin)
- [Top 25 laptop cho SV CNTT — An Khang](https://www.ankhang.vn/laptop-cho-sinh-vien-cong-nghe-thong-tin.html)
- [Cho thuê laptop sinh viên giá rẻ Đà Nẵng — leminhSTORE](https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html)
- [Cho thuê laptop 2025 cấu hình mạnh giá chỉ từ 29.000đ — MIT Group](https://mitgroup.vn/cho-thue-laptop/)
- [Cho thuê laptop Đà Nẵng giá rẻ theo ngày từ 50K — Trương Giang](https://truonggiang.vn/cho-thue-laptop.html)
- [Dịch vụ cho thuê laptop tại Đà Nẵng — Đình Hậu Computer](https://maytinhdinhhau.vn/dich-vu-cho-thue-laptop-tai-da-nang/)
- [Dịch vụ cho thuê máy tính laptop tại Đà Nẵng — Sky Computer](https://skycomputer.vn/dich-vu/cho-thue-may-tinh-laptop-tai-da-nang/)
- [Top 7 dịch vụ cho thuê laptop Đà Nẵng uy tín, giá rẻ — danang.plus](https://danang.plus/thue-laptop/)
- [Địa điểm cho thuê laptop tại Đà Nẵng giá rẻ — thuelaptop.com.vn](https://thuelaptop.com.vn/dia-diem-cho-thue-laptop-tai-da-nang-gia-re.html)

### Nguồn về địa giới hành chính
- [Phường Hòa Hải quận Ngũ Hành Sơn cũ đổi tên thành gì sau sáp nhập — Thư Viện Pháp Luật](https://thuvienphapluat.vn/phap-luat/phuong-hoa-hai-quan-ngu-hanh-son-cu-doi-ten-thanh-gi-sau-sap-nhap-phuong-hoa-hai-da-nang-cu-sap-nha-532300-234324.html)
- [Quận Ngũ Hành Sơn TP Đà Nẵng đổi thành gì sau sáp nhập 2025 — Thư Viện Pháp Luật](https://thuvienphapluat.vn/hoi-dap-phap-luat/quan-ngu-hanh-son-tp-da-nang-doi-thanh-gi-sau-sap-nhap-2025-138064839.html)
- [Đà Nẵng: Còn 16 đơn vị hành chính cấp xã sau sắp xếp — Báo Chính phủ](https://baochinhphu.vn/da-nang-con-16-don-vi-hanh-chinh-cap-xa-sau-sap-xep-102250423101211946.htm)
- [TP Đà Nẵng sau sắp xếp có 16 đơn vị hành chính cấp xã — Cổng TTĐT Đà Nẵng](https://danang.gov.vn/en/w/thanh-pho-da-nang-sau-sap-xep-co-16-on-vi-hanh-chinh-cap-xa)
- [FPT City Đà Nẵng — Vị trí & tiện ích](https://fptcity.vn/vi-tri/)

---

## PHỤ LỤC B — TÓM TẮT 10 CON SỐ QUAN TRỌNG NHẤT

| # | Con số | Giá trị | Nhãn | Dùng ở đâu trong proposal |
|---|---|---|---|---|
| 1 | Học phí chuyên ngành ĐH FPT Đà Nẵng | **22.120.000 VNĐ/học kỳ** | 🟢 | Sức chi trả khách hàng; phép tính "1 môn thi = 4,4 triệu" |
| 2 | Số học kỳ/năm | **3 kỳ** (Fall/Spring/Summer), mỗi kỳ **4 tháng / 15–16 tuần** | 🟢 | Mô hình mùa vụ doanh thu |
| 3 | OS bắt buộc để thi EOS | **Windows** (khuyến cáo Win 10); **không hỗ trợ Mac M1/M2** | 🟢 | Chứng minh pain point cốt lõi |
| 4 | Chỉ tiêu tuyển sinh ĐH FPT 2025 toàn quốc | **13.677 SV** | 🟢 | Cơ sở ước lượng SV campus ĐN |
| 5 | Tổng SV ĐH FPT toàn hệ thống | **~30.000** (2024) | 🟡 | Bối cảnh quy mô |
| 6 | **SV ĐH FPT Đà Nẵng (ước tính)** | **~5.000 (4.500–6.000)** | 🔴 | **SOM — con số cốt lõi, PHẢI ghi "ước tính"** |
| 7 | Diện tích campus ĐH FPT ĐN | **5,1 ha**, khởi công 2018 | 🟢 | Mô tả địa bàn |
| 8 | Giá đối thủ cho thuê laptop tại ĐN | **29.000 – 50.000 VNĐ/ngày** | 🟢 | Benchmark định giá |
| 9 | Lệ phí thi TOEIC IIG cho HSSV (L&R) | **1.430.000 VNĐ** | 🟡 | Thị trường mở rộng |
| 10 | ĐH Duy Tân / ĐH Đà Nẵng | **>20.000 / ~50.000 SV** | 🟡 | TAM mở rộng |

---

*Tài liệu lập ngày 14/09/2026. Mọi số gắn nhãn 🔴 là ước lượng, phải ghi rõ trong proposal. Mọi số gắn nhãn 🟡 nên được mở URL gốc kiểm chứng lại trước khi nộp.*
