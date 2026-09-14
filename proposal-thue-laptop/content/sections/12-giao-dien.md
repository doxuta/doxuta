## Ảnh trong chương này là bản dựng nguyên mẫu

Mười ảnh dưới đây là **bản dựng nguyên mẫu do nhóm thiết kế**, kết xuất từ mã HTML trong thư mục `prototype/screens/`. Chúng **không phải ảnh chụp một hệ thống đang chạy**: chưa có máy chủ, chưa có cơ sở dữ liệu thật phía sau. Mọi mã đơn, tên khách, doanh thu và tỉ lệ khai thác hiện trên ảnh là **dữ liệu minh hoạ** [Ước lượng của nhóm]; riêng bảng giá, tiền cọc 300.000đ và phí miễn trừ thiệt hại 15.000đ lấy đúng từ biểu phí chính thức của ExamLap.

Nhóm cũng phải nói rõ một khoảng trống của phần nghiên cứu giao diện: **chưa chụp được ảnh màn hình của bất kỳ website đối thủ nào**. Môi trường nghiên cứu chặn hoàn toàn việc tải trang, nên mọi mô tả về đối thủ chỉ suy ra từ tiêu đề trang, đường dẫn và đoạn trích kết quả tìm kiếm, không phải từ việc nhìn thấy giao diện thật.

