## Ba bề mặt sử dụng, một mã nguồn duy nhất

**Web cho sinh viên** chạy trên trình duyệt điện thoại: chọn ca thi, xác minh danh tính, trả tiền, theo dõi đơn. Từ vựng giao diện mượn của hệ thống "ĐK Mượn máy" mà sinh viên Đại học FPT đã quen: **Dashboard**, **ĐK thuê máy**, **Trả máy** [[ref:https://it-hcm.fpt.edu.vn/articles.php?news=huong-dan-muon-laptop-cua-sinh-vien-trong-truong&id=56]].

**Ứng dụng cho nhân viên giao nhận** là một ứng dụng web tiến bộ (PWA) cài lên màn hình chính điện thoại. Nhân viên có mười lăm phút để bàn giao cả chục máy nên chỉ còn ba thao tác: quét mã QR, chụp sáu ảnh, lấy chữ ký. Ảnh lưu tạm bằng IndexedDB rồi tự đẩy lên sau.

**Bảng điều khiển quản trị** chạy trên máy tính: lịch ngang máy nhân ca, hồ sơ thiết bị, cấu hình giá, báo cáo, nhật ký kiểm toán, theo đặc tả Booqable [[ref:https://booqable.com/features/]].

Ba bề mặt nhưng **một mã nguồn, một cơ sở dữ liệu, một bảng phân quyền**. Ba dự án riêng là ba bản sao của luật chuyển trạng thái, sớm muộn sẽ lệch nhau. Việc giữ chỗ một máy trong một khung giờ lại phải nằm gọn trong một giao dịch thì ràng buộc chống trùng lịch mới có tác dụng. Snipe-IT cũng chỉ là một ứng dụng Laravel phục vụ cả quản trị lẫn API [[ref:https://github.com/grokability/snipe-it]].

```php
// routes/web.php — tách bằng tiền tố và kiểm quyền
Route::middleware(['auth','verified.kyc'])->group(base_path('routes/student.php'));
Route::prefix('staff')->middleware(['auth','role:staff'])->group(base_path('routes/staff.php'));
Route::prefix('admin')->middleware(['auth','role:admin','twofactor'])->group(base_path('routes/admin.php'));
```
{caption: Ba bề mặt, một tầng nghiệp vụ.}

<<<landscape>>>

![Ba nhóm người dùng, một tầng ứng dụng, một cơ sở dữ liệu.](assets/diagrams/04-kien-truc.png){w=24}{src: Nguồn: nhóm tác giả.}

<<<portrait>>>

## Danh sách chức năng theo mức ưu tiên

SV: sinh viên. NV: nhân viên giao nhận. QT: quản trị viên. HT: tác vụ tự động.

| Mã | Chức năng | Vai trò | Ưu tiên | Ghi chú kỹ thuật |
|---|---|---|---|---|
| F01 | Đăng ký bằng email `@fpt.edu.vn` và mã sinh viên | SV | Bắt buộc | `users.email_fpt` duy nhất, danh tính trường thay giấy tờ [[ref:https://www.grover.com/us-en/how-it-works]] |
| F02 | Đăng nhập, hai lớp cho quản trị | SV·NV·QT | Bắt buộc | Quản trị khoá được máy khách |
| F03 | Xác minh CCCD kèm video người sống | SV·QT | Bắt buộc | `POST /api/kyc/submit`, duyệt tay khi điểm so khớp khuôn mặt trong khoảng 0,55 đến 0,68 (ngưỡng ở Chương 6) |
| F04 | Tra máy trống theo ca thi | SV | Bắt buộc | `GET /api/availability?slot_id=&model_id=` |
| F05 | Danh sách máy kèm ngày test EOS, SEB | SV | Bắt buộc | `devices.seb_tested_at` |
| F06 | Giữ chỗ có hạn mười phút | SV | Bắt buộc | `POST /api/holds`, `inventory_holds.expires_at`, dọn dẹp đổi cờ |
| F07 | Tạo đơn và sinh mã VietQR động | SV | Bắt buộc | `POST /api/orders` kèm `Idempotency-Key`, mẫu Stripe [[ref:https://stripe.com/blog/idempotency]] [[ref:https://brandur.org/idempotency-keys]] |
| F08 | Nhận báo tiền về, kiểm chữ ký | HT | Bắt buộc | `POST /webhooks/payment`, `payments.provider_txn_id` duy nhất |
| F09 | Đối soát tay giao dịch sai nội dung | QT | Bắt buộc | Chuyển khoản tay hay ghi sai nội dung |
| F10 | Ký hợp đồng, ô tích riêng khối loại trừ | SV | Bắt buộc | Bài học vụ Getaround [[ref:https://oag.dc.gov/release/attorney-general-schwalb-secures-refunds-dc]] |
| F11 | Gán máy cụ thể, ưu tiên máy pin cao | NV·QT | Bắt buộc | `orders.device_id` điền trễ nhất, mẫu Koha [[ref:https://raw.githubusercontent.com/Koha-Community/Koha/master/installer/data/mysql/kohastructure.sql]] |
| F12 | Biên bản bàn giao: sáu ảnh và chữ ký | NV·SV | Bắt buộc | `handovers.checklist`, `handover_photos(angle, url, sha256)` [[ref:https://github.com/grokability/snipe-it/blob/master/database/migrations/2018_07_28_023826_create_checkout_acceptances_table.php]] |
| F13 | Biên bản thu hồi, so ảnh trước và sau | NV | Bắt buộc | Tách hao mòn với hư hỏng [[ref:https://www.grover.com/at-en/g-about/asset-condition]] |
| F14 | Hoàn cọc khi máy nguyên vẹn | HT·QT | Bắt buộc | Quản trị duyệt lệnh dựng sẵn |
| F15 | Phiếu sự cố, khiếu nại 48 giờ | NV·SV·QT | Bắt buộc | `incidents(type, deduction_amount, status)` [[ref:https://www.trustpilot.com/review/fatllama.com]] |
| F16 | Quản lý kho theo mã tài sản, sê-ri | QT | Bắt buộc | `devices(asset_tag UK, serial UK, status, battery_health_pct, mdm_device_id)` |
| F17 | Lịch ngang máy nhân ca, ô màu trạng thái | QT | Bắt buộc | Màn hình điều phối của người trực |
| F18 | Nhật ký bảo trì, cảnh báo pin dưới 80% | QT | Nên có | `maintenance_logs(type, cost)` |
| F19 | Cấu hình giá theo nhóm máy và gói | QT | Bắt buộc | `pricing_rules(model_id, slot_type, price, deposit, valid_from)` |
| F20 | Điểm tín nhiệm và bậc cọc tự động | HT | Nên có | `users.trust_score`, cọc theo hồ sơ rủi ro [[ref:https://help.turo.com/en_us/security-deposits-us-HkbE44lE9]] |
| F21 | Danh sách chặn theo số CCCD đã băm | QT | Bắt buộc | `blocklist(id_number_hash, reason)` |
| F22 | Nhắc hạn và cảnh báo quá hạn | HT·QT | Bắt buộc | `outbox_messages`, mốc T-12h, T-2h, T+15 phút |
| F23 | Khoá màn hình qua MDM, hai người duyệt | QT | Nên có | `lock_requests(requested_by, approved_by, reason)`. Năm thao tác cần hai người duyệt được liệt kê thống nhất ở Chương 5 và Chương 7 |
| F24 | Báo cáo khai thác, doanh thu, sự cố | QT | Nên có | Đầu vào chương tài chính |
| F25 | Nhật ký kiểm toán chỉ ghi thêm, nối băm | HT | Bắt buộc | `audit_logs` có trigger chặn `UPDATE`, `DELETE` [[ref:https://www.locatorx.com/blog/the-truth-about-asset-records-why-immutability-is-the-foundation-of-a-verifiable-chain-of-custody]] |
| F26 | Kết xuất hồ sơ một đơn ra PDF | QT | Bắt buộc | Chứng cứ trình báo theo Điều 175 Bộ luật Hình sự 2015 *[Cần kiểm chứng, xem Chương 17]* |
| F27 | Xuất CSV, sinh viên tự tải hồ sơ | SV·QT | Nên có | Kế toán và quyền tiếp cận dữ liệu |
| F28 | Xoá theo yêu cầu, ảnh eKYC sau 90 ngày | HT·QT | Bắt buộc | `kyc_profiles.images_purge_at` |
| F29 | Đánh giá sau lượt thuê | SV | Để sau | Chưa đủ lượt để trung bình có nghĩa |
| F30 | Báo khi ca kín có chỗ trống lại | SV | Để sau | Khai thác năm đầu mới khoảng 42% |
{caption: Ba mươi chức năng của hệ thống.}
{widths: 1,5,2,2,6}
{note: Hai mươi ba bắt buộc, năm nên có, hai để sau.}

## Ranh giới của bản chạy được đầu tiên

| Không làm ở bản đầu | Làm thay bằng | Vì sao, và khi nào mở khoá |
|---|---|---|
| Ứng dụng di động riêng | Web đáp ứng, PWA cho nhân viên | Hai quy trình duyệt mà gần như không thêm chức năng. Mở khoá khi cần phần cứng trình duyệt không cho |
| Hoàn cọc tự động qua cổng | Quản trị duyệt lệnh chuyển khoản trong 5 phút | Chưa rõ hạ tầng thanh toán Việt Nam có cơ chế tương đương [[ref:https://help.turo.com/en_us/security-deposits-us-HkbE44lE9]] |
| Tích hợp hệ thống nhà trường | Chỉ kiểm tên miền email và mã sinh viên | Chưa xác nhận được nhà trường có cho mang máy thuê vào phòng thi [[ref:https://daihoc.fpt.edu.vn/tin-noi-bat-muc-tin-tuc/huong-dan-sinh-vien-su-dung-va-thi-tren-phan-mem-eos-tai-truong-dai-hoc-fpt/]]. Mở khoá khi có văn bản của Phòng Khảo thí |
| Nhiều điểm nhận máy | Một điểm hẹn cố định ghi trên đơn | Chia mười máy ra nhiều điểm thì không điểm nào đủ tồn kho. Mở khoá khi vượt mười sáu máy |
| Gợi ý bằng học máy | Quy tắc thẳng: pin cao nhất, rồi máy ít lượt nhất | Vài trăm lượt năm đầu không đủ cho mô hình học, quy tắc tường minh lại giải thích được |
{caption: Năm hạng mục ngoài phạm vi.}
{widths: 4,4,9}

:::warn Một ranh giới nữa
Bảng `checkout_requests` của Snipe-IT không có ngày bắt đầu và kết thúc: nó quản lý "ai đang giữ", không phải "ai sẽ giữ, từ khi nào" [[ref:https://github.com/grokability/snipe-it/blob/master/database/migrations/2016_09_02_001448_create_checkout_requests_table.php]]. Snipe-IT lại theo AGPL, sửa mã rồi chạy thành dịch vụ công khai là phải công bố [[ref:https://snipeitapp.com/faq]]. Nhóm học mô hình dữ liệu, không fork mã.
:::

## Câu chuyện người dùng theo từng vai trò

| Mã | Là sinh viên, tôi muốn… | …để… | Tiêu chí chấp nhận |
|---|---|---|---|
| U-SV-1 | xem ca nào còn máy ngay lần chạm đầu | biết nên đặt hay đi chỗ khác | Không cần đăng nhập, hiện xong dưới 2,5 giây |
| U-SV-2 | giữ chỗ trong lúc đi chuyển khoản | khỏi mất suất giữa chừng | Đếm ngược 10 phút, hết giờ suất tự về kho |
| U-SV-3 | xác minh một lần, lần sau đi thẳng | khỏi chụp lại giấy tờ | Lượt thứ hai trở đi không quá 4 bước |
| U-SV-4 | biết trường hợp nào phải đền bao nhiêu | khỏi bất ngờ khi trả máy | Chưa tích ô loại trừ thì nút xác nhận tắt |
| U-SV-5 | được nhắc trước hạn trả máy | khỏi bị tính phí trễ | Ba tin đúng mốc, ghi giờ hạn và phí trễ |
| U-SV-6 | thấy tiền cọc về sau khi trả máy | yên tâm thuê lần sau | Từ chốt biên bản thu hồi tới duyệt hoàn cọc dưới 5 phút |
{caption: Câu chuyện của sinh viên.}
{widths: 2,4,4,6}

| Mã | Là nhân viên giao nhận, tôi muốn… | …để… | Tiêu chí chấp nhận |
|---|---|---|---|
| U-NV-1 | danh sách đơn ca sắp tới xếp theo giờ giao | khỏi tra từng đơn | Mỗi dòng có nút quét QR mở thẳng biên bản |
| U-NV-2 | được gợi ý máy nào gán cho đơn nào | khỏi tự nhớ pin máy nào | Xếp theo pin giảm dần rồi số lượt tăng dần, đổi tay ghi lý do |
| U-NV-3 | chụp sáu ảnh và ký trên điện thoại | có bằng chứng khi tranh chấp | Thiếu ảnh hoặc chữ ký thì nút gửi khoá, ảnh kèm mã băm SHA-256 |
| U-NV-4 | đối chiếu mặt người với ảnh xác minh | khỏi giao nhầm máy | Quét QR xong hiện ảnh chân dung, phải tích xác nhận |
| U-NV-5 | làm việc được cả khi sóng yếu | khỏi để khách phải chờ | Biên bản lưu tạm rồi tự đẩy, hiện số bản còn chờ |
{caption: Câu chuyện của nhân viên.}
{widths: 2,4,4,6}

| Mã | Là quản trị viên, tôi muốn… | …để… | Tiêu chí chấp nhận |
|---|---|---|---|
| U-QT-1 | lịch ngang thấy máy nào rảnh ca nào | điều phối giờ cao điểm | Ô phân biệt màu: trống, đã đặt, đang thuê, bảo trì |
| U-QT-2 | duyệt tay hồ sơ bị đánh dấu | khỏi kẹt khách thật | Hiện ảnh và hai điểm số, quyết định kèm lý do |
| U-QT-3 | đổi giá không động tới đơn đã chốt | khỏi giải thích tiền đổi | Giá mới có ngày hiệu lực, đơn cũ giữ giá cũ |
| U-QT-4 | khoá máy quá hạn nhưng không tự quyết | tránh lạm quyền | Chỉ chạy khi người thứ hai duyệt, lý do vào nhật ký |
| U-QT-5 | xem tỉ lệ khai thác theo tuần | biết khi nào mua thêm | Số ca đã bán chia số ca khả dụng |
| U-QT-6 | kết xuất trọn hồ sơ một đơn | có đủ chứng cứ một lần bấm | PDF gồm hợp đồng, hai biên bản, mười hai ảnh, nhật ký |
{caption: Câu chuyện của quản trị viên.}
{widths: 2,4,4,6}

## Bảng phân quyền

**Có** là được phép, **Hai người** là phải có người thứ hai duyệt, **Không** là chặn ở máy chủ, không chỉ ẩn nút.

| Thao tác | Sinh viên | Nhân viên | Quản trị |
|---|---|---|---|
| Đặt đơn và giữ chỗ cho chính mình | Có | Không | Có |
| Xem hồ sơ xác minh của người khác | Không | Không | Có |
| Duyệt hồ sơ xác minh | Không | Không | Có |
| Gán máy cụ thể cho đơn | Không | Có | Có |
| Lập biên bản bàn giao, thu hồi | Không | Có | Có |
| Lập phiếu sự cố theo biểu phí | Không | Có | Có |
| Sửa biên bản đã ký | Không | Không | Không |
| Khấu trừ vượt biểu phí | Không | Không | Hai người |
| Hoàn cọc trong hạn mức 300.000đ | Không | Không | Có |
| Sửa bảng giá và mức cọc | Không | Không | Có |
| Thêm, sửa, ngừng dùng máy | Không | Không | Có |
| Khoá màn hình máy từ xa | Không | Không | Hai người |
| Thêm vào danh sách chặn | Không | Không | Hai người |
| Kết xuất hồ sơ đơn | Đơn của mình | Không | Có |
| Xoá dữ liệu theo yêu cầu | Gửi yêu cầu | Không | Hai người |
| Sửa, xoá nhật ký kiểm toán | Không | Không | Không |
{caption: Ma trận phân quyền.}
{widths: 7,3,3,3}
{note: Nhân viên chỉ thấy ảnh chân dung khách lúc bàn giao. Gỡ khoá thì một người làm được, khoá thì không. Thao tác "Hai người" ghi cả người yêu cầu lẫn người duyệt.}

:::ok Kết luận của chương
Hai mươi ba chức năng bắt buộc vừa đủ cho trọn một vòng đời đơn thuê: đặt được, xác minh được, bàn giao có bằng chứng, thu hồi có đối chiếu, hoàn cọc có dấu vết. Chưa website cho thuê laptop nào ở Việt Nam làm được như vậy [[ref:https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html]].
:::
