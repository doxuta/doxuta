## Bốn vai trò và ranh giới quyền hạn

ExamLap có bốn vai trò, không hơn. Mỗi vai trò được định nghĩa bằng **việc được phép làm**, không phải bằng chức danh. Nguyên tắc nền là: người chạm vào máy nhiều nhất lại là người có ít quyền trên hệ thống nhất, vì mọi thao tác sinh ra tiền hoặc sinh ra rủi ro pháp lý đều phải để lại dấu vết của ít nhất một người thứ hai.

| Vai trò | Ai đảm nhiệm | Việc chính | Ranh giới cứng |
|---|---|---|---|
| **Khách thuê** | Sinh viên Trường Đại học FPT Đà Nẵng, có email `@fpt.edu.vn` và mã số sinh viên | Đặt máy, xác minh eKYC một lần, thanh toán, nhận và trả máy, khiếu nại | Không xem được dữ liệu của khách khác; không tự huỷ đơn sau khi máy đã được gán và bàn giao |
| **Nhân viên giao nhận** | Cộng tác viên sinh viên, trả công theo giờ | Chuẩn bị máy, bàn giao, thu hồi, chấm hạng ngoại hình, lập biên bản | Không xem hồ sơ eKYC đầy đủ, không sửa giá, không hoàn tiền, không khoá máy |
| **Quản trị viên** | Thành viên nhóm sáng lập | Duyệt hồ sơ eKYC khó, cấu hình giá, xử lý sự cố và tranh chấp, đọc nhật ký kiểm toán | Không tự mình khoá máy hay xoá dữ liệu khách; không sửa biên bản đã ký |
| **Đối tác cung ứng và sửa chữa** | Cửa hàng laptop cũ và tiệm sửa tại Đà Nẵng | Cấp nguồn máy, bảo hành, báo giá và sửa chữa trong 24 giờ | Không có tài khoản trên hệ thống; nhận máy theo phiếu giao sửa có mã tài sản, không kèm dữ liệu khách hàng |
{caption: Bốn vai trò trong hệ thống vận hành của ExamLap và ranh giới quyền hạn của từng vai trò.}
{widths: 3,4,6,6}

