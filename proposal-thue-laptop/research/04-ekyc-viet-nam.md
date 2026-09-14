# 04 — eKYC / XÁC MINH DANH TÍNH TẠI VIỆT NAM
## Áp dụng cho website cho thuê laptop đi thi — ĐH FPT Đà Nẵng (Hoà Hải, Ngũ Hành Sơn)

> **Tài liệu nghiên cứu thô** — nguyên liệu cho người viết proposal.
> Ngày thực hiện: **14/09/2026**. Ưu tiên dữ liệu 2024–2026.

---

## 0. CẢNH BÁO VỀ PHƯƠNG PHÁP & GIỚI HẠN DỮ LIỆU (ĐỌC TRƯỚC TIÊN)

Phiên nghiên cứu này chạy trong môi trường có **proxy chặn egress**. Kết quả thực tế:

| Nhóm nguồn | Trạng thái | Ví dụ |
|---|---|---|
| GitHub, PyPI, pub.dev, registry.npmjs.org, developer.android.com | ✅ **Fetch được đầy đủ** | github.com, pypi.org, pub.dev |
| Toàn bộ website pháp luật VN | ❌ **Bị chặn** | thuvienphapluat.vn, vanban.chinhphu.vn, vbpl.vn, luatvietnam.vn, bocongan.gov.vn, vcci.com.vn |
| Toàn bộ website nhà cung cấp eKYC VN | ❌ **Bị chặn** | fpt.ai, docs-vision.fpt.ai, ekyc.vnpt.vn, vnpt.vn, vnptgroup.vn, smartid.com.vn |
| Báo chí / blog VN | ❌ **Bị chặn** | vnexpress.net, viblo.asia, medium.com |
| App Store / Google Play / vneid.gov.vn | ❌ **Bị chặn** | apps.apple.com, play.google.com, vneid.gov.vn |
| web.archive.org | ❌ Không khả dụng | — |

Ngân sách WebSearch của phiên cũng đã hết sau 4 truy vấn.

**Do đó tài liệu này phân loại mọi thông tin thành 3 mức tin cậy, và người viết proposal PHẢI tôn trọng phân loại này:**

- 🟢 **[ĐÃ FETCH]** — tôi đã tải trực tiếp trang nguồn và đọc nội dung. Dùng được, trích dẫn được.
- 🟡 **[CHỈ TỪ SNIPPET TÌM KIẾM]** — công cụ tìm kiếm trả về tóm tắt trang, tôi **KHÔNG** mở được trang gốc. **Phải tự kiểm chứng lại** trước khi đưa vào proposal nộp thầy.
- 🔴 **[CHƯA XÁC MINH ĐƯỢC]** — nằm trong mục "Uncertainties". **KHÔNG được viết như sự thật.**

**Kết luận quan trọng nhất của tài liệu:** phần **giá cụ thể bằng VND** của mọi nhà cung cấp eKYC Việt Nam và **số điều khoản chính xác** của Nghị định 69/2024 đều **không fetch được**. Xem Mục 11.

---

## 1. TÓM TẮT ĐIỀU HÀNH — KHUYẾN NGHỊ CHO DỰ ÁN

**Trả lời ngắn cho câu hỏi "startup sinh viên có nên làm eKYC không?":**

> **KHÔNG làm eKYC tự động ở MVP.** Với quy mô ~1 trường đại học, một nhóm sinh viên **không có pháp nhân** thì eKYC chuẩn ngân hàng là **bất khả thi về mặt pháp lý lẫn chi phí**, và còn tạo ra rủi ro pháp lý LỚN HƠN chính rủi ro nó định giải quyết (thu thập ảnh CCCD + dữ liệu sinh trắc học khuôn mặt = dữ liệu cá nhân nhạy cảm).
>
> **Thay vào đó**: xác minh dựa trên **tư cách sinh viên FPT** (mã sinh viên + email `@fpt.edu.vn` + thẻ sinh viên), **giao nhận trực tiếp mặt đối mặt** trong khuôn viên, **hợp đồng thuê giấy/điện tử đơn giản**, và **tiền cọc**. Chỉ nâng cấp lên eKYC thương mại khi đã lập doanh nghiệp và mở rộng ra ngoài trường.

Lý do cốt lõi (đều là dữ kiện đã fetch hoặc suy luận trực tiếp từ dữ kiện đã fetch):

1. **Mọi SDK eKYC VN đều yêu cầu `appKey` / `Token-id` / `Token-key` / `access_token` cấp theo hợp đồng** — FINOS 🟢, Kalapa 🟢, VNPT 🟢, FPT.AI 🟢. Không có nhà cung cấp nào cho tự đăng ký ẩn danh rồi chạy production.
2. **Model nhận dạng khuôn mặt "miễn phí" phổ biến nhất — InsightFace — CẤM dùng thương mại**: code MIT nhưng *pretrained models* là "non-commercial research only" 🟢. Dịch vụ cho thuê laptop có thu tiền = thương mại ⇒ vi phạm license.
3. **Đọc chip CCCD qua NFC về kỹ thuật là khả thi và miễn phí** (BAC + ISO-DEP) 🟢, nhưng **xác thực chữ ký số của chip với trung tâm RAR‑C06 thì không** — phải qua đơn vị được Bộ Công an cho phép 🟡.
4. Toàn hệ sinh thái GitHub công khai chỉ có **1 repo** đọc chip CCCD VN qua NFC 🟢 — cho thấy đây **không** phải thứ một nhóm sinh viên nên tự làm trong 1 học kỳ.

---

## 2. VNeID & NGHỊ ĐỊNH 69/2024/NĐ-CP

### 2.1. Những gì xác minh được

🟡 **[CHỈ TỪ SNIPPET TÌM KIẾM — chưa mở được trang gốc]**

