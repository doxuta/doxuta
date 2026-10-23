# 12 — KHẢO SÁT UX/UI & CẤU TRÚC TRANG CỦA CÁC WEBSITE THAM CHIẾU
## Đầu vào để thiết kế giao diện website "Cho thuê laptop đi thi" — ĐH FPT Đà Nẵng

> **Phục vụ:** Proposal môn Khởi nghiệp — website cho thuê laptop đi thi, quy mô 15–40 máy, quanh ĐH FPT Đà Nẵng (P. Ngũ Hành Sơn, TP. Đà Nẵng — tên phường mới từ 01/07/2025).
> **Ngày lập:** 14/09/2026
> **Bối cảnh đã xác minh:** SV FPT thi trên máy cá nhân bằng EOS + Safe Exam Browser, **bắt buộc Windows**; Mac M1/M2 không thi được.

---

## 0. ⚠️ CẢNH BÁO PHƯƠNG PHÁP — BẮT BUỘC ĐỌC TRƯỚC

Đây là điều kiện trung thực của tài liệu. **Người viết proposal phải đọc mục này trước khi trích bất cứ dòng nào.**

### 0.1. Hai giới hạn công cụ chồng lên nhau

| # | Giới hạn | Hệ quả |
|---|---|---|
| **1** | **WebFetch/curl bị chặn hoàn toàn** bởi chính sách egress của môi trường (lỗi `EGRESS_BLOCKED`, `CONNECT tunnel failed, response 403`) | **KHÔNG mở được bất kỳ trang web nào** để xem giao diện thật, chụp màn hình, hay đọc HTML/sitemap |
| **2** | 🔴 **Ngân sách WebSearch của phiên đã CẠN (200/200 lượt) TRƯỚC KHI nhiệm vụ này bắt đầu** | **Nhiệm vụ này thực hiện được 0 (KHÔNG) truy vấn tìm kiếm mới.** Toàn bộ nội dung dưới đây là **khai thác lại kho dữ liệu do các nhiệm vụ nghiên cứu trước trong cùng phiên thu thập** (các file `01`, `02`, `03`, `10` trong cùng thư mục), cộng với phần **tổng hợp/thiết kế của người nghiên cứu** |

### 0.2. Điều này có nghĩa gì với độ tin cậy

- **URL trong tài liệu này là URL THẬT**, do WebSearch trả về trong các nhiệm vụ trước của phiên. **Không có URL bịa.**
- **NHƯNG:** không một trang nào được mở ra để xem. Mọi mô tả về "trang này có gì" đều suy ra từ **tiêu đề trang, đường dẫn URL, và đoạn trích (snippet)** — **KHÔNG phải từ việc nhìn thấy giao diện**.
- Vì vậy, phần mô tả UX ở đây trả lời được câu hỏi **"website đó CÓ những trang nào, bán thông điệp gì"**, nhưng **KHÔNG trả lời được** câu hỏi *"nút bấm đặt ở đâu, màu gì, form có mấy ô"*.

### 0.3. Ký hiệu độ tin cậy dùng xuyên suốt

