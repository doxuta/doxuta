## Tổng thể kiến trúc

ExamLap dựng theo kiểu **một khối triển khai duy nhất, dữ liệu tập trung ở PostgreSQL, việc nặng đẩy sang tác vụ nền**. Sơ đồ dưới là bản vẽ mà nhóm sẽ lập trình theo.

<<<landscape>>>

![Kiến trúc ExamLap gồm bốn lớp: người dùng, ứng dụng, dữ liệu và dịch vụ ngoài, kèm đường đi của một yêu cầu xuyên qua cả bốn lớp.](assets/diagrams/04-kien-truc.png){w=0}{src: Nguồn: nhóm tác giả.}

<<<portrait>>>

- **Lớp người dùng** là ba loại thiết bị, không phải ba ứng dụng. Sinh viên dùng trình duyệt điện thoại; nhân viên giao nhận cài chính mã nguồn đó dạng PWA để ảnh biên bản xếp hàng trong `IndexedDB` rồi đẩy lên khi có sóng; quản trị viên dùng trình duyệt máy tính. Ba vai chung một mã nguồn, khác nhau ở quyền và bố cục.
- **CDN và tường lửa ứng dụng** ép HTTPS và giới hạn tần suất theo địa chỉ IP lẫn tài khoản cho hai điểm yếu nhất: trang tra máy trống và điểm nhận webhook.
- **Lớp ứng dụng** có ba khối chung một máy chủ ảo: giao diện dựng bằng Next.js; API giữ toàn bộ quy tắc nghiệp vụ và là nơi duy nhất được ghi vào cơ sở dữ liệu; tác vụ nền nhả suất kho hết hạn giữ, nhắc hạn trả máy, hoàn cọc, gửi thông báo.
- **Lớp dữ liệu** có ba kho. PostgreSQL là nguồn sự thật duy nhất. Redis chỉ giữ hàng đợi, phiên và bộ đếm tần suất, tức thứ mất đi thì phiền nhưng không hỏng nghiệp vụ. Kho ảnh giữ ảnh bàn giao, ảnh eKYC và ảnh hiện trạng máy, tách ra để tệp sao lưu không phình.
- **Lớp dịch vụ ngoài** có bốn đối tác: đối soát VietQR báo tiền về, eKYC đối chiếu căn cước với khuôn mặt sống, máy chủ MDM nhận check-in và khoá màn hình, Zalo và email gửi thông báo.

