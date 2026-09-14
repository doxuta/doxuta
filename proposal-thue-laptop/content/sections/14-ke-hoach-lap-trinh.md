## Lộ trình 12 tuần

Mười hai tuần neo vào một mốc có thật: bắt đầu đầu học kỳ Fall và kết thúc ngay trước đợt thi cuối kỳ. Người phụ trách viết tắt theo vai: **TK** trưởng nhóm kỹ thuật, **DL** lập trình viên dữ liệu và nghiệp vụ, **GD** lập trình viên giao diện, **KT** kiểm thử và tài liệu, **VH** vận hành và hạ tầng.

<<<landscape>>>

| Tuần | Mục tiêu | Bàn giao | Tiêu chí hoàn thành đo được | Ai |
|---|---|---|---|---|
| 1 | Khung và môi trường | Kho mã, `docker compose` với `postgres:17` và `redis:7`, quy trình dựng GitHub Actions, `.env.example` | Máy mới dựng xong dưới 10 phút; `CREATE EXTENSION btree_gist` chạy được **trên chính máy chủ ảo sẽ thuê** | TK, VH |
| 2 | Cụm dữ liệu đặt thuê | `users`, `kyc_profiles`, `device_models`, `devices`, `exam_slots`, `inventory_holds`, `orders`, tệp di trú, `seed.ts` | Di trú chạy sạch từ cơ sở dữ liệu rỗng; seed sinh đúng 5 máy nhóm A, 4 nhóm B, 1 nhóm C; hai lệnh chèn chồng khung giờ trả mã lỗi `23P01` [[ref:https://chat2db.ai/resources/blog/postgres-exclusion-constraints-guide]] | DL, TK |
| 3 | Máy trạng thái và nhật ký | Bảng chuyển trạng thái đơn và máy, `audit_logs` nối chuỗi băm, đăng nhập liên kết một lần | 13 trạng thái đơn và 9 trạng thái máy khớp sơ đồ chương 10; trigger chặn `UPDATE` và `DELETE` trên `audit_logs` [[ref:https://www.designgurus.io/answers/detail/how-do-you-enforce-immutability-and-appendonly-audit-trails]] | DL, GD |
| 4 | Giữ suất kho | `GET /api/availability`, `POST /api/holds` có `Idempotency-Key`, tác vụ nhả suất hết hạn | 20 yêu cầu song song vào suất cuối cho đúng 1 lần thành công; suất quá 10 phút tự chuyển `cancelled` trong 60 giây, **không dòng nào bị xoá** | DL, KT |
| 5 | Tiền vào | `POST /api/orders` sinh VietQR, `POST /api/webhooks/payment` kiểm HMAC, bảng `payments`, trang đối soát tay | Gửi lại một webhook 10 lần chỉ sinh 1 dòng `payments` [[ref:https://stripe.com/blog/idempotency]]; đơn sang `paid` dưới 30 giây kể từ khi nhận báo tiền | DL, TK |
| 6 | Khách đi hết luồng đặt | eKYC bản thử, hợp đồng điện tử, `outbox_messages`, ba màn hình khách | 5 sinh viên ngoài nhóm tự đặt xong, mỗi người dưới 4 phút; không lời gọi ra ngoài nào nằm trong giao dịch cơ sở dữ liệu [[ref:https://milanjovanovic.tech/blog/implementing-the-outbox-pattern]] | GD, DL |
| 7 | Bàn giao máy | Ứng dụng nhân viên dạng PWA, `assign`, tải 6 ảnh ký sẵn, `handover` | Chốt biên bản khi mất mạng rồi đồng bộ lại không mất ảnh, không sinh biên bản trùng; thiếu 1 ảnh trả `422`; mã băm khớp tệp trên kho [[ref:https://www.locatorx.com/blog/the-truth-about-asset-records-why-immutability-is-the-foundation-of-a-verifiable-chain-of-custody]] | GD, KT |
| 8 | Thu hồi và hoàn cọc | `return`, `inspection`, `swap`, hoàn cọc, phí trả trễ, quét đơn quá hạn | Hoàn cọc dưới 5 phút ở cả 10 lần thử, đúng cam kết công khai; hoàn cọc lần hai bị chặn; phí trễ chạm trần 200.000đ mỗi ngày | DL, GD |
| 9 | Quản trị và báo cáo | Kho máy, `pricing_rules`, bốn biểu đồ, lệnh khoá hai người duyệt, tra nhật ký | Mọi `/api/admin/*` trả `403` với vai `student`; người xin khoá máy không tự duyệt được lệnh của mình | GD, TK |
| 10 | Làm cứng | Danh sách kiểm tra bảo mật 15 mục, giới hạn tần suất, quét phụ thuộc, đo tải | 15 trên 15 mục tích kèm bằng chứng; độ trễ phân vị 95 của `GET /api/availability` dưới 800 ms với 50 người dùng ảo | TK, KT |
| 11 | Chạy thử thật có kiểm soát | 20 đơn thật của sinh viên tình nguyện trong một đợt progress test, diễn tập ứng cứu và khôi phục | 20 trên 20 đơn đi hết vòng đời tới `closed`; một lần đổi máy đo được dưới 15 phút; khôi phục sao lưu bấm giờ dưới 90 phút | Cả nhóm |
| 12 | Sửa lỗi và bàn giao | Sửa lỗi tuần 11, sổ tay vận hành, đổi toàn bộ khoá bí mật | Không còn lỗi mức chặn; thời gian khôi phục trong tuần thi đo được dưới 30 phút | Cả nhóm |
{caption: Lộ trình 12 tuần chia bốn giai đoạn, mỗi tuần một tiêu chí hoàn thành đo được bằng số hoặc bằng một phép thử.}
{widths: 1,3,6,9,2}

<<<portrait>>>

:::ok Mốc quan trọng nhất
**Cuối tuần 9 là bản chạy được đầu tiên có thể nhận đơn thật**: một đơn đi trọn vòng đời từ đặt, trả tiền, ký hợp đồng, nhận máy có biên bản ảnh, trả máy, hoàn cọc, tới đóng đơn. Ba tuần cuối không thêm tính năng, chỉ làm cứng và chạy thử.
Cuối tuần 6 đã có bản khách tự đặt và trả tiền được, nhưng khâu bàn giao vẫn làm trên biên bản giấy rồi nhập tay lại. Nhóm chấp nhận vận hành lai như vậy nếu đợt thi đến sớm hơn lịch.
:::

## Thứ tự làm và lý do

Thứ tự trên sắp theo **đường găng**, tức chuỗi việc mà chậm một mắt xích là chậm cả dự án: `btree_gist` chạy được trên máy chủ đã thuê (tuần 1) chặn ràng buộc `EXCLUDE USING gist` trên `inventory_holds` (tuần 2); bảng đó chặn `POST /api/holds` (tuần 4); không có suất giữ thì không có gì gắn tiền vào (tuần 5); đơn chưa sang `paid` thì không có gì để gán máy và bàn giao (tuần 7); chưa bàn giao thì không có gì để thu hồi (tuần 8); và chỉ khi đủ chuỗi đó mới chạy thử thật được (tuần 11).

Ràng buộc cơ sở dữ liệu nằm ngay tuần đầu vì đó là rủi ro lớn nhất và rẻ nhất khi phát hiện sớm: đổi nhà cung cấp ở tuần 1 tốn một buổi, đổi ở tuần 8 là viết lại cả tầng chống trùng lịch [[ref:https://dev.to/franckpachot/postgresql-exclude-constraints-for-better-concurrency-than-serializable-pob]]. Quy ước biên nửa mở `[)` và khoảng đệm 90 phút quay vòng cũng phải chốt trước dòng mã đầu tiên tính giờ, vì đổi quy ước biên giữa chừng là nguồn lỗi kinh điển [[ref:https://www.jusdb.com/blog/postgresql-range-types-exclusion-constraints]].

Hai việc cố tình nằm ngoài đường găng: trang quản trị đẩy về tuần 9 vì chín tuần đầu xem kho bằng `psql` và bảng tính là đủ; việc dựng ảnh hệ điều hành chuẩn, cài EOS Client và Safe Exam Browser, đo pin bằng `powercfg /batteryreport` do vai VH làm song song từ tuần 1. Ngược lại, hồ sơ đăng ký dịch vụ đối soát VietQR và hồ sơ dùng thử eKYC nộp ngay tuần 1 dù tới tuần 5 và tuần 6 mới cần, vì nhóm không kiểm soát được tốc độ trả lời của nhà cung cấp.

## Định nghĩa hoàn thành

Một hạng mục chỉ được gạch khỏi bảng lộ trình khi đủ bảy điều kiện, không phải khi chạy được trên máy người viết.

1. Có kiểm thử tự động, trong đó ít nhất một ca cho đường thất bại chứ không chỉ đường thành công.
2. Toàn bộ kiểm thử xanh trên GitHub Actions, chạy trên `postgres:17` thật chứ không trên cơ sở dữ liệu giả lập.
3. Đã qua rà soát mã của một người khác; không ai tự trộn nhánh của mình vào `main`.
4. Quy tắc nghiệp vụ mới được ép ở tầng thấp nhất có thể: ràng buộc, rồi trigger, rồi kiểm tra ở máy chủ, cuối cùng mới tới giao diện.
5. Có tài liệu: một đoạn trong `README`, một dòng trong danh mục endpoint, và một bước trong sổ tay nếu là việc vận hành.
6. Đã triển khai và chạy được trên môi trường thử nghiệm.
7. Đã thử với dữ liệu thật: một hộp thư `@fpt.edu.vn` thật, một lần chuyển khoản thật dù chỉ 2.000đ, một chiếc máy thật trong đội 10 máy.

## Chiến lược kiểm thử

| Loại | Phạm vi | Công cụ | Ai viết | Chạy khi nào |
|---|---|---|---|---|
| Đơn vị | Tính tiền thuê, phí trễ, bậc cọc theo `trust_score`, dựng chuỗi VietQR, tính mã băm ảnh | Vitest | DL, GD | Mỗi lần đẩy mã |
| Tích hợp cơ sở dữ liệu | Ràng buộc `EXCLUDE`, trigger nhật ký, 14 quy tắc bất biến R01 đến R14 ở chương 10 | Vitest trên `postgres:17` trong Docker | DL | Mỗi yêu cầu trộn mã |
| Đồng thời | Đặt trùng suất cuối, webhook lặp, bấm hoàn cọc hai lần | Kịch bản Node gửi song song bằng `Promise.all`, hai phiên `psql` chạy tay | TK | Mỗi yêu cầu trộn mã và trước mỗi lần phát hành |
| Đầu cuối | Bốn hành trình: đặt và trả tiền, bàn giao, trả máy và hoàn cọc, xử lý quá hạn | Playwright, chạy cả bố cục điện thoại | KT | Hằng đêm và trước mỗi lần phát hành |
| Chịu tải | `GET /api/availability` và `POST /api/holds` ở 20 lượt mỗi phút, gấp 30 lần nhu cầu bình quân năm 1 | k6 | TK | Tuần 10 và trước mỗi đợt thi |
| Thủ công theo kịch bản | 12 kịch bản viết sẵn, gồm khách ghi sai nội dung chuyển khoản và khách mất mạng giữa chừng | Danh sách in ra, tick bằng bút | KT | Trước mỗi lần phát hành lên môi trường thật |
| Diễn tập vận hành | Đổi máy khẩn theo quy trình SOP-04, khôi phục sao lưu bấm giờ, mất máy chủ giữa ngày thi | Đồng hồ bấm giờ và biên bản | VH | Trước mỗi đợt thi cuối kỳ |
{caption: Bảy loại kiểm thử của ExamLap, kèm phạm vi, công cụ, người viết và thời điểm chạy.}
{widths: 3,7,4,2,4}
{note: Nhóm không đặt mục tiêu phần trăm dòng mã được phủ. Mục tiêu là 14 quy tắc bất biến ở chương 10 đều có ít nhất một ca kiểm thử cố tình vi phạm chúng.}

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
{caption: Ca kiểm thử đồng thời cho bài toán đặt trùng, vì lỗi này không lộ ra khi bấm tay từng lần.}

Mười hai ca kiểm thử bắt buộc phải có, viết dưới dạng cho trước, khi, thì.

1. **Cho trước** ca thi chỉ còn một máy nhóm A ở trạng thái `ready`, **khi** 20 yêu cầu `POST /api/holds` gửi song song trong 200 mili giây, **thì** đúng một yêu cầu trả `201`, 19 yêu cầu trả `409 SLOT_SOLD_OUT`.
2. **Cho trước** một đơn chiếm máy tới 12:00 và `period` đã cộng 90 phút quay vòng, **khi** chèn suất mới bắt đầu 13:00, **thì** nhận mã `23P01`; suất bắt đầu 13:30 thì chèn được [[ref:https://www.odoo.com/documentation/18.0/applications/sales/rental.html]].
3. **Cho trước** một `Idempotency-Key` đã dùng, **khi** gửi lại `POST /api/orders` cùng thân yêu cầu, **thì** nhận đúng phản hồi cũ và chỉ có một dòng `orders`; thân khác thì nhận `422 IDEMPOTENCY_KEY_REUSED` [[ref:https://brandur.org/idempotency-keys]].
4. **Cho trước** một giao dịch đã xử lý, **khi** dịch vụ đối soát gửi lại cùng gói tin 10 lần, **thì** vẫn một dòng `payments` và đơn chỉ đổi trạng thái một lần [[ref:https://matheuspalma.com/blog/outbound-webhook-delivery-signing-retries-dead-letters]].
5. **Cho trước** webhook có chữ ký HMAC sai hoặc lệch giờ quá 5 phút, **khi** gọi vào hệ thống, **thì** bị từ chối, không ghi dòng nào và sinh một cảnh báo.
6. **Cho trước** suất giữ tạo lúc 08:00 hết hạn 08:10, **khi** tác vụ nền chạy lúc 08:11, **thì** dòng đó sang `cancelled`, đơn sang `hold_expired`, tổng số dòng không giảm, máy hiện lại trong `GET /api/availability`.
7. **Cho trước** biên bản bàn giao chỉ có 5 ảnh, **khi** nhân viên bấm chốt, **thì** nhận `422` và đơn vẫn ở `assigned`.
8. **Cho trước** nhân viên chốt biên bản lúc mất sóng, **khi** có sóng trở lại, **thì** đủ 6 ảnh được đẩy lên, mã băm khớp, không sinh biên bản thứ hai cho cùng đơn.
9. **Cho trước** đơn đã hoàn cọc thành công, **khi** bấm hoàn cọc lần hai, **thì** nhận `409` và vẫn chỉ một dòng `payments` chiều ra ở trạng thái `succeeded`.
10. **Cho trước** đơn trả trễ 95 phút, **khi** chốt biên bản thu hồi, **thì** phí trễ đúng 80.000đ; đơn trễ cả ngày dừng ở trần 200.000đ.
11. **Cho trước** sinh viên A đã đăng nhập, **khi** gọi `GET /api/orders/{code}` bằng mã đơn của sinh viên B, **thì** nhận `404` chứ không phải `403`, để không lộ việc mã đơn đó tồn tại.
12. **Cho trước** quản trị viên vừa tạo lệnh khoá màn hình, **khi** chính người đó bấm duyệt, **thì** bị từ chối và lần từ chối cũng vào `audit_logs`.

## Danh sách kiểm tra bảo mật trước khi mở cho người thật dùng

Mười lăm mục tích trong tuần 10, mỗi mục kèm bằng chứng là ảnh chụp màn hình, tệp nhật ký hoặc một ca kiểm thử. Không đủ thì không mở cho sinh viên ngoài nhóm dùng.

1. Ép HTTPS trên toàn bộ đường dẫn, bật HSTS; gọi bằng `http://` phải bị chuyển hướng chứ không phục vụ nội dung.
2. Không lưu mật khẩu dạng thô ở bất kỳ đâu; vai sinh viên dùng liên kết đăng nhập một lần, vai quản trị bắt buộc lớp xác thực thứ hai.
3. Mã đăng nhập sống tối đa 10 phút và dùng đúng một lần; thử dùng lại phải thất bại.
4. Giới hạn tần suất đăng nhập 3 lần mỗi giờ cho mỗi hộp thư, trả `429` kèm `Retry-After`.
5. Kiểm quyền ở mọi endpoint phía máy chủ: chạy kịch bản gọi lần lượt toàn bộ danh mục endpoint bằng phiên vai `student` rồi đối chiếu bảng phân quyền.
6. Truy vấn đơn thuê của sinh viên mang điều kiện chủ sở hữu ngay trong câu lệnh SQL, không lọc sau khi đã lấy dữ liệu về.
7. Ảnh giấy tờ và ảnh khuôn mặt mã hoá khi lưu, để trong khoang riêng, chỉ phục vụ qua đường dẫn ký sẵn hạn 15 phút.
8. Cột `kyc_profiles.images_purge_at` có giá trị ở mọi hồ sơ và tác vụ xoá tự động đã chạy đúng ít nhất một lần, xoá ảnh sau 90 ngày.
9. Không bảng nào chứa số căn cước thô: quét kết xuất `pg_dump` bằng biểu thức chính quy, kết quả phải rỗng.
10. Sao lưu hằng ngày **đã thử khôi phục thật** lên một máy trống, có bấm giờ và biên bản; sao lưu chưa từng khôi phục coi như chưa có.
11. Không tệp `.env` nào trong Git; quét lịch sử kho mã tìm khoá bí mật và xử lý hết kết quả.
12. Khoá ký webhook, khoá eKYC và khoá kho ảnh đã đổi một lần ngay trước khi mở dịch vụ, đổi được mà không phải triển khai lại.
13. Nhật ký không chứa dữ liệu nhạy cảm: bộ lọc bỏ mọi trường tên chứa `token`, `secret`, `id_number`, `password`, kiểm bằng cách tìm các chuỗi đó trong 1.000 dòng gần nhất.
14. Tệp tải lên chỉ nhận `image/jpeg` và `image/png`, tối đa 8 MB, nhận dạng bằng mã đầu tệp, đổi tên, qua hàng đợi quét mã độc trước khi hiển thị lại.
15. `audit_logs` chặn `UPDATE` và `DELETE` ở cả hai tầng và tác vụ kiểm chuỗi băm chạy được bảy đêm liên tiếp [[ref:https://tracehold.ai/blog/immutable-audit-log-hmac-hash-chain/]]; lệnh khoá máy ép hai người duyệt bằng ràng buộc `CHECK`.

## Phân công trong nhóm

| Vai trò | Trách nhiệm chính | Hạng mục phụ trách | Giờ mỗi tuần |
|---|---|---|---|
| Trưởng nhóm kỹ thuật | Chốt kiến trúc, rà soát mã, quyết định cắt phạm vi khi trễ, giữ khoá bí mật cùng một người nữa | Tuần 1, 5, 9, 10; kiểm thử đồng thời và chịu tải | 12 |
| Lập trình viên dữ liệu và nghiệp vụ | Lược đồ, di trú, module `booking/` và `billing/`, webhook, tác vụ nền | Tuần 2, 3, 4, 5, 8 | 12 |
| Lập trình viên giao diện | Giao diện khách, ứng dụng nhân viên dạng PWA, trang quản trị, bốn biểu đồ | Tuần 3, 6, 7, 8, 9 | 10 |
| Kiểm thử và tài liệu | Kiểm thử đầu cuối, 12 kịch bản thủ công, danh mục endpoint, sổ tay quy trình | Tuần 4, 7, 10, 11, 12 | 8 |
| Vận hành và hạ tầng | Máy chủ, sao lưu và diễn tập khôi phục, ảnh hệ điều hành chuẩn, cài EOS và Safe Exam Browser, đo pin | Tuần 1, 10, 11, 12 và toàn bộ việc đội máy | 6 |
{caption: Phân công năm vai trong nhóm, kèm hạng mục phụ trách và số giờ cam kết mỗi tuần.}
{widths: 3,7,5,2}
{right: 4}
{note: Tổng công 12 tuần khoảng 576 giờ **[Ước lượng của nhóm]**, cao hơn mức 200 đến 400 giờ mà nghiên cứu nội bộ ước cho một hệ tương đương; nhóm lấy 576 giờ làm mốc lập kế hoạch.}

Vai vận hành giữ số giờ thấp trong 12 tuần lập trình nhưng lên khoảng 4 giờ mỗi ngày trong tuần thi, đúng mô hình một người chuyên trách quản lý đội máy mà các chương trình cho mượn laptop trong trường đại học khuyến nghị [[ref:https://journal.code4lib.org/articles/5876]]. Hai nguyên tắc cứng: không ai tự trộn nhánh của mình, và không phát hành trong khoảng 06:00 đến 12:00 của ngày có lịch thi.

## Rủi ro kỹ thuật và phương án dự phòng

| # | Rủi ro | Dấu hiệu sớm | Phương án thay thế |
|---|---|---|---|
| 1 | Dịch vụ đối soát VietQR không nhận hồ sơ hộ kinh doanh hoặc duyệt quá chậm | Hết tuần 3 chưa có tài khoản thử; nhà cung cấp đòi giấy tờ mà hộ kinh doanh không có | Chuyển sang mã QR tĩnh cộng đối soát tay: khách ghi `orders.code` làm nội dung chuyển khoản, người trực khớp bằng `POST /api/admin/payments/reconcile` trong 5 phút. Endpoint này nằm trong phạm vi tuần 5 **chính vì nó là phương án dự phòng**. Đổi lại phải có người trực suốt khung giờ nhận đơn |
| 2 | Xác minh danh tính thuê ngoài quá đắt so với doanh thu bình quân 144.100đ mỗi lượt | Báo giá vượt 3.000đ mỗi lượt gọi, hoặc đòi cam kết số lượng tối thiểu | Giữ lớp sàng lọc rẻ nhất là email `@fpt.edu.vn` cộng mã số sinh viên, rồi xác minh tại quầy lần đầu: đối chiếu căn cước với khuôn mặt, chụp ảnh khách cầm thẻ sinh viên, **không giữ giấy tờ**. Chỉ bật eKYC tự động khi vượt 60 lượt mỗi tháng, lúc đó chi phí nhân công đã lớn hơn chi phí gọi dịch vụ |
| 3 | Máy chủ thuê không cho cài `btree_gist`, hoặc lớp truy cập dữ liệu không đỡ được kiểu `tstzrange` | `CREATE EXTENSION` báo lỗi quyền ngay tuần 1; `drizzle-kit` sinh di trú sai kiểu cột | Đổi sang máy chủ ảo tự quản chạy PostgreSQL trong Docker, vốn đã nằm trong thiết kế triển khai. Nếu lớp truy cập vướng thì viết phần khoảng thời gian bằng SQL thô; cùng lắm lùi về khoá bi quan `SELECT ... FOR UPDATE SKIP LOCKED`, chấp nhận mất lưới an toàn cấp cơ sở dữ liệu [[ref:https://medium.com/javarevisited/booking-system-with-pessimistic-locks-4ec107e4bd5]] |
| 4 | Sóng khu vực phòng thi yếu, ứng dụng nhân viên không đẩy được 6 ảnh đúng lúc bàn giao | Diễn tập tuần 11 cho thời gian bàn giao vượt mục tiêu 8 phút mỗi khách vì chờ tải ảnh | Chốt biên bản ngoại tuyến: ghi vào `IndexedDB`, sinh mã băm ngay trên máy, đẩy lên sau. Biên bản có hiệu lực từ lúc hai bên ký, không từ lúc ảnh lên tới máy chủ. Phương án cuối là biên bản giấy kèm ảnh chụp điện thoại, nhập lại trong ngày |
| 5 | Nhóm trượt tiến độ vì lịch học và kỳ thi của chính các thành viên | Hết tuần 6 chưa đạt mốc khách tự đặt và trả tiền; số yêu cầu trộn mã tồn đọng quá 5 | Cắt phạm vi theo danh sách xếp hạng sẵn, bỏ lần lượt: bốn biểu đồ báo cáo, trang bảng giá, tự động hoá quá hạn, kênh Zalo; thay tạm bằng `psql`, bảng tính dùng chung và nhóm trực. **Không bao giờ cắt**: ràng buộc chống trùng lịch, khử trùng lặp thanh toán, đủ 6 ảnh biên bản, nhật ký kiểm toán |
{caption: Năm rủi ro kỹ thuật lớn nhất của giai đoạn lập trình, kèm dấu hiệu sớm và phương án thay thế đã chuẩn bị trước.}
{widths: 1,4,5,10}

:::risk Điều nhóm chưa chứng minh được
Ba con số phải đo bằng chính đợt chạy thử tuần 11: độ trễ thật từ lúc tiền vào tài khoản tới lúc webhook về, giá mỗi lượt gọi eKYC, và thời gian bàn giao thật khi có 20 người xếp hàng cùng lúc. Nếu độ trễ webhook vượt 5 phút thì cam kết hoàn cọc trong 5 phút phải sửa thành con số đo được, chứ không giữ con số đẹp mà không đạt.
Chuẩn xoá dữ liệu giữa hai lượt thuê mà nhóm dự định dẫn là NIST SP 800-88 Revision 1 **[Cần kiểm chứng]**: chưa mở được bản gốc, phải đối chiếu trước khi in cam kết đó lên tài liệu bán hàng.
:::
