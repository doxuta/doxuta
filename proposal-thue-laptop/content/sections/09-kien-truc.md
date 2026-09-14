## Tổng thể kiến trúc

Hệ thống ExamLap được dựng theo kiểu **một khối triển khai duy nhất, dữ liệu tập trung ở PostgreSQL, và mọi việc nặng nhọc đẩy sang tác vụ nền**. Sơ đồ dưới đây là bản vẽ kiến trúc mà nhóm sẽ lập trình theo.

<<<landscape>>>

![Kiến trúc hệ thống ExamLap gồm bốn lớp: người dùng, ứng dụng, dữ liệu và dịch vụ ngoài, với đường đi của yêu cầu từ trình duyệt qua CDN vào ứng dụng rồi xuống cơ sở dữ liệu.](assets/diagrams/04-kien-truc.png){w=0}{src: Nguồn: nhóm tác giả.}

<<<portrait>>>

Đọc sơ đồ từ trái sang phải theo đúng đường đi của một yêu cầu.

**Lớp người dùng** có ba loại thiết bị khác nhau chứ không phải ba ứng dụng khác nhau. Sinh viên dùng trình duyệt trên điện thoại, vì phần lớn lượt đặt máy xảy ra ngoài giờ hành chính và trên 4G. Nhân viên giao nhận dùng cùng một ứng dụng web nhưng cài dưới dạng PWA để chụp ảnh biên bản bàn giao được ngay cả khi sóng chập chờn, ảnh xếp hàng trong `IndexedDB` rồi đẩy lên sau. Quản trị viên dùng trình duyệt máy tính cho các màn hình bảng biểu dày. Ba vai này dùng chung một mã nguồn, chỉ khác quyền và khác bố cục.

**CDN và tường lửa ứng dụng** đứng trước tất cả. Khối này làm ba việc: ép HTTPS, phục vụ tệp tĩnh và ảnh máy, và chặn dò quét. Quan trọng hơn, nó là chỗ đặt giới hạn tần suất theo địa chỉ IP và theo tài khoản, vì hai điểm đầu yếu nhất của hệ thống là trang tra máy trống và điểm nhận webhook thanh toán.

**Lớp ứng dụng** gồm ba khối chạy chung một máy chủ ảo. Khối giao diện dựng trang bằng Next.js. Khối API giữ toàn bộ quy tắc nghiệp vụ: xác thực, phân quyền theo vai trò, kiểm tra máy trạng thái đơn thuê, và là nơi duy nhất được phép ghi vào cơ sở dữ liệu. Khối tác vụ nền chạy các việc theo lịch và các việc chậm: nhả suất kho đã hết hạn giữ, nhắc hạn trả máy, hoàn cọc, gửi thông báo, đối chiếu nhật ký thiết bị.

**Lớp dữ liệu** có ba kho. PostgreSQL giữ toàn bộ dữ liệu nghiệp vụ và là nguồn sự thật duy nhất. Redis chỉ giữ hàng đợi tác vụ, phiên đăng nhập và bộ đếm giới hạn tần suất, tức là những thứ mất đi thì phiền nhưng không hỏng nghiệp vụ. Kho ảnh giữ ảnh biên bản bàn giao, ảnh eKYC và ảnh hiện trạng máy, tách khỏi cơ sở dữ liệu để không phình tệp sao lưu.

**Lớp dịch vụ ngoài** có bốn đối tác. Dịch vụ đối soát VietQR báo về khi tiền chuyển khoản đã tới tài khoản của ExamLap. Nhà cung cấp eKYC đối chiếu ảnh căn cước với khuôn mặt sống. Máy chủ MDM nhận tín hiệu check-in của từng máy và thực thi lệnh khoá màn hình. Kênh Zalo và email gửi thông báo cho khách.

