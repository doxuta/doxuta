## Ba bề mặt sử dụng, một mã nguồn duy nhất

**Web cho sinh viên** chạy trên trình duyệt điện thoại: chọn ca thi, xác minh danh tính, trả tiền, theo dõi đơn. Từ vựng giao diện mượn nguyên của hệ thống "ĐK Mượn máy" mà sinh viên Đại học FPT đã dùng sẵn, gồm **Dashboard**, **ĐK thuê máy** và **Trả máy** [[ref:https://it-hcm.fpt.edu.vn/articles.php?news=huong-dan-muon-laptop-cua-sinh-vien-trong-truong&id=56]]. Chi phí học của người dùng vì thế gần bằng không.

**Ứng dụng cho nhân viên giao nhận** là một ứng dụng web tiến bộ (PWA) cài lên màn hình chính điện thoại. Nhân viên có mười lăm phút để bàn giao cả chục máy, nên bề mặt này chỉ còn ba thao tác lớn: quét mã QR đơn, chụp sáu ảnh hiện trạng, lấy chữ ký. Ảnh lưu tạm bằng IndexedDB rồi tự đẩy lên khi có mạng, vì sóng ở sảnh thường chập chờn.

**Bảng điều khiển quản trị** chạy trên máy tính: lịch ngang máy nhân ca thi, hồ sơ từng thiết bị, cấu hình giá, báo cáo, nhật ký kiểm toán. Cấu trúc lấy theo đặc tả chức năng của Booqable, phần mềm cho thuê thiết bị quản lý theo mã vạch của từng cá thể [[ref:https://booqable.com/features/]].

Ba bề mặt nhưng **một mã nguồn, một cơ sở dữ liệu, một bảng phân quyền**, vì ba lý do. Cả ba cùng thao tác trên một máy trạng thái đơn thuê, tách thành ba dự án nghĩa là ba bản sao của luật chuyển trạng thái và sớm muộn chúng lệch nhau. Thao tác quan trọng nhất, giữ chỗ một máy trong một khung giờ, phải nằm gọn trong một giao dịch cơ sở dữ liệu thì ràng buộc chống trùng lịch mới phát huy tác dụng. Và rủi ro lớn nhất của dự án này là không kịp hạn chứ không phải hiệu năng. Snipe-IT cũng làm đúng như vậy: một ứng dụng Laravel duy nhất phục vụ cả giao diện quản trị lẫn API [[ref:https://github.com/grokability/snipe-it]].

```php
// routes/web.php — ba bề mặt tách bằng tiền tố và lớp kiểm quyền, không phải bằng ba dự án
Route::middleware(['auth','verified.kyc'])->group(base_path('routes/student.php'));
Route::prefix('staff')->middleware(['auth','role:staff'])->group(base_path('routes/staff.php'));
Route::prefix('admin')->middleware(['auth','role:admin','twofactor'])->group(base_path('routes/admin.php'));
```
{caption: Ba bề mặt dùng chung một tầng nghiệp vụ, chỉ khác nhau ở tiền tố đường dẫn và lớp kiểm quyền.}

<<<landscape>>>

![Ba nhóm người dùng ở bên trái sơ đồ dùng chung một tầng ứng dụng, một cơ sở dữ liệu PostgreSQL và một tập dịch vụ ngoài.](assets/diagrams/04-kien-truc.png){w=24}{src: Nguồn: nhóm tác giả.}

<<<portrait>>>

## Danh sách chức năng theo mức ưu tiên

Cột vai trò viết tắt: SV là sinh viên, NV là nhân viên giao nhận, QT là quản trị viên, HT là tác vụ tự động.

| Mã | Chức năng | Vai trò | Ưu tiên | Lý do và ghi chú kỹ thuật |
|---|---|---|---|---|
| F01 | Đăng ký bằng email `@fpt.edu.vn` và mã số sinh viên, xác nhận bằng OTP | SV | Bắt buộc | `users.email_fpt` đặt ràng buộc duy nhất; dùng danh tính trường thay cho việc đòi giấy tờ, theo cách Grover xác minh theo mức rủi ro [[ref:https://www.grover.com/us-en/how-it-works]] |
| F02 | Đăng nhập, quản lý phiên, bắt buộc hai lớp cho tài khoản quản trị | SV·NV·QT | Bắt buộc | Quản trị có quyền khoá máy nên không được dùng mật khẩu đơn |
| F03 | Xác minh danh tính một lần: hai mặt CCCD và video kiểm tra người sống | SV | Bắt buộc | `POST /api/kyc/submit`; ghi `kyc_profiles(id_number_hash, face_vector, match_score)` |
| F04 | Hàng chờ duyệt tay hồ sơ điểm thấp | QT | Bắt buộc | Kích hoạt khi điểm so khớp dưới 0,90; cam kết trả lời trong 30 phút |
| F05 | Tra máy trống theo ca thi, hiện số suất còn lại từng ca | SV | Bắt buộc | `GET /api/availability?slot_id=&model_id=`, loại trừ các `inventory_holds` còn hiệu lực |
| F06 | Danh sách máy nhóm A, B, C kèm nhãn "đã test EOS và SEB ngày dd/mm" | SV | Bắt buộc | Cột `devices.seb_tested_at`; tín hiệu niềm tin khác biệt nhất so với đối thủ |
| F07 | Giữ chỗ có hạn mười phút | SV | Bắt buộc | `POST /api/holds`; `inventory_holds.expires_at`; tác vụ dọn dẹp chỉ đổi cờ, không xoá dòng |
| F08 | Tạo đơn và sinh mã VietQR động, nội dung chuyển khoản là mã đơn | SV | Bắt buộc | `POST /api/orders` kèm tiêu đề `Idempotency-Key`, chống bấm hai lần theo chuẩn Stripe [[ref:https://stripe.com/blog/idempotency]] [[ref:https://brandur.org/idempotency-keys]] |
| F09 | Nhận thông báo tiền về, kiểm chữ ký, khử trùng lặp theo mã giao dịch | HT | Bắt buộc | `POST /webhooks/payment`; `payments.provider_txn_id` duy nhất; giữ `raw_payload` |
| F10 | Đối soát tay giao dịch lệch tiền hoặc sai nội dung | QT | Bắt buộc | Chuyển khoản thủ công luôn có tỉ lệ ghi sai nội dung, thiếu màn hình này thì tiền treo |
| F11 | Ký hợp đồng điện tử, ô tích riêng cho khối "không được miễn trừ" | SV | Bắt buộc | Hai ô tích tách rời, rút từ vụ Getaround bị Tổng Chưởng lý Washington DC xử lý [[ref:https://oag.dc.gov/release/attorney-general-schwalb-secures-refunds-dc]] |
| F12 | Trang đơn thành công kèm mã QR nhận máy và giờ giao ghi bằng số | SV | Bắt buộc | Cam kết bằng con số cụ thể giảm mạnh lượng khách nhắn hỏi, theo cách Turo làm [[ref:https://help.turo.com/en_us/security-deposits-us-HkbE44lE9]] |
| F13 | Gán máy cụ thể cho đơn, gợi ý tự động ưu tiên máy pin cao | NV·QT | Bắt buộc | `orders.device_id` chỉ điền ở bước này; đặt theo loại rồi gán cá thể là chuẩn chung của ngành [[ref:https://raw.githubusercontent.com/Koha-Community/Koha/master/installer/data/mysql/kohastructure.sql]] |
| F14 | Danh mục mười hai bước chuẩn bị máy trước ca thi | NV | Bắt buộc | `handovers.checklist` kiểu `jsonb`; thiếu bước nào thì không chuyển trạng thái được |
| F15 | Biên bản bàn giao: sáu ảnh bắt buộc và chữ ký hai bên | NV·SV | Bắt buộc | `handover_photos(angle, url, sha256)`, theo mẫu `checkout_acceptances` của Snipe-IT [[ref:https://github.com/grokability/snipe-it/blob/master/database/migrations/2018_07_28_023826_create_checkout_acceptances_table.php]] |
| F16 | Biên bản thu hồi, đặt ảnh trước và sau cạnh nhau theo từng khung | NV | Bắt buộc | Tách hao mòn thường miễn phí với hư hỏng có phí, theo cách Grover trình bày [[ref:https://www.grover.com/at-en/g-about/asset-condition]] |
| F17 | Hoàn cọc sau khi kết luận máy nguyên vẹn | HT·QT | Bắt buộc | Bản đầu bán tự động: hệ thống dựng sẵn lệnh chuyển khoản, quản trị bấm duyệt |
| F18 | Lập phiếu sự cố, tính khấu trừ theo biểu phí công khai | NV·QT | Bắt buộc | `incidents(type, deduction_amount, status)`; chỉ chọn hạng mục, không gõ số tự do |
| F19 | Khiếu nại phiếu sự cố trong 48 giờ kèm ảnh đối chiếu | SV | Nên có | Thiếu kênh khiếu nại thì tranh chấp chạy sang mạng xã hội, đúng vết Fat Llama [[ref:https://www.trustpilot.com/review/fatllama.com]] |
| F20 | Quản lý kho máy theo mã tài sản và số sê-ri | QT | Bắt buộc | `devices(asset_tag UK, serial UK, status, battery_health_pct, mdm_device_id)` |
| F21 | Lịch ngang: mỗi hàng một máy, mỗi cột một ca thi, ô màu theo trạng thái | QT | Bắt buộc | Màn hình điều phối chính của người trực ca |
| F22 | Nhật ký bảo trì và cảnh báo pin dưới 80% | QT | Nên có | `maintenance_logs(type, cost)`; pin yếu là nguyên nhân hỏng giữa ca thi hay gặp nhất |
| F23 | Cấu hình giá theo nhóm máy và loại gói, có ngày hiệu lực | QT | Bắt buộc | `pricing_rules(model_id, slot_type, price, deposit, waiver_fee, valid_from)`; đơn đã chốt giữ giá cũ |
| F24 | Điểm tín nhiệm và bậc cọc tự động theo số lượt thuê sạch | HT | Nên có | `users.trust_score`; cọc theo hồ sơ rủi ro thay vì cọc phẳng |
| F25 | Danh sách chặn nội bộ theo số CCCD đã băm | QT | Bắt buộc | `blocklist(id_number_hash, reason)`; băm để vẫn chặn được mà không giữ số thật |
| F26 | Nhắc hạn tự động trước 12 giờ, trước 2 giờ và sau hạn 15 phút | HT | Bắt buộc | Hàng đợi `outbox_messages` do tác vụ nền đọc, không gửi thẳng trong luồng web |
| F27 | Cảnh báo quá hạn trên bảng điều khiển kèm bộ đếm phí trễ | QT | Bắt buộc | Phí trễ 20.000đ mỗi 30 phút, trần 200.000đ một ngày, phải hiện cho cả hai bên |
| F28 | Khoá màn hình từ xa qua MDM, bắt buộc hai người duyệt | QT | Nên có | `lock_requests(requested_by, approved_by, reason)` |
| F29 | Báo cáo tỉ lệ khai thác, doanh thu theo gói, tỉ lệ sự cố | QT | Nên có | Số liệu đầu vào cho chương tài chính |
| F30 | Nhật ký kiểm toán chỉ ghi thêm, nối chuỗi băm | HT | Bắt buộc | `audit_logs` gắn trigger chặn `UPDATE` và `DELETE`; tính bất biến là nền của chuỗi bảo quản bằng chứng [[ref:https://www.locatorx.com/blog/the-truth-about-asset-records-why-immutability-is-the-foundation-of-a-verifiable-chain-of-custody]] |
| F31 | Kết xuất hồ sơ một đơn ra PDF: hợp đồng, biên bản, ảnh, nhật ký | QT | Bắt buộc | Bộ hồ sơ nộp kèm khi trình báo theo Điều 175 Bộ luật Hình sự 2015 |
| F32 | Xuất dữ liệu theo khoảng thời gian ra CSV | QT | Nên có | Phục vụ kế toán và đối soát cuối kỳ |
| F33 | Sinh viên tự tải về dữ liệu cá nhân của chính mình | SV | Nên có | Quyền tiếp cận dữ liệu, chi tiết ở chương tuân thủ |
| F34 | Xoá dữ liệu theo yêu cầu, tự xoá ảnh eKYC sau 90 ngày | HT·QT | Bắt buộc | `kyc_profiles.images_purge_at`; nhật ký giữ dấu vết xoá nhưng không giữ ảnh |
| F35 | Đánh giá sau lượt thuê | SV | Để sau | Chưa đủ lượt để điểm trung bình có ý nghĩa |
| F36 | Báo khi ca thi đã kín có chỗ trống trở lại | SV | Để sau | Chỉ có giá trị khi tỉ lệ kín chỗ cao; năm đầu khai thác bình quân mới khoảng 42% |
{caption: Ba mươi sáu chức năng của hệ thống, phân theo vai trò sử dụng và mức ưu tiên.}
{widths: 1,5,2,2,7}
{note: Hai mươi bốn chức năng ở mức bắt buộc cho bản chạy được đầu tiên, tám ở mức nên có, bốn để sau.}

## Ranh giới của bản chạy được đầu tiên

| Không làm ở bản đầu | Làm thay bằng | Vì sao, và khi nào mở khoá |
|---|---|---|
| Ứng dụng di động riêng cho iOS và Android | Web đáp ứng cho sinh viên, PWA cài màn hình chính cho nhân viên | Hai kho ứng dụng là hai quy trình duyệt và hai chu kỳ phát hành, đổi lại gần như không thêm chức năng nào. Mở khoá khi cần phần cứng mà trình duyệt không cho dùng |
| Hoàn cọc tự động qua cổng thanh toán | Hệ thống dựng sẵn lệnh chuyển khoản, quản trị duyệt trong 5 phút | Cơ chế giữ tiền trên thẻ rồi tự hoàn của nền tảng quốc tế chưa xác minh được là có tương đương ở Việt Nam [[ref:https://help.turo.com/en_us/security-deposits-us-HkbE44lE9]]. Mở khoá khi ký được cổng thanh toán có hoàn tiền qua API |
| Tích hợp trực tiếp với hệ thống của nhà trường | Sinh viên tự chọn ca thi; hệ thống chỉ kiểm tên miền email và mã số sinh viên | Nhóm không có thẩm quyền xin kết nối, và cũng chưa xác nhận được nhà trường có cho mang máy thuê vào phòng thi hay không [[ref:https://daihoc.fpt.edu.vn/tin-noi-bat-muc-tin-tuc/huong-dan-sinh-vien-su-dung-va-thi-tren-phan-mem-eos-tai-truong-dai-hoc-fpt/]]. Mở khoá khi có văn bản của Phòng Khảo thí |
| Nhiều điểm nhận máy | Một điểm hẹn cố định trong khuôn viên, ghi rõ trên đơn | Mười máy chia nhiều điểm thì mỗi điểm không đủ tồn kho để luôn còn máy. Mở khoá khi đội máy vượt mốc mười sáu máy của năm thứ hai |
| Gợi ý bằng học máy | Quy tắc gán máy viết thẳng: pin cao nhất trước, rồi đến máy ít lượt thuê nhất | Vài trăm lượt thuê năm đầu không đủ cho mô hình học được gì, mà quy tắc tường minh thì giải thích được cho khách. Mở khoá khi có vài nghìn lượt |
{caption: Năm hạng mục cố ý để ngoài phạm vi bản chạy được đầu tiên.}
{widths: 4,5,8}

:::warn Một ranh giới nữa, ít ai nghĩ tới
Hệ thống không thay thế phần mềm quản lý tài sản nói chung. Bảng `checkout_requests` của Snipe-IT không có cột ngày bắt đầu và ngày kết thúc, nghĩa là nó quản lý theo mô hình "ai đang giữ" chứ không theo mô hình "ai sẽ giữ, từ lúc nào tới lúc nào" [[ref:https://github.com/grokability/snipe-it/blob/master/database/migrations/2016_09_02_001448_create_checkout_requests_table.php]].
Thêm nữa Snipe-IT phát hành theo giấy phép AGPL, nên sửa mã rồi chạy thành dịch vụ công khai sẽ kéo theo nghĩa vụ công bố phần đã sửa [[ref:https://snipeitapp.com/faq]]. Nhóm học mô hình dữ liệu của họ, không fork mã nguồn của họ.
:::

## Câu chuyện người dùng theo từng vai trò

| Mã | Là sinh viên, tôi muốn… | …để… | Tiêu chí chấp nhận |
|---|---|---|---|
| U-SV-1 | xem ca thi nào còn máy trống ngay ở lần chạm đầu tiên | biết có nên tiếp tục hay đi hỏi chỗ khác | Không cần đăng nhập; nội dung chính hiện xong dưới 2,5 giây trên 4G; mỗi ca ghi đúng số suất còn lại |
| U-SV-2 | giữ chỗ một máy trong lúc đi chuyển khoản | không mất suất giữa chừng | Có bộ đếm ngược 10 phút; hết giờ chưa trả tiền thì suất tự về kho và máy hiện lại ở ca đó |
| U-SV-3 | xác minh danh tính một lần rồi lần sau đi thẳng | khỏi chụp lại giấy tờ mỗi kỳ thi | Lượt thứ hai trở đi từ chọn ca tới xác nhận không quá 4 bước, không bị hỏi lại giấy tờ |
| U-SV-4 | biết chính xác trường hợp nào phải đền bao nhiêu | không bị bất ngờ lúc trả máy | Khối "không được miễn trừ" có ô tích riêng; chưa tích thì nút xác nhận không bật; số tiền khớp biểu phí công khai |
| U-SV-5 | được nhắc trước khi tới hạn trả máy | không bị tính phí trễ vì quên | Có tin trước 12 giờ, trước 2 giờ và sau hạn 15 phút, mỗi tin ghi giờ hạn và mức phí trễ |
| U-SV-6 | thấy tiền cọc về tài khoản ngay sau khi trả máy | yên tâm thuê lần sau | Từ lúc nhân viên hoàn tất biên bản thu hồi tới lúc duyệt lệnh hoàn cọc không quá 5 phút, có biên lai điện tử |
{caption: Sáu câu chuyện người dùng của vai trò sinh viên.}
{widths: 2,5,4,7}

| Mã | Là nhân viên giao nhận, tôi muốn… | …để… | Tiêu chí chấp nhận |
|---|---|---|---|
| U-NV-1 | mở một danh sách duy nhất các đơn của ca sắp tới, sắp theo giờ giao | khỏi tra từng đơn | Hàng chờ hiện đủ đơn của ca kế tiếp, mỗi dòng có nút quét mã QR mở thẳng biên bản bàn giao |
| U-NV-2 | được gợi ý máy nào nên gán cho đơn nào | khỏi tự nhớ máy nào pin còn tốt | Gợi ý xếp theo pin giảm dần rồi số lượt thuê tăng dần; đổi tay được và lý do đổi được ghi lại |
| U-NV-3 | chụp sáu ảnh và lấy chữ ký ngay trên điện thoại | có bằng chứng nếu về sau tranh chấp | Thiếu một ảnh hoặc thiếu chữ ký thì nút gửi bị khoá; mỗi ảnh lưu kèm mã băm SHA-256 và dấu thời gian |
| U-NV-4 | đối chiếu mặt người trước mặt với ảnh đã xác minh | không giao nhầm máy | Sau khi quét mã QR, màn hình hiện ảnh chân dung đã xác minh; nhân viên phải tích xác nhận đã đối chiếu |
| U-NV-5 | làm việc được cả khi sóng yếu | không để hàng người phải chờ | Biên bản lưu tạm trên máy rồi tự đẩy lên khi có mạng; màn hình hiện số biên bản còn chờ gửi |
{caption: Năm câu chuyện người dùng của vai trò nhân viên giao nhận.}
{widths: 2,5,4,7}

| Mã | Là quản trị viên, tôi muốn… | …để… | Tiêu chí chấp nhận |
|---|---|---|---|
| U-QT-1 | nhìn một lịch ngang thấy ngay máy nào rảnh ca nào | điều phối được trong giờ cao điểm | Mỗi hàng một máy, mỗi cột một ca; ô phân biệt bằng màu giữa trống, đã đặt, đang thuê, bảo trì, đang chuẩn bị |
| U-QT-2 | duyệt tay hồ sơ xác minh bị đánh dấu nghi ngờ | không để khách thật bị kẹt vì máy chấm sai | Hàng chờ hiện ảnh và hai điểm số; mỗi quyết định bắt buộc kèm lý do và được ghi nhật ký |
| U-QT-3 | đổi bảng giá cho kỳ thi tới mà không động tới đơn đã chốt | khỏi phải giải thích vì sao tiền đổi | Giá mới có ngày hiệu lực; đơn tạo trước ngày đó giữ giá cũ; lịch sử đổi giá tra lại được |
| U-QT-4 | khoá màn hình máy quá hạn nhưng không tự mình quyết | tránh lạm quyền và khoá nhầm | Lệnh chỉ chạy khi có người thứ hai duyệt; người yêu cầu, người duyệt và lý do vào nhật ký bất biến; không xoá dữ liệu trên máy |
| U-QT-5 | xem tỉ lệ khai thác đội máy theo tuần | biết khi nào nên mua thêm máy | Số ca đã bán chia số ca khả dụng, xuất được ra CSV |
| U-QT-6 | kết xuất trọn hồ sơ một đơn khi có tranh chấp | có bộ chứng cứ đủ trong một lần bấm | Tệp PDF gồm hợp đồng đã ký, hai biên bản, mười hai ảnh, nhật ký chuyển trạng thái và nhật ký MDM cùng khoảng thời gian |
{caption: Sáu câu chuyện người dùng của vai trò quản trị viên.}
{widths: 2,5,4,7}

## Bảng phân quyền

Ma trận này là nguồn duy nhất để lập trình lớp kiểm quyền. **Có** là được phép, **Hai người** là chỉ thực thi khi có người thứ hai phê duyệt, **Không** là bị chặn ở tầng máy chủ chứ không chỉ ẩn nút trên giao diện.

| Thao tác | Sinh viên | Nhân viên | Quản trị |
|---|---|---|---|
| Xem danh mục máy và ca thi còn trống | Có | Có | Có |
| Tạo giữ chỗ và đặt đơn cho chính mình | Có | Không | Có |
| Xem hồ sơ xác minh của chính mình | Có | Không | Có |
| Xem hồ sơ xác minh của người khác | Không | Không | Có |
| Duyệt hoặc từ chối hồ sơ xác minh | Không | Không | Có |
| Gán máy cụ thể cho đơn | Không | Có | Có |
| Lập biên bản bàn giao và thu hồi | Không | Có | Có |
| Sửa một biên bản đã ký | Không | Không | Không |
| Lập phiếu sự cố theo biểu phí | Không | Có | Có |
| Khấu trừ vượt mức biểu phí công khai | Không | Không | Hai người |
| Hoàn cọc trong hạn mức 300.000đ | Không | Không | Có |
| Hoàn tiền ngoài phạm vi tiền cọc | Không | Không | Hai người |
| Sửa bảng giá và mức cọc | Không | Không | Có |
| Thêm, sửa, ngừng dùng thiết bị | Không | Không | Có |
| Đổi trạng thái máy sang bảo trì | Không | Có | Có |
| Khoá màn hình máy từ xa | Không | Không | Hai người |
| Gỡ khoá màn hình | Không | Không | Có |
| Thêm người vào danh sách chặn | Không | Không | Hai người |
| Kết xuất hồ sơ đơn ra PDF | Chỉ đơn của mình | Không | Có |
| Xoá dữ liệu cá nhân theo yêu cầu | Gửi yêu cầu | Không | Hai người |
| Đọc nhật ký kiểm toán | Không | Không | Có |
| Sửa hoặc xoá nhật ký kiểm toán | Không | Không | Không |
{caption: Ma trận phân quyền theo vai trò và thao tác.}
{widths: 7,3,3,3}
{note: Nhân viên chỉ thấy ảnh chân dung của khách tại thời điểm bàn giao, không mở được hồ sơ xác minh. Biên bản đã ký không sửa được, chỉ lập được biên bản đính chính mới tham chiếu tới bản cũ. Việc gỡ khoá dễ hơn khoá là cố ý, theo nguyên tắc thất bại an toàn. Mọi thao tác mức "Hai người" đều ghi cả người yêu cầu lẫn người phê duyệt vào nhật ký kiểm toán.}

:::ok Kết luận của chương
Phạm vi bản chạy được đầu tiên gồm hai mươi bốn chức năng bắt buộc, vừa đủ để hoàn thành trọn một vòng đời đơn thuê: đặt được, xác minh được, bàn giao có bằng chứng, thu hồi có đối chiếu, hoàn cọc có dấu vết. Đó cũng chính là những việc mà không một website cho thuê laptop nào ở Việt Nam đang làm được, vì toàn ngành vẫn chốt đơn qua điện thoại [[ref:https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html]].
:::
