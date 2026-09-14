Bài toán nói thẳng: giao một tài sản 6,5 đến 10 triệu đồng cho người lạ trong vài giờ, không có mặt để giám
sát, với giá thuê chưa tới một trăm nghìn. **Mất một máy nhóm A xoá sạch lợi nhuận của khoảng 59 lượt thuê.**

Nguyên tắc của ExamLap ngược với cách làm phổ biến: **cọc thấp, danh tính mạnh**, thay vì cọc cao và danh
tính yếu. Cụ thể, **không giữ căn cước, thẻ sinh viên hay bất kỳ giấy tờ tuỳ thân bản gốc nào** — vừa là
ranh giới pháp lý, vừa vì giữ giấy tờ không hề giúp thu hồi tài sản: thẻ căn cước không bán được, không phát
mại được, và người đã quyết định không trả máy thì vẫn xin cấp lại được.

## Năm lớp phòng thủ

| Lớp | Nội dung | Chặn được gì · không chặn được gì |
|---|---|---|
| **1. Sàng lọc đầu vào** | eKYC đối chiếu ảnh căn cước với khuôn mặt sống; bắt buộc email `@fpt.edu.vn` và mã số sinh viên; danh sách chặn nội bộ | Chặn người ngoài trường và người đã vi phạm. **Không** xác minh được giấy tờ là thật do cơ quan nhà nước cấp |
| **2. Ràng buộc kinh tế** | Cọc 300.000đ (giảm còn 150.000đ rồi 0đ theo điểm tín nhiệm), phí miễn trừ thiệt hại, **mất quyền dùng dịch vụ cả kỳ thi** | Chặn hành vi cẩu thả và tính toán ngắn hạn. Không chặn người quyết tâm lấy máy |
| **3. Bằng chứng** | Hợp đồng điện tử có chữ ký; biên bản bàn giao kèm 6 ảnh có mã băm SHA-256; nhật ký hệ thống chỉ ghi thêm | Tạo hồ sơ dùng được khi làm việc với cơ quan chức năng. Không ngăn được sự việc xảy ra |
| **4. Kiểm soát kỹ thuật** | MDM check-in mỗi 15 phút, khoá màn hình từ xa (hai người duyệt), BitLocker, mật khẩu BIOS, chặn khởi động USB, khắc laser mã tài sản, tem niêm phong vỡ | Làm máy khó bán lại. **Không** chặn được người tháo ổ cứng, gỡ pin CMOS hay tắt Wi-Fi |
| **5. Pháp lý** | Nhắc nợ bằng văn bản, rồi trình báo theo *Điều 175 Bộ luật Hình sự 2015* *[Cần kiểm chứng]* | Đường cuối cùng. Tốn thời gian, không nên là chỗ dựa chính |
{caption: Năm lớp phòng thủ, mỗi lớp kèm giới hạn của chính nó.}
{widths: 2.5,6,6}

Mục tiêu không phải làm cho việc lấy cắp **bất khả thi** — điều đó không tồn tại với tài sản di động — mà là
làm cho **kỳ vọng lợi ích của kẻ gian thấp hơn hẳn chi phí và rủi ro**, đồng thời giữ trải nghiệm của 99%
khách trung thực ở mức nhẹ nhàng.

## Ranh giới của việc theo dõi thiết bị

Phần mềm quản lý thiết bị trên máy cho thuê **chỉ được** báo trạng thái trực tuyến, báo vị trí gần đúng, và
khoá màn hình khi quá hạn. Nó **không** đọc nội dung tệp, không ghi thao tác bàn phím, không chụp màn hình,
không bật camera, và **không xoá dữ liệu do khách tạo ra**. Lệnh khoá chỉ khoá màn hình, hiển thị số điện
thoại liên hệ, và luôn cần hai người duyệt kèm ghi nhật ký. Điều khoản này được viết thành nghĩa vụ của bên
cho thuê trong hợp đồng, không phải một lời hứa miệng.

## Khi máy không được trả

Quy trình leo thang công bố trước: **15 phút** nhắn tin tự động và bắt đầu tính phí trễ · **60 phút** nhắc
lần hai kèm cảnh báo khoá · **2 giờ** gọi điện, khoá màn hình sau khi hai người duyệt · **24 giờ** gửi văn
bản yêu cầu trả tài sản · **48 giờ** kết xuất hồ sơ và trình báo.

## Dữ liệu cá nhân

| Có lưu | Không lưu |
|---|---|
| Số căn cước **đã băm SHA-256**, không lưu số gốc | Ảnh căn cước quá 90 ngày kể từ lượt thuê cuối |
| Họ tên, ngày sinh, mã số sinh viên | Mật khẩu tài khoản trường |
| Vector đặc trưng khuôn mặt và một ảnh chân dung độ phân giải thấp để nhân viên đối chiếu tại quầy | Vị trí GPS của người dùng |
| Bản ghi vị trí thiết bị chi tiết tối đa 24 giờ, sau đó ẩn danh hoá | Nội dung bài thi hay tệp của khách trên máy |
{caption: Dữ liệu ExamLap thu thập và không thu thập. Ảnh xác minh có hạn xoá tự động 90 ngày.}
{widths: 6,6}

Dữ liệu sinh trắc học thuộc nhóm nhạy cảm theo Nghị định 13/2023/NĐ-CP, nên phải có sự đồng ý tách bạch, hồ
sơ đánh giá tác động xử lý dữ liệu, và cơ chế cho khách tự tải về hoặc yêu cầu xoá.
