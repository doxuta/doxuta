# 16 — QUY CHẾ THI & RỦI RO NGÀY THI TẠI ĐẠI HỌC FPT
### Cơ sở chứng minh vấn đề (problem validation) và thiết kế Cam kết dịch vụ (SLA)

> **Tài liệu nghiên cứu thô** phục vụ proposal khởi nghiệp *"Website cho thuê laptop đi thi"* — Trường Đại học FPT Đà Nẵng, phường Ngũ Hành Sơn (Hoà Hải cũ), TP. Đà Nẵng.
> **Ngày lập:** 14/09/2026. Ưu tiên dữ liệu 2024–2026.
> **Quy mô mô hình:** 15–40 laptop.

---

## ⚠️ CẢNH BÁO PHƯƠNG PHÁP — BẮT BUỘC ĐỌC TRƯỚC KHI DÙNG SỐ LIỆU

Có **hai giới hạn công cụ** ảnh hưởng trực tiếp đến độ tin cậy của tài liệu này. Phải nêu rõ trong phần "Phương pháp nghiên cứu" của proposal.

### Giới hạn 1 — Không mở được trang gốc
Công cụ tải trang web trực tiếp (WebFetch / curl) **bị chặn hoàn toàn** bởi chính sách egress của tổ chức (`EGRESS_BLOCKED`, `CONNECT tunnel failed, response 403`). Các domain đã thử và bị chặn gồm: `daihoc.fpt.edu.vn`, `it.fpt.edu.vn`, `it-hcm.fpt.edu.vn`, `studocu.vn`, `vi.wikipedia.org`, `vnexpress.net`.

**Hệ quả:** toàn bộ số liệu là **nội dung trích xuất từ tiêu đề + đoạn trích (snippet) của công cụ tìm kiếm**, kèm **URL thật**, nhưng **không mở và đọc được trang gốc để xác minh từng con số**.

### Giới hạn 2 — Hết hạn mức tìm kiếm trong phiên này
Tại thời điểm chạy nhiệm vụ số 16, phiên làm việc **đã dùng hết 200/200 lượt WebSearch**. Vì vậy tài liệu này **KHÔNG phát sinh tìm kiếm mới**, mà là bản **tổng hợp – tái cấu trúc – phân tích chuyên sâu** trên kho dữ liệu đã thu thập và xác minh ở các nhiệm vụ trước, cụ thể:

| Tệp nguồn nội bộ | Nội dung khai thác |
|---|---|
| `03-fpt-da-nang-boi-canh.md` | EOS/SEB, quy chế thi, học phí, lịch học, quy mô SV, trường khác, thi chứng chỉ |
| `08-bao-hiem-rui-ro.md` | Ma trận rủi ro, SLA sửa chữa tại Đà Nẵng, điều khoản hợp đồng |
| `10-campus-laptop-loan.md` | Quy trình mượn laptop nội bộ của ĐH FPT (bằng chứng nhu cầu mạnh nhất) |

**→ Mọi ô ghi "KHÔNG TÌM ĐƯỢC" trong tài liệu này nghĩa là: chưa tìm được trong các phiên tìm kiếm trước, VÀ chưa thể tìm bổ sung trong phiên này.** Phần 10 liệt kê đầy đủ và đề xuất cách nhóm tự thu thập.

### Thang nhãn độ tin cậy dùng xuyên suốt

| Nhãn | Ý nghĩa | Cách dùng trong proposal |
|---|---|---|
| 🟢 | Xuất hiện ở **≥2 nguồn độc lập**, nhất quán | Dùng trực tiếp, ghi nguồn |
| 🟡 | Từ **1 nguồn**, qua snippet, chưa mở trang gốc | Dùng được nhưng **phải mở URL kiểm chứng lại** trước khi nộp |
| 🔴 | **Ước lượng / suy luận của người nghiên cứu** | **BẮT BUỘC ghi rõ "ước tính của nhóm"** |
| ⚫ | **Không có dữ liệu** — chỉ nêu giả thuyết | **Tuyệt đối không đưa số vào proposal** |

---

# PHẦN 1 — PHẦN MỀM THI EOS (EXAM ONLINE SYSTEM)

## 1.1. EOS là gì và vì sao nó tạo ra thị trường

**EOS (Exam Online System)** là hệ thống thi trực tuyến của Trường Đại học FPT. Điểm mấu chốt tạo nên toàn bộ cơ hội kinh doanh:

> **Sinh viên ĐH FPT dự thi cuối kỳ bằng LAPTOP CÁ NHÂN của chính mình. Nhà trường KHÔNG cấp máy cho kỳ thi cuối kỳ.**

Đây không phải "laptop là công cụ học tập tuỳ chọn" — mà **laptop là THIẾT BỊ DỰ THI BẮT BUỘC**, tương đương thẻ dự thi. Không có máy chạy được EOS vào đúng buổi thi = **không thể dự thi**.

## 1.2. Yêu cầu kỹ thuật chính thức

