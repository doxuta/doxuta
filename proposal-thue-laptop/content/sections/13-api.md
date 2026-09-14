## Quy ước chung

Giao diện lập trình của ExamLap là REST trên HTTPS, yêu cầu và phản hồi đều là JSON mã hoá UTF-8 với `Content-Type: application/json`. Mốc thời gian theo ISO 8601 kèm múi giờ, ví dụ `2026-09-24T07:00:00+07:00`. Tiền luôn là số nguyên đơn vị đồng, khớp kiểu `integer` của các cột tiền trong lược đồ dữ liệu. Mã định danh là `uuid`, riêng đơn thuê có thêm `code` dạng `EXL26-000123` để đọc qua điện thoại.

**Đánh phiên bản.** Phiên bản nằm trong đường dẫn `/api/v1/...`, trong chương này viết gọn thành `/api/...`. Thêm trường mới hoặc thêm giá trị enum mới thì giữ `v1`; đổi tên trường, bỏ trường hay đổi nghĩa một mã lỗi thì lên `v2` và chạy song song ít nhất một học kỳ, vì ứng dụng nhân viên dạng PWA có thể còn giữ bản cũ trong bộ nhớ đệm.

**Xác thực.** Ba vai người dùng dùng cookie phiên `HttpOnly; Secure; SameSite=Lax` trỏ tới bản ghi phiên trong Redis, lập sau khi bấm liên kết đăng nhập một lần gửi về hộp thư `@fpt.edu.vn`; vai quản trị bắt buộc thêm lớp thứ hai. Lời gọi máy chủ tới máy chủ, tức webhook đối soát và MDM, không dùng cookie mà ký HMAC-SHA256 trên thân yêu cầu thô. Mọi lời gọi thay đổi dữ liệu cần thêm `X-CSRF-Token` khớp phiên.

**Phân trang.** Endpoint trả danh sách dùng con trỏ chứ không dùng số trang: `?limit=20&cursor=<opaque>`, mặc định 20 và tối đa 100. Phản hồi dạng `{"items": [...], "next_cursor": "..."}`, hết dữ liệu thì `next_cursor` là `null`. Con trỏ mã hoá cặp `(created_at, id)` nên thêm bản ghi mới lúc đang duyệt không làm nhảy dòng.

**Cấu trúc lỗi thống nhất.** Mọi lỗi ở mọi endpoint trả đúng một hình dạng. Giao diện đọc `error.code` để quyết định hành vi và hiển thị nguyên văn `error.message`, không tự dịch lại.

```json
{
  "error": {
    "code": "SLOT_SOLD_OUT",
    "message": "Suất này vừa có người khác đặt mất, bạn chọn ca khác nhé.",
    "field": "slot_id",
    "details": { "slot_id": "0f2a...", "next_available_slot_id": "7c41..." },
    "request_id": "req_01JB8Z3M4K"
  }
}
```
{caption: Cấu trúc lỗi dùng chung cho toàn bộ giao diện lập trình, với request_id để đối chiếu ngược vào nhật ký máy chủ.}

`code` là hằng chữ hoa không đổi giữa các phiên bản, `field` chỉ có khi lỗi thuộc một trường cụ thể, `request_id` được ghi kèm mọi dòng nhật ký của yêu cầu đó. Mã HTTP dùng đúng nghĩa: `400` thân yêu cầu hỏng, `401` chưa đăng nhập, `403` không đủ quyền, `404` không tồn tại hoặc không được phép thấy, `409` xung đột trạng thái, `422` đúng cú pháp nhưng sai quy tắc nghiệp vụ, `429` vượt tần suất, `5xx` lỗi của nhóm.

