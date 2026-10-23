## Lộ trình 12 tuần

Mười hai tuần neo vào mốc có thật: bắt đầu đầu học kỳ Fall, kết thúc ngay trước đợt thi cuối kỳ. Vai viết tắt: **TK** trưởng nhóm kỹ thuật, **DL** lập trình viên dữ liệu và nghiệp vụ, **GD** lập trình viên giao diện, **KT** kiểm thử và tài liệu, **VH** vận hành và hạ tầng.

<<<landscape>>>

| Tuần | Mục tiêu | Bàn giao | Tiêu chí hoàn thành đo được | Ai |
|---|---|---|---|---|
| 1 | Khung và môi trường | Kho mã, `docker compose` với `postgres:17` và `redis:7`, quy trình dựng GitHub Actions | Máy mới dựng xong dưới 10 phút; `CREATE EXTENSION btree_gist` chạy được **trên chính máy chủ sẽ thuê** | TK, VH |
| 2 | Cụm dữ liệu đặt thuê | Bảy bảng từ `users` tới `orders`, tệp di trú, `seed.ts` | Di trú chạy sạch từ cơ sở dữ liệu rỗng; seed sinh đúng 5 máy nhóm A, 4 nhóm B, 1 nhóm C; hai lệnh chèn chồng khung giờ trả mã `23P01` [[ref:https://chat2db.ai/resources/blog/postgres-exclusion-constraints-guide]] | DL, TK |
| 3 | Máy trạng thái và nhật ký | Bảng chuyển trạng thái đơn và máy, `audit_logs` nối chuỗi băm, đăng nhập liên kết một lần | 13 trạng thái đơn và 9 trạng thái máy khớp sơ đồ chương 10; trigger chặn `UPDATE` và `DELETE` trên `audit_logs` | DL, GD |
| 4 | Giữ suất kho | `GET /api/availability`, `POST /api/holds`, tác vụ nhả suất hết hạn | 20 yêu cầu song song cho đúng 1 lần thành công; suất quá 10 phút tự sang `cancelled` trong 60 giây, không dòng nào bị xoá | DL, KT |
| 5 | Tiền vào | `POST /api/orders` sinh VietQR, webhook kiểm HMAC, bảng `payments`, trang đối soát tay | Gửi lại một webhook 10 lần chỉ sinh 1 dòng `payments` [[ref:https://stripe.com/blog/idempotency]]; đơn sang `paid` dưới 30 giây | DL, TK |
| 6 | Khách đi hết luồng đặt | eKYC bản thử, hợp đồng điện tử, `outbox_messages`, ba màn hình khách | 5 sinh viên ngoài nhóm tự đặt xong, mỗi người dưới 4 phút; không lời gọi ra ngoài nào nằm trong giao dịch [[ref:https://milanjovanovic.tech/blog/implementing-the-outbox-pattern]] | GD, DL |
| 7 | Bàn giao máy | Ứng dụng nhân viên dạng PWA, gán máy, 6 ảnh ký sẵn, chốt biên bản | Chốt lúc mất mạng rồi đồng bộ không mất ảnh, không sinh biên bản trùng; thiếu 1 ảnh trả `422`; mã băm khớp tệp trên kho | GD, KT |
| 8 | Thu hồi và hoàn cọc | Trả máy, kiểm tra, khấu trừ, đổi máy khẩn, phí trả trễ, quét đơn quá hạn | Hoàn cọc dưới 5 phút ở cả 10 lần thử; hoàn cọc lần hai bị chặn; phí trễ dừng đúng ở trần 200.000đ mỗi ngày | DL, GD |
| 9 | Quản trị và báo cáo | Kho máy, `pricing_rules`, bốn biểu đồ, lệnh khoá hai người duyệt | Mọi `/api/admin/*` trả `403` với vai `student`; người xin khoá máy không tự duyệt được lệnh của mình | GD, TK |
| 10 | Làm cứng | Danh sách kiểm tra bảo mật 15 mục, giới hạn tần suất, quét phụ thuộc, đo tải | 15 trên 15 mục tích kèm bằng chứng; phân vị 95 của `GET /api/availability` dưới 800 ms với 50 người dùng ảo | TK, KT |
| 11 | Chạy thử thật có kiểm soát | 20 đơn thật trong một đợt progress test, diễn tập ứng cứu và khôi phục | 20 trên 20 đơn đi hết vòng đời tới `closed`; một lần đổi máy đo được dưới 15 phút; khôi phục sao lưu dưới 90 phút | Cả nhóm |
| 12 | Sửa lỗi và bàn giao | Sửa lỗi tuần 11, sổ tay vận hành, đổi toàn bộ khoá bí mật | Không còn lỗi mức chặn; thời gian khôi phục trong tuần thi đo được dưới 30 phút | Cả nhóm |
{caption: Lộ trình 12 tuần chia bốn giai đoạn, mỗi tuần một tiêu chí hoàn thành đo được bằng số hoặc bằng một phép thử.}
{widths: 1,3,5,9,2}

<<<portrait>>>

:::ok Mốc quan trọng nhất
**Cuối tuần 9 là bản chạy được đầu tiên có thể nhận đơn thật**: một đơn đi trọn vòng đời từ đặt, trả tiền, ký hợp đồng, nhận máy có biên bản ảnh, trả máy, hoàn cọc, tới đóng đơn. Ba tuần cuối không thêm tính năng, chỉ làm cứng và chạy thử. Cuối tuần 6 đã có bản khách tự đặt và trả tiền được, nhưng bàn giao vẫn làm trên biên bản giấy rồi nhập tay lại.
:::

## Thứ tự làm và lý do

Đường găng của dự án là một chuỗi: `btree_gist` chạy được trên máy chủ đã thuê (tuần 1) chặn ràng buộc `EXCLUDE USING gist` trên `inventory_holds` (tuần 2); bảng đó chặn `POST /api/holds` (tuần 4); không có suất giữ thì không có gì gắn tiền vào (tuần 5); đơn chưa sang `paid` thì không có gì để gán máy và bàn giao (tuần 7); chưa bàn giao thì không có gì để thu hồi (tuần 8); đủ chuỗi đó mới chạy thử thật được (tuần 11).

Ràng buộc cơ sở dữ liệu nằm ngay tuần đầu vì đó là rủi ro rẻ nhất khi phát hiện sớm: đổi nhà cung cấp ở tuần 1 tốn một buổi, đổi ở tuần 8 là viết lại cả tầng chống trùng lịch [[ref:https://dev.to/franckpachot/postgresql-exclude-constraints-for-better-concurrency-than-serializable-pob]]. Quy ước biên nửa mở `[)` và đệm 90 phút quay vòng cũng phải chốt trước dòng mã đầu tiên tính giờ [[ref:https://www.jusdb.com/blog/postgresql-range-types-exclusion-constraints]].

Ngoài đường găng: trang quản trị đẩy về tuần 9 vì chín tuần đầu xem kho bằng `psql` là đủ; việc dựng ảnh hệ điều hành chuẩn, cài EOS Client và Safe Exam Browser, đo pin bằng `powercfg /batteryreport` do vai VH làm song song. Ngược lại, hồ sơ đăng ký dịch vụ đối soát VietQR và hồ sơ dùng thử eKYC nộp ngay tuần 1 dù tới tuần 5 và tuần 6 mới cần, vì nhóm không kiểm soát được tốc độ trả lời của nhà cung cấp.

## Định nghĩa hoàn thành

Một hạng mục chỉ được gạch khỏi bảng lộ trình khi đủ bảy điều kiện, không phải khi chạy được trên máy người viết.

1. Có kiểm thử tự động, trong đó ít nhất một ca cho đường thất bại.
2. Toàn bộ kiểm thử xanh trên GitHub Actions, chạy trên `postgres:17` thật chứ không trên cơ sở dữ liệu giả lập.
3. Đã qua rà soát mã của một người khác; không ai tự trộn nhánh của mình vào `main`.
4. Quy tắc nghiệp vụ mới được ép ở tầng thấp nhất có thể: ràng buộc, trigger, kiểm tra ở máy chủ, rồi mới tới giao diện [[ref:https://amitavroy.com/articles/postgresql-gist-exclusion-constraintthe-database-evel-answer-to-double-bookings]].
5. Có tài liệu: một đoạn trong `README`, một dòng trong danh mục endpoint, một bước trong sổ tay nếu là việc vận hành.
6. Đã triển khai và chạy được trên môi trường thử nghiệm.
7. Đã thử với dữ liệu thật: một hộp thư `@fpt.edu.vn` thật, một lần chuyển khoản thật dù chỉ 2.000đ, một chiếc máy thật trong đội 10 máy.

## Chiến lược kiểm thử

| Loại | Phạm vi | Công cụ | Ai viết | Chạy khi nào |
|---|---|---|---|---|
| Đơn vị | Tiền thuê, phí trễ, bậc cọc theo `trust_score`, chuỗi VietQR, mã băm ảnh | Vitest | DL, GD | Mỗi lần đẩy mã |
| Tích hợp cơ sở dữ liệu | Ràng buộc `EXCLUDE`, trigger nhật ký, 14 quy tắc bất biến R01 đến R14 | Vitest trên `postgres:17` trong Docker | DL | Mỗi yêu cầu trộn mã |
| Đồng thời | Đặt trùng suất cuối, webhook lặp, bấm hoàn cọc hai lần | Kịch bản Node dùng `Promise.all`, hai phiên `psql` chạy tay | TK | Mỗi yêu cầu trộn mã |
| Đầu cuối | Bốn hành trình: đặt và trả tiền, bàn giao, trả máy, xử lý quá hạn | Playwright, cả bố cục điện thoại | KT | Hằng đêm và trước mỗi lần phát hành |
| Chịu tải | `availability` và `holds` ở 20 lượt mỗi phút, gấp 30 lần nhu cầu bình quân năm 1 | k6 | TK | Tuần 10 và trước mỗi đợt thi |
| Thủ công theo kịch bản | 12 kịch bản, gồm khách ghi sai nội dung chuyển khoản và khách mất mạng | Danh sách in ra, tick bằng bút | KT | Trước mỗi lần phát hành thật |
| Diễn tập vận hành | Đổi máy khẩn theo quy trình SOP-04, khôi phục sao lưu bấm giờ, mất máy chủ giữa ngày thi | Đồng hồ bấm giờ và biên bản | VH | Trước mỗi đợt thi cuối kỳ |
{caption: Bảy loại kiểm thử của ExamLap, kèm phạm vi, công cụ, người viết và thời điểm chạy.}
{widths: 3,7,4,2,4}
{note: Nhóm không đặt mục tiêu phần trăm dòng mã được phủ. Mục tiêu là 14 quy tắc bất biến ở chương 10 đều có một ca kiểm thử cố tình vi phạm chúng.}

```ts
it('chỉ một người giành được chiếc máy cuối cùng', async () => {
  const slot = await seedSlot({ examDate: '2026-12-08', name: 'Ca 1 sáng' });
  await seedDevices({ model: 'A', ready: 1 });            // đúng 1 máy rảnh
  const res = await Promise.all(Array.from({ length: 20 }, (_, i) =>
    api.post('/api/holds', { slot_id: slot.id, model: 'A' },
      { headers: { 'Idempotency-Key': randomUUID(), 'X-Test-User': `sv${i}` } })));
  expect(res.filter(r => r.status === 201)).toHaveLength(1);
  expect(res.filter(r => r.status === 409)).toHaveLength(19);
});
```
{caption: Ca kiểm thử đồng thời cho bài toán đặt trùng, thứ không lộ ra khi bấm tay từng lần.}

Mười hai ca kiểm thử bắt buộc, viết dạng cho trước, khi, thì.

1. **Cho trước** ca thi chỉ còn một máy nhóm A `ready`, **khi** 20 yêu cầu `POST /api/holds` gửi song song, **thì** đúng một yêu cầu trả `201`, 19 yêu cầu trả `409 SLOT_SOLD_OUT`.
2. **Cho trước** đơn chiếm máy tới 12:00 và `period` đã cộng 90 phút quay vòng, **khi** chèn suất mới lúc 13:00, **thì** nhận mã `23P01`; suất lúc 13:30 thì chèn được [[ref:https://www.odoo.com/documentation/18.0/applications/sales/rental.html]].
3. **Cho trước** một `Idempotency-Key` đã dùng, **khi** gửi lại `POST /api/orders` cùng thân, **thì** nhận đúng phản hồi cũ và chỉ có một dòng `orders`; thân khác thì `422 IDEMPOTENCY_KEY_REUSED` [[ref:https://brandur.org/idempotency-keys]].
4. **Cho trước** giao dịch đã xử lý, **khi** dịch vụ đối soát gửi lại gói tin 10 lần, **thì** vẫn một dòng `payments` và đơn chỉ đổi trạng thái một lần [[ref:https://matheuspalma.com/blog/outbound-webhook-delivery-signing-retries-dead-letters]].
5. **Cho trước** webhook có chữ ký sai hoặc lệch giờ quá 5 phút, **khi** gọi vào hệ thống, **thì** bị từ chối, không ghi dòng nào, sinh một cảnh báo.
6. **Cho trước** suất giữ hết hạn lúc 08:10, **khi** tác vụ nền chạy lúc 08:11, **thì** dòng đó sang `cancelled`, đơn sang `hold_expired`, tổng số dòng không giảm, máy hiện lại trong `GET /api/availability`.
7. **Cho trước** biên bản bàn giao chỉ có 5 ảnh, **khi** nhân viên bấm chốt, **thì** nhận `422` và đơn vẫn ở `assigned`.
8. **Cho trước** nhân viên chốt biên bản lúc mất sóng, **khi** có sóng lại, **thì** đủ 6 ảnh được đẩy lên, mã băm khớp, không sinh biên bản thứ hai.
9. **Cho trước** đơn đã hoàn cọc, **khi** bấm hoàn cọc lần hai, **thì** nhận `409` và vẫn chỉ một dòng `payments` chiều ra `succeeded`.
10. **Cho trước** đơn trả trễ 95 phút, **khi** chốt biên bản thu hồi, **thì** phí trễ đúng 80.000đ; đơn trễ cả ngày dừng ở trần 200.000đ.
11. **Cho trước** sinh viên A đã đăng nhập, **khi** gọi `GET /api/orders/{code}` bằng mã đơn của sinh viên B, **thì** nhận `404` chứ không phải `403`, để không lộ mã đơn đó tồn tại.
12. **Cho trước** quản trị viên vừa tạo lệnh khoá màn hình, **khi** chính người đó bấm duyệt, **thì** bị từ chối và lần từ chối cũng vào `audit_logs`.

## Danh sách kiểm tra bảo mật trước khi mở cho người thật dùng

Mười lăm mục tích trong tuần 10, mỗi mục kèm bằng chứng là ảnh chụp màn hình, tệp nhật ký hoặc một ca kiểm thử.

1. Ép HTTPS toàn bộ đường dẫn, bật HSTS; gọi bằng `http://` phải bị chuyển hướng.
2. Không lưu mật khẩu dạng thô; sinh viên dùng liên kết đăng nhập một lần, quản trị bắt buộc lớp xác thực thứ hai.
3. Mã đăng nhập sống tối đa 10 phút, dùng đúng một lần; thử dùng lại phải thất bại.
4. Giới hạn tần suất đăng nhập 3 lần mỗi giờ cho mỗi hộp thư, trả `429` kèm `Retry-After`.
5. Kiểm quyền ở mọi endpoint: chạy kịch bản gọi lần lượt toàn bộ danh mục bằng phiên vai `student`, đối chiếu bảng phân quyền.
6. Truy vấn đơn thuê mang điều kiện chủ sở hữu ngay trong câu lệnh SQL, không lọc sau khi đã lấy dữ liệu về.
7. Ảnh giấy tờ và ảnh khuôn mặt mã hoá khi lưu, chỉ phục vụ qua đường dẫn ký sẵn hạn 15 phút.
8. `kyc_profiles.images_purge_at` có giá trị ở mọi hồ sơ và tác vụ xoá tự động đã chạy thật ít nhất một lần, xoá ảnh sau 90 ngày.
9. Không bảng nào chứa số căn cước thô: quét kết xuất `pg_dump` bằng biểu thức chính quy, kết quả phải rỗng.
10. Sao lưu hằng ngày **đã thử khôi phục thật** lên máy trống, có bấm giờ và biên bản; sao lưu chưa từng khôi phục coi như chưa có.
11. Không tệp `.env` nào trong Git; quét lịch sử kho mã tìm khoá bí mật và xử lý hết kết quả.
12. Khoá ký webhook, khoá eKYC, khoá kho ảnh đã đổi một lần trước khi mở dịch vụ và đổi được mà không phải triển khai lại; không khoá nào lộ ra phía trình duyệt [[ref:https://github.com/VNQuy94/vnpt-ekyc-poc]].
13. Nhật ký bỏ mọi trường tên chứa `token`, `secret`, `id_number`, `password`; kiểm bằng cách tìm các chuỗi đó trong 1.000 dòng gần nhất.
14. Tệp tải lên chỉ nhận `image/jpeg` và `image/png`, tối đa 8 MB, nhận dạng bằng mã đầu tệp, đổi tên, quét mã độc trước khi hiển thị lại.
15. `audit_logs` chặn `UPDATE` và `DELETE` ở cả hai tầng, tác vụ kiểm chuỗi băm chạy bảy đêm liên tiếp [[ref:https://tracehold.ai/blog/immutable-audit-log-hmac-hash-chain/]]; lệnh khoá máy ép hai người duyệt bằng ràng buộc `CHECK` [[ref:https://www.designgurus.io/answers/detail/how-do-you-enforce-immutability-and-appendonly-audit-trails]].

## Phân công trong nhóm

| Vai trò | Trách nhiệm chính | Hạng mục phụ trách | Giờ mỗi tuần |
|---|---|---|---|
| Trưởng nhóm kỹ thuật | Chốt kiến trúc, rà soát mã, quyết định cắt phạm vi khi trễ | Tuần 1, 5, 9, 10; kiểm thử đồng thời và chịu tải | 12 |
| Lập trình viên dữ liệu và nghiệp vụ | Lược đồ, di trú, module `booking/` và `billing/`, webhook, tác vụ nền | Tuần 2, 3, 4, 5, 8 | 12 |
| Lập trình viên giao diện | Giao diện khách, ứng dụng nhân viên dạng PWA, trang quản trị, bốn biểu đồ | Tuần 3, 6, 7, 8, 9 | 10 |
| Kiểm thử và tài liệu | Kiểm thử đầu cuối, 12 kịch bản thủ công, danh mục endpoint, sổ tay quy trình | Tuần 4, 7, 10, 11, 12 | 8 |
| Vận hành và hạ tầng | Máy chủ, sao lưu và diễn tập khôi phục, ảnh hệ điều hành chuẩn, cài EOS và SEB, đo pin | Tuần 1, 10, 11, 12 và việc đội máy | 6 |
{caption: Phân công năm vai trong nhóm, kèm hạng mục phụ trách và số giờ cam kết mỗi tuần.}
{widths: 3,7,5,2}
{right: 4}
{note: Tổng công 12 tuần khoảng 576 giờ **[Ước lượng của nhóm]**, cao hơn mức 200 đến 400 giờ mà nghiên cứu nội bộ ước cho một hệ tương đương.}

Vai vận hành giữ giờ thấp trong 12 tuần lập trình nhưng lên khoảng 4 giờ mỗi ngày trong tuần thi, đúng mô hình một người chuyên trách quản lý đội máy mà các chương trình cho mượn laptop trong trường đại học khuyến nghị [[ref:https://journal.code4lib.org/articles/5876]]. Trong tuần thi, vai này trực tại chỗ cùng máy dự phòng, vì cam kết đổi máy là kỳ vọng mặc định của thị trường Đà Nẵng [[ref:https://danang.plus/thue-laptop/]]. Hai nguyên tắc cứng: không ai tự trộn nhánh của mình, và không phát hành trong khoảng 06:00 đến 12:00 của ngày có lịch thi.

## Rủi ro kỹ thuật và phương án dự phòng

| # | Rủi ro | Dấu hiệu sớm | Phương án thay thế |
|---|---|---|---|
| 1 | Dịch vụ đối soát VietQR không nhận hồ sơ hộ kinh doanh | Hết tuần 3 chưa có tài khoản thử; nhà cung cấp đòi giấy tờ hộ kinh doanh không có | Chuyển sang mã QR tĩnh cộng đối soát tay: khách ghi `orders.code` làm nội dung, người trực khớp bằng `POST /api/admin/payments/reconcile`. Endpoint này có trong tuần 5 **chính vì nó là phương án dự phòng**; đổi lại phải có người trực suốt khung giờ nhận đơn |
| 2 | Xác minh danh tính thuê ngoài quá đắt so với doanh thu bình quân 144.100đ mỗi lượt | Báo giá vượt 3.000đ mỗi lượt gọi, hoặc đòi cam kết số lượng tối thiểu [[ref:https://docs-vision.fpt.ai/ekyc/I-introduction/gioi-thieu/]] [[ref:https://ekyc.vnpt.vn/vi/idcheck]] | Giữ lớp sàng lọc rẻ nhất là email `@fpt.edu.vn` cộng mã số sinh viên, rồi xác minh tại quầy lần đầu: đối chiếu căn cước với khuôn mặt, chụp ảnh khách cầm thẻ sinh viên, **không giữ giấy tờ**. Chỉ bật eKYC tự động khi vượt 60 lượt mỗi tháng |
| 3 | Máy chủ thuê không cho cài `btree_gist`, hoặc lớp truy cập dữ liệu không đỡ kiểu `tstzrange` | `CREATE EXTENSION` báo lỗi quyền ngay tuần 1; `drizzle-kit` sinh di trú sai kiểu cột | Đổi sang máy chủ ảo tự quản chạy PostgreSQL trong Docker. Nếu lớp truy cập vướng thì viết phần khoảng thời gian bằng SQL thô; cùng lắm lùi về khoá bi quan `SELECT ... FOR UPDATE SKIP LOCKED`, chấp nhận mất lưới an toàn cấp cơ sở dữ liệu [[ref:https://medium.com/javarevisited/booking-system-with-pessimistic-locks-4ec107e4bd5]] |
| 4 | Sóng khu vực phòng thi yếu, không đẩy được 6 ảnh đúng lúc bàn giao | Diễn tập tuần 11 cho thời gian bàn giao vượt mục tiêu 8 phút mỗi khách vì chờ tải ảnh | Chốt biên bản ngoại tuyến: ghi vào `IndexedDB`, sinh mã băm ngay trên máy, đẩy lên sau. Biên bản có hiệu lực từ lúc hai bên ký, không từ lúc ảnh lên tới máy chủ. Phương án cuối là biên bản giấy kèm ảnh điện thoại, nhập lại trong ngày |
| 5 | Nhóm trượt tiến độ vì lịch học và kỳ thi của chính các thành viên | Hết tuần 6 chưa đạt mốc khách tự đặt và trả tiền; yêu cầu trộn mã tồn đọng quá 5 | Cắt phạm vi theo danh sách xếp hạng sẵn, bỏ lần lượt: bốn biểu đồ báo cáo, trang bảng giá, tự động hoá quá hạn, kênh Zalo; thay tạm bằng `psql` và bảng tính. **Không bao giờ cắt**: chống trùng lịch, khử trùng lặp thanh toán, đủ 6 ảnh biên bản, nhật ký kiểm toán |
{caption: Năm rủi ro kỹ thuật của giai đoạn lập trình, kèm dấu hiệu sớm và phương án thay thế đã chuẩn bị trước.}
{widths: 1,4,5,10}

:::risk Điều nhóm chưa chứng minh được
Ba con số phải đo bằng chính đợt chạy thử tuần 11: độ trễ thật từ lúc tiền vào tài khoản tới lúc webhook về, giá mỗi lượt gọi eKYC, và thời gian bàn giao khi có 20 người xếp hàng cùng lúc. Nếu độ trễ webhook vượt 5 phút thì cam kết hoàn cọc trong 5 phút phải sửa thành con số đo được. Chuẩn xoá dữ liệu mà nhóm dự định dẫn là NIST SP 800-88 Revision 1 **[Cần kiểm chứng]**: chưa mở được bản gốc.
:::