| # | Yêu cầu | Nội dung | Nhãn | Nguồn |
|---|---|---|---|---|
| 1 | **Hệ điều hành** | **BẮT BUỘC Windows**. Khuyến cáo **Windows 10** để tương thích tốt với phần mềm thi | 🟢 | [Hướng dẫn cài đặt phần mềm thi EOS và SEB — Helpdesk FPTU](https://it.fpt.edu.vn/cantho/huong-dan-cai-dat-phan-mem-thi-eos-seb/) |
| 2 | **MacBook** | **Bắt buộc cài Windows qua Bootcamp**. **KHÔNG hỗ trợ Mac chip M1, M2** | 🟢 | [Helpdesk FPTU](https://it.fpt.edu.vn/cantho/huong-dan-cai-dat-phan-mem-thi-eos-seb/) · [HD SV sử dụng và thi trên phần mềm EOS tại Trường ĐH FPT](https://daihoc.fpt.edu.vn/tin-noi-bat-muc-tin-tuc/huong-dan-sinh-vien-su-dung-va-thi-tren-phan-mem-eos-tai-truong-dai-hoc-fpt/) |
| 3 | **Phần mềm phụ trợ** | **SEB (Safe Exam Browser)** cài kèm EOS | 🟢 | [Helpdesk FPTU](https://it.fpt.edu.vn/cantho/huong-dan-cai-dat-phan-mem-thi-eos-seb/) |
| 4 | **Mạng** | Kết nối internet **ổn định** — tài liệu trường mô tả là *"cực kỳ quan trọng"* | 🟢 | [HD SV sử dụng và thi trên phần mềm EOS](https://daihoc.fpt.edu.vn/tin-noi-bat-muc-tin-tuc/huong-dan-sinh-vien-su-dung-va-thi-tren-phan-mem-eos-tai-truong-dai-hoc-fpt/) |
| 5 | **Tai nghe** | **Tai nghe CÓ DÂY** bắt buộc cho phần thi Listening | 🟢 | [HD SV K18 thi EOS — kỳ thi Kiểm tra Tiếng Anh](https://daihoc.fpt.edu.vn/tin-tuc-chung-2/huong-dan-sinh-vien-k18-su-dung-va-thi-tren-phan-mem-eos-ky-thi-kiem-tra-tieng-anh/) |
| 6 | **Giấy tờ** | Thẻ sinh viên / CCCD hợp lệ để xác minh danh tính | 🟢 | [HD SV thi tiếng Anh xếp lớp trên EOS](https://daihoc.fpt.edu.vn/tin-tuc-chung-2/su-kien-tin-tuc-chung-2/huong-dan-sinh-vien-su-dung-va-thi-tieng-anh-xep-lop-tren-phan-mem-eos/) |
| 7 | **Màn hình** | **Chỉ được dùng 01 màn hình** khi thi | 🟡 | [HD SV sử dụng và thi trên phần mềm EOS](https://daihoc.fpt.edu.vn/tin-noi-bat-muc-tin-tuc/huong-dan-sinh-vien-su-dung-va-thi-tren-phan-mem-eos-tai-truong-dai-hoc-fpt/) |
| 8 | **Webcam (ca thi từ xa)** | Camera phải thấy rõ mặt và không gian xung quanh; Phòng Khảo thí gửi link Google Meet trước ngày thi | 🟡 | [HD làm bài thi cuối kỳ trên EOS Client — Studocu](https://www.studocu.vn/vn/document/truong-dai-hoc-fpt/quan-tri-kinh-doanh/huong-dan-lam-bai-thi-cuoi-ky-tren-eos-client/27055728) |
| 9 | **RAM / CPU / ổ cứng tối thiểu** | ⚫ **KHÔNG CÔNG BỐ** — không tìm được tài liệu nào của ĐH FPT nêu cấu hình tối thiểu bằng số | ⚫ | — (xem Phần 10) |

> **⚠️ Điểm cần chú ý cho proposal:** Yêu cầu số 9 là **lỗ hổng dữ liệu**. Đừng viết "EOS yêu cầu tối thiểu 4GB RAM" — **không có nguồn nào nói vậy**. Cách viết đúng: *"Nhà trường không công bố cấu hình tối thiểu; nhóm chọn spec dự phòng cao hơn mặt bằng để loại trừ rủi ro."*

## 1.3. Hai biến thể phần mềm thi — ảnh hưởng trực tiếp đến cơ cấu đội máy

| Phần mềm | Dùng cho môn nào | Hàm ý cấu hình máy | Nhãn |
|---|---|---|---|
| **EOS Client** | Business English (BE) và các môn **trắc nghiệm** chung | Máy nhẹ, cấu hình phổ thông là đủ | 🟡 |
| **IT Client** | **Java, C#, C/C++, Computer Network, Operating System, Introduction to Database** | Cần **RAM cao hơn** (biên dịch, chạy IDE/DBMS), ổ SSD nhanh | 🟡 |

> **Nguồn:** [HD sử dụng phần mềm thi EOS — Studocu](https://studocu.com/vn/document/fpt-university/trs601/huong-dan-sinh-vien-su-dung-phan-mem-thi-eos/23377167) · [HD sử dụng phần mềm thi EOS Client — Studocu](https://www.studocu.vn/vn/document/truong-dai-hoc-fpt/working-in-groups/huong-dan-su-dung-eos-client/58823637) · [HD sử dụng phần mềm thi EOS học kỳ SUMMER 2025 — Studocu](https://www.studocu.vn/vn/document/dai-hoc-fpt-ha-noi/english-trs3/huong-dan-su-dung-phan-mem-thi-eos-hoc-ky-summer-2025/134096866)

**👉 Hàm ý thiết kế đội máy:** phải chia **2 hạng máy**, không mua đồng loạt 1 loại. Chi tiết ở Phần 9.4.

## 1.4. ⭐ CƠ CHẾ KỸ THUẬT — VÌ SAO LAPTOP LÀ "ĐIỂM CHẾT ĐƠN LẺ" (single point of failure)

Luồng hoạt động của EOS theo mô tả trong tài liệu hướng dẫn của trường:

```
   Server trường
        │
        │  (1) tải đề thi xuống
        ▼
 ┌──────────────────────────────────┐
 │  LAPTOP CÁ NHÂN CỦA SINH VIÊN    │
 │                                  │
 │  (2) giải nén phần mềm thi       │
 │      → ĐÚNG thư mục              │
 │  (3) làm bài (offline)           │
 │  (4) bài lưu thành file .dat     │
 │      TRÊN Ổ CỨNG MÁY SINH VIÊN   │
 └──────────────────────────────────┘
        │
        │  (5) nộp bài lên server
        ▼
   Server trường
```

**Ba rủi ro do chính tài liệu hướng dẫn của trường cảnh báo:**

| # | Cảnh báo | Hệ quả | Nhãn |
|---|---|---|---|
| 1 | Bài thi **chỉ tồn tại trong thư mục đã giải nén trên máy sinh viên**. Nếu **không giải nén đúng** phần mềm thi trước khi thi → gặp lỗi và **MẤT BÀI THI** | Mất trắng bài đã làm | 🟡 |
| 2 | Khi máy gặp lỗi trong lúc thi, sinh viên **phải báo ngay giám thị** để được hướng dẫn | Không tự xử lý được | 🟢 |
| 3 | Quy trình xử lý sự cố phổ biến: **giữ nút nguồn 10 giây** để tắt hẳn máy rồi khởi động lại | Mất thời gian làm bài; rủi ro mất dữ liệu chưa lưu | 🟡 |

> **Nguồn:** [HD SV sử dụng và thi trên phần mềm EOS tại FPTU Hà Nội](https://daihoc.fpt.edu.vn/tin-tuc-chung-2/huong-dan-sinh-vien-su-dung-va-thi-tren-phan-mem-eos-tai-fptu-ha-noi/) · [HDSV sử dụng và thi trên phần mềm EOS — hanoi.fpt.edu.vn](https://hanoi.fpt.edu.vn/huong-dan-sinh-vien-su-dung-va-thi-tren-phan-mem-eos.html) · Hỗ trợ Khảo thí (số điện thoại nêu trên trang FPTU HN): **02462597749**

### 🎯 Luận điểm cốt lõi rút ra (đưa nguyên văn vào slide "Vấn đề")

> Vì bài thi **nằm vật lý trên ổ cứng máy sinh viên** chứ không nằm trên đám mây, **hỏng máy giữa giờ thi không chỉ là mất thiết bị — mà là mất bài thi**. Không có cơ chế "đăng nhập máy khác học tiếp". Đây là điều khác biệt căn bản so với thi trên trình duyệt web thông thường, và là lý do dịch vụ **thay máy trong vòng 60 phút** có giá trị thật.

## 1.5. Bảy kịch bản khiến sinh viên mất kỳ thi (danh mục nhu cầu)

| # | Kịch bản | Nhóm nguyên nhân | Có thể phòng trước? |
|---|---|---|---|
| 1 | Laptop hỏng đột ngột (màn hình, bàn phím, ổ cứng, mainboard) sát/đúng ngày thi | Phần cứng | Không |
| 2 | Pin chai + hỏng sạc, phòng thi không đủ ổ cắm | Phần cứng | Một phần |
| 3 | **MacBook chip M1/M2/M3** — không cài được Bootcamp → **không chạy được EOS** | Cấu trúc thiết bị | **Có — biết trước từ đầu khoá** |
| 4 | Máy Windows cấu hình yếu / lỗi hệ điều hành → không cài được SEB | Phần mềm | Một phần |
| 5 | Quên mang máy / mang nhầm sạc | Con người | Không |
| 6 | Máy đang bảo hành/sửa chữa đúng tuần thi | Lịch trình | Một phần |
| 7 | Laptop không có **jack tai nghe 3.5mm** → không thi được phần Listening | Cấu trúc thiết bị | **Có — biết trước** |

> **👉 Phân khúc khách hàng suy ra:** kịch bản 1, 2, 5, 6 là **cầu khẩn cấp, không dự đoán được** (thuê gấp, giá cao, biên lợi nhuận tốt). Kịch bản 3 và 7 là **cầu có kế hoạch, lặp lại đều mỗi kỳ** (thuê định kỳ, có thể bán gói theo kỳ). **Nhóm khách "Mac M-series" là nhóm giá trị vòng đời (LTV) cao nhất** vì họ sẽ cần thuê **mọi kỳ thi trong suốt 4 năm học** — không phải một lần.

---

# PHẦN 2 — SAFE EXAM BROWSER (SEB)

## 2.1. Những gì ĐÃ xác minh được

| Nội dung | Nhãn | Nguồn |
|---|---|---|
| SEB (Safe Exam Browser) **được cài kèm EOS** tại ĐH FPT; trường có bài hướng dẫn cài đặt riêng gộp chung "EOS và SEB" | 🟢 | [Hướng dẫn cài đặt phần mềm thi EOS và SEB — Helpdesk FPTU](https://it.fpt.edu.vn/cantho/huong-dan-cai-dat-phan-mem-thi-eos-seb/) |
| Việc cài SEB gắn với yêu cầu **Windows** (cùng bài hướng dẫn nêu bắt buộc Windows, không hỗ trợ Mac M1/M2) | 🟢 | như trên |
| ĐH FPT có kênh hướng dẫn phần mềm thi riêng ở nhiều campus (Cần Thơ, TP.HCM, Hà Nội) — cho thấy đây là quy trình chuẩn toàn hệ thống | 🟢 | [IT HCM — HD sử dụng phần mềm thi EOS_Client](https://it-hcm.fpt.edu.vn/articles.php?id=18) · [Video hướng dẫn sử dụng phần mềm thi](https://it-hcm.fpt.edu.vn/articles.php?news=video-huong-dan-su-dung-phan-mem-thi&id=19) · [FPT PolySchool — HD cài đặt & sử dụng phần mềm thi trực tuyến](https://polyschool.fpt.edu.vn/huong-dan-sinh-vien-cai-dat-va-su-dung-phan-mem-thi-truc-tuyen/) |

## 2.2. ⚫ Những gì CHƯA xác minh được — và tuyệt đối không được bịa

Nhiệm vụ yêu cầu làm rõ **phiên bản SEB dùng tại FPT** và **SEB có chặn máy ảo (VM/Parallels) hay không**. Kết quả trung thực:

| Câu hỏi | Trạng thái | Ghi chú |
|---|---|---|
| **Phiên bản SEB cụ thể** ĐH FPT đang dùng (2.x / 3.x) | ⚫ **KHÔNG XÁC MINH ĐƯỢC** | Không snippet nào nêu số phiên bản |
| **SEB có chặn chạy trong máy ảo (VMware/VirtualBox/Parallels) không** | ⚫ **KHÔNG XÁC MINH ĐƯỢC TRONG PHIÊN NÀY** | Xem cảnh báo bên dưới |
| Danh sách **mã lỗi SEB** thường gặp tại FPT | ⚫ **KHÔNG TÌM ĐƯỢC** | Không có trang tổng hợp lỗi công khai |
| Yêu cầu phần cứng tối thiểu của SEB | ⚫ **KHÔNG TÌM ĐƯỢC** | — |

> ### 🚨 CẢNH BÁO TRUNG THỰC VỀ CÂU HỎI "SEB CHẶN MÁY ẢO"
>
> Đề bài nêu giả định *"SEB thường CHẶN máy ảo"*. Đây là **hiểu biết phổ biến trong giới kỹ thuật**, nhưng trong phiên nghiên cứu này **tôi KHÔNG tìm được nguồn có URL thật để chứng minh**, và **không thể tìm bổ sung vì đã hết hạn mức tìm kiếm**.
>
> **→ Trong proposal, KHÔNG được viết "SEB chặn máy ảo" như một sự thật đã kiểm chứng.**
>
> **Cách viết an toàn và vẫn đủ mạnh:**
> *"Giải pháp thay thế bằng máy ảo Windows trên MacBook M-series là không khả thi trong thực tế: (a) tài liệu chính thức của ĐH FPT chỉ chấp nhận Bootcamp và ghi rõ không hỗ trợ chip M1/M2 [nguồn]; (b) phần mềm giám sát thi nói chung được thiết kế để phát hiện môi trường ảo hoá — nhóm sẽ kiểm chứng điểm này trực tiếp với Phòng IT campus Đà Nẵng trước khi triển khai."*
>
> **Cách nhóm tự kiểm chứng (rẻ, nhanh, và rất "ăn điểm" nếu đưa vào phụ lục):**
> 1. Mượn 1 MacBook M-series, cài Parallels + Windows ARM, thử cài SEB → **quay video kết quả**. Đây là **dữ liệu sơ cấp**, giá trị hơn mọi trích dẫn.
> 2. Gửi 1 email hỏi Phòng IT / Khảo thí campus Đà Nẵng, chụp màn hình trả lời đưa vào phụ lục.
> 3. Mở trang chủ dự án SEB và đọc mục yêu cầu hệ thống (nhóm làm được, tôi thì bị chặn egress).

## 2.3. 🔴 Danh mục lỗi phần mềm thi phải xử lý trước khi giao máy (suy luận kỹ thuật của người nghiên cứu)

> ⚠️ Bảng này là **thiết kế vận hành của nhóm nghiên cứu**, KHÔNG phải danh sách lỗi do ĐH FPT công bố. Trình bày trong proposal như **"quy trình kiểm soát chất lượng do nhóm tự xây"**, không như "lỗi trường ghi nhận".

| # | Lỗi tiềm ẩn | Hậu quả với sinh viên | Biện pháp trong Golden Image |
|---|---|---|---|
| 1 | **Windows Update tự chạy giữa giờ thi** → máy restart | **Mất bài thi** | Tắt/hoãn Windows Update; đặt Active Hours; khoá dịch vụ `wuauserv` trên bản Pro |
| 2 | **SEB không khởi động / lỗi file cấu hình** | Không vào được ca thi | Cài sẵn + **test SEB trước MỖI lượt giao**; lưu file cấu hình chuẩn |
| 3 | **Phần mềm diệt virus bên thứ ba chặn SEB** | SEB bị tắt giữa chừng | Gỡ sạch AV bên thứ ba; chỉ dùng Windows Defender + ngoại lệ cho SEB |
| 4 | **Máy tự ngủ / sleep giữa giờ thi** | Mất kết nối, SEB thoát | Power Plan = High Performance, **không bao giờ sleep**; tắt Fast Startup |
| 5 | **Hết pin giữa giờ thi** | Mất bài | Bắt buộc giao kèm sạc; kiểm tra **battery health > 70%**; dán nhãn *"CẮM SẠC KHI THI"* |
| 6 | **Lỗi driver Wi-Fi → không nộp được bài** | Không nộp bài | Test kết nối Wi-Fi trường trước khi giao |
| 7 | **Giải nén phần mềm thi sai thư mục** | **Mất bài thi** (rủi ro số 1 mục 1.4) | Giao máy **đã giải nén sẵn đúng vị trí**, hướng dẫn dán trên máy |
| 8 | **Không có jack 3.5mm** → không thi Listening | Mất điểm kỹ năng Nghe | Chỉ mua máy **có jack 3.5mm**; kèm sẵn tai nghe có dây |

> **👉 Đây chính là "hào cạnh tranh" (moat) của mô hình.** 8 mục trên là kiến thức vận hành mà **không cửa hàng cho thuê laptop chung chung nào ở Đà Nẵng có**. Nó biến sản phẩm từ *"cho thuê cái máy"* thành *"bảo đảm bạn thi được"*.

---

# PHẦN 3 — QUY CHẾ THI ĐẠI HỌC FPT & HẬU QUẢ KHI KHÔNG DỰ THI ĐƯỢC

## 3.1. Những gì đã xác minh

| Quy định | Nội dung | Nhãn | Nguồn |
|---|---|---|---|
| **Số lần thi** | Sinh viên được thi **tối đa 2 lần** theo lịch của trường. **Điểm lần 1 là điểm chính thức**; nếu không đạt thì dùng điểm lần 2 | 🟡 | [Sổ tay sinh viên Trường ĐH FPT (.doc)](https://daihoc.fpt.edu.vn/en/wp-content/uploads/2017/06/So-tay-sinh-vien-FUG-2016.doc) |
| **Đăng ký thi lại cải thiện** | Phải nộp đơn **trước 12 giờ** so với giờ thi lại | 🟡 | [FAP Mobile App Guide — Studocu](https://www.studocu.vn/vn/document/truong-dai-hoc-fpt/code-vhdl/fap-mobile-app-guide-procedures-important-notices/156254239) |
| **Tra cứu lịch thi** | Qua mục **"Xem lịch thi"** trên **FAP – FPT Academic Portal** (`fap.fpt.edu.vn`) | 🟢 | [Truy cập cổng học thuật Academic Portal (FAP) — Helpdesk FPTU](https://it.fpt.edu.vn/cantho/huong-dan-he-thong-academic-portal-fap/) |
| **Chế độ đào tạo** | Theo **tín chỉ**; có học phần tự chọn và học phần điều kiện | 🟢 | [Quy chế đào tạo đại học chính quy — ĐH FPT](https://daihoc.fpt.edu.vn/quy-che-dao-tao-dai-hoc-chinh-quy/) |

> **⚠️ Vấn đề về độ mới của nguồn:** quy định "thi tối đa 2 lần" đến từ **Sổ tay sinh viên bản 2016** (nhìn đường dẫn `/2017/06/...FUG-2016.doc`). **Đã 10 năm.** Quy chế có thể đã thay đổi. **Bắt buộc xin bản Sổ tay sinh viên mới nhất từ Phòng CTSV campus Đà Nẵng.**

## 3.2. ⚫ NHỮNG GÌ KHÔNG TÌM ĐƯỢC — và đây là lỗ hổng nghiêm trọng nhất của tài liệu

Nhiệm vụ yêu cầu làm rõ hậu quả khi vắng thi. Trung thực:

| Câu hỏi cần trả lời | Trạng thái | Mức độ quan trọng với proposal |
|---|---|---|
| Vắng thi không phép bị **điểm 0** hay bị **cấm thi**? | ⚫ **KHÔNG TÌM ĐƯỢC văn bản** | 🔴🔴🔴 Rất cao |
| Có được **thi bù** (make-up exam) không? Điều kiện gì? | ⚫ **KHÔNG TÌM ĐƯỢC** | 🔴🔴🔴 Rất cao |
| **Thủ tục xin hoãn thi / thi bù** vì lý do bất khả kháng (hỏng máy có được tính là lý do chính đáng không?) | ⚫ **KHÔNG TÌM ĐƯỢC** | 🔴🔴🔴 Rất cao |
| **PHÍ HỌC LẠI 1 môn** (VNĐ/môn) tại ĐH FPT 2025–2026 | ⚫ **KHÔNG TÌM ĐƯỢC SỐ NÀO** | 🔴🔴🔴 **Rất cao — đây là con số thiệt hại chính** |
| Trượt môn có bị **kéo dài thời gian tốt nghiệp** không, kéo dài bao lâu | ⚫ **KHÔNG TÌM ĐƯỢC** | 🔴🔴 Cao |

> ### 🚨 CẢNH BÁO ĐẶC BIỆT VỀ "PHÍ HỌC LẠI"
>
> Đề bài kỳ vọng có con số **VNĐ/môn học lại** để chứng minh thiệt hại. **Tôi KHÔNG tìm được con số này, và không được phép bịa.**
>
> **KHÔNG viết trong proposal:** *"Học lại 1 môn tại FPT tốn X triệu đồng"* — trừ khi nhóm tự tra được và dẫn nguồn.
>
> **Thay vào đó, dùng cách tính THAY THẾ đã có nguồn chắc chắn** (Phần 4.2) — cách này thậm chí thuyết phục hơn vì nó dựa trên học phí công bố công khai, không phải bảng phí nội bộ.
>
> **Cách nhóm tự lấy số thật (rất dễ, nhóm là sinh viên FPT):**
> 1. Đăng nhập **FAP → mục Tuition / Học phí** → chụp màn hình bảng phí học lại. **Đây là bằng chứng sơ cấp mạnh nhất có thể có.**
> 2. Hỏi Phòng Tài chính / Phòng Đào tạo campus Đà Nẵng, xin email trả lời.
> 3. Hỏi 5–10 sinh viên khoá trên đã từng học lại.

## 3.3. 🔑 BẰNG CHỨNG NỘI BỘ MẠNH NHẤT: ĐH FPT ĐÃ CÓ HỆ THỐNG "MƯỢN LAPTOP ĐỂ ĐI THI"

Đây là **phát hiện có sức nặng nhất trong toàn bộ nghiên cứu** cho phần chứng minh vấn đề.

**Nguồn:** [it-hcm.fpt.edu.vn — "Hướng dẫn mượn laptop của sinh viên trong trường"](https://it-hcm.fpt.edu.vn/articles.php?news=huong-dan-muon-laptop-cua-sinh-vien-trong-truong&id=56) (Phòng IT, ĐH FPT campus TP.HCM) 🟡

| Yếu tố | Chi tiết |
|---|---|
| **Bản chất** | Sinh viên mượn laptop **của SINH VIÊN KHÁC** trong trường, **"để dùng hoặc ĐI THI"** — peer-to-peer, **KHÔNG phải trường cho mượn máy của trường** |
| **Thời gian mượn tối thiểu** | **60 phút** |
| **Hệ thống** | Website IT campus, đăng nhập bằng **tài khoản nội bộ (tài khoản WiFi)**, chọn **"ĐK Mượn máy"** trên Dashboard |
| **Thao tác** | Nhập **MSSV của chủ máy cho mượn** |
| **Xác nhận** | **Chủ máy phải đăng nhập hệ thống xác nhận**; mỗi lần mượn/trả đều thao tác trên hệ thống |
| **Lưu ý phòng thi** | Dù mượn máy người khác, SV **phải ngắt WiFi_Student và WiFi_Exam, đăng nhập lại bằng tài khoản WiFi của CHÍNH MÌNH** |

### Vì sao đây là bằng chứng mạnh nhất

| # | Luận điểm | Diễn giải |
|---|---|---|
| 1 | **Nhu cầu là THẬT và đủ lớn để nhà trường phải xây phần mềm** | Không tổ chức nào bỏ công lập một module IT, quy trình xác nhận 2 bước và bài hướng dẫn riêng cho một nhu cầu hiếm gặp |
| 2 | **Nhu cầu gắn ĐÚNG với việc ĐI THI** | Bài hướng dẫn nêu thẳng cụm *"để dùng hoặc đi thi"*, và có lưu ý riêng về **WiFi_Exam** (mạng phòng thi) |
| 3 | **Chỉ ra chính xác KHOẢNG TRỐNG startup lấp vào** | Nguồn cung hiện tại là **bạn bè**: SV phải (a) quen ai đó có máy Windows rảnh, (b) người đó **không thi cùng ca**, (c) người đó **đồng ý đưa máy cá nhân chứa dữ liệu riêng tư** cho người khác mang vào phòng thi. **Cả 3 điều kiện đều mong manh — và điều kiện (b) gần như luôn thất bại đúng tuần thi, vì cả trường thi cùng lúc.** |
| 4 | **Chỉ ra rào cản kỹ thuật phải xử lý** | Máy cho thuê phải tương thích quy trình đăng nhập **WiFi_Exam bằng tài khoản cá nhân người thi** |

> ### 🎯 CÂU CHỐT ĐỂ ĐƯA VÀO SLIDE "VẤN ĐỀ" (mạnh nhất trong toàn bộ nghiên cứu)
>
> *"Chúng tôi không phải người đầu tiên phát hiện vấn đề này — chính Đại học FPT đã phát hiện ra trước. Trường đã xây hẳn một hệ thống IT với quy trình xác nhận hai bước chỉ để quản lý việc sinh viên mượn laptop của nhau 'để dùng hoặc đi thi'. Nhưng giải pháp của trường phụ thuộc vào một điều kiện luôn thất bại đúng vào tuần thi: phải có một sinh viên khác đang rảnh máy. Trong tuần thi cuối kỳ, tất cả sinh viên đều thi. Chúng tôi cung cấp nguồn cung không phụ thuộc vào điều đó."*

### ⚠️ RỦI RO PHÁP LÝ / VẬN HÀNH SỐ 1 PHẢI KIỂM CHỨNG TRƯỚC

Trang nguồn trên là của **campus TP.HCM**. Nhóm **bắt buộc** phải xác minh 2 điều với campus Đà Nẵng **trước khi đầu tư một đồng nào**:

1. **Campus Đà Nẵng có quy trình "ĐK Mượn máy" tương tự không?**
2. **⭐ Quy chế thi của ĐH FPT có CHO PHÉP dùng laptop thuê từ bên ngoài trường trong phòng thi không?**

> **Nếu câu 2 là KHÔNG → toàn bộ mô hình kinh doanh phải điều chỉnh.** Đây là **giả định sống-còn (kill assumption)** của dự án. Phải nêu thẳng trong proposal cùng kế hoạch kiểm chứng — giám khảo môn Khởi nghiệp đánh giá rất cao nhóm dám chỉ ra giả định có thể giết chết chính dự án của mình.
>
> **Kế hoạch kiểm chứng đề xuất:** gửi văn bản/email tới **Phòng Khảo thí + Phòng Công tác Sinh viên campus Đà Nẵng**, xin xác nhận bằng văn bản. Đưa cả **email gửi đi lẫn thư trả lời** vào phụ lục proposal.

---

# PHẦN 4 — HỌC PHÍ & LƯỢNG HOÁ THIỆT HẠI KHI LỠ THI

## 4.1. Học phí ĐH FPT — campus Đà Nẵng

| Khoản | Mức | Năm áp dụng | Nhãn | Nguồn |
|---|---|---|---|---|
| **Học phí giai đoạn chuyên ngành (Đà Nẵng)** | **22.120.000 VNĐ/học kỳ** | 2025–2026 và 2026–2027 | 🟢 | [Học phí Trường ĐH FPT 2025-2026 tại các cơ sở trên cả nước — Báo Đà Nẵng](https://baodanang.vn/hoc-phi-truong-dai-hoc-fpt-2025-2026-tai-cac-co-so-tren-ca-nuoc-3151966.html) · [Học phí ĐH FPT 2026–2027 — jobtest.vn](https://jobtest.vn/hrblog/hoc-phi-dai-hoc-fpt) |
| Dải học phí Đà Nẵng (tuỳ chương trình) | **15.480.000 – 25.060.000 VNĐ/học kỳ** | 2025–2026 | 🟡 | [Học phí ĐH FPT 2025 chính thức — Phongvu.vn](https://phongvu.vn/cong-nghe/hoc-phi-dai-hoc-fpt-2025-chinh-thuc/) |
| Giai đoạn định hướng (tân SV K22) | **6.420.000 VNĐ** (KV ưu tiên 1) / **9.170.000 VNĐ** (khu vực khác) | 2026 | 🟡 | [jobtest.vn](https://jobtest.vn/hrblog/hoc-phi-dai-hoc-fpt) |
| Ưu đãi vùng | Đà Nẵng & Cần Thơ **giảm 30%** so với chuẩn | 2026 | 🟡 | [jobtest.vn](https://jobtest.vn/hrblog/hoc-phi-dai-hoc-fpt) |
| Mức tăng 2025→2026 | **+2% đến +5%** tuỳ ngành/khu vực | 2026 | 🟡 | [dienthoaivui.com.vn](https://dienthoaivui.com.vn/back-to-school-hoc-phi-fpt) |
| Dải toàn hệ thống | **15.480.000 – 31.600.000 VNĐ/học kỳ** | 2026–2027 | 🟡 | [Học phí chính thức ĐH FPT 2026–2027 — VietJack](https://khoahoc.vietjack.com/tuyen-sinh/1392/hoc-phi-chinh-thuc-truong-dai-hoc-fpt-nam-2026-2027) |
| **Phí học lại 1 môn** | ⚫ **KHÔNG TÌM ĐƯỢC** | — | ⚫ | — (xem 3.2) |

## 4.2. ⭐ PHÉP TÍNH THIỆT HẠI — dùng học phí thay cho phí học lại

> 🔴 **Đây là tính toán suy luận của nhóm nghiên cứu** dựa trên các số 🟢 ở trên. Phải ghi rõ giả định trong proposal.

```
Học phí chuyên ngành 1 kỳ (Đà Nẵng)          = 22.120.000 VNĐ   [🟢 có nguồn]
Một học kỳ = 4 tháng ≈ 15–16 tuần            [🟢 có nguồn]

→ Chi phí học tập mỗi TUẦN                   ≈  1.383.000 VNĐ
→ Chi phí học tập mỗi NGÀY (7 ngày/tuần)     ≈    198.000 VNĐ

Giả định 1 kỳ có ~5 môn thi cuối kỳ  [🔴 giả định — nhóm phải đếm từ lộ trình học thật]
→ "Giá trị kinh tế" đã trả cho 1 môn         ≈  4.424.000 VNĐ
```

### Bảng so sánh chi phí / rủi ro — đưa nguyên vào slide định giá

| Hạng mục | Số tiền | Ghi chú |
|---|---|---|
| Thuê laptop 1 ngày thi (giá đề xuất) | **100.000 – 200.000 VNĐ** | 🔴 giá dự kiến của nhóm |
| Giá đối thủ cho thuê chung chung tại Đà Nẵng | 29.000 – 50.000 VNĐ/ngày | 🟢 [MIT Group](https://mitgroup.vn/cho-thue-laptop/), [leminhSTORE](https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html), [Trương Giang](https://truonggiang.vn/cho-thue-laptop.html) |
| **Giá trị học phí đã trả cho 1 môn bị trượt** | **≈ 4.424.000 VNĐ** | 🔴 suy từ số 🟢 |
| **Tỷ lệ chi phí thuê : thiệt hại** | **1 : 22 đến 1 : 44** | |

> ### 🎯 LUẬN ĐIỂM ĐỊNH GIÁ MẠNH NHẤT
>
> *"Sinh viên FPT Đà Nẵng đã trả 22,12 triệu đồng cho một học kỳ. Chia ra, mỗi môn thi tương ứng khoảng 4,4 triệu đồng học phí đã đóng. Chúng tôi bán một khoản chi 150.000 đồng để bảo vệ 4,4 triệu đồng đó. Tỷ lệ 1:29. Đây không phải quyết định mua sắm — đây là quyết định bảo hiểm, và với sinh viên đã trả 22 triệu/kỳ thì nó là quyết định hiển nhiên."*
>
> **Lưu ý phản biện giám khảo sẽ hỏi:** *"Sao thu 150k khi đối thủ thu 29–50k?"*
> **Trả lời:** *"Chúng tôi không bán thời gian sử dụng máy. Chúng tôi bán sự chắc chắn được dự thi: máy đã cài và test sẵn EOS + SEB, giao tận cổng phòng thi trước giờ thi, có máy dự phòng đổi trong 60 phút, có người trực suốt ca thi. Đối thủ ở Hải Châu cách campus 8–15 km và giao trong giờ hành chính — họ không thể phục vụ ca thi 7 giờ sáng."*

## 4.3. ⚠️ Điểm yếu của phép tính này (nêu trước để chặn phản biện)

| Điểm yếu | Cách xử lý trong proposal |
|---|---|
| Trượt môn **không mất toàn bộ** 4,4 triệu — sinh viên vẫn học được kiến thức, chỉ mất tiền học lại | Diễn đạt là **"giá trị kinh tế của một lượt thi"**, không phải "thiệt hại tiền mặt". Hoặc dùng số học lại thật khi nhóm tra được. |
| Giả định 5 môn/kỳ chưa kiểm chứng | Nhóm **đếm từ lộ trình học của chính mình** và ghi rõ |
| Còn thiệt hại phi tiền tệ: chậm tốt nghiệp, mất học bổng, áp lực tâm lý | **Nêu ra như phần bổ sung** — làm luận điểm mạnh hơn chứ không yếu đi |

---

# PHẦN 5 — LỊCH HỌC, TẦN SUẤT THI & MÙA VỤ KINH DOANH

## 5.1. Hệ 3 học kỳ/năm

| Học kỳ | Thời gian | Nhãn |
|---|---|---|
| **Spring** | Tháng 1 → tháng 5 | 🟢 |
| **Summer** | Tháng 5 → tháng 9 | 🟢 |
| **Fall** | Tháng 9 → hết tháng 12 | 🟢 |

- Một năm học có **3 học kỳ**, bắt đầu vào **tháng 9 – tháng 1 – tháng 5**. 🟢
- Mỗi học kỳ kéo dài **04 tháng ≈ 15–16 tuần**. 🟢
- Mô tả khác: mỗi kỳ **học 3 tháng, nghỉ 1 tháng** → sinh viên FPT **học 9 tháng/năm**. 🟡
- Toàn khoá: **4 năm – 9 kỳ – 4 giai đoạn**. 🟡

> **Nguồn:** [Ở FPTU, một năm học có 3 học kỳ — Fanpage Trường ĐH FPT](https://www.facebook.com/university.fpt.edu.vn/posts/1183525043803905/) · [Thời gian học Đại học FPT: 4 năm – 9 kỳ – 4 giai đoạn](https://hanoi.fpt.edu.vn/tu-van/thoi-gian-hoc-dai-hoc-fpt.html) · [Lộ trình đào tạo của Trường ĐH FPT](https://daihoc.fpt.edu.vn/lo-trinh-dao-tao-cua-truong-dai-hoc-fpt/) · ["Mùa học thêm" tại ĐH FPT](https://daihoc.fpt.edu.vn/tin-tuc-chung-2/mua-hoc-them-tai-dai-hoc-fpt/)

## 5.2. ⚫ Progress Test — không xác minh được

| Câu hỏi | Trạng thái |
|---|---|
| Mỗi môn có bao nhiêu Progress Test/kỳ? | ⚫ **KHÔNG TÌM ĐƯỢC** |
| Progress Test có thi trên EOS bằng laptop cá nhân không? | ⚫ **KHÔNG XÁC MINH ĐƯỢC** |
| Lịch thi cuối kỳ cụ thể (ngày, số ca) của campus Đà Nẵng | ⚫ **KHÔNG TÌM ĐƯỢC** |

> **→ Cách khắc phục dễ nhất:** nhóm là sinh viên FPT ĐN. **Chụp màn hình lịch thi thật trên FAP của chính thành viên nhóm** và đưa vào phụ lục. Đây là dữ liệu sơ cấp không ai phản biện được, và mạnh hơn mọi nguồn thứ cấp.

## 5.3. 🔴 Lịch mùa vụ suy ra (dùng cho mô hình tài chính)

> ⚠️ **SUY LUẬN của người nghiên cứu**, không phải lịch thi công bố.

| Đỉnh cầu | Thời điểm ước tính | Loại thi | Cường độ |
|---|---|---|---|
| **Đỉnh 1** | Cuối tháng 4 – đầu tháng 5 | Final Exam kỳ Spring | Cao |
| **Đỉnh 2** | Cuối tháng 8 – đầu tháng 9 | Final Exam kỳ Summer | Cao |
| **Đỉnh 3** | Cuối tháng 12 | Final Exam kỳ Fall | Cao |
| **Đỉnh 4 ⭐** | **Tháng 9 (đầu khoá mới)** | **Thi tiếng Anh đầu vào/xếp lớp cho tân sinh viên — cũng thi trên EOS** 🟢 | **Cao + là cơ hội thu hút khách hàng tốt nhất năm** |
| Đỉnh phụ ×3 | Giữa mỗi kỳ | Progress Test | Trung bình (chưa xác minh) |

**Vì sao Đỉnh 4 là quan trọng nhất về mặt marketing:**
Kỳ thi tiếng Anh đầu vào/xếp lớp diễn ra ngay đầu khoá cho hàng nghìn tân sinh viên, **và cũng thi trên EOS bằng laptop cá nhân** 🟢. Tân sinh viên là nhóm rủi ro cao nhất: vừa nhập học, nhiều em chưa kịp mua laptop, hoặc **đã lỡ mua MacBook M-series** mà chưa biết không thi được.

> **Nguồn:** [HD SV sử dụng và thi tiếng Anh xếp lớp trên phần mềm EOS](https://daihoc.fpt.edu.vn/tin-tuc-chung-2/su-kien-tin-tuc-chung-2/huong-dan-sinh-vien-su-dung-va-thi-tieng-anh-xep-lop-tren-phan-mem-eos/) · [Tra cứu lịch thi tiếng Anh đầu vào khoá 20 — ĐH FPT Hà Nội](https://daihoc.fpt.edu.vn/tra-cuu-lich-thi-tieng-anh-dau-vao-khoa-20-dh-fpt-ha-noi/)

### 👉 Hàm ý tài chính bắt buộc nêu trong proposal

Doanh thu **không đều**: tập trung vào **~6 đợt/năm, mỗi đợt 1–2 tuần**. Mô hình tài chính **phải mô hình hoá theo mùa vụ**, tuyệt đối không chia đều 12 tháng. Giữa các đợt thi, đội laptop nên chuyển sang **cho thuê theo tháng** (đồ án, thực tập, OJT, máy đang sửa) để giảm thời gian nằm không.

---

# PHẦN 6 — QUY MÔ SINH VIÊN (CƠ SỞ TÍNH THỊ TRƯỜNG)

## 6.1. Toàn hệ thống

| Chỉ số | Giá trị | Thời điểm | Nhãn | Nguồn |
|---|---|---|---|---|
| Số campus ĐH FPT | **5** (Hà Nội, TP.HCM, Đà Nẵng, Cần Thơ, Quy Nhơn) | 2025 | 🟢 | [Campus — Trường ĐH FPT](https://daihoc.fpt.edu.vn/campus/) |
| Tổng SV ĐH & sau ĐH toàn hệ thống ĐH FPT | **~30.000** | 2024 | 🟡 | [FPT University — Wikipedia](https://en.wikipedia.org/wiki/FPT_University) |
| **Chỉ tiêu tuyển sinh ĐH FPT toàn quốc** | **13.677 sinh viên** | 2025 | 🟢 | [Quy chế tuyển sinh 2025 — ĐH FPT](https://daihoc.fpt.edu.vn/quy-che-tuyen-sinh-2025/) · [situ.edu.vn](https://situ.edu.vn/de-an-va-chi-tieu-tuyen-sinh-dai-hoc-fpt/) |
| FPT Education — bậc đại học | Giữ ổn định **~50.000 sinh viên** | 2025 | 🟡 | [chungta.vn — Anh Lê Trường Tùng](https://chungta.vn/longform/b-anh-le-truong-tung-2026-se-la-nam-nang-tam-toan-dien-giao-duc-fpt-b-1140961.html) |
| FPT Education — mục tiêu quy mô HSSV | **150.000** HSSV | mục tiêu 2025 | 🟡 | [fpt.com](https://fpt.com/vi/tin-tuc/tin-fpt/fpt-day-manh-phat-trien-he-thong-giao-duc-pho-thong) |
| FPT Schools (phổ thông) | **>18.000 học sinh** | năm học 2026–2027 | 🟢 | [Lễ khai giảng 2026–2027 toàn hệ thống FPT Schools](https://fschool.fpt.edu.vn/tung-bung-le-khai-giang-nam-hoc-2026-2027-toan-he-thong-fpt-schools-hon-18-000-hoc-sinh-cung-buoc-vao-hanh-trinh-moi/) |

> **⚠️ Mâu thuẫn nguồn:** [uniRank](https://www.unirank.org/vn/uni/fpt-university/) xếp ĐH FPT vào nhóm **8.000–8.999 SV**, mâu thuẫn với ~30.000 của Wikipedia. uniRank là dữ liệu tự khai, thường lỗi thời. **Dùng ~30.000 và ghi rõ nguồn + năm.**
>
> **⚠️ Con số KHÔNG được dùng:** một kết quả tìm kiếm nêu *"gần 25.000 sinh viên, học viên"* — mâu thuẫn rõ với các số khác, có vẻ là dữ liệu cũ nhiều năm trước.

## 6.2. ⭐ Campus Đà Nẵng

### Dữ liệu thật tìm được

| Dữ liệu | Giá trị | Thời điểm | Nhãn | Nguồn |
|---|---|---|---|---|
| Tân sinh viên khoá 16 khai giảng | **gần 1.000** | 26/09/2020 | 🟢 | [1.000 tân sinh viên ĐH FPT Đà Nẵng khai giảng năm học mới — FPT City](https://fptcity.vn/1-000-tan-sinh-vien-dai-hoc-fpt-da-nang-khai-giang-nam-hoc-moi/) |
| Sinh viên quốc tế đón hằng năm | **gần 1.000** SV/năm | ~2025 | 🟡 | [FPT University, Da Nang Campus — International Office UI](https://international.ui.ac.id/shortcourse-fpt/) |
| Diện tích campus | **5,1 ha**, khởi công 2018 | — | 🟢 | [Campus Đà Nẵng — Trường ĐH FPT](https://daihoc.fpt.edu.vn/da-nang/) |
| Slot ký túc xá đợt 1 (K19) | **500 slot** | — | 🟡 | [KTX tại ĐH FPT Đà Nẵng cho tân SV K19](https://daihoc.fpt.edu.vn/chua-phan-loai/ky-tuc-xa-tai-dh-fpt-da-nang-danh-cho-tan-sinh-vien-k19/) |
| **Tổng số sinh viên hiện tại campus ĐN** | ⚫ **KHÔNG CÔNG BỐ** | — | ⚫ | — |

### 🔴 Ước lượng tam giác hoá — SV ĐH FPT Đà Nẵng

| Cách | Lập luận | Kết quả |
|---|---|---|
| **Cách 1** | Chỉ tiêu toàn quốc 2025 = 13.677 🟢; giả định campus ĐN chiếm **10–12%** 🔴 → tân SV ĐN 1.370–1.640/năm; × 4 khoá − 15% rơi rớt/OJT | **4.500 – 6.000** |
| **Cách 2** | 2020 (K16) gần 1.000 tân SV 🟢; giả định tăng 8–12%/năm 🔴 → 2025 (K21) ≈ 1.470–1.760 tân SV; × 4 khoá | **5.000 – 6.500** |
| **Cách 3 (kiểm chéo)** | 500 slot KTX đợt 1; nếu KTX phục vụ ~10% tổng SV → ~5.000 SV | **≈ 5.000** ✓ nhất quán |

> ### 🎯 CON SỐ ĐỀ XUẤT DÙNG
> **Sinh viên ĐH FPT Đà Nẵng ≈ 5.000 (khoảng 4.500 – 6.000)** 🔴
>
> **BẮT BUỘC ghi chú kèm:** *"Ước tính của nhóm dựa trên chỉ tiêu tuyển sinh toàn quốc 2025 là 13.677 SV và số tân sinh viên khoá 16 tại Đà Nẵng năm 2020 là gần 1.000; nhà trường không công bố số sinh viên theo từng campus."*
>
> **Cách kiểm chứng thật (khuyến nghị mạnh):** nhóm là sinh viên FPT ĐN → **xin số liệu trực tiếp từ Phòng Công tác Sinh viên / Phòng Đào tạo campus Đà Nẵng**. Một email xin số liệu kèm thư trả lời đưa vào phụ lục sẽ nâng điểm hơn hẳn mọi ước lượng.

## 6.3. Hệ sinh thái FPT khác tại Đà Nẵng (mở rộng thị trường phục vụ được)

| Đơn vị | Quy mô | Vị trí | Nhãn | Nguồn |
|---|---|---|---|---|
| **CĐ FPT Polytechnic** (toàn quốc) | **40.000+** SV đã theo học | Có cơ sở tại Đà Nẵng | 🟡 | [tuyensinhso.vn](https://tuyensinhso.vn/school/cao-dang-fpt-polytechnic.html) · [Đà Nẵng — CĐ FPT Polytechnic](https://caodang.fpt.edu.vn/category/tin-tuc-poly/tin-da-nang) |
| **FPT Schools Đà Nẵng** | Đón **>700 học sinh** nhập học | Campus hoàn thiện đầu tiên toàn quốc | 🟡 | [Lễ nhập học FSchools Đà Nẵng](https://danang12-school.fpt.edu.vn/le-nhap-hoc-fschools-da-nang/) · [chungta.vn](https://chungta.vn/nguoi-fpt/fpt-schools-da-nang-la-don-vi-dau-tien-hoan-thien-campus-tren-ca-nuoc-1136593.html) |
| **Greenwich Việt Nam** (toàn quốc) | **gần 20.000** SV / 4 campus | ĐN: **658 Ngô Quyền, P. An Hải** — **cách Hoà Hải ~8–10 km** | 🟡 | [Greenwich Việt Nam](https://greenwich.edu.vn/) · [Wikipedia](https://vi.wikipedia.org/wiki/Greenwich_Vi%E1%BB%87t_Nam) |

> **⚠️ Lưu ý chiến lược:** Greenwich ĐN **không nằm trong bán kính phục vụ ban đầu**. Chỉ đưa vào giai đoạn mở rộng, và phải tính lại chi phí giao hàng.

---

# PHẦN 7 — CÁC TRƯỜNG ĐẠI HỌC KHÁC TẠI ĐÀ NẴNG (TIỀM NĂNG MỞ RỘNG)

## 7.1. Bảng tổng hợp quy mô

| Trường | Quy mô sinh viên | Chỉ tiêu 2025 | Khoảng cách tới Hoà Hải | Nhãn | Nguồn |
|---|---|---|---|---|---|
| **Đại học Đà Nẵng** (ĐH vùng) | **~50.000 SV** (Wikipedia) / **60.839** (US News) | **>17.000** | Đa cơ sở (Hải Châu / Liên Chiểu / Cẩm Lệ) | 🟡 | [Wikipedia](https://en.wikipedia.org/wiki/University_of_Da_Nang) · [US News](https://www.usnews.com/education/best-global-universities/university-of-danang-530596) · [VnExpress](https://vnexpress.net/diem-chuan-dai-hoc-da-nang-2025-chinh-xac-nhat-4929604.html) |
| ├ **ĐH Bách khoa – ĐHĐN (DUT)** | — | **3.900** SV | 54 Nguyễn Lương Bằng, Liên Chiểu (**~15 km**) | 🟢 | [VnExpress](https://vnexpress.net/diem-chuan-dai-hoc-bach-khoa-da-nang-2025-moi-nhat-4929639.html) · [Tuyển sinh DUT](https://tuyensinh.dut.udn.vn/) |
| ├ **ĐH CNTT&TT Việt–Hàn (VKU)** | ~450 SV tốt nghiệp khoá 2021–2026 | **1.500** SV | Ngũ Hành Sơn — **gần Hoà Hải nhất trong nhóm ĐHĐN** | 🟢 | [VKU tuyển sinh 2025](https://vku.udn.vn/vi/truong-dai-hoc-cong-nghe-thong-tin-va-truyen-thong-viet-han-thong-bao-tuyen-sinh-dai-hoc-chinh-quy-nam-2025-du-kien/) · [VKU điểm trúng tuyển 2025](https://vku.udn.vn/vi/vku-cong-bo-diem-trung-tuyen-tuyen-sinh-dai-hoc-nam-2025/) |
| ├ **ĐH Kinh tế – ĐHĐN** | ⚫ chưa có số | — | 71 Ngũ Hành Sơn, gần cầu Trần Thị Lý | 🟡 | [tuyensinhso.vn](https://tuyensinhso.vn/school/dai-hoc-kinh-te-dai-hoc-da-nang.html) |
| ├ **ĐH Ngoại ngữ – ĐHĐN** | 18 chuyên ngành | — | 131 Lương Nhữ Học, Cẩm Lệ | 🟡 | [IELTS Fighter](https://ielts-fighter.com/tin-tuc/cac-truong-dai-hoc-o-da-nang_mt1641797220.html) |
| **Đại học Duy Tân** | **>20.000 SV**; **>90 chuyên ngành** | — | Đa cơ sở (Hải Châu / Ngũ Hành Sơn) | 🟢 | [Tổng quan ĐH Duy Tân](https://duytan.edu.vn/gioi-thieu) · [Tuyển sinh 2025](https://tuyensinh2025.duytan.edu.vn) |
| **Đại học Đông Á** | — | **6.179** SV | 33 Xô Viết Nghệ Tĩnh, Hải Châu | 🟢 | [ĐH Đông Á tuyển sinh 2025](https://donga.edu.vn/tuyensinh/ts-chi-tiet/dai-hoc-dong-a-cong-bo-06-phuong-thuc-tuyen-sinh-he-chinh-quy-nam-2025-37366) |
| **Greenwich VN – cơ sở ĐN** | Toàn hệ thống ~20.000 SV | — | 658 Ngô Quyền, An Hải (~8–10 km) | 🟡 | [greenwich.edu.vn](https://greenwich.edu.vn/) |
| **CĐ Đại Việt Đà Nẵng** | — | **2.000** SV | Hải Châu | 🟡 | [Đại Việt ĐN tuyển sinh 2025](https://daivietdanang.edu.vn/dao-tao/bai-viet/thong-bao-tuyen-sinh-cao-dang-chinh-quy-nam-2025-1037.html) |
| **Tổng số trường ĐH tại Đà Nẵng** | **17 trường / cơ sở đào tạo** | — | — | 🟡 | [trangedu.com](https://trangedu.com/blog/dai-hoc-hoc-vien-tai-da-nang/) · [Tuyển Sinh Số](https://tuyensinhso.vn/khu-vuc/khu-vuc-da-nang-c11808.html) |

**ĐH Sư phạm Kỹ thuật – ĐH Đà Nẵng:** ⚫ **không thu thập được số liệu riêng** trong các phiên trước.

## 7.2. 🚨 RÀO CẢN QUAN TRỌNG NHẤT KHI MỞ RỘNG — phải nêu thẳng

> **Không tìm được bằng chứng nào cho thấy các trường khác tại Đà Nẵng (ĐH Đà Nẵng, Duy Tân, Đông Á, VKU, Bách khoa…) yêu cầu sinh viên mang LAPTOP CÁ NHÂN đi thi cuối kỳ.** Các trường này chủ yếu thi giấy hoặc thi tại **phòng lab của trường**.
>
> **→ "Pain point ngày thi" là ĐẶC THÙ CỦA HỆ THỐNG FPT.** Nó **không tự động mở rộng** sang trường khác.

### Hệ quả với chiến lược mở rộng

| Thị trường | Sản phẩm phải bán | Tính khẩn cấp | Biên lợi nhuận | Đối thủ |
|---|---|---|---|---|
| **ĐH FPT ĐN (lõi)** | *"Bảo đảm dự thi"* — máy cài sẵn EOS+SEB | **Rất cao** | **Cao** | Gần như không có |
| Các trường khác ở ĐN | *"Thuê laptop cho đồ án / thực tập / khi máy đang sửa"* | Thấp | Thấp | ≥7 cửa hàng hiện hữu, giá 29–50k/ngày |

> **Khuyến nghị:** **KHÔNG vẽ TAM = toàn bộ sinh viên Đà Nẵng.** Giám khảo môn Khởi nghiệp đánh giá cao **thị trường ngách được định nghĩa sắc nét** hơn là TAM khổng lồ không có cơ sở.

### ✅ Một tín hiệu tích cực cho hướng B2B
Có bằng chứng các trường ĐH tại Đà Nẵng **CÓ thuê laptop số lượng lớn**: đơn vị SEA Event ghi nhận cho thuê **hơn 100 laptop** phục vụ đào tạo/đánh giá AUN-QA tại **Trường ĐH Bách Khoa – ĐH Đà Nẵng**, ngày **26–30/10/2020** 🟡 — [SEA Event case study](https://seaevent.vn/cho-thue-laptop-phuc-vu-dao-tao-tai-truong-dai-hoc-bach-khoa-da-nang/).

**→ Đây là hướng mở rộng B2B (sự kiện, kiểm định, tập huấn), khác hoàn toàn với B2C ngày thi.** Có thể nêu như "giai đoạn 3" trong lộ trình.

---

# PHẦN 8 — CÁC KỲ THI CHỨNG CHỈ TẠI ĐÀ NẴNG CẦN MÁY TÍNH

| Chứng chỉ | Hình thức thi | Địa điểm tại Đà Nẵng | Lệ phí | Phù hợp mô hình? | Nhãn | Nguồn |
|---|---|---|---|---|---|---|
| **TOEIC (IIG Việt Nam)** | **Thi trên máy tính (CBT)** có kết nối internet tại trung tâm uỷ quyền; báo điểm ngay | VP IIG: **19 Hoàng Văn Thụ, Hải Châu** | **L&R:** 1.590.000 VNĐ (người đi làm) / **1.430.000 VNĐ (HSSV)**; **S&W:** 2.270.000 VNĐ. Từ **09/06/2025** có gói 4 kỹ năng cho SV **giảm 450.000 VNĐ** | ⚠️ **Máy do trung tâm cấp** → không cần thuê | 🟡 | [MS Hoa](https://www.anhngumshoa.com/tin-tuc/dia-diem-thong-tin-dang-ky-thi-toeic-tai-iig-vietnam-34944.html) · [ZIM](https://zim.vn/le-phi-thi-toeic) · [IIG gói ưu đãi SV](https://iigvietnam.com/announcement-iig-vietnam-launches-special-discount-package-for-toeic-4-skill-test-only-for-students/) · [Lịch thi tiếng Anh IIG](https://online.iigvietnam.com/lich-thi-tieng-anh) |
| **AWS / Microsoft (Pearson VUE)** | Thi tại **phòng lab đạt chuẩn**, HOẶC **thi online tại nhà (OnVUE)** | Có trung tâm Pearson VUE tại Đà Nẵng | ⚫ chưa tìm được giá tại ĐN | ✅ **CÓ tiềm năng — nhánh thi online tại nhà cần máy cá nhân đạt chuẩn** | 🟡 | [CodeGym](https://codegym.vn/blog/thi-chung-chi-aws-o-dau-cach-toi-uu-hoa-chi-phi-thi-chung-chi-aws/) · [Atoha — danh sách Pearson VUE VN](https://www.atoha.com/blogs/tin-tuc/cap-nhat-dia-diem-thi-pearson-vue) · [AWS Certification Testing](https://aws.amazon.com/vi/certification/certification-prep/testing/) |
| **JLPT (tiếng Nhật)** | **Thi trên GIẤY** (paper-based) | Khoa NN&VH Nhật Bản, **ĐH Ngoại ngữ – ĐHĐN, 131 Lương Nhữ Học, Cẩm Lệ** | — | ❌ **KHÔNG phải thị trường mục tiêu** | 🟡 | [Japan Foundation](https://hn.jpf.go.jp/posts/jlpt1225-vn) · [Khoa NN&VH Nhật Bản ĐHĐN](https://nnvhnhatban.ufl.udn.vn/category/thong-bao/jlpt/) |
| Lịch JLPT | 2 đợt/năm: **06/07/2025** và **07/12/2025** | | | | 🟢 | [Japan Foundation](https://hn.jpf.go.jp/posts/jlpt1225-vn) |
| **TOPIK (tiếng Hàn)** | ⚫ **KHÔNG TÌM ĐƯỢC** thông tin địa điểm thi tại Đà Nẵng | — | — | ⚫ Chưa kết luận được | ⚫ | — |
| **Coursera proctored exam** | ⚫ **KHÔNG NGHIÊN CỨU ĐƯỢC** trong các phiên trước | — | — | ⚫ | ⚫ | — |

## 8.1. ⭐ Thi TOEIC nội bộ tại ĐH FPT — đỉnh cầu bị bỏ sót

- ĐH FPT (campus Hà Nội) tổ chức **thi TOEIC định kỳ từ thứ 2 đến thứ 7 hàng tuần**, trong giờ hành chính, tại 3 cơ sở. 🟡
- Sinh viên đạt **TOEIC ≥ 800** được **miễn thi tiếng Anh đầu vào** FPT. 🟡
- **Kỳ thi tiếng Anh đầu vào / xếp lớp của FPT cũng thi trên phần mềm EOS.** 🟢

> **Nguồn:** [PTE Magic](https://ptemagic.com.vn/chung-chi-nao-phu-hop-de-duoc-mien-thi-tieng-anh-dau-vao-fpt/) · [HD SV thi tiếng Anh xếp lớp trên EOS](https://daihoc.fpt.edu.vn/tin-tuc-chung-2/su-kien-tin-tuc-chung-2/huong-dan-sinh-vien-su-dung-va-thi-tieng-anh-xep-lop-tren-phan-mem-eos/)

## 8.2. 🎯 Kết luận thẳng thắn về nhánh "thi chứng chỉ"

> **Đây KHÔNG phải thị trường tốt cho mô hình cho thuê laptop, và proposal nên nói thẳng điều đó.**
>
> Lý do: **TOEIC (IIG) và Pearson VUE tại trung tâm đều CẤP MÁY cho thí sinh.** JLPT thi giấy. Chỉ còn nhánh nhỏ **"thi chứng chỉ online tại nhà"** (OnVUE của Pearson) là cần máy cá nhân đạt chuẩn.
>
> **Cách trình bày ăn điểm:** *"Chúng tôi đã kiểm tra nhánh thi chứng chỉ và kết luận nó KHÔNG phải thị trường mục tiêu, vì hầu hết trung tâm khảo thí đều cấp máy. Chúng tôi tập trung 100% nguồn lực vào đúng nhóm khách hàng duy nhất bắt buộc phải tự mang máy: sinh viên Đại học FPT."* — Việc **chủ động loại bỏ một thị trường** thể hiện tư duy chiến lược tốt hơn nhiều so với liệt kê mọi thứ vào TAM.

---

# PHẦN 9 — ⭐⭐ THIẾT KẾ SLA (CAM KẾT CHẤT LƯỢNG DỊCH VỤ)

> Đây là **phần ứng dụng chính** của toàn bộ nghiên cứu trên. Mọi con số SLA dưới đây là **thiết kế của nhóm** 🔴, nhưng **được neo vào các dữ kiện có nguồn** — cột "Neo vào dữ kiện nào" là phần quan trọng nhất để trả lời phản biện.

## 9.1. Nguyên lý thiết kế: bán "sự chắc chắn", không bán "cái máy"

| Dữ kiện đã xác minh | Suy ra yêu cầu SLA nào |
|---|---|
| Bài thi lưu **trên ổ cứng máy sinh viên**, hỏng máy = mất bài (1.4) | Phải có **máy thay thế cực nhanh**, không phải "sửa máy" |
| **SLA sửa chữa nhanh nhất đo được tại Đà Nẵng là 48 giờ** ([FPT Shop](https://fptshop.com.vn/tin-tuc/tin-khuyen-mai/goi-bao-hanh-roi-vo-dien-thoai-laptop-tai-fpt-shop-gia-chi-tu-79000-dong-137045)) 🟡 | 48h **quá chậm** — kỳ thi đã kết thúc. **Không thể dựa vào sửa chữa. Bắt buộc phải có máy dự phòng tồn kho.** |
| Hệ thống mượn máy nội bộ FPT có **thời gian mượn tối thiểu 60 phút** (3.3) | **60 phút** là đơn vị thời gian mà chính hệ sinh thái FPT đã dùng → chọn làm mốc SLA đổi máy để dễ hiểu, dễ nhớ |
| Toàn trường thi **cùng 1–2 tuần** (5.3) | Trong tuần thi, **100% đội máy được thuê cùng lúc → không còn máy trống**. Bắt buộc giữ **đệm dự phòng không cho thuê** |
| Thi Listening cần **tai nghe có dây / jack 3.5mm** (1.2) | Đưa **tai nghe có dây vào gói giao máy mặc định**, không bán thêm |
| Trường yêu cầu đăng nhập **WiFi_Exam bằng tài khoản cá nhân người thi** (3.3) | Máy giao phải ở trạng thái **chưa lưu tài khoản WiFi của ai**, và có hướng dẫn dán sẵn |

## 9.2. 🎯 BẢNG SLA ĐỀ XUẤT (đưa nguyên vào proposal)

| # | Cam kết | Mức cam kết | Neo vào dữ kiện nào | Chế tài nếu vi phạm |
|---|---|---|---|---|
| **S1** | **Giao máy trước giờ thi** | **≥ 60 phút** trước giờ thi ghi trên FAP | Ca thi sáng bắt đầu sớm; SV cần thời gian đăng nhập WiFi_Exam | Miễn 100% phí thuê |
| **S2** | ⭐ **Đổi máy dự phòng khi máy hỏng** | **≤ 60 phút** kể từ lúc nhận báo, trong bán kính campus | Không thể dựa vào sửa chữa (SLA thị trường 48h) → phải có máy dự phòng tại chỗ | Miễn 100% phí thuê + hoàn cọc ngay |
| **S3** | **Máy đã cài & test sẵn EOS + IT Client + SEB** | 100% máy, **test lại trước MỖI lượt giao**, có checklist ký xác nhận | Rủi ro R2 "lỗi EOS/SEB" điểm 20/25 trong ma trận rủi ro | Miễn 100% phí thuê |
| **S4** | **Máy đã giải nén phần mềm thi đúng thư mục** | 100% máy | Cảnh báo của trường: giải nén sai → **mất bài thi** (1.4) | Miễn 100% phí thuê |
| **S5** | **Giao kèm phụ kiện đầy đủ** | Sạc + **tai nghe có dây** + túi chống sốc | Listening bắt buộc tai nghe có dây 🟢 | Bù phụ kiện ngay trong 30 phút |
| **S6** | **Pin đạt chuẩn** | Battery health **> 70%**, sạc đầy khi giao | Kịch bản "hết pin giữa giờ thi" | Đổi máy theo S2 |
| **S7** | **Trực hỗ trợ trong mùa thi** | Hotline/Zalo trực **từ 30 phút trước ca thi đầu đến hết ca thi cuối**, mọi ngày trong tuần thi | Sự cố xảy ra đúng lúc thi, không phải giờ hành chính | — |
| **S8** | **Máy sạch dữ liệu, tài khoản trống** | Ghi đè **Golden Image** sau MỖI lượt thuê | Tránh vướng quy chế thi (nghi gian lận) + bảo vệ dữ liệu khách trước | — |
| **S9** | **Không tự ý cập nhật / không tự ngủ** | Windows Update tắt, Power Plan High Performance, Fast Startup tắt | Kịch bản "máy restart giữa giờ thi → mất bài" | Đổi máy theo S2 |

## 9.3. ⚠️ Giới hạn trách nhiệm — điều khoản BẮT BUỘC phải có

> **Đây là điều khoản quan trọng nhất về mặt pháp lý của toàn bộ mô hình.**

| Điều khoản | Nội dung đề xuất |
|---|---|
| **Giới hạn trách nhiệm** | Bên cho thuê **KHÔNG chịu trách nhiệm về kết quả thi** của khách hàng. **Trách nhiệm tối đa = hoàn 100% phí thuê + cung cấp máy thay thế.** |
| **Không cam kết kết quả** | Dịch vụ cam kết về **thiết bị và thời gian phục vụ**, **không cam kết** sinh viên sẽ thi đạt |
| **Dữ liệu cá nhân** | Máy được **xoá sạch và cài lại** sau khi trả; khách tự sao lưu; bên cho thuê không chịu trách nhiệm mất dữ liệu |
| **Không dùng từ "bảo hiểm"** | Gói bảo vệ thiệt hại phải gọi là **"Gói Miễn trừ thiệt hại"**, tránh rủi ro bị coi là kinh doanh bảo hiểm không phép |

> **⚠️ Vì sao bắt buộc:** nếu máy hỏng khiến sinh viên trượt môn, khách **có thể đòi bồi thường học phí học lại**. Chính phép tính ở Phần 4.2 (1 môn ≈ 4,4 triệu VNĐ) mà nhóm dùng để **bán hàng** cũng chính là con số khách sẽ dùng để **đòi bồi thường**. **Phải chặn bằng điều khoản, ngay từ hợp đồng mẫu đầu tiên.**

## 9.4. Cơ cấu đội máy để đáp ứng SLA (15–40 máy)

| Hạng | Cấu hình đề xuất 🔴 | Phục vụ | Tỷ trọng đề xuất |
|---|---|---|---|
| **Hạng A — "Thi chuẩn"** | i5 gen 8–10 / Ryzen 5, **8 GB RAM**, SSD 256 GB, Win 10/11, **có jack 3.5mm**, webcam, pin ≥ 3h | EOS Client: Business English, các môn trắc nghiệm, thi tiếng Anh đầu vào | ~60% |
| **Hạng B — "Thi IT"** | i5/i7 gen 11+, **16 GB RAM**, SSD 512 GB | IT Client: Java, C#, C/C++, Database, OS, Computer Network; đồ án | ~25% |
| **Đệm dự phòng** | Trộn cả 2 hạng | **KHÔNG BAO GIỜ cho thuê trong mùa thi** — chỉ để thực hiện S2 | **~15%** |

> **⚠️ Con số phải vào bảng vốn đầu tư:** với đội **25 máy cho thuê**, đệm 15% = **4 máy dự phòng**. Nếu tính 12 triệu/máy → **48 triệu VNĐ vốn nằm im**. **Đây là chi phí của lời hứa "đổi máy trong 60 phút" — phải hạch toán minh bạch, đừng giấu.**

## 9.5. Checklist bàn giao máy (in ra, ký 2 bên mỗi lượt)

```
□  Windows 10/11 bản quyền, đã update xong, ĐÃ TẮT auto-update
□  EOS Client + IT Client + SEB đã cài, ĐÃ TEST CHẠY
□  Phần mềm thi ĐÃ GIẢI NÉN đúng thư mục
□  Test jack tai nghe 3.5mm — OK
□  Test webcam + micro — OK
□  Battery health > 70%, pin sạc đầy
□  Kèm: củ sạc + dây + tai nghe có dây + túi chống sốc
□  Power Plan = High Performance, sleep = Never, Fast Startup = Off
□  Chỉ có Windows Defender, đã gỡ AV bên thứ ba
□  Đã wipe Golden Image, tài khoản Windows trống, chưa lưu WiFi của ai
□  Dán nhãn: mã máy + hotline + dòng chữ "CẮM SẠC KHI THI"
□  Chụp ảnh/quay video tình trạng máy 2 chiều, khách ký xác nhận
□  Ghi Serial/Service Tag vào biên bản
```

## 9.6. Hai rủi ro nghiêm trọng nhất — và vì sao tiền không giải quyết được

Trích từ ma trận rủi ro (`08-bao-hiem-rui-ro.md`), thang Khả năng × Tác động, tối đa 25 điểm:

| # | Rủi ro | KN | TĐ | Điểm | Biện pháp | Rủi ro còn lại |
|---|---|---|---|---|---|---|
| **R1** | **Máy hỏng giữa mùa thi, không có máy thay** | 4 | 5 | **20** 🔴 | Đệm 4 máy dự phòng (15%); cam kết đổi máy 60 phút; trực suốt tuần thi | 🟡 Trung bình |
| **R2** | **Lỗi EOS/SEB không chạy được khi thi** | 4 | 5 | **20** 🔴 | Golden Image; **test EOS+SEB trước mặt khách khi giao**; tắt Windows Update; tài khoản không có quyền admin | 🟢 Thấp |

> **Kết luận có sức nặng:** *"Hai rủi ro nghiêm trọng nhất của mô hình đều KHÔNG phải rủi ro tài chính. Chúng là rủi ro vận hành. Chúng không được giải quyết bằng bảo hiểm hay quỹ dự phòng tiền mặt, mà bằng hai thứ: đệm máy dự phòng và quy trình Golden Image. Đó là lý do chúng tôi thiết kế SLA trước, rồi mới thiết kế bảng giá."*

## 9.7. Vì sao SLA này là hào cạnh tranh, không phải chi phí

| Yếu tố | Đối thủ hiện tại tại Đà Nẵng | Mô hình đề xuất |
|---|---|---|
| Vị trí | Nội thành (Hải Châu, Liên Chiểu) — cách Hoà Hải **8–15 km** | **Ngay trong/cạnh campus** |
| Chuẩn bị máy | Máy trắng, khách tự cài | **Cài sẵn EOS + IT Client + SEB, đã test** |
| Giờ giao | Giờ hành chính | **Trước ca thi sáng (6–7h) và ca chiều** |
| Đặt máy | Gọi điện / inbox | **Website đặt online, xem máy trống theo lịch thi** |
| Hiểu ngữ cảnh | Không | **Hiểu quy chế thi FPT, biết Mac M-series không thi được, biết cần jack 3.5mm** |
| Máy dự phòng | Không | **Đệm 15%, đổi máy ≤ 60 phút** |
| Giá | 29.000 – 50.000 VNĐ/ngày | 100.000 – 200.000 VNĐ/ngày thi |

> **Dòng đầu tiên nên đặt trên trang chủ website:**
> ### **"Máy hỏng giữa giờ thi? Chúng tôi đổi máy khác trong 60 phút. Miễn phí."**

---

# PHẦN 10 — DANH MỤC DỮ LIỆU CÒN THIẾU & CÁCH NHÓM TỰ THU THẬP

> **Đây là phần trung thực nhất và cũng dễ ăn điểm nhất của proposal.** Trình bày dưới dạng "Kế hoạch kiểm chứng giả định" chứ không phải "những gì chúng tôi không biết".

## 10.1. Bảng dữ liệu thiếu, xếp theo mức độ nguy hiểm

| # | Dữ liệu thiếu | Mức nguy hiểm | Cách nhóm tự lấy | Chi phí |
|---|---|---|---|---|
| 1 | ⭐ **Quy chế thi FPT có CHO PHÉP dùng laptop thuê ngoài không** | 🔴🔴🔴 **GIẢ ĐỊNH SỐNG-CÒN** | Văn bản/email hỏi **Phòng Khảo thí + CTSV campus ĐN**; đưa cả câu hỏi và trả lời vào phụ lục | 0đ |
| 2 | **Trường có sẵn máy dự phòng cho SV mượn khi sự cố không** | 🔴🔴🔴 Rất cao — nếu CÓ thì nhu cầu gần như biến mất | Hỏi Phòng Khảo thí campus ĐN | 0đ |
| 3 | **Tỷ lệ SV gặp sự cố laptop đúng/sát ngày thi** | 🔴🔴🔴 Rất cao — là giả định cốt lõi của toàn bộ mô hình doanh thu | **Khảo sát Google Form n = 100–200 SV FPT ĐN** (xem 10.2) | 0đ |
| 4 | **Phí học lại 1 môn (VNĐ/môn)** | 🔴🔴🔴 Rất cao | Đăng nhập **FAP → mục học phí**, chụp màn hình; hoặc hỏi Phòng Tài chính | 0đ |
| 5 | **Hậu quả vắng thi: điểm 0? cấm thi? có thi bù không?** | 🔴🔴🔴 Rất cao | Xin **Sổ tay sinh viên bản mới nhất** từ Phòng CTSV (bản đang có là 2016) | 0đ |
| 6 | **Số SV chính xác của campus Đà Nẵng** | 🔴🔴🔴 Rất cao | Xin Phòng CTSV / Phòng Đào tạo campus ĐN | 0đ |
| 7 | **Lịch thi cuối kỳ cụ thể** (ngày, số ca, số ngày) | 🔴🔴🔴 Rất cao | **Chụp màn hình lịch thi trên FAP của chính thành viên nhóm** | 0đ |
| 8 | **SEB có chạy được trên máy ảo/Parallels không** | 🔴🔴 Cao | **Tự test**: mượn MacBook M-series, cài Parallels + Windows ARM, thử cài SEB, **quay video** | 0đ |
| 9 | **Phiên bản SEB đang dùng tại FPT** | 🔴 Trung bình | Xem trên máy của chính thành viên nhóm đã cài | 0đ |
| 10 | **Cấu hình tối thiểu chính thức để chạy EOS** | 🔴 Trung bình | Hỏi Helpdesk IT campus ĐN | 0đ |
| 11 | **Số môn thi trung bình mỗi kỳ** | 🔴🔴 Cao | Đếm từ lộ trình học của chính nhóm | 0đ |
| 12 | **Tần suất & hình thức Progress Test** | 🔴 Trung bình | Từ trải nghiệm của nhóm + hỏi giảng viên | 0đ |
| 13 | Số SV FPT Polytechnic Đà Nẵng | 🟡 Thấp | Liên hệ cơ sở FPT Polytechnic ĐN | 0đ |
| 14 | Địa điểm thi TOPIK tại Đà Nẵng | 🟡 Thấp | Website TOPIK VN / Trung tâm Văn hoá Hàn Quốc | 0đ |
| 15 | Trung tâm Pearson VUE cụ thể tại ĐN (tên, địa chỉ) | 🟡 Thấp | Tra trên pearsonvue.com | 0đ |
| 16 | Coursera proctored exam tại VN | 🟡 Thấp | Tra trực tiếp | 0đ |

> **💡 Điểm đáng chú ý: 16/16 hạng mục đều lấy được với chi phí 0 đồng, vì nhóm là sinh viên FPT Đà Nẵng.** Đây là **lợi thế không công bằng (unfair advantage)** của nhóm — nên nói rõ trong proposal.

## 10.2. 📋 Bảng khảo sát sơ cấp đề xuất (dữ liệu quan trọng nhất của cả proposal)

**Mẫu tối thiểu n = 100; lý tưởng n = 200** (≈4% dân số SV ĐH FPT ĐN ước tính) → sai số ~±7% ở độ tin cậy 95%.

| # | Câu hỏi | Dùng để làm gì |
|---|---|---|
| 1 | Bạn dùng laptop gì để thi EOS? (Windows / MacBook Intel + Bootcamp / **MacBook M-series** / khác) | **Định lượng nhóm khách hàng LTV cao nhất** |
| 2 | ⭐ Trong 12 tháng qua, laptop của bạn có gặp sự cố (hỏng, hết pin, lỗi phần mềm) **vào đúng ngày thi hoặc sát ngày thi** không? (Có/Không) | **CON SỐ QUAN TRỌNG NHẤT CỦA CẢ PROPOSAL** — là tỷ lệ chuyển đổi nền của mô hình doanh thu |
| 3 | Nếu có, bạn xử lý thế nào? (mượn bạn / hoãn thi / thi lại / đi thuê / bỏ thi / khác) | Đo **quy mô giải pháp thay thế** (mượn bạn = đối thủ thật sự) |
| 4 | Nếu có dịch vụ cho thuê laptop đã cài sẵn EOS, giao tận campus, bạn sẵn sàng trả bao nhiêu cho 1 ngày thi? (<100k / 100–150k / 150–200k / >200k) | **Xác thực mức giá** — trả lời trực tiếp phản biện "sao đắt hơn đối thủ" |
| 5 | Bạn đã biết dịch vụ cho thuê laptop nào ở Đà Nẵng chưa? | Đo **độ nhận biết của đối thủ** |
| 6 | *(bổ sung)* Bạn có biết trường có hệ thống "ĐK Mượn máy" không? Đã từng dùng chưa? | Kiểm chứng phát hiện ở mục 3.3 bằng dữ liệu sơ cấp |
| 7 | *(bổ sung)* Nếu trượt 1 môn vì hỏng máy, bạn ước tính thiệt hại bao nhiêu tiền? | Lấy **con số phí học lại thật** từ người từng trải qua |

## 10.3. 🚨 Sáu rủi ro lớn nhất của mô hình — nêu thẳng trong proposal

| # | Rủi ro | Vì sao nghiêm trọng |
|---|---|---|
| 1 | **Quy chế thi có thể CẤM dùng máy thuê ngoài** | Giết chết mô hình. **Phải kiểm chứng đầu tiên.** |
| 2 | **Trường có thể đã có máy dự phòng cho mượn** | Nhu cầu gần như biến mất |
| 3 | **Đối thủ thật sự là "bạn cùng phòng", không phải cửa hàng** | Giá tham chiếu của khách là **0 đồng**, không phải 29–50k |
| 4 | **Nhu cầu cực kỳ mùa vụ** — ~6 đợt/năm, máy nằm không phần lớn thời gian | Hiệu suất sử dụng tài sản thấp → phải có dòng doanh thu phụ |
| 5 | **Vốn đọng lớn** — 15 máy × ~10 triệu = **150 triệu**; 40 máy = **400 triệu**, chưa kể đệm dự phòng | Rào cản vốn với nhóm sinh viên |
| 6 | **Thị trường đã có ≥7 đối thủ tại Đà Nẵng**, giá thấp 29–50k/ngày | Phải bảo vệ được mức giá cao gấp 3–4 lần |

> Mốc giá tham chiếu nội địa cho laptop mới: **10.000.000 VNĐ/máy** (chương trình "Bank of Laptop" của Quỹ Dariu, laptop mới 100%) 🟡 — [ctsv.uit.edu.vn](https://ctsv.uit.edu.vn/bai-viet/chuong-trinh-cho-sinh-vien-muon-may-tinh-mien-phi) · [sggp.org.vn](https://www.sggp.org.vn/cho-sinh-vien-muon-laptop-mien-phi-post566364.html). Nếu mua máy cũ/refurbished, suất đầu tư sẽ thấp hơn.

---

# PHỤ LỤC A — 12 CON SỐ QUAN TRỌNG NHẤT CỦA TÀI LIỆU NÀY

| # | Con số | Giá trị | Mốc thời gian | Nhãn | Dùng ở đâu |
|---|---|---|---|---|---|
| 1 | Hệ điều hành bắt buộc để thi EOS | **Windows** (khuyến cáo Win 10); **KHÔNG hỗ trợ Mac M1/M2** | 2024–2026 | 🟢 | Slide "Vấn đề" — luận điểm cốt lõi |
| 2 | Học phí chuyên ngành ĐH FPT Đà Nẵng | **22.120.000 VNĐ/học kỳ** | 2025–2026 & 2026–2027 | 🟢 | Sức chi trả + phép tính thiệt hại |
| 3 | Giá trị học phí quy đổi cho 1 môn thi | **≈ 4.424.000 VNĐ** | suy từ 2025–2026 | 🔴 | Slide định giá — tỷ lệ 1:29 |
| 4 | Số học kỳ/năm | **3 kỳ**, mỗi kỳ **4 tháng / 15–16 tuần** | 2024–2026 | 🟢 | Mô hình mùa vụ doanh thu |
| 5 | Số đỉnh cầu/năm | **6 đợt** (3 final + 3 progress) + **1 đợt thi tiếng Anh đầu khoá** | ước tính | 🔴 | Mô hình tài chính theo mùa |
| 6 | Thời gian mượn máy tối thiểu trong hệ thống nội bộ FPT | **60 phút** | — | 🟡 | Neo cho SLA "đổi máy ≤ 60 phút" |
| 7 | SLA sửa laptop nhanh nhất đo được tại Đà Nẵng | **48 giờ** (FPT Shop) | — | 🟡 | Chứng minh **phải có máy dự phòng**, không thể dựa vào sửa chữa |
| 8 | Tỷ lệ đệm máy dự phòng đề xuất | **15%** (25 máy → 4 máy dự phòng ≈ **48 triệu VNĐ** vốn nằm im) | thiết kế | 🔴 | Bảng vốn đầu tư |
| 9 | SV ĐH FPT Đà Nẵng | **≈ 5.000 (4.500 – 6.000)** | 2025–2026 | 🔴 | SOM — **PHẢI ghi "ước tính của nhóm"** |
| 10 | Chỉ tiêu tuyển sinh ĐH FPT toàn quốc | **13.677 SV** | 2025 | 🟢 | Cơ sở ước lượng campus ĐN |
| 11 | Giá đối thủ cho thuê laptop tại Đà Nẵng | **29.000 – 50.000 VNĐ/ngày** | 2025 | 🟢 | Benchmark định giá |
| 12 | Phí học lại 1 môn tại ĐH FPT | ⚫ **KHÔNG CÓ SỐ — nhóm phải tự tra trên FAP** | — | ⚫ | **Không được bịa** |

---

# PHỤ LỤC B — DANH MỤC NGUỒN (URL thật, thu thập qua WebSearch ở các phiên trước)

### B1. Hệ thống thi EOS / SEB / FAP
- [Hướng dẫn cài đặt phần mềm thi EOS và SEB — Helpdesk FPTU](https://it.fpt.edu.vn/cantho/huong-dan-cai-dat-phan-mem-thi-eos-seb/)
- [Truy cập cổng học thuật Academic Portal (FAP) — Helpdesk FPTU](https://it.fpt.edu.vn/cantho/huong-dan-he-thong-academic-portal-fap/)
- [Hướng dẫn sử dụng phần mềm thi EOS_Client — IT HCM](https://it-hcm.fpt.edu.vn/articles.php?id=18)
- [Video hướng dẫn sử dụng phần mềm thi — IT HCM](https://it-hcm.fpt.edu.vn/articles.php?news=video-huong-dan-su-dung-phan-mem-thi&id=19)
- [⭐ Hướng dẫn mượn laptop của sinh viên trong trường — IT HCM](https://it-hcm.fpt.edu.vn/articles.php?news=huong-dan-muon-laptop-cua-sinh-vien-trong-truong&id=56)
- [HD SV sử dụng và thi trên phần mềm EOS tại Trường ĐH FPT](https://daihoc.fpt.edu.vn/tin-noi-bat-muc-tin-tuc/huong-dan-sinh-vien-su-dung-va-thi-tren-phan-mem-eos-tai-truong-dai-hoc-fpt/)
- [HD SV sử dụng và thi trên phần mềm EOS tại FPTU Hà Nội](https://daihoc.fpt.edu.vn/tin-tuc-chung-2/huong-dan-sinh-vien-su-dung-va-thi-tren-phan-mem-eos-tai-fptu-ha-noi/)
- [HD SV K18 sử dụng và thi trên EOS — kỳ thi Kiểm tra Tiếng Anh](https://daihoc.fpt.edu.vn/tin-tuc-chung-2/huong-dan-sinh-vien-k18-su-dung-va-thi-tren-phan-mem-eos-ky-thi-kiem-tra-tieng-anh/)
- [HD SV sử dụng và thi tiếng Anh xếp lớp trên phần mềm EOS](https://daihoc.fpt.edu.vn/tin-tuc-chung-2/su-kien-tin-tuc-chung-2/huong-dan-sinh-vien-su-dung-va-thi-tieng-anh-xep-lop-tren-phan-mem-eos/)
- [HDSV sử dụng và thi trên phần mềm EOS — hanoi.fpt.edu.vn](https://hanoi.fpt.edu.vn/huong-dan-sinh-vien-su-dung-va-thi-tren-phan-mem-eos.html)
- [HD SV cài đặt và sử dụng phần mềm thi trực tuyến — FPT PolySchool](https://polyschool.fpt.edu.vn/huong-dan-sinh-vien-cai-dat-va-su-dung-phan-mem-thi-truc-tuyen/)
- [Tra cứu lịch thi tiếng Anh đầu vào khoá 20 — ĐH FPT Hà Nội](https://daihoc.fpt.edu.vn/tra-cuu-lich-thi-tieng-anh-dau-vao-khoa-20-dh-fpt-ha-noi/)
- [HD làm bài thi cuối kỳ môn học trên EOS Client — Studocu](https://www.studocu.vn/vn/document/truong-dai-hoc-fpt/quan-tri-kinh-doanh/huong-dan-lam-bai-thi-cuoi-ky-tren-eos-client/27055728)
- [HD sử dụng phần mềm thi EOS Client — Studocu](https://www.studocu.vn/vn/document/truong-dai-hoc-fpt/working-in-groups/huong-dan-su-dung-eos-client/58823637)
- [HD sử dụng phần mềm thi EOS học kỳ Summer 2025 — Studocu](https://www.studocu.vn/vn/document/dai-hoc-fpt-ha-noi/english-trs3/huong-dan-su-dung-phan-mem-thi-eos-hoc-ky-summer-2025/134096866)
- [HD sử dụng phần mềm thi EOS — Studocu (bản 04/17)](https://studocu.com/vn/document/fpt-university/trs601/huong-dan-sinh-vien-su-dung-phan-mem-thi-eos/23377167)
- [FAP Mobile App Guide — Studocu](https://www.studocu.vn/vn/document/truong-dai-hoc-fpt/code-vhdl/fap-mobile-app-guide-procedures-important-notices/156254239)

### B2. Quy chế đào tạo & sổ tay sinh viên
- [Quy chế đào tạo đại học chính quy — ĐH FPT](https://daihoc.fpt.edu.vn/quy-che-dao-tao-dai-hoc-chinh-quy/)
- [Sổ tay sinh viên Trường ĐH FPT (.doc, bản 2016 — CẦN BẢN MỚI)](https://daihoc.fpt.edu.vn/en/wp-content/uploads/2017/06/So-tay-sinh-vien-FUG-2016.doc)
- [Sổ tay sinh viên FPT Polytechnic](https://caodang.fpt.edu.vn/thong-tin/sinh-vien/so-tay-sinh-vien/so-tay-sinh-vien.html)
- [Quy chế tuyển sinh hệ đại học chính quy 2025 — ĐH FPT](https://daihoc.fpt.edu.vn/quy-che-tuyen-sinh-2025/)

### B3. Lịch học / học kỳ
- [Ở FPTU, một năm học có 3 học kỳ — Fanpage Trường ĐH FPT](https://www.facebook.com/university.fpt.edu.vn/posts/1183525043803905/)
- [Thời gian học Đại học FPT: 4 năm – 9 kỳ – 4 giai đoạn](https://hanoi.fpt.edu.vn/tu-van/thoi-gian-hoc-dai-hoc-fpt.html)
- [Lộ trình đào tạo của Trường ĐH FPT](https://daihoc.fpt.edu.vn/lo-trinh-dao-tao-cua-truong-dai-hoc-fpt/)
- ["Mùa học thêm" tại Đại học FPT](https://daihoc.fpt.edu.vn/tin-tuc-chung-2/mua-hoc-them-tai-dai-hoc-fpt/)

### B4. Học phí
- [Học phí Trường ĐH FPT 2025-2026 tại các cơ sở trên cả nước — Báo Đà Nẵng](https://baodanang.vn/hoc-phi-truong-dai-hoc-fpt-2025-2026-tai-cac-co-so-tren-ca-nuoc-3151966.html)
- [Học phí Đại học FPT 2026–2027: Bảng giá chuẩn & Học bổng — jobtest.vn](https://jobtest.vn/hrblog/hoc-phi-dai-hoc-fpt)
- [Học phí Đại học FPT 2025 chính thức — Phongvu.vn](https://phongvu.vn/cong-nghe/hoc-phi-dai-hoc-fpt-2025-chinh-thuc/)
- [Học phí FPT 2026 — dienthoaivui.com.vn](https://dienthoaivui.com.vn/back-to-school-hoc-phi-fpt)
- [Học phí chính thức ĐH FPT 2026–2027 — VietJack](https://khoahoc.vietjack.com/tuyen-sinh/1392/hoc-phi-chinh-thuc-truong-dai-hoc-fpt-nam-2026-2027)
- [Học phí Trường ĐH FPT (Đà Nẵng) năm 2026 — VietJack](https://vietjack.com/thong-tin-tuyen-sinh/hoc-phi-truong-dai-hoc-fpt-da-nang.jsp)
- [Học phí đại học FPT năm 2025 — Campus Đà Nẵng](https://daihoc.fpt.edu.vn/hoc-phi-dai-hoc-fpt-nam-2025-campus-da-nang/)

### B5. Quy mô sinh viên
- [Campus Đà Nẵng — Trường Đại học FPT](https://daihoc.fpt.edu.vn/da-nang/)
- [Campus — Trường ĐH FPT](https://daihoc.fpt.edu.vn/campus/)
- [1.000 tân sinh viên ĐH FPT Đà Nẵng khai giảng năm học mới — FPT City](https://fptcity.vn/1-000-tan-sinh-vien-dai-hoc-fpt-da-nang-khai-giang-nam-hoc-moi/)
- [KTX tại ĐH FPT Đà Nẵng dành cho tân sinh viên K19](https://daihoc.fpt.edu.vn/chua-phan-loai/ky-tuc-xa-tai-dh-fpt-da-nang-danh-cho-tan-sinh-vien-k19/)
- [FPT University — Wikipedia](https://en.wikipedia.org/wiki/FPT_University)
- [Đề án và chỉ tiêu tuyển sinh ĐH FPT 2025 — situ.edu.vn](https://situ.edu.vn/de-an-va-chi-tieu-tuyen-sinh-dai-hoc-fpt/)
- [uniRank — FPT University 2026 (⚠️ số mâu thuẫn)](https://www.unirank.org/vn/uni/fpt-university/)
- [Anh Lê Trường Tùng: 2026 sẽ là năm nâng tầm toàn diện Giáo dục FPT — chungta.vn](https://chungta.vn/longform/b-anh-le-truong-tung-2026-se-la-nam-nang-tam-toan-dien-giao-duc-fpt-b-1140961.html)
- [FPT đẩy mạnh phát triển hệ thống giáo dục phổ thông — fpt.com](https://fpt.com/vi/tin-tuc/tin-fpt/fpt-day-manh-phat-trien-he-thong-giao-duc-pho-thong)
- [Lễ khai giảng 2026–2027 toàn hệ thống FPT Schools — hơn 18.000 học sinh](https://fschool.fpt.edu.vn/tung-bung-le-khai-giang-nam-hoc-2026-2027-toan-he-thong-fpt-schools-hon-18-000-hoc-sinh-cung-buoc-vao-hanh-trinh-moi/)
- [Lễ nhập học FSchools Đà Nẵng — hơn 700 học sinh](https://danang12-school.fpt.edu.vn/le-nhap-hoc-fschools-da-nang/)
- [FPT University, Da Nang Campus — International Office UI](https://international.ui.ac.id/shortcourse-fpt/)
- [Thông tin tuyển sinh CĐ FPT Polytechnic](https://tuyensinhso.vn/school/cao-dang-fpt-polytechnic.html)

### B6. Các trường khác tại Đà Nẵng
- [University of Da Nang — Wikipedia](https://en.wikipedia.org/wiki/University_of_Da_Nang)
- [US News — University of Danang](https://www.usnews.com/education/best-global-universities/university-of-danang-530596)
- [Điểm chuẩn Đại học Đà Nẵng 2025 — VnExpress](https://vnexpress.net/diem-chuan-dai-hoc-da-nang-2025-chinh-xac-nhat-4929604.html)
- [Điểm chuẩn ĐH Bách khoa Đà Nẵng 2025 — VnExpress](https://vnexpress.net/diem-chuan-dai-hoc-bach-khoa-da-nang-2025-moi-nhat-4929639.html)
- [Tuyển sinh ĐH Bách khoa – ĐH Đà Nẵng](https://tuyensinh.dut.udn.vn/)
- [VKU thông báo tuyển sinh đại học chính quy 2025](https://vku.udn.vn/vi/truong-dai-hoc-cong-nghe-thong-tin-va-truyen-thong-viet-han-thong-bao-tuyen-sinh-dai-hoc-chinh-quy-nam-2025-du-kien/)
- [VKU công bố điểm trúng tuyển 2025](https://vku.udn.vn/vi/vku-cong-bo-diem-trung-tuyen-tuyen-sinh-dai-hoc-nam-2025/)
- [Thông tin tuyển sinh ĐH Kinh tế — ĐH Đà Nẵng](https://tuyensinhso.vn/school/dai-hoc-kinh-te-dai-hoc-da-nang.html)
- [Tổng quan về Đại học Duy Tân](https://duytan.edu.vn/gioi-thieu)
- [Tuyển sinh 2025 — Đại học Duy Tân](https://tuyensinh2025.duytan.edu.vn)
- [ĐH Đông Á công bố phương thức tuyển sinh 2025](https://donga.edu.vn/tuyensinh/ts-chi-tiet/dai-hoc-dong-a-cong-bo-06-phuong-thuc-tuyen-sinh-he-chinh-quy-nam-2025-37366)
- [Greenwich Việt Nam](https://greenwich.edu.vn/)
- [Greenwich Việt Nam — Wikipedia](https://vi.wikipedia.org/wiki/Greenwich_Vi%E1%BB%87t_Nam)
- [Các trường ĐH ở Đà Nẵng — IELTS Fighter](https://ielts-fighter.com/tin-tuc/cac-truong-dai-hoc-o-da-nang_mt1641797220.html)
- [Full danh sách 17 trường Đại học tại Đà Nẵng — trangedu.com](https://trangedu.com/blog/dai-hoc-hoc-vien-tai-da-nang/)
- [Danh sách các trường Đại học ở Đà Nẵng 2025 — Tuyển Sinh Số](https://tuyensinhso.vn/khu-vuc/khu-vuc-da-nang-c11808.html)
- [Thông báo tuyển sinh CĐ chính quy 2025 — CĐ Đại Việt Đà Nẵng](https://daivietdanang.edu.vn/dao-tao/bai-viet/thong-bao-tuyen-sinh-cao-dang-chinh-quy-nam-2025-1037.html)
- [SEA Event — Cho thuê hơn 100 laptop phục vụ đào tạo tại ĐH Bách Khoa Đà Nẵng](https://seaevent.vn/cho-thue-laptop-phuc-vu-dao-tao-tai-truong-dai-hoc-bach-khoa-da-nang/)

### B7. Thi chứng chỉ
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

### B8. SLA sửa chữa & đối thủ cho thuê tại Đà Nẵng
- [Gói bảo hành rơi vỡ điện thoại, laptop tại FPT Shop (SLA 24h HN/HCM, **48h Đà Nẵng**)](https://fptshop.com.vn/tin-tuc/tin-khuyen-mai/goi-bao-hanh-roi-vo-dien-thoai-laptop-tai-fpt-shop-gia-chi-tu-79000-dong-137045)
- [Cho thuê laptop sinh viên giá rẻ Đà Nẵng — leminhSTORE (từ 38.000đ/ngày)](https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html)
- [Cho thuê laptop 2025 — MIT Group (từ 29.000đ/ngày)](https://mitgroup.vn/cho-thue-laptop/)
- [Cho thuê laptop Đà Nẵng theo ngày — Trương Giang (từ 50.000đ/ngày)](https://truonggiang.vn/cho-thue-laptop.html)
- [Dịch vụ cho thuê laptop tại Đà Nẵng — Đình Hậu Computer](https://maytinhdinhhau.vn/dich-vu-cho-thue-laptop-tai-da-nang/)
- [Dịch vụ cho thuê máy tính laptop tại Đà Nẵng — Sky Computer](https://skycomputer.vn/dich-vu/cho-thue-may-tinh-laptop-tai-da-nang/)
- [Top 7 dịch vụ cho thuê laptop Đà Nẵng — danang.plus](https://danang.plus/thue-laptop/)

### B9. Chương trình cho mượn laptop tại Việt Nam (mốc giá tham chiếu)
- [Chương trình cho sinh viên mượn máy tính miễn phí — CTSV, ĐH CNTT ĐHQG TP.HCM](https://ctsv.uit.edu.vn/bai-viet/chuong-trinh-cho-sinh-vien-muon-may-tinh-mien-phi)
- [Cho sinh viên mượn laptop miễn phí — SGGP](https://www.sggp.org.vn/cho-sinh-vien-muon-laptop-mien-phi-post566364.html)

---

*Tài liệu lập ngày **14/09/2026**. Tổng hợp từ kho dữ liệu đã thu thập ở các nhiệm vụ nghiên cứu trước (03, 08, 10); phiên này đã hết hạn mức WebSearch nên không phát sinh nguồn mới.*
*Mọi số gắn nhãn 🔴 là **ước lượng của nhóm nghiên cứu** — bắt buộc ghi rõ trong proposal. Mọi số gắn nhãn 🟡 **phải mở URL gốc kiểm chứng lại** trước khi nộp. Mọi ô gắn ⚫ là **không có dữ liệu — tuyệt đối không được điền số vào**.*