Ba đường mũi tên hai chiều trên sơ đồ là ba chỗ dễ hỏng nhất, và nhóm xử lý chúng theo cùng một nguyên tắc: **không bao giờ để một cuộc gọi ra bên ngoài nằm trong một giao dịch cơ sở dữ liệu**. Với thanh toán, API tạo bản ghi `payments` rồi trả mã QR động; khi tiền về, dịch vụ đối soát gọi vào `POST /webhooks/payment`, hệ thống kiểm chữ ký HMAC, ghi thô vào `payments.raw_payload` với ràng buộc `UNIQUE (provider, provider_txn_id)` rồi trả HTTP 200 ngay, còn việc chuyển trạng thái đơn để tác vụ nền làm. Ràng buộc duy nhất này là lý do cổng thanh toán có gửi lại cùng một sự kiện mười lần thì đơn vẫn chỉ được cộng tiền một lần [[ref:https://matheuspalma.com/blog/outbound-webhook-delivery-signing-retries-dead-letters]]. Với thông báo, tác vụ nền đọc bảng `outbox_messages` được ghi trong **cùng giao dịch** với thay đổi trạng thái đơn, nên không có cảnh khách nhận xác nhận cho một đơn đã rollback [[ref:https://milanjovanovic.tech/blog/implementing-the-outbox-pattern]] [[ref:https://github.com/Zehelein/pg-transactional-outbox]].

## Vì sao chọn một khối thay vì vi dịch vụ

Quy mô cần phục vụ là **382 lượt thuê ca, ngày và tuần cộng 30 máy-tháng trong năm thứ nhất**, tức trung bình chưa tới hai lượt đặt mỗi ngày, dồn vào sáu đợt cao điểm mỗi năm theo lịch ba học kỳ của trường. Đội lập trình là bốn đến năm sinh viên làm ngoài giờ học. Trong bối cảnh đó, tách vi dịch vụ là một quyết định sai về mặt kỹ thuật chứ không chỉ là chuyện tốn công.

Lý do cụ thể, không phải khẩu hiệu. Thứ nhất, bài toán đắt nhất của hệ thống này là **không được cho thuê một chiếc máy hai lần trong cùng khung giờ**, và cách giải rẻ nhất là một ràng buộc ở cấp cơ sở dữ liệu chứ không phải một dịch vụ riêng. PostgreSQL cho phép viết ràng buộc `EXCLUDE USING gist` trên cặp `(device_id, period)` để chính máy chủ dữ liệu từ chối bản ghi chồng lịch, bất kể yêu cầu đến từ API, từ tác vụ nền hay từ một lần sửa tay trong `psql` [[ref:https://chat2db.ai/resources/blog/postgres-exclusion-constraints-guide]] [[ref:https://dev.to/franckpachot/postgresql-exclude-constraints-for-better-concurrency-than-serializable-pob]]. Ràng buộc đó chỉ hoạt động khi dữ liệu nằm chung một cơ sở dữ liệu. Tách kho máy và kho đơn thành hai dịch vụ là tự tay vứt bỏ công cụ mạnh nhất mình đang có, rồi phải dựng lại bằng Saga và bù trừ giao dịch, vốn là thứ được thiết kế cho hệ phân tán chứ không cho 400 lượt thuê một năm [[ref:https://microservices.io/patterns/data/saga.html]].

Thứ hai, tất cả hệ thống tham chiếu gần nhất đều là một khối. Snipe-IT, phần mềm quản lý tài sản có mô hình dữ liệu giống ExamLap nhất, là một ứng dụng Laravel đơn khối [[ref:https://github.com/grokability/snipe-it]]. Koha, hệ quản lý thư viện đang chạy ở hàng nghìn thư viện với lượng giao dịch lớn hơn nhiều, cũng vậy [[ref:https://raw.githubusercontent.com/Koha-Community/Koha/master/installer/data/mysql/kohastructure.sql]].

Thứ ba, chi phí vận hành. Một khối chạy trên một máy chủ ảo 160.000đ mỗi tháng. Cùng hệ thống đó tách thành năm dịch vụ cần thêm hàng đợi thông điệp, truy vết phân tán và ít nhất ba máy chủ ảo, đẩy chi phí hạ tầng vượt xa ngân sách 450.000đ mỗi tháng đã chốt trong mô hình tài chính.

Nhóm vẫn giữ **ranh giới module rõ ràng bên trong một khối**: bốn thư mục `booking/`, `inventory/`, `billing/`, `identity/`, mỗi module chỉ được gọi module khác qua một tệp `index.ts` công khai, và mỗi module sở hữu nhóm bảng riêng. Đây là chuẩn bị cho việc tách sau này mà không phải trả giá bây giờ.

:::note Điều kiện cụ thể để tách dịch vụ
Nhóm sẽ chỉ tách một module thành dịch vụ riêng khi có ít nhất một trong bốn dấu hiệu sau, đo được bằng số:
đội máy vượt 150 chiếc hoặc trên 500 lượt thuê mỗi tháng; hoặc thời gian dựng và kiểm thử vượt 15 phút làm nghẽn việc phát hành;
hoặc số lập trình viên thường trực vượt 8 người và các nhóm giẫm chân nhau trong cùng tệp; hoặc một module cần quy mô riêng biệt,
ví dụ máy chủ MDM phải nhận check-in của hàng nghìn máy mỗi 15 phút. Module tách đầu tiên gần như chắc chắn là MDM, vì nó có tải đều và không cần giao dịch chung với đơn thuê.
:::

## Lựa chọn công nghệ và lý do

Bảng dưới đây là toàn bộ quyết định công nghệ của dự án, kèm phương án đã cân nhắc và rủi ro của chính lựa chọn đã chọn. Bối cảnh ràng buộc: nhóm sinh viên, ngân sách hạ tầng dưới 500.000đ mỗi tháng, và mốc phải chạy thật vào đợt thi cuối kỳ gần nhất.

| Lớp | Công nghệ chọn | Đã cân nhắc | Lý do chọn | Rủi ro của lựa chọn |
|---|---|---|---|---|
| Ngôn ngữ và khung web | TypeScript trên Next.js 16, một khối dựng cả giao diện lẫn API | Laravel 13 với Livewire; Go với templ và HTMX | Sinh viên Đại học FPT đã quen JavaScript và React, nên chi phí học gần bằng không; một ngôn ngữ duy nhất cho cả hai đầu; dựng trang phía máy chủ tốt cho trang giới thiệu và SEO [[ref:https://nihardaily.com/56-nextjs-15-vs-laravel-when-to-choose-what-in-2025]] [[ref:https://www.adriano-junior.com/best-web-frameworks-2026]] | Laravel có sẵn hàng đợi, lịch chạy, xác thực và bảng quản trị Filament, nên đội một người ra sản phẩm nhanh hơn hẳn [[ref:https://wishtreetech.com/blogs/tech-stack/laravel-vs-next-js-which-framework-should-you-choose-for-your-full-stack-web-app/]]; chọn Next.js nghĩa là nhóm phải tự dựng bảng quản trị kho máy, ước thêm hai tuần công |
| Cơ sở dữ liệu | PostgreSQL 17, bật extension `btree_gist` | MySQL 8; MariaDB | MySQL **không có** ràng buộc `EXCLUDE` và không có kiểu range, nên không thể chống trùng lịch ở cấp dữ liệu. Bằng chứng: cả Koha lẫn LibreBooking đều chạy MySQL và cả hai đều phải kiểm tra trùng lịch bằng mã ứng dụng [[ref:https://raw.githubusercontent.com/Koha-Community/Koha/master/installer/data/mysql/kohastructure.sql]] [[ref:https://raw.githubusercontent.com/LibreBooking/app/master/database_schema/create-schema.sql]] [[ref:https://www.jusdb.com/blog/postgresql-range-types-exclusion-constraints]] | Hosting chia sẻ giá rẻ ở Việt Nam thiên về MySQL, nên phải thuê máy chủ ảo thay vì hosting; nhóm phải học kiểu `tstzrange` và ngữ nghĩa biên nửa mở `[)` |
| Lớp truy cập dữ liệu | Drizzle ORM, di trú bằng `drizzle-kit` | Prisma 8; viết SQL thuần | Prisma hỗ trợ kiểu range của PostgreSQL kém hơn, trong khi `tstzrange` là trung tâm của bài toán; Drizzle cho phép trộn SQL thô tự nhiên [[ref:https://amitavroy.com/articles/postgresql-gist-exclusion-constraintthe-database-evel-answer-to-double-bookings]] | Cộng đồng nhỏ hơn Prisma, ít tài liệu tiếng Việt; ràng buộc `EXCLUDE` vẫn phải viết bằng SQL thô trong tệp di trú |
| Hàng đợi và bộ nhớ đệm | Redis 7 với BullMQ cho tác vụ nền; Redis giữ phiên và bộ đếm giới hạn tần suất | Hàng đợi trên chính PostgreSQL bằng `FOR UPDATE SKIP LOCKED`; khoá phân tán Redis | Cần lịch chạy mỗi phút cho việc nhả suất kho hết hạn và nhắc hạn trả máy; BullMQ cho sẵn thử lại có giãn cách và hàng đợi chết | Thêm một tiến trình phải giám sát. Nhóm **không** dùng khoá phân tán Redis để chống trùng lịch, vì ràng buộc `EXCLUDE` đã giải triệt để và khoá Redis chỉ cần khi tồn kho nằm ngoài cơ sở dữ liệu [[ref:https://redis.io/tutorials/inventory-reservation-in-real-time-with-redis/]] |
| Lưu trữ ảnh | Kho đối tượng tương thích S3, đường dẫn ký sẵn có hạn 15 phút, mỗi ảnh lưu kèm mã băm SHA-256 trong cột `handover_photos.sha256` | Lưu ảnh trong PostgreSQL dạng `bytea`; lưu thẳng trên đĩa máy chủ ảo | Sáu ảnh mỗi lần bàn giao nhân hai chiều nhân 400 lượt là vài nghìn tệp mỗi năm; để trong cơ sở dữ liệu thì tệp sao lưu phình và thời gian khôi phục kéo dài; mã băm là bằng chứng ảnh chưa bị thay khi tranh chấp hư hỏng [[ref:https://tracehold.ai/blog/immutable-audit-log-hmac-hash-chain/]] | Phụ thuộc một nhà cung cấp ngoài; ảnh eKYC là dữ liệu cá nhân nhạy cảm nên bắt buộc mã hoá khi lưu và tự xoá sau 90 ngày |
| Xác thực | Đăng nhập bằng email `@fpt.edu.vn` với liên kết một lần, phiên lưu trong Redis, phân quyền ba vai `student`, `staff`, `admin`; eKYC do bên thứ ba thực hiện | Mật khẩu truyền thống; đăng nhập bằng Google; tự làm đối chiếu khuôn mặt | Bắt buộc email trường là lớp sàng lọc đầu vào rẻ nhất và mạnh nhất; sinh viên Đại học FPT đã quen mô hình đăng nhập và từ vựng "Dashboard" của hệ thống mượn máy nội bộ [[ref:https://it-hcm.fpt.edu.vn/articles.php?news=huong-dan-muon-laptop-cua-sinh-vien-trong-truong&id=56]]; kiểm tra khuôn mặt sống là bài toán chuyên ngành, nhà cung cấp trong nước có sẵn tài liệu tích hợp [[ref:https://docs-vision.fpt.ai/ekyc/I-introduction/gioi-thieu/]] [[ref:https://ekyc.vnpt.vn/vi/idcheck]] | Phụ thuộc máy chủ thư của trường; giá eKYC theo lượt chưa xác minh được, nếu cao hơn dự kiến thì phải chuyển sang xác minh một lần cho cả học kỳ |
| Thư viện máy trạng thái | Bảng `order_state_transitions(from_state, event, to_state)` trong cơ sở dữ liệu, cộng ràng buộc `CHECK` trên `orders.status`, mọi lần chuyển ghi một dòng vào `audit_logs` | XState 5; tự viết `switch` rải rác | Vòng đời đơn có 13 trạng thái phẳng, không phân cấp, không song song. XState mạnh cho giao diện phức tạp nhưng chi phí học cao và khó bảo vệ trước hội đồng hơn một bảng dữ liệu đọc được bằng mắt [[ref:https://stately.ai/docs/xstate]] [[ref:https://github.com/statelyai/xstate]]. Koha cũng enum hoá trạng thái ngay ở cấp dữ liệu [[ref:https://raw.githubusercontent.com/Koha-Community/Koha/master/installer/data/mysql/kohastructure.sql]] | Không có công cụ vẽ trực quan sẵn; nhóm phải tự giữ cho sơ đồ trong tài liệu khớp với dữ liệu trong bảng, nên có một bài kiểm thử đối chiếu hai nguồn |
| Thư viện biểu đồ | Chart.js phiên bản 4, vẽ trên trình duyệt, dữ liệu lấy từ `GET /api/admin/reports/*` | Recharts; ECharts; ảnh biểu đồ dựng sẵn phía máy chủ | Bảng điều khiển quản trị chỉ cần bốn biểu đồ: doanh thu theo tháng, công suất khai thác, cơ cấu chi phí, dòng tiền. Thư viện nhẹ, không kéo theo React, dùng được cả trong trang in báo cáo [[ref:https://it-hcm.fpt.edu.vn/articles.php?news=huong-dan-muon-laptop-cua-sinh-vien-trong-truong&id=56]] | Biểu đồ vẽ phía trình duyệt nên xuất PDF báo cáo phải chụp lại màn hình; nhóm phải tự kiểm chứng phiên bản và giấy phép tại thời điểm lập trình |
| Gửi tin nhắn | Zalo là kênh chính, email giao dịch là kênh dự phòng, mọi tin đi qua bảng `outbox_messages` rồi tới bảng `notifications` | Tin nhắn SMS; gọi thẳng API gửi tin trong luồng xử lý | Sinh viên đọc Zalo nhiều hơn email; outbox bảo đảm tin nhắn gửi ít nhất một lần và xử lý đúng một lần, đây là mức bảo đảm khả thi duy nhất trên mạng [[ref:https://milanjovanovic.tech/blog/implementing-the-outbox-pattern]] [[ref:https://www.npmjs.com/package/pg-transactional-outbox]] | Tài khoản Zalo chính thức cần hồ sơ doanh nghiệp, nên giai đoạn đầu phải chạy bằng email cộng nhắn tay; chi phí mỗi tin chưa xác minh được |
| Nền tảng triển khai | Một máy chủ ảo đặt tại Việt Nam chạy Ubuntu 24.04, Docker Compose, Caddy làm proxy ngược và cấp chứng chỉ tự động | Vercel cộng cơ sở dữ liệu thuê ngoài; Railway; Coolify tự dựng | Đặt máy trong nước cho độ trễ thấp với người dùng tại Đà Nẵng; máy chủ ảo Việt Nam bắt đầu từ 157.000đ mỗi tháng [[ref:https://vietnix.vn/vps/]] [[ref:https://azdigi.com/blog/kien-thuc-vps/bang-gia-thue-vps-viet-nam]]; gói miễn phí của Vercel không chạy được PostgreSQL nên vẫn phải thuê cơ sở dữ liệu riêng, còn Railway chỉ cho tín dụng dùng thử 30 ngày [[ref:https://phamhai.com/vercel-netlify-railway-so-sanh-hosting-free/]] [[ref:https://danubedata.ro/blog/best-vercel-alternatives-nextjs-hosting-2025]] | Một máy chủ là một điểm chết duy nhất, đúng vào mùa thi thì rất đắt. Cách giảm thiểu nằm ở mục sao lưu và quy trình dự phòng thủ công bên dưới |
{caption: Chín quyết định công nghệ của ExamLap, kèm phương án đã cân nhắc và rủi ro mà chính lựa chọn được chọn mang lại.}
{widths: 2,4,3,7,6}
{note: Số phiên bản thư viện lấy từ kho gói công khai tại ngày 14/09/2026. Nhóm phải kiểm tra lại phiên bản và giấy phép ngay khi bắt đầu lập trình.}

Một quyết định đáng nói riêng là **không dùng lại Snipe-IT**. Phần mềm này có mô hình tài sản rất tốt, nhưng bảng `checkout_requests` của nó không có cột ngày bắt đầu và ngày kết thúc, nghĩa là nó không mô hình hoá được việc đặt trước theo khung giờ, tức là đúng thứ ExamLap bán [[ref:https://github.com/grokability/snipe-it/blob/master/database/migrations/2016_09_02_001448_create_checkout_requests_table.php]]. Ngoài ra Snipe-IT dùng giấy phép AGPL-3.0-or-later, nên nếu fork rồi chạy thành dịch vụ thương mại thì phải công khai toàn bộ mã nguồn đã sửa [[ref:https://raw.githubusercontent.com/grokability/snipe-it/master/composer.json]]. Nhóm học mô hình dữ liệu của họ nhưng viết mã riêng.

## Môi trường và quy trình triển khai

Hệ thống có đúng ba môi trường, không hơn.

**Máy lập trình viên.** Một lệnh `docker compose up` dựng `postgres:17`, `redis:7` và một kho đối tượng giả. Dữ liệu mẫu do tệp `seed.ts` sinh ra: 10 máy đúng cơ cấu năm 1 gồm 5 máy nhóm A, 4 máy nhóm B, 1 máy nhóm C, kèm 20 ca thi và 30 đơn ở các trạng thái khác nhau. Không lập trình viên nào được dùng dữ liệu thật để thử.

**Môi trường thử nghiệm.** Một máy chủ ảo nhỏ hơn, cùng phiên bản hệ điều hành và cùng phiên bản PostgreSQL với môi trường thật, chạy trên tên miền phụ `staging.` và chặn bằng xác thực HTTP cơ bản. Đây là nơi duy nhất nhóm được thử tích hợp với môi trường thử của nhà cung cấp eKYC và dịch vụ đối soát VietQR. Dữ liệu là dữ liệu giả, và có một tác vụ chạy hằng đêm xoá sạch rồi gieo lại để không ai lỡ coi nó là thật.

**Môi trường thật.** Một máy chủ ảo tại Việt Nam. Phát hành theo quy trình: đẩy mã lên nhánh `main`, GitHub Actions chạy kiểm thử và dựng ảnh Docker, rồi kết nối SSH chạy `docker compose pull && docker compose up -d`. Caddy chuyển dần lưu lượng sang phiên bản mới. Toàn bộ mất dưới 5 phút, và nhóm quy định **không phát hành trong khoảng 06:00 đến 12:00 của ngày có lịch thi**.

**Quản lý biến bí mật.** Không tệp `.env` nào được đưa vào Git; kho mã chỉ có `.env.example` liệt kê tên biến cùng mô tả, và có một bước kiểm tra trong quy trình dựng sẽ làm hỏng bản dựng nếu thiếu biến. Trên máy chủ thật, biến nằm trong một tệp thuộc quyền `root` với chế độ `600` và được nạp qua `EnvironmentFile` của systemd. Bản sao dự phòng của toàn bộ khoá nằm trong một kho mật khẩu dùng chung có xác thực hai lớp, và **chỉ hai thành viên có quyền đọc**. Khoá bí mật ký webhook thanh toán, khoá API eKYC và khoá kho ảnh được đổi mỗi cuối học kỳ và đổi ngay khi có thành viên rời nhóm. Nhật ký ứng dụng lọc bỏ mọi trường có tên chứa `token`, `secret`, `id_number` hoặc `password` trước khi ghi.

**Di trú cơ sở dữ liệu.** Mỗi thay đổi lược đồ là một tệp SQL đánh số trong `drizzle/migrations/`, chạy bằng `drizzle-kit migrate` như một bước riêng trước khi khởi động phiên bản ứng dụng mới. Các thay đổi phá vỡ tương thích đi theo nguyên tắc mở rộng rồi thu hẹp: thêm cột mới, ghi song song hai cột một thời gian, chuyển đọc sang cột mới, rồi mới xoá cột cũ ở một lần phát hành sau. Ràng buộc chống trùng lịch phải viết bằng SQL thô vì không ORM nào sinh được, và được kèm ngay một bài kiểm thử tự động cố tình chèn hai suất chồng nhau để xác nhận PostgreSQL trả về mã lỗi `23P01`.

```sql
CREATE EXTENSION IF NOT EXISTS btree_gist;

ALTER TABLE inventory_holds
  ADD COLUMN period tstzrange NOT NULL;

ALTER TABLE inventory_holds
  ADD CONSTRAINT inventory_holds_no_overlap
  EXCLUDE USING gist (device_id WITH =, period WITH &&)
  WHERE (status <> 'cancelled');

CREATE INDEX inventory_holds_expires_idx
  ON inventory_holds (expires_at) WHERE status = 'active';
```
{caption: Tệp di trú tạo ràng buộc chống trùng lịch. Khoảng thời gian ghi vào cột period luôn đã cộng thêm 90 phút đệm sau giờ trả để kịp chuẩn bị máy cho lượt kế tiếp, đúng khái niệm "Security Time" của Odoo Rental.}

Thời gian đệm 90 phút không phải con số tuỳ tiện. Giữa hai lượt thuê, máy phải được xoá dữ liệu người dùng trước, chạy lại danh mục kiểm tra máy sẵn sàng thi và sạc pin. Odoo gọi đúng khái niệm này là thời gian an toàn giữa hai đơn thuê [[ref:https://www.odoo.com/documentation/18.0/applications/sales/rental.html]]. Kiểu biên nửa mở `[)` được chọn có chủ ý để một đơn kết thúc lúc 12:00 và một đơn bắt đầu lúc 12:00 không bị coi là chồng nhau.

**Sao lưu và khôi phục.** Bản sao lưu đầy đủ bằng `pg_dump -Fc` chạy lúc 03:00 hằng ngày, cộng với việc đẩy đoạn nhật ký ghi trước lên kho đối tượng ngoài với `archive_timeout = 900`, tức mỗi 15 phút. Bản sao được giữ 30 ngày theo ngày, cộng 6 bản theo tháng. Ảnh biên bản bàn giao đồng bộ sang một vùng lưu trữ thứ hai khác nhà cung cấp mỗi đêm.

:::ok Mục tiêu thời gian khôi phục và mất dữ liệu
**Mục tiêu mất dữ liệu tối đa (RPO): 15 phút**, tương ứng chu kỳ đẩy nhật ký ghi trước ra ngoài.
**Mục tiêu thời gian khôi phục (RTO): 90 phút vào ngày thường và 30 phút trong tuần thi**, vì trong tuần thi nhóm giữ sẵn một máy chủ ảo thứ hai đã cài đặt xong, chỉ cần nạp dữ liệu và đổi bản ghi DNS.
Một lần diễn tập khôi phục thật được thực hiện **trước mỗi kỳ thi cuối kỳ**, có bấm giờ và ghi biên bản. Nếu số đo vượt mục tiêu thì mục tiêu được sửa lại trong tài liệu, chứ không giữ một con số đẹp mà không đạt.
Ngoài ra luôn tồn tại **quy trình dự phòng thủ công**: một bảng tính dùng chung cộng nhóm Zalo trực, đủ để tiếp tục nhận đơn và bàn giao máy nếu website sập hoàn toàn.
:::

## Chi phí hạ tầng hằng tháng

Bảng dưới đây là chi tiết của dòng "Máy chủ, tên miền, email, dịch vụ đối soát VietQR" trị giá **450.000đ mỗi tháng** trong bảng định phí. Hai dòng công nghệ khác nằm riêng trong bảng định phí và không tính lại ở đây: phần mềm quản lý thiết bị cho 10 máy là 150.000đ, và nhóm dịch vụ khác gồm lưu trữ ảnh, sao lưu và công cụ thiết kế là 150.000đ.

| Hạng mục | Cấu hình | Chi phí mỗi tháng | Căn cứ |
|---|---|---|---|
| Máy chủ ảo môi trường thật | 2 vCPU, 4 GB RAM, 60 GB NVMe, đặt tại Việt Nam; chạy ứng dụng, PostgreSQL và Redis trên cùng máy | 160.000đ | Máy chủ ảo Việt Nam công bố từ 157.000đ mỗi tháng [[ref:https://vietnix.vn/vps/]] [[ref:https://azdigi.com/blog/kien-thuc-vps/bang-gia-thue-vps-viet-nam]] |
| Máy chủ ảo môi trường thử nghiệm | 1 vCPU, 2 GB RAM; kiêm nơi chạy công cụ giám sát | 60.000đ | Gói thấp của các nhà cung cấp trong nước từ 29.000đ đến 55.000đ mỗi tháng [[ref:https://azdigi.com/blog/kien-thuc-hosting/top-5-hosting-gia-re-tot-nhat-viet-nam-2026]] |
| Tên miền `.vn`, quy về tháng | Năm đầu 770.000đ gồm lệ phí đăng ký, phí duy trì và phí tài khoản quản trị; tên miền `.vn` không chịu thuế giá trị gia tăng | 65.000đ | Bảng phí tên miền của nhà đăng ký [[ref:https://helpdesk.inet.vn/knowledgebase/bang-gia-ten-mien-va-cac-loai-phi]] [[ref:https://vinahost.vn/phi-duy-tri-ten-mien/]] |
| Email giao dịch | Dưới 3.000 thư mỗi tháng cho xác nhận đơn, nhắc hạn và biên bản | 30.000đ | [Ước lượng của nhóm], giả định dùng gói trả phí mức thấp nhất thay vì gói miễn phí để có độ tin cậy gửi thư |
| Dịch vụ đối soát biến động số dư VietQR | Nhận thông báo tiền về theo thời gian thực và gọi webhook vào hệ thống | 120.000đ | [Ước lượng của nhóm]. Giá công bố của các nhà cung cấp trong nước chưa mở được trang để xác minh, nên đây là khoản phải kiểm chứng trước khi ký hợp đồng |
| Giám sát ngoài và cảnh báo | Kiểm tra trạng thái từ bên ngoài mỗi 60 giây, gửi cảnh báo qua Zalo và email | 15.000đ | [Ước lượng của nhóm], dựa trên mức gói cá nhân của các dịch vụ giám sát phổ biến |
| Chứng chỉ TLS | Let's Encrypt, Caddy tự gia hạn | 0đ | Miễn phí |
| **Cộng** | | **450.000đ** | Khớp với dòng tương ứng trong bảng định phí hằng tháng |
{caption: Chi tiết chi phí hạ tầng hằng tháng của ExamLap, tổng cộng khớp đúng với dòng 450.000đ trong bảng định phí.}
{widths: 4,6,2,7}
{right: 3}
{note: Ba khoản mang nhãn [Ước lượng của nhóm] chiếm 165.000đ, tức 37% của bảng này. Đây là phần rủi ro dự toán lớn nhất và nằm trong danh sách phải kiểm chứng ở Phụ lục E.}

Để đối chiếu, một phần mềm cho thuê thiết bị thương mại niêm yết khoảng 50 đô la Mỹ mỗi tháng cho hai người dùng, tức cao gấp nhiều lần toàn bộ bảng trên [[ref:https://ezo.io/ezrentout/pricing/]]. Nhóm không dùng con số đó để kết luận tự xây rẻ hơn, vì phép so sánh ấy bỏ qua 200 đến 400 giờ công lập trình. Với một đồ án môn học thì số giờ đó là thứ đã trả bằng học phí; với một doanh nghiệp thật thì tự xây không rẻ hơn.

## Quan sát hệ thống

Nguyên tắc là mỗi thứ được đo phải trả lời một câu hỏi vận hành cụ thể, không đo cho đẹp bảng điều khiển.

**Ghi nhật ký.** Mọi bản ghi ở dạng JSON một dòng, bắt buộc có `request_id`, `actor_id`, `actor_type`, `route`, `status_code`, `duration_ms`. Với nghiệp vụ, thêm `order_code` và `device_tag`. Nhật ký nghiệp vụ quan trọng không nằm trong tệp log mà nằm trong bảng `audit_logs`, là bảng chỉ ghi thêm, có trigger chặn `UPDATE` và `DELETE`, và mỗi dòng chứa mã băm của dòng trước để phát hiện can thiệp [[ref:https://tracehold.ai/blog/immutable-audit-log-hmac-hash-chain/]] [[ref:https://www.designgurus.io/answers/detail/how-do-you-enforce-immutability-and-appendonly-audit-trails]]. **Tuyệt đối không ghi vào nhật ký**: số căn cước, vector khuôn mặt, đường dẫn ảnh eKYC chưa ký, nội dung webhook có thông tin tài khoản ngân hàng.

**Đo chỉ số.** Bốn chỉ số hạ tầng: tỉ lệ phản hồi lỗi, độ trễ phân vị 95 theo từng endpoint, số kết nối PostgreSQL đang mở, độ dài hàng đợi BullMQ. Sáu chỉ số nghiệp vụ ghi thẳng từ dữ liệu: số đơn tạo mới mỗi giờ, tỉ lệ đơn rơi ở trạng thái "Chờ thanh toán", thời gian trung bình từ lúc tiền về đến lúc đơn chuyển trạng thái, số máy đang cho thuê trên tổng đội máy, tuổi của lần check-in gần nhất theo từng máy, số đơn quá hạn.

**Cảnh báo.** Bốn cảnh báo dưới đây là bốn cảnh báo có quyền đánh thức người trực lúc 05:00 sáng ngày thi. Mọi cảnh báo khác chỉ vào kênh Zalo và đọc trong giờ làm việc.

| # | Cảnh báo | Ngưỡng kích hoạt | Hành động bắt buộc |
|---|---|---|---|
| 1 | Máy không check-in | `devices.last_checkin_at` cũ hơn **45 phút** với bất kỳ máy nào đang gắn với đơn ở trạng thái "Đang thuê", tức đã lỡ ba nhịp check-in 15 phút liên tiếp. Nâng lên mức khẩn nếu quá **4 giờ** | Gọi điện cho khách trước khi làm bất cứ điều gì khác. Lệnh khoá màn hình chỉ được phát khi có hai người duyệt và luôn ghi vào `audit_logs` [[ref:https://github.com/Ylianst/MeshCentral]] |
| 2 | Webhook thanh toán lỗi | Từ **3 lần xử lý webhook thất bại trong 10 phút**, hoặc bất kỳ bản ghi `payments` nào ở trạng thái đã nhận tiền mà chưa khớp được vào đơn sau **5 phút** | Mở trang đối soát tay, khớp thủ công theo mã đơn trong nội dung chuyển khoản. Ngưỡng 5 phút được chọn để không phá vỡ cam kết hoàn cọc trong 5 phút |
| 3 | Đơn quá hạn | Bất kỳ đơn nào ở trạng thái "Đang thuê" mà đã qua `exam_slots.return_due_at` quá **30 phút**. Báo lại mỗi giờ. Quá **48 giờ** và không liên lạc được thì đơn tự chuyển sang trạng thái "Mất tài sản" | Nhắn tin tự động lần một; nhân viên gọi ở mốc 2 giờ; quy trình văn bản nhắc nợ ở mốc 48 giờ |
| 4 | Lỗi ứng dụng tăng đột biến | Tỉ lệ phản hồi mã 5xx vượt **2% tổng số yêu cầu trong 5 phút liên tiếp**, hoặc vượt **10 lỗi mỗi phút**; hoặc độ trễ phân vị 95 của `GET /api/availability` vượt **800 ms trong 10 phút** | Quay lui phiên bản trước bằng `docker compose` trong vòng 10 phút, rồi mới tìm nguyên nhân. Trong tuần thi, quay lui trước, phân tích sau |
{caption: Bốn cảnh báo có quyền đánh thức người trực, kèm ngưỡng kích hoạt cụ thể và hành động bắt buộc đi kèm.}
{widths: 1,4,8,8}

Trong sáu đợt cao điểm mỗi năm, nhóm siết ngưỡng lại: cảnh báo số 4 hạ xuống 1% trong khoảng 05:00 đến 12:00 của ngày thi, và có một người trực điện thoại theo lịch phân công. Ngoài các đợt đó, hệ thống chạy với ngưỡng bình thường.

:::risk Điểm yếu nhóm thừa nhận
Kiến trúc này có một máy chủ duy nhất. Nếu nhà cung cấp máy chủ ảo gặp sự cố đúng sáng ngày thi, không có bản sao đang chạy nào đỡ được.
Nhóm chọn đánh đổi này một cách có ý thức: chi phí cho một cấu hình hai máy có chuyển đổi tự động vượt ngân sách 450.000đ mỗi tháng, trong khi xác suất sự cố đúng vào sáu buổi sáng cao điểm là thấp.
Cách bù đắp là mục tiêu khôi phục 30 phút trong tuần thi, bản sao lưu 15 phút một lần, và quy trình dự phòng thủ công bằng bảng tính cùng nhóm Zalo. Đây là giảm thiểu, không phải triệt tiêu rủi ro.
:::
