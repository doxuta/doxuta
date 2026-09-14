## Máy trạng thái của đơn thuê

Đơn thuê của ExamLap không phải một bản ghi có cột trạng thái viết tự do. Nó là một máy trạng thái hữu hạn gồm **13 trạng thái và 17 đường chuyển hợp lệ**; mọi đường không có trong sơ đồ dưới đây đều bị máy chủ từ chối với mã lỗi `409 INVALID_TRANSITION`. Cách làm này không mới: Koha, phần mềm thư viện đang chạy ở hàng nghìn thư viện, khai báo `bookings.status` bằng `enum('new','cancelled','issued','completed')` ngay ở tầng cơ sở dữ liệu chứ không dùng `varchar` tự do [[ref:https://raw.githubusercontent.com/Koha-Community/Koha/master/installer/data/mysql/kohastructure.sql]]. ExamLap cần nhiều trạng thái hơn vì có tiền cọc và có một tài sản vật lý trị giá 6.500.000đ đến 10.000.000đ đi kèm mỗi đơn, nhưng nguyên tắc thì giống hệt.

![Máy trạng thái của đơn thuê ExamLap với mười ba trạng thái, từ Nháp qua Chờ thanh toán, Đã thanh toán, Đã gán máy, Đang thuê cho tới bốn nhánh kết thúc là Đã hoàn cọc, Khách không đến, Mất tài sản và Huỷ do hết hạn giữ, tất cả cùng đổ về trạng thái Đóng.](assets/diagrams/02-trang-thai-don.png){w=12}{src: Nguồn: nhóm tác giả.}

| Trạng thái (`orders.status`) | Ý nghĩa | Ai gây chuyển đổi | Điều kiện bắt buộc | Hệ thống tự làm khi vào | Tối đa ở lại |
|---|---|---|---|---|---|
| Nháp `draft` | Khách đang chọn ca thi và kiểu máy, chưa giữ gì | Sinh viên | Đã đăng nhập bằng `users.email_fpt` | Sinh `orders.code` dạng `EL-8241`, chưa đụng tới kho | 30 phút, sau đó xoá |
| Chờ thanh toán `awaiting_payment` | Một suất kho đã bị khoá cho riêng đơn này | Sinh viên bấm "Chọn máy" | Còn suất rảnh, hồ sơ eKYC ở trạng thái đã xác minh | Ghi `inventory_holds` với `period` và `expires_at = now() + 10 phút`, sinh chuỗi VietQR động, bật đồng hồ đếm ngược | **10 phút** |
| Đã thanh toán `paid` | Tiền cọc và tiền thuê đã về tài khoản | Webhook đối soát | Chữ ký HMAC hợp lệ, số tiền khớp, nội dung chuyển khoản chứa `orders.code` | Xoá `expires_at`, đẩy hai bản tin vào `outbox_messages`, phát mã QR nhận máy | Tới mốc T-60 phút trước giờ giao |
| Đã gán máy `device_assigned` | Đã chốt một máy vật lý cụ thể cho đơn | Nhân viên hoặc tác vụ nền | `devices.status = 'ready'`, máy đã qua 12 mục kiểm tra, `devices.seb_tested_at` trong 7 ngày gần nhất | Điền `orders.device_id`, bật theo dõi MDM, khoá máy khỏi mọi đơn khác | Tới 30 phút sau giờ hẹn |
| Đang thuê `renting` | Máy đã ở trong tay khách | Nhân viên lập biên bản | Đủ 6 ảnh có mã băm SHA-256, chữ ký điện tử của khách, ô đối chiếu khuôn mặt đã tích, kết quả chạy thử EOS | `devices.status = 'rented'`, hẹn ba tin nhắc ở mốc T-12 giờ, T-2 giờ, T+15 phút | Tới `exam_slots.return_due_at` |
| Quá hạn `overdue` | Đã qua giờ trả mà máy chưa về | Tác vụ nền chạy mỗi phút | `now() > exam_slots.return_due_at` | Bắt đầu cộng dồn phí trễ 20.000đ mỗi 30 phút, tối đa 200.000đ một ngày; đẩy cảnh báo lên bảng điều khiển | **48 giờ** |
| Chờ kiểm tra trả `awaiting_inspection` | Máy đã về quầy, đang đối chiếu | Khách quét mã QR trả máy | Nhân viên đã chụp đủ 6 ảnh chiều trả | So ảnh trước và sau, tính phí trễ, khoá thao tác sửa biên bản | 10 phút |
| Có sự cố `incident` | Phát hiện hư hỏng hoặc thiếu phụ kiện | Nhân viên | Có phiếu `incidents` kèm ảnh đối chiếu | Giữ cọc, gửi bảng kê khấu trừ theo biểu phí công khai, mở cửa sổ khiếu nại | 7 ngày, gồm 48 giờ khiếu nại |
| Đã hoàn cọc `refunded` | Đã trả tiền cọc về tài khoản khách | Quản trị viên duyệt lệnh | Biên bản thu hồi đã chốt, chưa từng có lệnh hoàn cọc nào cho đơn này | Ghi `payments` chiều ra, cộng điểm `users.trust_score`, gửi biên lai | 5 phút |
| Khách không đến `no_show` | Quá giờ hẹn mà khách không xuất hiện | Tác vụ nền | Quá 30 phút sau giờ hẹn, đã gọi và nhắn ít nhất hai lần | Nhả máy về `ready`, hoàn tiền theo chính sách huỷ muộn | Tức thì |
| Mất tài sản `lost` | Coi như máy không quay lại | Quản trị viên, hai người duyệt | Quá 48 giờ, không liên lạc được qua cả ba kênh | `devices.status = 'lost'`, kết xuất hồ sơ PDF, ghi tổn thất | 90 ngày hồ sơ pháp lý |
| Huỷ do hết hạn giữ `hold_expired` | Suất giữ hết hạn trước khi tiền về | Tác vụ nền | `expires_at < now()` và chưa có bản ghi `payments` | Đổi `inventory_holds.status` sang `cancelled`, suất tự về kho | Tức thì |
| Đóng `closed` | Không còn nghĩa vụ nào giữa hai bên | Hệ thống | Đã tất toán tiền, đã đóng mọi phiếu sự cố | Đóng băng bản ghi, chỉ còn đọc và kết xuất | Vĩnh viễn |
{caption: Mười ba trạng thái của đơn thuê, kèm tác nhân, điều kiện bảo vệ, hiệu ứng phụ và thời gian tối đa được ở lại.}
{widths: 3,4,3,5,5,3}
{note: Cột cuối là đầu vào của tác vụ nền quét mỗi phút. Trạng thái nào quá thời hạn mà không tự chuyển được sẽ hiện thành cảnh báo trên bảng điều khiển quản trị.}

Điểm cần giải thích kỹ nhất là khoảng cách giữa **Đã thanh toán** và **Đã gán máy**. Khách trả tiền cho một *kiểu máy* chứ không phải cho một *cái máy*. Cột `orders.device_id` để trống suốt từ lúc đặt cho tới trước giờ giao 60 phút, và chỉ khi đó nhân viên hoặc tác vụ nền mới điền vào. Nhóm gọi đây là nguyên tắc **gán máy muộn nhất có thể**. Koha mô hình hoá đúng như vậy: bảng `bookings` có `biblio_id NOT NULL` cho đầu sách và `item_id DEFAULT NULL` cho bản sách cụ thể, với chú thích trong mã nguồn ghi rõ `item_id` mang nghĩa "bản sách mà lệnh giữ này được thực hiện bằng" [[ref:https://raw.githubusercontent.com/Koha-Community/Koha/master/installer/data/mysql/kohastructure.sql]]. Ngành khách sạn làm y hệt khi chuyển từ bán từng phòng sang bán theo hạng phòng [[ref:https://www.hospitalitynet.org/opinion/4074675.html]], và phần mềm cho thuê xe cũng giữ nguyên đơn đặt rồi tự động đổi sang xe khác khi xe dự kiến gặp sự cố [[ref:https://www.altexsoft.com/blog/car-rental-reservation-system/]].

Lợi ích cụ thể với bối cảnh thi cử: 05:30 sáng ngày thi, nhân viên mở máy EL-T490-07 thì màn hình không lên. Nếu hệ thống đã bán đích danh máy đó cho khách thì phải huỷ đơn, hoàn tiền, tạo đơn mới, và khách nhận tin nhắn xấu đúng lúc đang căng thẳng nhất. Với mô hình gán muộn, thao tác chỉ là một câu `UPDATE inventory_holds SET device_id = ...`, ràng buộc `EXCLUDE USING gist` tự kiểm hộ xem máy mới có rảnh trong khung giờ đó không, và khách không hề biết có chuyện gì xảy ra [[ref:https://www.jusdb.com/blog/postgresql-range-types-exclusion-constraints]] [[ref:https://dev.to/franckpachot/postgresql-exclude-constraints-for-better-concurrency-than-serializable-pob]]. Đơn đã bán vẫn nguyên vẹn; chỉ có cái máy bị thay.

Nhóm giữ lại một ngoại lệ có kiểm soát: cột `orders.pinned_device` cho phép khách quen yêu cầu đúng máy đã dùng lần trước. Khi cờ này bật, máy bị gán ngay từ lúc đặt và mất quyền hoán đổi tự động, đổi lại khách được bàn phím và bộ cài đã quen tay.

## Vòng đời thiết bị

Máy trạng thái thứ hai chạy song song, trên bảng `devices`. Đơn thuê và thiết bị là hai vòng đời độc lập, giao nhau đúng hai điểm: lúc gán máy và lúc thu hồi.

![Vòng đời một chiếc laptop trong đội máy ExamLap, từ Nhập kho qua Đang chuẩn bị, Sẵn sàng, Đã bị giữ chỗ, Đang cho thuê, Chờ vệ sinh, với hai nhánh rẽ sang Bảo trì và Mất máy, kết thúc ở Thanh lý.](assets/diagrams/03-vong-doi-thiet-bi.png){w=12}{src: Nguồn: nhóm tác giả.}

| Trạng thái (`devices.status`) | Ý nghĩa | Ai gây chuyển đổi | Điều kiện bắt buộc | Hệ thống tự làm khi vào | Tối đa ở lại |
|---|---|---|---|---|---|
| Nhập kho `intake` | Máy vừa mua, chưa thuộc đội máy khai thác | Quản trị viên | `asset_tag` và `serial` duy nhất, có hoá đơn mua | Khoá khỏi mọi truy vấn máy trống, tạo hồ sơ khấu hao | 3 ngày |
| Đang chuẩn bị `preparing` | Cài ảnh hệ điều hành chuẩn, MDM, BitLocker, EOS, Safe Exam Browser | Nhân viên | Đã khắc laser mã tài sản và dán tem niêm phong | Mở danh mục 12 mục kiểm tra, bắt buộc tích đủ mới đóng được | 90 phút |
| Sẵn sàng `ready` | Máy sẵn sàng thi, hiện ra trong kết quả tra máy trống | Nhân viên | Đủ 12 mục kiểm tra, pin từ 80% trở lên, `seb_tested_at` mới cập nhật | Cộng máy vào tồn kho khả dụng của kiểu máy đó | Không giới hạn, kiểm pin mỗi 14 ngày |
| Đã bị giữ chỗ `held` | Một đơn đang nắm suất của máy trong một khung giờ | Hệ thống | Có dòng `inventory_holds` còn hiệu lực | Chặn mọi đơn khác trùng khung giờ bằng ràng buộc cấp cơ sở dữ liệu | Hết `period` hoặc hết `expires_at` |
| Đang cho thuê `rented` | Máy đang ở ngoài, trong tay khách | Nhân viên bàn giao | Biên bản bàn giao đã chốt | Bật MDM check-in mỗi 15 phút, ghi `custody_events` chiều ra | `return_due_at` cộng 48 giờ |
| Chờ vệ sinh `awaiting_wipe` | Máy đã về nhưng chưa được xử lý | Nhân viên thu hồi | Biên bản thu hồi đã chốt | Tắt theo dõi MDM, ghi `custody_events` chiều vào, **cấm mọi đường chuyển thẳng sang Sẵn sàng** | 12 giờ |
| Bảo trì `maintenance` | Đang sửa hoặc chờ linh kiện | Nhân viên hoặc tác vụ nền | Có dòng `maintenance_logs` kèm lý do | Trừ máy khỏi tồn kho khả dụng, cảnh báo nếu kiểu máy còn dưới `min_amt` | 72 giờ, tiệm đối tác cam kết 24 giờ |
| Mất máy `lost` | Không thu hồi được | Quản trị viên, hai người duyệt | Đơn tương ứng đã ở trạng thái Mất tài sản | Ghi tổn thất, giữ nguyên hồ sơ làm chứng cứ | Tới khi đóng hồ sơ |
| Thanh lý `retired` | Ra khỏi đội máy | Quản trị viên | Chi phí sửa vượt 40% giá trị còn lại, hoặc đã bán | Chốt khấu hao, xoá khỏi mọi bảng tồn kho | Vĩnh viễn |
{caption: Chín trạng thái của một thiết bị, với quy tắc chặn đường tắt từ Chờ vệ sinh sang Sẵn sàng.}
{widths: 3,4,3,5,5,3}
{note: Mô hình ba cờ `deployable`, `pending`, `archived` của Snipe-IT được giữ nguyên để quản trị viên tự tạo nhãn trạng thái mới mà không phải sửa mã.}

Quy tắc quan trọng nhất trong bảng trên là **không có đường tắt từ Chờ vệ sinh sang Sẵn sàng**. Máy vừa từ tay khách về bắt buộc quay lại **Đang chuẩn bị**, tức phải xoá sạch dữ liệu người dùng trước, khôi phục ảnh gốc, chạy lại đủ 12 mục kiểm tra và cập nhật `seb_tested_at`. Lý do có ba. Thứ nhất, sản phẩm bán ra là "máy sẵn sàng thi", và lời hứa đó chỉ đúng nếu mỗi lượt đều được chứng nhận lại. Thứ hai, dữ liệu của người thuê trước còn trên ổ là một sự cố quyền riêng tư, không phải một sự bất tiện. Thứ ba, khoảng 90 phút đệm cộng vào `period` mỗi lượt chính là để dành cho công đoạn này; nếu cho phép đường tắt thì khoảng đệm đó mất ý nghĩa. Odoo gọi khoảng đệm này là thời gian an toàn giữa hai đơn thuê [[ref:https://www.odoo.com/documentation/18.0/applications/sales/rental.html]]. Snipe-IT cài cùng tinh thần theo hướng khác: form giao máy chỉ cho chọn nhãn trạng thái có cờ `deployable`, còn form nhận máy về thì cho chọn mọi nhãn để đưa vào bảo trì hoặc thanh lý [[ref:https://deepwiki.com/grokability/snipe-it/2.5-asset-checkout-and-checkin]].

Ràng buộc này được ép ở tầng dữ liệu chứ không chỉ ở tầng giao diện.

```sql
INSERT INTO device_state_transitions (from_status, event, to_status) VALUES
  ('awaiting_wipe', 'wipe_done',      'preparing'),
  ('awaiting_wipe', 'defect_found',   'maintenance'),
  ('preparing',     'qc_passed',      'ready'),
  ('ready',         'hold_created',   'held');
-- Không có dòng ('awaiting_wipe', *, 'ready'): đường tắt không tồn tại trong dữ liệu.

CREATE OR REPLACE FUNCTION assert_device_transition() RETURNS trigger AS $$
BEGIN
  IF NEW.status <> OLD.status AND NOT EXISTS (
      SELECT 1 FROM device_state_transitions t
      WHERE t.from_status = OLD.status AND t.to_status = NEW.status) THEN
    RAISE EXCEPTION 'Chuyen trang thai khong hop le: % -> %', OLD.status, NEW.status;
  END IF;
  RETURN NEW;
END; $$ LANGUAGE plpgsql;
```
{caption: Bảng chuyển trạng thái thiết bị và trigger chặn mọi đường không khai báo, kèm kiểm thử tự động cố tình đẩy một máy từ `awaiting_wipe` sang `ready` để xác nhận trigger ném lỗi.}

## Luồng đặt thuê và thanh toán

<<<landscape>>>

![Trình tự đặt thuê và thanh toán: sinh viên tra máy trống, giữ chỗ mười phút, nhận mã VietQR động, chuyển khoản, và webhook có chữ ký báo tiền về để đơn chuyển sang Đã thanh toán.](assets/diagrams/05-seq-dat-thue.png){w=0}{src: Nguồn: nhóm tác giả.}

<<<portrait>>>

Luồng có bốn chặng. **Chặng tra cứu**: sinh viên chọn ngày thi, ca thi và kiểu máy; giao diện gọi `GET /api/availability?slot_id=&model_id=`; máy chủ đếm số máy có cờ `deployable` trừ đi số suất đang bị giữ trong cùng khung giờ và trả về, ví dụ, còn 4 suất. Truy vấn này dùng chính chỉ mục GiST đã tạo cho ràng buộc chống trùng lịch nên không cần thêm chỉ mục nào.

**Chặng giữ chỗ** là chỗ dễ sai nhất. Khi khách bấm "Chọn máy", `POST /api/holds` mở một giao dịch, khoá hàng tồn kho bằng `SELECT ... FOR UPDATE SKIP LOCKED` để hai yêu cầu đồng thời không chộp cùng một máy, chèn một dòng `inventory_holds` với `expires_at = now() + interval '10 minutes'`, rồi commit. Ba lớp phòng thủ xếp chồng: giao diện chỉ hiện khung giờ còn trống, giao dịch tuần tự hoá logic, và ràng buộc `EXCLUDE USING gist (device_id WITH =, period WITH &&)` là lưới an toàn cuối cùng, từ chối bản ghi chồng lịch kể cả khi yêu cầu đến từ tác vụ nền hay từ một lần sửa tay trong `psql` [[ref:https://chat2db.ai/resources/blog/postgres-exclusion-constraints-guide]] [[ref:https://blog.danielclayton.co.uk/posts/overlapping-data-postgres-exclusion-constraints/]]. Khi vi phạm, PostgreSQL trả mã `23P01` và tầng ứng dụng đổi thành câu tiếng Việt "Suất này vừa có người khác đặt mất, bạn chọn ca khác nhé".

Giữ chỗ **trước** khi thanh toán, chứ không phải "ai trả tiền trước được máy". Đây là lựa chọn có lý do: nếu để nhiều người cùng chạy đua trả tiền thì sẽ có người chuyển khoản xong mới biết mình mất suất, và khoá lạc quan kiểu đếm phiên bản không dùng được cho luồng có chờ thanh toán [[ref:https://dev.to/iprajapatiparesh/stop-double-booking-optimistic-locking-in-laravel-j5n]]. Mô hình giữ chỗ có hạn là mẫu chuẩn của bài toán giữ hàng trong giỏ [[ref:https://redis.io/tutorials/inventory-reservation-in-real-time-with-redis/]].

Con số **10 phút** là đánh đổi có chủ ý. Ngắn hơn thì khách chuyển khoản chậm bị mất suất; dài hơn thì trong giờ cao điểm sáng ngày thi, một suất bị treo vô ích quá lâu trong khi đội máy chỉ có 10 chiếc.

**Chặng thanh toán**: `POST /api/orders` bắt buộc mang tiêu đề `Idempotency-Key` là một UUID do trình duyệt sinh. Máy chủ `INSERT ... ON CONFLICT (user_id, key) DO NOTHING` vào bảng `idempotency_keys`; chèn được thì xử lý bình thường rồi lưu lại nguyên văn phản hồi, chèn không được thì trả lại đúng phản hồi cũ nếu đã xong, hoặc `409` nếu đang xử lý. Bảng còn lưu `request_hash` là SHA-256 của thân yêu cầu, để cùng một khoá mà thân khác nhau thì bị trả `422`. Đây là cách Stripe làm và là chuẩn thực tế của ngành thanh toán [[ref:https://stripe.com/blog/idempotency]] [[ref:https://brandur.org/idempotency-keys]] [[ref:https://httptoolkit.com/blog/idempotency-keys/]]. Tình huống cụ thể nó cứu: sinh viên bấm nút trên sóng 4G chập chờn trong khuôn viên trường, bấm lại hai ba lần, và nếu không có khoá chống lặp thì sinh ra hai ba đơn, giữ hai ba máy, thu hai ba lần cọc [[ref:https://arpit.substack.com/p/designing-idempotent-payment-apis]].

Hệ thống sinh chuỗi VietQR động với số tiền chính xác và nội dung chuyển khoản chứa `orders.code`. **Chặng đối soát**: khi tiền về, dịch vụ đối soát gọi `POST /webhooks/payment` kèm chữ ký HMAC-SHA256 tính trên thân thô. Máy chủ so chữ ký bằng hàm so sánh hằng thời gian chứ không dùng phép so bằng thường, vì điểm nhận webhook là một URL công khai và ai biết URL cũng có thể giả một thông báo "đã nhận 3 triệu". Sau khi chữ ký hợp lệ, sự kiện được ghi thô vào `payments` với ràng buộc `UNIQUE (provider, provider_txn_id)` rồi trả HTTP 200 ngay; việc đổi trạng thái đơn để tác vụ nền làm. Nhờ vậy cổng gửi lại mười lần thì đơn vẫn chỉ cộng tiền một lần [[ref:https://matheuspalma.com/blog/outbound-webhook-delivery-signing-retries-dead-letters]] [[ref:https://www.educative.io/blog/webhook-system-design]]. Webhook có thể thất lạc, nên mỗi 15 phút có thêm một tác vụ đối soát gọi API lịch sử giao dịch và vá chênh lệch; webhook là đường nhanh, đối soát định kỳ mới là nguồn sự thật.

:::warn Khách chuyển tiền sau khi giữ chỗ đã hết hạn
Đây là tình huống chắc chắn xảy ra và phải có đáp án viết sẵn. Khi `expires_at` trôi qua, tác vụ nền chỉ **đổi cờ** `inventory_holds.status` sang `cancelled` chứ không xoá dòng, nên lịch sử vẫn còn nguyên và ràng buộc chống trùng lịch tự động bỏ qua dòng đã huỷ.
Nếu tiền về sau đó, webhook vẫn được ghi nhận bình thường vì tiền là sự thật đã xảy ra. Hệ thống tra `orders.code` trong nội dung chuyển khoản, thấy đơn đang ở `hold_expired`, và chạy đúng một trong hai nhánh. **Nhánh một**: ca thi đó vẫn còn suất rảnh thì tạo lại giữ chỗ ngay trong cùng giao dịch với việc ghi nhận thanh toán, đơn chuyển thẳng sang Đã thanh toán, khách nhận tin "suất của bạn đã được khôi phục". **Nhánh hai**: ca thi đã kín thì hệ thống **không** giữ tiền im lặng; nó lập tức đẩy một bản tin vào `outbox_messages` báo cho khách và cho quản trị viên, đề xuất ca thi gần nhất còn trống, và nếu khách không chọn trong 30 phút thì lệnh hoàn tiền được dựng sẵn chờ quản trị viên duyệt.
Đây chính là chỗ duy nhất trong hệ thống chạm tới tinh thần giao dịch bù trừ của mẫu Saga, vì cổng thanh toán nằm ngoài giao dịch cơ sở dữ liệu của ExamLap [[ref:https://microservices.io/patterns/data/saga.html]]. Nhóm không dựng Saga đầy đủ, chỉ cài đúng một bước bù trừ cho đúng một tình huống.
:::

## Luồng xác minh danh tính

<<<landscape>>>

![Trình tự xác minh danh tính: sinh viên chụp hai mặt căn cước và quay video ngắn, hệ thống lưu ảnh mã hoá, gửi dịch vụ eKYC chấm điểm, rồi rẽ hai nhánh là tự động duyệt hoặc chuyển sang hàng chờ duyệt tay.](assets/diagrams/06-seq-ekyc.png){w=0}{src: Nguồn: nhóm tác giả.}

<<<portrait>>>

Xác minh chỉ làm một lần cho mỗi tài khoản và là điều kiện tiên quyết để được đặt máy. Sinh viên chụp mặt trước căn cước, mặt sau căn cước, rồi quay một video ngắn quay trái quay phải. Giao diện gửi `POST /api/kyc/submit`. Máy chủ làm hai việc song song: đẩy ảnh và video vào kho đã mã hoá với `kyc_profiles.images_purge_at = now() + 90 ngày`, và gửi sang dịch vụ eKYC để đọc ký tự quang học, kiểm giả mạo và so khớp khuôn mặt. Dịch vụ trả về số căn cước, họ tên, ngày sinh kèm hai điểm số: điểm chống giả mạo và điểm so khớp. Bộ tính năng này là chuẩn của các nhà cung cấp trong nước [[ref:https://docs-vision.fpt.ai/ekyc/I-introduction/gioi-thieu/]] [[ref:https://ekyc.vnpt.vn/vi/idcheck]], và có nhiều phương án kiểm giả mạo với mức độ khắt khe khác nhau để chọn theo rủi ro [[ref:https://docs-vision.fpt.ai/en/ekyc/IV-guides/comparing%20liveness%20methods/]].

Ngưỡng nhóm chọn: **điểm so khớp khuôn mặt từ 0,90 và điểm chống giả mạo từ 0,90 thì tự động duyệt**. Đạt cả hai, hệ thống lưu số căn cước đã băm vào `kyc_profiles.id_number_hash` chứ không lưu số gốc, lưu vector khuôn mặt, rồi gửi mã một lần tới hộp thư `@fpt.edu.vn`. Khách nhập mã, hệ thống gắn mã số sinh viên và mở quyền đặt máy. Hai lớp danh tính độc lập chồng lên nhau, đúng khẩu quyết **cọc thấp và danh tính mạnh**.

Nhánh còn lại: dưới ngưỡng ở bất kỳ điểm nào, hoặc số căn cước trùng `blocklist.id_number_hash`, thì hồ sơ vào hàng chờ duyệt tay và khách nhận lời hứa trả lời trong 30 phút. Quản trị viên thấy hai ảnh, hai điểm số, và phải ghi lý do cho quyết định; nhân viên giao nhận không có quyền này. Ngưỡng 0,90 là **[Ước lượng của nhóm]** dựa trên thực tế các nhà cung cấp không công bố bảng ngưỡng, và phải hiệu chỉnh lại sau 100 hồ sơ đầu tiên: nếu tỉ lệ phải duyệt tay vượt 15% thì ngưỡng đang quá chặt và đang đốt thời gian người thật; nếu lọt một hồ sơ giả thì ngưỡng quá lỏng. Trong mọi trường hợp, ExamLap **không giữ căn cước hay thẻ sinh viên của khách**, chỉ giữ bản băm và bằng chứng đối chiếu.

## Luồng chuẩn bị và bàn giao máy

<<<landscape>>>

![Trình tự chuẩn bị và bàn giao: trước giờ thi sáu mươi phút nhân viên gán máy theo gợi ý và hoàn tất mười hai mục chuẩn bị, sau đó quét mã QR của khách, đối chiếu khuôn mặt, chụp sáu ảnh và lấy chữ ký điện tử.](assets/diagrams/07a-seq-ban-giao.png){w=0}{src: Nguồn: nhóm tác giả.}

<<<portrait>>>

Chặng chuẩn bị bắt đầu trước giờ thi 60 phút. Ứng dụng nhân viên mở danh sách đơn của ca, máy chủ trả về, ví dụ, 12 đơn kèm gợi ý gán máy xếp theo pin giảm dần rồi số lượt thuê tăng dần. Quy tắc xếp thứ hai là để cân bằng hao mòn giữa các máy, đúng cách các hệ thống cho thuê xe phân bổ đều tải sử dụng trên toàn đội [[ref:https://www.altexsoft.com/blog/car-rental-reservation-system/]]. Nhân viên xác nhận gán máy EL-T490-07, hệ thống bật theo dõi MDM, rồi nhân viên hoàn tất 12 mục chuẩn bị gồm chạy thử EOS, kiểm Safe Exam Browser, sạc pin và vệ sinh máy.

Chặng bàn giao diễn ra ở sảnh: khách xuất trình mã QR, nhân viên quét, máy chủ trả thông tin khách kèm ảnh chân dung đã xác minh, nhân viên đối chiếu mặt người với ảnh, chụp 6 ảnh hiện trạng, khách ký điện tử.

Điểm cốt lõi của cả chương nằm ở bước áp chót: **máy chủ chặn, chứ không phải giao diện ẩn nút**. Yêu cầu chuyển đơn sang Đang thuê bị từ chối nếu thiếu bất kỳ điều kiện nào trong sáu điều kiện sau, và mỗi lần từ chối đều ghi một dòng vào `audit_logs`:

1. `orders.device_id` chưa điền, hoặc máy được gán không ở trạng thái `held` của chính đơn này.
2. Số ảnh trong `handover_photos` chiều giao chưa đủ 6, hoặc có ảnh thiếu `sha256`.
3. Chưa có chữ ký điện tử của khách trên biên bản.
4. Ô đối chiếu khuôn mặt chưa được tích, hoặc hồ sơ eKYC chưa ở trạng thái đã xác minh.
5. Danh mục `handovers.checklist` chưa đủ 12 mục, hoặc `devices.seb_tested_at` cũ hơn 7 ngày.
6. Chưa có bản ghi `payments` chiều vào đủ tiền thuê cộng tiền cọc cho đơn.

Cùng cơ chế đó áp cho chiều ngược lại: chưa đủ 6 ảnh trả máy và chữ ký thì lệnh hoàn cọc không phát sinh được. Biên bản đã chốt không sửa được bởi bất kỳ vai nào, kể cả quản trị viên; muốn sửa thì lập biên bản đính chính mới, và cả hai bản cùng nằm trong hồ sơ. Đây là điều kiện để bộ ảnh có mã băm thực sự dùng được làm bằng chứng khi tranh chấp [[ref:https://www.locatorx.com/blog/the-truth-about-asset-records-why-immutability-is-the-foundation-of-a-verifiable-chain-of-custody]].

## Luồng trả máy và hoàn cọc

<<<landscape>>>

![Trình tự trả máy và hoàn cọc với hai nhánh: máy nguyên vẹn thì lệnh hoàn cọc ba trăm nghìn đồng chạy trong năm phút, còn có hư hỏng thì lập phiếu sự cố và gửi bảng kê khấu trừ kèm ảnh đối chiếu.](assets/diagrams/07b-seq-tra-may.png){w=0}{src: Nguồn: nhóm tác giả.}

<<<portrait>>>

Khách trả máy và xuất trình mã QR, nhân viên quét, chụp 6 ảnh sau khi thuê, gửi biên bản thu hồi. Máy chủ so ảnh trước với ảnh sau theo từng góc, đối chiếu danh sách phụ kiện, và tính phí trễ nếu giờ nhận thực tế vượt `exam_slots.return_due_at`.

**Nhánh máy nguyên vẹn và đúng giờ**: hệ thống dựng lệnh hoàn cọc 300.000đ, quản trị viên duyệt, tiền về tài khoản khách trong 5 phút đúng như cam kết công khai. Bản ghi `payments` chiều ra mang cùng `orders.code`, và ràng buộc "một đơn chỉ có một lần hoàn cọc thành công" được ép bằng chỉ mục duy nhất một phần chứ không bằng câu lệnh `if` trong mã. Khách nhận biên lai kèm lời mời đánh giá, điểm `users.trust_score` được cộng, và từ lượt thứ ba mức cọc hạ xuống 150.000đ, từ lượt thứ sáu không vi phạm thì về 0đ.

**Nhánh có hư hỏng hoặc thiếu phụ kiện**: hệ thống lập một dòng `incidents` với loại sự cố và số tiền khấu trừ lấy thẳng từ biểu phí công khai, gửi cho khách bảng kê kèm ảnh trước và sau đặt cạnh nhau, và mở cửa sổ khiếu nại 48 giờ. Quy tắc vận hành đi kèm là không tranh cãi tại quầy: nhân viên chỉ lập biên bản và chụp ảnh, báo giá từ tiệm sửa đối tác gửi trong 24 giờ. Khấu trừ vượt biểu phí công khai cần hai người duyệt, vì đó là chỗ dễ lạm quyền nhất trong toàn hệ thống.

Cả hai nhánh đều hợp lưu ở hai bước cuối: tắt theo dõi MDM và đưa máy về `awaiting_wipe`. Không nhánh nào được phép đưa máy thẳng về `ready`.

## Luồng xử lý quá hạn

<<<landscape>>>

![Trình tự xử lý đơn quá hạn với năm mốc leo thang: nhắc lần một ở mười lăm phút, nhắc lần hai kèm cảnh báo ở sáu mươi phút, khoá màn hình sau khi hai người duyệt, gọi điện và gửi văn bản ở hai mươi bốn giờ, kết xuất hồ sơ và trình báo ở bốn mươi tám giờ.](assets/diagrams/08-seq-qua-han.png){w=0}{src: Nguồn: nhóm tác giả.}

<<<portrait>>>

Một tác vụ nền chạy mỗi phút quét các đơn đã qua `return_due_at`. Thang leo thang có năm mốc, công bố trước trong hợp đồng để không ai bất ngờ.

| Mốc | Việc hệ thống làm | Ai quyết định |
|---|---|---|
| T+15 phút | Nhắc lần một qua Zalo và email, bắt đầu cộng phí trễ 20.000đ mỗi 30 phút | Tự động |
| T+60 phút | Nhắc lần hai kèm cảnh báo khoá máy, đẩy cảnh báo lên bảng điều khiển quản trị | Tự động |
| Sau T+60 phút | Khoá màn hình từ xa qua MDM, hiện thông tin liên hệ, **không xoá dữ liệu người dùng** | Hai người duyệt |
| T+24 giờ | Gọi điện, gửi văn bản nhắc nợ | Quản trị viên |
| T+48 giờ | Kết xuất hồ sơ PDF gồm hợp đồng, hai biên bản, 12 ảnh, nhật ký MDM; đơn sang Mất tài sản | Hai người duyệt |
{caption: Năm mốc leo thang khi đơn quá hạn, với hai điểm chốt bắt buộc có người thứ hai duyệt.}
{widths: 3,9,3}

Hai chi tiết cần nhấn mạnh. Thứ nhất, **lệnh khoá màn hình không bao giờ do một người phát ra**. Yêu cầu khoá ghi vào `lock_requests(requested_by, approved_by, reason)`, và máy chủ chỉ gọi API của MDM khi `approved_by` khác `requested_by` và cả hai đều có vai `admin`. Mỗi lệnh ghi một dòng vào nhật ký chỉ ghi thêm có nối chuỗi mã băm [[ref:https://tracehold.ai/blog/immutable-audit-log-hmac-hash-chain/]] [[ref:https://www.designgurus.io/answers/detail/how-do-you-enforce-immutability-and-appendonly-audit-trails]]. Đây vừa là kỷ luật nội bộ vừa là lá chắn pháp lý: khoá thiết bị của người khác là hành vi nhạy cảm, và hồ sơ chứng minh có quy trình duyệt là thứ cần có nếu sự việc đi xa. Nghịch lý có chủ ý: **gỡ khoá thì một người làm được, khoá thì không**.

Thứ hai, khoá màn hình chỉ chặn truy cập, **không xoá dữ liệu**. Bài làm và tài liệu cá nhân của khách vẫn còn nguyên trên máy. Đây là ranh giới nhóm không vượt qua kể cả khi khách đang chiếm giữ tài sản.

Tới mốc 48 giờ, hồ sơ đủ để trình báo theo *Điều 175 Bộ luật Hình sự 2015* về lạm dụng tín nhiệm chiếm đoạt tài sản. Thang thời gian này là **[Ước lượng của nhóm]** hiệu chỉnh cho vòng quay theo ca thi, ngắn hơn thông lệ cho thuê dài ngày vì một máy bị giữ quá 48 giờ trong tuần thi là mất luôn cả chục lượt thuê.

## Các quy tắc nghiệp vụ bất biến

Mười bốn mệnh đề dưới đây phải đúng ở **mọi thời điểm**, kể cả giữa hai giao dịch, kể cả khi có người sửa tay trong cơ sở dữ liệu. Mỗi mệnh đề viết dưới dạng kiểm tra được, kèm nơi ép và câu lệnh dùng để kiểm.

| # | Mệnh đề phải luôn đúng | Ép ở đâu | Cách kiểm |
|---|---|---|---|
| R01 | Một máy không nằm trong hai suất giữ chồng khung giờ | `EXCLUDE USING gist (device_id WITH =, period WITH &&) WHERE status <> 'cancelled'` | Cố chèn hai dòng chồng nhau, phải nhận mã `23P01` |
| R02 | Một máy không nằm trong hai đơn đang hoạt động cùng lúc | Chỉ mục duy nhất một phần trên `orders(device_id)` với `status IN ('device_assigned','renting','overdue')` | `SELECT device_id FROM orders WHERE ... GROUP BY 1 HAVING count(*) > 1` phải rỗng |
| R03 | Tổng suất giữ chưa hết hạn cộng đơn đã xác nhận không vượt số máy `ready` của kiểu máy đó trong ca thi đó | Giao dịch có `FOR UPDATE SKIP LOCKED`, cộng R01 làm lưới cuối | So `count(holds)` với `count(devices)` theo từng cặp kiểu máy và ca thi |
| R04 | Không thể hoàn cọc hai lần cho một đơn | Chỉ mục duy nhất một phần trên `payments(order_id)` với `direction = 'out' AND status = 'succeeded'` | Gọi lệnh hoàn cọc hai lần, lần hai phải bị từ chối |
| R05 | Không thể chuyển sang Đang thuê nếu thiếu ảnh hoặc chữ ký | Sáu điều kiện chặn ở máy chủ, kiểm lại bằng trigger đếm `handover_photos` | Gửi biên bản thiếu một ảnh, phải nhận `422` |
| R06 | Một đơn chỉ có một dòng `payments` chiều vào ứng với mỗi `provider_txn_id` | `UNIQUE (provider, provider_txn_id)` | Gửi lại cùng một webhook 10 lần, số dòng không đổi |
| R07 | Không có đường từ `awaiting_wipe` sang `ready` | Bảng `device_state_transitions` cộng trigger | Cố `UPDATE`, trigger phải ném lỗi |
| R08 | Mọi lần chuyển trạng thái đơn đều có đúng một dòng trong `order_state_log` | Ghi trong cùng giao dịch với thay đổi trạng thái | Đối chiếu số lần chuyển với số dòng log |
| R09 | Không dòng nào trong `audit_logs` bị sửa hoặc xoá | `REVOKE UPDATE, DELETE` cộng trigger `BEFORE UPDATE/DELETE` | Chạy kiểm chuỗi băm hằng đêm, mọi `prev_hash` phải khớp `row_hash` dòng trước |
| R10 | Lệnh khoá máy luôn có hai người khác nhau | `CHECK (approved_by IS NOT NULL AND approved_by <> requested_by)` | Cố duyệt lệnh do chính mình tạo, phải bị chặn |
| R11 | Không tài khoản nào đặt được máy khi hồ sơ eKYC chưa ở trạng thái đã xác minh | Lớp kiểm quyền trên `POST /api/holds` cộng khoá ngoại tới `kyc_profiles` | Gọi API bằng tài khoản chưa xác minh, phải nhận `403` |
| R12 | Số căn cước gốc không tồn tại ở bất kỳ bảng nào, chỉ có bản băm | Lược đồ không có cột số gốc; bộ lọc nhật ký bỏ mọi trường tên chứa `id_number` | Quét toàn bộ kết xuất `pg_dump` bằng biểu thức chính quy số căn cước, kết quả phải rỗng |
| R13 | Suất giữ hết hạn không bao giờ bị xoá, chỉ đổi cờ sang `cancelled` | Tác vụ nền chỉ chạy `UPDATE`, vai ứng dụng không có quyền `DELETE` trên bảng này | Đếm số dòng trước và sau khi tác vụ dọn dẹp chạy |
| R14 | Đơn ở trạng thái Đóng không đổi được nữa | Trigger chặn mọi `UPDATE` khi `OLD.status = 'closed'` | Cố mở lại một đơn đã đóng, phải ném lỗi |
{caption: Mười bốn quy tắc bất biến của hệ thống, mỗi quy tắc kèm nơi ép và cách kiểm chứng.}
{widths: 1,7,6,6}
{note: Mười bốn quy tắc này là mười bốn ca kiểm thử tự động chạy trong quy trình dựng, không phải mười bốn dòng ghi chú trong tài liệu.}

:::ok Nguyên tắc chung của cả chương
Mỗi quy tắc nghiệp vụ quan trọng được ép ở **tầng thấp nhất có thể ép được**. Ràng buộc cấp cơ sở dữ liệu tốt hơn trigger, trigger tốt hơn kiểm tra trong mã máy chủ, kiểm tra trong mã máy chủ tốt hơn việc ẩn nút trên giao diện. Lý do rất thực tế: đội lập trình là bốn đến năm sinh viên làm ngoài giờ, và thứ duy nhất chắc chắn đúng sau sáu tháng thay người là thứ mà chính máy chủ dữ liệu từ chối vi phạm.
:::
