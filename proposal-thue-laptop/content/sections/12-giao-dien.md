## Ảnh trong chương này là bản dựng nguyên mẫu

Mười ảnh dưới đây là **bản dựng nguyên mẫu do nhóm thiết kế**, kết xuất từ mã HTML trong `prototype/screens/`, **không phải ảnh chụp một hệ thống đang chạy**. Mã đơn, tên khách, doanh thu và tỉ lệ khai thác trên ảnh là dữ liệu minh hoạ [Ước lượng của nhóm]; riêng giá thuê, cọc 300.000đ và phí miễn trừ thiệt hại 15.000đ lấy đúng biểu phí ExamLap.

Nhóm cũng **chưa chụp được ảnh màn hình của website đối thủ nào**, vì môi trường nghiên cứu chặn hoàn toàn việc tải trang. Mọi mô tả về giao diện đối thủ chỉ suy ra từ tiêu đề trang, đường dẫn và đoạn trích kết quả tìm kiếm.

:::warn Sáu địa chỉ nhóm phải tự mở trình duyệt chụp bổ sung
[leminhstore.vn](https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html) · [maytinhdinhhau.vn](https://maytinhdinhhau.vn/dich-vu-cho-thue-laptop-tai-da-nang/) · [truonggiang.vn](https://truonggiang.vn/cho-thue-laptop.html) · [mitgroup.vn](https://mitgroup.vn/thue-laptop-sinh-vien/) · [phuongnamco.com](https://phuongnamco.com/cho-thue-laptop-thi-cu-giai-phap-huu-ich-cho-sinh-vien-mua-thi/) · và Dashboard "ĐK Mượn máy" của [hệ thống nội bộ Đại học FPT](https://it-hcm.fpt.edu.vn/articles.php?news=huong-dan-muon-laptop-cua-sinh-vien-trong-truong&id=56) sau khi đăng nhập bằng tài khoản trường.
Lập bảng so sánh sáu cột: có form đặt hàng, có hiện tồn kho, có chọn ngày, có tài khoản người dùng, số bước tới lúc chốt đơn, kênh liên hệ chính.
:::

## Nguyên tắc thiết kế

Bối cảnh dùng thật rất hẹp: khách mở web bằng điện thoại, khoảng 06:00 sáng ngày thi, máy vừa hỏng, đang lo mất môn, mạng yếu.

**1. Hỏi càng muộn càng tốt.** Grover cho khách đi hết luồng đặt rồi mới xác minh ở nền, và chỉ đòi giấy tờ khi hệ thống nghi ngờ [[ref:https://service.grover.com/hc/en-us/articles/19920531898642-How-does-Grover-s-credit-check-work]]. Hệ quả: màn hình đầu chỉ hỏi ngày thi, ca thi, điểm nhận. Căn cước và tiền dời sang bước 2 và bước 3.

**2. Mỗi lời hứa là một con số.** Turo công bố mốc tự hoàn cọc 80 giờ thay vì viết "sẽ hoàn sớm" [[ref:https://help.turo.com/en_us/security-deposits-us-HkbE44lE9]]. Hệ quả: "giao trước giờ thi 30 phút", "đổi máy trong 15 phút", "hoàn cọc trong 5 phút" nằm ngay chỗ khách đang lo, không giấu trong trang điều khoản như cách ngành trong nước ghi "hỗ trợ 24/7" [[ref:https://laptopsgn.com/cho-thue-laptop/]].

**3. Nói trước điều bất lợi.** Getaround bị Tổng Chưởng lý Washington DC xử lý vì không công bố rõ các trường hợp loại trừ [[ref:https://oag.dc.gov/release/attorney-general-schwalb-secures-refunds-dc]]; Fat Llama quảng cáo "bảo hiểm toàn phần" rồi từ chối bồi thường [[ref:https://www.trustpilot.com/review/fatllama.com]]. Hệ quả: khối "không được miễn trừ" nằm trong luồng thanh toán, có ô tích riêng tách khỏi ô điều khoản chung.

**4. Mượn từ vựng nhà trường.** Sinh viên Đại học FPT đã quen "Dashboard", "ĐK Mượn máy", "Trả máy" và bước chờ xác nhận [[ref:https://it-hcm.fpt.edu.vn/articles.php?news=huong-dan-muon-laptop-cua-sinh-vien-trong-truong&id=56]]. Hệ quả: giữ nguyên các nhãn đó, chi phí học gần bằng không.

**5. Một ngón tay cái, không có trạng thái cụt.** Luồng đặt phải bấm được bằng một tay khi đang xách cặp, nên nút chính dính đáy màn hình và biểu mẫu chỉ một cột. Mỗi tin xấu kèm một hành động: hết máy thì có nút báo khi có, máy lỗi giữa ca thi thì có nút gọi hỗ trợ khẩn kèm cam kết 15 phút [[ref:https://mitgroup.vn/cho-thue-laptop/]].

## Các màn hình chính

![Trang chủ với khẩu hiệu về ngày thi, hộp tra máy trống theo ca, bốn bước quy trình và ba nhóm máy kèm giá.](assets/screenshots/01-landing.png){w=16}{src: Nguồn: bản dựng nguyên mẫu của nhóm tác giả.}

Trang chủ đặt hộp tra cứu ngay dưới khẩu hiệu, gồm ba trường ngày thi, ca thi và nhu cầu, thay cho lối bán theo ngày và tháng của cả ngành [[ref:https://skylap.vn/dich-vu-cho-thue/cho-thue-laptop/]]. Khối bốn bước đặt trước danh mục máy, học theo cách Grover dựng trang "cách hoạt động" [[ref:https://www.grover.com/us-en/how-it-works]].

| Phần tử | Mục đích |
|---|---|
| Huy hiệu "Còn 6/10 máy hôm nay" | Biến tồn kho thành lý do hành động ngay |
| Hộp ngày thi, ca thi, nhu cầu | Bắt đầu bằng thứ khách đã biết chắc |
| Dòng "Không giữ CCCD" | Trả lời trước nỗi sợ lớn nhất |
{caption: Phần tử chính của trang chủ.}
{widths: 2,3}

![Màn hình tìm máy trống theo ca thi, cột bộ lọc bên trái và các thẻ máy kèm phần trăm pin, thời điểm kiểm tra, số máy còn lại.](assets/screenshots/02-catalog.png){w=16}{src: Nguồn: bản dựng nguyên mẫu của nhóm tác giả.}

Màn hình chỉ hiện máy thật sự đặt được trong ca đã chọn nên không bao giờ phải báo "hết máy" ở bước sau. Mỗi thẻ có phần trăm pin và giờ kiểm tra gần nhất, thay cho ảnh catalog chung chung của các trang trong nước [[ref:https://ictsaigon.com.vn/cho-thue-laptop-hp-elitebook-9480m]]. Máy bảo trì và máy dự phòng vẫn hiện nhưng bị khoá nút.

| Phần tử | Mục đích |
|---|---|
| Bộ lọc ca thi và điểm nhận | Khoá ngữ cảnh cho mọi kết quả phía sau |
| Dòng "Giữ chỗ tự động 10 phút" | Đặt kỳ vọng đúng về thời hạn giữ máy |
| Nhãn pin và giờ kiểm tra | Bằng chứng máy đã được chuẩn bị |
{caption: Phần tử chính của màn hình tìm máy trống.}
{widths: 2,3}

![Màn hình xác minh danh tính với ba ảnh căn cước và selfie, sáu dòng kết quả kiểm tra, hai cột dữ liệu có lưu và không lưu.](assets/screenshots/03-ekyc.png){w=16}{src: Nguồn: bản dựng nguyên mẫu của nhóm tác giả.}

Đây là bước duy nhất có thể làm khách chùn tay nên nhóm tách riêng và ghi rõ "chỉ làm một lần duy nhất". Sáu dòng kết quả hiện điểm số của từng phép kiểm tra: đọc mã MRZ, kiểm tra người sống, so khớp khuôn mặt [[ref:https://docs-vision.fpt.ai/ekyc/I-introduction/gioi-thieu/]] [[ref:https://docs-vision.fpt.ai/en/ekyc/IV-guides/comparing%20liveness%20methods/]]. Grover cũng đòi selfie thấy rõ đồng thời mặt người và giấy tờ [[ref:https://service.grover.com/hc/en-us/articles/35704298814866-Identity-Verification]].

| Phần tử | Mục đích |
|---|---|
| Câu "không giữ CCCD bản cứng" | Điểm khác biệt thương mại, đặt ngay đầu trang |
| Sáu dòng kết quả kèm điểm số | Cho thấy hệ thống làm gì với ảnh của khách |
| Hai cột có lưu và không lưu | Cam kết phạm vi dữ liệu cá nhân |
{caption: Phần tử chính của màn hình xác minh danh tính.}
{widths: 2,3}

![Màn hình đặt cọc với ba lựa chọn thanh toán, mã VietQR kèm nội dung chuyển khoản bắt buộc, ba ô tích điều khoản và bảng cơ chế cọc.](assets/screenshots/04-payment.png){w=16}{src: Nguồn: bản dựng nguyên mẫu của nhóm tác giả.}

Nhóm cố tình không bắt chước mẫu giữ tiền trên thẻ tín dụng, vì đó là tính năng của mạng thẻ [[ref:https://docs.stripe.com/payments/extended-authorization]] còn sinh viên Việt Nam gần như chỉ chuyển khoản và dùng ví. Thay vào đó là mã VietQR kèm nội dung chuyển khoản bắt buộc, hệ thống tự xác nhận khi có tín hiệu đối soát. Khối "cơ chế cọc" nói thẳng vì sao cọc chỉ bằng 4,0% giá trị máy.

| Phần tử | Mục đích |
|---|---|
| Đồng hồ "Giữ máy còn 08:42" | Giới hạn thời gian rõ ràng, không thúc ép mơ hồ |
| Nội dung chuyển khoản bắt buộc | Điều kiện để đối soát tự động |
| Bảng "hoàn cọc khi nào" | Công khai mức khấu trừ trước khi trả tiền |
{caption: Phần tử chính của màn hình đặt cọc và thanh toán.}
{widths: 2,3}

![Vé nhận máy với mã QR lớn, danh sách sáu việc đã làm để chuẩn bị máy, tiến trình đơn thuê sáu mốc và khối gọi hỗ trợ khẩn.](assets/screenshots/05-pass.png){w=16}{src: Nguồn: bản dựng nguyên mẫu của nhóm tác giả.}

Khách mở lại màn hình này nhiều nhất, thường lúc đang đi bộ tới sảnh, nên mã QR chiếm nửa trên và không cần thao tác nào để hiện ra. Danh sách chuẩn bị máy trả lời trước câu hỏi "máy này có chạy được bài thi không". Tiến trình sáu mốc kết thúc ở lần hoàn cọc tự động, đúng tinh thần công bố mốc bằng số của Turo [[ref:https://help.turo.com/en_us/security-deposits-us-HkbE44lE9]].

| Phần tử | Mục đích |
|---|---|
| Mã QR kèm chuỗi dự phòng | Quét nhanh, vẫn đọc tay được khi camera lỗi |
| Danh sách chuẩn bị máy | Chứng minh sản phẩm là máy sẵn sàng thi |
| Nút gọi hỗ trợ khẩn | Lối thoát khi máy lỗi giữa ca thi |
{caption: Phần tử chính của vé nhận máy.}
{widths: 2,3}

![Ứng dụng nhân viên trên điện thoại với biên bản kiểm tra bảy mục, sáu mục đã tích, và nút ký điện tử đang bị khoá.](assets/screenshots/06-staff.png){w=8}{src: Nguồn: bản dựng nguyên mẫu của nhóm tác giả.}

Ứng dụng chạy trên điện thoại vì việc bàn giao diễn ra ở sảnh, trong mười lăm phút cao điểm. Cần phân biệt hai danh mục dễ lẫn: **danh mục chuẩn bị máy mười hai mục** ở Phụ lục D chạy trong kho trước khi máy rời quầy, còn **biên bản kiểm tra bảy mục** trên màn hình này là phần đối chiếu tình trạng ngay lúc giao máy trước mặt khách. Bảy mục đó mở rộng từ danh mục kiểm tra khi thu hồi của Grover: màn hình, bàn phím, loa, camera, kết nối [[ref:https://www.grover.com/at-en/g-about/asset-condition]]. Quyết định đáng chú ý nhất: nút ký và giao máy bị khoá cho tới khi đủ bảy mục và đủ ảnh, và quy tắc chặn nằm ở tầng máy chủ chứ không chỉ ở giao diện.

| Phần tử | Mục đích |
|---|---|
| Thẻ khách kèm nhãn "Khớp" | Xác thực lại danh tính ở từng lượt giao dịch |
| Bộ đếm "6/7" trên biên bản | Biết còn thiếu gì mà không phải cuộn tìm |
| Nút bị khoá kèm lời giải thích | Biến quy tắc nghiệp vụ thành hướng dẫn thao tác |
{caption: Phần tử chính của ứng dụng nhân viên khi lập biên bản bàn giao.}
{widths: 2,3}

![Bảng điều khiển vận hành với bốn ô chỉ số, bảng đơn trong ngày, lưới lịch khai thác bảy ngày theo ba ca và danh sách cảnh báo.](assets/screenshots/07-dashboard.png){w=16}{src: Nguồn: bản dựng nguyên mẫu của nhóm tác giả.}

Bảng điều khiển trả lời đúng câu hỏi quản trị viên hỏi mỗi sáng: ca tới có gì phải lo. Lưới bảy ngày tới có mỗi hàng là một ca thi. Khối cảnh báo không dừng ở việc báo vấn đề mà nêu luôn bước kế tiếp, ví dụ đơn quá hạn 45 phút đã gửi hai tin nhắn và mốc khoá máy từ xa là 10:15.

| Phần tử | Mục đích |
|---|---|
| Bốn ô chỉ số có mũi tên so sánh | Nhìn một lần biết tình hình tốt hay xấu |
| Lưới ca thi bảy ngày | Phát hiện sớm ca sắp kín để mở máy dự phòng |
| Cảnh báo kèm bước kế tiếp | Rút ngắn khoảng cách giữa biết và làm |
{caption: Phần tử chính của bảng điều khiển vận hành.}
{widths: 2,3}

![Màn hình kho máy dạng bảng, mỗi hàng một thiết bị với mã tài sản, số sê-ri, trạng thái, nhóm, pin, đơn hiện tại, giờ check-in và số lượt thuê.](assets/screenshots/08-inventory.png){w=16}{src: Nguồn: bản dựng nguyên mẫu của nhóm tác giả.}

Màn hình này gần một phần mềm quản lý tài sản thuần tuý nhất, nên nhóm giữ dạng bảng và mượn mô hình định danh từng thiết bị bằng mã duy nhất [[ref:https://booqable.com/features/]] [[ref:https://github.com/grokability/snipe-it]]. Cột đáng chú ý nhất là giờ check-in của phần mềm quản lý thiết bị: máy im lặng quá 30 phút trong thời gian thuê sẽ tự sinh cảnh báo và bị chặn khỏi các lượt đặt kế tiếp.

| Phần tử | Mục đích |
|---|---|
| Mã tài sản và số sê-ri | Khớp với mã khắc laser trên vỏ máy |
| Cột pin và cột lượt thuê | Đầu vào cho quyết định bảo trì và thanh lý |
| Cột check-in thiết bị | Biến sự im lặng của một máy thành cảnh báo |
{caption: Phần tử chính của màn hình kho máy.}
{widths: 2,3}

![Chi tiết đơn thuê với dải trạng thái rút gọn còn tám chặng, nhật ký tám sự kiện có dấu thời gian, sáu khung ảnh hiện trạng và thẻ người thuê.](assets/screenshots/09-order.png){w=16}{src: Nguồn: bản dựng nguyên mẫu của nhóm tác giả.}

Màn hình này dùng khi có tranh chấp nên được thiết kế để đọc chứ không để sửa. Nhật ký ghi từng sự kiện kèm giờ, diễn giải và nguồn phát sinh, theo mô hình chỉ ghi thêm [[ref:https://deepwiki.com/grokability/snipe-it/4.4-activity-logging]]. Sáu ảnh hiện trạng lưu kèm mã băm SHA-256. Nút khoá máy từ xa nằm cuối cùng, màu cảnh báo, ghi rõ cần hai người duyệt.

| Phần tử | Mục đích |
|---|---|
| Dải trạng thái rút gọn còn tám chặng | Định vị đơn trong vòng đời chỉ bằng một cái liếc. Mười ba trạng thái kỹ thuật ở Chương 10 được gộp lại thành tám chặng khách và nhân viên nhìn thấy; các nhánh ngoại lệ chỉ hiện khi thực sự xảy ra |
| Nhật ký sự kiện có nguồn | Phân biệt việc do hệ thống, nhân viên hay cổng thanh toán làm |
| Nút khoá máy cần hai người duyệt | Không cá nhân nào tự khoá được máy của khách |
{caption: Phần tử chính của màn hình chi tiết đơn và nhật ký.}
{widths: 2,3}

![Báo cáo kinh doanh với bốn chỉ số, biểu đồ doanh thu và chi phí theo tháng, thanh tỉ lệ khai thác theo dòng máy và danh sách nguồn đơn.](assets/screenshots/10-report.png){w=16}{src: Nguồn: bản dựng nguyên mẫu của nhóm tác giả.}

Màn hình báo cáo được thiết kế để nói ra điểm yếu chứ không chỉ khoe điểm mạnh. Biểu đồ theo tháng hiện rõ ba đỉnh trùng ba kỳ thi cuối kỳ, kèm một câu ghi thẳng rằng doanh thu ngoài mùa thi thấp hơn nhiều và đó là rủi ro dòng tiền lớn nhất của mô hình.

| Phần tử | Mục đích |
|---|---|
| Bốn chỉ số có mũi tên xu hướng | Theo dõi doanh thu mỗi máy và tỉ lệ hư hỏng mỗi lượt |
| Biểu đồ doanh thu và chi phí | Nhìn thấy tính mùa vụ thay vì chỉ nghe nói |
| Thanh khai thác theo dòng máy | Quyết định mua thêm hay thanh lý từng dòng |
{caption: Phần tử chính của màn hình báo cáo kinh doanh.}
{widths: 2,3}

## Các tín hiệu tạo niềm tin

Khách giao một tài sản trị giá từ 6.500.000đ đến 10.000.000đ cho một nhóm sinh viên chưa có thương hiệu. Những chi tiết dưới đây tồn tại để rút ngắn khoảng cách đó.

| Tín hiệu | Vì sao có tác dụng |
|---|---|
| Ngày kiểm tra máy in trên từng thẻ máy | Biến lời hứa "máy sẵn sàng thi" thành mốc kiểm chứng được |
| Ảnh thật của chính chiếc máy sẽ giao | Đối thủ dùng ảnh catalog nên đây là điểm vượt rẻ nhất [[ref:https://ictsaigon.com.vn/cho-thue-laptop-hp-elitebook-9480m]] |
| Hai cột hao mòn thường và hư hỏng có phí | Cách Grover giảm tranh chấp là tách đôi và công khai [[ref:https://www.grover.com/at-en/g-about/asset-condition]] |
| Khối loại trừ trong luồng thanh toán, ô tích riêng | Bài học pháp lý từ vụ Getaround [[ref:https://oag.dc.gov/release/attorney-general-schwalb-secures-refunds-dc]] |
| Cam kết bằng số: 30 phút, 15 phút, 5 phút | Mô phỏng cách Turo công bố mốc 80 giờ [[ref:https://help.turo.com/en_us/security-deposits-us-HkbE44lE9]] |
| Bảng khấu trừ cọc hiện trước khi trả tiền | Không ai bị bất ngờ lúc trả máy |
| Số máy còn trống theo thời gian thực | Không đơn vị nội địa nào công bố con số này |
| Mức cọc gắn với hạng tín nhiệm hiển thị cho khách | Turo giảm cọc đổi lấy dữ liệu, nhóm giảm cọc đổi lấy lịch sử tốt [[ref:https://help.turo.com/en_us/security-deposits-us-HkbE44lE9]] |
| Câu "không giữ CCCD" lặp ở ba màn hình | Đối lập với việc đối thủ giữ giấy tờ và hỏi thông tin gia đình [[ref:https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html]] |
| Hai cột dữ liệu có lưu và không lưu | Cùng tinh thần công khai "phí của bạn dùng làm gì" của Hygglo [[ref:https://help.hygglo.info/en/articles/10415333-how-hygglo-works]] |
| Nhật ký đơn mở cho khách xem | Xác thực lặp lại ở từng giao dịch, không chỉ lúc đăng ký [[ref:https://www.miteksystems.com/blog/innovator-qa-mike-wilkins-senior-director-trust-safety-at-turo]] |
{caption: Mười một chi tiết giao diện có mục đích tạo niềm tin.}
{widths: 2,3}
{note: Ba điều tự cấm: không viết "cam kết 100%" mà thiếu danh sách loại trừ ngay cạnh; không quảng cáo giá mồi kiểu "chỉ từ 10k" [[ref:https://www.thuelaptop.vn/thue-laptop-da-nang-gia-re-chi-tu-10k/]]; không giấu điều khoản bất lợi ở cuối trang [[ref:https://saolatech.com.vn/bang-gia-thue-3425667]].}

## Khả năng tiếp cận và điều kiện thực tế

Các ngưỡng dưới đây là quy ước thiết kế của nhóm [Ước lượng của nhóm], chọn để dùng được bằng một tay, ngoài trời, lúc trời còn tối.

- **Cỡ chữ.** Thân bài tối thiểu 16 pixel, phụ chú không nhỏ hơn 13 pixel. Mọi con số tiền và mốc giờ dùng cỡ từ 18 pixel và in đậm.
- **Vùng bấm.** Mọi nút và ô tích có vùng chạm tối thiểu 44 × 44 pixel, cách nhau tối thiểu 8 pixel. Nút chính của mỗi bước dính đáy màn hình, chiếm trọn chiều ngang.
- **Tương phản.** Chữ thường đạt tỉ lệ tương phản tối thiểu 4,5 trên 1, chữ lớn và biểu tượng 3 trên 1. Trạng thái không bao giờ chỉ mã hoá bằng màu: ô "Quá hạn 45 phút" và ô "Đang thuê" đều có chữ kèm theo.
- **Mạng yếu.** Ứng dụng nhân viên là ứng dụng web tiến bộ: sáu ảnh hiện trạng lưu tạm trong IndexedDB rồi tự đẩy lên khi có sóng. Vé nhận máy nằm trong bộ nhớ đệm của service worker nên mở lại được khi mất mạng.
- **Khách không có dữ liệu di động.** Dưới mã QR luôn có chuỗi dạng `EL8241-5410-02` để nhân viên gõ tay. Mã đơn cũng gửi qua email và Zalo ngay khi xác nhận. Xấu nhất thì nhân viên tra bằng mã số sinh viên trên máy của mình, khách không cần chạm vào điện thoại.