Mô hình bốn vai trò này không phải phát minh của nhóm. Nghiên cứu vận hành chương trình cho mượn laptop của thư viện Đại học Arizona, chạy liên tục từ năm 2003 với hơn 300 thiết bị luân chuyển, kết luận rằng điều kiện sống còn là **phân công một người chuyên trách quản lý đội máy** kèm một bảng theo dõi từng thiết bị [[ref:https://journal.code4lib.org/articles/5876]]. Bộ phận IS&T của MIT cũng tách bạch rõ: người mượn ký điều khoản riêng, còn quyền thu giá trị thay thế thiết bị không trả thuộc về đơn vị quản lý chương trình [[ref:https://ist.mit.edu/loaner-equipment]].

Bảng dưới là ma trận quyền vận hành. **Có** là được phép, **Hai người** là chỉ chạy khi có người thứ hai phê duyệt, **Không** là chặn ở tầng máy chủ chứ không chỉ ẩn nút.

| Thao tác nhạy cảm | Khách | Nhân viên | Quản trị | Đối tác |
|---|---|---|---|---|
| Xem ảnh chân dung đã xác minh tại thời điểm bàn giao | Của mình | Có | Có | Không |
| Xem hồ sơ eKYC đầy đủ (ảnh CCCD, kết quả đối chiếu) | Của mình | Không | Có | Không |
| Gán một máy cụ thể cho một đơn | Không | Có | Có | Không |
| Đổi trạng thái máy sang bảo trì hoặc giao sửa | Không | Có | Có | Không |
| Sửa bảng giá, mức cọc, biểu phí trễ | Không | Không | Có | Không |
| Hoàn cọc trong hạn mức 300.000đ | Không | Không | Có | Không |
| Hoàn tiền ngoài phạm vi tiền cọc | Không | Không | Hai người | Không |
| Khoá màn hình máy từ xa | Không | Không | Hai người | Không |
| Xoá dữ liệu cá nhân của khách theo yêu cầu | Gửi yêu cầu | Không | Hai người | Không |
| Sửa hoặc xoá một biên bản đã ký | Không | Không | Không | Không |
{caption: Ma trận quyền hạn cho các thao tác nhạy cảm, áp dụng cho cả bốn vai trò.}
{widths: 7,2,2,2,2}
{note: Nhân viên giao nhận chỉ thấy ảnh chân dung để đối chiếu tại quầy, không thấy số CCCD và không tải được ảnh giấy tờ. Biên bản đã ký chỉ được đính chính bằng một biên bản mới tham chiếu tới bản cũ.}

:::warn Nguyên tắc hai người duyệt
Năm thao tác bắt buộc có hai người duyệt: khoá màn hình máy của khách, **thêm** một người vào danh sách chặn nội bộ, hoàn tiền ngoài phạm vi tiền cọc, khấu trừ vượt biểu phí công khai, và xoá dữ liệu cá nhân theo yêu cầu. Chiều ngược lại — gỡ khoá màn hình và gỡ một khách khỏi danh sách chặn — chỉ cần một người, theo nguyên tắc thất bại an toàn: gây hại cho khách phải khó hơn sửa sai. Danh sách này lặp lại y nguyên ở Chương 7 và Chương 8.
Mỗi lệnh ghi lại người yêu cầu, người duyệt, lý do và dấu thời gian vào nhật ký chỉ ghi thêm. Gỡ khoá chỉ cần một người, vì hệ thống phải nghiêng về phía trả quyền sử dụng lại cho khách.
Stanford cho thấy khoá máy từ xa là biện pháp đã được dùng thật trong môi trường đại học, với mốc quá hạn hai ngày làm việc [[ref:https://thehub.stanford.edu/borrow-equipment/loan-policies]]. Nhóm giữ công cụ đó nhưng đặt nó sau một cánh cửa hai khoá.
:::

## Quy trình chuẩn: chuẩn bị máy giữa hai lượt thuê

Sai lầm tốn kém nhất của một đội máy mới là cài lại toàn bộ hệ điều hành sau mỗi lượt thuê. Với mười máy, làm như vậy tốn khoảng sáu đến bảy giờ nhân công mỗi ngày thi, không đội sinh viên nào gánh nổi. ExamLap chia việc chuẩn bị thành ba mức và chỉ dùng mức nặng khi thật sự cần.

| Mức | Khi nào dùng | Nhân công mỗi máy | Tỉ lệ dự kiến |
|---|---|---|---|
| **M1 — Quay vòng nhanh** | Máy trả đúng hạn, tem niêm phong nguyên, không báo lỗi, cơ chế đóng băng phân vùng hệ thống hoạt động | khoảng 20 phút | khoảng 80% số lượt |
| **M2 — Khôi phục ảnh chuẩn** | Khách báo đã cài phần mềm, tem bị bóc, định kỳ mỗi 5 lượt, và bắt buộc trước mỗi đợt thi cuối kỳ | khoảng 40 phút | khoảng 18% |
| **M3 — Dựng lại từ đầu** | Nghi nhiễm mã độc, lỗi lạ, trước mỗi học kỳ, trước khi thanh lý máy | 4 đến 8 giờ, phần lớn là chờ | khoảng 2% |
{caption: Ba mức chuẩn bị máy và tỉ lệ áp dụng dự kiến.}
{widths: 4,8,3,3}
{note: Thời lượng là ước lượng kỹ thuật của nhóm [Ước lượng của nhóm], phải bấm giờ lại trên máy thật trong tháng vận hành đầu tiên.}

Quy trình chuẩn cho mức M1, mười hai bước, làm đúng thứ tự này:

1. **Tiếp nhận và đối chiếu** mã tài sản, số sê-ri và số tem niêm phong với biên bản bàn giao. 1 phút.
2. **Đếm phụ kiện**: củ sạc, tai nghe có dây 3.5mm, chuột, túi đựng. 1 phút.
3. **Chụp 6 ảnh hiện trạng** đúng sáu góc đã quy định, đẩy vào thư mục lượt trả. 2 phút.
4. **Chấm hạng ngoại hình theo thang A/B/C** ở bảng dưới, so với hạng lúc giao. 2 phút.
5. **Khởi động lại máy** để cơ chế đóng băng đưa phân vùng hệ thống về đúng bản gốc. 1 đến 3 phút.
6. **Xoá dữ liệu người dùng** ở phân vùng dữ liệu và xác nhận không còn tài khoản nào đăng nhập, không còn hồ sơ trình duyệt. 2 phút.
7. **Chạy danh mục kiểm tra chức năng 12 điểm**: màn hình, bàn phím, chuột cảm ứng, loa, micro, webcam, wifi, cổng USB, jack 3.5mm, cổng sạc, bản lề, quạt. 5 phút.
8. **Đo pin bằng `powercfg /batteryreport`** và ghi chỉ số sức khoẻ pin vào nhật ký máy. 2 phút.
9. **Kiểm tra EOS Client còn nằm đúng thư mục giải nén gốc và Safe Exam Browser đúng phiên bản**, rồi chạy thử trọn một vòng đăng nhập EOS và thoát sạch. 3 phút.
10. **Vệ sinh** bằng khăn sợi nhỏ và dung dịch chuyên dụng, lau kỹ bàn phím và chiếu nghỉ tay. 3 phút.
11. **Cắm sạc tới ít nhất 95%**, chạy song song với các bước trên. 30 đến 90 phút đồng hồ thực.
12. **Cập nhật nhật ký máy và chuyển trạng thái sang Sẵn sàng** trên hệ thống. 1 phút.

Tổng nhân công khoảng 22 phút. Tổng thời gian quay vòng thực tế, tính từ lúc khách trả máy tới lúc máy được đánh dấu Sẵn sàng, đặt mục tiêu **không quá 90 phút cho mức M1 và không quá 3 giờ cho mức M2**. Nút thắt không phải con người mà là **pin**: bước 11 quyết định tất cả, nên điểm trực phải có ổ cắm nhiều cổng và đủ củ sạc rời. Khi cần tăng công suất, mua thêm sạc rời rẻ hơn mua thêm máy nhiều lần.

Bước 9 là bước không được rút gọn. Tài liệu hướng dẫn của nhà trường nêu rõ tệp `EOSClient.exe` chỉ khởi động được khi nằm nguyên trong thư mục giải nén ban đầu [[ref:https://it.fpt.edu.vn/cantho/huong-dan-cai-dat-phan-mem-thi-eos-seb/]], nghĩa là một thao tác dọn dẹp vô hại của nhân viên cũng đủ làm hỏng cả ca thi của khách. Cấu trúc kiểm tra 12 điểm ở bước 7 được xây theo mẫu của Grover, nơi thiết bị trả về được kiểm tra từ mọi góc và thử toàn diện màn hình, Bluetooth, loa, camera và bàn phím trước khi quay lại kho cho thuê [[ref:https://www.grover.com/at-en/g-about/asset-condition]]. Grover cũng đặt **xoá sạch dữ liệu là bước thứ hai trong bốn bước tân trang**, ngay sau đánh giá tình trạng, đúng vị trí mà bước 6 chiếm trong quy trình này.

| Hạng | Tiêu chí đếm được, quan sát ở khoảng cách 30 cm | Dùng để làm gì |
|---|---|---|
| **A** | Tối đa 2 vết xước dài trên 5 mm, không vết nào dài quá 20 mm, không móp, không nứt, màn hình không điểm chết | Máy tuyến đầu: khách lần đầu, gói khẩn cấp, máy dự phòng nóng ngày thi |
| **B** | 3 đến 8 vết xước, hoặc tối đa 2 vết dài 20 đến 50 mm, móp nhẹ dưới 5 mm ở tối đa 2 vị trí, tối đa 1 điểm chết ngoài vùng trung tâm | Máy chủ lực, dùng bình thường cho mọi đơn |
| **C** | Trên 8 vết xước, hoặc có vết dài trên 50 mm, móp rõ từ 3 vị trí, nứt nhựa dưới 10 mm không xuyên thấu | Gói tuần và gói tháng, giảm giá 15% và ghi rõ trên web. Không dùng làm máy dự phòng nóng |
{caption: Thang chấm hạng ngoại hình có định lượng, thiết kế để hai người khác nhau chấm cùng một máy ra cùng một hạng.}
{widths: 2,9,6}
{note: Máy tụt xuống dưới hạng C ra khỏi đội cho thuê. Chấm hạng chỉ nói về ngoại hình: một máy đẹp nhưng liệt một phím không phải hạng A mà là máy lỗi.}

Hai lần chấm hạng trong một lượt thuê tạo ra bằng chứng: chênh lệch hạng giữa lúc giao và lúc nhận chính là định nghĩa vận hành của "có hư hỏng phát sinh". Nhóm áp dụng ranh giới hai tầng đã được Grover chứng minh là cách giảm tranh chấp mạnh nhất: **hao mòn bình thường thì doanh nghiệp chịu, sự kiện rời rạc thì khách chịu** [[ref:https://www.grover.com/at-en/g-about/asset-condition]]. Thêm một vài vết xước nhỏ sau nhiều lượt thuê không tính tiền. Móp mới, nứt mới, vỡ màn, vào nước mới tính tiền theo biểu phí công khai.

Cuối cùng, thời gian chuẩn bị phải được đưa thẳng vào bộ máy đặt lịch chứ không nằm trong đầu người trực. Phần mềm quản lý cho thuê Odoo gọi tham số này là *Security Time*, khoảng thời gian tính bằng giờ làm sản phẩm tạm thời không khả dụng giữa hai đơn thuê [[ref:https://www.odoo.com/documentation/18.0/applications/sales/rental.html]]. ExamLap đặt 90 phút cho quay vòng trong cùng một ngày thi, 12 giờ cho quay vòng qua đêm, 24 giờ sau một lượt thuê từ 7 ngày trở lên, và khoá thủ công không tự mở lại sau mọi lượt có báo sự cố.

## Quy trình bàn giao và thu hồi

Bàn giao là lúc duy nhất trong cả vòng đời đơn thuê mà nhóm nhìn thấy khách bằng mắt thường. Mục tiêu là **không quá 8 phút mỗi khách khi giao và không quá 6 phút khi nhận**, nhưng không được đánh đổi bằng việc bỏ bớt bằng chứng.

Các bước tại quầy khi giao máy:

1. Nhân viên **quét mã QR trên phiếu đặt** của khách. Ứng dụng mở thẳng biên bản bàn giao của đúng đơn đó, không phải tìm trong danh sách.
2. Màn hình hiện **ảnh chân dung đã xác minh trong hồ sơ eKYC**. Nhân viên **đối chiếu khuôn mặt người đang đứng trước mặt** với ảnh đó và bấm xác nhận đã đối chiếu. Nhân viên không thấy số CCCD và không tải được ảnh giấy tờ.
3. Mở máy và **chạy thử EOS cùng Safe Exam Browser trước mặt khách**, cho khách nhìn thấy màn hình đăng nhập hiện ra.
4. **Chụp 6 ảnh hiện trạng** ngay tại quầy: mặt A, mặt đáy, hai cạnh bên, màn hình đang bật nền trắng, và cụm phụ kiện trải ra. Mỗi ảnh được gắn mã băm SHA-256 và dấu thời gian.
5. Cùng khách **đếm phụ kiện**, tích từng món trên màn hình.
6. Khách đọc và **ký điện tử** trên biên bản, trong đó có ba ô tích riêng: hiểu mức phí trễ, hiểu các trường hợp không được miễn trừ thiệt hại, đồng ý điều khoản khoá máy từ xa khi quá hạn.
7. Thu tiền và tiền cọc, xuất biên nhận, chuyển trạng thái máy sang Đang cho thuê.
8. Nhắc miệng ba điều: giờ trả chính xác, số hotline, và câu quan trọng nhất là *có sự cố thì gọi ngay, đừng tự xử lý*.

:::warn Hệ thống chặn, không phải nhắc
Nút hoàn tất bàn giao bị khoá ở tầng máy chủ nếu thiếu bất kỳ điều kiện nào: chưa đủ 6 ảnh, chưa có chữ ký điện tử của khách, chưa tích ô đối chiếu khuôn mặt, hoặc chưa có kết quả chạy thử EOS.
Đơn không chuyển được sang trạng thái Đang cho thuê khi hồ sơ bàn giao chưa đủ. Cùng cơ chế đó áp dụng cho chiều thu hồi: chưa đủ 6 ảnh trả máy và chữ ký thì lệnh hoàn cọc không phát sinh được.
Đây là lý do kỹ thuật khiến cam kết hoàn cọc trong 5 phút vừa nhanh vừa an toàn: hệ thống chỉ hoàn tiền khi bộ bằng chứng đã khép kín.
:::

Khi nhận máy về, thứ tự đảo lại: đối chiếu mã tài sản và số tem, đếm phụ kiện, chụp 6 ảnh vào thư mục lượt trả, chấm hạng ngoại hình so với lúc giao, chạy nhanh danh mục 12 điểm, ghi phần trăm pin, khách ký phần thu hồi của biên bản, rồi xử lý cọc ngay tại chỗ. Nếu phát hiện hư hỏng, quy tắc cứng là **không tranh cãi tại quầy**: lập biên bản, chụp ảnh so sánh, hẹn gửi báo giá từ tiệm sửa đối tác trong 24 giờ. Đây chính là cấu trúc hai tầng trách nhiệm mà Rent the Runway dùng, trong đó hư hỏng nhẹ được bao gồm sẵn còn mất hoặc hỏng không sửa được thì khách chịu nguyên giá trị thay thế đã niêm yết [[ref:https://www.renttherunway.com/pages/termsofservice]].

![Ứng dụng dành cho nhân viên giao nhận, màn hình bàn giao với ô đối chiếu khuôn mặt, lưới sáu ảnh hiện trạng và vùng ký điện tử.](assets/screenshots/06-staff.png){w=9}{src: Nguồn: bản dựng nguyên mẫu do nhóm thiết kế, không phải ảnh chụp một hệ thống đang chạy.}

## Bố trí nhân lực theo mùa thi

Nhu cầu của ExamLap không trải đều. Một năm học của Trường Đại học FPT có ba học kỳ, kéo theo ba đỉnh thi cuối kỳ và ba đợt progress test. Kế hoạch nhân sự vì thế phải viết theo hai chế độ khác hẳn nhau.

| Hạng mục công việc | Ngày thường | Ngày thi cao điểm |
|---|---|---|
| Chuẩn bị máy giữa hai lượt | 0,5 giờ | 3,5 giờ |
| Giao máy | 0,3 giờ | 1,6 giờ |
| Thu hồi máy | 0,2 giờ | 1,2 giờ |
| Trực ứng cứu tại sảnh trong khung giờ thi | 0 giờ | 10,0 giờ |
| Quản lý đội máy, đối soát tiền, trả lời tin nhắn | 0,5 giờ | 1,5 giờ |
| **Tổng nhân công một ngày** | **khoảng 1,5 giờ** | **khoảng 18 giờ** |
{caption: Khối lượng công việc một ngày thường so với một ngày thi cao điểm, tính cho đội 10 máy và khoảng 12 lượt thuê một ngày cao điểm.}
{widths: 8,3,3}
{note: [Ước lượng của nhóm], suy ra từ định mức 20 phút chuẩn bị, 8 phút giao và 6 phút thu hồi mỗi lượt. Giờ trực ứng cứu phần lớn là thời gian chờ, nên người trực kiêm luôn việc chuẩn bị máy tại chỗ.}

Từ bảng trên suy ra lịch ca. **Ngày thường** cần đúng một người, trực theo lịch hẹn, khoảng một tiếng rưỡi. **Ngày thi cao điểm** chia làm ba ca. Ca sáng 06:00 đến 11:30 cần hai người, vì đây là khung dồn cả việc giao máy trước ca thi đầu tiên lẫn việc trực ứng cứu: một người đứng quầy, một người ôm bộ ứng cứu. Ca chiều 11:30 đến 17:00 chỉ cần một người, do quầy giao nhận và điểm đặt máy dự phòng nóng là cùng một chỗ ở sảnh. Ca tối 17:00 đến 19:00 cần một người để thu hồi nốt và chuẩn bị máy cho hôm sau.

Cách bố trí đó có một đánh đổi phải nói rõ: trong ca chiều, khi người trực rời sảnh để đi đổi máy, quầy giao nhận tạm dừng tối đa 15 phút. Nhóm chấp nhận đánh đổi này vì cam kết đổi máy luôn được ưu tiên trước việc nhận máy trả, và vì lượng đơn buổi chiều thấp hơn buổi sáng.

Đơn giá dùng cho dự toán lấy từ mặt bằng thị trường Đà Nẵng. Công việc phục vụ và bán hàng bán thời gian tại Đà Nẵng được trả **20.000đ đến 35.000đ mỗi giờ**, còn cộng tác viên sự kiện được trả **150.000đ đến 500.000đ mỗi ngày** [[ref:https://vn.joboko.com/blog/luong-part-time-nwi5750]] [[ref:https://careerviet.vn/viec-lam/parttime-tai-da-nang-kl511-vi.html]]. Nhóm chốt **25.000đ đến 30.000đ mỗi giờ** cho cộng tác viên giao nhận và **150.000đ đến 250.000đ mỗi ngày** cho ca trực cao điểm trọn ngày, tức nửa dưới của dải cộng tác viên sự kiện.

Sàn pháp lý phải được kiểm tra trước khi ký bất kỳ thoả thuận nào. Theo Nghị định 293/2025/NĐ-CP có hiệu lực từ 01/01/2026, lương tối thiểu giờ là **22.700đ với vùng II**, 20.000đ với vùng III và 17.000đ với vùng IV, mức tăng chung 7,2% [[ref:https://luatvietnam.vn/lao-dong-tien-luong/muc-luong-toi-thieu-vung-tai-thanh-pho-da-nang-nam-2026-562-105277-article.html]] [[ref:https://thuvienphapluat.vn/phap-luat-doanh-nghiep/bai-viet/muc-luong-toi-thieu-vung-thanh-pho-da-nang-tu-01-01-2026-15957.html]] [[ref:https://xaydungchinhsach.chinhphu.vn/de-xuat-muc-luong-toi-thieu-vung-tu-1-1-2026-119250718084713755.htm]]. Thành phố Đà Nẵng trải trên cả ba vùng tuỳ địa bàn cấp xã và phường, và nhóm **chưa xác minh được phường Hoà Hải thuộc vùng nào** [Cần kiểm chứng]. Vì vậy mô hình lấy 22.700đ mỗi giờ làm sàn an toàn, và mức 25.000đ đến 30.000đ của nhóm nằm trên sàn đó.

| Chế độ | Ca | Người mỗi ca | Giờ công một ngày | Chi phí một ngày |
|---|---|---|---|---|
| Ngày thường | 1 ca theo lịch hẹn | 1 | 1,5 | 38.000đ đến 45.000đ |
| Ngày thi cao điểm | sáng 5,5 giờ · chiều 5,5 giờ · tối 2 giờ | 2 · 1 · 1 | 18,5 | 463.000đ đến 555.000đ |
{caption: Lịch ca và chi phí nhân công theo hai chế độ vận hành.}
{widths: 4,3,3,3,4}
{note: Chi phí tính ở mức 25.000đ đến 30.000đ mỗi giờ. Đây là chi phí nếu thuê ngoài toàn bộ; trên thực tế năm 1 phần lớn số giờ này do ba thành viên sáng lập đảm nhiệm và không tính lương.}

:::risk Điểm yếu thật của mô hình nhân sự năm 1
Mô hình tài chính đặt biến phí **27.600đ mỗi lượt thuê**, nhân với 382 lượt của năm 1 ra **10.543.200đ** cho toàn bộ nhân công cộng tác viên, chi phí giao nhận và vật tư tiêu hao. Con số đó chỉ đủ trả khoảng 300 giờ công cộng tác viên ở mức 30.000đ mỗi giờ.
Trong khi đó tổng nhu cầu nhân công năm 1 vào khoảng **900 giờ** [Ước lượng của nhóm], gồm khoảng 610 giờ của 33 ngày thi cao điểm và khoảng 300 giờ rải trên các ngày thường. Phần chênh khoảng 600 giờ do ba thành viên sáng lập gánh mà không nhận lương. Quy ra chi phí cơ hội ở đúng đơn giá cộng tác viên, 600 giờ tương đương **18.000.000đ**, tức **lớn hơn toàn bộ lợi nhuận sau thuế 14.442.672đ** của năm 1.
Nói thẳng: **nếu tính đủ công sức của nhóm theo giá thị trường thì năm đầu tiên dự án chưa thực sự có lãi.** Đây là lý do năm 2 phải nâng số lượt thuê trên mỗi máy chứ không chỉ nâng số máy, và là lý do mọi phút rút ngắn được ở quy trình chuẩn bị đều là tiền thật.
:::

Chi phí giao nhận cũng cần được quản như một khoản nhân công. Giao một chiều bằng dịch vụ xe máy nội thành có giá khoảng 18.000đ đến 23.000đ cho bốn ki-lô-mét đầu, tức 36.000đ đến 46.000đ cho một vòng giao và thu hồi [[ref:https://topkinhdoanh.net/bang-gia-ahamove/]] [[ref:https://ahamove.com/giao-hang-tieu-chuan-la-gi]]. So với giá một ca thi 79.000đ, thuê ngoài việc giao nhận sẽ ăn hết biên lợi nhuận. Vì vậy trong năm 1 nhóm tự giao bằng xe máy trong bán kính quanh phường Hoà Hải, và chỉ gói **ca thi khẩn cấp 179.000đ** mới bao gồm giao tận cổng trường.

## Xử lý sự cố trong giờ thi

Đây là kịch bản mà toàn bộ phần còn lại của chương này tồn tại để phục vụ. Cam kết công khai là **đổi máy trong 15 phút nếu máy lỗi giữa ca thi**. Dưới đây là cách 15 phút đó được tiêu.

| Mốc | Việc | Ai làm |
|---|---|---|
| Phút 0 đến 1 | Bắt máy hotline trong 60 giây. Hỏi đúng ba câu: đang ở phòng nào, máy bị gì, ca thi kết thúc lúc mấy giờ | Người trực ứng cứu |
| Phút 1 đến 3 | Phân loại. Nếu là lỗi sửa được dưới 3 phút qua điện thoại thì hướng dẫn và gọi lại xác nhận. Nếu không, dừng chẩn đoán ngay lập tức | Người trực ứng cứu |
| Phút 3 đến 5 | Cầm bộ ứng cứu đã đóng sẵn gồm máy dự phòng nóng, củ sạc, tai nghe, chuột, rời điểm trực | Người trực ứng cứu |
| Phút 5 đến 9 | Di chuyển trong khuôn viên tới phòng thi, xin phép cán bộ coi thi | Người trực ứng cứu |
| Phút 9 đến 13 | Đặt máy thay thế đã bật sẵn và đã đăng nhập, mở Safe Exam Browser giúp khách, xác nhận khách vào lại được bài thi | Người trực ứng cứu |
| Phút 13 đến 15 | Ký biên bản đổi máy khẩn một mặt giấy trong 60 giây, mang máy lỗi về và khoá trạng thái máy đó lại | Người trực ứng cứu và khách |
{caption: Phân bổ 15 phút của quy trình đổi máy khẩn trong ca thi.}
{widths: 3,10,4}

Quy tắc vàng của quy trình này là **không sửa máy trong giờ thi**. Khi đồng hồ phòng thi đang chạy, mỗi phút dùng để chẩn đoán là một phút khách mất bài. Đổi máy trước, sửa sau. Đó cũng là lý do duy nhất máy dự phòng nóng tồn tại.

Máy dự phòng nóng không nằm trong kho. Nó nằm trong ba lô, ngay sảnh toà nhà có phòng thi, pin 100%, đã bật sẵn, đã đăng nhập tài khoản cục bộ dùng cho thí sinh, và **đã chạy thử EOS cùng Safe Exam Browser sáng hôm đó**. Chỉ máy hạng A hoặc hạng B mới được làm máy dự phòng nóng: khách đang hoảng loạn mà nhận một chiếc máy xấu là trải nghiệm tệ nhất có thể tạo ra.

Cam kết 15 phút chỉ khả thi khi đủ **năm điều kiện**, và nhóm nêu thẳng cả năm trong hợp đồng:

1. Có người trực **tại chỗ** suốt khung giờ thi, không phải gọi thì chạy tới.
2. Máy dự phòng nóng đặt ngay sảnh, pin đầy, đã chạy thử sáng hôm đó.
3. Phạm vi địa lý **giới hạn trong khuôn viên trường**.
4. Một số hotline duy nhất, in trên phiếu của mọi khách, có người cầm máy.
5. Biên bản đổi máy khẩn rút gọn một mặt giấy, ký trong 60 giây, không làm lại hợp đồng.

:::warn Khi nào cam kết 15 phút KHÔNG áp dụng
Ngoài khuôn viên trường. Ngoài khung giờ trực đã công bố, tức từ một giờ trước ca thi đầu tiên tới một giờ sau ca thi cuối cùng của ngày đó. Khi số máy hỏng cùng lúc vượt số máy dự phòng nóng đang có. Khi cán bộ coi thi không cho phép mang thiết bị vào phòng, đây là quyền của nhà trường và nằm ngoài tầm kiểm soát của nhóm.
Rủi ro nguy hiểm nhất lại không nằm trong danh sách trên: nếu bản ảnh hệ điều hành chuẩn có lỗi, ví dụ phiên bản Safe Exam Browser không khớp bản trường vừa cập nhật, thì không phải 2% máy hỏng mà **100% máy hỏng cùng lúc**, và máy dự phòng cũng hỏng y hệt vì dùng chung bản ảnh. Hai biện pháp chặn: chạy thử trên hai máy ngẫu nhiên trước ca thi đầu tiên mỗi đợt, và luôn giữ một máy dự phòng chạy **bản ảnh phiên bản trước**.
:::

Thị trường hiện không có ai cạnh tranh ở mức cam kết này. Đơn vị nhanh nhất tìm được trên toàn quốc cam kết giao trong vòng **2 giờ** và chỉ ở nội thành Thành phố Hồ Chí Minh [[ref:https://laptopsgn.com/tin-tuc/dich-vu-cho-thue-laptop-tphcm-gia-re-giao-2h/]]. Tại Đà Nẵng, cam kết tốt nhất chỉ là **giao trong ngày** [[ref:https://truonggiang.vn/cho-thue-laptop.html]] [[ref:https://mitgroup.vn/cho-thue-laptop/]]. Một đơn vị có cam kết đổi máy nếu hư hỏng trong lúc sử dụng nhưng không gắn con số thời gian nào vào lời hứa đó [[ref:https://danang.plus/thue-laptop/]]. Với ca thi bắt đầu lúc 07:30, "trong ngày" là vô nghĩa. Việc các trường nước ngoài đặt tên riêng cho loại nhu cầu này, như chương trình *Emergency Laptop Loan* của Đại học Michigan Flint, xác nhận sự cố thiết bị sát giờ là một hạng mục nhu cầu độc lập chứ không phải trường hợp hiếm [[ref:https://www.umflint.edu/ellp/]].

## Quản lý đội máy và bảo trì

Đội máy năm 1 gồm 10 máy, năm 2 lên 16 máy. Ở quy mô này, mỗi máy hỏng là 10% năng lực biến mất, nên bảo trì phải là lịch chứ không phải phản ứng.

![Vòng đời một thiết bị trong đội máy ExamLap, nhắc lại từ Chương 10 để đối chiếu với lịch bảo dưỡng và quy tắc thanh lý bên dưới.](assets/diagrams/03-vong-doi-thiet-bi.png){w=13}{src: Nguồn: nhóm tác giả.}

Pin là bộ phận duy nhất chắc chắn hỏng dần không thể đảo ngược, và là bộ phận duy nhất mà hỏng giữa ca thi thì máy dự phòng cũng không cứu kịp. Sức khoẻ pin được đo bằng lệnh `powercfg /batteryreport` có sẵn trong Windows, lấy tỉ số giữa dung lượng sạc đầy hiện tại và dung lượng thiết kế [Cần kiểm chứng: nhóm phải tự chạy một lần để xác nhận cú pháp và tên các trường trong báo cáo].

| Sức khoẻ pin đo được | Được làm gì | Hành động bắt buộc |
|---|---|---|
| Từ 90% trở lên | Mọi gói, kể cả máy dự phòng nóng ngày thi | Đo lại mỗi 3 tháng |
| 80% đến 89% | Mọi gói thuê theo ca thi | Đo lại mỗi 2 tháng |
| 70% đến 79% | **Không cho thuê ca thi.** Chỉ dùng cho gói tuần và gói tháng có ổ cắm cố định | Đo lại mỗi tháng, lên kế hoạch thay pin |
| 60% đến 69% | Rút khỏi tuyến thi, chỉ cho thuê tuần và tháng, ghi rõ "pin yếu" trên web | Xin báo giá thay pin |
| Dưới 60% | Dừng cho thuê | Thay pin hoặc chuyển sang thanh lý |
{caption: Ngưỡng sức khoẻ pin và hành động tương ứng. Ngưỡng nhận máy mới vào đội là từ 80% trở lên.}
{widths: 4,7,5}
{note: [Ước lượng của nhóm]. Phần trăm một mình là chỉ số gây hiểu nhầm, vì 75% trên viên pin thiết kế lớn vẫn dài hơn 90% trên viên pin nhỏ. Mỗi máy phải vượt bài đo thời lượng thực tối thiểu 3,5 giờ chạy liên tục Safe Exam Browser ở độ sáng 50% và bật wifi.}

Lịch bảo dưỡng cố định: đo pin theo tần suất ở bảng trên, khôi phục ảnh chuẩn định kỳ mỗi 5 lượt thuê và bắt buộc trước mỗi đợt thi cuối kỳ, dựng lại từ đầu mỗi học kỳ một lần cho toàn đội, vệ sinh sâu bao gồm hút bụi quạt tản nhiệt mỗi 6 tháng. Máy nằm kho quá một tuần giữ pin ở khoảng 50% đến 60% chứ không để đầy và cũng không để cạn.

Quy tắc thanh lý gồm bốn điều kiện, chạm một điều kiện là kích hoạt xem xét: hạng ngoại hình tụt xuống dưới C, pin dưới 60% mà chi phí thay không đáng, đã có từ ba sự cố trở lên trong sáu tháng, hoặc **chi phí một lần sửa vượt 40% giá trị còn lại của máy**. Giá trị còn lại tính theo đường hao mòn kinh tế khoảng **2,17% mỗi tháng**, ứng với vòng đời vận hành **30 tháng** và giá trị thu hồi 35% [Ước lượng của nhóm], đúng bằng giả định khấu hao 1.571.000đ mỗi tháng của mô hình tài chính ở Chương 15. Đường mất giá này khớp với mô tả thị trường: laptop mất giá nhanh nhất trong năm đầu rồi ổn định dần nếu được giữ gìn, và máy cũ dòng doanh nghiệp rẻ hơn máy mới cùng phân khúc khoảng 30% đến 50% [[ref:https://macvn.com.vn/dinh-gia-laptop-cu/]] [[ref:https://laptops.vn/review/laptop-thinkpad-cu-gia-re/]].

Áp vào một máy nhóm A mua 6.500.000đ: sau 18 tháng giá trị còn lại khoảng 3.965.000đ nên ngưỡng sửa là 1.586.000đ; sau 30 tháng giá trị còn lại đúng bằng mức thanh lý 2.275.000đ nên ngưỡng sửa chỉ còn khoảng 910.000đ. Con số đó có ý nghĩa thực tế ngay: thay pin dòng Dell Latitude được báo ở dải **1.200.000đ đến 2.500.000đ** [[ref:https://lacviet.vn/en/thay-pin-laptop-dell]], còn thay màn hình 11 đến 14 inch ở mặt bằng chung là **1.500.000đ đến 3.000.000đ** [[ref:https://bcavn.com/tin-tuc/thay-man-hinh-laptop-bao-nhieu-tien-30474.html]]. Nghĩa là một máy 30 tháng tuổi bị vỡ màn hoặc chai pin nặng thì **thanh lý rẻ hơn sửa**. Ngược lại, thay bàn phím từ 350.000đ và lấy trong một giờ [[ref:https://fastcare.vn/thay-ban-phim-laptop]] gần như luôn đáng sửa. Riêng khoản pin cần lưu ý khi chọn model: có dòng pin rời tháo được trong 30 giây, giảm hẳn thời gian máy nằm chờ so với dòng pin liền.

Tỉ lệ máy dự phòng đặt theo quy tắc **khoảng 10% số máy đang cho thuê, tối thiểu 2 máy, cộng một máy chạy bản ảnh phiên bản trước**. Với đội 10 máy, nhóm giữ tối đa 8 máy cho thuê cùng lúc và 2 máy dự phòng nóng. Phép tính nhị thức với xác suất sự cố mỗi máy mỗi ngày là 2% cho thấy: ngay cả khi cả 10 máy đều đang trên tay khách, xác suất hỏng từ 2 máy trở lên trong cùng một ngày chỉ khoảng 1,6% [Ước lượng của nhóm]. Với mức tối đa 8 máy cho thuê cùng lúc, rủi ro còn thấp hơn nữa, nên 2 máy dự phòng là đủ, với điều kiện các sự cố độc lập với nhau.

:::note Ghi chú kế toán về đội máy
Theo Thông tư 45/2013/TT-BTC, tài sản chỉ được ghi nhận là tài sản cố định khi nguyên giá từ 30.000.000đ trở lên [[ref:https://docs.kreston.vn/vbpl/chi-phi-tai-chinh/tai-san-co-dinh/thong-tu-45-2013-tt-btc/]]. Máy của ExamLap có đơn giá 6.500.000đ đến 10.000.000đ nên về mặt thuế là công cụ dụng cụ, không phải tài sản cố định.
Mô hình tài chính của nhóm vẫn trích khấu hao kinh tế 1.571.000đ mỗi tháng để tính đúng điểm hoàn vốn. Hai cách trình bày khác nhau và nhóm nêu rõ cả hai để tránh bị phản biện.
:::

## Các chỉ số vận hành phải theo dõi

Nhóm theo dõi mười chỉ số, cập nhật hằng tuần vào một bảng in ra dán tường. Ngưỡng tốt và ngưỡng báo động dưới đây là ngưỡng quản trị nội bộ do nhóm đặt, không phải chuẩn ngành.

| Chỉ số | Cách tính | Tần suất | Ngưỡng tốt | Ngưỡng báo động |
|---|---|---|---|---|
| Tỉ lệ khai thác theo thời gian | ngày-máy đang cho thuê chia ngày-máy khả dụng | Tuần | từ 40% | dưới 25% |
| Tỉ lệ sẵn sàng | ngày-máy sẵn sàng chia ngày-máy sở hữu | Tuần | từ 95% | dưới 90% |
| Thời gian quay vòng mức M1 | trung bình từ lúc nhận máy tới lúc đánh dấu Sẵn sàng | Tuần | không quá 90 phút | trên 150 phút |
| Số lượt thuê mỗi máy mỗi tháng | tổng lượt chia số máy | Tháng | từ 4 lượt | dưới 2 lượt |
| Tỉ lệ giao đúng giờ | lượt giao trước giờ cam kết chia tổng lượt | Mỗi đợt thi | 100% | dưới 97% |
| Tỉ lệ sự cố trên 100 lượt | số ca thi có sự cố chia tổng lượt nhân 100 | Mỗi đợt thi | 0 | từ 2 vụ một đợt thi |
| Tỉ lệ đạt cam kết đổi máy 15 phút | lần đổi đúng hạn chia tổng lần đổi | Mỗi đợt thi | 100% | dưới 90% |
| Tỉ lệ trả trễ | lượt trả sau giờ cam kết chia tổng lượt | Tuần | không quá 5% | trên 12% |
| Tỉ lệ hoàn cọc đúng hạn 5 phút | lượt hoàn cọc trong 5 phút chia tổng lượt | Tuần | từ 98% | dưới 95% |
| Tỉ lệ hư hỏng có tính phí | lượt phát sinh hư hỏng phải tính tiền chia tổng lượt | Tháng | không quá 3% | trên 8% |
{caption: Mười chỉ số vận hành, cách tính và ngưỡng đèn báo.}
{widths: 5,7,2,3,3}
{note: Mẫu số của tỉ lệ khai thác là ngày-máy KHẢ DỤNG, không phải ngày-máy sở hữu. Máy đang chờ sửa phải bị trừ khỏi mẫu số, nếu không một đội máy hỏng nhiều sẽ trông như đội máy ế khách.}

Chỉ số **tỉ lệ sự cố ngày thi** là chỉ số chất lượng quan trọng nhất và ngưỡng của nó là 0. Thứ ExamLap bán không phải một chiếc laptop mà là sự chắc chắn vào được phòng thi. Một sự cố phá huỷ toàn bộ lời hứa đó, và trong một cộng đồng khép kín cỡ một campus, tin xấu lan nhanh hơn mọi hoạt động truyền thông.

Về benchmark ngành, nhóm nói thẳng một điều bất lợi: **không tìm được bộ chuẩn nào đáng tin cho ngành cho thuê thiết bị**. Nguồn duy nhất có con số cụ thể cho rằng tỉ lệ sử dụng thực tế năm đầu của ngành cho thuê thiết bị thường ở mức **35% đến 45%**, chứ không phải 80% như các nhà cung cấp quảng cáo [[ref:https://www.natejonesentrepreneur.com/post/equipment-rental-business-startup-costs]]. Đây là một blog khởi nghiệp cá nhân, không phải báo cáo ngành, nên nhóm dùng nó làm mốc thận trọng chứ không làm mục tiêu [Cần kiểm chứng]. Mô hình tài chính của ExamLap đặt tỉ lệ khai thác bình quân năm 1 ở mức **42%**, nằm trong khoảng đó.

Ba mốc tham chiếu đáng tin hơn đến từ Rent the Runway, doanh nghiệp có cấu trúc bài toán giống hệt là tài sản đắt tiền cho thuê ngắn hạn rồi phục hồi để cho thuê tiếp. Số lượt thuê để hoàn vốn một món là **17 đến 18 lượt** trong khi thực tế đạt khoảng **20 lượt**, tức biên an toàn chỉ 2 đến 3 lượt [[ref:https://gadallon.substack.com/p/rent-the-runway-when-complexity-collides]]. Doanh nghiệp này hướng tới **quay vòng trong ngày** và duy trì vòng quay dưới một tuần nhờ theo dõi dữ liệu vị trí và tình trạng của từng món [[ref:https://d3.harvard.edu/platform-rctom/submission/rent-the-runway-digitizes-high-fashion/]] [[ref:https://www.renttherunway.com/about-us/process]]. Và sau khi lần đầu có lãi theo quý, việc đầu tiên họ làm là **cắt mạnh đầu tư mua thêm hàng** [[ref:https://investors.renttherunway.com/news-releases/news-release-details/rent-runway-inc-announces-fourth-quarter-and-full-year-2025]]. Bài học chuyển thẳng vào ExamLap: chỉ số bắc đẩu là **số lượt thuê trên mỗi máy mỗi tháng**, không phải số máy trong kho.

Ngưỡng cho tỉ lệ trả trễ và mốc chuyển trạng thái từ trễ sang mất được neo theo thông lệ thư viện đại học, nơi mốc rất khác nhau: 7 ngày ở Northern Illinois University [[ref:https://library.niu.edu/university-libraries/about/policies/laptopcirculation.shtml]], trên 34 ngày ở University of Connecticut [[ref:https://library.uconn.edu/?p=967]]. Nguyên tắc chung rút ra được là phạt trễ theo giờ với hợp đồng ngắn và **luôn có trần phạt**, như mức 0,10 USD mỗi phút với trần 30 USD mỗi máy của University of Kansas [[ref:https://services.ku.edu/TDClient/818/Portal/KB/Article/20717/KU-Libraries-Fines-Fees-Lost-Item-and-Damage-Charges-for-Library-Equipment-and-Accessories-Laptops-H]]. ExamLap đi theo đúng logic đó với phí trễ 20.000đ mỗi 30 phút, trần 200.000đ mỗi ngày, và mốc chuyển sang xử lý mất máy ở **48 giờ** (quy trình năm mốc đầy đủ ở Chương 6 và Phụ lục B), ngắn hơn hẳn mức 7 đến 34 ngày của các trường vì vòng quay của dịch vụ tính bằng giờ chứ không bằng học kỳ.

:::ok Kết luận của chương
Vận hành của ExamLap gói gọn trong bốn con số phải giữ bằng được: **22 phút** nhân công chuẩn bị một máy, **90 phút** quay vòng từ lúc nhận tới lúc sẵn sàng, **8 phút** bàn giao tại quầy, và **15 phút** đổi máy khi sự cố xảy ra giữa ca thi.
Ba con số đầu quyết định chi phí. Con số thứ tư quyết định việc khách có quay lại hay không, và nó chỉ khả thi khi có người trực tại chỗ cùng hai máy dự phòng nóng đã chạy thử trong ngày.
Điểm yếu lớn nhất của chương này đã được nêu thẳng: năm 1 chỉ chạy được nếu ba thành viên sáng lập bỏ vào khoảng 600 giờ công không tính lương. Kế hoạch năm 2 vì thế đặt trọng tâm vào việc tăng số lượt thuê trên mỗi máy, không phải tăng số máy.
:::