| Nội dung | Giá trị | Nguồn (KHÔNG fetch được, chỉ snippet) |
|---|---|---|
| Tên văn bản | Nghị định 69/2024/NĐ-CP quy định về định danh và xác thực điện tử | [Nghị định 69/2024/NĐ-CP — thuvienphapluat.vn](https://thuvienphapluat.vn/van-ban/Cong-nghe-thong-tin/Nghi-dinh-69-2024-ND-CP-quy-dinh-dinh-danh-xac-thuc-dien-tu-597437.aspx) |
| Ngày ban hành | 25/6/2024 | [vanban.chinhphu.vn](https://vanban.chinhphu.vn/?pageid=27160&docid=210491) |
| Ngày hiệu lực | **01/7/2024** | như trên |
| Thay thế | Nghị định 59/2022/NĐ-CP | như trên |
| Cấu trúc | **6 chương, 41 điều** | như trên |
| Phạm vi điều chỉnh | Danh tính điện tử; cấp & quản lý tài khoản định danh điện tử; cập nhật/lưu trữ thông tin trong hệ thống định danh & xác thực điện tử; **điều kiện kết nối vào hệ thống**; dịch vụ xác thực điện tử; trình tự cấp/khoá/mở khoá căn cước điện tử | như trên |
| Đối tượng áp dụng | Cơ quan, tổ chức, công dân VN; tổ chức/cá nhân nước ngoài cư trú & hoạt động tại VN tham gia hoặc liên quan hoạt động định danh & xác thực điện tử | như trên |
| Cơ quan phát triển VNeID | Trung tâm Dữ liệu quốc gia về dân cư — Bộ Công an | [Bộ Công an — Nghị định quy định về định danh và xác thực điện tử](https://bocongan.gov.vn/chinh-sach-phap-luat/bai-viet/nghi-dinh-quy-dinh-ve-dinh-danh-va-xac-thuc-dien-tu-d1-t1418) |

### 2.2. Mức độ 1 vs Mức độ 2 — 🔴 CHƯA XÁC MINH ĐƯỢC SỐ ĐIỀU

Tôi **không mở được** toàn văn nghị định nên **không trích được số điều và danh sách trường thông tin chính xác** của tài khoản mức 1 / mức 2. Đây là lỗ hổng dữ liệu, đã ghi vào `uncertainties`.

**Việc người viết proposal phải làm:** mở [Nghị định 69/2024/NĐ-CP trên thuvienphapluat.vn](https://thuvienphapluat.vn/van-ban/Cong-nghe-thong-tin/Nghi-dinh-69-2024-ND-CP-quy-dinh-dinh-danh-xac-thuc-dien-tu-597437.aspx) hoặc [bản trên Cổng thông tin Chính phủ](https://vanban.chinhphu.vn/?pageid=27160&docid=210491) từ máy cá nhân (2 trang này chỉ bị chặn trong môi trường chạy nghiên cứu, không bị chặn ở VN), tra đúng điều khoản, rồi điền vào bảng khung dưới đây:

| Tiêu chí | Mức độ 1 | Mức độ 2 |
|---|---|---|
| Điều khoản quy định | _(điền)_ | _(điền)_ |
| Cách đăng ký | _(điền)_ | _(điền)_ |
| Có cần đến cơ quan Công an không | _(điền)_ | _(điền)_ |
| Có thu sinh trắc học (ảnh, vân tay) không | _(điền)_ | _(điền)_ |
| Giá trị pháp lý khi giao dịch | _(điền)_ | _(điền)_ |

*(Hiểu biết phổ thông — **KHÔNG trích dẫn được, chỉ để định hướng tra cứu**: mức 1 thường đăng ký online trên app, thông tin cơ bản; mức 2 phải đến cơ quan Công an để thu nhận sinh trắc học và có giá trị thay thế giấy tờ. **Phải kiểm chứng trước khi viết.**)*

### 2.3. VNeID có API cho bên thứ ba không?

🟡 **[CHỈ TỪ SNIPPET]** Có cơ chế kết nối, nhưng **không phải API mở**:

- Doanh nghiệp/tổ chức **có thể kết nối** vào hệ thống định danh & xác thực điện tử và sử dụng dịch vụ xác thực điện tử để xác thực thông tin công dân, **khi hệ thống của bên thứ ba đáp ứng đủ điều kiện kết nối** — [Bộ Công an](https://bocongan.gov.vn/chinh-sach-phap-luat/bai-viet/nghi-dinh-quy-dinh-ve-dinh-danh-va-xac-thuc-dien-tu-d1-t1418).
- Công dân chia sẻ thông tin cho bên thứ ba (cổng DVC quốc gia, ngân hàng, tổ chức, doanh nghiệp) **qua quét mã QR trong ứng dụng VNeID** hoặc giải pháp kỹ thuật khác — như trên.
- Mọi khai thác đều cần **sự đồng ý của chủ tài khoản**.

🟡 **QUY ĐỊNH MỚI RẤT QUAN TRỌNG — cần kiểm chứng gấp:** theo snippet của [luatvietnam.vn — "Thông tin khai thác từ VNeID có được chia sẻ tiếp cho bên thứ ba không?"](https://luatvietnam.vn/linh-vuc-khac/thong-tin-khai-thac-tu-vneid-co-duoc-chia-se-tiep-cho-ben-thu-ba-khong-883-111530-article.html), **từ 28/9/2026**, thông tin khai thác từ ứng dụng VNeID **KHÔNG được chia sẻ tiếp cho bên thứ ba** (cá nhân, cơ quan, tổ chức), trừ 2 ngoại lệ: (a) chủ thể dữ liệu yêu cầu chia sẻ; (b) luật khác có quy định khác.

> ⚠️ Mốc **28/9/2026** rơi **sau** thời điểm nghiên cứu (14/9/2026) — tức là sắp có hiệu lực. Nếu proposal định dùng dữ liệu VNeID, **bắt buộc** phải mở trang trên và xác định đây là văn bản nào (nghị định/thông tư số mấy). Đây là rủi ro pháp lý trực tiếp của mô hình kinh doanh.

### 2.4. Bằng chứng kỹ thuật từ GitHub về VNeID

🟢 **[ĐÃ FETCH]** [GitHub repository search "VNeID"](https://github.com/search?q=VNeID&type=repositories) — **31 repository** liên quan. Đáng chú ý:

| Repo | Ngôn ngữ | Nội dung |
|---|---|---|
| `TaQuangTu/id-scan-fe` | TypeScript | Quét mã QR trên VNeID |
| `Dophi85/Vneid` | — | "App tích hợp dữ liệu API cổng dịch vụ công của quốc gia Việt Nam" |
| `kyonest12/multimodalRAG-VNeid` | Jupyter Notebook | Chatbot RAG hỏi đáp về VNeID |
| `DuySeu/VNeID` | C++ | Quản lý giấy tờ cá nhân (bài tập) |

**Nhận định:** không tồn tại SDK/API client VNeID chính thức, công khai trên GitHub. Toàn bộ là dự án học thuật hoặc quét QR. ⇒ **Bằng chứng gián tiếp mạnh** rằng VNeID **không có API tự phục vụ (self-serve) cho lập trình viên/startup nhỏ**, khác hoàn toàn với mô hình "đăng ký lấy API key" như Stripe/Google.

---

## 3. CCCD GẮN CHIP — ĐỌC CHIP QUA NFC

### 3.1. Về mặt kỹ thuật thuần tuý: KHẢ THI VÀ MIỄN PHÍ

🟢 **[ĐÃ FETCH]** — Repo mở duy nhất về CCCD VN: [huyhuynh1905/flutter-cccd-nfc-reader](https://github.com/huyhuynh1905/flutter-cccd-nfc-reader) (Dart, Flutter, cập nhật 28/5, 0 sao).

Quy trình kỹ thuật repo này mô tả:

| Bước | Nội dung |
|---|---|
| 1 | **Quét MRZ** (Machine Readable Zone) ở mặt sau thẻ **qua camera** |
| 2 | Dẫn xuất khoá **BAC (Basic Access Control)** từ dữ liệu MRZ |
| 3 | Kết nối chip qua **NFC**, thiết lập **Secure Messaging** |
| 4 | Đọc dữ liệu: **họ tên, số CCCD, ngày sinh, giới tính, ngày hết hạn, ảnh chân dung** |

Thư viện dùng (🟢 đã fetch từ README repo):

| Thư viện | Vai trò |
|---|---|
| `nfc_manager` | Giao tiếp chip NFC |
| `google_mlkit_text_recognition` | Nhận diện MRZ qua camera |
| `pointycastle` + `crypto` | **TripleDES, SHA1, Retail MAC** (thuật toán bắt buộc của BAC) |
| `camera` | Quét thẻ |

Yêu cầu nền tảng (🟢):

| Nền tảng | Yêu cầu |
|---|---|
| Flutter | ≥ 3.11.4 |
| Android | API 21+ (Android 5.0+), **phần cứng NFC** |
| iOS | **16.0+, iPhone 7 trở lên**, bật NFC capability |
| Thiết bị | ⚠️ **NFC KHÔNG chạy trên Android Emulator / iOS Simulator** — bắt buộc máy thật |

README repo cũng ghi rõ: ứng dụng xử lý **thông tin cá nhân nhạy cảm**, lập trình viên **phải tự đảm bảo tuân thủ quy định bảo vệ dữ liệu**; dự án phục vụ **mục đích học thuật và tham khảo**.

### 3.2. Nền tảng Android cho việc đọc chip

🟢 **[ĐÃ FETCH]** [Android NFC documentation — developer.android.com](https://developer.android.com/develop/connectivity/nfc/nfc):

```xml
<uses-permission android:name="android.permission.NFC" />
<uses-feature android:name="android.hardware.nfc" android:required="true" />
```

- Thẻ chip loại contactless smart card dùng lớp **`android.nfc.tech.IsoDep`** (ISO‑DEP), gửi **APDU thô** bằng `isoDep.transceive(commandApdu)`.
- Intent filter dùng **`ACTION_TECH_DISCOVERED`** với `res/xml/nfc_tech_filter.xml` khai báo `IsoDep` + `NfcA`.
- ⚠️ **Android 17 trở lên**: Activity phải khai báo thêm quyền `android.permission.DISPATCH_NFC_MESSAGE`.

**Chi phí phần mềm để đọc chip: 0 VND** (API hệ điều hành + thư viện mã nguồn mở).

### 3.3. Chuẩn quốc tế & thư viện tham chiếu

🟢 **[ĐÃ FETCH]** [tananaev/passport-reader](https://github.com/tananaev/passport-reader):
- Dùng thư viện **JMRTD** — license **LGPL 3.0** ⚠️ (ràng buộc copyleft: nếu nhúng vào app đóng nguồn phải cho phép người dùng thay thế thư viện / cung cấp object file).
- App bản thân: Apache License 2.0.
- README **không đề cập** yêu cầu cấp phép từ cơ quan nhà nước.

### 3.4. Điểm mấu chốt: ĐỌC ĐƯỢC ≠ XÁC THỰC ĐƯỢC

Đây là điểm **quan trọng nhất** của toàn Mục 3 và cần đưa vào proposal:

| Việc | Tự làm được? | Ghi chú |
|---|---|---|
| Đọc dữ liệu trong chip (tên, số CCCD, ảnh) | ✅ Được, miễn phí, BAC | Nhưng chỉ chứng minh "thẻ này có chip đọc được" |
| Kiểm tra **tính toàn vẹn & chữ ký số** của dữ liệu chip (Passive Authentication) | ❌ Cần **chứng thư số gốc (CSCA)** của Bộ Công an | 🔴 Không tra được cơ chế công bố CSCA của VN |
| Đối chiếu với **CSDL quốc gia về dân cư** để biết thẻ có thật/còn hiệu lực | ❌ **Phải qua RAR‑C06** | Xem Mục 4 |

⇒ Nếu tự đọc chip mà không xác thực chữ ký, **một thẻ CCCD giả có chip ghi dữ liệu tuỳ ý vẫn "đọc thành công"**. Giá trị chống gian lận gần như bằng 0. Đây là lý do các nhà cung cấp thương mại đều quảng cáo "xác thực với RAR‑C06" chứ không chỉ "đọc NFC".

### 3.5. RAR / C06 — 🟡 CHỈ TỪ SNIPPET

| Nội dung | Chi tiết | Nguồn (không fetch được) |
|---|---|---|
| RAR là gì | **Trung tâm nghiên cứu, ứng dụng dữ liệu dân cư và căn cước công dân (RAR)**, trực thuộc **Cục Cảnh sát QLHC về TTXH (C06) — Bộ Công an** | [quangtrungqts.com — Định danh điện tử C06](https://www.quangtrungqts.com/) |
| Số đơn vị được liên kết | Snippet nêu QTS là **1 trong 5 đơn vị** liên kết với RAR, được phép truy cập và xác thực dữ liệu định danh hợp pháp | như trên |
| Vai trò của RAR‑C06 | Xác minh **tính đúng đắn và toàn vẹn của thông tin và chữ ký trên thẻ chip** | [VNPT eKYC IDCheck](https://ekyc.vnpt.vn/vi/idcheck) |
| Thiết bị đọc CCCD | Có **tem chứng nhận RAR (C06)** — thị trường có sản phẩm từ TQ, Mỹ, Hàn, VN; tính năng: đọc chip NFC, QR, MRZ, tích hợp nhận diện khuôn mặt, vân tay, OCR | [azza.vn](https://azza.vn/thiet-bi-doc-can-cuoc-cong-dan-gan-chip-co-tem-chung-nhan-rar-c06/), [smartid.com.vn](https://smartid.com.vn/thiet-bi-xac-thuc-can-cuoc-cong-dan-gan-chip-co-tem-chung-nhan-rar-c06) |
| CCCD gắn chip phát hành từ | **22/01/2021** | [pinata.vn](https://pinata.vn/huong-dan-su-dung-cccd-chip-nfc/) |

🔴 **KHÔNG tra được:** điều kiện cụ thể để doanh nghiệp được kết nối RAR‑C06, hồ sơ cần nộp, thời gian thẩm định, **và CHI PHÍ** (phí kết nối / phí thường niên / phí theo lượt xác thực). Ghi vào `uncertainties`.

---

## 4. KẾT NỐI CSDL QUỐC GIA VỀ DÂN CƯ (C06) — ĐIỀU KIỆN CHO DOANH NGHIỆP

🔴 **CHƯA XÁC MINH ĐƯỢC CHI TIẾT.** Tất cả nguồn quy phạm đều bị chặn.

Những gì **suy ra được một cách an toàn** từ dữ kiện đã có:

1. Nghị định 69/2024/NĐ-CP **có riêng nội dung về "điều kiện kết nối vào hệ thống định danh và xác thực điện tử"** 🟡 — nghĩa là đây là chế độ **cấp phép có điều kiện**, không phải đăng ký tự do.
2. Chỉ có **một số ít đơn vị** được liên kết với RAR‑C06 (snippet nêu con số 5) 🟡 ⇒ đây là mô hình **trung gian được chỉ định**, không phải mô hình mở.
3. Các SDK thương mại quảng cáo tính năng "**C06 verification**" (FINOS 🟢) ⇒ xác nhận rằng **doanh nghiệp thường tiếp cận C06 GIÁN TIẾP qua nhà cung cấp trung gian**, chứ không tự kết nối.

**⇒ Hệ quả trực tiếp cho dự án:** một nhóm sinh viên (dù có pháp nhân hay không) **gần như chắc chắn không thể kết nối trực tiếp C06**. Con đường duy nhất khả thi là **mua dịch vụ của FPT.AI / VNPT / FINOS / Kalapa**, và điều đó **bắt buộc phải có pháp nhân để ký hợp đồng**.

**Người viết proposal cần tra bổ sung (từ máy cá nhân):**
- Nghị định 69/2024/NĐ-CP — chương về điều kiện kết nối.
- Nghị định 70/2024/NĐ-CP (hướng dẫn Luật Căn cước) — cơ chế khai thác CSDL quốc gia về dân cư.
- Thông tư của Bộ Công an về kết nối, chia sẻ dữ liệu dân cư.
- Quy định về **phí khai thác thông tin trong CSDL quốc gia về dân cư** (nếu có thông tư về phí của Bộ Tài chính).

---

## 5. NHÀ CUNG CẤP eKYC THƯƠNG MẠI TẠI VIỆT NAM

### 5.1. Bảng tổng hợp

| Nhà cung cấp | Tính năng xác minh được | Cách lấy credential | NFC CCCD | Xác thực C06 | Giá |
|---|---|---|---|---|---|
| **FPT.AI** | OCR (FPT.AI Vision — IDR), Liveness v3, Face match 🟢 | **API key từ `console.fpt.ai`** 🟢 | 🔴 chưa rõ | 🟡 snippet có nêu | 🔴 **Không công bố** |
| **VNPT eKYC** | OCR, liveness (document + face), masked-face detection, face compare 🟢 | `Token-id`, `Token-key`, `Authorization: Bearer <token>` 🟢 | Có sản phẩm **IDCheck** riêng 🟡 | 🟡 IDCheck xác thực với RAR‑C06 | 🔴 **Không công bố** |
| **FINOS eKYC** | **CCCD NFC reading**, OCR, **Active/Passive liveness**, **Face match 1:1**, **C06 residence verification**, SMS OTP, chữ ký số 🟢 | **`appKey`** do FINOS cấp (có thể tách key riêng cho OCR/NFC/Liveness) 🟢 | ✅ **Có** 🟢 | ✅ **Có** 🟢 | 🔴 **Không công bố** |
| **Kalapa** | eKYC chuẩn (document + face), **NFC eKYC**, **NFC‑only**, liveness v1–v3 🟢 | **session ID (JWT)** tạo từ backend Kalapa, **hiệu lực 10 phút** 🟢 | ✅ **Có** 🟢 | 🔴 chưa rõ | 🔴 **Không công bố** |
| VinCSS | 🔴 Không tìm được dữ liệu trong phiên này | — | — | — | 🔴 |
| Viettel eKYC | 🔴 Không tìm được dữ liệu trong phiên này | — | — | — | 🔴 |
| Trusting Social | 🔴 Không tìm được dữ liệu trong phiên này | — | — | — | 🔴 |
| ZaloPay / MoMo SDK | 🔴 Không tìm được SDK eKYC công khai | — | — | — | 🔴 |

> ⚠️ **KHÔNG có nhà cung cấp eKYC Việt Nam nào công bố bảng giá công khai mà tôi fetch được.** Toàn bộ theo mô hình "liên hệ báo giá". Xem `uncertainties`.

### 5.2. FPT.AI eKYC — chi tiết

🟢 **[ĐÃ FETCH]** từ [daohd2003/FPT_AI_EKYC](https://github.com/daohd2003/FPT_AI_EKYC) — dự án demo .NET 8 tích hợp FPT.AI (repo cập nhật 09/01):

- Dịch vụ FPT.AI được dùng:
  - **FPT.AI Vision (IDR — document recognition)**: OCR "trích xuất thông tin tự động từ ảnh mặt trước CCCD/CMND".
  - **FPT.AI eKYC v3**: **liveness detection** + **face matching** (so selfie với ảnh trên CCCD và với frame video).
- Cấu hình trong `VNeIDAPI/appsettings.json`:
  ```json
  "FptAi": { "ApiKey": "YOUR_FPT_AI_API_KEY_HERE" }
  ```
- **Lấy credential tại `console.fpt.ai`** (cần tài khoản FPT.AI).
- Stack demo: .NET 8, EF Core 9.0.7, SQL Server, Razor Pages, Swagger.

🟡 **[SNIPPET]** từ [FPT AI Vision Documentation](https://docs-vision.fpt.ai/ekyc/I-introduction/gioi-thieu/) và [FPT.AI eKYC — FPT Cloud](https://fptcloud.com/product/fpt-ai-ekyc/):
- Bộ tính năng đầy đủ: **OCR, Image Quality Check, Face Match, Liveness Detection, Fraud Detection, Face Search**.
- OCR nhận dạng CMND/CCCD, Passport, GPLX với **độ chính xác lên tới 98%**.
- Hỗ trợ liveness trên **cả ảnh tĩnh và video** (nhiều phương án theo mức độ rủi ro) — xem [So sánh các phương pháp liveness](https://docs-vision.fpt.ai/en/ekyc/IV-guides/comparing%20liveness%20methods/).
- 🟡 Có nêu **xác thực với CSDL C06 của Bộ Công an**.

### 5.3. VNPT eKYC — chi tiết

🟢 **[ĐÃ FETCH]** từ [VNQuy94/vnpt-ekyc-poc](https://github.com/VNQuy94/vnpt-ekyc-poc) (Java 21, Spring Boot 3, cập nhật ~09/2026):

| Hạng mục | Giá trị |
|---|---|
| **Base URL API** | `https://api.idg.vnpt.vn` |
| **Header xác thực** | `Token-id`, `Token-key`, `Authorization: Bearer <token>` |
| Biến môi trường | `VNPT_BASE_URL`, `VNPT_TOKEN_ID`, `VNPT_TOKEN_KEY`, `VNPT_ACCESS_TOKEN` |
| Web SDK bundle | **v3.2.1.0** |
| Nhóm API | upload ảnh, **OCR tài liệu**, **liveness (document + face)**, **masked face detection**, **face comparison** |
| Kiến trúc khuyến nghị | Backend proxy `/vnpt-proxy/**` — **không gọi trực tiếp từ trình duyệt** (để không lộ credential) |
| Ghi chú của tác giả | "Chưa có runtime VNPT thật" — 5 bước lõi còn ở trạng thái **UNKNOWN** |

🟢 **[ĐÃ FETCH]** SDK mẫu chính thức:
- Android: [joshien1997/ekyc-android-sdk-samples](https://github.com/joshien1997/ekyc-android-sdk-samples) — "Sample Android apps for SDK VNPT eKYC" (Java). Tích hợp bằng **file `.aar`**, khởi chạy `VnptIdentityActivity` với **`ACCESS_TOKEN`, `TOKEN_ID`, `TOKEN_KEY`** truyền qua Intent, nhận kết quả ở `onActivityResult`. Hỗ trợ **minSdkVersion 16**, chạy tốt Android 10+. Luồng "Scan full flow": OCR tài liệu + so khuôn mặt selfie với tài liệu + xử lý ảnh. **Tài liệu KHÔNG đề cập NFC/chip CCCD** và **KHÔNG có thông tin giá**.
- iOS: [vuduc4793/ekyc-ios-sdk-samples](https://github.com/vuduc4793/ekyc-ios-sdk-samples) — "Sample iOS apps for SDK VNPT eKYC" (Objective‑C + Swift demo).
- Các repo khác: [nmhung190398/vnpt-ekyc-web-demo](https://github.com/nmhung190398/vnpt-ekyc-web-demo) (chứa `ekyc-web-sdk-2.1.0.js`, `demo-params.js`, `key.json`), [gonexteam/vnpt_ekyc](https://github.com/gonexteam/vnpt_ekyc), [definev/vnpt_ekyc](https://github.com/definev/vnpt_ekyc).

🟢 Tổng số repo công khai liên quan VNPT/FPT eKYC: **49** — [GitHub search](https://github.com/search?q=VNeID+OR+%22VNPT+eKYC%22+OR+%22FPT.AI+eKYC%22&type=repositories).

🟡 **[SNIPPET]** [VNPT eKYC IDCheck](https://ekyc.vnpt.vn/vi/idcheck): dịch vụ xác thực **tính đúng đắn và toàn vẹn của thông tin và chữ ký trên thẻ chip** với **trung tâm RAR‑C06** của Bộ Công an. [VNPT TP.HCM](https://vnpttphcm.com.vn/vnpt-id-check) quảng cáo "chính xác 100% với CSDL RAR‑C06". OCR của VNPT được nêu **độ chính xác tới 99%** ([VNPT — Nền tảng định danh điện tử](https://vnpt.vn/doanh-nghiep/san-pham-dich-vu/nen-tang-dinh-danh-dien-tu-vnpt-ekyc/)).

### 5.4. FINOS eKYC — nhà cung cấp VN đầy đủ tính năng nhất tìm được

🟢 **[ĐÃ FETCH]** từ [pub.dev/packages/finos_ekyc_flutter](https://pub.dev/packages/finos_ekyc_flutter) và [registry.npmjs.org/finos-ekyc-sdk](https://registry.npmjs.org/finos-ekyc-sdk):

| Hạng mục | Giá trị |
|---|---|
| Tính năng | **Đọc chip NFC CCCD Việt Nam**, OCR, **Active + Passive Liveness**, **Face matching 1:1**, **xác thực cư trú C06**, SMS OTP, chữ ký số |
| Credential | **`appKey`** (FINOS cấp) + `apiKey` (SMS OTP) + `token` (chữ ký điện tử); có thể cấu hình key riêng cho từng module (OCR / NFC / Liveness) |
| License gói | **MIT** |
| Phiên bản npm mới nhất | **2.0.5 — phát hành 09/09/2026** |
| Phiên bản pub.dev | 2.0.5 (cập nhật ~09/09/2026) |
| Repo binary | [github.com/finosvn/finos.ekyc.sdk](https://github.com/finosvn/finos.ekyc.sdk) — **chỉ chứa prebuilt binaries** (iOS XCFramework qua CocoaPods/SPM; Android AAR `asia.finos:*` qua Maven/GitHub Packages), phiên bản 2.0.3; source đóng |
| Yêu cầu nền tảng | React Native ≥ 0.70 (hỗ trợ New Architecture 0.77+), **Android API 24+ (Android 7.0+)**, **iOS 13.0+ (Swift 5.7+, Xcode 16+)**, Node.js ≥ 18 |
| Liên hệ | `finos.technology.vietnam@gmail.com` |
| Trạng thái publisher pub.dev | **"unverified uploader"** ⚠️ |
| **Giá** | 🔴 **Không công bố** |

⚠️ Ghi chú đánh giá: publisher chưa xác minh trên pub.dev + repo chỉ có binary + liên hệ bằng Gmail ⇒ **rủi ro nhà cung cấp (vendor risk) cao**. Không nên đặt cược mô hình kinh doanh vào đây nếu không thẩm định pháp nhân trước.

### 5.5. Kalapa eKYC

🟢 **[ĐÃ FETCH]** từ [registry.npmjs.org/react-native-kalapa-ekyc](https://registry.npmjs.org/react-native-kalapa-ekyc) và [github.com/tobe-ookii/react-native-kalapa-ekyc](https://github.com/tobe-ookii/react-native-kalapa-ekyc):

| Hạng mục | Giá trị |
|---|---|
| 3 luồng hỗ trợ | (1) eKYC chuẩn: giấy tờ + khuôn mặt; (2) **NFC eKYC**: thêm xác thực chip; (3) **NFC‑only** |
| Cơ chế xác thực | **session ID dạng JWT access token** lấy từ backend Kalapa; **hiệu lực mặc định 10 phút**; **không nhúng API key cứng trong client** ✅ (thiết kế tốt về bảo mật) |
| Cấu hình | domain, màu UI, ngôn ngữ, **liveness version 1–3**, dữ liệu điền sẵn (MRZ, face, QR) |
| Phiên bản | **1.3.2 — 09/07/2026** (bật lại quét QR trên iOS); 1.3.1 tối ưu QR Android |
| License | MIT |
| Nền tảng | Android minSdk 24, iOS 13.0+, cần khai báo NFC capability trên iOS |
| **Giá** | 🔴 **Không công bố** |

### 5.6. Các SDK eKYC khác trên npm (tham chiếu so sánh)

🟢 **[ĐÃ FETCH]** [registry.npmjs.org search "ekyc"](https://registry.npmjs.org/-/v1/search?text=ekyc&size=20):

| Gói | Phiên bản | Mô tả |
|---|---|---|
| `@finos_sdk/sdk-ekyc` | 1.5.6 | RN SDK — CCCD NFC, OCR, Liveness, Face matching (VN) |
| `finos-ekyc-sdk` | 2.0.5 | như trên |
| `react-native-kalapa-ekyc` | 1.3.2 | Kalapa eKYC (VN) |
| `@xungchan/ekyc-core` | 0.9.3 | RN iOS/Android, luồng đăng ký + xác minh |
| `my-ekyc` | 1.2.0 | RN cơ bản |
| `@unbraided/kenal-ekyc-rn` | 1.0.0 | Malaysia — MyKad + passport, face liveness |
| `@iapp-technology/ekyc-sdk` | 0.2.1 | Thái Lan — auto-capture OCR, active/passive liveness |
| `pipwave-ekyc-sdk` | 2.2.0 | JS SDK cho web |

🟢 [pub.dev search "ekyc"](https://pub.dev/packages?q=ekyc): **~99 gói** tổng cộng; các gói VN nổi bật là `finos_ekyc_flutter`; các gói khu vực khác: AuthMe eKYC SDK (OCR + NFC passport), Skaletek KYC, Prism eKYC (giấy tờ Nhật + NFC + face).

---

## 6. GIẢI PHÁP MIỄN PHÍ / MÃ NGUỒN MỞ — CHI PHÍ THỰC CHO STARTUP SINH VIÊN

### 6.1. OCR tiếng Việt & giấy tờ

🟢 **[ĐÃ FETCH TOÀN BỘ]**

| Thư viện | License | Phiên bản & ngày | Độ chính xác công bố | Tốc độ | Ghi chú cho dự án |
|---|---|---|---|---|---|
| **VietOCR** ([pypi](https://pypi.org/project/vietocr/), [github](https://github.com/pbcquoc/vietocr)) | PyPI ghi **MIT**; trang GitHub ghi **Apache 2.0** ⚠️ (mâu thuẫn — phải kiểm file LICENSE) | **0.3.13 — 29/03/2024** | Trên tập 10 triệu ảnh: **VGG19‑bn Transformer 88%**, **VGG19‑bn Seq2Seq 87,01%** (full-sequence precision) | Transformer **86 ms**, Seq2Seq **12 ms** | Chuyên tiếng Việt (in + viết tay). **Không có sẵn module trích xuất trường của CCCD** — phải tự làm detection + template |
| **Tesseract** ([tessdata](https://github.com/tesseract-ocr/tessdata)) | **Apache‑2.0** | — | — | — | ⚠️ Trong trang tessdata tôi fetch được, **không thấy hiển thị file `vie.traineddata`** — cần tự kiểm chứng lại |
| **EasyOCR** ([pypi](https://pypi.org/project/easyocr/)) | **Apache 2.0** | **1.7.2 — 24/09/2024** | Không công bố số liệu | — | Quảng cáo 80+ ngôn ngữ; **trang PyPI không nêu rõ có tiếng Việt** |
| **PaddleOCR** ([pypi](https://pypi.org/project/paddleocr/)) | **Apache 2.0** | **3.7.0 — 11/06/2026** | PP‑OCRv6 +4,6% detection / +5,1% recognition so bản trước; PaddleOCR‑VL‑1.6 đạt **96,3%** trên OmniDocBench v1.6 | — | 100+ ngôn ngữ, 50 ngôn ngữ trong 1 model hợp nhất (46 ngôn ngữ hệ Latin); **không nêu rõ tiếng Việt** |
| **Google ML Kit Text Recognition** | — | — | — | — | 🟢 Được dùng trong repo `flutter-cccd-nfc-reader` (gói `google_mlkit_text_recognition`) để đọc MRZ — chạy **on‑device**. 🔴 Chưa fetch được trang giá/điều khoản chính thức |

🟢 Cộng đồng đã có sẵn nhiều dự án OCR CCCD: [GitHub search "CCCD OCR"](https://github.com/search?q=CCCD+OCR&type=repositories) — **47 repository**, ví dụ `Vietnamese-Paper-OCR-Application` (Python, 6 sao, nhận dạng CCCD/CMND/sổ hộ khẩu), `OCR_Vietnamese_Read_CCCD` (3 sao), `OCR_CCCD_FlaskAPI` (3 sao, triển khai Flask API), `QuangDuyxyz/OCR_CCCD` (3 sao, 08/2025), `2tocom/cccd-ocr` (2 sao, 05/2025).

### 6.2. So khớp khuôn mặt (Face match)

🟢 **[ĐÃ FETCH TOÀN BỘ]**

| Thư viện | License code | ⚠️ License MODEL | Độ chính xác | Ghi chú |
|---|---|---|---|---|
| **`face_recognition`** ([github](https://github.com/ageitgey/face_recognition)) | **MIT** | dlib model đi kèm | **99,38% trên LFW** | Python 3.3+/2.7, cần dlib + cmake, **macOS/Linux** (Windows không hỗ trợ chính thức). **KHÔNG có liveness detection** |
| **DeepFace** ([pypi](https://pypi.org/project/deepface/)) | **MIT** | — | **FaceNet512 98,4%**; FaceNet 97,4%; Dlib 96,8%; VGG‑Face 96,7%; ArcFace 96,7%; GhostFaceNet 93,3%; SFace 93,0%; OpenFace 78,7%; DeepFace 69,0%; DeepID 66,5% (LFW) | **v0.0.100 — 09/05/2026**. ✅ **Có module anti‑spoofing** qua tham số `anti_spoofing` |
| **InsightFace** ([pypi](https://pypi.org/project/insightface/), [github](https://github.com/deepinsight/insightface)) | Code **MIT** | 🔴 **PRETRAINED MODELS: "non‑commercial research only"** | Hạng 1 track VISA của **NIST‑FRVT 1:1** | **v2.0 — 08/09/2026**. Model mặc định `buffalo_l`, tự tải về `~/.insightface/models/`. Thuật toán: ArcFace, SubCenter ArcFace, PartialFC, VPL |

> 🚨 **CẢNH BÁO LICENSE — ĐIỂM CHẾT NGƯỜI CHO PROPOSAL**
> InsightFace là lựa chọn "miễn phí" phổ biến nhất trong các đồ án sinh viên VN. Nhưng trang PyPI ghi rõ: *"The pretrained models provided with this library are for non-commercial research only"* — và giải thích: **bạn được dùng code theo MIT cho mục đích thương mại, nhưng TRIỂN KHAI MODEL pretrained đi kèm cho mục đích thương mại là VI PHẠM**.
> Dịch vụ cho thuê laptop **có thu tiền** = thương mại. ⇒ **Nếu proposal viết "dùng InsightFace để xác thực khuôn mặt khách thuê" thì đó là một lỗi pháp lý có thể bị thầy bắt lỗi.**
> **Thay thế an toàn:** dùng **DeepFace** (MIT) với model **FaceNet512 (98,4% LFW)** hoặc **`face_recognition`** (MIT, 99,38% LFW).

### 6.3. Liveness / chống giả mạo (Anti‑spoofing)

🟢 **[ĐÃ FETCH]** [minivision-ai/Silent-Face-Anti-Spoofing](https://github.com/minivision-ai/Silent-Face-Anti-Spoofing):

| Chỉ tiêu | Giá trị |
|---|---|
| License | **Apache‑2.0** ✅ (dùng thương mại được) |
| Cơ chế | Silent liveness — **không cần người dùng tương tác**; dùng phân tích **phổ Fourier** làm giám sát phụ trợ để phân biệt thật/giả trong miền tần số |
| MiniFASNetV1 | **0,081G FLOPs, 0,414M tham số** |
| MiniFASNetV2 | **0,081G FLOPs, 0,435M tham số** |
| Hiệu năng | **TPR 97,8% tại FPR = 1e‑5** (model APK mã nguồn mở) |
| Tốc độ | **20 ms** bản mobile; dải **19–90 ms** tuỳ chip (đã test Snapdragon 845, Kirin) |
| Nền tảng | Có mã nguồn cho **Android** + APK để thử |

⇒ Đây là **lựa chọn liveness miễn phí + license thương mại sạch** tốt nhất tìm được trong phiên này.

### 6.4. Bảng chi phí "stack miễn phí" — ước tính cho MVP

🟢 = chi phí license đã xác minh. 🔴 = chưa xác minh được đơn giá.

| Thành phần | Giải pháp miễn phí | Chi phí license | Chi phí vận hành thực tế |
|---|---|---|---|
| OCR CCCD | VietOCR / PaddleOCR / Tesseract | **0 VND** 🟢 | Cần máy chủ có CPU/GPU — 🔴 chưa khảo giá VPS |
| Face match | DeepFace (FaceNet512) hoặc `face_recognition` | **0 VND** 🟢 | như trên |
| Liveness | Silent‑Face‑Anti‑Spoofing | **0 VND** 🟢 | như trên |
| Đọc chip NFC | Android IsoDep + BAC tự viết / JMRTD | **0 VND** (JMRTD LGPL‑3.0 ⚠️ ràng buộc) 🟢 | Cần **điện thoại thật có NFC**; iOS cần **iPhone 7+ / iOS 16+** |
| Xác thực với C06 | ❌ **KHÔNG có giải pháp miễn phí** | — | Bắt buộc mua dịch vụ ⇒ cần pháp nhân |
| **Tổng license phần mềm** | | **0 VND** | |

**Nhưng chi phí thật không nằm ở license, mà ở:**
1. Công sức phát triển (1 repo CCCD‑NFC công khai duy nhất ⇒ phải tự làm gần như từ đầu).
2. Nghĩa vụ tuân thủ bảo vệ dữ liệu cá nhân (xem Mục 7).
3. Không có khả năng đối chiếu C06 ⇒ **giá trị chống gian lận thực tế thấp**.

---

## 7. RỦI RO PHÁP LÝ KHI TỰ THU THẬP ẢNH CCCD

### 7.1. Rủi ro đã xác minh được bằng nguồn fetch

🟢 **[ĐÃ FETCH]** Bằng chứng trực tiếp rằng chính cộng đồng lập trình viên coi đây là vùng rủi ro:

- README của [flutter-cccd-nfc-reader](https://github.com/huyhuynh1905/flutter-cccd-nfc-reader) nhấn mạnh ứng dụng xử lý **thông tin cá nhân nhạy cảm** và lập trình viên **phải tự đảm bảo tuân thủ quy định bảo vệ dữ liệu**; dự án chỉ dành cho **mục đích học thuật và tham khảo**.
- Tài liệu gói [finos_ekyc_flutter trên pub.dev](https://pub.dev/packages/finos_ekyc_flutter) **không nêu** nghĩa vụ tuân thủ GDPR/CCPA hay luật riêng tư Việt Nam ⇒ **nghĩa vụ tuân thủ rơi hoàn toàn về phía bên tích hợp (tức là nhóm sinh viên)**.
- Kiến trúc mà [vnpt-ekyc-poc](https://github.com/VNQuy94/vnpt-ekyc-poc) khuyến nghị là **backend proxy**, tuyệt đối **không gọi API eKYC trực tiếp từ trình duyệt** — vì credential và ảnh giấy tờ sẽ lộ ra phía client.

### 7.2. Khung pháp lý cần tra — 🔴 CHƯA XÁC MINH ĐƯỢC

Tôi **không fetch được** bất kỳ nguồn quy phạm nào. Danh sách dưới đây là **checklist tra cứu bắt buộc**, **KHÔNG được trích dẫn như sự thật** cho đến khi người viết proposal tự mở và kiểm chứng:

| Văn bản cần tra | Nội dung cần xác định | Vì sao quan trọng với dự án |
|---|---|---|
| **Luật Căn cước 2023** (có hiệu lực 01/7/2024) — điều về **hành vi bị nghiêm cấm** | Có cấm **cầm cố / nhận cầm cố / giữ thẻ căn cước** của người khác không? | 🚨 **Cực kỳ quan trọng**: rất nhiều cửa hàng cho thuê đồ ở VN **giữ CCCD làm tin**. Nếu bị cấm, mô hình "giữ CCCD làm cọc" của dự án là **vi phạm pháp luật** |
| **Luật Bảo vệ dữ liệu cá nhân** (nếu đã có hiệu lực) và/hoặc **Nghị định 13/2023/NĐ-CP** về bảo vệ dữ liệu cá nhân | Ảnh CCCD và **dữ liệu sinh trắc học khuôn mặt** có thuộc **dữ liệu cá nhân nhạy cảm** không? Nghĩa vụ: sự đồng ý, thông báo xử lý, **hồ sơ đánh giá tác động xử lý DLCN**, thời hạn lưu trữ, quyền xoá | Quyết định toàn bộ thiết kế tính năng "tải ảnh CCCD lên web" |
| **Nghị định 69/2024/NĐ-CP** | Điều kiện kết nối hệ thống định danh & xác thực điện tử; ai được cung cấp **dịch vụ xác thực điện tử** | Xác định dự án có được phép "xác thực danh tính" hay không |
| Văn bản có hiệu lực **28/9/2026** về chia sẻ thông tin khai thác từ VNeID | Số hiệu văn bản, phạm vi cấm chia sẻ cho bên thứ ba | Nếu dự án nhận dữ liệu VNeID từ khách rồi lưu lại ⇒ có thể vi phạm |
| Quy định xử phạt vi phạm hành chính trong lĩnh vực dữ liệu cá nhân / an ninh mạng | Mức phạt (VND) | Để viết mục "rủi ro" trong proposal có sức nặng |

### 7.3. Nguyên tắc thiết kế giảm rủi ro (áp dụng được ngay, không cần chờ tra luật)

Các nguyên tắc này là **thực hành tốt phổ quát**, suy ra trực tiếp từ kiến trúc mà các nguồn đã fetch khuyến nghị:

1. **Data minimisation** — chỉ thu thập cái thật sự cần: **mã số sinh viên + họ tên + số điện thoại**. Không thu ảnh CCCD nếu không bắt buộc.
2. **Không lưu ảnh CCCD**. Nếu buộc phải đối chiếu, đối chiếu **trực tiếp tại quầy**, tick "đã xem giấy tờ", **không chụp, không upload, không lưu**.
3. **Không lưu vector khuôn mặt** nếu không có cơ sở pháp lý rõ ràng — dữ liệu sinh trắc học là loại rủi ro cao nhất.
4. Nếu bắt buộc lưu: **mã hoá at‑rest**, **đặt hạn xoá tự động** (ví dụ xoá sau khi kết thúc hợp đồng thuê + N ngày), **nhật ký truy cập**.
5. **Không bao giờ** đặt credential eKYC ở frontend — luôn qua **backend proxy** (mô hình của [vnpt-ekyc-poc](https://github.com/VNQuy94/vnpt-ekyc-poc) 🟢).
6. Có **văn bản đồng ý** (consent) rõ ràng, tách bạch, ghi rõ mục đích – phạm vi – thời hạn lưu.
7. Ghi vào proposal một mục **"Giới hạn & tuân thủ"** — điều này thường được chấm điểm cao trong bài tập khởi nghiệp.

---

## 8. STARTUP SINH VIÊN **KHÔNG CÓ PHÁP NHÂN** — ĐƯỢC VÀ KHÔNG ĐƯỢC LÀM GÌ

> Phần này kết hợp **dữ kiện đã fetch** (mức tin cậy cao) với **suy luận trực tiếp** từ các dữ kiện đó. Những chỗ cần tra luật đã được đánh dấu 🔴.

### 8.1. ❌ KHÔNG ĐƯỢC / KHÔNG THỂ LÀM

| # | Việc | Mức tin cậy | Căn cứ |
|---|---|---|---|
| 1 | **Kết nối trực tiếp vào CSDL quốc gia về dân cư (C06/RAR)** | 🟢 Rất cao | Chỉ một số ít đơn vị được liên kết với RAR‑C06 🟡; Nghị định 69/2024 quy định **điều kiện kết nối** 🟡 ⇒ đây là chế độ cấp phép cho **tổ chức**, không cho cá nhân |
| 2 | **Ký hợp đồng dịch vụ eKYC với FPT.AI / VNPT / FINOS / Kalapa ở tư cách "nhóm sinh viên"** | 🟢 Cao | Cả 4 nhà cung cấp đều cấp credential theo tài khoản/hợp đồng: `appKey` (FINOS 🟢), session JWT từ backend (Kalapa 🟢), `Token-id`/`Token-key` (VNPT 🟢), API key `console.fpt.ai` (FPT.AI 🟢). 🔴 Chưa xác minh được liệu họ có bán cho **cá nhân** hay không — **phải hỏi trực tiếp** |
| 3 | **Xuất hoá đơn VAT hợp lệ cho khách thuê** | 🟢 Cao (hệ quả hiển nhiên của việc không có MST) | — |
| 4 | **Tự xưng là "dịch vụ xác thực điện tử"** | 🟡 | Nghị định 69/2024 có chương riêng về **dịch vụ xác thực điện tử** và ai được cung cấp 🟡 ⇒ đây là ngành nghề có điều kiện |
| 5 | **Dùng model pretrained của InsightFace trong dịch vụ có thu tiền** | 🟢 **Chắc chắn** | [PyPI InsightFace](https://pypi.org/project/insightface/): pretrained models **"non-commercial research only"** |
| 6 | **Giữ/cầm cố thẻ CCCD của khách làm tài sản bảo đảm** | 🔴 **PHẢI TRA LUẬT CĂN CƯỚC 2023** | Nghi vấn có trong danh mục hành vi bị nghiêm cấm — **kiểm chứng trước khi đưa vào mô hình vận hành** |
| 7 | **Thu thập & lưu trữ ảnh CCCD + dữ liệu sinh trắc học ở quy mô có tổ chức** | 🔴 Cần tra Nghị định 13/2023 / Luật BVDLCN | Nghĩa vụ (hồ sơ đánh giá tác động, đăng ký...) thường đặt lên **tổ chức**; nhóm không pháp nhân khó đáp ứng |
| 8 | **Chia sẻ tiếp cho bên thứ ba thông tin khai thác từ VNeID** | 🟡 | Quy định dự kiến hiệu lực **28/9/2026** 🟡 |

### 8.2. ✅ ĐƯỢC LÀM (phù hợp cho MVP môn Khởi nghiệp)

| # | Việc | Ghi chú |
|---|---|---|
| 1 | **Xây website/app demo**, chạy thử nghiệm trong nhóm & với bạn bè, coi là **dự án học thuật** | Đúng như tinh thần repo `flutter-cccd-nfc-reader` tự mô tả: "academic and reference purposes" 🟢 |
| 2 | **Xác minh dựa trên tư cách sinh viên FPT**: mã sinh viên + **email `@fpt.edu.vn`** (gửi OTP/magic link) + đối chiếu **thẻ sinh viên** khi giao máy | Không đụng dữ liệu nhạy cảm, chi phí ~0 VND, độ tin cậy thực tế **cao hơn** eKYC vì có ràng buộc thể chế (trường biết bạn là ai) |
| 3 | **Đối chiếu giấy tờ trực tiếp (visual check) tại điểm giao nhận** — nhìn CCCD/thẻ SV, tick xác nhận, **không chụp lưu** | Giảm mạnh nghĩa vụ bảo vệ dữ liệu |
| 4 | **Hợp đồng thuê tài sản dân sự giữa các cá nhân** + biên bản bàn giao có chữ ký + ảnh tình trạng máy | Giao dịch dân sự giữa cá nhân — 🔴 nên tra Bộ luật Dân sự 2015 về hợp đồng thuê tài sản để viết đúng thuật ngữ |
| 5 | **Thu tiền cọc** thay vì giữ giấy tờ | Tránh hoàn toàn rủi ro #6 ở bảng trên |
| 6 | **Dùng thư viện mã nguồn mở license thương mại sạch** để làm demo kỹ thuật: DeepFace (MIT), `face_recognition` (MIT), Silent‑Face‑Anti‑Spoofing (Apache‑2.0), PaddleOCR/EasyOCR/Tesseract (Apache‑2.0), VietOCR | 🟢 Tất cả license đã xác minh |
| 7 | **Đọc chip CCCD qua NFC để tự kiểm tra kỹ thuật** trên máy của chính mình (demo) | 🟢 Kỹ thuật miễn phí; **nhưng không được quảng cáo là "xác thực"** vì không có Passive Authentication với CSCA |
| 8 | **Thiết kế kiến trúc backend‑proxy sẵn sàng cắm eKYC thương mại về sau** | Cho phép viết trong proposal: "khi lên pháp nhân, chỉ cần cắm API key là chạy" — điểm cộng cho lộ trình mở rộng |
| 9 | **Đăng ký hộ kinh doanh cá thể** (nếu muốn hợp thức hoá sớm với chi phí thấp) | 🔴 Chưa tra được lệ phí đăng ký và thủ tục — cần bổ sung |

### 8.3. Lộ trình 3 giai đoạn đề xuất (đưa thẳng vào proposal)

| Giai đoạn | Tư cách pháp lý | Cơ chế xác minh | Chi phí eKYC |
|---|---|---|---|
| **P0 — MVP (học kỳ này)** | Nhóm sinh viên, dự án học thuật | Email `@fpt.edu.vn` + mã SV + thẻ SV đối chiếu trực tiếp + cọc + hợp đồng giấy | **0 VND** |
| **P1 — Vận hành thật trong trường** | **Hộ kinh doanh cá thể** | P0 + OCR mã SV tự động (PaddleOCR/VietOCR) + chụp ảnh tình trạng máy | **0 VND** license 🟢, 🔴 chưa rõ chi phí VPS |
| **P2 — Mở rộng ngoài trường** | **Doanh nghiệp (TNHH)** | Ký hợp đồng eKYC thương mại: OCR + liveness + face match + **xác thực C06** qua FPT.AI / VNPT / FINOS / Kalapa | 🔴 **Chưa xác minh được — phải xin báo giá** |

---

## 9. KIẾN TRÚC KỸ THUẬT ĐỀ XUẤT CHO MVP (P0/P1)

```
[ Web (Next.js / React) ]
        |  HTTPS
        v
[ Backend API (Node/Spring/.NET) ]   <-- credential eKYC CHỈ nằm ở đây (nếu có P2)
        |
        +--> [ Xác minh sinh viên ]
        |       - Gửi magic-link / OTP tới email @fpt.edu.vn
        |       - Lưu: mã SV (hash), email, SĐT. KHÔNG lưu ảnh CCCD.
        |
        +--> [ Đặt lịch + hợp đồng ]
        |       - Sinh hợp đồng thuê PDF, ký khi nhận máy
        |
        +--> [ Bàn giao tại quầy ]
                - Nhân viên đối chiếu thẻ SV trực quan -> tick "đã xác minh"
                - Chụp ảnh TÌNH TRẠNG MÁY (không phải giấy tờ)
                - Thu cọc

[ (P2, sau khi có pháp nhân) ]
Backend --> /ekyc-proxy/** --> api.idg.vnpt.vn  (Token-id / Token-key / Bearer)
                           hoặc FPT.AI (api-key từ console.fpt.ai)
                           hoặc FINOS SDK (appKey) / Kalapa (session JWT 10 phút)
```

**Lý do kiến trúc proxy (🟢 theo [vnpt-ekyc-poc](https://github.com/VNQuy94/vnpt-ekyc-poc)):** SDK web gọi về backend của mình theo `/{prefix}/**`, backend **strip prefix** rồi forward tới upstream, **gỡ bỏ hop-by-hop header và credential header ở biên proxy**, giữ nguyên status/body/content-type.

---

## 10. CHECKLIST VIỆC CẦN LÀM TIẾP (cho người viết proposal)

- [ ] Mở [Nghị định 69/2024/NĐ-CP](https://thuvienphapluat.vn/van-ban/Cong-nghe-thong-tin/Nghi-dinh-69-2024-ND-CP-quy-dinh-dinh-danh-xac-thuc-dien-tu-597437.aspx) → điền bảng Mức 1 / Mức 2 ở Mục 2.2, ghi **số điều**.
- [ ] Tra **Luật Căn cước 2023**, điều về hành vi bị nghiêm cấm → xác định có được **giữ CCCD làm cọc** không. **Ưu tiên số 1.**
- [ ] Tra **Nghị định 13/2023/NĐ-CP** (hoặc Luật BVDLCN nếu đã hiệu lực) → ảnh CCCD & dữ liệu khuôn mặt có phải **DLCN nhạy cảm** không, nghĩa vụ gì.
- [ ] Mở [luatvietnam.vn về chia sẻ thông tin VNeID](https://luatvietnam.vn/linh-vuc-khac/thong-tin-khai-thac-tu-vneid-co-duoc-chia-se-tiep-cho-ben-thu-ba-khong-883-111530-article.html) → xác định **số hiệu văn bản** có hiệu lực 28/9/2026.
- [ ] Gửi email xin báo giá (ghi rõ "sinh viên làm đồ án", hỏi có gói dùng thử / gói startup không):
  - FPT.AI — đăng ký `console.fpt.ai`, `support@fpt.ai`
  - VNPT eKYC — [ekyc.vnpt.vn](https://ekyc.vnpt.vn/vi/idcheck)
  - FINOS — `finos.technology.vietnam@gmail.com` 🟢
  - Kalapa — qua [repo SDK](https://github.com/tobe-ookii/react-native-kalapa-ekyc)
- [ ] Hỏi thêm 4 nhà cung cấp chưa có dữ liệu: **VinCSS, Viettel eKYC (Viettel AI), Trusting Social, MoMo/ZaloPay**.
- [ ] Khảo giá **VPS/cloud VN** (nếu chọn self‑host OCR/face match).
- [ ] Kiểm chứng file `LICENSE` của VietOCR (PyPI ghi MIT, GitHub ghi Apache 2.0 — mâu thuẫn 🟢 đã ghi nhận).
- [ ] Tra thủ tục + lệ phí **đăng ký hộ kinh doanh cá thể** tại phường Hoà Hải / Ngũ Hành Sơn, Đà Nẵng.

---

## 11. DANH MỤC NGUỒN — KÈM TRẠNG THÁI

### 11.1. 🟢 Nguồn ĐÃ FETCH TRỰC TIẾP (dùng được, trích dẫn được)

| # | Nguồn | Hỗ trợ nội dung gì |
|---|---|---|
| 1 | [developer.android.com — NFC](https://developer.android.com/develop/connectivity/nfc/nfc) | IsoDep, quyền NFC, `ACTION_TECH_DISCOVERED`, `DISPATCH_NFC_MESSAGE` (Android 17+) |
| 2 | [github.com/huyhuynh1905/flutter-cccd-nfc-reader](https://github.com/huyhuynh1905/flutter-cccd-nfc-reader) | Quy trình đọc chip CCCD VN: MRZ → BAC → Secure Messaging; thư viện; yêu cầu nền tảng; cảnh báo dữ liệu nhạy cảm |
| 3 | [github.com/tananaev/passport-reader](https://github.com/tananaev/passport-reader) | JMRTD **LGPL‑3.0**, app Apache‑2.0 |
| 4 | [github.com/VNQuy94/vnpt-ekyc-poc](https://github.com/VNQuy94/vnpt-ekyc-poc) | `https://api.idg.vnpt.vn`, header `Token-id`/`Token-key`/`Bearer`, Web SDK v3.2.1.0, nhóm API, kiến trúc proxy |
| 5 | [github.com/joshien1997/ekyc-android-sdk-samples](https://github.com/joshien1997/ekyc-android-sdk-samples) | VNPT eKYC Android SDK: `.aar`, `VnptIdentityActivity`, ACCESS_TOKEN/TOKEN_ID/TOKEN_KEY, minSdk 16, không có NFC, không có giá |
| 6 | [github.com/vuduc4793/ekyc-ios-sdk-samples](https://github.com/vuduc4793/ekyc-ios-sdk-samples) | Tồn tại SDK mẫu iOS của VNPT eKYC |
| 7 | [github.com/daohd2003/FPT_AI_EKYC](https://github.com/daohd2003/FPT_AI_EKYC) | FPT.AI Vision (IDR) + FPT.AI eKYC v3 (liveness, face match); API key từ `console.fpt.ai`; cấu hình `appsettings.json` |
| 8 | [pub.dev/packages/finos_ekyc_flutter](https://pub.dev/packages/finos_ekyc_flutter) | FINOS: NFC CCCD, OCR, liveness, face match, **C06**; `appKey`; MIT; unverified uploader; Android 24+/iOS 13+ |
| 9 | [registry.npmjs.org/finos-ekyc-sdk](https://registry.npmjs.org/finos-ekyc-sdk) | FINOS v2.0.5 (09/09/2026), repo, email liên hệ, yêu cầu RN/Node |
| 10 | [github.com/finosvn/finos.ekyc.sdk](https://github.com/finosvn/finos.ekyc.sdk) | Chỉ chứa prebuilt binaries (XCFramework, AAR `asia.finos:*`), v2.0.3 |
| 11 | [registry.npmjs.org/react-native-kalapa-ekyc](https://registry.npmjs.org/react-native-kalapa-ekyc) | Kalapa: 3 luồng, session JWT 10 phút, liveness v1–3, v1.3.2 (09/07/2026), MIT |
| 12 | [github.com/tobe-ookii/react-native-kalapa-ekyc](https://github.com/tobe-ookii/react-native-kalapa-ekyc) | Xác nhận luồng OCR+Face / NFC / NFC‑only, cần backend session |
| 13 | [registry.npmjs.org search "ekyc"](https://registry.npmjs.org/-/v1/search?text=ekyc&size=20) | Danh sách SDK eKYC VN & khu vực |
| 14 | [pub.dev/packages?q=ekyc](https://pub.dev/packages?q=ekyc) | ~99 gói eKYC trên pub.dev |
| 15 | [pypi.org/project/insightface/](https://pypi.org/project/insightface/) | 🚨 **Pretrained models "non‑commercial research only"**; v2.0 (08/09/2026); buffalo_l |
| 16 | [github.com/deepinsight/insightface](https://github.com/deepinsight/insightface) | Code MIT, model non‑commercial; hạng 1 NIST‑FRVT VISA track; ArcFace/PartialFC/VPL |
| 17 | [github.com/ageitgey/face_recognition](https://github.com/ageitgey/face_recognition) | MIT, **99,38% LFW**, không có liveness, cần dlib+cmake |
| 18 | [pypi.org/project/deepface/](https://pypi.org/project/deepface/) | MIT, v0.0.100 (09/05/2026), bảng LFW 10 model, **có `anti_spoofing`** |
| 19 | [github.com/minivision-ai/Silent-Face-Anti-Spoofing](https://github.com/minivision-ai/Silent-Face-Anti-Spoofing) | Apache‑2.0, MiniFASNetV1/V2 FLOPs & params, **TPR 97,8% @ FPR 1e‑5**, 20 ms mobile |
| 20 | [pypi.org/project/vietocr/](https://pypi.org/project/vietocr/) | MIT, v0.3.13 (29/03/2024), 88% / 87,01%, 86 ms / 12 ms |
| 21 | [github.com/pbcquoc/vietocr](https://github.com/pbcquoc/vietocr) | Apache 2.0 (mâu thuẫn với PyPI), 0.8800 precision, 2 kiến trúc |
| 22 | [pypi.org/project/easyocr/](https://pypi.org/project/easyocr/) | Apache 2.0, v1.7.2 (24/09/2024), 80+ ngôn ngữ |
| 23 | [pypi.org/project/paddleocr/](https://pypi.org/project/paddleocr/) | Apache 2.0, v3.7.0 (11/06/2026), 96,3% OmniDocBench v1.6 |
| 24 | [github.com/tesseract-ocr/tessdata](https://github.com/tesseract-ocr/tessdata) | Apache‑2.0; không thấy `vie` trong listing đã xem |
| 25 | [GitHub search "CCCD OCR"](https://github.com/search?q=CCCD+OCR&type=repositories) | 47 repo OCR CCCD/CMND |
| 26 | [GitHub search "CCCD chip reader nfc"](https://github.com/search?q=cccd+chip+reader+nfc&type=repositories) | **Chỉ 1 repo** đọc chip CCCD VN |
| 27 | [GitHub search VNeID/VNPT eKYC/FPT.AI eKYC](https://github.com/search?q=VNeID+OR+%22VNPT+eKYC%22+OR+%22FPT.AI+eKYC%22&type=repositories) | 49 repo |
| 28 | [GitHub search "VNeID"](https://github.com/search?q=VNeID&type=repositories) | 31 repo, không có SDK chính thức |
| 29 | [github.com/thanhdinhbao/MRZ_Generator](https://github.com/thanhdinhbao/MRZ_Generator) | Công cụ sinh MRZ cho CCCD VN (C#, 20/04/2024) |

### 11.2. 🟡 Nguồn CHỈ CÓ SNIPPET (phải tự kiểm chứng lại)

| Nguồn | Nội dung snippet cung cấp |
|---|---|
| [thuvienphapluat.vn — Nghị định 69/2024/NĐ-CP](https://thuvienphapluat.vn/van-ban/Cong-nghe-thong-tin/Nghi-dinh-69-2024-ND-CP-quy-dinh-dinh-danh-xac-thuc-dien-tu-597437.aspx) | Toàn văn nghị định (BỊ CHẶN) |
| [vanban.chinhphu.vn — Nghị định 69/2024](https://vanban.chinhphu.vn/?pageid=27160&docid=210491) | 25/6/2024; hiệu lực 1/7/2024; 6 chương 41 điều; thay NĐ 59/2022 |
| [bocongan.gov.vn](https://bocongan.gov.vn/chinh-sach-phap-luat/bai-viet/nghi-dinh-quy-dinh-ve-dinh-danh-va-xac-thuc-dien-tu-d1-t1418) | Điều kiện kết nối; chia sẻ qua QR VNeID; cần đồng ý của chủ tài khoản |
| [luatvietnam.vn — chia sẻ thông tin VNeID cho bên thứ ba](https://luatvietnam.vn/linh-vuc-khac/thong-tin-khai-thac-tu-vneid-co-duoc-chia-se-tiep-cho-ben-thu-ba-khong-883-111530-article.html) | **Từ 28/9/2026 không được chia sẻ tiếp cho bên thứ ba**, trừ 2 ngoại lệ |
| [docs-vision.fpt.ai — Giới thiệu eKYC](https://docs-vision.fpt.ai/ekyc/I-introduction/gioi-thieu/) | OCR, Image Quality Check, Face Match, Liveness, Fraud Detection, Face Search; **OCR tới 98%** |
| [docs-vision.fpt.ai — So sánh liveness](https://docs-vision.fpt.ai/en/ekyc/IV-guides/comparing%20liveness%20methods/) | Liveness trên ảnh tĩnh và video |
| [fptcloud.com — FPT.AI eKYC](https://fptcloud.com/product/fpt-ai-ekyc/) | Giới thiệu sản phẩm |
| [fpt.ai — FPT AI eKYC](https://fpt.ai/products/fpt-ai-ekyc/) | Trang sản phẩm (BỊ CHẶN) |
| [ekyc.vnpt.vn/vi/idcheck](https://ekyc.vnpt.vn/vi/idcheck) | IDCheck xác thực thông tin & chữ ký trên thẻ chip với **RAR‑C06** |
| [vnpttphcm.com.vn — VNPT ID Check](https://vnpttphcm.com.vn/vnpt-id-check) | "Chính xác 100% với CSDL RAR‑C06 của Bộ Công an" |
| [vnpt.vn — Nền tảng định danh điện tử VNPT eKYC](https://vnpt.vn/doanh-nghiep/san-pham-dich-vu/nen-tang-dinh-danh-dien-tu-vnpt-ekyc/) | OCR độ chính xác tới 99% |
| [vnptgroup.vn — Báo giá VNPT eKYC 2025](https://vnptgroup.vn/bao-gia-dich-vu-dinh-danh-dien-tu-vnpt-ekyc/) | **Có trang báo giá nhưng BỊ CHẶN — chưa đọc được số liệu** |
| [vnpt-dongnai.com — Bảng giá VNPT eKYC](https://vnpt-dongnai.com/gia-vnpt-ekyc.html) | **Có bảng giá nhưng BỊ CHẶN** |
| [quangtrungqts.com — Định danh điện tử C06](https://www.quangtrungqts.com/) | RAR thuộc C06; QTS là 1 trong 5 đơn vị liên kết |
| [azza.vn — thiết bị đọc CCCD tem RAR (C06)](https://azza.vn/thiet-bi-doc-can-cuoc-cong-dan-gan-chip-co-tem-chung-nhan-rar-c06/) | Thiết bị có tem chứng nhận RAR (C06) |
| [smartid.com.vn — thiết bị xác thực CCCD tem RAR (C06)](https://smartid.com.vn/thiet-bi-xac-thuc-can-cuoc-cong-dan-gan-chip-co-tem-chung-nhan-rar-c06) | Chủng loại thiết bị, tính năng |
| [pinata.vn — CCCD chip NFC](https://pinata.vn/huong-dan-su-dung-cccd-chip-nfc/) | CCCD gắn chip phát hành từ **22/01/2021** |
| [ekyc.efy.com.vn — Review TOP5+ nhà cung cấp eKYC VN](https://ekyc.efy.com.vn/hddt/review-nha-cung-cap-ekyc-tot-nhat-tai-viet-nam.html) | Danh sách nhà cung cấp (BỊ CHẶN) |

---

## 12. PHỤ LỤC — TRÍCH DẪN GỐC ĐÁNG GIÁ NHẤT

**InsightFace (PyPI):**
> "The pretrained models provided with this library are for non-commercial research only" — áp dụng cho cả model tải tự động lẫn tải thủ công. Code thư viện MIT dùng thương mại được, **nhưng triển khai model pretrained đi kèm cho mục đích thương mại là vi phạm**.

**`face_recognition` (GitHub):** "The world's simplest facial recognition api for Python and the command line" — **99,38% trên LFW**; tài liệu **không đề cập liveness detection**.

**flutter-cccd-nfc-reader (README):** "Tính năng NFC **không hoạt động** trên Android Emulator hoặc iOS Simulator"; dự án dành cho "academic and reference purposes"; ứng dụng xử lý thông tin cá nhân nhạy cảm, lập trình viên phải tự đảm bảo tuân thủ quy định bảo vệ dữ liệu.

**vnpt-ekyc-poc (README):** "Chưa có runtime VNPT thật" — 5 bước transport lõi ở trạng thái **UNKNOWN**, chưa được kiểm chứng với credential VNPT thật.