**Mã chống lặp yêu cầu.** Mọi `POST` sinh ra tiền hoặc chiếm tài nguyên đều mang tiêu đề `Idempotency-Key` là một UUID do trình duyệt sinh, theo cách Stripe áp dụng cho các endpoint thay đổi dữ liệu [[ref:https://stripe.com/blog/idempotency]] [[ref:https://brandur.org/idempotency-keys]]. Máy chủ `INSERT ... ON CONFLICT (user_id, key) DO NOTHING` vào `idempotency_keys`; chèn được thì xử lý rồi lưu nguyên văn phản hồi, chèn không được thì trả lại phản hồi cũ, hoặc `409 REQUEST_IN_PROGRESS` nếu đang chạy. Cột `request_hash` giữ SHA-256 của thân yêu cầu, cùng khoá mà thân khác thì trả `422 IDEMPOTENCY_KEY_REUSED`. Khoá giữ 24 giờ *[Cần kiểm chứng]* [[ref:https://httptoolkit.com/blog/idempotency-keys/]] [[ref:https://arpit.substack.com/p/designing-idempotent-payment-apis]].

**Giới hạn tần suất.** Bộ đếm cửa sổ trượt đặt trong Redis, tính theo cả tài khoản lẫn địa chỉ IP và lấy mức chặt hơn [[ref:https://redis.io/tutorials/inventory-reservation-in-real-time-with-redis/]]. Bốn mức: `GET /api/availability` 60 lần mỗi phút mỗi IP, `POST /api/auth/magic-link` 3 lần mỗi giờ mỗi hộp thư, `POST /api/holds` 10 lần mỗi 10 phút mỗi tài khoản, mặc định 120 lần mỗi phút. Mọi phản hồi mang `RateLimit-Limit` và `RateLimit-Remaining`, khi chặn thì trả `429` kèm `Retry-After` tính bằng giây. Riêng webhook giới hạn theo nhà cung cấp chứ không theo IP, vì chặn nhầm báo tiền về còn hại hơn.

<<<pagebreak>>>

## Danh mục endpoint

<<<landscape>>>

| Phương thức | Đường dẫn | Mục đích | Vai gọi được | Ghi chú |
|---|---|---|---|---|
| POST | `/api/auth/magic-link` | Gửi liên kết đăng nhập một lần | Khách | Chỉ nhận đuôi `@fpt.edu.vn` |
| POST | `/api/auth/session` | Đổi mã một lần lấy phiên | Khách | Mã sống 10 phút, dùng một lần |
| DELETE | `/api/auth/session` | Đăng xuất, xoá phiên Redis | SV·NV·QT | |
| POST | `/api/auth/mfa/verify` | Lớp xác thực thứ hai | QT | Bắt buộc với vai quản trị |
| GET | `/api/me` | Hồ sơ, vai, điểm tín nhiệm, bậc cọc | SV·NV·QT | Đọc `users.trust_score` |
| PATCH | `/api/me` | Sửa điện thoại, tài khoản Zalo | SV | Không sửa được `email_fpt` |
| POST | `/api/kyc/submit` | Nộp hai mặt căn cước và video người sống | SV | `multipart`, mỗi tệp ≤ 8 MB |
| GET | `/api/kyc/status` | Trạng thái xác minh và lý do từ chối | SV | Không trả về ảnh gốc |
| POST | `/api/admin/kyc/{id}/decision` | Duyệt tay khi điểm khớp dưới 0,90 | QT | Ghi `audit_logs` |
| GET | `/api/slots` | Ca thi đang mở bán | Công khai | Lọc theo ngày |
| GET | `/api/models` | Nhóm máy A, B, C kèm ngày thử SEB | Công khai | `devices.seb_tested_at` |
| GET | `/api/availability` | Đếm suất còn trống theo ca và nhóm máy | Công khai | Dùng chỉ mục GiST sẵn có |
| POST | `/api/holds` | Giữ suất 10 phút | SV | `Idempotency-Key` |
| GET | `/api/holds/{id}` | Thời gian còn lại của suất giữ | SV | Đếm ngược trên giao diện |
| DELETE | `/api/holds/{id}` | Tự bỏ suất, trả máy về kho | SV | Đổi cờ, không xoá dòng |
| POST | `/api/orders` | Tạo đơn từ suất giữ, sinh VietQR | SV | `Idempotency-Key` |
| GET | `/api/orders` | Danh sách đơn của chính mình | SV | Phân trang con trỏ |
| GET | `/api/orders/{code}` | Chi tiết một đơn | SV·NV·QT | Sinh viên chỉ thấy đơn mình |
| POST | `/api/orders/{code}/contract` | Ký hợp đồng điện tử | SV | Ô tích riêng cho khối loại trừ |
| POST | `/api/orders/{code}/cancel` | Huỷ đơn trước giờ giao | SV | Theo chính sách hoàn cọc |
| GET | `/api/orders/{code}/qr` | Mã QR để nhận máy | SV | Hết hạn sau giờ trả |
| GET | `/api/orders/{code}/payment` | Chuỗi VietQR, số tiền, nội dung | SV | Nội dung là `code` của đơn |
| POST | `/api/webhooks/payment` | Nhận báo có tiền | Dịch vụ đối soát | Ký HMAC, chống phát lại |
| POST | `/api/admin/payments/reconcile` | Đối soát tay giao dịch sai nội dung | QT | Bắt buộc ghi lý do |
| POST | `/api/admin/orders/{code}/refund` | Duyệt hoàn cọc | QT | Mục tiêu dưới 5 phút |
| POST | `/api/orders/{code}/assign` | Gán máy cụ thể cho đơn | NV·QT | Ưu tiên pin cao, ít lượt |
| POST | `/api/uploads/handover-photos` | Xin đường dẫn tải ảnh ký sẵn | NV | Hạn 15 phút |
| POST | `/api/orders/{code}/handover` | Chốt biên bản bàn giao | NV | Đủ 6 ảnh và chữ ký |
| POST | `/api/orders/{code}/swap` | Đổi máy khi máy lỗi giữa ca thi | NV | Cam kết 15 phút |
| POST | `/api/orders/{code}/return` | Chốt biên bản thu hồi | NV | So ảnh trước và sau |
| POST | `/api/orders/{code}/inspection` | Kết luận kiểm tra, khấu trừ | NV·QT | Theo biểu phí công khai |
| POST | `/api/incidents` | Mở phiếu sự cố | SV·NV | Khiếu nại trong 48 giờ |
| GET | `/api/incidents` | Danh sách phiếu theo bộ lọc | NV·QT | |
| PATCH | `/api/incidents/{id}` | Cập nhật khấu trừ và trạng thái | QT | |
| GET | `/api/admin/devices` | Kho máy kèm pin và trạng thái | NV·QT | |
| POST | `/api/admin/devices` | Nhập máy mới vào kho | QT | `asset_tag` và `serial` duy nhất |
| PATCH | `/api/admin/devices/{id}` | Đổi trạng thái vòng đời máy | QT | Chín trạng thái hợp lệ |
| GET | `/api/admin/devices/{id}/timeline` | Lịch sử một máy | QT | Ghép từ `audit_logs` |
| POST | `/api/admin/devices/{id}/lock` | Xin khoá màn hình từ xa | QT | Tạo `lock_requests` |
| POST | `/api/admin/lock-requests/{id}/approve` | Người thứ hai duyệt lệnh khoá | QT | Người xin không tự duyệt |
| GET | `/api/admin/maintenance` | Nhật ký bảo trì | QT | Cảnh báo pin dưới 80% |
| POST | `/api/admin/maintenance` | Ghi một lần sửa chữa và chi phí | QT | |
| GET | `/api/admin/pricing` | Bảng giá đang hiệu lực | NV·QT | `pricing_rules.valid_from` |
| PUT | `/api/admin/pricing` | Ban hành bảng giá mới | QT | Không sửa dòng cũ |
| GET | `/api/admin/reports/revenue` | Doanh thu theo tháng và theo gói | QT | Nguồn của biểu đồ |
| GET | `/api/admin/reports/utilization` | Tỉ lệ khai thác đội máy | QT | |
| GET | `/api/admin/reports/incidents` | Sự cố, khấu trừ, trả trễ | QT | |
| GET | `/api/admin/users` | Danh sách tài khoản | QT | |
| PATCH | `/api/admin/users/{id}` | Khoá, mở khoá, đổi vai | QT | |
| POST | `/api/admin/blocklist` | Thêm số căn cước đã băm vào danh sách chặn | QT | Lưu băm, không lưu số gốc |
| GET | `/api/admin/audit-logs` | Tra nhật ký kiểm toán | QT | Chỉ đọc |
| GET | `/api/admin/audit-logs/verify` | Kiểm toàn vẹn chuỗi băm | QT | Chạy hằng đêm |
| GET | `/api/me/export` | Sinh viên tự tải hồ sơ của mình | SV | JSON kèm CSV |
| POST | `/api/me/deletion-request` | Yêu cầu xoá dữ liệu cá nhân | SV | |
| POST | `/api/admin/deletion-requests/{id}/execute` | Thực thi xoá | QT | Giữ lại chứng từ kế toán |
{caption: Năm mươi lăm endpoint của ExamLap chia theo mười sáu nhóm chức năng, kèm vai được phép gọi.}
{widths: 2,7,7,3,5}
{note: SV sinh viên, NV nhân viên giao nhận, QT quản trị viên. Mọi đường dẫn ngầm hiểu có tiền tố phiên bản `/api/v1`.}

<<<portrait>>>

## Ba endpoint quan trọng nhất

### POST /api/holds

Đây là endpoint quyết định đúng sai của cả hệ thống, vì nó là nơi một chiếc máy thật bị chiếm. Sinh viên chọn ca thi và nhóm máy, máy chủ chọn giúp một máy cụ thể rồi giữ mười phút để khách đi chuyển khoản. Thân yêu cầu có ba tham số: `slot_id`, `model_id` và `waiver` kiểu boolean cho phí miễn trừ thiệt hại.

```json
POST /api/v1/holds
Idempotency-Key: 9f1c2b7e-5d0a-4a11-9c33-6b2e77f0a841

{ "slot_id": "0f2a8c31-...", "model_id": "b7d4-nhomA-...", "waiver": true }

--- 201 Created ---
{
  "hold_id": "3e9b1a77-...",
  "expires_at": "2026-09-24T06:50:00+07:00",
  "seconds_left": 600,
  "quote": { "rent_fee": 79000, "waiver_fee": 15000, "deposit": 300000, "total_due": 394000 }
}
```
{caption: Yêu cầu và phản hồi của endpoint giữ chỗ, với báo giá một ca thi bốn giờ nhóm máy A cộng phí miễn trừ và cọc chuẩn.}

Phản hồi cố ý **không** trả `device_id`: khách không cần biết mình được giữ máy nào, và giấu đi thì nhân viên hoán đổi máy trước giờ giao mà không phải giải thích gì.

| Mã | `error.code` | Ý nghĩa |
|---|---|---|
| 401 | `UNAUTHENTICATED` | Chưa đăng nhập hoặc phiên hết hạn |
| 403 | `KYC_REQUIRED` | Hồ sơ eKYC chưa ở trạng thái đã xác minh |
| 403 | `ACCOUNT_BLOCKED` | Tài khoản bị khoá hoặc số căn cước băm nằm trong `blocklist` |
| 409 | `SLOT_SOLD_OUT` | Hết máy nhóm đó trong ca, sinh từ mã PostgreSQL `23P01` |
| 409 | `DUPLICATE_ORDER_FOR_SLOT` | Đã có một đơn còn sống cho đúng ca thi này |
| 422 | `SLOT_CLOSED` | Ca thi đã qua giờ hoặc đã đóng bán |
| 429 | `RATE_LIMITED` | Quá 10 lần giữ chỗ trong 10 phút |
{caption: Bảy mã lỗi mà endpoint giữ chỗ có thể trả về.}
{widths: 1,4,8}

Bảy quy tắc nghiệp vụ kiểm trong đúng một giao dịch: tài khoản `active` và đã xác minh eKYC; không nằm trong danh sách chặn; ca thi còn mở bán; mỗi sinh viên chỉ một đơn còn sống cho mỗi ca, ép bằng chỉ mục `orders_one_live_per_slot`; `period` ghi vào `inventory_holds` đã cộng 90 phút quay vòng để kịp vệ sinh và nạp pin; `expires_at = now() + interval '10 minutes'`; bậc cọc theo `users.trust_score`, là 300.000đ, 150.000đ hoặc 0đ. Lưới an toàn cuối cùng là ràng buộc `EXCLUDE USING gist (device_id WITH =, period WITH &&)`, thứ khiến chính PostgreSQL từ chối bản ghi chồng lịch dù yêu cầu đến từ API, tác vụ nền hay một lần sửa tay trong `psql` [[ref:https://chat2db.ai/resources/blog/postgres-exclusion-constraints-guide]] [[ref:https://dev.to/franckpachot/postgresql-exclude-constraints-for-better-concurrency-than-serializable-pob]] [[ref:https://blog.danielclayton.co.uk/posts/overlapping-data-postgres-exclusion-constraints/]].

### POST /api/webhooks/payment

Dịch vụ đối soát biến động số dư gọi vào đây khi tiền về tài khoản ngân hàng của nhóm. Nhóm **chưa chọn được nhà cung cấp cụ thể** và chưa lấy được bảng giá của bên nào *[Cần kiểm chứng — xem mục E11 ở Phụ lục E]*, nên đặc tả dưới đây viết theo dạng chung: bất kỳ dịch vụ nào ký gói tin bằng HMAC và gửi lại khi thất bại đều khớp được. Đây là endpoint công khai duy nhất làm đổi trạng thái tiền, nên cũng là bề mặt tấn công đáng lo nhất.

```json
POST /api/v1/webhooks/payment
X-Signature: sha256=6f8a...c214
X-Signature-Timestamp: 1790232600

{
  "provider": "sepay",
  "provider_txn_id": "FT26268123456",
  "amount": 394000,
  "content": "EXL26-000123",
  "account": "0123456789",
  "occurred_at": "2026-09-24T06:44:12+07:00"
}

--- 200 OK ---
{ "received": true, "event_id": "c81f...", "duplicate": false }
```
{caption: Gói tin báo có tiền và phản hồi xác nhận đã ghi nhận, trả về trong dưới 500 mili giây.}

Xử lý theo đúng năm bước. Một, tính lại HMAC-SHA256 trên **thân yêu cầu thô** rồi so sánh bằng hàm hằng thời gian, không dùng toán tử bằng. Hai, từ chối nếu `X-Signature-Timestamp` lệch quá 5 phút so với giờ máy chủ, để gói tin cũ bị chụp lại không dùng lại được. Ba, chèn vào `payments` với `UNIQUE (provider, provider_txn_id)`, nhận mười lần vẫn chỉ ghi một dòng [[ref:https://matheuspalma.com/blog/outbound-webhook-delivery-signing-retries-dead-letters]]. Bốn, trả `200` ngay, việc đổi trạng thái đơn để tác vụ nền làm, vì xử lý chậm sẽ khiến nhà cung cấp timeout rồi gửi lại thành bão [[ref:https://www.educative.io/blog/webhook-system-design]]. Năm, thông báo cho khách đi qua bảng `outbox_messages` ghi trong cùng giao dịch với thay đổi trạng thái [[ref:https://milanjovanovic.tech/blog/implementing-the-outbox-pattern]] [[ref:https://www.npmjs.com/package/pg-transactional-outbox]].

| Mã | `error.code` | Ý nghĩa |
|---|---|---|
| 401 | `INVALID_SIGNATURE` | Chữ ký sai, ghi cảnh báo bảo mật, không xử lý |
| 401 | `SIGNATURE_EXPIRED` | Dấu thời gian lệch quá 5 phút, nghi phát lại |
| 400 | `MALFORMED_PAYLOAD` | Thiếu trường bắt buộc, nhà cung cấp không nên gửi lại |
| 200 | `duplicate: true` | Đã nhận giao dịch này rồi, bỏ qua, vẫn trả 200 |
| 200 | cần đối soát tay | Số tiền thiếu hoặc nội dung không khớp mã đơn nào |
{caption: Phản hồi của endpoint webhook, với nguyên tắc chỉ trả lỗi khi bản thân gói tin sai chứ không trả lỗi vì nghiệp vụ.}
{widths: 1,4,8}

Quy tắc quan trọng nhất là **khớp cả ba điều kiện** trước khi cho đơn sang đã thanh toán: nội dung chuyển khoản chứa đúng `orders.code`, số tiền lớn hơn hoặc bằng số phải trả, và đơn đang ở `pending_payment`. Khách gõ đúng mã nhưng chuyển 39.400đ thay vì 394.000đ thì gói tin vẫn được ghi, đơn vẫn đứng yên, hàng chờ đối soát tay nhận việc. Webhook là đường nhanh, còn nguồn sự thật là tác vụ đối soát chạy mỗi 15 phút, đọc lịch sử giao dịch rồi vá chênh lệch [[ref:https://simplico.net/2026/04/04/idempotency-in-payment-apis-prevent-double-charges-with-stripe-omise-and-2c2p/]] [[ref:https://newsletter.systemdesign.one/p/idempotent-api]].

### POST /api/orders/{code}/handover

Endpoint này biến biên bản giấy thành bằng chứng số. Nó là nơi trách nhiệm với chiếc máy trị giá 6.500.000đ đến 10.000.000đ chuyển từ nhóm sang sinh viên, nên điều kiện chốt rất chặt.

```json
POST /api/v1/orders/EXL26-000123/handover
Idempotency-Key: 44b0e2a1-...

{
  "device_id": "d51a-EL-T490-07",
  "checklist": { "eos_installed": true, "seb_tested": true, "charger": true,
                 "headset_35mm": true, "battery_pct": 96, "wiped": true },
  "os_version": "Windows 11 Pro 24H2",
  "photos": [ { "angle": "mat_a", "upload_id": "u1", "sha256": "e3b0c442..." },
              { "angle": "ban_phim", "upload_id": "u2", "sha256": "5d41402a..." } ],
  "signature_upload_id": "sig_9f",
  "id_match_confirmed": true
}

--- 200 OK ---
{ "order": { "code": "EXL26-000123", "status": "renting",
             "device_asset_tag": "EL-T490-07",
             "return_due_at": "2026-09-24T11:30:00+07:00" },
  "handover_id": "h_7c2e...", "audit_seq": 184213 }
```
{caption: Biên bản bàn giao gửi lên kèm mã băm của từng ảnh; ví dụ rút gọn còn hai trong sáu ảnh bắt buộc.}

| Mã | `error.code` | Ý nghĩa |
|---|---|---|
| 403 | `NOT_ON_SHIFT` | Người gọi không phải nhân viên trực ca đó |
| 404 | `ORDER_NOT_FOUND` | Sai mã đơn, hoặc đơn không thuộc phạm vi được xem |
| 409 | `INVALID_STATE` | Đơn chưa ở trạng thái đã gán máy |
| 422 | `HANDOVER_INCOMPLETE` | Thiếu ảnh, thiếu góc chụp, hoặc thiếu chữ ký khách |
| 422 | `PHOTO_HASH_MISMATCH` | Mã băm gửi lên khác mã băm của tệp đã tải |
| 422 | `PAYMENT_INCOMPLETE` | Chưa thu đủ tiền thuê, phí miễn trừ và cọc |
| 423 | `DEVICE_LOCKED` | Máy đang bị khoá từ xa, không được giao |
{caption: Bảy mã lỗi của endpoint bàn giao, phần lớn là chặn nghiệp vụ chứ không phải lỗi kỹ thuật.}
{widths: 1,4,8}

Sáu quy tắc được kiểm: đơn phải ở trạng thái đã gán máy và `orders.device_id` khác `NULL`; đủ sáu ảnh thuộc sáu góc khác nhau, mỗi ảnh có `sha256` khớp tệp trong kho đối tượng; có chữ ký điện tử của sinh viên; tổng các khoản `payments` trạng thái `succeeded` phải bằng tiền thuê cộng phí miễn trừ cộng cọc; `devices.seb_tested_at` phải nằm trong 24 giờ gần nhất, vì lời hứa bán ra là "máy sẵn sàng thi"; và nhân viên phải xác nhận đã đối chiếu mặt người với ảnh chân dung eKYC. Chốt xong, hệ thống ghi một dòng `handovers` cùng các dòng `handover_photos`, đổi `devices.status` sang đang cho thuê, đẩy `orders.status` sang đang thuê, và nối thêm một mắt xích vào `audit_logs`. Mô hình biên bản có chữ ký học từ bảng `checkout_acceptances` của Snipe-IT [[ref:https://github.com/grokability/snipe-it/blob/master/database/migrations/2018_07_28_023826_create_checkout_acceptances_table.php]], còn việc chuỗi bằng chứng phải chỉ ghi thêm và kiểm tra được bằng mã băm là yêu cầu của mọi hệ theo dõi chuyển giao tài sản [[ref:https://www.locatorx.com/blog/the-truth-about-asset-records-why-immutability-is-the-foundation-of-a-verifiable-chain-of-custody]] [[ref:https://tracehold.ai/blog/immutable-audit-log-hmac-hash-chain/]].

## Bảo mật giao diện lập trình

Tám mục dưới đây nhóm tích từng dòng trước khi mở cho sinh viên dùng thật.

1. **Xác thực chữ ký webhook.** Tính HMAC-SHA256 trên thân yêu cầu thô trước khi phân tích JSON, so sánh hằng thời gian. Khoá bí mật nằm trong biến môi trường, không nằm trong mã nguồn, và đổi được mà không phải triển khai lại.
2. **Chống tấn công phát lại.** Từ chối gói tin lệch giờ quá 5 phút, khử trùng lặp bằng `UNIQUE (provider, provider_txn_id)`, mã đăng nhập chỉ dùng được một lần và sống 10 phút.
3. **Kiểm quyền ở tầng dữ liệu, không chỉ ở tầng giao diện.** Mọi truy vấn đơn thuê của sinh viên mang `WHERE user_id = $session_user` ngay trong câu lệnh, chứ không lọc sau khi đã lấy về. Ẩn một nút trên màn hình không phải là phân quyền.
4. **Không để lộ mã đơn đoán được.** Khoá chính là `uuid` sinh bằng `gen_random_uuid()`; `orders.code` chỉ để đọc qua điện thoại và luôn đi kèm kiểm quyền, vì biết `EXL26-000123` thì đoán ra `EXL26-000124`.
5. **Giới hạn tần suất theo cả tài khoản và địa chỉ.** Lấy mức chặt hơn giữa hai bộ đếm, để một tài khoản đổi IP liên tục hoặc một dải IP tạo nhiều tài khoản đều bị chặn.
6. **Kiểm kích thước và kiểu tệp tải lên.** Ảnh biên bản và ảnh eKYC chỉ nhận `image/jpeg` và `image/png`, tối đa 8 MB mỗi tệp, kiểu thật xác định bằng mã nhận dạng ở đầu tệp chứ không tin phần mở rộng hay `Content-Type`. Tệp lưu dưới tên sinh mới, không giữ tên gốc của khách.
7. **Quét mã độc với ảnh tải lên.** Mọi tệp vào kho đối tượng qua một hàng đợi quét trước khi được hiển thị lại, chưa quét xong thì biên bản chưa chốt được. Đường dẫn tải lên ký sẵn hạn 15 phút, và kho ảnh không phục vụ tệp thẳng ra Internet.
8. **Nhật ký kiểm toán chỉ ghi thêm.** Bảng `audit_logs` có trigger chặn `UPDATE` và `DELETE`, tài khoản ứng dụng bị thu quyền sửa xoá, mỗi dòng chứa mã băm của dòng trước [[ref:https://www.designgurus.io/answers/detail/how-do-you-enforce-immutability-and-appendonly-audit-trails]].

:::warn Điểm yếu nhóm tự nhận
Ba hạng mục chưa kiểm chứng được: cơ chế ký webhook của từng dịch vụ đối soát, giá mỗi lượt gọi eKYC, và độ trễ thật từ lúc tiền vào tài khoản tới lúc webhook về. Cả ba phải hỏi thẳng nhà cung cấp và thử trong môi trường thử nghiệm trước khi chốt thiết kế.
:::
