Mười hai mục dưới đây là danh mục đầy đủ của **mức chuẩn bị M2 — khôi phục ảnh chuẩn**, theo cách phân mức
ở Chương 5. Mức này áp dụng khi khách báo đã cài thêm phần mềm, khi tem niêm phong bị bóc, định kỳ mỗi năm
lượt thuê, và bắt buộc trước mỗi đợt thi cuối kỳ. Với khoảng 80% số lượt còn lại, máy đi theo **mức M1 —
quay vòng nhanh**, trong đó bước 3 được thay bằng khởi động lại để cơ chế đóng băng đưa phân vùng hệ thống về
trạng thái gốc, cộng xoá sạch phân vùng dữ liệu; mười một mục còn lại vẫn giữ nguyên. Dù ở mức nào, mười hai
mục đều là điều kiện để một chiếc máy được chuyển sang trạng thái *Sẵn sàng* trong hệ thống.
Phần mềm **không cho phép** bỏ qua mục nào: thiếu một mục là máy không xuất hiện trong danh sách cho thuê.
Người thực hiện ký tên điện tử và hệ thống ghi lại thời điểm, thiết bị, và người thao tác.

| # | Mục kiểm tra | Tiêu chuẩn đạt | Thời gian | Cách kiểm |
|---|---|---|---|---|
| 1 | Thu hồi và đối chiếu ảnh | Sáu ảnh sau khi thuê khớp sáu ảnh trước khi thuê, chênh lệch không quá cấp 1 | 3 phút | Ứng dụng nhân viên, so ảnh cạnh nhau |
| 2 | Kiểm phụ kiện | Đủ sạc, chuột, tai nghe có dây, túi chống sốc | 1 phút | Đếm tay, tích vào biểu mẫu |
| 3 | Xoá dữ liệu người thuê trước | Máy trở về đúng trạng thái gốc, không còn tài khoản hay tệp nào của người thuê trước | 2 phút (M1) · 20 phút (M2) | M1: khởi động lại cho cơ chế đóng băng khôi phục phân vùng hệ thống, rồi xoá phân vùng dữ liệu. M2: khôi phục ảnh gốc từ ổ cứng ngoài, đối chiếu mã băm |
| 4 | Kiểm tra sức khoẻ pin | Dung lượng thiết kế còn lại **từ 80% trở lên** | 2 phút | `powercfg /batteryreport` trên Windows |
| 5 | Cài và bật mã hoá ổ đĩa | BitLocker đang bật, khoá phục hồi đã lưu vào kho khoá | 3 phút | Kiểm tra trạng thái trong Windows |
| 6 | Cài tác nhân quản lý thiết bị | Tác nhân đang chạy, đã check-in về máy chủ trong 5 phút gần nhất | 2 phút | Bảng điều khiển quản trị hiển thị máy trực tuyến |
| 7 | Cài phần mềm thi | EOS Client giải nén **đúng thư mục quy định**, Safe Exam Browser đúng phiên bản lấy từ cổng thi của trường | 8 phút | Chạy thử một lượt, chụp màn hình lưu vào hồ sơ máy |
| 8 | Kiểm tra cổng và thiết bị ngoại vi | Jack 3.5mm phát được tiếng, webcam có hình, đủ cổng USB, bàn phím đủ phím | 3 phút | Chạy kịch bản kiểm tra chuẩn |
| 9 | Kiểm tra mạng | Kết nối được mạng không dây của trường, tốc độ đủ tải đề thi | 2 phút | Thử tải một tệp mẫu |
| 10 | Khoá cấu hình khởi động | Mật khẩu BIOS đã đặt, chặn khởi động từ USB, chặn thay đổi thứ tự khởi động | 3 phút | Vào BIOS kiểm tra |
| 11 | Vệ sinh và niêm phong | Máy sạch, tem tài sản còn nguyên, tem niêm phong ốc vỏ chưa vỡ | 4 phút | Mắt thường, chụp ảnh tem |
| 12 | Sạc đầy và cất vào tủ | Pin 100%, máy nằm đúng ô tủ sạc theo mã tài sản | 90 phút (song song) | Quét mã tài sản khi cất |
{caption: Danh mục chuẩn bị máy giữa hai lượt thuê, ghi theo mức M2. Tổng thời gian thao tác của người là khoảng 51 phút ở mức M2 và khoảng 22 phút ở mức M1, chưa kể thời gian sạc chạy song song.}
{widths: 0.5,3.4,4.6,1.2,3.3}
{note: Thời gian quay vòng mục tiêu là 90 phút cho mức M1 và 3 giờ cho mức M2, đúng bằng khoảng đệm cộng vào `inventory_holds.period` ở Chương 11. Trong tuần thi cao điểm, các máy dự phòng nóng giúp giữ nhịp này mà không làm chậm đơn nào.}

### Quy tắc không có ngoại lệ

1. **Không có đường tắt từ *Chờ vệ sinh* sang *Sẵn sàng*.** Mọi máy quay về đều phải đi qua bước 3, ở mức
   M1 hay mức M2 tuỳ tình huống, nhưng không bao giờ được bỏ qua. Đây là điều kiện để cam kết "xoá sạch dữ
   liệu người dùng trước" có giá trị thật chứ không phải khẩu hiệu.
2. **Máy dưới ngưỡng pin 80% không được cho thuê ca thi.** Máy đó chuyển sang hàng chờ bảo trì và chỉ
   dùng cho gói thuê tháng có ổ cắm cố định, cho tới khi thay pin.
3. **Ảnh chạy thử phần mềm thi phải mới hơn 7 ngày.** Phiên bản Safe Exam Browser có thể thay đổi theo
   thông báo của trường; một ảnh chạy thử cũ không chứng minh được máy còn thi được.
