Một mã nguồn, ba giao diện: web cho sinh viên, ứng dụng web chạy trên điện thoại cho nhân viên giao nhận, và
bảng điều khiển cho quản trị viên. Quy mô 382 lượt thuê một năm và một nhóm bốn đến năm người **không** biện
minh được cho kiến trúc vi dịch vụ.

## Kiến trúc

<<<landscape>>>

![Kiến trúc hệ thống: người dùng, lớp biên, ứng dụng, dữ liệu và các dịch vụ ngoài.](assets/diagrams/04-kien-truc.png){w=0}{src: Nguồn: nhóm tác giả.}

<<<portrait>>>

| Lớp | Chọn | Lý do |
|---|---|---|
| Ngôn ngữ và khung web | TypeScript trên Next.js, một khối | Sinh viên FPT đã quen JavaScript, một ngôn ngữ cho cả hai đầu |
| Cơ sở dữ liệu | **PostgreSQL** với extension `btree_gist` | MySQL không có ràng buộc `EXCLUDE` và không có kiểu range — thứ giải triệt để bài toán đặt trùng |
| Hàng đợi | Redis với BullMQ | Cần lịch chạy mỗi phút để nhả suất giữ chỗ hết hạn và nhắc hạn |
| Lưu ảnh | Kho đối tượng tương thích S3, đường dẫn ký sẵn 15 phút | Vài nghìn tệp một năm; mã băm là bằng chứng khi tranh chấp |
| Xác thực | Liên kết đăng nhập một lần tới email `@fpt.edu.vn`; **eKYC tự dựng bằng mã nguồn mở** | Nhóm chưa có pháp nhân nên không ký được hợp đồng với nhà cung cấp eKYC nào |
| Triển khai | Một máy chủ ảo tại Việt Nam, Docker Compose | Độ trễ thấp, từ 157.000đ một tháng [[ref:https://vietnix.vn/vps/]] |
{caption: Sáu quyết định công nghệ chính. Ngân sách hạ tầng dưới 500.000đ một tháng.}
{widths: 3,4,7}

## Vòng đời đơn thuê

![Máy trạng thái của một đơn thuê, mười ba trạng thái với các nhánh quá hạn, sự cố và mất tài sản.](assets/diagrams/02-trang-thai-don.png){w=12}{src: Nguồn: nhóm tác giả.}

Nguyên tắc quan trọng nhất: **gán máy muộn nhất có thể**. Đơn chỉ gắn với *kiểu* máy cho tới sát giờ giao,
nên một máy hỏng đột xuất không làm hỏng đơn đã bán.

## Luồng đặt thuê và thanh toán

<<<landscape>>>

![Trình tự đặt thuê: kiểm tra máy trống, giữ chỗ mười phút có khoá tồn kho, sinh mã VietQR động, nhận webhook có chữ ký rồi xác nhận đơn.](assets/diagrams/05-seq-dat-thue.png){w=0}{src: Nguồn: nhóm tác giả.}

<<<portrait>>>

## Bài toán kỹ thuật khó nhất: không được bán trùng một chiếc máy

Ba cách chống đặt trùng: khoá bi quan bằng `SELECT ... FOR UPDATE`, khoá lạc quan bằng cột phiên bản, và
**ràng buộc loại trừ của PostgreSQL** với kiểu khoảng thời gian. Nhóm chọn cách thứ ba vì nó ép ở tầng cơ sở
dữ liệu, đúng hay sai không phụ thuộc vào việc lập trình viên có nhớ viết khoá hay không.

```sql
CREATE TABLE inventory_holds (
    id         uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    device_id  uuid NOT NULL REFERENCES devices(id),
    order_id   uuid REFERENCES orders(id),
    period     tstzrange NOT NULL,          -- biên nửa mở [)
    status     text NOT NULL DEFAULT 'active',
    expires_at timestamptz NOT NULL,        -- giữ chỗ 10 phút
    EXCLUDE USING gist (device_id WITH =, period WITH &&)
        WHERE (status <> 'cancelled')
);
```
{caption: Ràng buộc loại trừ — hai suất giữ chồng khung giờ trên cùng một máy bị cơ sở dữ liệu từ chối với mã lỗi 23P01.}

Hai người bấm đặt cùng lúc: cả hai cùng chèn một dòng `inventory_holds`; PostgreSQL cho một dòng qua, dòng
còn lại nhận `23P01`, ứng dụng bắt lỗi đó và gợi ý máy khác. Không có cửa sổ nào để hai đơn cùng thắng.

Ba bài toán còn lại được xử lý tương tự ở tầng dữ liệu: **tiền vào một lần ghi nhận một lần** bằng
`UNIQUE (provider, provider_txn_id)` và mã chống lặp yêu cầu; **nhật ký không sửa được** bằng cách thu hồi
quyền `UPDATE` và `DELETE` trên bảng nhật ký cộng chuỗi mã băm nối tiếp; **ảnh hiện trạng chứng minh được**
bằng mã băm SHA-256 lưu kèm mỗi bản ghi.

## Lược đồ dữ liệu

<<<landscape>>>

![Lược đồ dữ liệu phần đặt thuê: người dùng, hồ sơ xác minh, kiểu máy, ca thi, suất giữ chỗ và đơn thuê.](assets/diagrams/09a-erd-dat-thue.png){w=0}{src: Nguồn: nhóm tác giả.}

<<<portrait>>>

## Giao diện

Mười màn hình đã được dựng thành nguyên mẫu HTML. Đây là **bản dựng thiết kế**, không phải ảnh chụp hệ thống
đang chạy.

![Trang chủ: định vị sản phẩm, ô kiểm tra máy trống theo ca thi, và bốn bước sử dụng.](assets/screenshots/01-landing.png){w=16}{src: Nguồn: bản dựng nguyên mẫu của nhóm tác giả.}

![Bước đặt cọc và thanh toán: mã VietQR động, cơ chế cọc, biểu phí khấu trừ công khai trước khi bấm xác nhận.](assets/screenshots/04-payment.png){w=16}{src: Nguồn: bản dựng nguyên mẫu của nhóm tác giả.}

![Bảng điều khiển vận hành: bốn chỉ số chính, đơn thuê trong ngày, lịch khai thác bảy ngày và cảnh báo cần xử lý.](assets/screenshots/07-dashboard.png){w=16}{src: Nguồn: bản dựng nguyên mẫu của nhóm tác giả.}

## Kế hoạch lập trình 12 tuần

| Giai đoạn | Tuần | Kết quả |
|---|---|---|
| Khung và dữ liệu | 1–3 | Lược đồ cơ sở dữ liệu, xác thực, kho máy, ràng buộc chống đặt trùng đã có kiểm thử đồng thời |
| Đặt thuê và thanh toán | 4–6 | Khách tự đặt và trả tiền được; bàn giao còn làm trên giấy rồi nhập tay |
| Bàn giao và quản trị | 7–9 | **Cuối tuần 9: bản chạy được nhận đơn thật**, một đơn đi trọn vòng đời |
| Làm cứng và chạy thử | 10–12 | Danh sách kiểm tra bảo mật, chạy thử với 3 máy và khách thật |
{caption: Lộ trình mười hai tuần. Ba tuần cuối không thêm tính năng.}
{widths: 3,1.5,8}
