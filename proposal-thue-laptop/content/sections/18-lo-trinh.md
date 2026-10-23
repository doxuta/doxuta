## Ba cổng chi tiêu

Vốn đầu tư 93.250.000đ ở Chương 15 không được bỏ ra một lần. Nhóm chia nó thành ba cổng, và mỗi cổng chỉ mở khi cổng trước trả về những con số đạt ngưỡng đặt ra từ trước. Nguyên tắc gói gọn trong một câu: **tiền đi sau dữ liệu, không đi trước dữ liệu.**

Lý do không chỉ là thận trọng. Vòng SV-STARTUP 2026 công bố định hướng "Làm thật – Thi thật", chuyển trọng tâm chấm điểm từ ý tưởng sang sản phẩm có khách hàng thật [[ref:https://vjst.vn/sv-startup-2026-chuyen-bien-ro-net-tu-y-tuong-sang-san-pham-tu-phong-trao-sang-hieu-qua-thuc-chat-86335.html]] [[ref:https://doanhnhan.congly.vn/sv-startup-2026-lam-that-thi-that-hieu-qua-thuc-chat.html]]. Một đội đã chạy ba máy thật và có số liệu đối chiếu đứng vững hơn một đội trình bày kế hoạch mua mười máy. Cách chia cổng vì vậy vừa là kỷ luật tài chính, vừa là cách tạo ra bằng chứng.

| Cổng | Trần chi | Chi vào việc gì | Số máy sau cổng |
|---|---|---|---|
| **1 — Khảo sát và phần mềm** | dưới **5.000.000đ** (kế hoạch 3.550.000đ) | Đăng ký hộ kinh doanh và giấy tờ 1.500.000đ · tên miền .com và .vn năm đầu 1.050.000đ · một tháng máy chủ, email, dịch vụ đối soát 450.000đ · một tháng dịch vụ lưu trữ và sao lưu 150.000đ · một tháng truyền thông cơ bản, gồm in ấn khảo sát, 400.000đ | 0 |
| **2 — Chạy thử** | **22.690.000đ** | 2 máy nhóm A × 6.500.000đ · 1 máy nhóm B × 7.500.000đ · 3 bộ phụ kiện × 300.000đ · tem chống bóc và khắc laser 3 × 30.000đ · 1 ổ cứng ngoài lưu ảnh hệ điều hành chuẩn 1.200.000đ | 3 |
| **3 — Đủ đội máy** | **68.010.000đ** | 7 máy còn lại (3 nhóm A, 3 nhóm B, 1 nhóm C) 52.000.000đ · phụ kiện, tem, tủ sạc, bàn kiểm máy, ổ cứng thứ hai, ba bản quyền Windows 11 Pro 11.610.000đ · dự phòng 5% 4.400.000đ | 10 |
{caption: Ba cổng chi tiêu, cộng lại đúng bằng 93.250.000đ vốn đầu tư ở Bảng T-CAPEX cộng 1.000.000đ chi phí vận hành của tháng 09/2026, tháng chưa có doanh thu.}
{widths: 2,2,7,2}

**Điều kiện mở cổng 2.** Cả bốn điều kiện phải đạt cùng lúc, ngưỡng là quy ước của nhóm [Ước lượng của nhóm]. Một, có văn bản trả lời của Phòng Khảo thí xác nhận nhà trường **không** bố trí sẵn máy dự phòng miễn phí đủ dùng cho ngày thi; đây là câu hỏi sống còn vì đã có trường đại học tại Việt Nam vận hành chương trình cho sinh viên mượn máy tính miễn phí [[ref:https://ctsv.uit.edu.vn/bai-viet/chuong-trinh-cho-sinh-vien-muon-may-tinh-mien-phi]] [[ref:https://www.sggp.org.vn/cho-sinh-vien-muon-laptop-mien-phi-post566364.html]]. Hai, thu được ít nhất **150 phản hồi khảo sát** có email `@fpt.edu.vn`, trong đó ít nhất **10%** từng lỡ hoặc suýt lỡ một buổi thi vì thiết bị. Ba, ít nhất **40 sinh viên** để lại số Zalo vào danh sách chờ. Bốn, có lịch thi chính thức của ít nhất một kỳ, vì toàn bộ lịch vận hành vô nghĩa nếu sai ngày.

**Điều kiện mở cổng 3.** Đo ngay sau đợt chạy thử, tất cả lấy từ hệ thống chứ không lấy từ cảm nhận. Ít nhất **9 lượt thuê hoàn tất**, đúng bằng con số tháng 10/2026 trong Bảng T-PNL. **0 lượt giao trễ** so với mốc trước giờ thi 30 phút, và **0 lượt** máy không khởi động được EOS Client hoặc Safe Exam Browser trong phòng thi. Doanh thu bình quân mỗi lượt **từ 120.000đ** trở lên, so với 144.100đ trong mô hình. Tỉ lệ khai thác ba máy trong mười ngày đợt thi **từ 35%**, tức cận dưới của dải 35–45% năm đầu mà ngành cho thuê thiết bị hay nhắc tới [[ref:https://www.natejonesentrepreneur.com/post/equipment-rental-business-startup-costs]]; nguồn này là blog cá nhân chứ không phải báo cáo ngành, nên nhóm dùng nó làm mức sàn thận trọng chứ không làm mục tiêu. Cuối cùng, **0 máy mất** và ít nhất **2 trong 9 đơn** đến từ giới thiệu.

```sql
-- Di trú nhỏ, chạy trước đợt chạy thử: gắn kênh và mã giới thiệu vào đơn
ALTER TABLE orders    ADD COLUMN referral_code text,
                      ADD COLUMN channel_code  text;
ALTER TABLE handovers ADD COLUMN signed_at timestamptz NOT NULL DEFAULT now();
CREATE INDEX orders_channel_code_idx ON orders (channel_code)
  WHERE channel_code IS NOT NULL;

-- Bảng điều khiển cổng 2: chạy đúng một lần sau ngày cuối đợt chạy thử
SELECT count(*) FILTER (WHERE o.status = 'completed')              AS luot_hoan_tat,
       round(avg(o.rent_fee + o.waiver_fee)
             FILTER (WHERE o.status = 'completed'))                AS doanh_thu_binh_quan,
       count(*) FILTER (WHERE h.signed_at > s.pickup_at)           AS luot_giao_tre,
       count(*) FILTER (WHERE o.referral_code IS NOT NULL)         AS luot_tu_gioi_thieu,
       count(DISTINCT o.device_id)                                 AS so_may_da_chay
FROM orders o
JOIN exam_slots s ON s.id = o.slot_id
LEFT JOIN handovers h ON h.order_id = o.id AND h.direction = 'out'
WHERE s.exam_date BETWEEN DATE '2026-10-05' AND DATE '2026-10-16';
```
{caption: Truy vấn đo năm chỉ số của cổng 2, chạy trên đúng lược đồ dữ liệu ở Chương 11.}

<<<pagebreak>>>

## Lộ trình 12 tháng

Lộ trình bắt đầu từ tháng 09/2026 là tháng chuẩn bị chưa có doanh thu, nên nó lệch một tháng so với mô hình tài chính ở Chương 15, vốn tính năm thứ nhất từ tháng 10/2026 là tháng đầu tiên có doanh thu. Cột lượt thuê trong bảng dưới lấy nguyên từ Bảng T-PNL, không phải con số mới.

<<<landscape>>>

| Tháng | Giai đoạn | Việc chính | Cột mốc kiểm tra được | Số máy | Ngân sách luỹ kế |
|---|---|---|---|---|---|
| 09/2026 | Xác thực | Gửi văn bản hỏi Phòng Khảo thí và Phòng Công tác sinh viên; phát khảo sát; lập bản đồ nhóm Facebook và câu lạc bộ; chạy Meta Ads Manager ở chế độ ước tính, không xuất bản | Có văn bản trả lời về máy dự phòng của trường; ≥ 150 phản hồi khảo sát; ≥ 40 số Zalo trong danh sách chờ; có lịch thi ba kỳ | 0 | 3.550.000đ |
| 10/2026 | Chạy thử · **Cổng 2** | Mua 3 máy; dựng ảnh hệ điều hành chuẩn có EOS Client và Safe Exam Browser; chạy thử trong đợt progress test Fall, giới hạn 12 đơn | 9 lượt hoàn tất; 0 lượt giao trễ; 100% lượt có biên bản đủ 6 ảnh mỗi chiều | 3 | 26.240.000đ |
| 11/2026 | Mở quy mô · **Cổng 3** | Mua 7 máy còn lại; tủ sạc, bàn kiểm máy; tuyển 3–5 cộng tác viên điểm; phát mã giới thiệu | 10/10 máy đạt đủ 12 mục kiểm tra chất lượng, pin ≥ 80% và chạy thực ≥ 3,5 giờ; 11 lượt thuê | 10 | 94.250.000đ |
| 12/2026 | **Đỉnh 1 — Final Fall** | Ra mắt chính thức; trực suốt ca thi; đặt máy dự phòng nóng tại sảnh toà nhà có phòng thi | 42 lượt; cam kết đổi máy trong 15 phút đạt 100% số ca phát sinh; 0 máy mất | 10 | 94.250.000đ |
| 01/2027 | Ngoài đỉnh | Chào gói tháng cho đồ án, thực tập và kỳ OJT | 14 lượt và 2 máy-tháng | 10 | 94.250.000đ |
| 02/2027 | Bảo dưỡng | Đo lại pin toàn đội, thay pin dưới ngưỡng, cập nhật ảnh hệ điều hành chuẩn theo phiên bản Safe Exam Browser mới | 16 lượt; 100% máy có nhật ký pin cập nhật trong 30 ngày | 10 | 94.250.000đ |
| 03/2027 | Progress test Spring | Kích hoạt mã giới thiệu hai chiều và giá nhóm; đo hệ số lan truyền | 26 lượt; ≥ 20% đơn có mã giới thiệu | 10 | 94.250.000đ |
| 04/2027 | **Đỉnh 2 — Final Spring** | Lặp lại kịch bản đỉnh 1 với quy trình đã sửa sau đỉnh 1 | 56 lượt; tỉ lệ khai thác trong tuần thi ≥ 70% | 10 | 94.250.000đ |
| 05/2027 | Chuyển kỳ | Rà soát giá theo dữ liệu thật; gia hạn gói tháng | 43 lượt; luỹ kế lợi nhuận chuyển dương, đạt 1.358.472đ | 10 | 94.250.000đ |
| 06/2027 | Progress test Summer | Đẩy gói tháng lên 5 máy-tháng để lấp tháng trũng | 30 lượt và 5 máy-tháng | 10 | 94.250.000đ |
| 07/2027 | Tổng kết giữa năm | Lập hồ sơ dự thi FPT Biz Talent và SV-STARTUP bằng số liệu thật | 25 lượt; hồ sơ dự thi đã nộp | 10 | 94.250.000đ |
| 08/2027 | **Đỉnh 3 — Final Summer** | Chốt số năm thứ nhất; quyết định có mua thêm 6 máy cho năm thứ hai hay không | 65 lượt; luỹ kế lợi nhuận sau thuế ≥ 11.371.200đ | 10 | 94.250.000đ |
{caption: Lộ trình 12 tháng, mỗi tháng có đúng một cột mốc đo được bằng số lấy từ hệ thống hoặc từ Bảng T-PNL.}
{note: Cột ngân sách luỹ kế là tiền cam kết chi qua ba cổng, gồm 93.250.000đ vốn đầu tư và 1.000.000đ chi phí vận hành tháng 09/2026. Định phí 2.800.000đ mỗi tháng từ 10/2026 trở đi đã nằm trong Bảng T-PNL nên không cộng lại ở đây.}

<<<portrait>>>

Ba đỉnh trong bảng không phải lựa chọn của nhóm mà là cấu trúc của trường. Một năm học của Đại học FPT có ba học kỳ Fall, Spring và Summer [[ref:https://www.facebook.com/university.fpt.edu.vn/posts/1183525043803905/]] [[ref:https://hanoi.fpt.edu.vn/tu-van/thoi-gian-hoc-dai-hoc-fpt.html]] [[ref:https://daihoc.fpt.edu.vn/lo-trinh-dao-tao-cua-truong-dai-hoc-fpt/]], kéo theo ba kỳ thi cuối kỳ và ba đợt progress test. Mọi việc trong lộ trình đều neo vào sáu cửa sổ đó.

## Kế hoạch tiếp cận thị trường

Quy mô nhiệm vụ nhỏ hơn nhiều so với cảm giác ban đầu. Tháng cao nhất của năm thứ nhất cần 65 lượt thuê, tức khoảng **1,3% trong số 4.500 đến 6.000 sinh viên** của campus Đà Nẵng [Ước lượng của nhóm]. Với quy mô đó, nhóm **đặt ngân sách quảng cáo trả tiền khởi điểm bằng 0đ** và chỉ mở khi đo được chi phí thật. Toàn bộ dòng truyền thông trong Bảng T-OPEX là 400.000đ một tháng, tức 4.800.000đ cả năm, dùng cho in ấn, quà giới thiệu và sản xuất nội dung.

Trần chi phí thu hút một khách hàng tính từ chính số của dự án: số dư đóng góp 110.736đ mỗi lượt, nhân với 3 lượt cho mỗi vòng đời khách [Ước lượng của nhóm], ra giá trị vòng đời 332.208đ; chia cho 3 theo quy tắc kinh nghiệm tỉ lệ 3:1 trong quản trị khởi nghiệp, ra **trần 110.736đ mỗi khách**. Quy tắc 3:1 là thông lệ quản trị, không phải số liệu thị trường Việt Nam, và nhóm ghi rõ như vậy. Mọi kênh có chi phí vượt trần này đều bị tắt.

| Kênh | Chi phí | Chỉ số đo | Ghi chú |
|---|---|---|---|
| **Giới thiệu truyền miệng trong mùa thi** | Chiết khấu, không phải tiền mặt. Giá nhóm 10–20% cho nhóm 2 người trở lên, bằng mức đối thủ đang áp dụng | % đơn có `referral_code`; hệ số lan truyền K; chi phí chiết khấu chia số đơn giới thiệu | Kênh nhóm tin nhất |
| **Cộng tác viên điểm (3–5 người)** | Hoa hồng 10–15% giá trị đơn, tức 14.410đ đến 21.615đ mỗi đơn trên doanh thu bình quân 144.100đ. Không lương cố định | Số đơn theo mã riêng từng cộng tác viên | Chỉ giới thiệu, không được báo giá, không được cầm cọc. Trả hoa hồng sau khi khách trả máy |
| **Nhóm Facebook và trang confession** | 0đ cho bài tự đăng. Giá bài trả phí phải tự khảo bằng tin nhắn cho quản trị viên, chưa có bảng giá công khai | Mã ưu đãi riêng cho từng bài để truy ngược đơn | Bài đầu tiên là bài khảo sát, không phải bài bán hàng |
| **Zalo là nơi chốt đơn** | 0đ | Số tin nhắn mới; tỉ lệ tin nhắn thành đơn | Toàn bộ 12 website cho thuê laptop Việt Nam được khảo sát đều đặt hotline nổi bật và không có giỏ hàng |
| **Tài trợ hiện vật cho câu lạc bộ** | Chi phí cơ hội máy-ngày, không chi tiền mặt | Số sự kiện, số sinh viên tiếp xúc, số đơn phát sinh sau sự kiện | Cho mượn máy khi câu lạc bộ tổ chức hackathon hoặc workshop |
| **Quảng cáo trả tiền** | 0đ ở năm thứ nhất | Chi phí mỗi tin nhắn so với trần 110.736đ | Chỉ mở sau khi biết chi phí thật của đợt thi đầu |
{caption: Sáu kênh tiếp cận, chi phí và chỉ số đo tương ứng.}
{widths: 3,4,4,4}

**Vì sao nhóm tin nhất vào giới thiệu truyền miệng.** Có ba lý do thuộc về bản chất dịch vụ. Thứ nhất, rào cản niềm tin rất cao: khách phải đặt cọc cho một dịch vụ mới không có cửa hàng, trong khi mức cọc phổ biến của đối thủ tại Đà Nẵng là 500.000đ đến 2.000.000đ [[ref:https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html]]. Lời của bạn cùng lớp phá được rào cản đó, quảng cáo thì không. Thứ hai, nhu cầu phát sinh đột ngột: người phát hiện máy hỏng lúc 22:00 hôm trước ngày thi không đi tìm quảng cáo mà hỏi bạn bè, nên kênh phân phối thật của dịch vụ chính là một cuộc trò chuyện giữa hai sinh viên. Thứ ba, trải nghiệm dễ kể lại. Một lần cứu nguy thành công tạo ra nhiều đơn hơn bất kỳ phần thưởng nào.

Mức thưởng được neo vào dữ liệu thật chứ không bịa: leminhSTORE, đơn vị duy nhất tại Đà Nẵng tự nhận chuyên mảng sinh viên, đang giảm **10 đến 20% cho nhóm 2 đến 10 bạn** [[ref:https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html]] [[ref:https://www.facebook.com/leminhstore.vn/]]. Thưởng dưới 10% là yếu hơn thứ khách đã có sẵn ngoài thị trường. Nhóm chọn chiết khấu và ngày thuê miễn phí thay vì tiền mặt, vì thưởng tiền mặt tạo động cơ giới thiệu ảo trong môi trường campus.

## Thời điểm ra mắt

Ra mắt chính thức được đặt vào tháng 12/2026, ngay trước kỳ thi cuối kỳ Fall, vì ba lý do. Một, nhu cầu dồn vào sáu cửa sổ mỗi cửa sổ một đến hai tuần, nên ra mắt ngoài cửa sổ là trả định phí mà không có doanh thu; dự báo cho thấy tháng thấp nhất 9 lượt và tháng cao nhất 65 lượt, chênh hơn bảy lần. Hai, lời hứa của dịch vụ chỉ chứng minh được trong một kỳ thi thật, không chứng minh được bằng lời. Ba, truyền miệng chỉ lan khi nhiều người cùng chịu một áp lực trong cùng vài ngày, và kỳ thi cuối kỳ là lúc duy nhất điều đó xảy ra.

Nhưng lần **chạy thử** đầu tiên lại đặt sớm hơn, vào đợt progress test tháng 10/2026, và **giới hạn ở 12 đơn**. Lý do giới hạn rất cụ thể. Với 3 máy, nhóm giữ 1 máy làm dự phòng nóng nên chỉ cho thuê tối đa 2 máy cùng lúc, đúng quy tắc dự phòng nóng bằng khoảng 10% số máy đang cho thuê và tối thiểu 2 máy khi đội lớn hơn. Rủi ro lớn nhất của đợt đầu không phải thiếu khách mà là **lỗi hệ thống**: nếu bản ảnh hệ điều hành chuẩn sai phiên bản Safe Exam Browser, không phải 2% máy hỏng mà là 100% máy hỏng cùng lúc, và máy dự phòng cũng hỏng y hệt vì dùng chung bản ảnh. Chạy 12 đơn thay vì 60 đơn giữ vùng thiệt hại đủ nhỏ để sửa được. Trong một campus vài nghìn người nơi truyền miệng là kênh chính, một lần làm hỏng việc lan nhanh đúng bằng một lần cứu nguy thành công. Cuối cùng, giới hạn đơn cũng giới hạn tiền: tối đa 22.690.000đ nằm trong tài sản trước khi nhóm biết nhu cầu có thật hay không.

Progress test là kỳ thi ít rủi ro hơn thi cuối kỳ, nên nó là buổi tổng duyệt đúng nghĩa, cách đỉnh lớn nhất hai tháng, đủ thời gian sửa quy trình trước khi mười máy cùng ra đường.

## Các cột mốc và tín hiệu dừng

<<<landscape>>>

| Cột mốc | Thời hạn | Chỉ số đạt | Nếu không đạt |
|---|---|---|---|
| **M1** Trả lời của Phòng Khảo thí về máy dự phòng miễn phí | 30/09/2026 | Có văn bản, và nhà trường không bố trí đủ máy | **Dừng mô hình bán cho sinh viên.** Chuyển sang đề xuất vận hành đội máy dự phòng cho chính nhà trường |
| **M2** Xác nhận quy chế thi cho dùng máy không thuộc sở hữu thí sinh | 30/09/2026 | Có văn bản chấp thuận | **Dừng toàn bộ sản phẩm theo ca thi**, chỉ giữ gói tháng cho đồ án và thực tập |
| **M3** Đợt chạy thử 3 máy | 31/10/2026 | ≥ 9 lượt hoàn tất, 0 lượt giao trễ, 0 lượt lỗi phần mềm thi | Không mở cổng 3. Chạy thêm một đợt. Nếu đợt hai dưới 6 lượt thì thanh lý 3 máy và dừng dự án |
| **M4** Đỉnh Final Fall | 31/12/2026 | ≥ 42 lượt; đổi máy trong 15 phút đạt 100% số ca phát sinh | Hoãn mọi khoản chi ngoài định phí; rà lại giá và kênh trước đỉnh Spring |
| **M5** Sáu tháng đầu | 31/03/2027 | Bình quân ≥ 25 lượt một tháng, tức ngưỡng hoà vốn tiền mặt | Cắt đội máy xuống 5 máy, thanh lý 5 máy còn lại khi giá thanh lý còn tốt |
| **M6** Hai đỉnh thi liên tiếp | 30/04/2027 | Luỹ kế lợi nhuận sau thuế ≥ −1.491.528đ | **Tín hiệu dừng cứng**: thanh lý toàn bộ đội máy trong 60 ngày, hoàn vốn góp phần còn lại |
| **M7** Thất thoát tài sản | Mỗi quý | Không quá 1% số lượt thuê bị mất máy hoặc hư hỏng nặng | Dừng bậc cọc 0đ và 150.000đ, mọi khách quay về cọc 300.000đ |
| **M8** Chốt năm thứ nhất | 30/09/2027 | ≥ 382 lượt và lợi nhuận sau thuế ≥ 14.442.672đ | Không mở rộng lên 16 máy ở năm thứ hai; giữ nguyên 10 máy thêm một năm |
{caption: Tám cột mốc, mỗi cột mốc có một hành động bắt buộc khi không đạt, kể cả hành động dừng.}
{widths: 4,2,5,6}

<<<portrait>>>

:::risk Tín hiệu dừng cứng, viết ra trước khi bắt đầu
Nếu đến 30/04/2027, sau **hai kỳ thi cuối kỳ đã đi qua**, luỹ kế lợi nhuận sau thuế vẫn thấp hơn −1.491.528đ trong Bảng T-PNL, nhóm thanh lý toàn bộ đội máy trong 60 ngày thay vì bơm thêm tiền.
Lý do chọn đúng mốc này: hai đỉnh thi là đủ để phân biệt vận hành kém với nhu cầu không tồn tại, và máy cũ dòng doanh nghiệp mua vào tháng 11/2026 vẫn còn thanh khoản tốt tại thị trường Đà Nẵng ở thời điểm đó. Càng để lâu, tài sản càng mất giá và khoản lỗ càng khó thu hồi.
:::

Nguồn vốn dự phòng cho các cột mốc có lãi nằm ở các cuộc thi khởi nghiệp, nhưng nhóm không coi đó là tiền chắc chắn. FPT Biz Talent do chính Trường Đại học FPT tổ chức có tổng giải thưởng 260.000.000đ chia cho nhiều giải [[ref:https://daihoc.fpt.edu.vn/tin-noi-bat-muc-tin-tuc/fpt-biz-talent-2025-truong-dh-fpt-kien-tao-the-he-doanh-nhan-tre/]] [[ref:https://www.vista.gov.vn/vi/news/khoi-nghiep-doi-moi-sang-tao/khoi-dong-cuoc-thi-khoi-nghiep-quy-mo-toan-quoc-fpt-biz-talent-2025-uom-mam-tai-nang-doanh-nhan-doi-moi-sang-tao-tuong-lai-11452.html]]; Startup Wheel 2026 có giải Nhất tổng trị giá 400.000.000đ trong đó hiện kim là 150.000.000đ [[ref:https://startupwheel.vn/vi/giai-thuong/]] [[ref:https://startupwheel.vn/vi/top-100-startup-wheel-2026/]]; SV-STARTUP 2026 có 15 giải Nhất, 30 giải Nhì, 55 giải Ba và 34 giải Khuyến khích [[ref:https://tuoitre.vn/15-du-an-khoi-nghiep-cua-hoc-sinh-sinh-vien-gianh-giai-nhat-sv-startup-2026-20260419203319353.htm]]. Mọi kế hoạch chi ở trên đều đứng được mà không cần đồng nào từ các nguồn này. Tiền thưởng nếu có chỉ dùng để rút ngắn cổng 3 hoặc đi thẳng vào đội máy năm thứ hai.

## Hướng mở rộng sau năm đầu

**Hướng một, mở sang các trường khác tại Đà Nẵng.** Thị trường tiềm năng là khoảng 90.000 đến 120.000 sinh viên đại học và cao đẳng toàn thành phố [Ước lượng của nhóm]. Điều kiện tiên quyết có ba phần. Năm thứ nhất phải đạt đủ 382 lượt và tỉ lệ khai thác 42%. Trường đích phải được xác minh là có hình thức thi trên máy cá nhân của sinh viên, vì định vị "máy sẵn sàng thi" không tự chuyển giao sang một trường thi trên giấy. Và phải có điểm trực trong bán kính đi xe máy dưới 15 phút tới cổng trường đó, bởi cam kết đổi máy trong 15 phút không vượt được quãng đường 8 đến 15 km, đúng khoảng cách khiến bảy đơn vị cho thuê hiện có tại Đà Nẵng không phục vụ nổi khu Hoà Hải.

**Hướng hai, thêm dịch vụ cho kỳ thi chứng chỉ.** Điều kiện tiên quyết là văn bản của đơn vị tổ chức xác nhận thí sinh được dùng máy của mình. Nếu kỳ thi diễn ra tại trung tâm khảo thí và dùng máy của trung tâm thì không có thị trường, và nhóm phải xác minh điều này trước khi chi bất kỳ khoản nào. Điều kiện thứ hai là ký được hợp đồng với ít nhất một trung tâm, vì đây là bán theo lô chứ không bán lẻ.

**Hướng ba, cho thuê thiết bị khác.** Chỉ thêm loại thiết bị **dùng lại được toàn bộ quy trình hiện có**: biên bản sáu ảnh hai chiều có mã băm, xoá dữ liệu theo chuẩn, kiểm tra 12 điểm. Màn hình rời và bộ trình chiếu mini cho nhóm đồ án là ví dụ. Điều kiện tiên quyết bằng số: tỉ lệ khai thác đội laptop phải đạt **từ 60% trong hai quý liên tiếp** trước khi bỏ vốn vào loại tài sản thứ hai. Mua tài sản mới khi tài sản cũ còn chưa chạy hết công suất là cách chôn vốn nhanh nhất trong một mô hình thâm dụng tài sản.

:::warn Hướng nhóm chủ động không theo đuổi
Nhóm **không** mở sang cho thuê máy cấu hình cao phục vụ chơi game hoặc dựng phim cho khách ngoài sinh viên, dù đó là phân khúc giá thuê cao hơn. Hai lý do. Một chiếc máy như vậy có giá mua bằng ba máy nhóm A, làm tỉ lệ vốn trên mỗi khách xấu đi đúng vào chỗ mô hình đang yếu. Quan trọng hơn, lớp phòng thủ đầu tiên của nhóm là bắt buộc email `@fpt.edu.vn` và mã số sinh viên; khách ngoài trường không có hai thứ đó, nên toàn bộ khẩu quyết "cọc thấp và danh tính mạnh" sụp đổ và rủi ro mất máy tăng vọt.
Tương tự, nhóm **không** mở sang thành phố khác trong hai năm đầu. Cam kết đổi máy trong 15 phút đòi hỏi có người và có máy đứng sẵn tại chỗ, và đó là thứ duy nhất hiện chưa đơn vị nào tại Đà Nẵng làm được.
:::