:::warn Việc nhóm phải tự làm trước khi nộp bản cuối
Mở trình duyệt, chụp toàn trang sáu địa chỉ sau và lập bảng so sánh theo các cột: có form đặt hàng không, có hiện tồn kho không, có chọn ngày không, có tài khoản người dùng không, mấy bước tới lúc chốt đơn, kênh liên hệ chính.
1. [leminhstore.vn — thuê laptop sinh viên Đà Nẵng](https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html)
2. [maytinhdinhhau.vn — dịch vụ cho thuê tại Đà Nẵng](https://maytinhdinhhau.vn/dich-vu-cho-thue-laptop-tai-da-nang/)
3. [truonggiang.vn — cho thuê laptop](https://truonggiang.vn/cho-thue-laptop.html)
4. [mitgroup.vn — thuê laptop sinh viên](https://mitgroup.vn/thue-laptop-sinh-vien/)
5. [phuongnamco.com — cho thuê laptop thi cử](https://phuongnamco.com/cho-thue-laptop-thi-cu-giai-phap-huu-ich-cho-sinh-vien-mua-thi/)
6. [it-hcm.fpt.edu.vn — hướng dẫn mượn laptop trong trường](https://it-hcm.fpt.edu.vn/articles.php?news=huong-dan-muon-laptop-cua-sinh-vien-trong-truong&id=56), chụp lại Dashboard sau khi đăng nhập bằng tài khoản trường.
:::

## Nguyên tắc thiết kế

Bối cảnh dùng thật rất hẹp: khách mở web bằng điện thoại, lúc khoảng 06:00 sáng ngày thi, máy vừa hỏng, đang lo mất môn, và mạng trong ký túc xá hoặc trên đường thường yếu. Sáu nguyên tắc dưới đây rút từ bối cảnh đó cộng với khảo sát các nền tảng tham chiếu.

**1. Một màn hình, một quyết định, và hỏi càng muộn càng tốt.** Grover cho khách đi hết luồng đặt hàng rồi mới chạy xác minh ở nền, và chỉ đòi giấy tờ khi hệ thống nghi ngờ [[ref:https://service.grover.com/hc/en-us/articles/19920531898642-How-does-Grover-s-credit-check-work]]. Hệ quả thiết kế: màn hình đầu tiên chỉ hỏi đúng ba thứ khách đã biết chắc là ngày thi, ca thi và điểm nhận máy. Số CCCD, ảnh selfie và tiền chỉ xuất hiện ở bước 2 và bước 3.

**2. Mọi lời hứa phải là một con số hiện ngay trên màn hình.** Turo công bố mốc tự hoàn cọc là 80 giờ sau chuyến, chứ không viết "sẽ hoàn sớm" [[ref:https://help.turo.com/en_us/security-deposits-us-HkbE44lE9]]. Hệ quả: giao diện ExamLap viết "giao trước giờ thi 30 phút", "đổi máy trong 15 phút", "hoàn cọc tự động trong 5 phút" ở đúng chỗ khách đang lo, không giấu trong trang điều khoản. Ngành cho thuê trong nước làm ngược lại, chỉ ghi "hỗ trợ 24/7" hoặc "giao nhanh" [[ref:https://laptopsgn.com/cho-thue-laptop/]].

**3. Nói trước điều bất lợi.** Getaround bị Tổng Chưởng lý Washington DC xử lý không phải vì xe bị mất, mà vì không công bố rõ các trường hợp loại trừ bảo hiểm [[ref:https://oag.dc.gov/release/attorney-general-schwalb-secures-refunds-dc]]; Fat Llama viết "bảo hiểm toàn phần" trên trang chủ rồi từ chối bồi thường và lãnh hàng loạt đánh giá một sao [[ref:https://www.trustpilot.com/review/fatllama.com]]. Hệ quả: khối "những trường hợp không được miễn trừ" nằm trong luồng thanh toán với ô tích riêng, tách khỏi ô tích điều khoản chung.

**4. Mượn từ vựng của nhà trường.** Sinh viên Đại học FPT đã quen một hệ thống nội bộ có "Dashboard", nút "ĐK Mượn máy", nút "Trả máy" và bước chờ bên kia xác nhận [[ref:https://it-hcm.fpt.edu.vn/articles.php?news=huong-dan-muon-laptop-cua-sinh-vien-trong-truong&id=56]]. Hệ quả: nhóm giữ nguyên các nhãn đó, chi phí học của người dùng gần bằng không, và màn hình "chờ xác nhận" không gây khó chịu.

**5. Thiết kế cho một ngón tay cái.** Toàn bộ luồng đặt máy phải bấm được bằng một tay khi đang xách cặp. Hệ quả: nút hành động chính dính đáy màn hình, biểu mẫu một cột, không có bảng ngang nào trong luồng khách.

**6. Không có trạng thái cụt.** Mỗi tin xấu phải đi kèm một hành động kế tiếp: ca thi hết máy thì có nút báo khi có máy, máy lỗi giữa ca thi thì có nút gọi hỗ trợ khẩn kèm cam kết 15 phút. Cam kết đổi máy khi lỗi vốn đã là thông điệp bán hàng của đối thủ [[ref:https://mitgroup.vn/cho-thue-laptop/]], nhóm đưa nó thành một nút bấm thay vì một câu quảng cáo.

## Các màn hình chính

![Trang chủ ExamLap với khẩu hiệu về ngày thi, hộp tra máy trống theo ngày và ca thi, bốn bước quy trình và ba nhóm máy kèm giá theo ca.](assets/screenshots/01-landing.png){w=16}{src: Nguồn: bản dựng nguyên mẫu của nhóm tác giả.}

Trang chủ chỉ bán một ý: máy hỏng sáng ngày thi không còn là mất một môn. Hộp tra cứu đặt ngay dưới khẩu hiệu, gồm ba trường ngày thi, ca thi và nhu cầu sử dụng, thay cho lối bán theo ngày và tháng của cả ngành [[ref:https://skylap.vn/dich-vu-cho-thue/cho-thue-laptop/]]. Thanh điều hướng luôn hiện số máy còn trống hôm nay, một dữ kiện không đối thủ nội địa nào công bố. Khối bốn bước đặt ngay trên trang chủ học theo cách Grover đặt trang "cách hoạt động" trước cả danh mục sản phẩm [[ref:https://www.grover.com/us-en/how-it-works]].

| Phần tử | Mục đích |
|---|---|
| Huy hiệu "Còn 6/10 máy hôm nay" | Biến tồn kho thành lý do hành động ngay |
| Hộp ngày thi, ca thi, nhu cầu | Bắt đầu luồng bằng thứ khách đã biết chắc |
| Dòng "Không giữ CCCD" | Trả lời trước nỗi sợ lớn nhất của sinh viên |
| Ba thẻ máy kèm giá theo ca | Cho biết giá trước khi phải khai báo gì |
{caption: Các phần tử chính của trang chủ và mục đích của từng phần tử.}
{widths: 2,3}

![Màn hình tìm máy trống cho ca thi, có cột bộ lọc bên trái và danh sách thẻ máy kèm trạng thái pin, thời điểm kiểm tra gần nhất và số máy còn lại.](assets/screenshots/02-catalog.png){w=16}{src: Nguồn: bản dựng nguyên mẫu của nhóm tác giả.}

Màn hình này chỉ hiện những máy thật sự đặt được trong ca đã chọn, nên hệ thống không bao giờ phải báo lỗi "hết máy" ở bước sau. Mỗi thẻ máy hiện phần trăm pin còn lại và thời điểm kiểm tra gần nhất, thay cho ảnh catalog chung chung mà các trang trong nước đang dùng [[ref:https://ictsaigon.com.vn/cho-thue-laptop-hp-elitebook-9480m]]. Máy đang bảo trì và máy dự phòng nóng vẫn hiển thị nhưng bị khoá nút, để khách thấy đội máy được quản lý chứ không phải bị giấu.

| Phần tử | Mục đích |
|---|---|
| Bộ lọc ca thi và điểm nhận | Khoá ngữ cảnh, mọi kết quả sau đều đúng ca |
| Dòng "Giữ chỗ tự động 10 phút" | Đặt kỳ vọng đúng về thời hạn giữ máy |
| Nhãn pin và thời điểm kiểm tra | Bằng chứng máy đã được chuẩn bị |
| Thẻ máy bị khoá nút | Minh bạch về tình trạng đội máy |
{caption: Các phần tử chính của màn hình tìm máy trống theo ca thi.}
{widths: 2,3}

![Màn hình xác minh danh tính với ba ảnh chụp căn cước và selfie, sáu dòng kết quả kiểm tra tự động, và hai cột liệt kê dữ liệu có lưu và không lưu.](assets/screenshots/03-ekyc.png){w=16}{src: Nguồn: bản dựng nguyên mẫu của nhóm tác giả.}

Đây là màn hình duy nhất trong luồng khách có thể làm người dùng chùn tay, nên nhóm tách nó thành một bước riêng và nói rõ "chỉ làm một lần duy nhất". Sáu dòng kết quả hiện điểm số thật của từng phép kiểm tra, gồm đọc mã MRZ mặt sau, kiểm tra người sống và so khớp khuôn mặt, theo đúng cách các nhà cung cấp eKYC trong nước mô tả quy trình [[ref:https://docs-vision.fpt.ai/ekyc/I-introduction/gioi-thieu/]] [[ref:https://docs-vision.fpt.ai/en/ekyc/IV-guides/comparing%20liveness%20methods/]]. Grover cũng yêu cầu ảnh selfie thấy rõ đồng thời mặt người và giấy tờ [[ref:https://service.grover.com/hc/en-us/articles/35704298814866-Identity-Verification]].

| Phần tử | Mục đích |
|---|---|
| Câu "Chúng tôi không giữ CCCD bản cứng" | Điểm khác biệt thương mại, đặt ngay đầu trang |
| Sáu dòng kết quả kèm điểm số | Cho khách thấy hệ thống làm gì với ảnh của họ |
| Hai cột "có lưu" và "không lưu" | Cam kết phạm vi dữ liệu, chống hiểu lầm về quyền riêng tư |
| Thẻ tóm tắt đơn cố định bên phải | Nhắc khách đang ở giữa một giao dịch dở dang |
{caption: Các phần tử chính của màn hình xác minh danh tính.}
{widths: 2,3}

![Màn hình đặt cọc và thanh toán với ba lựa chọn thanh toán, khối mã VietQR kèm nội dung chuyển khoản bắt buộc, ba ô tích điều khoản và bảng giải thích cơ chế cọc.](assets/screenshots/04-payment.png){w=16}{src: Nguồn: bản dựng nguyên mẫu của nhóm tác giả.}

Màn hình cọc của ExamLap cố tình không bắt chước mẫu giữ tiền trên thẻ tín dụng của các nền tảng phương Tây, vì cơ chế đó là tính năng của mạng thẻ [[ref:https://docs.stripe.com/payments/extended-authorization]] còn sinh viên Việt Nam gần như chỉ chuyển khoản và dùng ví. Thay vào đó là mã VietQR kèm nội dung chuyển khoản bắt buộc, và hệ thống tự xác nhận khi nhận được tín hiệu đối soát, khách không phải bấm thêm gì. Khối "cơ chế cọc" giải thích thẳng vì sao cọc chỉ bằng 4,0% giá trị máy: rào cản nằm ở danh tính đã xác minh và khả năng khoá máy từ xa.

| Phần tử | Mục đích |
|---|---|
| Đồng hồ "Giữ máy còn 08:42" | Tạo giới hạn thời gian rõ ràng thay vì thúc ép mơ hồ |
| Nội dung chuyển khoản bắt buộc | Điều kiện để đối soát tự động, tránh tra soát tay |
| Ba ô tích tách rời | Ô riêng cho việc cài phần mềm quản lý thiết bị |
| Bảng "hoàn cọc khi nào" | Công khai mức khấu trừ trước khi khách trả tiền |
{caption: Các phần tử chính của màn hình đặt cọc và thanh toán.}
{widths: 2,3}

![Vé nhận máy hiển thị mã QR lớn, danh sách sáu việc đã làm để chuẩn bị máy, tiến trình đơn thuê theo mốc thời gian và khối gọi hỗ trợ khẩn.](assets/screenshots/05-pass.png){w=16}{src: Nguồn: bản dựng nguyên mẫu của nhóm tác giả.}

Vé nhận máy là màn hình khách mở lại nhiều nhất, thường vào lúc 06:45 khi đang đi bộ tới sảnh, nên mã QR chiếm nửa trên và không cần thao tác nào để hiện ra. Danh sách sáu việc đã làm để chuẩn bị máy trả lời trước câu hỏi "máy này có chạy được bài thi không". Tiến trình đơn thuê hiện đủ sáu mốc kèm giờ, trong đó mốc cuối là hoàn cọc tự động, đúng tinh thần công bố mốc thời gian bằng con số của Turo [[ref:https://help.turo.com/en_us/security-deposits-us-HkbE44lE9]].

| Phần tử | Mục đích |
|---|---|
| Mã QR kèm chuỗi dự phòng | Quét nhanh, vẫn đọc tay được khi camera lỗi |
| Danh sách chuẩn bị máy | Chứng minh sản phẩm là "máy sẵn sàng thi" |
| Tiến trình sáu mốc có giờ | Loại bỏ tin nhắn hỏi "bao giờ được hoàn cọc" |
| Nút gọi hỗ trợ khẩn | Lối thoát cho tình huống máy lỗi giữa ca thi |
{caption: Các phần tử chính của vé nhận máy.}
{widths: 2,3}

![Ứng dụng nhân viên trên điện thoại, hiển thị biên bản kiểm tra bảy mục với sáu mục đã tích, và nút ký điện tử đang bị khoá.](assets/screenshots/06-staff.png){w=8}{src: Nguồn: bản dựng nguyên mẫu của nhóm tác giả.}

Ứng dụng nhân viên chạy trên điện thoại vì việc bàn giao diễn ra ở sảnh, trong khoảng mười lăm phút cao điểm trước ca thi. Biên bản kiểm tra gồm bảy mục, mở rộng từ danh mục kiểm tra khi thu hồi thiết bị của Grover là màn hình, bàn phím, loa, camera và kết nối [[ref:https://www.grover.com/at-en/g-about/asset-condition]]. Quyết định thiết kế đáng chú ý nhất: nút "Khách ký điện tử và giao máy" bị khoá cho tới khi đủ bảy mục và đủ ảnh hiện trạng, kèm dòng giải thích vì sao nút bị khoá. Quy tắc chặn nằm ở tầng máy chủ chứ không chỉ ở giao diện.

| Phần tử | Mục đích |
|---|---|
| Thẻ khách kèm nhãn "Khớp" | Xác thực lại danh tính ở từng lượt giao dịch |
| Bộ đếm "6/7" trên biên bản | Cho biết còn thiếu gì mà không phải cuộn tìm |
| Nút bị khoá kèm lời giải thích | Biến quy tắc nghiệp vụ thành hướng dẫn thao tác |
| Ô chụp ảnh hiện trạng | Sinh bằng chứng có mã băm cho tranh chấp sau này |
{caption: Các phần tử chính của ứng dụng nhân viên khi lập biên bản bàn giao.}
{widths: 2,3}

![Bảng điều khiển vận hành với bốn ô chỉ số, bảng đơn thuê trong ngày, lưới lịch khai thác bảy ngày theo ba ca và danh sách cảnh báo cần xử lý.](assets/screenshots/07-dashboard.png){w=16}{src: Nguồn: bản dựng nguyên mẫu của nhóm tác giả.}

Bảng điều khiển trả lời đúng một câu hỏi mà quản trị viên hỏi mỗi sáng: ca tới có gì phải lo. Bốn ô chỉ số nằm trên cùng, dưới đó là bảng đơn trong ngày với cột trạng thái viết bằng tiếng Việt đời thường, rồi lưới lịch khai thác bảy ngày tới với mỗi hàng là một ca thi. Khối cảnh báo không dừng ở việc báo vấn đề mà nêu luôn bước kế tiếp, ví dụ đơn quá hạn 45 phút đã gửi hai tin nhắn và mốc khoá máy từ xa là 10:15.

| Phần tử | Mục đích |
|---|---|
| Bốn ô chỉ số có mũi tên so sánh | Nhìn một lần biết tình hình đang tốt hay xấu |
| Lưới ca thi bảy ngày | Phát hiện sớm ca sắp kín để mở máy dự phòng |
| Cảnh báo kèm bước kế tiếp | Rút ngắn khoảng cách giữa biết và làm |
| Khối tình trạng kho máy | Đối chiếu nhanh tổng đội máy mười chiếc |
{caption: Các phần tử chính của bảng điều khiển vận hành.}
{widths: 2,3}

![Màn hình kho máy dạng bảng, mỗi hàng một thiết bị với mã tài sản, số sê-ri, trạng thái, nhóm máy, phần trăm pin, đơn hiện tại, thời điểm check-in của phần mềm quản lý thiết bị và số lượt thuê.](assets/screenshots/08-inventory.png){w=16}{src: Nguồn: bản dựng nguyên mẫu của nhóm tác giả.}

Kho máy là màn hình gần nhất với một phần mềm quản lý tài sản thuần tuý, nên nhóm giữ nguyên dạng bảng và mượn mô hình định danh từng thiết bị bằng mã duy nhất của các phần mềm cho thuê thương mại [[ref:https://booqable.com/features/]] [[ref:https://github.com/grokability/snipe-it]]. Cột đáng chú ý nhất là thời điểm check-in gần nhất của phần mềm quản lý thiết bị: máy không check-in quá 30 phút trong thời gian thuê sẽ tự sinh cảnh báo và bị chặn khỏi các lượt đặt kế tiếp.

| Phần tử | Mục đích |
|---|---|
| Mã tài sản và số sê-ri | Khớp với mã khắc laser trên vỏ máy |
| Cột pin và cột lượt thuê | Đầu vào cho quyết định bảo trì và thanh lý |
| Cột check-in thiết bị | Biến im lặng của một máy thành cảnh báo |
| Nút nhập kho hàng loạt | Giảm thao tác khi đội máy lên 16 chiếc ở năm 2 |
{caption: Các phần tử chính của màn hình kho máy.}
{widths: 2,3}

![Màn hình chi tiết đơn thuê với dải tám trạng thái vòng đời, bảng nhật ký tám sự kiện có dấu thời gian, sáu khung ảnh hiện trạng lúc bàn giao và thẻ thông tin người thuê.](assets/screenshots/09-order.png){w=16}{src: Nguồn: bản dựng nguyên mẫu của nhóm tác giả.}

Đây là màn hình dùng khi có tranh chấp, nên nó được thiết kế để đọc chứ không để sửa. Dải tám trạng thái cho biết đơn đang ở đâu trong vòng đời; bảng nhật ký ghi từng sự kiện kèm giờ, diễn giải và nguồn phát sinh, theo mô hình nhật ký chỉ ghi thêm [[ref:https://deepwiki.com/grokability/snipe-it/4.4-activity-logging]]. Sáu ảnh hiện trạng lúc bàn giao lưu kèm mã băm SHA-256. Nút khoá máy từ xa nằm ở góc dưới cùng, màu cảnh báo, và ghi rõ cần hai người duyệt.

| Phần tử | Mục đích |
|---|---|
| Dải tám trạng thái | Định vị đơn trong vòng đời chỉ bằng một cái liếc |
| Nhật ký sự kiện có nguồn | Phân biệt việc do hệ thống, nhân viên hay cổng thanh toán làm |
| Sáu ảnh kèm mã băm | Bằng chứng chống sửa cho tranh chấp hư hỏng |
| Nút khoá máy cần hai người duyệt | Không một cá nhân nào tự khoá được máy của khách |
{caption: Các phần tử chính của màn hình chi tiết đơn và nhật ký.}
{widths: 2,3}

![Báo cáo kinh doanh với bốn chỉ số chính, biểu đồ cột doanh thu và chi phí theo tháng, thanh tỉ lệ khai thác theo dòng máy và danh sách nguồn đơn.](assets/screenshots/10-report.png){w=16}{src: Nguồn: bản dựng nguyên mẫu của nhóm tác giả.}

Màn hình báo cáo được thiết kế để nói ra điểm yếu chứ không chỉ khoe điểm mạnh. Biểu đồ theo tháng hiện rõ ba đỉnh trùng ba kỳ thi cuối kỳ trong năm học, kèm một câu ghi thẳng rằng doanh thu ngoài mùa thi chỉ bằng khoảng 30% đỉnh và đó là rủi ro dòng tiền lớn nhất của mô hình. Thanh tỉ lệ khai thác theo dòng máy cho phép nhận ra dòng nào đang dưới ngưỡng hoà vốn để cân nhắc thanh lý.

| Phần tử | Mục đích |
|---|---|
| Bốn chỉ số có mũi tên xu hướng | Theo dõi doanh thu mỗi máy và tỉ lệ hư hỏng mỗi lượt |
| Biểu đồ doanh thu và chi phí | Nhìn thấy tính mùa vụ thay vì chỉ nghe nói |
| Thanh khai thác theo dòng máy | Quyết định mua thêm hay thanh lý từng dòng |
| Danh sách nguồn đơn | Đo hiệu quả từng kênh tiếp cận sinh viên |
{caption: Các phần tử chính của màn hình báo cáo kinh doanh.}
{widths: 2,3}

## Các tín hiệu tạo niềm tin

Khách đang giao dịch một tài sản trị giá từ 6.500.000đ đến 10.000.000đ với một nhóm sinh viên chưa có thương hiệu. Những chi tiết giao diện dưới đây tồn tại để rút ngắn khoảng cách đó.

| Tín hiệu | Vì sao nó có tác dụng |
|---|---|
| Ngày kiểm tra máy gần nhất in trên từng thẻ máy | Biến lời hứa "máy sẵn sàng thi" thành một mốc thời gian kiểm chứng được |
| Ảnh thật của chính chiếc máy sẽ giao | Đối thủ trong nước dùng ảnh catalog nên đây là điểm vượt rẻ nhất [[ref:https://ictsaigon.com.vn/cho-thue-laptop-hp-elitebook-9480m]] |
| Hai cột "hao mòn thường miễn phí" và "hư hỏng có phí" | Cách Grover giảm tranh chấp là tách đôi và công khai, không viết thành đoạn văn [[ref:https://www.grover.com/at-en/g-about/asset-condition]] |
| Khối loại trừ nằm trong luồng thanh toán, có ô tích riêng | Bài học pháp lý từ vụ Getaround bị xử lý vì giấu điều khoản loại trừ [[ref:https://oag.dc.gov/release/attorney-general-schwalb-secures-refunds-dc]] |
| Mọi cam kết là một con số: 30 phút, 15 phút, 5 phút | Mô phỏng cách Turo công bố mốc 80 giờ [[ref:https://help.turo.com/en_us/security-deposits-us-HkbE44lE9]] |
| Bảng khấu trừ cọc hiện trước khi khách trả tiền | Không ai bị bất ngờ lúc trả máy, đây là thời điểm dễ sinh cãi vã nhất |
| Số máy còn trống theo thời gian thực | Không đơn vị nội địa nào công bố, vừa tạo tin cậy vừa thúc đặt sớm |
| Mức cọc gắn với hạng tín nhiệm hiển thị cho khách | Turo giảm cọc để đổi lấy dữ liệu, nhóm giảm cọc để đổi lấy lịch sử tốt [[ref:https://help.turo.com/en_us/security-deposits-us-HkbE44lE9]] |
| Câu "không giữ CCCD" lặp ở ba màn hình | Đối lập trực tiếp với yêu cầu giữ giấy tờ và xin thông tin gia đình của đối thủ [[ref:https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html]] |
| Hai cột dữ liệu có lưu và không lưu | Minh bạch phạm vi xử lý dữ liệu, cùng tinh thần công khai phí dùng làm gì của Hygglo [[ref:https://help.hygglo.info/en/articles/10415333-how-hygglo-works]] |
| Hotline và Zalo hiện ở mọi trang | Toàn ngành trong nước chạy bằng kênh thoại, bỏ hẳn kênh này là rủi ro |
| Nhật ký sự kiện mở cho khách xem phần liên quan tới đơn của họ | Xác thực lặp lại ở từng giao dịch, không chỉ lúc đăng ký [[ref:https://www.miteksystems.com/blog/innovator-qa-mike-wilkins-senior-director-trust-safety-at-turo]] |
{caption: Mười hai chi tiết giao diện có mục đích tạo niềm tin, kèm lý do thiết kế.}
{widths: 2,3}
{note: Ba điều nhóm tự cấm: không viết "cam kết 100%" mà thiếu danh sách loại trừ ngay cạnh; không quảng cáo giá mồi kiểu "chỉ từ 10k" [[ref:https://www.thuelaptop.vn/thue-laptop-da-nang-gia-re-chi-tu-10k/]]; không giấu điều khoản bất lợi ở cuối trang [[ref:https://saolatech.com.vn/bang-gia-thue-3425667]].}

## Khả năng tiếp cận và điều kiện thực tế

Các ngưỡng dưới đây là **quy ước thiết kế của nhóm** [Ước lượng của nhóm], chọn sao cho dùng được bằng một tay, ngoài trời, lúc trời còn tối.

- **Cỡ chữ.** Chữ thân bài tối thiểu 16 pixel trên điện thoại, chữ phụ chú không nhỏ hơn 13 pixel. Mọi con số tiền và mọi mốc giờ dùng cỡ ít nhất 18 pixel và in đậm, vì đó là thứ khách đọc lướt.
- **Vùng bấm.** Mọi nút và ô tích có vùng chạm tối thiểu 44 × 44 pixel, khoảng cách giữa hai vùng chạm liền kề tối thiểu 8 pixel. Nút hành động chính của mỗi bước dính đáy màn hình, chiếm trọn chiều ngang.
- **Tương phản màu.** Chữ trên nền đạt tỉ lệ tương phản tối thiểu 4,5 trên 1, chữ lớn và biểu tượng tối thiểu 3 trên 1. Trạng thái không bao giờ chỉ mã hoá bằng màu: ô "Quá hạn 45 phút" có cả chữ, ô "Đang thuê" có cả nhãn, để người mù màu vẫn đọc được.
- **Mạng yếu.** Ứng dụng nhân viên là ứng dụng web tiến bộ. Sáu ảnh hiện trạng lưu tạm trong IndexedDB rồi tự đẩy lên khi có sóng, nên biên bản vẫn lập được ở sảnh sóng kém. Trang vé nhận máy được lưu vào bộ nhớ đệm của service worker, mở lại được khi mất mạng hoàn toàn.
- **Khách không có dữ liệu di động.** Vé nhận máy luôn kèm một chuỗi ký tự dạng `EL8241-5410-02` ngay dưới mã QR, nhân viên gõ tay tra được. Mã đơn cũng được gửi qua email và tin nhắn Zalo ngay khi xác nhận, nên khách chỉ cần mở lại tin nhắn cũ. Trường hợp xấu nhất, nhân viên tra bằng mã số sinh viên trên ứng dụng của mình và khách không cần chạm vào điện thoại.
