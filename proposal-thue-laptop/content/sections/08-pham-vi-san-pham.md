## Ba bề mặt sử dụng, một mã nguồn duy nhất

**Web cho sinh viên** chạy trên trình duyệt điện thoại: chọn ca thi, xác minh danh tính, trả tiền, theo dõi đơn. Từ vựng giao diện mượn nguyên hệ thống "ĐK Mượn máy" mà sinh viên Đại học FPT đã dùng sẵn, gồm **Dashboard**, **ĐK thuê máy** và **Trả máy** [[ref:https://it-hcm.fpt.edu.vn/articles.php?news=huong-dan-muon-laptop-cua-sinh-vien-trong-truong&id=56]], nên chi phí học của người dùng gần bằng không.

**Ứng dụng cho nhân viên giao nhận** là một ứng dụng web tiến bộ (PWA) cài lên màn hình chính điện thoại. Nhân viên có mười lăm phút để bàn giao cả chục máy, nên bề mặt này chỉ còn ba thao tác: quét mã QR đơn, chụp sáu ảnh hiện trạng, lấy chữ ký. Ảnh lưu tạm bằng IndexedDB rồi tự đẩy lên khi có mạng.

**Bảng điều khiển quản trị** chạy trên máy tính: lịch ngang máy nhân ca thi, hồ sơ thiết bị, cấu hình giá, báo cáo, nhật ký kiểm toán. Cấu trúc lấy theo đặc tả của Booqable, phần mềm cho thuê thiết bị quản lý theo mã vạch từng cá thể [[ref:https://booqable.com/features/]].

Ba bề mặt nhưng **một mã nguồn, một cơ sở dữ liệu, một bảng phân quyền**. Cả ba cùng thao tác trên một máy trạng thái đơn thuê, tách thành ba dự án là ba bản sao của luật chuyển trạng thái và sớm muộn chúng lệch nhau. Thao tác quan trọng nhất, giữ chỗ một máy trong một khung giờ, phải nằm gọn trong một giao dịch cơ sở dữ liệu thì ràng buộc chống trùng lịch mới có tác dụng. Snipe-IT cũng làm vậy: một ứng dụng Laravel duy nhất phục vụ cả giao diện quản trị lẫn API [[ref:https://github.com/grokability/snipe-it]].

```php
// routes/web.php — tách bằng tiền tố và lớp kiểm quyền, không phải bằng ba dự án
Route::middleware(['auth','verified.kyc'])->group(base_path('routes/student.php'));
Route::prefix('staff')->middleware(['auth','role:staff'])->group(base_path('routes/staff.php'));
Route::prefix('admin')->middleware(['auth','role:admin','twofactor'])->group(base_path('routes/admin.php'));
```
{caption: Ba bề mặt dùng chung một tầng nghiệp vụ.}

<<<landscape>>>

![Ba nhóm người dùng dùng chung một tầng ứng dụng và một cơ sở dữ liệu.](assets/diagrams/04-kien-truc.png){w=24}{src: Nguồn: nhóm tác giả.}

<<<portrait>>>

## Danh sách chức năng theo mức ưu tiên

Vai trò viết tắt: SV là sinh viên, NV là nhân viên giao nhận, QT là quản trị viên, HT là tác vụ tự động.

| Mã | Chức năng | Vai trò | Ưu tiên | Ghi chú kỹ thuật |
|---|---|---|---|---|
| F01 | Đăng ký bằng email `@fpt.edu.vn` và mã số sinh viên | SV | Bắt buộc | `users.email_fpt` duy nhất; danh tính trường thay giấy tờ [[ref:https://www.grover.com/us-en/how-it-works]] |
| F02 | Đăng nhập, hai lớp cho tài khoản quản trị | SV·NV·QT | Bắt buộc | Quản trị khoá được máy nên không dùng mật khẩu đơn |
| F03 | Xác minh CCCD kèm video người sống, có hàng chờ duyệt tay | SV·QT | Bắt buộc | `POST /api/kyc/submit`; duyệt tay khi điểm so khớp dưới 0,90 |
| F04 | Tra máy trống theo ca thi | SV | Bắt buộc | `GET /api/availability?slot_id=&model_id=` |
| F05 | Danh sách máy nhóm A, B, C kèm ngày test EOS và SEB | SV | Bắt buộc | Cột `devices.seb_tested_at` |
| F06 | Giữ chỗ có hạn mười phút | SV | Bắt buộc | `POST /api/holds`; `inventory_holds.expires_at`; dọn dẹp chỉ đổi cờ |
| F07 | Tạo đơn, sinh mã VietQR động, trả về mã QR nhận máy | SV | Bắt buộc | `POST /api/orders` kèm `Idempotency-Key`, chuẩn Stripe [[ref:https://stripe.com/blog/idempotency]] [[ref:https://brandur.org/idempotency-keys]] |
| F08 | Nhận thông báo tiền về, kiểm chữ ký, khử trùng lặp | HT | Bắt buộc | `POST /webhooks/payment`; `payments.provider_txn_id` duy nhất |
| F09 | Đối soát tay giao dịch lệch tiền hoặc sai nội dung | QT | Bắt buộc | Chuyển khoản tay luôn có tỉ lệ ghi sai nội dung |
| F10 | Ký hợp đồng điện tử, ô tích riêng cho khối không miễn trừ | SV | Bắt buộc | Hai ô tích tách rời, bài học vụ Getaround [[ref:https://oag.dc.gov/release/attorney-general-schwalb-secures-refunds-dc]] |
| F11 | Gán máy cụ thể cho đơn, gợi ý ưu tiên pin cao | NV·QT | Bắt buộc | `orders.device_id` điền trễ nhất có thể, mẫu Koha [[ref:https://raw.githubusercontent.com/Koha-Community/Koha/master/installer/data/mysql/kohastructure.sql]] |
| F12 | Biên bản bàn giao: mười hai bước kiểm, sáu ảnh, chữ ký hai bên | NV·SV | Bắt buộc | `handovers.checklist`, `handover_photos(angle, url, sha256)` [[ref:https://github.com/grokability/snipe-it/blob/master/database/migrations/2018_07_28_023826_create_checkout_acceptances_table.php]] |
| F13 | Biên bản thu hồi, ảnh trước và sau đặt cạnh nhau | NV | Bắt buộc | Tách hao mòn thường với hư hỏng có phí [[ref:https://www.grover.com/at-en/g-about/asset-condition]] |
| F14 | Hoàn cọc sau khi kết luận máy nguyên vẹn | HT·QT | Bắt buộc | Bán tự động, quản trị duyệt lệnh chuyển khoản đã dựng sẵn |
| F15 | Phiếu sự cố theo biểu phí, khách khiếu nại trong 48 giờ | NV·SV·QT | Bắt buộc | `incidents(type, deduction_amount, status)`, không gõ số tự do [[ref:https://www.trustpilot.com/review/fatllama.com]] |
| F16 | Quản lý kho máy theo mã tài sản và số sê-ri | QT | Bắt buộc | `devices(asset_tag UK, serial UK, status, battery_health_pct, mdm_device_id)` |
| F17 | Lịch ngang máy nhân ca thi, ô màu theo trạng thái | QT | Bắt buộc | Màn hình điều phối chính của người trực ca |
| F18 | Nhật ký bảo trì, cảnh báo pin dưới 80% | QT | Nên có | `maintenance_logs(type, cost)` |
| F19 | Cấu hình giá theo nhóm máy và loại gói | QT | Bắt buộc | `pricing_rules(model_id, slot_type, price, deposit, valid_from)` |
| F20 | Điểm tín nhiệm và bậc cọc tự động | HT | Nên có | `users.trust_score`, cọc theo hồ sơ rủi ro [[ref:https://help.turo.com/en_us/security-deposits-us-HkbE44lE9]] |
| F21 | Danh sách chặn nội bộ theo số CCCD đã băm | QT | Bắt buộc | `blocklist(id_number_hash, reason)`, không giữ số thật |
| F22 | Nhắc hạn và cảnh báo quá hạn kèm bộ đếm phí trễ | HT·QT | Bắt buộc | `outbox_messages`; mốc trước 12 giờ, trước 2 giờ, sau hạn 15 phút |
| F23 | Khoá màn hình từ xa qua MDM, hai người duyệt | QT | Nên có | `lock_requests(requested_by, approved_by, reason)` |
| F24 | Báo cáo khai thác, doanh thu theo gói, tỉ lệ sự cố | QT | Nên có | Đầu vào cho chương tài chính |
| F25 | Nhật ký kiểm toán chỉ ghi thêm, nối chuỗi băm | HT | Bắt buộc | `audit_logs` có trigger chặn `UPDATE` và `DELETE` [[ref:https://www.locatorx.com/blog/the-truth-about-asset-records-why-immutability-is-the-foundation-of-a-verifiable-chain-of-custody]] |
| F26 | Kết xuất hồ sơ một đơn ra PDF | QT | Bắt buộc | Chứng cứ khi trình báo theo Điều 175 Bộ luật Hình sự 2015 |
| F27 | Xuất dữ liệu ra CSV, sinh viên tự tải hồ sơ của mình | SV·QT | Nên có | Kế toán và quyền tiếp cận dữ liệu cá nhân |
| F28 | Xoá dữ liệu theo yêu cầu, tự xoá ảnh eKYC sau 90 ngày | HT·QT | Bắt buộc | `kyc_profiles.images_purge_at` |
| F29 | Đánh giá sau lượt thuê | SV | Để sau | Chưa đủ lượt để điểm trung bình có ý nghĩa |
| F30 | Báo khi ca thi đã kín có chỗ trống trở lại | SV | Để sau | Năm đầu khai thác bình quân mới khoảng 42% |
{caption: Ba mươi chức năng, phân theo vai trò và mức ưu tiên.}
{widths: 1,5,2,2,6}
{note: Hai mươi ba chức năng bắt buộc, năm nên có, hai để sau.}

## Ranh giới của bản chạy được đầu tiên

| Không làm ở bản đầu | Làm thay bằng | Vì sao, và khi nào mở khoá |
|---|---|---|
| Ứng dụng di động riêng | Web đáp ứng, PWA cho nhân viên | Hai kho ứng dụng là hai quy trình duyệt và hai chu kỳ phát hành, gần như không thêm chức năng. Mở khoá khi cần phần cứng trình duyệt không cho dùng |
| Hoàn cọc tự động qua cổng | Quản trị duyệt lệnh chuyển khoản trong 5 phút | Cơ chế giữ tiền trên thẻ rồi tự hoàn chưa xác minh được là có tương đương ở Việt Nam [[ref:https://help.turo.com/en_us/security-deposits-us-HkbE44lE9]] |
| Tích hợp hệ thống nhà trường | Sinh viên tự chọn ca, chỉ kiểm tên miền email | Nhóm chưa xác nhận được nhà trường có cho mang máy thuê vào phòng thi hay không [[ref:https://daihoc.fpt.edu.vn/tin-noi-bat-muc-tin-tuc/huong-dan-sinh-vien-su-dung-va-thi-tren-phan-mem-eos-tai-truong-dai-hoc-fpt/]]. Mở khoá khi có văn bản của Phòng Khảo thí |
| Nhiều điểm nhận máy | Một điểm hẹn cố định ghi trên đơn | Mười máy chia nhiều điểm thì mỗi điểm không đủ tồn kho. Mở khoá khi đội máy vượt mười sáu máy |
| Gợi ý bằng học máy | Quy tắc thẳng: pin cao nhất, rồi máy ít lượt nhất | Vài trăm lượt năm đầu không đủ cho mô hình học, còn quy tắc tường minh thì giải thích được cho khách |
{caption: Năm hạng mục cố ý để ngoài phạm vi bản đầu.}
{widths: 4,4,9}

:::warn Một ranh giới nữa
Bảng `checkout_requests` của Snipe-IT không có ngày bắt đầu và ngày kết thúc, nên nó quản lý "ai đang giữ" chứ không phải "ai sẽ giữ, từ lúc nào tới lúc nào" [[ref:https://github.com/grokability/snipe-it/blob/master/database/migrations/2016_09_02_001448_create_checkout_requests_table.php]]. Snipe-IT lại theo giấy phép AGPL, sửa mã rồi chạy thành dịch vụ công khai sẽ kéo theo nghĩa vụ công bố phần đã sửa [[ref:https://snipeitapp.com/faq]]. Nhóm học mô hình dữ liệu, không fork mã nguồn.
:::

## Câu chuyện người dùng theo từng vai trò

| Mã | Là sinh viên, tôi muốn… | …để… | Tiêu chí chấp nhận |
|---|---|---|---|
| U-SV-1 | xem ca nào còn máy ngay lần chạm đầu | biết nên tiếp tục hay đi hỏi chỗ khác | Không cần đăng nhập, hiện xong dưới 2,5 giây trên 4G |
| U-SV-2 | giữ chỗ trong lúc đi chuyển khoản | không mất suất giữa chừng | Đếm ngược 10 phút, hết giờ thì suất tự về kho |
| U-SV-3 | xác minh một lần rồi lần sau đi thẳng | khỏi chụp lại giấy tờ mỗi kỳ | Lượt thứ hai trở đi từ chọn ca tới xác nhận không quá 4 bước |
| U-SV-4 | biết trường hợp nào phải đền bao nhiêu | không bất ngờ lúc trả máy | Chưa tích ô khối không miễn trừ thì nút xác nhận không bật |
| U-SV-5 | được nhắc trước hạn trả máy | không bị tính phí trễ vì quên | Ba tin đúng mốc, mỗi tin ghi giờ hạn và mức phí trễ |
| U-SV-6 | thấy tiền cọc về ngay sau khi trả máy | yên tâm thuê lần sau | Từ lúc chốt biên bản thu hồi tới lúc duyệt hoàn cọc không quá 5 phút |
{caption: Sáu câu chuyện của vai trò sinh viên.}
{widths: 2,4,4,6}

| Mã | Là nhân viên giao nhận, tôi muốn… | …để… | Tiêu chí chấp nhận |
|---|---|---|---|
| U-NV-1 | một danh sách đơn của ca sắp tới xếp theo giờ giao | khỏi tra từng đơn | Mỗi dòng có nút quét mã QR mở thẳng biên bản bàn giao |
| U-NV-2 | được gợi ý máy nào gán cho đơn nào | khỏi tự nhớ máy nào pin tốt | Xếp theo pin giảm dần rồi số lượt tăng dần, đổi tay thì ghi lý do |
| U-NV-3 | chụp sáu ảnh và lấy chữ ký trên điện thoại | có bằng chứng khi tranh chấp | Thiếu ảnh hoặc chữ ký thì nút gửi bị khoá, mỗi ảnh kèm mã băm SHA-256 |
| U-NV-4 | đối chiếu mặt người với ảnh đã xác minh | không giao nhầm máy | Quét mã QR xong hiện ảnh chân dung, phải tích xác nhận |
| U-NV-5 | làm việc được cả khi sóng yếu | không để hàng người phải chờ | Biên bản lưu tạm rồi tự đẩy lên, hiện số biên bản còn chờ |
{caption: Năm câu chuyện của vai trò nhân viên giao nhận.}
{widths: 2,4,4,6}

| Mã | Là quản trị viên, tôi muốn… | …để… | Tiêu chí chấp nhận |
|---|---|---|---|
| U-QT-1 | một lịch ngang thấy ngay máy nào rảnh ca nào | điều phối được giờ cao điểm | Ô phân biệt màu giữa trống, đã đặt, đang thuê, bảo trì, đang chuẩn bị |
| U-QT-2 | duyệt tay hồ sơ bị đánh dấu nghi ngờ | không để khách thật bị kẹt | Hiện ảnh và hai điểm số, mỗi quyết định kèm lý do và vào nhật ký |
| U-QT-3 | đổi giá mà không động tới đơn đã chốt | khỏi giải thích vì sao tiền đổi | Giá mới có ngày hiệu lực, đơn cũ giữ giá cũ, lịch sử tra lại được |
| U-QT-4 | khoá máy quá hạn nhưng không tự mình quyết | tránh lạm quyền và khoá nhầm | Chỉ chạy khi có người thứ hai duyệt, ghi lý do vào nhật ký bất biến |
| U-QT-5 | xem tỉ lệ khai thác đội máy theo tuần | biết khi nào nên mua thêm máy | Số ca đã bán chia số ca khả dụng, xuất được ra CSV |
| U-QT-6 | kết xuất trọn hồ sơ một đơn | có đủ chứng cứ trong một lần bấm | PDF gồm hợp đồng, hai biên bản, mười hai ảnh và nhật ký trạng thái |
{caption: Sáu câu chuyện của vai trò quản trị viên.}
{widths: 2,4,4,6}

## Bảng phân quyền

**Có** là được phép, **Hai người** là chỉ thực thi khi có người thứ hai duyệt, **Không** là chặn ở tầng máy chủ chứ không chỉ ẩn nút.

| Thao tác | Sinh viên | Nhân viên | Quản trị |
|---|---|---|---|
| Xem danh mục máy và ca còn trống | Có | Có | Có |
| Đặt đơn cho chính mình | Có | Không | Có |
| Xem hồ sơ xác minh của chính mình | Có | Không | Có |
| Xem hồ sơ xác minh của người khác | Không | Không | Có |
| Duyệt hoặc từ chối hồ sơ xác minh | Không | Không | Có |
| Gán máy cụ thể cho đơn | Không | Có | Có |
| Lập biên bản bàn giao và thu hồi | Không | Có | Có |
| Sửa biên bản đã ký | Không | Không | Không |
| Lập phiếu sự cố theo biểu phí | Không | Có | Có |
| Khấu trừ vượt biểu phí | Không | Không | Hai người |
| Hoàn cọc trong hạn mức 300.000đ | Không | Không | Có |
| Hoàn tiền ngoài phạm vi cọc | Không | Không | Hai người |
| Sửa bảng giá và mức cọc | Không | Không | Có |
| Thêm, sửa, ngừng dùng thiết bị | Không | Không | Có |
| Đổi trạng thái máy sang bảo trì | Không | Có | Có |
| Khoá màn hình máy từ xa | Không | Không | Hai người |
| Gỡ khoá màn hình | Không | Không | Có |
| Thêm vào danh sách chặn | Không | Không | Hai người |
| Kết xuất hồ sơ đơn ra PDF | Đơn của mình | Không | Có |
| Xoá dữ liệu cá nhân theo yêu cầu | Gửi yêu cầu | Không | Hai người |
| Đọc nhật ký kiểm toán | Không | Không | Có |
| Sửa hoặc xoá nhật ký kiểm toán | Không | Không | Không |
{caption: Ma trận phân quyền theo vai trò và thao tác.}
{widths: 7,3,3,3}
{note: Nhân viên chỉ thấy ảnh chân dung khách lúc bàn giao. Biên bản đã ký chỉ sửa được bằng biên bản đính chính. Mọi thao tác mức "Hai người" đều ghi cả người yêu cầu lẫn người duyệt vào nhật ký.}

:::ok Kết luận của chương
Bản chạy được đầu tiên gồm hai mươi ba chức năng bắt buộc, vừa đủ cho trọn một vòng đời đơn thuê: đặt được, xác minh được, bàn giao có bằng chứng, thu hồi có đối chiếu, hoàn cọc có dấu vết. Đó cũng là những việc không website cho thuê laptop nào ở Việt Nam đang làm được, vì toàn ngành vẫn chốt đơn qua điện thoại [[ref:https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html]].
:::