Ba mũi tên hai chiều là ba chỗ dễ hỏng nhất, và nguyên tắc xử lý chỉ có một: **không để một cuộc gọi ra ngoài nằm trong một giao dịch cơ sở dữ liệu**. Khi tiền về, dịch vụ đối soát gọi `POST /webhooks/payment`; hệ thống kiểm chữ ký HMAC, ghi thô vào `payments.raw_payload` với ràng buộc `UNIQUE (provider, provider_txn_id)` rồi trả HTTP 200 ngay, việc đổi trạng thái để tác vụ nền làm. Nhờ vậy cổng thanh toán gửi lại một sự kiện mười lần thì đơn vẫn chỉ cộng tiền một lần [[ref:https://matheuspalma.com/blog/outbound-webhook-delivery-signing-retries-dead-letters]] [[ref:https://stripe.com/blog/idempotency]]. Thông báo đi qua bảng `outbox_messages` ghi trong **cùng giao dịch** với thay đổi trạng thái, nên không có cảnh khách nhận xác nhận cho đơn đã rollback [[ref:https://milanjovanovic.tech/blog/implementing-the-outbox-pattern]].

## Vì sao chọn một khối thay vì vi dịch vụ

Quy mô phải phục vụ là **382 lượt thuê ca, ngày và tuần cộng 30 máy-tháng trong năm thứ nhất**, tức chưa tới hai lượt đặt mỗi ngày, dồn vào sáu đợt cao điểm. Đội lập trình là bốn đến năm sinh viên làm ngoài giờ. Ở quy mô đó, tách vi dịch vụ là quyết định sai về kỹ thuật.

Bài toán đắt nhất là **không cho thuê một máy hai lần trong cùng khung giờ**, và cách giải rẻ nhất là ràng buộc cấp cơ sở dữ liệu. `EXCLUDE USING gist` trên cặp `(device_id, period)` khiến chính máy chủ dữ liệu từ chối bản ghi chồng lịch, dù yêu cầu đến từ API, tác vụ nền hay một lần sửa tay trong `psql` [[ref:https://chat2db.ai/resources/blog/postgres-exclusion-constraints-guide]] [[ref:https://dev.to/franckpachot/postgresql-exclude-constraints-for-better-concurrency-than-serializable-pob]]. Ràng buộc đó chỉ chạy khi dữ liệu nằm chung một cơ sở dữ liệu. Tách kho máy khỏi kho đơn là tự vứt công cụ mạnh nhất mình có, rồi phải dựng lại bằng Saga, thứ sinh ra cho hệ phân tán chứ không cho 400 lượt thuê một năm [[ref:https://microservices.io/patterns/data/saga.html]].

Hai lý do nữa. Mọi hệ tham chiếu gần nhất đều là một khối: Snipe-IT là ứng dụng Laravel đơn khối [[ref:https://github.com/grokability/snipe-it]], Koha cũng vậy dù chạy ở hàng nghìn thư viện [[ref:https://raw.githubusercontent.com/Koha-Community/Koha/master/installer/data/mysql/kohastructure.sql]]. Và về tiền: một khối chạy trên máy chủ ảo 160.000đ mỗi tháng, còn năm dịch vụ cần thêm hàng đợi thông điệp, truy vết phân tán và ba máy chủ, vượt xa ngân sách 450.000đ mỗi tháng.

Ranh giới module vẫn được giữ bên trong khối: bốn thư mục `booking/`, `inventory/`, `billing/`, `identity/`, mỗi module sở hữu nhóm bảng riêng và chỉ gọi module khác qua tệp `index.ts` công khai.

:::note Điều kiện cụ thể để tách dịch vụ
Chỉ tách khi đo được một trong bốn dấu hiệu: đội máy vượt 150 chiếc hoặc trên 500 lượt thuê mỗi tháng; dựng và kiểm thử vượt 15 phút; lập trình viên thường trực vượt 8 người; hoặc một module cần quy mô riêng. Module tách đầu tiên chắc chắn là MDM, vì tải đều và không cần giao dịch chung với đơn thuê.
:::

## Lựa chọn công nghệ và lý do

Bối cảnh ràng buộc: nhóm sinh viên, ngân sách hạ tầng dưới 500.000đ mỗi tháng, phải chạy thật vào đợt thi cuối kỳ gần nhất.

| Lớp | Chọn | Đã cân nhắc | Lý do chọn | Rủi ro của lựa chọn |
|---|---|---|---|---|
| Ngôn ngữ và khung web | TypeScript trên Next.js 16, một khối dựng cả giao diện lẫn API | Laravel 13 với Livewire; Go với templ và HTMX | Sinh viên Đại học FPT đã quen JavaScript và React nên chi phí học gần bằng không, và chỉ một ngôn ngữ cho cả hai đầu [[ref:https://nihardaily.com/56-nextjs-15-vs-laravel-when-to-choose-what-in-2025]] [[ref:https://www.adriano-junior.com/best-web-frameworks-2026]] | Laravel có sẵn hàng đợi, lịch chạy và bảng quản trị Filament nên đội nhỏ ra sản phẩm nhanh hơn [[ref:https://wishtreetech.com/blogs/tech-stack/laravel-vs-next-js-which-framework-should-you-choose-for-your-full-stack-web-app/]]; chọn Next.js là phải tự dựng bảng quản trị kho, thêm hai tuần công |
| Cơ sở dữ liệu | PostgreSQL 17 với extension `btree_gist` | MySQL 8; MariaDB | MySQL **không có** `EXCLUDE` và không có kiểu range; Koha lẫn LibreBooking chạy MySQL nên đều phải kiểm trùng lịch bằng mã ứng dụng [[ref:https://raw.githubusercontent.com/LibreBooking/app/master/database_schema/create-schema.sql]] [[ref:https://www.jusdb.com/blog/postgresql-range-types-exclusion-constraints]] | Hosting rẻ trong nước thiên về MySQL nên phải thuê máy chủ ảo; phải học `tstzrange` và biên nửa mở `[)` |
| Lớp truy cập dữ liệu | Drizzle ORM, di trú bằng `drizzle-kit` | Prisma 8; SQL thuần | Prisma hỗ trợ kiểu range kém hơn, trong khi `tstzrange` là trung tâm bài toán [[ref:https://amitavroy.com/articles/postgresql-gist-exclusion-constraintthe-database-evel-answer-to-double-bookings]] | Cộng đồng nhỏ, ít tài liệu tiếng Việt; `EXCLUDE` vẫn phải viết bằng SQL thô |
| Hàng đợi và bộ nhớ đệm | Redis 7 với BullMQ; Redis giữ phiên và bộ đếm tần suất | Hàng đợi trên PostgreSQL bằng `FOR UPDATE SKIP LOCKED`; khoá phân tán Redis | Cần lịch chạy mỗi phút để nhả suất kho hết hạn và nhắc hạn; BullMQ có sẵn thử lại giãn cách, hàng đợi chết | Thêm một tiến trình phải giám sát. Nhóm **không** dùng khoá phân tán Redis chống trùng lịch, vì `EXCLUDE` đã đủ [[ref:https://redis.io/tutorials/inventory-reservation-in-real-time-with-redis/]] |
| Lưu trữ ảnh | Kho đối tượng tương thích S3, đường dẫn ký sẵn hạn 15 phút, mã băm ở `handover_photos.sha256` | Lưu `bytea` trong PostgreSQL; lưu thẳng trên đĩa | Sáu ảnh mỗi chiều bàn giao nhân 400 lượt là vài nghìn tệp mỗi năm; mã băm chứng minh ảnh chưa bị thay khi tranh chấp [[ref:https://www.locatorx.com/blog/the-truth-about-asset-records-why-immutability-is-the-foundation-of-a-verifiable-chain-of-custody]] | Phụ thuộc nhà cung cấp ngoài; ảnh eKYC là dữ liệu nhạy cảm nên phải mã hoá và xoá sau 90 ngày |
| Xác thực | Liên kết đăng nhập một lần tới email `@fpt.edu.vn`, phiên trong Redis, ba vai `student`, `staff`, `admin`; eKYC thuê ngoài | Mật khẩu; đăng nhập Google; tự đối chiếu khuôn mặt | Bắt buộc email trường là lớp sàng lọc đầu vào rẻ và mạnh nhất; đối chiếu khuôn mặt sống là bài toán chuyên ngành, nhà cung cấp trong nước có tài liệu tích hợp [[ref:https://docs-vision.fpt.ai/ekyc/I-introduction/gioi-thieu/]] [[ref:https://ekyc.vnpt.vn/vi/idcheck]] | Phụ thuộc máy chủ thư của trường; giá eKYC theo lượt chưa xác minh được |
| Thư viện máy trạng thái | Bảng `order_state_transitions(from_state, event, to_state)` cộng `CHECK` trên `orders.status`; mỗi lần chuyển ghi một dòng `audit_logs` | XState 5; viết `switch` rải rác | Vòng đời đơn có 13 trạng thái phẳng; XState mạnh cho giao diện phức tạp nhưng khó bảo vệ hơn một bảng dữ liệu [[ref:https://stately.ai/docs/xstate]] [[ref:https://github.com/statelyai/xstate]] | Không có công cụ vẽ trực quan; cần kiểm thử đối chiếu sơ đồ tài liệu với dữ liệu trong bảng |
| Thư viện biểu đồ | Chart.js 4, vẽ trên trình duyệt, dữ liệu từ `GET /api/admin/reports/*` | Recharts; ECharts; ảnh dựng sẵn phía máy chủ | Chỉ cần bốn biểu đồ: doanh thu, công suất, cơ cấu chi phí, dòng tiền; thư viện nhẹ, dùng được trong trang Dashboard quen thuộc [[ref:https://it-hcm.fpt.edu.vn/articles.php?news=huong-dan-muon-laptop-cua-sinh-vien-trong-truong&id=56]] | Vẽ phía trình duyệt nên xuất PDF phải chụp màn hình; phiên bản và giấy phép phải tự kiểm chứng |
| Gửi tin nhắn | Zalo là kênh chính, email dự phòng; mọi tin qua `outbox_messages` rồi tới `notifications` | Tin nhắn SMS; gọi thẳng API gửi tin trong luồng xử lý | Sinh viên đọc Zalo nhiều hơn email; outbox bảo đảm gửi ít nhất một lần và xử lý đúng một lần [[ref:https://www.npmjs.com/package/pg-transactional-outbox]] | Tài khoản Zalo chính thức cần hồ sơ doanh nghiệp nên đầu kỳ chạy bằng email; giá mỗi tin chưa xác minh |
| Nền tảng triển khai | Một máy chủ ảo tại Việt Nam, Ubuntu 24.04, Docker Compose, Caddy làm proxy ngược | Vercel cộng cơ sở dữ liệu thuê ngoài; Railway; Coolify tự dựng | Đặt máy trong nước cho độ trễ thấp, giá từ 157.000đ mỗi tháng [[ref:https://vietnix.vn/vps/]]; Vercel bản miễn phí không chạy được PostgreSQL, Railway chỉ cho tín dụng thử 30 ngày [[ref:https://phamhai.com/vercel-netlify-railway-so-sanh-hosting-free/]] [[ref:https://danubedata.ro/blog/best-vercel-alternatives-nextjs-hosting-2025]] | Một máy chủ là một điểm chết duy nhất, đúng mùa thi thì rất đắt |
{caption: Mười quyết định công nghệ của ExamLap, kèm phương án đã cân nhắc và rủi ro mà chính lựa chọn được chọn mang lại.}
{widths: 2,4,3,7,6}
{note: Số phiên bản lấy từ kho gói công khai ngày 14/09/2026 và phải kiểm tra lại khi bắt đầu lập trình.}

Nhóm cũng quyết định **không dùng lại Snipe-IT**: bảng `checkout_requests` của nó không có cột ngày bắt đầu và ngày kết thúc, tức không mô hình hoá được việc đặt trước theo khung giờ [[ref:https://github.com/grokability/snipe-it/blob/master/database/migrations/2016_09_02_001448_create_checkout_requests_table.php]]. Nó lại dùng giấy phép AGPL-3.0-or-later, nên fork rồi chạy thành dịch vụ thương mại thì phải công khai toàn bộ mã đã sửa [[ref:https://raw.githubusercontent.com/grokability/snipe-it/master/composer.json]].

## Môi trường và quy trình triển khai

Hệ thống có đúng ba môi trường.

- **Máy lập trình viên.** `docker compose up` dựng `postgres:17`, `redis:7` và kho đối tượng giả; tệp `seed.ts` sinh 10 máy đúng cơ cấu năm 1 gồm 5 máy nhóm A, 4 máy nhóm B, 1 máy nhóm C, kèm 20 ca thi và 30 đơn.
- **Môi trường thử nghiệm.** Máy chủ ảo nhỏ hơn, cùng phiên bản hệ điều hành và PostgreSQL với môi trường thật, chạy trên tên miền phụ `staging.` và chặn bằng xác thực HTTP cơ bản. Đây là nơi duy nhất được thử tích hợp với bản thử của eKYC và dịch vụ đối soát.
- **Môi trường thật.** Đẩy mã lên nhánh `main`, GitHub Actions chạy kiểm thử và dựng ảnh Docker, rồi SSH chạy `docker compose pull && docker compose up -d`. Toàn bộ dưới 5 phút. Nhóm quy định **không phát hành trong khoảng 06:00 đến 12:00 của ngày có lịch thi**.

**Biến bí mật.** Không tệp `.env` nào vào Git; kho mã chỉ có `.env.example`, và bước kiểm tra khi dựng làm hỏng bản dựng nếu thiếu biến. Trên máy chủ thật, biến nằm trong tệp thuộc `root` chế độ `600`, nạp qua `EnvironmentFile` của systemd. Bản dự phòng nằm trong kho mật khẩu có xác thực hai lớp, **chỉ hai thành viên đọc được**. Khoá ký webhook, khoá API eKYC và khoá kho ảnh đổi mỗi cuối học kỳ, và đổi ngay khi có thành viên rời nhóm. Nhật ký lọc bỏ mọi trường tên chứa `token`, `secret`, `id_number`, `password`.

**Di trú cơ sở dữ liệu.** Mỗi thay đổi lược đồ là một tệp SQL đánh số trong `drizzle/migrations/`, chạy bằng `drizzle-kit migrate` ở một bước riêng trước khi khởi động phiên bản mới. Thay đổi phá vỡ tương thích theo nguyên tắc mở rộng rồi thu hẹp: thêm cột, ghi song song, chuyển đọc, rồi mới xoá cột cũ ở lần phát hành sau.

```sql
CREATE EXTENSION IF NOT EXISTS btree_gist;

ALTER TABLE inventory_holds ADD COLUMN period tstzrange NOT NULL;

ALTER TABLE inventory_holds
  ADD CONSTRAINT inventory_holds_no_overlap
  EXCLUDE USING gist (device_id WITH =, period WITH &&)
  WHERE (status <> 'cancelled');

CREATE INDEX inventory_holds_expires_idx
  ON inventory_holds (expires_at) WHERE status = 'active';
```
{caption: Tệp di trú tạo ràng buộc chống trùng lịch, kèm kiểm thử tự động cố tình chèn hai suất chồng nhau để xác nhận PostgreSQL trả mã lỗi 23P01.}

Giá trị ghi vào `period` luôn cộng thêm 90 phút đệm sau giờ trả, vì giữa hai lượt máy phải xoá dữ liệu người dùng trước, chạy lại danh mục kiểm tra máy sẵn sàng thi và sạc pin. Odoo gọi đây là thời gian an toàn giữa hai đơn thuê [[ref:https://www.odoo.com/documentation/18.0/applications/sales/rental.html]]. Biên nửa mở `[)` được chọn có chủ ý, để đơn kết thúc lúc 12:00 và đơn bắt đầu lúc 12:00 không bị coi là chồng nhau.

**Sao lưu.** `pg_dump -Fc` lúc 03:00 hằng ngày, cộng đẩy nhật ký ghi trước ra kho đối tượng ngoài với `archive_timeout = 900`. Giữ 30 bản theo ngày và 6 bản theo tháng. Ảnh bàn giao đồng bộ sang một vùng lưu trữ khác nhà cung cấp mỗi đêm.

:::ok Mục tiêu khôi phục
**Mục tiêu mất dữ liệu tối đa (RPO): 15 phút**, đúng chu kỳ đẩy nhật ký ghi trước ra ngoài.
**Mục tiêu thời gian khôi phục (RTO): 90 phút ngày thường và 30 phút trong tuần thi**, vì tuần thi nhóm giữ sẵn một máy chủ ảo thứ hai đã cài đặt xong, chỉ cần nạp dữ liệu và đổi bản ghi DNS.
Diễn tập khôi phục thật, có bấm giờ và ghi biên bản, thực hiện trước mỗi kỳ thi cuối kỳ. Nếu số đo vượt mục tiêu thì sửa lại mục tiêu, không giữ con số đẹp mà không đạt.
Luôn có quy trình dự phòng thủ công bằng bảng tính dùng chung và nhóm Zalo trực, đủ để tiếp tục nhận đơn nếu website sập.
:::

## Chi phí hạ tầng hằng tháng

Bảng dưới chi tiết hoá dòng "Máy chủ, tên miền, email, dịch vụ đối soát VietQR" trị giá **450.000đ mỗi tháng**. Hai dòng công nghệ khác nằm riêng trong bảng định phí: phần mềm quản lý thiết bị 150.000đ, nhóm dịch vụ khác 150.000đ.

| Hạng mục | Cấu hình | Mỗi tháng | Căn cứ |
|---|---|---|---|
| Máy chủ ảo môi trường thật | 2 vCPU, 4 GB RAM, 60 GB NVMe, đặt trong nước; chạy ứng dụng, PostgreSQL, Redis chung máy | 160.000đ | Máy chủ ảo Việt Nam công bố từ 157.000đ [[ref:https://vietnix.vn/vps/]] [[ref:https://azdigi.com/blog/kien-thuc-vps/bang-gia-thue-vps-viet-nam]] |
| Máy chủ ảo môi trường thử nghiệm | 1 vCPU, 2 GB RAM; kiêm nơi chạy công cụ giám sát | 60.000đ | Gói thấp trong nước từ 29.000đ đến 55.000đ [[ref:https://azdigi.com/blog/kien-thuc-hosting/top-5-hosting-gia-re-tot-nhat-viet-nam-2026]] |
| Tên miền `.vn` quy về tháng | Năm đầu 770.000đ gồm lệ phí đăng ký, phí duy trì, phí tài khoản quản trị; không chịu thuế giá trị gia tăng | 65.000đ | Bảng phí của nhà đăng ký [[ref:https://helpdesk.inet.vn/knowledgebase/bang-gia-ten-mien-va-cac-loai-phi]] [[ref:https://vinahost.vn/phi-duy-tri-ten-mien/]] |
| Email giao dịch | Dưới 3.000 thư mỗi tháng cho xác nhận đơn, nhắc hạn, biên bản | 30.000đ | [Ước lượng của nhóm], giả định gói trả phí thấp nhất |
| Đối soát biến động số dư VietQR | Báo tiền về theo thời gian thực và gọi webhook vào hệ thống | 120.000đ | [Ước lượng của nhóm]. Chưa mở được trang giá nhà cung cấp để xác minh |
| Giám sát ngoài và cảnh báo | Kiểm tra trạng thái từ bên ngoài mỗi 60 giây, báo qua Zalo và email | 15.000đ | [Ước lượng của nhóm], theo mức gói cá nhân phổ biến |
| Chứng chỉ TLS | Let's Encrypt, Caddy tự gia hạn | 0đ | Miễn phí |
| **Cộng** | | **450.000đ** | Khớp dòng tương ứng trong bảng định phí |
{caption: Chi tiết chi phí hạ tầng hằng tháng của ExamLap, tổng cộng khớp đúng dòng 450.000đ trong bảng định phí.}
{widths: 4,6,2,7}
{right: 3}
{note: Ba khoản mang nhãn [Ước lượng của nhóm] chiếm 165.000đ, tức 37% bảng này, và nằm trong danh sách kiểm chứng ở Phụ lục E.}

Để đối chiếu, một phần mềm cho thuê thiết bị thương mại niêm yết khoảng 50 đô la Mỹ mỗi tháng cho hai người dùng [[ref:https://ezo.io/ezrentout/pricing/]]. Nhóm không kết luận tự xây rẻ hơn, vì phép so sánh đó bỏ qua 200 đến 400 giờ công.

## Quan sát hệ thống

**Ghi nhật ký.** Mỗi bản ghi là một dòng JSON có `request_id`, `actor_id`, `actor_type`, `route`, `status_code`, `duration_ms`, và với nghiệp vụ thì thêm `order_code`, `device_tag`. Nhật ký nghiệp vụ quan trọng nằm ở bảng `audit_logs` chứ không nằm trong tệp log: chỉ ghi thêm, trigger chặn `UPDATE` và `DELETE`, mỗi dòng chứa mã băm của dòng trước [[ref:https://tracehold.ai/blog/immutable-audit-log-hmac-hash-chain/]] [[ref:https://www.designgurus.io/answers/detail/how-do-you-enforce-immutability-and-appendonly-audit-trails]]. **Tuyệt đối không ghi** số căn cước, vector khuôn mặt, đường dẫn ảnh eKYC chưa ký và webhook chứa thông tin tài khoản ngân hàng.

**Đo chỉ số.** Bốn chỉ số hạ tầng: tỉ lệ phản hồi lỗi, độ trễ phân vị 95 theo endpoint, số kết nối PostgreSQL đang mở, độ dài hàng đợi BullMQ. Sáu chỉ số nghiệp vụ đọc thẳng từ dữ liệu: số đơn mới mỗi giờ, tỉ lệ đơn rơi ở "Chờ thanh toán", thời gian từ lúc tiền về tới lúc đơn đổi trạng thái, số máy đang cho thuê trên tổng đội, tuổi lần check-in gần nhất theo máy, số đơn quá hạn.

**Cảnh báo.** Bốn cảnh báo dưới đây có quyền đánh thức người trực lúc 05:00 ngày thi; mọi cảnh báo khác chỉ vào kênh Zalo, đọc trong giờ làm việc.

| # | Cảnh báo | Ngưỡng kích hoạt | Hành động bắt buộc |
|---|---|---|---|
| 1 | Máy không check-in | `devices.last_checkin_at` cũ hơn **45 phút** với máy đang gắn đơn "Đang thuê", tức lỡ ba nhịp 15 phút liên tiếp; nâng mức khẩn nếu quá **4 giờ** | Gọi điện cho khách trước đã. Lệnh khoá màn hình chỉ phát khi có hai người duyệt và luôn ghi vào `audit_logs` [[ref:https://github.com/Ylianst/MeshCentral]] |
| 2 | Webhook thanh toán lỗi | Từ **3 lần xử lý webhook thất bại trong 10 phút**, hoặc một bản ghi `payments` đã nhận tiền mà chưa khớp vào đơn sau **5 phút** | Mở trang đối soát, khớp thủ công theo mã đơn trong nội dung chuyển khoản. Ngưỡng 5 phút chọn theo cam kết hoàn cọc trong 5 phút |
| 3 | Đơn quá hạn | Đơn "Đang thuê" đã qua `exam_slots.return_due_at` quá **30 phút**, báo lại mỗi giờ; quá **48 giờ** không liên lạc được thì đơn chuyển sang "Mất tài sản" | Nhắn tin tự động lần một, nhân viên gọi ở mốc 2 giờ, quy trình văn bản nhắc nợ ở mốc 48 giờ |
| 4 | Lỗi ứng dụng tăng đột biến | Tỉ lệ mã 5xx vượt **2% số yêu cầu trong 5 phút liên tiếp** hoặc vượt **10 lỗi mỗi phút**; hoặc độ trễ phân vị 95 của `GET /api/availability` vượt **800 ms trong 10 phút** | Quay lui phiên bản trước bằng `docker compose` trong 10 phút rồi mới tìm nguyên nhân. Tuần thi: quay lui trước, phân tích sau |
{caption: Bốn cảnh báo có quyền đánh thức người trực, kèm ngưỡng kích hoạt và hành động bắt buộc.}
{widths: 1,4,8,8}

Trong sáu đợt cao điểm mỗi năm, cảnh báo số 4 siết xuống 1% trong khoảng 05:00 đến 12:00 ngày thi, và có người trực điện thoại theo lịch.

:::risk Điểm yếu nhóm thừa nhận
Kiến trúc này có một máy chủ duy nhất. Nếu nhà cung cấp gặp sự cố đúng sáng ngày thi thì không có bản sao đang chạy nào đỡ được.
Đây là đánh đổi có ý thức: cấu hình hai máy chuyển đổi tự động vượt ngân sách 450.000đ mỗi tháng, còn xác suất sự cố rơi đúng sáu buổi sáng cao điểm là thấp.
Bù đắp bằng mục tiêu khôi phục 30 phút trong tuần thi, sao lưu 15 phút một lần và quy trình dự phòng thủ công. Đây là giảm thiểu, không phải triệt tiêu rủi ro.
:::