| Ký hiệu | Ý nghĩa |
|---|---|
| `[S]` | Rút từ **snippet/tiêu đề/URL** do WebSearch trả về ở nhiệm vụ trước — **chưa mở trang** |
| `[URL-IA]` | **Suy luận cấu trúc trang từ chính đường dẫn URL** (ví dụ `/thue-laptop-khong-coc` ⇒ site có một landing page riêng về chủ đề "không cọc"). Đây là suy luận **khá chắc** vì URL là dữ kiện thật, nhưng vẫn là suy luận |
| **`[TK]`** | 🟠 **THIẾT KẾ / ĐỀ XUẤT của người nghiên cứu** — **KHÔNG PHẢI DỮ LIỆU**, không phải điều website nào đó đang làm. Đây là phần sáng tạo để nhóm dùng, nhưng **không được trích như "theo nghiên cứu thì..."** |
| 🔴 | **Chưa nghiên cứu được** — nằm ở [Mục 14](#14--những-phần-chưa-nghiên-cứu-được--truy-vấn-cần-chạy-lại) |

### 0.4. 🔴 Bốn nhóm nguồn trong đề bài KHÔNG nghiên cứu được

Do hết ngân sách tìm kiếm, **4 nhóm sau hoàn toàn chưa có dữ liệu** và nhóm phải tự tra:

1. **Snipe-IT demo** (giao diện quản trị tài sản)
2. **LibCal / Springshare equipment booking** (giao diện đặt lịch mượn thiết bị thư viện)
3. **Baymard Institute** (nghiên cứu UX checkout — số liệu tỷ lệ bỏ giỏ hàng, lỗi form)
4. **Nielsen Norman Group (NN/g)** (nguyên tắc UX booking flow, trust signals)

👉 **Tôi CỐ TÌNH KHÔNG ghi URL phỏng đoán cho 4 nhóm này**, kể cả những URL "ai cũng biết". Quy tắc của tài liệu là URL phải do tìm kiếm trả về. Truy vấn cụ thể để nhóm chạy lại nằm ở [Mục 14](#14--những-phần-chưa-nghiên-cứu-được--truy-vấn-cần-chạy-lại).

---

## 1. TÓM TẮT ĐIỀU HÀNH — 6 PHÁT HIỆN CHÍNH

| # | Phát hiện | Hàm ý thiết kế giao diện |
|---|---|---|
| **1** | **Toàn bộ ~20 website cho thuê laptop VN khảo sát được đều là "website catalogue + hotline", KHÔNG phải "website đặt hàng"** `[URL-IA]`. Không tìm thấy bất kỳ dấu vết nào của trang giỏ hàng, trang chọn ngày, trang thanh toán, hay tài khoản người dùng trên các domain này | 👉 **Đây là khoảng trống UX lớn nhất và là điểm khác biệt rẻ nhất để giành.** Chỉ cần có **lịch chọn ca thi + xác nhận tự động**, sản phẩm đã vượt 100% đối thủ nội địa về trải nghiệm |
| **2** | Cấu trúc IA của ngành cho thuê laptop VN rất nhất quán: **trang chủ → landing theo TỈNH → landing theo ĐỐI TƯỢNG (sinh viên/doanh nghiệp/sự kiện) → landing theo CHÍNH SÁCH ("không cọc") → bảng giá → tin tức SEO** `[URL-IA]` | 👉 Đây là **bản đồ SEO đã được thị trường kiểm chứng**. Nhóm nên sao chép cấu trúc này nhưng thu hẹp: thay "theo tỉnh" bằng **"theo CA THI"** |
| **3** | **Grover thay tiền cọc bằng "cọc danh tính"**: soft credit check + upload giấy tờ + selfie cầm giấy tờ + khớp địa chỉ giao hàng `[S]` ([Grover Help — credit check](https://service.grover.com/hc/en-us/articles/19920531898642-How-does-Grover-s-credit-check-work), [Identity Verification](https://service.grover.com/hc/en-us/articles/35704298814866-Identity-Verification)) | 👉 Bản sao cho FPT: **đăng nhập @fpt.edu.vn + ảnh thẻ SV** thay cho cọc. Cần một **màn hình xác minh riêng**, không nhét vào form đặt hàng |
| **4** | **Turo công khai con số cụ thể cho từng mốc thời gian**: giữ cọc **24–48h trước chuyến**, tự hoàn **80 giờ sau chuyến** `[S]` ([Turo Help — Security deposits](https://help.turo.com/en_us/security-deposits-us-HkbE44lE9)) | 👉 Bài học UX mạnh nhất: **mọi cam kết thời gian phải là SỐ, hiển thị ngay trên màn hình**, không phải "sẽ hoàn sớm". Giảm mạnh tin nhắn hỏi han |
| **5** | **Getaround bị Tổng Chưởng lý Washington DC xử lý vì KHÔNG công bố rõ các trường hợp LOẠI TRỪ bảo hiểm** `[S]` ([oag.dc.gov](https://oag.dc.gov/release/attorney-general-schwalb-secures-refunds-dc)) | 👉 Quy tắc bố cục bắt buộc: khối **"NHỮNG TRƯỜNG HỢP KHÔNG ĐƯỢC MIỄN TRỪ"** phải nằm **ĐẦU** trang điều khoản và **trong luồng checkout**, không giấu ở footer |
| **6** | **ĐH FPT ĐÃ có sẵn một hệ thống web cho SV mượn laptop của SV khác "để dùng hoặc đi thi"**, có Dashboard, nút "ĐK Mượn máy", nút "Trả máy", xác nhận 2 bước `[S]` ([it-hcm.fpt.edu.vn](https://it-hcm.fpt.edu.vn/articles.php?news=huong-dan-muon-laptop-cua-sinh-vien-trong-truong&id=56)) | 👉 **Đây là tham chiếu UX gần nhất và quan trọng nhất.** Sinh viên FPT **đã quen mô hình tương tác này**. Sao chép từ vựng giao diện của trường ("Dashboard", "ĐK Mượn máy", "Trả máy") sẽ giảm chi phí học của người dùng gần bằng 0 |

---

## 2. NHÓM A — WEBSITE CHO THUÊ LAPTOP/THIẾT BỊ TẠI VIỆT NAM

### 2.1. Bảng 1 — 12 website tham chiếu, URL thật, và các trang quan sát được

Đề bài yêu cầu ít nhất 6 site; dưới đây là **12 site có URL thật**.

| # | Đơn vị | URL gốc (thật) | Các trang/loại trang xác định được | Cách đặt hàng quan sát được |
|---|---|---|---|---|
| 1 | **thuelaptop.com.vn** (Cty Phương Châu) | [thuelaptop.com.vn](https://thuelaptop.com.vn/) | Trang chủ; [bảng giá laptop văn phòng](https://thuelaptop.com.vn/bang-gia-cho-thue-laptop-van-phong.html); [bảng giá laptop đồ hoạ](https://thuelaptop.com.vn/bang-gia-cho-thue-laptop-do-hoa.html); [landing theo tỉnh: Đà Nẵng](https://thuelaptop.com.vn/dia-diem-cho-thue-laptop-tai-da-nang-gia-re.html); [landing chính sách: SV thuê không cần cọc](https://thuelaptop.com.vn/cho-sinh-vien-thue-may-tinh-khong-can-dat-coc.html); [landing sản phẩm: laptop gaming](https://thuelaptop.com.vn/dich-vu-cho-thue-laptop-gaming.html) `[URL-IA]` | **Hotline 0936 228 200** `[S]` — không thấy dấu vết trang đặt hàng |
| 2 | **ictsaigon.com.vn** | [ictsaigon.com.vn/cho-thue-laptop](https://ictsaigon.com.vn/cho-thue-laptop) | Trang dịch vụ tổng; [trang sản phẩm theo MODEL cụ thể](https://ictsaigon.com.vn/cho-thue-laptop-hp-elitebook-9480m); [landing "thuê laptop không cọc"](https://ictsaigon.com.vn/thue-laptop-khong-coc); [landing gaming](https://ictsaigon.com.vn/thue-laptop-gaming); [landing PC để bàn](https://ictsaigon.com.vn/cho-thue-pc-may-tinh-de-ban); [bài kiến thức "kinh nghiệm thuê laptop uy tín"](https://ictsaigon.com.vn/kinh-nghiem-thue-laptop-uy-tin-dam-bao) `[URL-IA]` | **Hotline 0906 652 739** `[S]` |
| 3 | **mitgroup.vn** | [mitgroup.vn/cho-thue-laptop/](https://mitgroup.vn/cho-thue-laptop/) | Trang dịch vụ tổng; [landing "không cọc"](https://mitgroup.vn/thue-laptop-khong-coc/); [landing "thuê laptop sinh viên"](https://mitgroup.vn/thue-laptop-sinh-vien/) `[URL-IA]` | Không xác định `[S]` |
| 4 | **skylap.vn** | [skylap.vn/dich-vu-cho-thue/cho-thue-laptop/](https://skylap.vn/dich-vu-cho-thue/cho-thue-laptop/) | **Có cấu trúc phân cấp rõ nhất**: `/dich-vu-cho-thue/` là danh mục cha → [`/cho-thue-laptop-dell-van-phong/`](https://skylap.vn/dich-vu-cho-thue/cho-thue-laptop-dell-van-phong/) là danh mục con theo HÃNG → [`/thue-laptop-dell-precision-core-i7-7700hq/`](https://skylap.vn/thue-laptop-dell-precision-core-i7-7700hq/) là **trang chi tiết theo MODEL** `[URL-IA]` | Không xác định `[S]` |
| 5 | **laptopsgn.com** | [laptopsgn.com/cho-thue-laptop/](https://laptopsgn.com/cho-thue-laptop/) | Trang dịch vụ; [chuyên mục tin tức `/tin-tuc/`](https://laptopsgn.com/tin-tuc/dich-vu-cho-thue-laptop-tphcm-gia-re-giao-2h/); [bài "thuê laptop sinh viên"](https://laptopsgn.com/tin-tuc/thue-laptop-sinh-vien/) `[URL-IA]` | **Hotline 0906 961 347 + email**. ⭐ Trang công bố **SLA "giao trong 2 GIỜ kể từ khi XÁC NHẬN ĐƠN"** — hàm ý có bước "xác nhận đơn" thủ công `[S]` |
| 6 | **saolatech.com.vn** | [saolatech.com.vn](https://saolatech.com.vn/) | ⭐ [**Bảng giá thuê công khai** dạng trang riêng](https://saolatech.com.vn/bang-gia-thue-3425667); [landing "không cọc tại Hà Nội"](https://saolatech.com.vn/thue-laptop-khong-can-dat-coc-tai-ha-noi-giai-phap-tiet-kiem-cho-sinh-vien-3425752); [landing "thuê laptop cho sinh viên"](https://saolatech.com.vn/thue-laptop-cho-sinh-vien-giai-phap-tien-loi-tiet-kiem-va-hien-dai-3425768) `[URL-IA]` | Không xác định. **URL kết thúc bằng ID số (`-3425667`) ⇒ chạy trên CMS dựng sẵn**, không phải web tự code `[URL-IA]` |
| 7 | **leminhstore.vn** (Đà Nẵng) | [leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html](https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html) | Trang "thuê laptop sinh viên Đà Nẵng"; [trang "thuê PC Gaming/Workstation Đà Nẵng"](https://leminhstore.vn/thue-pc-gaming-da-nang-104910u.html) `[URL-IA]` | **Điện thoại/SMS/Zalo 0915 819 967**, hotline 0236 7777 999. Trang **công bố GIỜ MỞ CỬA** (T2–T7 08:00–12:00 & 13:30–19:00; CN 08:30–12:00 & 13:30–17:30) `[S]` |
| 8 | **truonggiang.vn** (Đà Nẵng) | [truonggiang.vn/cho-thue-laptop.html](https://truonggiang.vn/cho-thue-laptop.html) | Trang dịch vụ thuê; đồng thời là site **bán laptop cũ** — [trang sản phẩm máy cũ](https://truonggiang.vn/laptop-cu-dell-3500-i5-8250) `[URL-IA]` | **Hotline 1900 2007 + Zalo 0972.0909.49 + email** `[S]` |
| 9 | **maytinhdinhhau.vn** (Đà Nẵng) | [maytinhdinhhau.vn/dich-vu-cho-thue-laptop-tai-da-nang/](https://maytinhdinhhau.vn/dich-vu-cho-thue-laptop-tai-da-nang/) | Trang dịch vụ; [landing đối tượng "địa chỉ cho SINH VIÊN thuê laptop giá rẻ tại Đà Nẵng"](https://maytinhdinhhau.vn/dia-chi-cho-sinh-vien-thue-laptop-gia-re-tai-da-nang/) `[URL-IA]` | **2 số điện thoại** 0948 637 037 / 0984 637 037 `[S]` |
| 10 | **chothuelaptop.com.vn** (Đà Nẵng) | [chothuelaptop.com.vn/thue-laptop-da-nang/](https://chothuelaptop.com.vn/thue-laptop-da-nang/) | Landing theo tỉnh; [landing theo KỲ HẠN "thuê laptop theo tháng"](https://chothuelaptop.com.vn/thue-laptop-theo-thang/) `[URL-IA]` | Không xác định `[S]` |
| 11 | **thuelaptop.vn** | [thuelaptop.vn/thue-laptop-da-nang-gia-re-chi-tu-10k/](https://www.thuelaptop.vn/thue-laptop-da-nang-gia-re-chi-tu-10k/) | Landing theo tỉnh **có GIÁ NHÚNG THẲNG VÀO URL** (`-chi-tu-10k`); ⭐ [**trang "chính sách kinh doanh cho thuê thiết bị"** nằm trong mục `/gioi-thieu/`](https://www.thuelaptop.vn/gioi-thieu/chinh-sach-kinh-doanh-cho-thue-thiet-bi/) `[URL-IA]` | Không xác định `[S]` |
| 12 | **phuongnamco.com** | [phuongnamco.com](https://phuongnamco.com/) | ⭐⭐ **Đối thủ khái niệm gần nhất**: [landing "Cho thuê laptop THI CỬ — giải pháp hữu ích cho sinh viên MÙA THI"](https://phuongnamco.com/cho-thue-laptop-thi-cu-giai-phap-huu-ich-cho-sinh-vien-mua-thi/) `[URL-IA]` | Không xác định `[S]` |

**Site bổ sung có URL thật** (chưa phân tích sâu): [seaevent.vn](https://seaevent.vn/cho-thue-laptop-su-kien-tai-da-nang/) và [case study cho ĐH Bách Khoa ĐN](https://seaevent.vn/cho-thue-laptop-phuc-vu-dao-tao-tai-truong-dai-hoc-bach-khoa-da-nang/) · [skycomputer.vn](https://skycomputer.vn/dich-vu/cho-thue-may-tinh-laptop-tai-da-nang/) · [xooevent.com](https://xooevent.com/cho-thue-laptop-may-tinh-so-luong-lon-tai-da-nang/) · [laptopchothue.com](https://laptopchothue.com/) và [trang Đà Nẵng](https://laptopchothue.com/dich-vu-cho-thue-laptop-tai-da-nang-laptop-cau-hinh-cao-gia-tot/) · [tinhocpnn.com](https://tinhocpnn.com/bang-gia-cho-thue-laptop-may-tinh-gia-re/) · [vietbis.vn](https://vietbis.vn/tin-tuc/thue-laptop-khong-can-dat-coc-tai-ha-noi-dieu-kien-ap-dung-3116.html) · [bk4.com.vn](https://bk4.com.vn/dich-vu-cho-thue-laptop-theo-ngay-tai-ha-noi/) · [laptopthienan.com](https://laptopthienan.com/cho-thue-laptop-may-tinh-hcm-gia-re-50k.html) · [chothuelaptop.info](https://chothuelaptop.info/cho-thue-laptop-da-nang-thu-tuc-nhanh-gon/) · [chothuemaytinh.vn](https://chothuemaytinh.vn/cho-thue-laptop-sinh-vien/) · [quangtin.com](https://quangtin.com/pages/cho-thue-may-tinh-laptop-gia-re-tai-tp-hcm-dich-vu-chuyen-nghiep) · [thietbichothue.com](https://thietbichothue.com/cho-thue-laptop/) · [kimanh.com.vn](https://www.kimanh.com.vn/linh-kien-laptop/)

### 2.2. Sitemap CHUNG của ngành cho thuê laptop Việt Nam (suy ra từ URL)

Gộp 12 site trên lại, hiện ra một **kiến trúc thông tin (IA) 6 tầng lặp đi lặp lại** `[URL-IA]`:

```
Trang chủ
├── 1. Trang DỊCH VỤ tổng            /cho-thue-laptop
├── 2. Landing theo ĐỊA PHƯƠNG        /thue-laptop-da-nang, /...-tai-ha-noi
├── 3. Landing theo ĐỐI TƯỢNG         /thue-laptop-sinh-vien, /cho-thue-laptop-su-kien,
│                                     /cho-thue-laptop-thi-cu   ← chỉ 1 site có
├── 4. Landing theo CHÍNH SÁCH        /thue-laptop-khong-coc    ← xuất hiện ở 4+ site
├── 5. Landing theo SẢN PHẨM/KỲ HẠN   /cho-thue-laptop-gaming, /thue-laptop-theo-thang,
│   └── Trang chi tiết theo MODEL     /thue-laptop-dell-precision-core-i7-7700hq
├── 6. BẢNG GIÁ (trang riêng)         /bang-gia-cho-thue-laptop-van-phong
└── 7. Blog/Tin tức SEO               /tin-tuc/..., /kinh-nghiem-thue-laptop-uy-tin
    └── (hiếm) Chính sách kinh doanh  /gioi-thieu/chinh-sach-kinh-doanh-cho-thue-thiet-bi
```

### 2.3. 🔑 Phát hiện quan trọng nhất về UX ngành VN: **KHÔNG CÓ AI ĐẶT HÀNG ONLINE**

Trong toàn bộ ~40 URL thu thập được từ 20 nhà cung cấp, **không xuất hiện một URL nào** thuộc các mẫu đặc trưng của thương mại điện tử:

| Mẫu URL đặc trưng của đặt hàng online | Số lần xuất hiện |
|---|---|
| `/gio-hang`, `/cart`, `/checkout`, `/thanh-toan` | **0** |
| `/dang-nhap`, `/login`, `/tai-khoan`, `/account` | **0** |
| `/dat-hang`, `/booking`, `/dat-lich`, `/reservation` | **0** |
| `/lich`, `/calendar`, `/tra-cuu-don` | **0** |

**Bằng chứng gián tiếp củng cố kết luận này:** tín hiệu chuyển đổi (conversion) mà các site đặt lên trang là **số điện thoại, Zalo, email, và GIỜ MỞ CỬA CỬA HÀNG** — cả 4 đều là tín hiệu của **kênh thoại/nhắn tin**, không phải kênh tự phục vụ `[S]`. Riêng laptopsgn.com nói *"giao trong 2 giờ kể từ khi **xác nhận đơn**"* — cụm "xác nhận đơn" hàm ý **có một con người gọi lại xác nhận**, chứ không phải hệ thống tự chốt `[S]`.

> ⚠️ **Giới hạn của kết luận này:** đây là suy luận từ việc **thiếu vắng URL**, không phải từ việc mở trang và xác nhận không có nút "Đặt ngay". Có thể một site nào đó **có form đặt hàng nhúng ngay trong trang dịch vụ** (dạng popup hoặc form dưới bài) mà URL không phản ánh. **Nhóm phải mở 5 site và kiểm chứng bằng mắt** — xem [Mục 14](#14--những-phần-chưa-nghiên-cứu-được--truy-vấn-cần-chạy-lại).

> 🟠 **`[TK]` HÀM Ý CHIẾN LƯỢC:** nếu kết luận này đúng, thì **chỉ riêng việc có một lịch đặt ca thi hoạt động được** đã là lợi thế cạnh tranh về sản phẩm — và nó **gần như miễn phí để xây** (Google Form + Sheet ở mức MVP). Trong proposal, đây là luận điểm mạnh hơn nhiều so với "giá rẻ hơn".

### 2.4. Thông tin mà các site VN hiển thị (dùng làm checklist nội dung trang sản phẩm)

Tổng hợp các trường dữ liệu xuất hiện lặp lại trên trang dịch vụ/bảng giá của các site trên `[S]`:

| Trường thông tin | Ví dụ thực tế thu thập được | Nguồn |
|---|---|---|
| **Cấu hình cụ thể theo model** | "HP Elitebook 9480m — i5-4310U, 8GB DDR3, SSD 240GB, 14" FHD" | [ictsaigon.com.vn](https://ictsaigon.com.vn/cho-thue-laptop-hp-elitebook-9480m) |
| **Giá theo 3 kỳ hạn: NGÀY / TUẦN / THÁNG** | 49.000đ / 300.000đ / 600.000đ | [skylap.vn](https://skylap.vn/dich-vu-cho-thue/cho-thue-laptop-dell-van-phong/), [ictsaigon.com.vn](https://ictsaigon.com.vn/cho-thue-laptop-hp-elitebook-9480m) |
| **Mức cọc, dạng khoảng** | "500.000đ – 2.000.000đ tuỳ dòng máy & thời gian, hoàn 100% khi trả đúng tình trạng" | [leminhstore.vn](https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html) |
| **Giấy tờ chấp nhận (dạng HOẶC)** | "CCCD/CMND **HOẶC** GPLX **HOẶC** SIM chính chủ" — chỉ cần 1 trong 3 | [laptopsgn.com](https://laptopsgn.com/cho-thue-laptop/) |
| **Chiết khấu theo nhóm** | "Giảm 10–20% cho nhóm 2–10 bạn" | [leminhstore.vn](https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html) |
| **Cam kết giao hàng (SLA)** | "Trong 2 GIỜ kể từ khi xác nhận đơn" / "Giao trong ngày" / "Miễn phí vận chuyển và lắp đặt" | [laptopsgn.com](https://laptopsgn.com/tin-tuc/dich-vu-cho-thue-laptop-tphcm-gia-re-giao-2h/), [truonggiang.vn](https://truonggiang.vn/cho-thue-laptop.html), [maytinhdinhhau.vn](https://maytinhdinhhau.vn/dich-vu-cho-thue-laptop-tai-da-nang/) |
| **Cam kết đổi máy khi lỗi** | "Đổi máy hoặc nâng cấu hình không mất thêm chi phí" | [mitgroup.vn](https://mitgroup.vn/cho-thue-laptop/) |
| **Hỗ trợ kỹ thuật 24/7** | Xuất hiện ở ≥3 site | [laptopsgn.com](https://laptopsgn.com/cho-thue-laptop/), [maytinhdinhhau.vn](https://maytinhdinhhau.vn/dich-vu-cho-thue-laptop-tai-da-nang/) |
| **Quy trình kiểm tra trước bàn giao** | "Máy được kiểm tra kỹ để đảm bảo Windows và phần mềm cơ bản sẵn sàng, **pin ổn định**, ngoại hình sạch sẽ" | [laptopsgn.com](https://laptopsgn.com/cho-thue-laptop/) |
| **Giờ mở cửa cửa hàng** | Ghi chi tiết theo thứ trong tuần | [leminhstore.vn](https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html) |
| ⚠️ **Điều khoản BẤT LỢI (phản ví dụ)** | SAOLA: "ký thuê theo tuần/tháng nhưng **trả sớm hơn thì vẫn phải trả đủ giá trị hợp đồng**" | [saolatech.com.vn](https://saolatech.com.vn/bang-gia-thue-3425667) |

---

## 3. NHÓM B — GROVER.COM (ĐỨC): LUỒNG ĐĂNG KÝ, KIỂM TRA TÍN DỤNG, CHECKOUT, HƯ HỎNG

> Nguồn gốc là help center chính chủ (các bài trên tên miền `service.grover.com`, liệt kê ở bảng 3.1) và trang sản phẩm — **nhưng cả hai đều KHÔNG mở được** (`EGRESS_BLOCKED`). Toàn bộ dưới đây là `[S]`.

### 3.1. Các trang/khu vực xác định được trên grover.com

| Khu vực | URL thật | Vai trò trong luồng |
|---|---|---|
| Trang "Cách hoạt động" | [grover.com/us-en/how-it-works](https://www.grover.com/us-en/how-it-works) | **Trang giáo dục mô hình** — đứng trước cả catalogue |
| Trang chi tiết sản phẩm (PDP) | [MacBook Air M2](https://www.grover.com/de-en/products/apple-laptop-macbook-air-m2-8gb-256gb-ssd-10-core-gpu), [MacBook Pro 13 M2](https://www.grover.com/de-en/products/apple-macbook-pro-13-3-m2-8cpu-16gb-512gb-10gpu-67w) | Hiển thị giá dạng **"từ X EUR/tháng"** — giá của gói THUÊ DÀI NHẤT (12 tháng), là **neo giá (price anchoring)** rồi upsell `[S]` |
| Trang chính sách bảo vệ | [grover.com — Grover Care](https://www.grover.com/us-en/g-about/grover-care) | Giải thích gói miễn trừ hư hỏng |
| Trang tình trạng thiết bị | [grover.com — Signs of use / Asset condition](https://www.grover.com/at-en/g-about/asset-condition) | ⭐ **Trang tách bạch "hao mòn thường" vs "hư hỏng"** |
| Trang B2B | [grover.com/de-en/for-business](https://www.grover.com/de-en/for-business) | Kỳ hạn 6/12/18 tháng, >10.000 DN |
| Trang bền vững | [grover.com — sustainable tech](https://www.grover.com/de-en/g-explore/sustainable-tech) | Câu chuyện thương hiệu "Rent. Return. Reuse." |
| Help center | [service.grover.com](https://service.grover.com/hc/en-us/articles/19920531898642-How-does-Grover-s-credit-check-work) và các bài liên quan | Xem bảng 3.2 |

### 3.2. Luồng đăng ký + kiểm tra tín dụng — "bức tường xác minh 3 lớp"

**Grover KHÔNG thu tiền đặt cọc.** Khách chỉ trả tháng đầu tiên rồi máy được giao `[S]`. Thay vào đó `[S]`:

| Lớp | Nội dung | Thời gian | Nguồn |
|---|---|---|---|
| **Lớp 1 — Credit check** | Chạy **soft credit check qua CRIF Bürgel và Schufa** (2 cơ quan tín dụng Đức) ngay khi đặt đơn. Vì là truy vấn "Anfrage Kreditkonditionen" nên **không làm giảm điểm Schufa** của khách | **Vài phút, tối đa 1 ngày làm việc** | [Grover Help — credit check](https://service.grover.com/hc/en-us/articles/19920531898642-How-does-Grover-s-credit-check-work); [Gründer Vision](https://gruender-vision.de/grover-schufa-alles-was-du-wissen-solltest/) |
| **Lớp 2 — ID verification (chỉ khi hệ thống nghi ngờ)** | Upload ảnh hộ chiếu/CCCD, **hoặc** ảnh chụp sao kê ngân hàng. Với cá nhân: yêu cầu **ảnh selfie cầm mặt trước giấy tờ giơ lên camera, thấy rõ ĐỒNG THỜI cả mặt người và giấy tờ** | — | [Grover Help — Identity Verification](https://service.grover.com/hc/en-us/articles/35704298814866-Identity-Verification), [Additional Verification](https://service.grover.com/hc/en-us/articles/19920613200914-Additional-Verification) |
| **Lớp 3 — Khớp thông tin giao hàng** | Tên đầy đủ phải **khớp chính xác với giấy tờ**; địa chỉ giao hàng phải **khớp địa chỉ đăng ký thường trú**, kể cả số tầng/số căn hộ | — | như trên |
| **Xử lý khi FAIL** | Grover **từ chối giao máy và KHÔNG nêu lý do cụ thể** (lý do bảo vệ dữ liệu cá nhân) | — | như trên |

**Nhà cung cấp công nghệ:** **Onfido** (Grover báo cáo **giảm 60% thời gian onboarding**, khách DN rút ngắn **nguyên 1 ngày** — [onfido.com/customer/grover](https://onfido.com/customer/grover/)) và **SEON** (chống gian lận — [seon.io](https://seon.io/resources/news/grover-partners-with-seon-to-verify-user-ids-as-it-expands-worldwide/)) `[S]`.

> **🔑 Bài học UX số 1 — TÁCH XÁC MINH RA KHỎI CHECKOUT.**
> Grover cho khách đi hết luồng đặt hàng **rồi mới** chạy xác minh ở nền, và **chỉ đòi giấy tờ khi có nghi ngờ** (progressive/risk-based verification). Đây là ngược lại với thiết kế ngây thơ "bắt upload CCCD ngay ở bước 1" — vốn giết chết tỷ lệ chuyển đổi.
>
> 🟠 **`[TK]` Bản sao cho dự án FPT:** bước 1 chỉ hỏi **email @fpt.edu.vn + MSSV**. Ảnh thẻ SV chỉ yêu cầu **ở lần thuê đầu tiên**, và các lần sau thì bỏ qua. Người thuê lần thứ 2 trở đi phải đi được từ mở web đến xác nhận trong **dưới 60 giây**.

### 3.3. Chính sách hư hỏng — cấu trúc và cách trình bày

| Nội dung | Chi tiết | Nguồn |
|---|---|---|
| Cấu trúc gói Grover Care | Tùy quốc gia/thời điểm: hoặc **theo %** (Care chi trả 50% hoặc 80% ⇒ khách trả 50% hoặc 20% chi phí hư hỏng), hoặc **phí cố định** (gói Basic/Premium với "repair service fee" cố định) | [Grover Help — What is Grover Care](https://service.grover.com/hc/en-us/articles/19920685566610-What-is-Grover-Care-and-how-does-it-work) |
| Hỏng không sửa được | Khách trả **20% giá bán lẻ đề xuất (RRP)** tại thời điểm bắt đầu thuê. Drone & scooter điện: **50%** | [Repair and replacement costs](https://service.grover.com/hc/en-us/articles/19918338642578-Repair-and-replacement-costs), [Drones and e-mobility](https://service.grover.com/hc/en-us/articles/19908669018002-Drones-and-e-mobility-products) |
| ⭐ **Hao mòn thường** | **Xước nhỏ và dấu hiệu sử dụng bình thường được làm sạch MIỄN PHÍ** sau khi trả | [Signs of use](https://www.grover.com/at-en/g-about/asset-condition) |
| ⭐ **Phí phạt đặc thù** | Thiết bị trả về **vẫn còn đăng nhập tài khoản người dùng (vd iCloud chưa đăng xuất)**: phạt thêm **49 EUR** | [Repair and replacement costs](https://service.grover.com/hc/en-us/articles/19918338642578-Repair-and-replacement-costs) |
| Cách tính giá sửa | Dựa trên **market-standard grading guidelines** + **database hàng nghìn ca sửa chữa** | như trên |
| Checklist kiểm tra khi thu hồi | Chuyên gia kiểm **từ mọi góc độ** về hình thức + test: **màn hình, Bluetooth, loa, camera, bàn phím** | [Signs of use](https://www.grover.com/at-en/g-about/asset-condition) |

> **🔑 Bài học UX số 2 — HAI CỘT "MIỄN PHÍ" vs "TÍNH TIỀN".**
> Cách giảm tranh chấp mạnh nhất mà Grover dùng là **công khai hoá và TÁCH ĐÔI**: một bên là hao mòn thường (miễn phí), một bên là hư hỏng (có bảng giá). Trên giao diện, điều này nên là **một bảng 2 cột đặt cạnh nhau**, không phải một đoạn văn.
>
> **Bài học số 3 — cái phí "49 EUR vì chưa đăng xuất iCloud"** cho thấy Grover học từ nỗi đau vận hành thật: *thiết bị bị khoá tài khoản = thiết bị chết*. 🟠 **`[TK]` Tương đương cho dự án:** máy trả về còn khoá Windows/BitLocker, còn tài khoản cá nhân, còn phần mềm thi chưa gỡ ⇒ phải có mục phí riêng trên bảng giá đền bù.

---

## 4. NHÓM C — FAT LLAMA & HYGGLO (P2P): LUỒNG ĐẶT, XÁC MINH, BẢO HIỂM

### 4.1. Hygglo (Thuỵ Điển) — mô hình niềm tin dựa trên định danh quốc gia

| Chỉ tiêu | Nội dung | Nguồn |
|---|---|---|
| Hoa hồng | **20%**/giao dịch (chủ đồ giữ 80%). Riêng drone **50%** | [Hygglo Help — How Hygglo works](https://help.hygglo.info/en/articles/10415333-how-hygglo-works) |
| **Xác minh danh tính** | **BankID** — hệ thống định danh điện tử QUỐC GIA của Bắc Âu | [Hygglo Help — What is Hygglo](https://help.hygglo.info/en/articles/10420308-what-is-hygglo), [Circular X](https://www.circularx.eu/en/cases/75/hygglo-peer-to-peer-rental-instead-of-buying) |
| Bảo hiểm | **Mọi giao dịch** đều bao gồm bảo vệ chống **hư hỏng bất ngờ, trộm cắp hoặc mất mát** trong thời gian thuê | [Hygglo Help — security & protection](https://help.hygglo.info/en/articles/10587214-how-to-provide-great-service-and-understand-security-protection) |
| Đơn vị bảo hiểm | **Omocom**, hoặc **Hygglo Lender Guarantee** | [Hygglo Care for lenders](https://help.hygglo.info/en/articles/12890765-hygglo-care-for-lenders) |
| Phí dùng làm gì (minh bạch) | Chi trả **bảo hiểm, xử lý thanh toán, hỗ trợ khách hàng, vận hành và phát triển nền tảng** | [Hygglo Help](https://help.hygglo.info/en/articles/10415333-how-hygglo-works) |

**Omocom — bảo hiểm nhúng, con số vàng:** **2–6 EUR/giao dịch, hạn mức bồi thường 1.000 EUR**, tích hợp bằng **API tính rủi ro thời gian thực**, chỉ bảo hiểm **trong khoảng thời gian tài sản đang được dùng/vận chuyển** ([Van Ameyde — Omocom](https://www.vanameyde.com/stories/omocom-circular-economy/), [omocom.insurance](https://www.omocom.insurance/en/), [Ellen MacArthur Foundation](https://www.ellenmacarthurfoundation.org/circular-examples/creating-trust-in-the-sharing-economy-omocom)) `[S]`.

### 4.2. Fat Llama (Anh/Mỹ) — và **mặt tối** cực kỳ hữu ích cho phần thiết kế

| Nội dung | Chi tiết | Nguồn |
|---|---|---|
| KYC | Xác minh mọi người dùng qua **2 hoặc 3 loại giấy tờ**; chủ đồ phải dùng **giấy tờ do chính phủ cấp**; **kiểm tra bổ sung với đồ giá trị cao** | [Sharetribe](https://www.sharetribe.com/create/how-to-build-website-like-fatllama/), [Yo-Rent](https://www.yo-rent.com/blog/build-p2p-rental-website-like-fat-llama/) **[nguồn yếu]** |
| Đặt cọc | **Chủ đồ tự đặt** địa điểm nhận, giới hạn sử dụng, **và mức cọc** | như trên **[nguồn yếu]** |
| Bảo hiểm | Tự quảng bá là **"marketplace P2P được bảo hiểm toàn phần đầu tiên thế giới"** | như trên **[nguồn yếu]** |
| ⚠️ **Thực tế** | Nhiều vụ trộm & tranh chấp bồi thường công khai: chủ đồ mất **>5.000 USD thiết bị ảnh**; có ca mất **1.700 GBP** không được đền; nền tảng có xu hướng lập luận *"đó là tài khoản của bạn, bạn chịu trách nhiệm"* | [PetaPixel](https://petapixel.com/2019/03/20/how-i-had-over-5000-in-camera-gear-stolen-through-fat-llama/), [DIYPhotography](https://www.diyphotography.net/i-got-5000-worth-of-gear-stolen-from-me-through-fat-llama/), [Trustpilot](https://www.trustpilot.com/review/fatllama.com), [Reviews.io](https://www.reviews.io/company-reviews/store/fatllama-com) |

> **🔑 Bài học UX số 4 — KHOẢNG CÁCH GIỮA LỜI HỨA TRÊN GIAO DIỆN VÀ THỰC TẾ CHÍNH LÀ RỦI RO THƯƠNG HIỆU.**
> Fat Llama viết "fully insured" to đùng trên trang chủ, rồi đội resolutions từ chối bồi thường ⇒ hàng loạt review 1 sao. Bài học cho giao diện: **đừng bao giờ viết một lời hứa bảo vệ mà không kèm ngay cạnh nó một link tới danh sách LOẠI TRỪ.** Xem tiếp Getaround ở [Mục 5.3](#53-getaround--bài-học-pháp-lý-về-cách-KHÔNG-được-trình-bày-bảo-hiểm).
>
> **Bài học số 5 — vì sao dự án KHÔNG nên làm P2P:** mô hình P2P chuyển toàn bộ rủi ro mất máy sang chủ đồ trong khi nền tảng ăn phí. Ở quy mô 15–40 máy, **một vụ mất laptop 15–20 triệu VND đủ giết dự án**. Hygglo chạy được P2P vì Bắc Âu **có BankID**; Anh không có ⇒ Fat Llama gian lận nhiều hơn rõ rệt.

---

## 5. NHÓM D — TURO & GETAROUND (P2P Ô TÔ): KYC, DEPOSIT/HOLD, ẢNH TRƯỚC–SAU

> **Đây là nhóm liên quan trực tiếp nhất tới mô hình của dự án**, vì cùng bài toán: *tài sản giá trị cao, giao cho người lạ, thời gian ngắn, phải chứng minh tình trạng trước–sau.*

### 5.1. Turo — cơ chế đặt cọc (deposit/hold), chi tiết kỹ thuật

| Nội dung | Chi tiết | Nguồn |
|---|---|---|
| **Mức cọc** | **0 – 750 USD**, thay đổi theo **độ tuổi người thuê** và **hạng xe**. Ví dụ **750 USD** nếu người thuê **dưới 30 tuổi** thuê xe **hạng Deluxe** | [Turo Help — Security deposits (US)](https://help.turo.com/en_us/security-deposits-us-HkbE44lE9); [Jerry](https://jerry.ai/car-insurance/how-much-is-the-deposit-for-turo/) **[nguồn yếu]** |
| **Cơ chế** | **Authorization hold** — tiền bị "khoá" trên thẻ nhưng **chưa trừ** | [Ride-Share.com](https://ride-share.com/does-turo-charge-a-deposit/) **[nguồn yếu]** |
| **Thời điểm giữ** | **24–48 giờ TRƯỚC khi chuyến bắt đầu** | như trên **[nguồn yếu]** |
| ⭐ **Thời điểm trả** | **Tự động hoàn 80 giờ sau khi chuyến kết thúc**, với 2 điều kiện: (1) không bên nào báo cáo hư hỏng, (2) không có hoá đơn bồi hoàn chưa thanh toán | [Turo Help — Security deposits](https://help.turo.com/en_us/security-deposits-us-HkbE44lE9) |
| ⭐ **Giảm cọc đổi lấy dữ liệu** | Turo **giảm 250 USD** nếu người thuê **cung cấp thông tin bảo hiểm ô tô cá nhân** khi đặt xe | như trên |

> **🔑 Bài học UX số 6 — BA CHI TIẾT ĐÁNG SAO CHÉP NGUYÊN VĂN:**
> 1. **Cọc THAY ĐỔI theo hồ sơ rủi ro, không phẳng.** Giao diện phải hiển thị **mức cọc của CHÍNH BẠN** sau khi đăng nhập, không phải một khoảng "500k–2tr" mơ hồ như [leminhstore.vn](https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html) đang làm.
> 2. **Biến việc giảm cọc thành PHẦN THƯỞNG cho việc nộp bằng chứng danh tính.** Đây là một cơ chế giao diện, không chỉ là chính sách: hiện một thanh *"Cọc của bạn: 500.000đ → Thêm ảnh thẻ SV để giảm còn 0đ"*.
> 3. **"80 giờ" là con số cụ thể, công khai.** Khách biết chính xác khi nào được hoàn tiền ⇒ giảm mạnh tin nhắn "bao giờ trả cọc?".

### 5.2. Turo — KYC (Trust & Safety)

| Lớp | Chi tiết | Nguồn |
|---|---|---|
| Nhà cung cấp | **ComplyCube** — xây vòng đời xác minh khách hàng end-to-end | [ComplyCube — Turo case](https://www.complycube.com/en/customer/turo-strengthens-car-sharing-compliance/) |
| Thành phần | **Xác minh giấy tờ** + **sinh trắc học liveness** (chống ảnh/video giả) + **kiểm tra bằng lái** | như trên |
| Chống gian lận sau đặt | Phát hiện **chiếm đoạt tài khoản, thiết bị bị đánh cắp, mẫu email đáng ngờ, tín hiệu gian lận di động** | như trên |
| ⭐ **Triết lý** | *"Authentication giúp Turo giảm gian lận bằng cách xác minh danh tính người dùng **MỖI LẦN** họ dùng sản phẩm"* — Mike Wilkins, Senior Director Trust & Safety | [Mitek — Q&A with Turo](https://www.miteksystems.com/blog/innovator-qa-mike-wilkins-senior-director-trust-safety-at-turo) |
| Trang công khai | Turo có **trang Trust & Safety riêng** ở cấp điều hướng chính | [turo.com/us/en/trust-and-safety](https://turo.com/us/en/trust-and-safety) |
| ⚠️ Giới hạn | Vẫn có kẻ xấu lọt lưới; sau vụ nổ Cybertruck 01/2025, Turo thuê **chuyên gia an ninh quốc gia và chống khủng bố** | [TechCrunch 03/01/2025](https://techcrunch.com/2025/01/03/turo-taps-national-security-and-counterterrorism-experts-after-cybertruck-explosion) |

> **🔑 Bài học UX số 7 — XÁC MINH LẠI MỖI GIAO DỊCH, KHÔNG CHỈ LÚC ĐĂNG KÝ.** Nhiều startup chỉ KYC một lần khi tạo tài khoản. Turo xác thực **mỗi chuyến**. 🟠 **`[TK]`** Với dự án: mỗi lần giao máy phải có **1 ảnh người nhận cầm thẻ SV bên cạnh máy, có dấu thời gian** — vừa là xác thực, vừa là bằng chứng bàn giao. Đây chính là cầu nối sang mục 5.4.

### 5.3. Getaround — bài học PHÁP LÝ về cách KHÔNG được trình bày bảo hiểm

| Nội dung | Chi tiết | Nguồn |
|---|---|---|
| Vụ việc | Tổng Chưởng lý Washington DC (Brian Schwalb) điều tra và đạt thoả thuận buộc Getaround hoàn tiền | [oag.dc.gov](https://oag.dc.gov/release/attorney-general-schwalb-secures-refunds-dc) |
| Cáo buộc | Getaround **đưa thông tin sai lệch**, gồm **sai lệch về mức độ an toàn/bảo mật của nền tảng**, dẫn tới xe khách bị hư hỏng và đánh cắp | như trên |
| ⭐ **Hành vi bị xử lý** | Giai đoạn **2022→2025**: gây hiểu lầm về phạm vi bảo hiểm và **KHÔNG CÔNG BỐ RÕ CÁC TRƯỜNG HỢP LOẠI TRỪ (exclusions)** | như trên |
| Chế tài | Hoàn tiền cho **hơn 50 người tiêu dùng ở DC** | như trên |
| Khiếu nại khác | Nhiều khiếu nại 2024–2025 về phí gian lận, yêu cầu bồi thường sai, phí tranh chấp | [BBB — Getaround complaints](https://www.bbb.org/us/ca/san-francisco/profile/auto-renting-and-leasing/getaround-1116-390772/complaints) **[nguồn yếu]** |

> 🔴 **🔑 Bài học UX số 8 — QUY TẮC BỐ CỤC BẮT BUỘC.**
> Getaround bị cơ quan nhà nước xử lý **không phải vì xe bị mất**, mà vì **nói không rõ về việc bảo hiểm KHÔNG bao gồm cái gì**.
>
> 🟠 **`[TK]`** ⇒ Trên giao diện dự án, khối **"NHỮNG TRƯỜNG HỢP KHÔNG ĐƯỢC MIỄN TRỪ"** phải:
> - Nằm **ĐẦU** trang Điều khoản, không phải cuối;
> - Xuất hiện **ngay trong luồng checkout** (bước xác nhận), không chỉ ở trang riêng;
> - Có **checkbox riêng** để khách tick, tách khỏi checkbox "đồng ý điều khoản chung";
> - Liệt kê cụ thể: *rơi vỡ màn hình, vào nước, mất máy, cho người khác mượn lại, mang ra khỏi khuôn viên trường khi chưa đăng ký*.
>
> **Một proposal môn Khởi nghiệp có phần "minh bạch điều khoản" viết tốt sẽ ghi điểm rất cao** — đây là thứ ~90% nhóm khác bỏ qua.

### 5.4. 🔴 Biên bản ảnh trước–sau (photo check-in / check-out) — **CHƯA XÁC MINH ĐƯỢC CHI TIẾT**

Đề bài nêu đây là phần "RẤT liên quan". **Tôi phải nói thẳng: chi tiết luồng chụp ảnh check-in/check-out của Turo và Getaround KHÔNG nằm trong kho dữ liệu đã thu thập, và tôi không còn lượt tìm kiếm để tra.**

**Cái ĐÃ có (có nguồn):**
- Turo xác thực danh tính **mỗi lần dùng sản phẩm**, không chỉ lúc đăng ký ([Mitek](https://www.miteksystems.com/blog/innovator-qa-mike-wilkins-senior-director-trust-safety-at-turo)) `[S]`
- Cọc chỉ được tự hoàn sau 80 giờ **nếu KHÔNG bên nào báo cáo hư hỏng** ([Turo Help](https://help.turo.com/en_us/security-deposits-us-HkbE44lE9)) `[S]` ⇒ **hàm ý logic** rằng phải tồn tại một cơ chế cho cả hai bên **báo cáo hư hỏng có bằng chứng** trong cửa sổ 80 giờ đó
- Grover có checklist kiểm tra khi thu hồi: **màn hình, Bluetooth, loa, camera, bàn phím** ([Signs of use](https://www.grover.com/at-en/g-about/asset-condition)) `[S]`
- Booqable (phần mềm cho thuê thương mại) có tính năng **gán barcode/định danh duy nhất cho từng thiết bị, quét khi giao/nhận, ghi log hư hỏng và ghi chú** ([Booqable Features](https://booqable.com/features/)) `[S]`

**Cái KHÔNG có:** số lượng ảnh Turo bắt buộc, các góc chụp cụ thể, có bắt chụp đồng hồ công-tơ-mét/mức xăng không, cửa sổ thời gian cho phép chụp, giao diện so sánh ảnh trước–sau. 🔴 Xem truy vấn ở [Mục 14](#14--những-phần-chưa-nghiên-cứu-được--truy-vấn-cần-chạy-lại).

> 🟠 **`[TK]` THIẾT KẾ ĐỀ XUẤT — Biên bản ảnh 2 chiều cho laptop** (tổng hợp từ checklist Grover + logic cửa sổ 80h của Turo + barcode của Booqable; **KHÔNG phải mô tả của bất kỳ nền tảng nào**):
>
> **Khi GIAO máy — 6 ảnh bắt buộc, chụp trong app/web, có dấu thời gian tự động:**
> | # | Ảnh | Mục đích |
> |---|---|---|
> | 1 | Toàn cảnh máy mở nắp, **màn hình đang bật** hiện màn hình test màu trắng | Chứng minh màn hình không nứt/không điểm chết |
> | 2 | Mặt A (nắp ngoài) | Ghi nhận xước sẵn có |
> | 3 | Mặt D (đáy máy) + **ảnh cận mã QR/nhãn tài sản** | Định danh đúng máy nào |
> | 4 | Bàn phím + touchpad | Phím thiếu/kẹt |
> | 5 | Cụm phụ kiện: sạc + tai nghe có dây + túi | Chống thất lạc phụ kiện (UConn tính riêng sạc 30 USD) |
> | 6 | ⭐ **Người nhận cầm thẻ SV bên cạnh máy** | Vừa KYC vừa bằng chứng bàn giao (bài học Turo số 7) |
>
> **Khi TRẢ máy — chụp lại đúng 6 khung hình đó**, giao diện hiện **2 ảnh cạnh nhau (trước | sau)** để cả hai bên cùng nhìn và bấm "Đồng ý — không phát sinh". Khoảnh khắc này là **màn hình quan trọng nhất của cả sản phẩm** về mặt giảm tranh chấp.
>
> **Cửa sổ khiếu nại:** 🟠 đề xuất **24 giờ** (thay vì 80 giờ như Turo, vì vòng quay của dự án ngắn hơn nhiều — theo ca thi). Quá 24h không ai khiếu nại ⇒ tự động hoàn cọc và đóng đơn.

---

## 6. NHÓM E — PHẦN MỀM QUẢN TRỊ TÀI SẢN / ĐẶT LỊCH THIẾT BỊ

### 6.1. 🔴 Snipe-IT demo và LibCal — KHÔNG NGHIÊN CỨU ĐƯỢC

Hết ngân sách tìm kiếm trước khi tra được hai hệ thống này. **Không có URL, không có mô tả màn hình.** Xem [Mục 14](#14--những-phần-chưa-nghiên-cứu-được--truy-vấn-cần-chạy-lại) để biết truy vấn cần chạy.

### 6.2. Booqable — nguồn thay thế tốt nhất hiện có cho "đặc tả chức năng"

Booqable là phần mềm quản lý cho thuê thương mại; dữ liệu tính năng của nó **thay thế được vai trò của Snipe-IT** trong việc trả lời câu hỏi *"hệ thống quản trị cho thuê tối thiểu cần những màn hình gì"* `[S]`.

| Tính năng | Chi tiết | Nguồn |
|---|---|---|
| **Đặt cọc** | Thu thanh toán và **damage deposit** online qua **50+ phương thức**; áp cọc theo **số tiền cố định HOẶC % giá trị thuê**; **authorize & hold trên thẻ từ back office**, rồi **release hoặc capture** tuỳ tình trạng hư hỏng | [Booqable Features](https://booqable.com/features/) |
| **Hợp đồng** | Tự sinh hợp đồng thuê từ chi tiết đơn (khách, ngày, thiết bị); thêm **điều khoản riêng, điều khoản trách nhiệm, chính sách hư hỏng** | [Booqable — IT Equipment Rental Software](https://booqable.com/industries/technology-rental-software/) |
| **Chữ ký điện tử** | Yêu cầu **e-signature** trên báo giá và hợp đồng | [Booqable Features](https://booqable.com/features/) |
| **Theo dõi thiết bị** | Gán **barcode/định danh duy nhất** cho từng sản phẩm để theo dõi **vị trí và tình trạng**; **quét barcode khi giao/nhận**; **ghi log hư hỏng và ghi chú** | như trên |
| **Giá** | **Từ 29 USD/tháng** (~730.000 VND/tháng); dùng thử 14 ngày; không phí setup; không ăn chia doanh thu | [Booqable Pricing](https://booqable.com/pricing/) |

> **🔑 Đặc tả chức năng tối thiểu (6 mục) rút từ Booqable** — nhóm nên dùng chính danh sách này làm **functional spec** cho website trong proposal:
> 1. Lịch/đặt trước theo thiết bị (**tránh double-booking**)
> 2. Định danh từng máy bằng mã duy nhất (**QR dán trên máy**)
> 3. Hợp đồng tự sinh + chữ ký điện tử
> 4. Ghi nhận tình trạng máy khi giao và khi nhận (**ảnh + checklist**)
> 5. Xử lý cọc (**hold / capture / release**)
> 6. Lịch sử hư hỏng theo từng máy

### 6.3. ⚠️ Cảnh báo hạ tầng thanh toán — ảnh hưởng TRỰC TIẾP tới thiết kế màn hình cọc

Cơ chế **pre-authorization hold** (Stripe: `PaymentIntent` với `capture_method: manual`, giữ mặc định **7 ngày**, mở rộng tới **~28–30 ngày** tuỳ mạng thẻ — [Stripe Docs](https://docs.stripe.com/payments/extended-authorization)) là **tính năng của MẠNG THẺ TÍN DỤNG** `[S]`.

Nhưng phần lớn sinh viên VN thanh toán bằng **chuyển khoản / MoMo / ZaloPay / VNPay / QR** — **những phương thức này không có cơ chế "giữ rồi nhả"**. 🔴 **Chưa xác minh được** liệu cổng thanh toán VN nào hỗ trợ pre-auth hold.

> 🟠 **`[TK]` HÀM Ý THIẾT KẾ:** **không được thiết kế màn hình "Đặt cọc" theo kiểu Turo/Stripe.** Thay vào đó, màn hình cọc của dự án phải là một trong ba dạng phi-thẻ:
> - **(a) Cọc bằng danh tính** — thẻ SV + email @fpt.edu.vn, không có tiền (khuyến nghị làm mặc định);
> - **(b) Cọc chuyển khoản thật + cam kết hoàn thủ công trong X giờ** (X phải là số cụ thể, bài học Turo);
> - **(c) Cọc bằng người bảo lãnh** — SV khác đã thuê ≥2 lần đứng tên.
>
> Việc **thừa nhận hạ tầng thanh toán VN khác phương Tây và thiết kế cơ chế tin cậy "low-tech" phù hợp bối cảnh** là một điểm sáng để viết vào proposal — thông minh hơn nhiều việc copy Stripe.

---

## 7. NHÓM F — 🔑 THAM CHIẾU UX GẦN NHẤT: HỆ THỐNG "ĐK MƯỢN MÁY" CỦA CHÍNH ĐH FPT

**Đây là nguồn tham chiếu giao diện quan trọng nhất của cả tài liệu**, vì đối tượng người dùng của dự án **đã đang dùng nó**.

**Nguồn:** [it-hcm.fpt.edu.vn — "Hướng dẫn mượn laptop của sinh viên trong trường"](https://it-hcm.fpt.edu.vn/articles.php?news=huong-dan-muon-laptop-cua-sinh-vien-trong-truong&id=56) (Phòng IT, ĐH FPT campus TP.HCM) `[S]`

| Yếu tố giao diện | Chi tiết `[S]` |
|---|---|
| **Bản chất** | SV mượn laptop **của SINH VIÊN KHÁC**, **"để dùng hoặc ĐI THI"** — P2P, không phải trường cho mượn máy của trường |
| **Đăng nhập** | Bằng **tài khoản nội bộ (tài khoản WiFi của trường)** |
| **Màn hình chính** | Gọi là **"Dashboard"** |
| **Nút hành động chính** | **"ĐK Mượn máy"** trên Dashboard |
| **Trường nhập liệu** | Nhập **MSSV của chủ máy cho mượn** |
| **Xác nhận 2 bước** | **Chủ máy phải đăng nhập hệ thống để xác nhận**; mỗi lần mượn/trả đều thao tác trên hệ thống |
| **Kết thúc** | Về Dashboard bấm **"Trả máy"** |
| **Ràng buộc** | Thời gian mượn **tối thiểu 60 phút** |
| **Lưu ý phòng thi** | Dù mượn máy người khác, SV phải **ngắt WiFi_Student và WiFi_Exam, rồi đăng nhập lại bằng tài khoản WiFi của CHÍNH MÌNH** |

> **🔑 Bài học UX số 9 — MƯỢN TỪ VỰNG GIAO DIỆN CỦA NHÀ TRƯỜNG.**
> 🟠 **`[TK]`** Website của dự án nên dùng đúng các nhãn mà SV FPT đã quen: **"Dashboard"**, **"ĐK thuê máy"** (song song với "ĐK Mượn máy"), **"Trả máy"**. Chi phí học của người dùng gần bằng 0. Đây là chi tiết nhỏ nhưng cho thấy nhóm **thực sự nghiên cứu người dùng** — rất ăn điểm.
>
> **Bài học số 10 — MÔ HÌNH XÁC NHẬN 2 BƯỚC ĐÃ ĐƯỢC NHÀ TRƯỜNG HỢP THỨC HOÁ.** SV FPT **đã quen** với việc "đăng ký xong phải chờ bên kia xác nhận". Nghĩa là màn hình **"Chờ xác nhận"** của dự án **không gây khó chịu** như với người dùng thương mại điện tử thông thường. Đây là lý do để **KHÔNG cần tự động hoá 100% ngay ở MVP**.
>
> ⚠️ **BẮT BUỘC KIỂM CHỨNG:** trang trên là của **campus TP.HCM**. Nhóm phải xác minh **campus Đà Nẵng có quy trình tương tự không**, và quan trọng hơn — **quy chế thi của ĐH FPT có CHO PHÉP dùng máy thuê từ bên ngoài trong phòng thi không**. Nếu cấm, toàn bộ mô hình phải điều chỉnh. Hỏi trực tiếp **Phòng Khảo thí / Phòng IT campus Đà Nẵng**.

---

## 8. 🟠 `[TK]` TỔNG HỢP — DANH SÁCH MÀN HÌNH CẦN CÓ (SITEMAP ĐỀ XUẤT)

> **Toàn bộ Mục 8–12 là THIẾT KẾ ĐỀ XUẤT của người nghiên cứu**, tổng hợp từ các bài học có nguồn ở Mục 2–7. Đây **không phải mô tả của website nào đang tồn tại**. Trong proposal nên trình bày là *"thiết kế của nhóm, dựa trên khảo sát X nền tảng tham chiếu"*.

### 8.1. Bảng 2 — 22 màn hình, chia 4 nhóm, có ưu tiên MVP

Cột **Ưu tiên**: **P0** = bắt buộc có ở MVP (bản demo nộp bài) · **P1** = giai đoạn 2 · **P2** = khi có quy mô.

#### Nhóm 1 — Trang công khai (không cần đăng nhập)

| # | Màn hình | Nội dung chính | Học từ | Ưu tiên |
|---|---|---|---|---|
| **S1** | **Trang chủ** | Một câu định vị duy nhất: *"Máy đã cài sẵn EOS + SEB, đã test, giao tận cổng trường"*. Ô **"Bạn thi ca nào?"** ngay đầu trang. Đếm ngược tới kỳ thi gần nhất. Số máy còn trống hôm nay | Grover có trang "How it works" đứng trước catalogue | **P0** |
| **S2** | **Cách hoạt động (4 bước)** | Trang giáo dục mô hình, 4 ô: Chọn ca → Xác minh SV → Nhận máy tại điểm hẹn → Trả máy | [Grover — How It Works](https://www.grover.com/us-en/how-it-works) | **P0** |
| **S3** | **Danh sách máy** | Lọc theo: **còn trống trong ca đã chọn** / cấu hình / giá. Mỗi thẻ máy hiện **badge "Đã test EOS + SEB ngày dd/mm"** | IA của [skylap.vn](https://skylap.vn/dich-vu-cho-thue/cho-thue-laptop/) (danh mục → model) | **P0** |
| **S4** | **Chi tiết máy (PDP)** | Cấu hình đầy đủ; **giá theo CA THI / ngày / tuần**; ảnh thật của **chính chiếc máy đó** (không phải ảnh catalog); tình trạng pin (% health); mã tài sản; **lịch trống dạng calendar** | Cấu trúc PDP của [ictsaigon](https://ictsaigon.com.vn/cho-thue-laptop-hp-elitebook-9480m) + neo giá của [Grover PDP](https://www.grover.com/de-en/products/apple-laptop-macbook-air-m2-8gb-256gb-ssd-10-core-gpu) | **P0** |
| **S5** | **Bảng giá** | Trang riêng, giá theo **ca thi** là đơn vị chính (ngành VN dùng ngày/tuần/tháng — dự án khác biệt ở đây) | [saolatech](https://saolatech.com.vn/bang-gia-thue-3425667), [thuelaptop.com.vn](https://thuelaptop.com.vn/bang-gia-cho-thue-laptop-van-phong.html) | **P0** |
| **S6** | ⭐ **Chính sách & Điều khoản** | **Bố cục 2 cột: "Hao mòn thường — MIỄN PHÍ" vs "Hư hỏng — CÓ PHÍ"**. Khối **"KHÔNG ĐƯỢC MIỄN TRỪ"** đặt **ĐẦU TRANG** | [Grover — Asset condition](https://www.grover.com/at-en/g-about/asset-condition) + bài học pháp lý [Getaround/OAG DC](https://oag.dc.gov/release/attorney-general-schwalb-secures-refunds-dc) | **P0** |
| **S7** | **Bảng giá đền bù** | Số tiền **CỤ THỂ theo từng model**, tách riêng phụ kiện (sạc, tai nghe) | UConn tách laptop 1.500 USD / sạc 30 USD; Grover 20% RRP | **P0** |
| **S8** | **Câu hỏi thường gặp (FAQ)** | "Máy có chạy được EOS không?", "Mac M1 của tôi thì sao?", "Tôi hỏng máy lúc 6h sáng ngày thi thì làm gì?" | FAQ/help center của Grover, Hygglo, Turo | **P1** |
| **S9** | **Trang Tin cậy & An toàn** | Gom mọi tín hiệu niềm tin về một chỗ (xem [Mục 11](#11--🟠-tk-tín-hiệu-tạo-niềm-tin-trust-signals)) | [turo.com/us/en/trust-and-safety](https://turo.com/us/en/trust-and-safety) | **P1** |
| **S10** | **Liên hệ / Zalo / Hotline** | ⚠️ **Vẫn phải có, và phải nổi bật.** Toàn ngành VN chạy bằng hotline — bỏ hẳn kênh thoại là rủi ro | 12/12 site khảo sát đều đặt hotline ở vị trí nổi bật | **P0** |

#### Nhóm 2 — Luồng đặt thuê (checkout)

| # | Màn hình | Nội dung chính | Học từ | Ưu tiên |
|---|---|---|---|---|
| **S11** | **B1 — Chọn CA THI** | Lịch theo ca, không theo ngày. Hiện **số máy còn trống mỗi ca**. Chọn điểm nhận | Không nền tảng VN nào có ⇒ điểm khác biệt | **P0** |
| **S12** | **B2 — Chọn máy** | Lọc sẵn theo ca đã chọn, chỉ hiện máy thật sự trống | Booqable: chống double-booking | **P0** |
| **S13** | **B3 — Xác minh sinh viên** | Email **@fpt.edu.vn** + MSSV. **Chỉ lần đầu**: thêm ảnh thẻ SV | Grover 3 lớp, risk-based; FPT "ĐK Mượn máy" | **P0** |
| **S14** | **B4 — Cọc & gói dịch vụ** | Hiện **mức cọc CỦA CHÍNH BẠN** (đã cá nhân hoá theo hồ sơ). Thanh *"Thêm bằng chứng → giảm cọc"*. Chọn gói Cơ bản / An tâm / Cấp tốc | [Turo Help — deposits](https://help.turo.com/en_us/security-deposits-us-HkbE44lE9): cọc theo hồ sơ rủi ro + giảm cọc đổi lấy dữ liệu | **P0** |
| **S15** | ⭐ **B5 — Xác nhận & Điều khoản** | Tóm tắt đơn. **Khối "KHÔNG ĐƯỢC MIỄN TRỪ" hiện ngay tại đây với checkbox RIÊNG**. Chữ ký điện tử | Getaround/OAG DC + e-signature của [Booqable](https://booqable.com/features/) | **P0** |
| **S16** | **B6 — Đơn thành công** | Mã đơn + **QR code** để quét khi nhận máy. **Cam kết thời gian bằng SỐ**: "Nhận máy tại … lúc …", "Hoàn cọc trong 24 giờ sau khi trả" | Turo công khai "80 giờ" | **P0** |

#### Nhóm 3 — Bàn giao (đây là phần khác biệt nhất so với mọi website VN)

| # | Màn hình | Nội dung chính | Học từ | Ưu tiên |
|---|---|---|---|---|
| **S17** | ⭐⭐ **Biên bản GIAO máy** | Quét QR máy → chụp **6 ảnh bắt buộc** (xem [Mục 5.4](#54--biên-bản-ảnh-trướcsau-photo-check-in--check-out--chưa-xác-minh-được-chi-tiết)) → checklist test **màn hình / bàn phím / pin / wifi / webcam / mic / cổng sạc / tai nghe** → 2 chữ ký | Checklist 5 điểm của [Grover](https://www.grover.com/at-en/g-about/asset-condition), mở rộng cho nhu cầu thi | **P0** |
| **S18** | ⭐⭐ **Biên bản TRẢ máy** | Chụp lại đúng 6 khung hình → **giao diện so sánh TRƯỚC \| SAU cạnh nhau** → kết luận "Không phát sinh" / "Có phát sinh" | Logic cửa sổ báo cáo hư hỏng của Turo | **P0** |
| **S19** | **Xử lý phát sinh** | Chọn hạng mục từ **bảng giá đền bù công khai** (S7), không nhập tay tuỳ tiện. Hiện rõ phần nào là hao mòn thường (0đ) | Grover tách bạch 2 loại | **P1** |

#### Nhóm 4 — Tài khoản & Quản trị

| # | Màn hình | Nội dung chính | Học từ | Ưu tiên |
|---|---|---|---|---|
| **S20** | **Dashboard sinh viên** | Đơn đang thuê, lịch sử, **hạng tín nhiệm** ("Đã thuê 3 lần — cọc 0đ"), nút **"Trả máy"** | Từ vựng của [hệ thống FPT](https://it-hcm.fpt.edu.vn/articles.php?news=huong-dan-muon-laptop-cua-sinh-vien-trong-truong&id=56) | **P0** |
| **S21** | **Admin — Lịch & tồn kho** | Timeline ngang: mỗi hàng 1 máy, mỗi cột 1 ca thi. Ô màu = đã đặt/đang thuê/bảo trì/trống | 🔴 Đáng lẽ học từ Snipe-IT/LibCal — chưa tra được. Tạm dựa trên Booqable | **P0** |
| **S22** | **Admin — Hồ sơ từng máy** | Mã tài sản, số lượt đã cho thuê, **lịch sử hư hỏng**, ngày test EOS/SEB gần nhất, % pin health | [Booqable](https://booqable.com/features/): barcode + log hư hỏng theo thiết bị | **P1** |

**Bổ sung P2 (khi có quy mô):** trang Gói mùa thi cho tập thể (lớp/CLB/Phòng Khảo thí — học từ [Grover for Business](https://www.grover.com/de-en/for-business)); trang blog SEO theo mẫu ngành VN.

### 8.2. MVP tối thiểu để nộp bài

Nếu chỉ demo được **6 màn hình**, chọn: **S1 → S11 → S13 → S15 → S17 → S18**. Sáu màn hình này kể trọn câu chuyện *"đặt được – xác minh được – bàn giao có bằng chứng"*, tức là **đúng ba thứ mà 12 website VN khảo sát được đều không có**.

---

## 9. 🟠 `[TK]` LUỒNG ĐẶT THUÊ — THỨ TỰ BƯỚC & HỎI GÌ Ở BƯỚC NÀO

### 9.1. Bảng 3 — Ma trận "hỏi gì ở bước nào" (nguyên tắc: hỏi càng muộn càng tốt)

| Bước | Màn hình | **Hỏi những gì** | **CỐ TÌNH chưa hỏi** | Vì sao |
|---|---|---|---|---|
| **0** | S1 Trang chủ | *Không hỏi gì* — chỉ 1 câu: "Bạn thi ca nào?" | Mọi thứ | Mọi câu hỏi ở đây đều làm rơi khách |
| **1** | S11 Chọn ca | **Ngày thi + ca thi + điểm nhận máy** | Danh tính, thanh toán | Ca thi là thứ khách đã biết chắc, trả lời được ngay lập tức |
| **2** | S12 Chọn máy | **Chọn 1 máy** (đã lọc sẵn máy trống) | — | Chỉ hiện máy thật sự đặt được ⇒ không bao giờ báo lỗi "hết máy" ở bước sau |
| **3** | S13 Xác minh | **Email @fpt.edu.vn, MSSV, họ tên, SĐT/Zalo**. *Lần đầu tiên:* thêm **ảnh thẻ SV** | Ảnh CCCD, địa chỉ nhà, thông tin gia đình | Grover chỉ đòi giấy tờ **khi có nghi ngờ**, không đòi mặc định. Đây là nơi bỏ được nhiều ma sát nhất so với [leminhstore.vn](https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html) (đòi CCCD gốc + thẻ SV + **thông tin liên hệ gia đình** + địa chỉ tạm trú) |
| **4** | S14 Cọc & gói | **Chọn gói** (Cơ bản/An tâm/Cấp tốc). Hiện **mức cọc cá nhân hoá**. Tuỳ chọn: thêm người bảo lãnh để giảm cọc | — | Turo: cọc theo hồ sơ rủi ro, giảm cọc đổi lấy bằng chứng |
| **5** | S15 Xác nhận | **Tick riêng khối "KHÔNG ĐƯỢC MIỄN TRỪ"** + tick điều khoản chung + **ký điện tử** | — | Bài học pháp lý Getaround: hai checkbox tách rời, không gộp làm một |
| **6** | S16 Thành công | *Không hỏi* — **trả về QR code + cam kết thời gian bằng SỐ** | — | Turo công khai "80 giờ" ⇒ giảm mạnh tin nhắn hỏi han |
| **7** | S17 Giao máy (tại điểm hẹn) | **6 ảnh + checklist phần cứng + 2 chữ ký** | — | Đây là lúc duy nhất hỏi nhiều được, vì đang gặp mặt trực tiếp |
| **8** | S18 Trả máy | **6 ảnh lặp lại + đối chiếu trước/sau** | — | — |

### 9.2. Ba quy tắc luồng rút từ nghiên cứu

1. **Không bắt tạo tài khoản trước khi chọn ca.** Việc chọn ca thi phải làm được ngay ở lần chạm đầu tiên. (Suy từ nguyên tắc chung; 🔴 chưa có số liệu Baymard/NN/g để hậu thuẫn — xem Mục 14.)
2. **Xác minh theo mức rủi ro (risk-based), không xác minh phẳng.** Grover chỉ đòi selfie + giấy tờ **khi hệ thống nghi ngờ** `[S]`. ⇒ SV thuê lần thứ 2 trở đi đi thẳng từ chọn ca sang xác nhận.
3. **Mỗi lời hứa phải là một con số.** "Hoàn cọc **trong 24 giờ**", "Giao máy **trước giờ thi 30 phút**", "Máy được test EOS+SEB **ngày 12/09/2026**". Đây là bài học Turo ("80 giờ") và cũng là thứ ngành VN làm rất kém (họ ghi "hỗ trợ 24/7", "giao nhanh" — mơ hồ).

---

## 10. 🟠 `[TK]` MÔ TẢ 3 MÀN HÌNH QUAN TRỌNG NHẤT (để nhóm vẽ wireframe)

### 10.1. S11 — Chọn ca thi (màn hình khác biệt nhất so với đối thủ)

```
┌──────────────────────────────────────────────────────────┐
│  Bạn cần máy cho ca thi nào?                             │
│                                                          │
│  [ Thứ 2 16/09 ] [ Thứ 3 17/09 ] [ Thứ 4 18/09 ]  ...   │
│                                                          │
│   Ca 1  07:30–09:00     ●●●●○○   4 máy trống            │
│   Ca 2  09:30–11:00     ●●○○○○   2 máy trống            │
│   Ca 3  13:00–14:30     ○○○○○○   HẾT MÁY  [Báo tôi khi có]│
│   Ca 4  15:00–16:30     ●●●●●●   6 máy trống            │
│                                                          │
│  Nhận máy tại:  ( ) Cổng chính  ( ) Sảnh Alpha           │
│                                                          │
│  ⓘ Máy được giao TRƯỚC GIỜ THI 30 PHÚT                   │
│                                    [ Tiếp tục → ]        │
└──────────────────────────────────────────────────────────┘
```
**Vì sao thiết kế thế này:** đơn vị "ca thi" thay cho "ngày" là toàn bộ định vị sản phẩm. Ngành VN bán theo ngày/tuần/tháng ([skylap.vn](https://skylap.vn/dich-vu-cho-thue/cho-thue-laptop/), [chothuelaptop.com.vn](https://chothuelaptop.com.vn/thue-laptop-theo-thang/)); các chương trình mượn máy của ĐH Mỹ dùng đơn vị **giờ** cho hợp đồng ngắn (KU tính 0,10 USD/phút; UConn 1 USD/giờ) `[S]`. Ca thi là đơn vị tự nhiên của khách hàng.

### 10.2. S15 — Xác nhận & Điều khoản (màn hình chống rủi ro pháp lý)

```
┌──────────────────────────────────────────────────────────┐
│  Xác nhận đơn thuê #DN-2609-014                          │
│  Máy: Dell Latitude 5400 (mã TS-07)                      │
│  Ca 2, Thứ 3 17/09, 09:30–11:00 · Nhận: Sảnh Alpha 09:00 │
│  Giá: 60.000đ   Cọc: 0đ (SV đã xác minh)                 │
│──────────────────────────────────────────────────────────│
│  ⚠️  NHỮNG TRƯỜNG HỢP BẠN PHẢI ĐỀN — KHÔNG ĐƯỢC MIỄN TRỪ  │
│                                                          │
│   ✗ Rơi vỡ / nứt màn hình                                │
│   ✗ Vào nước                                             │
│   ✗ Mất máy hoặc mất sạc / tai nghe                      │
│   ✗ Cho người khác mượn lại                              │
│   ✗ Mang máy ra khỏi khuôn viên trường khi chưa đăng ký  │
│                        → Xem bảng giá đền bù chi tiết    │
│                                                          │
│   [ ] Tôi đã đọc và hiểu 5 trường hợp trên               │
│──────────────────────────────────────────────────────────│
│   [ ] Tôi đồng ý Điều khoản dịch vụ                      │
│                                                          │
│   Ký tên: [ ____vùng ký____ ]      [ Xác nhận thuê ]     │
└──────────────────────────────────────────────────────────┘
```
**Vì sao thiết kế thế này:** trực tiếp từ vụ [Getaround bị Tổng Chưởng lý DC xử lý vì không công bố rõ các trường hợp loại trừ](https://oag.dc.gov/release/attorney-general-schwalb-secures-refunds-dc) `[S]`. **Hai checkbox tách rời** là chi tiết cốt lõi — gộp chung thì không chứng minh được khách đã đọc phần loại trừ.

### 10.3. S18 — Biên bản trả máy (màn hình giảm tranh chấp)

```
┌──────────────────────────────────────────────────────────┐
│  Trả máy TS-07 · Đơn #DN-2609-014                        │
│                                                          │
│      LÚC GIAO 09:02          LÚC TRẢ 11:14               │
│   ┌────────────┐          ┌────────────┐                 │
│   │ [ảnh mặt A]│          │ [ảnh mặt A]│   ✓ Khớp        │
│   └────────────┘          └────────────┘                 │
│   ┌────────────┐          ┌────────────┐                 │
│   │ [màn hình] │          │ [màn hình] │   ✓ Khớp        │
│   └────────────┘          └────────────┘                 │
│   ┌────────────┐          ┌────────────┐                 │
│   │ [phụ kiện] │          │ [phụ kiện] │   ⚠ Thiếu tai nghe│
│   └────────────┘          └────────────┘                 │
│                                                          │
│  Hao mòn thường (xước nhẹ, vết dùng): MIỄN PHÍ ✓         │
│  Phát sinh: Mất tai nghe có dây ......... 80.000đ        │
│                                                          │
│  Hoàn cọc: 0đ (không thu cọc) · Cần thanh toán: 80.000đ  │
│                                                          │
│  SV ký [____]        Nhân viên ký [____]   [ Hoàn tất ]  │
└──────────────────────────────────────────────────────────┘
```
**Vì sao thiết kế thế này:** hợp nhất 3 bài học có nguồn — checklist kiểm tra của [Grover](https://www.grover.com/at-en/g-about/asset-condition), việc [Grover tách "hao mòn thường = miễn phí"](https://www.grover.com/at-en/g-about/asset-condition), và việc UConn **tách giá phụ kiện riêng** (laptop 1.500 USD / sạc 30 USD) `[S]`. Đặt hai ảnh cạnh nhau khiến tranh cãi trở nên **không cần lời**.

---

## 11. 🟠 `[TK]` TÍN HIỆU TẠO NIỀM TIN (TRUST SIGNALS)

> 🔴 **Lưu ý:** phần này **KHÔNG dựa trên Baymard/NN/g** (không tra được). Nó rút từ **hành vi quan sát được của các nền tảng đã khảo sát** và **các vụ việc pháp lý thật**.

### Bảng 4 — 14 tín hiệu niềm tin, xếp theo sức mạnh, gắn với màn hình

| Hạng | Tín hiệu | Đặt ở màn hình | Bằng chứng/nguồn cảm hứng |
|---|---|---|---|
| **1** | ⭐ **Badge "Đã test EOS + SEB ngày dd/mm/yyyy"** trên từng máy | S3, S4, S17 | Khác biệt lõi duy nhất; Drexel Law bắt buộc SV chạy thử bài thi trước khi được dùng máy mượn `[S]` |
| **2** | ⭐ **Ảnh THẬT của chính chiếc máy đó**, không phải ảnh catalog | S4 | Ngành VN dùng ảnh catalog ⇒ dễ vượt |
| **3** | ⭐ **Bảng 2 cột "Hao mòn thường (miễn phí)" vs "Hư hỏng (có phí)"** | S6 | [Grover — Asset condition](https://www.grover.com/at-en/g-about/asset-condition) |
| **4** | ⭐ **Khối "KHÔNG ĐƯỢC MIỄN TRỪ" đặt đầu trang + checkbox riêng** | S6, S15 | [OAG DC vs Getaround](https://oag.dc.gov/release/attorney-general-schwalb-secures-refunds-dc) |
| **5** | ⭐ **Cam kết thời gian bằng CON SỐ** ("hoàn cọc trong 24 giờ") | S16, S6 | [Turo: "80 giờ"](https://help.turo.com/en_us/security-deposits-us-HkbE44lE9) |
| **6** | **Bảng giá đền bù công khai theo từng model, tách phụ kiện** | S7 | UConn (laptop 1.500 USD / sạc 30 USD); Grover (20% RRP) `[S]` |
| **7** | **Số máy còn trống hiển thị theo thời gian thực** | S1, S11 | Không nền tảng VN nào có; chống rủi ro "hết máy ngày cao điểm" |
| **8** | **Biên bản ảnh 2 chiều có dấu thời gian** | S17, S18 | Grover checklist + logic báo cáo hư hỏng của Turo |
| **9** | **Hạng tín nhiệm hiển thị cho SV** ("Đã thuê 3 lần — cọc 0đ") | S20, S14 | [Turo: cọc theo hồ sơ rủi ro](https://help.turo.com/en_us/security-deposits-us-HkbE44lE9) |
| **10** | **Đăng nhập bằng @fpt.edu.vn** (thay vì đòi CCCD) | S13 | Grover thay cọc bằng danh tính; Hygglo dựa vào BankID |
| **11** | **Phương án dự phòng công bố sẵn** ("máy lỗi trong ca thi → có máy thứ 2 trong 15 phút, hoặc hoàn 100%") | S1, S8 | [mitgroup.vn](https://mitgroup.vn/cho-thue-laptop/): "đổi máy không mất thêm chi phí" |
| **12** | **Hotline + Zalo hiển thị mọi trang** | Toàn site | 12/12 site VN khảo sát; SV VN quen kênh Zalo |
| **13** | **Minh bạch "phí của bạn dùng để làm gì"** | S6 | [Hygglo Help](https://help.hygglo.info/en/articles/10415333-how-hygglo-works) liệt kê rõ 5 khoản |
| **14** | **Giờ hoạt động cụ thể theo thứ trong tuần** | S10 | [leminhstore.vn](https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html) |

### Ba PHẢN tín hiệu — tuyệt đối tránh

| ✗ Không làm | Vì sao | Bằng chứng |
|---|---|---|
| Viết "bảo hiểm toàn phần" / "cam kết 100%" mà không kèm danh sách loại trừ ngay cạnh | Fat Llama viết "fully insured" rồi từ chối bồi thường ⇒ review 1 sao hàng loạt | [Trustpilot](https://www.trustpilot.com/review/fatllama.com), [PetaPixel](https://petapixel.com/2019/03/20/how-i-had-over-5000-in-camera-gear-stolen-through-fat-llama/) |
| Giá "từ 10k/ngày" kiểu mồi nhử | [thuelaptop.vn nhúng "chi-tu-10k" vào URL](https://www.thuelaptop.vn/thue-laptop-da-nang-gia-re-chi-tu-10k/) trong khi mặt bằng ĐN là 80.000đ/máy/ngày ⇒ mất niềm tin khi khách gọi hỏi | So sánh Bảng giá trong `01-thi-truong-cho-thue-laptop-vn.md` |
| Điều khoản bất lợi giấu ở cuối trang | SAOLA: "trả sớm vẫn phải trả đủ giá trị hợp đồng" | [saolatech.com.vn](https://saolatech.com.vn/bang-gia-thue-3425667) |

---

## 12. 🟠 `[TK]` MÀN HÌNH QUẢN TRỊ (ADMIN)

> 🔴 Đáng lẽ mục này dựa trên **Snipe-IT demo** và **LibCal equipment booking** — cả hai chưa tra được. Dưới đây dựa trên **đặc tả chức năng của Booqable** ([Features](https://booqable.com/features/)) và thực tiễn quản lý cho mượn của thư viện ĐH `[S]`.

| Màn hình admin | Thành phần | Nguồn cảm hứng |
|---|---|---|
| **A1 — Lịch & tồn kho** | Timeline ngang: hàng = từng máy (mã tài sản), cột = từng ca thi. Ô màu: trống / đã đặt / đang thuê / bảo trì / đang test EOS | Booqable chống double-booking; Stanford dùng hệ thống reservation `[S]` |
| **A2 — Hàng chờ bàn giao hôm nay** | Danh sách đơn của ca sắp tới, sắp xếp theo giờ giao. Nút quét QR mở thẳng S17 | Nhu cầu vận hành: giờ cao điểm trước ca thi rất ngắn |
| **A3 — Hồ sơ từng máy** | Mã tài sản, số lượt cho thuê tích luỹ, lịch sử hư hỏng, ngày test EOS/SEB gần nhất, % pin health, ảnh gần nhất | [Booqable](https://booqable.com/features/): barcode + log hư hỏng theo thiết bị |
| **A4 — Hồ sơ khách** | MSSV, số lần thuê, số lần trễ, hạng tín nhiệm, mức cọc áp dụng | Turo: hồ sơ rủi ro; thư viện ĐH: nợ phí → chặn mượn tiếp `[S]` |
| **A5 — Checklist chuẩn bị máy** | Bắt buộc trước mỗi lần giao: **wipe sạch + pin 100% + test wifi/webcam/bàn phím + xác nhận EOS/SEB chạy được** | Grover: assessment → data wipe → làm sạch → sửa → về kho `[S]`; LaptopsAnytime tự động reset + sạc giữa 2 phiên `[S]` |
| **A6 — Sổ phạt & phát sinh** | Ghi nhận trễ hạn (tính theo GIỜ, có TRẦN), phát sinh hư hỏng, mốc chuyển "trễ → mất" | KU: 0,10 USD/phút, trần 30 USD; NIU: quá hạn 7 ngày = mất `[S]` |

---

## 13. BẢNG QUY CHIẾU NHANH — "HỌC GÌ TỪ AI"

| Nền tảng | Thứ đáng sao chép nhất vào giao diện | Thứ tuyệt đối không sao chép |
|---|---|---|
| **Website cho thuê laptop VN** (12 site) | Kiến trúc landing page theo địa phương/đối tượng/chính sách; nội dung trang sản phẩm (cấu hình + 3 mức giá + cọc + giấy tờ + SLA) | Việc **không có luồng đặt hàng online**; giá mồi nhử "từ 10k"; điều khoản bất lợi giấu cuối trang |
| **Grover** | Xác minh theo mức rủi ro (không đòi giấy tờ mặc định); bảng "hao mòn thường vs hư hỏng"; checklist 5 điểm khi thu hồi; phí phạt cho máy chưa đăng xuất tài khoản | Mô hình credit-check (VN không có Schufa); mở rộng đội thiết bị bằng vốn vay (dẫn tới tái cấu trúc StaRUG 4/2025) |
| **Hygglo** | Minh bạch "phí của bạn dùng để làm gì"; bảo hiểm nhúng theo giao dịch | Phụ thuộc định danh quốc gia (VN chưa có tương đương dễ tích hợp cho startup SV) |
| **Fat Llama** | (Chủ yếu là bài học ngược) | Mô hình P2P; khẩu hiệu "fully insured" không kèm loại trừ |
| **Turo** | Cọc theo hồ sơ rủi ro; giảm cọc đổi lấy bằng chứng; **cam kết thời gian bằng số**; xác thực mỗi giao dịch; trang Trust & Safety riêng | Cơ chế card authorization hold (hạ tầng thanh toán VN chưa xác minh được là hỗ trợ) |
| **Getaround** | (Hoàn toàn là bài học ngược) | Trình bày bảo hiểm mập mờ, giấu điều khoản loại trừ |
| **Booqable** | Đặc tả chức năng 6 mục; barcode theo thiết bị; e-signature; hold/capture/release | — |
| **Hệ thống "ĐK Mượn máy" ĐH FPT** | Từ vựng giao diện ("Dashboard", "ĐK Mượn máy", "Trả máy"); mô hình xác nhận 2 bước mà SV đã quen | — |

---

## 14. 🔴 NHỮNG PHẦN CHƯA NGHIÊN CỨU ĐƯỢC + TRUY VẤN CẦN CHẠY LẠI

### 14.1. Nguyên nhân

**Ngân sách WebSearch của phiên đã cạn (200/200) TRƯỚC KHI nhiệm vụ này bắt đầu** ⇒ nhiệm vụ này chạy **0 truy vấn mới**. WebFetch bị chặn hoàn toàn.

### 14.2. Bảng 5 — Khoảng trống và truy vấn cụ thể để nhóm tự chạy

| # | Khoảng trống | Truy vấn đề xuất |
|---|---|---|
| 1 | 🔴 **Snipe-IT** — giao diện quản trị tài sản, các màn hình chính | `Snipe-IT demo asset management screenshots dashboard` · `Snipe-IT check-in check-out asset workflow interface` · `Snipe-IT vs alternatives IT asset management UI review 2025` |
| 2 | 🔴 **LibCal equipment booking** (Springshare) | `LibCal equipment booking module interface library` · `Springshare LibCal equipment reservation student workflow` · `library equipment booking system UX laptop reservation` |
| 3 | 🔴 **Baymard Institute** — số liệu checkout UX | `Baymard Institute checkout usability research findings` · `Baymard cart abandonment rate statistics 2025` · `Baymard form field usability guidelines checkout` |
| 4 | 🔴 **Nielsen Norman Group** — booking flow & trust | `Nielsen Norman Group booking flow usability guidelines` · `NNgroup trust signals e-commerce high value transaction` · `nngroup progressive disclosure form design` |
| 5 | 🔴 **Turo/Getaround photo check-in** — chi tiết luồng chụp ảnh | `Turo photo check-in requirements how many photos guest host` · `Turo check-out process damage documentation timestamp` · `Getaround photo inspection before after rental` |
| 6 | 🔴 **Grover checkout** — số bước cụ thể trên trang | `Grover checkout process step by step review` · `Grover rental sign up experience walkthrough 2025` |
| 7 | 🔴 **Fat Llama luồng đặt** — các bước từ tìm đồ tới nhận đồ | `Fat Llama booking process steps renter guide` · `Fat Llama verification ID requirements borrower` |
| 8 | 🔴 **Cổng thanh toán VN có hỗ trợ pre-auth hold không** (ảnh hưởng trực tiếp màn hình S14) | `VNPay pre-authorization hold tạm giữ tiền` · `MoMo ZaloPay đặt cọc giữ tiền hoàn trả API` · `PayOS pre-authorization capture Việt Nam` |
| 9 | 🔴 **Có site cho thuê laptop VN nào thật sự có form đặt hàng online không** | `"thuê laptop" "đặt hàng online" form đặt thuê website` · `website cho thuê thiết bị Việt Nam có giỏ hàng đặt lịch` |

### 14.3. Việc kiểm chứng thủ công BẮT BUỘC (không cần công cụ, chỉ cần mở trình duyệt)

Đây là phần **rẻ nhất và có giá trị cao nhất** nhóm có thể tự làm — và nó tạo ra **dữ liệu sơ cấp**, thường được chấm điểm cao hơn dữ liệu thứ cấp trong bài tập Khởi nghiệp:

1. **Mở 6 website ở Bảng 1, chụp màn hình toàn trang** (trang chủ + trang dịch vụ + bảng giá). Lập một **bảng so sánh UX** với các cột: *có form đặt hàng không / có hiện tồn kho không / có chọn ngày không / có tài khoản không / bao nhiêu bước tới lúc chốt / kênh liên hệ chính*. **Đây chính là phụ lục mạnh nhất cho phần "Phân tích đối thủ" của proposal.**
2. **Đăng nhập hệ thống IT của ĐH FPT campus Đà Nẵng**, tìm module tương đương "ĐK Mượn máy" ([hướng dẫn của campus TP.HCM](https://it-hcm.fpt.edu.vn/articles.php?news=huong-dan-muon-laptop-cua-sinh-vien-trong-truong&id=56)), **chụp lại Dashboard**. Đây là tham chiếu UX gần nhất và là bằng chứng nội bộ mạnh nhất của proposal.
3. **Gọi hotline 3–5 đơn vị tại Đà Nẵng** (số điện thoại có trong Bảng 1) và **ghi lại kịch bản hội thoại**: họ hỏi những thông tin gì, theo thứ tự nào, mất bao lâu. → **Đây chính là "luồng đặt hàng" thật của thị trường**, và nó là đầu vào trực tiếp để thiết kế form của nhóm.
4. **Hỏi Phòng Khảo thí / Phòng IT campus Đà Nẵng**: quy chế thi có cho phép dùng **máy thuê từ bên ngoài** trong phòng thi không. 🔴 **Đây là rủi ro số 1 của toàn bộ mô hình** — phải làm trước mọi việc khác.

---

## 15. DANH SÁCH NGUỒN (URL THẬT, gom theo nhóm)

> Tất cả URL dưới đây do WebSearch trả về trong các nhiệm vụ trước của phiên. **Không URL nào được mở đọc trực tiếp** (WebFetch bị chặn).

### A. Website cho thuê laptop Việt Nam
- [thuelaptop.com.vn](https://thuelaptop.com.vn/) · [bảng giá văn phòng](https://thuelaptop.com.vn/bang-gia-cho-thue-laptop-van-phong.html) · [bảng giá đồ hoạ](https://thuelaptop.com.vn/bang-gia-cho-thue-laptop-do-hoa.html) · [landing Đà Nẵng](https://thuelaptop.com.vn/dia-diem-cho-thue-laptop-tai-da-nang-gia-re.html) · [SV thuê không cần cọc](https://thuelaptop.com.vn/cho-sinh-vien-thue-may-tinh-khong-can-dat-coc.html) · [gaming](https://thuelaptop.com.vn/dich-vu-cho-thue-laptop-gaming.html)
- [ictsaigon.com.vn/cho-thue-laptop](https://ictsaigon.com.vn/cho-thue-laptop) · [HP Elitebook 9480m](https://ictsaigon.com.vn/cho-thue-laptop-hp-elitebook-9480m) · [không cọc](https://ictsaigon.com.vn/thue-laptop-khong-coc) · [gaming](https://ictsaigon.com.vn/thue-laptop-gaming) · [PC để bàn](https://ictsaigon.com.vn/cho-thue-pc-may-tinh-de-ban) · [kinh nghiệm thuê laptop](https://ictsaigon.com.vn/kinh-nghiem-thue-laptop-uy-tin-dam-bao)
- [mitgroup.vn/cho-thue-laptop](https://mitgroup.vn/cho-thue-laptop/) · [không cọc](https://mitgroup.vn/thue-laptop-khong-coc/) · [sinh viên](https://mitgroup.vn/thue-laptop-sinh-vien/)
- [skylap.vn — cho thuê laptop](https://skylap.vn/dich-vu-cho-thue/cho-thue-laptop/) · [Dell văn phòng](https://skylap.vn/dich-vu-cho-thue/cho-thue-laptop-dell-van-phong/) · [Dell Precision i7-7700HQ](https://skylap.vn/thue-laptop-dell-precision-core-i7-7700hq/)
- [laptopsgn.com/cho-thue-laptop](https://laptopsgn.com/cho-thue-laptop/) · [giao 2h](https://laptopsgn.com/tin-tuc/dich-vu-cho-thue-laptop-tphcm-gia-re-giao-2h/) · [thuê laptop sinh viên](https://laptopsgn.com/tin-tuc/thue-laptop-sinh-vien/)
- [saolatech.com.vn](https://saolatech.com.vn/) · [bảng giá thuê](https://saolatech.com.vn/bang-gia-thue-3425667) · [không cọc Hà Nội](https://saolatech.com.vn/thue-laptop-khong-can-dat-coc-tai-ha-noi-giai-phap-tiet-kiem-cho-sinh-vien-3425752) · [thuê cho sinh viên](https://saolatech.com.vn/thue-laptop-cho-sinh-vien-giai-phap-tien-loi-tiet-kiem-va-hien-dai-3425768)
- [leminhstore.vn — thuê laptop SV Đà Nẵng](https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html) · [thuê PC gaming ĐN](https://leminhstore.vn/thue-pc-gaming-da-nang-104910u.html)
- [truonggiang.vn/cho-thue-laptop.html](https://truonggiang.vn/cho-thue-laptop.html) · [laptop cũ Dell 3500](https://truonggiang.vn/laptop-cu-dell-3500-i5-8250)
- [maytinhdinhhau.vn — dịch vụ cho thuê ĐN](https://maytinhdinhhau.vn/dich-vu-cho-thue-laptop-tai-da-nang/) · [địa chỉ cho SV thuê](https://maytinhdinhhau.vn/dia-chi-cho-sinh-vien-thue-laptop-gia-re-tai-da-nang/)
- [chothuelaptop.com.vn — Đà Nẵng](https://chothuelaptop.com.vn/thue-laptop-da-nang/) · [theo tháng](https://chothuelaptop.com.vn/thue-laptop-theo-thang/)
- [thuelaptop.vn — ĐN từ 10k](https://www.thuelaptop.vn/thue-laptop-da-nang-gia-re-chi-tu-10k/) · [chính sách kinh doanh cho thuê thiết bị](https://www.thuelaptop.vn/gioi-thieu/chinh-sach-kinh-doanh-cho-thue-thiet-bi/)
- [phuongnamco.com](https://phuongnamco.com/) · ⭐ [cho thuê laptop THI CỬ](https://phuongnamco.com/cho-thue-laptop-thi-cu-giai-phap-huu-ich-cho-sinh-vien-mua-thi/)
- [seaevent.vn — cho thuê laptop sự kiện ĐN](https://seaevent.vn/cho-thue-laptop-su-kien-tai-da-nang/) · [case study ĐH Bách Khoa ĐN](https://seaevent.vn/cho-thue-laptop-phuc-vu-dao-tao-tai-truong-dai-hoc-bach-khoa-da-nang/)
- [skycomputer.vn](https://skycomputer.vn/dich-vu/cho-thue-may-tinh-laptop-tai-da-nang/) · [xooevent.com](https://xooevent.com/cho-thue-laptop-may-tinh-so-luong-lon-tai-da-nang/) · [laptopchothue.com](https://laptopchothue.com/) · [laptopchothue — ĐN](https://laptopchothue.com/dich-vu-cho-thue-laptop-tai-da-nang-laptop-cau-hinh-cao-gia-tot/) · [tinhocpnn.com](https://tinhocpnn.com/bang-gia-cho-thue-laptop-may-tinh-gia-re/) · [vietbis.vn — không cọc HN](https://vietbis.vn/tin-tuc/thue-laptop-khong-can-dat-coc-tai-ha-noi-dieu-kien-ap-dung-3116.html) · [bk4.com.vn](https://bk4.com.vn/dich-vu-cho-thue-laptop-theo-ngay-tai-ha-noi/) · [laptopthienan.com](https://laptopthienan.com/cho-thue-laptop-may-tinh-hcm-gia-re-50k.html) · [chothuelaptop.info](https://chothuelaptop.info/cho-thue-laptop-da-nang-thu-tuc-nhanh-gon/) · [chothuemaytinh.vn](https://chothuemaytinh.vn/cho-thue-laptop-sinh-vien/) · [quangtin.com](https://quangtin.com/pages/cho-thue-may-tinh-laptop-gia-re-tai-tp-hcm-dich-vu-chuyen-nghiep) · [thietbichothue.com](https://thietbichothue.com/cho-thue-laptop/) · [top10danang.com — top công ty cho thuê laptop ĐN](https://top10danang.com/top-10-cong-ty-cho-thue-laptop-da-nang-uy-tin-gia-re/) · [danang.plus](https://danang.plus/thue-laptop/)

### B. Grover
- [Grover — How It Works](https://www.grover.com/us-en/how-it-works) · [Grover Care](https://www.grover.com/us-en/g-about/grover-care) · [Signs of use / Asset condition](https://www.grover.com/at-en/g-about/asset-condition) · [Sustainable tech](https://www.grover.com/de-en/g-explore/sustainable-tech) · [For Business](https://www.grover.com/de-en/for-business) · [PDP MacBook Air M2](https://www.grover.com/de-en/products/apple-laptop-macbook-air-m2-8gb-256gb-ssd-10-core-gpu) · [PDP MacBook Pro 13 M2](https://www.grover.com/de-en/products/apple-macbook-pro-13-3-m2-8cpu-16gb-512gb-10gpu-67w)
- Help center: [Credit check](https://service.grover.com/hc/en-us/articles/19920531898642-How-does-Grover-s-credit-check-work) · [Identity Verification](https://service.grover.com/hc/en-us/articles/35704298814866-Identity-Verification) · [Additional Verification](https://service.grover.com/hc/en-us/articles/19920613200914-Additional-Verification) · [What is Grover Care](https://service.grover.com/hc/en-us/articles/19920685566610-What-is-Grover-Care-and-how-does-it-work) · [Repair and replacement costs](https://service.grover.com/hc/en-us/articles/19918338642578-Repair-and-replacement-costs) · [Drones and e-mobility](https://service.grover.com/hc/en-us/articles/19908669018002-Drones-and-e-mobility-products)
- [Onfido — Grover case study](https://onfido.com/customer/grover/) · [SEON — Grover partnership](https://seon.io/resources/news/grover-partners-with-seon-to-verify-user-ids-as-it-expands-worldwide/) · [Gründer Vision — Grover Schufa](https://gruender-vision.de/grover-schufa-alles-was-du-wissen-solltest/) **[nguồn yếu]** · [Waste360 — How Grover's model works](https://www.waste360.com/e-waste/how-grover-s-electronics-rental-model-works)

### C. Fat Llama & Hygglo
- [Hygglo Help — How Hygglo works](https://help.hygglo.info/en/articles/10415333-how-hygglo-works) · [What is Hygglo](https://help.hygglo.info/en/articles/10420308-what-is-hygglo) · [Security & protection](https://help.hygglo.info/en/articles/10587214-how-to-provide-great-service-and-understand-security-protection) · [Hygglo Care for lenders](https://help.hygglo.info/en/articles/12890765-hygglo-care-for-lenders)
- [Omocom](https://www.omocom.insurance/en/) · [Van Ameyde — Omocom](https://www.vanameyde.com/stories/omocom-circular-economy/) · [Ellen MacArthur Foundation — Omocom](https://www.ellenmacarthurfoundation.org/circular-examples/creating-trust-in-the-sharing-economy-omocom) · [Circular X — Hygglo case](https://www.circularx.eu/en/cases/75/hygglo-peer-to-peer-rental-instead-of-buying)
- [Sharetribe — How to build a website like Fat Llama](https://www.sharetribe.com/create/how-to-build-website-like-fatllama/) **[nguồn yếu]** · [Yo-Rent — build P2P rental like Fat Llama](https://www.yo-rent.com/blog/build-p2p-rental-website-like-fat-llama/) **[nguồn yếu]**
- [PetaPixel — $5,000 camera gear stolen through Fat Llama](https://petapixel.com/2019/03/20/how-i-had-over-5000-in-camera-gear-stolen-through-fat-llama/) · [DIYPhotography](https://www.diyphotography.net/i-got-5000-worth-of-gear-stolen-from-me-through-fat-llama/) · [Trustpilot — Fat Llama](https://www.trustpilot.com/review/fatllama.com) · [Reviews.io — Fat Llama](https://www.reviews.io/company-reviews/store/fatllama-com)

### D. Turo & Getaround
- [Turo Help — Security deposits (US)](https://help.turo.com/en_us/security-deposits-us-HkbE44lE9) · [Turo — Trust & Safety](https://turo.com/us/en/trust-and-safety)
- [ComplyCube — Turo case](https://www.complycube.com/en/customer/turo-strengthens-car-sharing-compliance/) · [Mitek — Q&A with Turo Trust & Safety](https://www.miteksystems.com/blog/innovator-qa-mike-wilkins-senior-director-trust-safety-at-turo) · [TechCrunch 03/01/2025 — Turo hires security experts](https://techcrunch.com/2025/01/03/turo-taps-national-security-and-counterterrorism-experts-after-cybertruck-explosion)
- [Jerry — Turo deposit](https://jerry.ai/car-insurance/how-much-is-the-deposit-for-turo/) **[nguồn yếu]** · [Ride-Share.com — Does Turo charge a deposit](https://ride-share.com/does-turo-charge-a-deposit/) **[nguồn yếu]**
- ⭐ [OAG DC — AG Schwalb secures refunds (Getaround)](https://oag.dc.gov/release/attorney-general-schwalb-secures-refunds-dc) · [BBB — Getaround complaints](https://www.bbb.org/us/ca/san-francisco/profile/auto-renting-and-leasing/getaround-1116-390772/complaints) **[nguồn yếu]**

### E. Phần mềm quản lý cho thuê & thanh toán
- [Booqable — Features](https://booqable.com/features/) · [Pricing](https://booqable.com/pricing/) · [Technology & IT Equipment Rental Software](https://booqable.com/industries/technology-rental-software/)
- [Stripe Docs — Extended authorization](https://docs.stripe.com/payments/extended-authorization) · [Stripe Docs — Terminal extended authorizations](https://docs.stripe.com/terminal/features/extended-authorizations) · [Stripe — Preauthorization charges](https://stripe.com/resources/more/preauthorization-charges-on-credit-cards-what-they-are-and-how-long-they-last) · [PayRequest — Stripe deposits guide](https://payrequest.io/guides/stripe-deposits) **[nguồn yếu]** · [PayRequest — Stripe pre-authorization](https://payrequest.io/stripe-pre-authorization/) **[nguồn yếu]**

### F. ĐH FPT & chương trình cho mượn máy tại ĐH
- ⭐ [it-hcm.fpt.edu.vn — Hướng dẫn mượn laptop của sinh viên trong trường](https://it-hcm.fpt.edu.vn/articles.php?news=huong-dan-muon-laptop-cua-sinh-vien-trong-truong&id=56)
- [daihoc.fpt.edu.vn — Hướng dẫn sử dụng và thi trên phần mềm EOS](https://daihoc.fpt.edu.vn/tin-noi-bat-muc-tin-tuc/huong-dan-sinh-vien-su-dung-va-thi-tren-phan-mem-eos-tai-truong-dai-hoc-fpt/) · [it.fpt.edu.vn — Hướng dẫn cài EOS và SEB](https://it.fpt.edu.vn/cantho/huong-dan-cai-dat-phan-mem-thi-eos-seb/) · [Campus Đà Nẵng](https://daihoc.fpt.edu.vn/da-nang/)
- [Stanford — The Hub loan policies](https://thehub.stanford.edu/borrow-equipment/loan-policies) · [UConn Library](https://library.uconn.edu/?p=967) · [KU Libraries fines & fees](https://services.ku.edu/TDClient/818/Portal/KB/Article/20717/KU-Libraries-Fines-Fees-Lost-Item-and-Damage-Charges-for-Library-Equipment-and-Accessories-Laptops-H) · [NIU laptop circulation](https://library.niu.edu/university-libraries/about/policies/laptopcirculation.shtml) · [UNT Dallas laptop checkout](https://www.untdallas.edu/oit/digital-spaces/laptop-checkout.php) · [Columbia Law — Laptop Loaner Program](https://finance-admin.law.columbia.edu/form/laptop-loaner-program-for-studen)
- [LaptopsAnytime](https://www.laptopsanytime.com/) · [Spaces4Learning — Laptop checkouts made easy (2024)](https://spaces4learning.com/whitepapers/2024/03/laptop-checkouts-made-easy.aspx) · [PUPN — Automated dispensing kiosks](https://pupnmag.com/article/laptop-checkouts-automated-dispensing-kiosk-systems-transform-higher-ed-computing/)

---

## 16. GHI CHÚ CUỐI CHO NGƯỜI VIẾT PROPOSAL

1. **Phân biệt rạch ròi 3 loại nội dung khi trích:** `[S]` = dữ liệu có nguồn nhưng chưa mở trang · `[URL-IA]` = suy luận từ URL · 🟠 **`[TK]`** = **thiết kế của nhóm**, phải viết là *"nhóm đề xuất"*, không được viết *"theo nghiên cứu thì"*.
2. **Mục 8–12 (sitemap, luồng, wireframe, trust signals, admin) là ĐÓNG GÓP THIẾT KẾ của nhóm.** Trình bày chúng như vậy sẽ ăn điểm cao hơn là cố làm ra vẻ đó là "phát hiện nghiên cứu".
3. **Ba việc kiểm chứng ưu tiên tuyệt đối, theo thứ tự:** (a) hỏi Phòng Khảo thí về việc dùng máy thuê trong phòng thi; (b) chụp màn hình 6 website đối thủ để làm phụ lục so sánh UX; (c) gọi hotline 3–5 đơn vị ĐN để ghi lại luồng đặt hàng thật.
4. **Luận điểm sản phẩm mạnh nhất rút ra từ tài liệu này:** *"Không đối thủ nào tại Việt Nam cho phép đặt thuê laptop trực tuyến — họ đều chạy bằng hotline. Chúng tôi bán một thứ họ không bán: sự chắc chắn có máy vào đúng ca thi, đặt được lúc 6 giờ sáng, và một biên bản ảnh khiến không ai phải cãi nhau khi trả máy."*
