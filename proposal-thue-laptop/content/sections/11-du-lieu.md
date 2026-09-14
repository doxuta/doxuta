## Lược đồ dữ liệu phần đặt thuê

Toàn bộ dữ liệu ExamLap nằm trong một cơ sở dữ liệu PostgreSQL 17 duy nhất, chia làm ba cụm theo nghiệp vụ. Cụm thứ nhất trả lời câu hỏi "ai đặt gì, cho ca thi nào".

<<<landscape>>>

![Lược đồ quan hệ cụm đặt thuê, gồm bảy bảng: users nối với kyc_profiles một-một và với orders một-nhiều; device_models và exam_slots cùng cấp suất cho inventory_holds và orders; mỗi suất giữ trong inventory_holds chuyển thành tối đa một đơn.](assets/diagrams/09a-erd-dat-thue.png){w=0}{src: Nguồn: nhóm tác giả.}

<<<portrait>>>

Điểm cần đọc kỹ trong hình là bảng `inventory_holds` nằm giữa `device_models` và `orders`. Khách chọn **nhóm máy** chứ không chọn một chiếc máy cụ thể, nhưng hệ thống vẫn âm thầm giữ một máy thật cho khách. Mũi tên `INVENTORY_HOLDS ||--o| ORDERS` nói đúng điều đó: suất giữ sinh ra trước, đơn sinh ra sau, và một suất chỉ hoá thành tối đa một đơn. Bảng `kyc_profiles` tách khỏi `users` vì nó chứa dữ liệu nhạy cảm với vòng đời riêng, có cột `images_purge_at` để tự xoá ảnh căn cước sau 90 ngày.

## Lược đồ dữ liệu phần tài sản và vận hành

Cụm thứ hai trả lời câu hỏi "máy nào, đang ở đâu, tình trạng ra sao, ai đã cầm nó".

![Lược đồ quan hệ cụm tài sản, gồm devices thuộc device_models, mỗi đơn có các biên bản handovers, mỗi biên bản kèm nhiều handover_photos có mã băm, cùng hai nhánh incidents và maintenance_logs.](assets/diagrams/09b-erd-tai-san.png){w=12}{src: Nguồn: nhóm tác giả.}

Hai tầng `device_models` và `devices` là chuẩn chung của cả ngành quản lý tài sản, không phải sáng tạo của nhóm. Snipe-IT chia `models` rồi tới `assets` [[ref:https://raw.githubusercontent.com/grokability/snipe-it/master/app/Models/AssetModel.php]], Koha chia đầu sách rồi tới bản sách, và phần mềm cho thuê xe chia hạng xe rồi tới số VIN [[ref:https://www.altexsoft.com/blog/car-rental-reservation-system/]]. Bảng `handovers` có cột `direction` phân biệt chiều giao và chiều thu hồi, nên hai biên bản của cùng một đơn dùng chung một cấu trúc và so được với nhau từng ảnh một.

## Lược đồ dữ liệu phần tiền và kiểm toán

Cụm thứ ba giữ tiền, giá và mọi dấu vết.

<<<landscape>>>

![Lược đồ quan hệ cụm tiền và kiểm toán, gồm payments gắn với orders, pricing_rules gắn với device_models theo ngày hiệu lực, cùng ba bảng audit_logs, notifications và blocklist gắn với users.](assets/diagrams/09c-erd-tien-kiem-toan.png){w=0}{src: Nguồn: nhóm tác giả.}

<<<portrait>>>

Giá không nằm trong mã nguồn mà nằm ở `pricing_rules`, có cột `valid_from` nên đổi giá là thêm một dòng chứ không sửa dòng cũ, và đơn cũ vẫn tra lại được mức giá đúng ngày đặt. Bảng `payments` giữ nguyên văn gói tin của nhà cung cấp ở `raw_payload` kiểu `jsonb`, để khi đối soát lệch thì còn bản gốc mà cãi.

## Mô tả các bảng chính

Toàn bộ tiền dùng kiểu `integer` đơn vị đồng, không dùng số thực và không có phần lẻ. Khoá chính dùng `uuid` sinh bằng `gen_random_uuid()` để mã đơn không đoán được từ mã đơn khác.

| Bảng | Cột | Kiểu | Ràng buộc | Ý nghĩa nghiệp vụ |
|---|---|---|---|---|
| `users` | `id` | `uuid` | `PRIMARY KEY` | Định danh người dùng |
| | `email_fpt` | `citext` | `NOT NULL UNIQUE` | Lớp sàng lọc đầu vào thứ nhất, bắt buộc đuôi `@fpt.edu.vn` |
| | `student_code` | `text` | `NOT NULL` | Mã số sinh viên, đối chiếu với hồ sơ eKYC |
| | `role` | `text` | `CHECK IN ('student','staff','admin')` | Ba vai trong hệ thống |
| | `status` | `text` | `CHECK IN ('pending_kyc','active','blocked')` | Chưa xác minh thì không đặt được |
| | `trust_score` | `smallint` | `NOT NULL DEFAULT 0` | Quyết định bậc cọc 300.000đ, 150.000đ hay 0đ |
| `devices` | `asset_tag` | `text` | `NOT NULL UNIQUE` | Mã khắc laser trên vỏ máy |
| | `serial` | `text` | `NOT NULL UNIQUE` | Sê-ri nhà sản xuất, dùng khi trình báo mất máy |
| | `status` | `text` | `CHECK` chín giá trị vòng đời | Từ `intake` tới `retired`, khớp sơ đồ vòng đời thiết bị |
| | `battery_health_pct` | `smallint` | `CHECK BETWEEN 0 AND 100` | Dưới 80 thì máy tự rơi vào diện bảo trì |
| | `seb_tested_at` | `timestamptz` | có thể `NULL` | Lần cuối chạy thử Safe Exam Browser, là lời hứa bán hàng |
| | `last_checkin_at` | `timestamptz` | có thể `NULL` | Nhịp check-in MDM 15 phút một lần |
| | `total_rented_minutes` | `integer` | `NOT NULL DEFAULT 0` | Dùng để rải hao mòn đều khi tự chọn máy |
| `exam_slots` | `exam_date` | `date` | `NOT NULL` | Ngày thi |
| | `name` | `text` | `NOT NULL`, `UNIQUE (exam_date, name)` | Tên ca, ví dụ "Ca 1 sáng" |
| | `pickup_at` | `timestamptz` | `NOT NULL` | Giờ hẹn giao, đặt trước giờ thi 30 phút |
| | `return_due_at` | `timestamptz` | `CHECK (return_due_at > pickup_at)` | Mốc bắt đầu tính phí trả trễ |
| `inventory_holds` | `device_id` | `uuid` | `NOT NULL REFERENCES devices` | Máy thật bị giữ, khách không nhìn thấy |
| | `period` | `tstzrange` | `NOT NULL`, biên nửa mở `[)` | Khoảng thời gian bị chiếm, đã cộng 90 phút quay vòng |
| | `status` | `text` | `CHECK IN ('active','converted','cancelled')` | Huỷ thì đổi cờ, không xoá dòng |
| | `expires_at` | `timestamptz` | có chỉ mục riêng | Hạn giữ suất 10 phút |
| | ràng buộc bảng | | `EXCLUDE USING gist` | Chống trùng lịch ở cấp cơ sở dữ liệu |
| `orders` | `code` | `text` | `NOT NULL UNIQUE` | Mã đơn khách đọc được, dạng `EXL26-000123` |
| | `device_id` | `uuid` | `NULL` tới bước gán máy | Điền trễ nhất có thể, để còn hoán đổi máy |
| | `status` | `text` | `CHECK` mười ba giá trị | Khớp đúng máy trạng thái đơn thuê |
| | `rent_fee` | `integer` | `CHECK (rent_fee >= 0)` | 79.000đ, 99.000đ hay 129.000đ tuỳ nhóm máy |
| | `waiver_fee` | `integer` | `CHECK (waiver_fee IN (0, 15000))` | Phí miễn trừ thiệt hại tự chọn |
| | `deposit` | `integer` | `CHECK (deposit IN (0, 150000, 300000))` | Ba bậc cọc theo điểm tín nhiệm |
| `payments` | `order_id` | `uuid` | `NOT NULL REFERENCES orders` | Một đơn có nhiều giao dịch |
| | `kind` | `text` | `CHECK IN ('rent','waiver','deposit','late_fee','deduction','refund')` | Tách tiền thuê với tiền cọc, vì cọc phải trả lại |
| | `provider_txn_id` | `text` | `UNIQUE (provider, provider_txn_id)` | Khoá khử trùng lặp webhook |
| | `raw_payload` | `jsonb` | `NOT NULL` | Gói tin gốc của nhà cung cấp, giữ để đối soát |
| | `status` | `text` | `CHECK IN ('pending','succeeded','failed','refunded')` | Chỉ `succeeded` mới vào báo cáo doanh thu |
{caption: Cột, kiểu, ràng buộc và ý nghĩa nghiệp vụ của sáu bảng quan trọng nhất trong lược đồ ExamLap.}
{widths: 3,4,3,6,8}
{note: Các cột phụ trợ như `created_at`, `updated_at`, `deleted_at` có ở mọi bảng nhưng không liệt kê lại.}

Dưới đây là câu lệnh tạo thật của hai bảng nặng nhất về quy tắc.

```sql
CREATE TABLE orders (
    id          uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    code        text NOT NULL UNIQUE,
    user_id     uuid NOT NULL REFERENCES users(id),
    model_id    uuid NOT NULL REFERENCES device_models(id),
    slot_id     uuid NOT NULL REFERENCES exam_slots(id),
    device_id   uuid REFERENCES devices(id),          -- NULL cho tới bước gán máy
    status      text NOT NULL DEFAULT 'draft',
    rent_fee    integer NOT NULL CHECK (rent_fee >= 0),
    waiver_fee  integer NOT NULL DEFAULT 0      CHECK (waiver_fee IN (0, 15000)),
    deposit     integer NOT NULL DEFAULT 300000 CHECK (deposit IN (0, 150000, 300000)),
    late_fee    integer NOT NULL DEFAULT 0      CHECK (late_fee BETWEEN 0 AND 200000),
    created_at  timestamptz NOT NULL DEFAULT now(),
    updated_at  timestamptz NOT NULL DEFAULT now(),

    CONSTRAINT orders_status_valid CHECK (status IN (
        'draft','pending_payment','paid','assigned','renting','overdue',
        'pending_inspection','incident','refunded','no_show','lost',
        'hold_expired','closed')),

    -- Từ bước gán máy trở đi, đơn bắt buộc phải trỏ vào một máy thật.
    CONSTRAINT orders_device_required CHECK (
        device_id IS NOT NULL
        OR status IN ('draft','pending_payment','paid','hold_expired','no_show'))
);

-- Một sinh viên chỉ giữ được một đơn còn sống cho mỗi ca thi.
CREATE UNIQUE INDEX orders_one_live_per_slot ON orders (user_id, slot_id)
    WHERE status NOT IN ('hold_expired','no_show','closed');
```
{caption: Câu lệnh tạo bảng orders, với ràng buộc CHECK làm mười ba trạng thái của đơn thành dữ liệu tường minh thay vì rải điều kiện trong mã nguồn.}

```sql
CREATE EXTENSION IF NOT EXISTS btree_gist;   -- cần để dùng '=' trong chỉ mục GiST

CREATE TABLE inventory_holds (
    id          uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    order_id    uuid REFERENCES orders(id) ON DELETE CASCADE,  -- suất sinh trước đơn
    user_id     uuid NOT NULL REFERENCES users(id),
    model_id    uuid NOT NULL REFERENCES device_models(id),
    slot_id     uuid NOT NULL REFERENCES exam_slots(id),
    device_id   uuid NOT NULL REFERENCES devices(id),
    period      tstzrange NOT NULL,          -- đã cộng 90 phút quay vòng
    status      text NOT NULL DEFAULT 'active'
                CHECK (status IN ('active','converted','cancelled')),
    expires_at  timestamptz,                 -- hạn giữ suất, 10 phút
    created_at  timestamptz NOT NULL DEFAULT now(),

    -- Hai suất chồng thời gian trên cùng một máy là điều PostgreSQL từ chối ghi.
    CONSTRAINT inventory_holds_no_overlap
        EXCLUDE USING gist (device_id WITH =, period WITH &&)
        WHERE (status <> 'cancelled')
);

CREATE INDEX inventory_holds_expiry_idx ON inventory_holds (expires_at)
    WHERE status = 'active';
CREATE INDEX inventory_holds_slot_idx ON inventory_holds (slot_id, model_id)
    WHERE status <> 'cancelled';
```
{caption: Câu lệnh tạo bảng inventory_holds, trái tim kỹ thuật của hệ thống, với ràng buộc loại trừ chống trùng lịch.}

## Bài toán thứ nhất: không được bán trùng một chiếc máy

Đây là bài toán tốn công nhất, và cũng là bài toán mà một lỗi duy nhất đủ giết dịch vụ: hai sinh viên cầm hai xác nhận đặt chỗ cho cùng một chiếc máy, sáng ngày thi chỉ một người có máy.

### Vì sao đặt theo nhóm máy lại dễ hơn đặt theo máy cụ thể

Có hai bài toán khác nhau rất dễ bị nhầm làm một. Bài toán thứ nhất là **trùng lịch trên một máy**: máy `FPTDN-LT-007` có bị đặt hai lần trong khung 07:30 tới 11:30 ngày 20/09 không. Bài toán thứ hai là **bán vượt tổng kho**: ngày 20/09 có 12 người đặt nhóm A trong khi nhóm A chỉ có 5 máy. Bài toán thứ nhất là ràng buộc giữa hai dòng dữ liệu, cơ sở dữ liệu tự ép được. Bài toán thứ hai là ràng buộc trên một phép đếm, không ép bằng ràng buộc được mà phải khoá hoặc đếm bằng bảng riêng.

ExamLap chọn cách khiến bài toán thứ hai biến mất: khách chọn nhóm máy, nhưng ngay trong giao dịch đó hệ thống gán luôn một máy thật vào `inventory_holds.device_id`. Không còn suất trừu tượng nào để đếm, nên chỉ còn bài toán thứ nhất. Khách vẫn không thấy sê-ri, nên người trực được quyền hoán đổi máy tới tận phút chót bằng một câu `UPDATE inventory_holds SET device_id = ...`, và ràng buộc loại trừ tự kiểm tra hộ. Mô hình lai này chính là cách Koha làm với sách: cột `item_id` trong bảng `bookings` để được `NULL`, còn chú thích của cột `itemnumber` trong bảng `reserves` ghi rõ nó vừa có nghĩa "bản sách khách chỉ đích danh" vừa có nghĩa "bản sách mà suất giữ này được gán lúc thực hiện" [[ref:https://raw.githubusercontent.com/Koha-Community/Koha/master/installer/data/mysql/kohastructure.sql]]. Ngành khách sạn gọi đây là bán theo hạng phòng và gán phòng lúc nhận phòng, và nguồn nhóm đọc được cho rằng chuyển sang cách bán này đẩy công suất phòng lên trên 80% *[Cần kiểm chứng]*, nhưng cũng cảnh báo mặt trái là gán quá sớm thì phải từ chối khách trong khi vẫn còn phòng phù hợp [[ref:https://www.hospitalitynet.org/opinion/4074675.html]] [[ref:https://dev.to/sumedhbala/hotel-booking-schema-design-comparison-g3h]]. Với ExamLap, lợi ích lớn nhất không phải công suất mà là khả năng đổi máy: cam kết đổi máy trong 15 phút nếu máy lỗi giữa ca thi chỉ thực hiện được khi đơn không bị đóng đinh vào một sê-ri.

### Ba cách chống đặt trùng

**Cách một, khoá bi quan bằng `SELECT ... FOR UPDATE`.** Giao dịch giành khoá độc quyền trên dòng máy ngay đầu, mọi yêu cầu khác trên cùng máy phải xếp hàng chờ tới khi khoá được nhả [[ref:https://medium.com/javarevisited/booking-system-with-pessimistic-locks-4ec107e4bd5]] [[ref:https://oneuptime.com/blog/post/2026-01-30-pessimistic-locking-implementation/view]]. Nguồn kỹ thuật nhóm đọc được nói đúng bối cảnh của ExamLap: khoá bi quan là lựa chọn đúng khi va chạm thường xuyên và việc thử lại tốn kém, đặc biệt với hệ thống tồn kho và hệ thống đặt chỗ, còn lưu lượng thấp thì khoá bi quan là cách đơn giản nhất [[ref:https://adamdjellouli.com/articles/databases_notes/07_concurrency_control/04_double_booking_problem]] [[ref:https://clixo.sh/blog/prevent-double-booking-concurrent-reservation-requests]]. Nhược điểm là giảm thông lượng, tăng nguy cơ khoá chết, và quan trọng hơn cả: nó chỉ đúng khi mọi đường ghi đều nhớ khoá. Một lập trình viên viết đường ghi mới mà quên khoá là thủng.

**Cách hai, khoá lạc quan bằng cột phiên bản.** Thêm cột `version`, câu `UPDATE` chỉ thành công nếu `version` chưa đổi, không dòng nào bị ảnh hưởng thì đọc lại và thử lại [[ref:https://dev.to/iprajapatiparesh/stop-double-booking-optimistic-locking-in-laravel-j5n]] [[ref:https://dev.to/jacktt/optimistic-lock-pessimistic-lock-4h36]]. Cách này hợp khi va chạm hiếm, nhưng có một cảnh báo giết chết nó trong bối cảnh ExamLap: không dùng được khoá lạc quan khi phải chờ thanh toán, vì nhiều người kịp trả tiền nhưng chỉ người đầu tiên nhận được chỗ [[ref:https://flylib.com/books/en/2.196.1/hack_66_use_optimistic_locking.html]]. ExamLap có bước chuyển khoản VietQR nằm giữa lúc bấm đặt và lúc xác nhận, nên nhóm loại cách này.

**Cách ba, ràng buộc loại trừ của PostgreSQL.** Cột thời gian khai kiểu `tstzrange`, cặp `(device_id, period)` gắn `EXCLUDE USING gist` với toán tử `=` và `&&`, và extension `btree_gist` cho phép toán tử `=` nằm chung một chỉ mục GiST với cột khoảng thời gian [[ref:https://chat2db.ai/resources/blog/postgres-exclusion-constraints-guide]] [[ref:https://www.jusdb.com/blog/postgresql-range-types-exclusion-constraints]]. Quy tắc "không hai suất nào chồng lịch trên cùng một máy" trở thành một luật mà cơ sở dữ liệu tự thực thi y như `UNIQUE`, bất kể yêu cầu đến từ API, từ tác vụ nền hay từ một lần sửa tay trong `psql` [[ref:https://dev.to/akincskn/i-solved-double-booking-without-locks-using-one-postgresql-constraint-209m]] [[ref:https://dev.to/franckpachot/postgresql-exclude-constraints-for-better-concurrency-than-serializable-pob]]. MySQL không có `EXCLUDE` và không có kiểu khoảng, và bằng chứng thực nghiệm cho điều đó nằm ngay trong mã nguồn: Koha lẫn LibreBooking đều là hệ đặt lịch trưởng thành, đều chạy MySQL, và đều không có ràng buộc chống trùng lịch nào ở cấp cơ sở dữ liệu, buộc phải kiểm bằng mã PHP [[ref:https://raw.githubusercontent.com/LibreBooking/app/master/database_schema/create-schema.sql]].

### Nhóm chọn gì

Nhóm dùng cả cách một và cách ba, xếp thành ba lớp. Lớp giao diện chỉ hiển thị ca còn chỗ, nên chặn phần lớn va chạm trước khi chúng xảy ra. Lớp nghiệp vụ dùng `FOR UPDATE SKIP LOCKED` để tuần tự hoá và trả thông báo tiếng Việt tử tế. Lớp cơ sở dữ liệu dùng `EXCLUDE` làm lưới cuối, không bao giờ sai kể cả khi hai lớp trên có lỗi. Nhóm **không** dùng khoá phân tán Redis, vì hệ thống chỉ có một cơ sở dữ liệu và khoá Redis không có tính bền vững của giao dịch [[ref:https://redis.io/tutorials/inventory-reservation-in-real-time-with-redis/]].

```sql
BEGIN;

-- Bước 1: chọn một máy thật còn rảnh trong đúng nhóm khách đã chọn.
--   ORDER BY total_rented_minutes: rải hao mòn đều toàn đội, không luôn lấy máy cũ nhất.
--   SKIP LOCKED: yêu cầu tới sau không xếp hàng chờ mà nhảy ngay sang máy kế tiếp.
SELECT d.id
FROM devices d
WHERE d.model_id = $1
  AND d.status   = 'ready'
  AND NOT EXISTS (
        SELECT 1 FROM inventory_holds h
        WHERE h.device_id = d.id
          AND h.status <> 'cancelled'
          AND h.period && tstzrange($2, $3, '[)')   -- && là toán tử giao nhau
  )
ORDER BY d.total_rented_minutes ASC, d.id
FOR UPDATE OF d SKIP LOCKED
LIMIT 1;

-- Bước 2: ghi suất giữ. Cộng 90 phút quay vòng vào biên phải, vì giữa hai lượt
--   máy phải xoá dữ liệu, chạy lại danh mục sẵn sàng thi và sạc pin.
--   Nếu có ai chen vào giữa bước 1 và bước 2, ràng buộc loại trừ ném lỗi
--   và cả giao dịch bị huỷ, không có chuyện ghi được nửa vời.
INSERT INTO inventory_holds (order_id, user_id, model_id, slot_id, device_id,
                             period, expires_at)
VALUES ($4, $5, $1, $6, $7,
        tstzrange($2, $3 + interval '90 minutes', '[)'),
        now() + interval '10 minutes');

COMMIT;
```
{caption: Giao dịch giữ suất kho của ExamLap, kết hợp khoá bi quan bỏ qua dòng đã khoá ở tầng nghiệp vụ với ràng buộc loại trừ ở tầng cơ sở dữ liệu.}

Biên nửa mở `[)` được chọn có chủ ý: một đơn kết thúc lúc 12:00 và một đơn bắt đầu lúc 12:00 không bị coi là chồng nhau, nên cho thuê nối tiếp được. Khoảng đệm 90 phút là tham số mà phần mềm cho thuê Odoo gọi là thời gian an toàn giữa hai đơn thuê [[ref:https://www.odoo.com/documentation/18.0/applications/sales/rental.html]]. Khi vi phạm, PostgreSQL ném lỗi `exclusion_violation` mã `23P01` *[Cần kiểm chứng, nhóm phải tự chạy hai phiên `psql` để xác nhận]*, và tầng ứng dụng bắt đúng mã này rồi trả về câu "Máy nhóm này vừa hết chỗ cho ca thi bạn chọn, mời chọn nhóm khác".

### Hai người bấm đặt cùng lúc thì ai được máy

Giả sử nhóm A còn đúng một máy rảnh cho ca sáng 20/09, mã `FPTDN-LT-003`. An và Bình cùng bấm "Đặt" lúc 07:12:03.

1. Giao dịch của An mở trước vài mili giây, chạy bước 1, tìm thấy `LT-003` và giành khoá dòng đó.
2. Giao dịch của Bình chạy bước 1 ngay sau. Vì có `SKIP LOCKED`, Bình **không** phải chờ An. Bình bỏ qua `LT-003` đang bị khoá và đi tìm máy kế tiếp trong nhóm A.
3. Không còn máy nào khác rảnh, câu lệnh của Bình trả về không dòng nào. Tầng ứng dụng thấy kết quả rỗng, trả ngay cho Bình màn hình "nhóm A đã hết cho ca này" kèm gợi ý nhóm B với giá 99.000đ. Bình biết kết quả trong dưới một giây, không phải ngồi chờ.
4. An ghi dòng `inventory_holds` với `expires_at` là 07:22:03 rồi `COMMIT`. Máy được giữ.
5. Nếu An không chuyển khoản trong 10 phút, tác vụ nền chạy mỗi phút sẽ đổi cờ dòng đó thành `cancelled`. Vì ràng buộc loại trừ có mệnh đề `WHERE (status <> 'cancelled')`, máy tự động rảnh lại mà không cần xoá dòng nào, nên lịch sử vẫn còn nguyên để phân tích tỉ lệ rơi đơn.

Trường hợp xấu nhất là hai giao dịch cùng đọc thấy `LT-003` rảnh vì lý do nào đó ở lớp nghiệp vụ, ví dụ một tác vụ nền viết sai. Khi đó cả hai cùng chạy `INSERT`, giao dịch thứ hai vi phạm ràng buộc loại trừ, PostgreSQL huỷ nguyên giao dịch. Kết quả xấu nhất là một người nhận thông báo lỗi, chứ không bao giờ là hai người cùng nhận xác nhận cho một máy.

## Bài toán thứ hai: tiền vào một lần, ghi nhận một lần

Sinh viên bấm nút "Đặt máy" trên điện thoại, sóng 4G trong khuôn viên trường chập chờn, và bấm lại hai ba lần. Nếu không chống gì, hệ thống tạo ba đơn, giữ ba máy và thu ba lần cọc 300.000đ.

**Mã chống lặp yêu cầu.** Mọi lời gọi `POST /api/orders` phải mang tiêu đề `Idempotency-Key` là một UUID do trình duyệt sinh, theo đúng cách Stripe làm với mọi endpoint có tác dụng thay đổi dữ liệu [[ref:https://stripe.com/blog/idempotency]] [[ref:https://brandur.org/idempotency-keys]]. Máy chủ lưu khoá đó cùng kết quả đã trả; lần gọi sau mang cùng khoá thì nhận lại nguyên văn kết quả cũ chứ không chạy lại việc [[ref:https://httptoolkit.com/blog/idempotency-keys/]]. Nhóm giữ khoá 24 giờ, bằng mức mà tài liệu Stripe nêu *[Cần kiểm chứng]*. Cột `request_hash` chứa mã băm của thân yêu cầu, để chặn trường hợp tái sử dụng cùng một khoá cho hai nội dung khác nhau.

```sql
CREATE TABLE idempotency_keys (
    id            bigserial PRIMARY KEY,
    user_id       uuid NOT NULL REFERENCES users(id),
    key           text NOT NULL,                    -- UUID do trình duyệt sinh
    request_path  text NOT NULL,                    -- 'POST /api/orders'
    request_hash  text NOT NULL,                    -- SHA-256 của thân yêu cầu
    state         text NOT NULL DEFAULT 'in_progress'
                  CHECK (state IN ('in_progress','succeeded','failed')),
    response_code int,
    response_body jsonb,
    created_at    timestamptz NOT NULL DEFAULT now(),
    expires_at    timestamptz NOT NULL DEFAULT now() + interval '24 hours',
    UNIQUE (user_id, key)
);

-- Chèn được nghĩa là lần đầu, xử lý bình thường rồi ghi kết quả vào response_body.
-- Không chèn được: state='succeeded' thì trả lại y nguyên response_body cũ;
-- state='in_progress' thì trả HTTP 409, nghĩa là "đang xử lý, đừng bấm nữa".
INSERT INTO idempotency_keys (user_id, key, request_path, request_hash)
VALUES ($1, $2, 'POST /api/orders', $3)
ON CONFLICT (user_id, key) DO NOTHING
RETURNING id;
```
{caption: Bảng chống lặp yêu cầu theo mẫu Stripe, và câu lệnh chèn quyết định đây là lần gọi đầu hay lần bấm lại.}

**Khử trùng lặp webhook.** Cổng thanh toán chắc chắn sẽ gửi lại cùng một sự kiện nhiều lần, đó là thiết kế chứ không phải lỗi: mọi hệ gửi webhook tử tế đều thử lại theo lịch giãn cách khi không nhận được HTTP 200 [[ref:https://matheuspalma.com/blog/outbound-webhook-delivery-signing-retries-dead-letters]] [[ref:https://www.educative.io/blog/webhook-system-design]]. Vì vậy cột `provider_txn_id` phải là duy nhất theo cặp `(provider, provider_txn_id)`. Đó là mã giao dịch do chính nhà cung cấp sinh, ổn định qua mọi lần gửi lại, nên nó là thứ duy nhất trong gói tin có thể dùng làm danh tính của sự kiện. Nếu chỉ dựa vào số tiền và mã đơn thì hai lần chuyển khoản hợp lệ cùng số tiền cho cùng đơn sẽ bị nhầm thành một, và một lần gửi lại sẽ bị nhầm thành hai. Quy trình xử lý gồm ba việc theo đúng thứ tự: kiểm chữ ký HMAC trên thân thô trước khi tin bất cứ điều gì, ghi bản ghi rồi trả HTTP 200 thật nhanh, và để tác vụ nền đổi trạng thái đơn. Trả 200 chậm thì cổng thanh toán coi là thất bại và gửi lại, nhân đôi tải đúng lúc đang nghẽn.

**Mẫu hộp thư đi.** Khi đơn chuyển sang trạng thái đã thanh toán, hệ thống phải báo cho khách. Gọi API gửi tin ngay trong giao dịch thì giao dịch có thể quay lui trong khi tin đã bay đi, khách nhận xác nhận cho một đơn không tồn tại. Gọi sau khi kết thúc giao dịch thì máy chủ sập giữa chừng là khách không nhận được gì. Cách giải là ghi một dòng vào `outbox_messages` **trong cùng giao dịch** với thay đổi nghiệp vụ, rồi một tiến trình riêng đọc bảng đó và gửi đi [[ref:https://milanjovanovic.tech/blog/implementing-the-outbox-pattern]] [[ref:https://github.com/Zehelein/pg-transactional-outbox]]. Thứ đạt được không phải là gửi đúng một lần, vì trên mạng điều đó bất khả thi, mà là gửi ít nhất một lần cộng với xử lý có tính chống lặp, cho ra kết quả tương đương gửi đúng một lần [[ref:https://www.glukhov.org/app-architecture/integration-patterns/transactional-outbox-pattern-go/]].

```sql
-- Cùng một giao dịch: đổi trạng thái đơn và xếp hàng thông báo.
BEGIN;
  INSERT INTO payments (order_id, kind, method, amount, provider, provider_txn_id,
                        status, raw_payload)
  VALUES ($1, 'rent', 'vietqr', $2, 'vietqr', $3, 'succeeded', $4)
  ON CONFLICT (provider, provider_txn_id) DO NOTHING;   -- gửi lại 10 lần vẫn 1 dòng

  UPDATE orders SET status = 'paid', updated_at = now()
   WHERE id = $1 AND status = 'pending_payment';        -- chỉ tiến, không lùi

  INSERT INTO outbox_messages (topic, payload)
  VALUES ('order.paid', jsonb_build_object('order_id', $1));
COMMIT;

-- Tiến trình gửi tin chạy riêng, nhiều bản sao chạy song song vẫn an toàn.
BEGIN;
  SELECT id, topic, payload FROM outbox_messages
   WHERE processed_at IS NULL AND retry_after <= now()
   ORDER BY id
   FOR UPDATE SKIP LOCKED
   LIMIT 20;
  -- gửi Zalo hoặc email, thành công thì UPDATE processed_at = now();
  -- thất bại thì attempts = attempts + 1,
  --   retry_after = now() + interval '1 minute' * power(2, attempts)
COMMIT;
```
{caption: Ghi thanh toán, đổi trạng thái đơn và xếp hàng thông báo trong cùng một giao dịch, kèm vòng lấy việc của tiến trình gửi tin.}

## Bài toán thứ ba: nhật ký không sửa được

Ba tranh chấp gần như chắc chắn sẽ xảy ra: máy đã xước từ trước khi thuê, khách khai trả máy lúc 17:00 chứ không phải 19:00, và khách khẳng định đã trả đủ sạc. Với giá trị mỗi máy từ 6.500.000đ tới 10.000.000đ, một vụ tranh chấp có thể lên tới vài triệu đồng, nên nhật ký phải đủ tin cậy để làm bằng chứng.

Bảng `audit_logs` ghi mọi thao tác có ý nghĩa: chuyển trạng thái đơn, gán máy, hoán đổi máy, ký biên bản, hoàn cọc, khấu trừ, khoá màn hình, sửa giá, mở hồ sơ eKYC, thêm người vào danh sách chặn. Mỗi dòng lưu người gây ra, hành động, đối tượng, giá trị trước và sau ở cột `payload` kiểu `jsonb`, địa chỉ IP và thời điểm. Đây là mô hình đa hình mà Snipe-IT dùng cho bảng `action_logs` của nó, với cặp `item_type` và `item_id` cho đối tượng bị tác động [[ref:https://deepwiki.com/grokability/snipe-it/4.4-activity-logging]]. Nhưng nhóm làm khác Snipe-IT ở một điểm quan trọng: bảng `action_logs` của Snipe-IT có xoá mềm, nghĩa là nhật ký của nó vẫn xoá được [[ref:https://github.com/grokability/snipe-it/blob/master/database/migrations/2016_09_04_180400_create_actionlog_table.php]].

Chống sửa ở mức cơ sở dữ liệu gồm hai việc: thu hồi quyền của tài khoản ứng dụng, và gắn trigger ném ngoại lệ. Hai việc chứ không phải một, vì thu hồi quyền chặn tài khoản ứng dụng nhưng không chặn tài khoản chủ sở hữu bảng, còn trigger chặn mọi vai [[ref:https://www.designgurus.io/answers/detail/how-do-you-enforce-immutability-and-appendonly-audit-trails]].

```sql
CREATE OR REPLACE FUNCTION audit_logs_immutable() RETURNS trigger AS $$
BEGIN
    RAISE EXCEPTION 'audit_logs chi ghi them: khong duoc UPDATE hoac DELETE';
END; $$ LANGUAGE plpgsql;

CREATE TRIGGER audit_logs_no_update BEFORE UPDATE ON audit_logs
    FOR EACH ROW EXECUTE FUNCTION audit_logs_immutable();
CREATE TRIGGER audit_logs_no_delete BEFORE DELETE ON audit_logs
    FOR EACH ROW EXECUTE FUNCTION audit_logs_immutable();

REVOKE UPDATE, DELETE, TRUNCATE ON audit_logs FROM examlap_app;
GRANT  INSERT, SELECT ON audit_logs TO examlap_app;

-- Tác vụ chạy hằng đêm: trả về dòng nào đứt chuỗi băm thì nhật ký đã bị can thiệp.
SELECT a.seq, a.occurred_at
FROM audit_logs a
JOIN audit_logs b ON b.seq = a.seq - 1
WHERE a.prev_hash <> b.row_hash;
```
{caption: Chặn sửa và xoá nhật ký ở cấp cơ sở dữ liệu bằng trigger cộng thu hồi quyền, kèm truy vấn kiểm tra chuỗi băm chạy hằng đêm.}

Điều này quan trọng khi phải chứng minh với bên thứ ba. Khi hồ sơ một đơn được kết xuất để trình báo theo *Điều 175 Bộ luật Hình sự 2015*, thứ có sức nặng không phải là ảnh chụp màn hình mà là một chuỗi bản ghi mà chính nhóm cũng không sửa được. Chỉ ghi thêm bảo vệ nhóm khỏi lỗi của mã nguồn mình, nhưng tự nó chưa chứng minh được với người ngoài rằng không ai có quyền truy cập đã lặng lẽ sửa một dòng, và đó là lý do mỗi dòng còn mang mã băm của dòng trước [[ref:https://tracehold.ai/blog/immutable-audit-log-hmac-hash-chain/]] [[ref:https://medium.com/@veritaschain/append-only-is-the-easy-part-e25820208213]].

## Bài toán thứ tư: ảnh hiện trạng phải chứng minh được

Mỗi chiều bàn giao có sáu ảnh: mặt A, mặt đáy, hai cạnh bên, màn hình đang bật nền trắng và cụm phụ kiện trải ra. Ảnh nằm ở kho đối tượng, còn cơ sở dữ liệu chỉ giữ đường dẫn, nên có một lỗ hổng hiển nhiên: ai có quyền ghi vào kho ảnh đều thay được tệp mà bản ghi không đổi. Vì vậy mỗi dòng `handover_photos` lưu thêm `sha256`, là mã băm của đúng chuỗi byte ảnh tại thời điểm tải lên, tính trên máy chủ sau khi nhận tệp chứ không tính ở điện thoại, để thiết bị của người dùng không quyết định được kết quả. Một hệ chuỗi trách nhiệm bất biến đúng nghĩa phải chỉ ghi thêm về kiến trúc và dùng kiểm tra toàn vẹn bằng mã băm, sao cho mọi nỗ lực sửa sự kiện quá khứ đều lộ ra khi kiểm chứng [[ref:https://www.locatorx.com/blog/the-truth-about-asset-records-why-immutability-is-the-foundation-of-a-verifiable-chain-of-custody]].

Cách kiểm tra lại sau này rất đơn giản, và đó chính là điểm mạnh: bất kỳ ai cũng làm được bằng một lệnh có sẵn trên mọi máy tính, không cần phần mềm của ExamLap.

```bash
sha256sum mat-a-giao.jpg    # bên khiếu nại tự tính lại mã băm của ảnh tải về
9f2ca41b8d3e...c07  mat-a-giao.jpg    # so với con số in trên biên bản PDF
```
{caption: Kiểm chứng một ảnh hiện trạng bằng lệnh có sẵn trên mọi hệ điều hành, không cần công cụ của ExamLap.}

```sql
-- Chống thay ảnh im lặng: cùng một biên bản không được có hai ảnh cùng góc,
-- và mã băm được ghi một lần rồi không sửa nữa.
ALTER TABLE handover_photos
  ADD CONSTRAINT handover_photos_one_per_angle UNIQUE (handover_id, angle),
  ADD CONSTRAINT handover_photos_sha256_format CHECK (sha256 ~ '^[0-9a-f]{64}$');

-- Truy vấn đối chiếu sáu ảnh lúc giao với sáu ảnh lúc nhận của cùng một đơn.
SELECT g.angle, g.sha256 AS bam_luc_giao, n.sha256 AS bam_luc_nhan
FROM handover_photos g
JOIN handovers hg ON hg.id = g.handover_id AND hg.direction = 'out'
JOIN handovers hn ON hn.order_id = hg.order_id AND hn.direction = 'in'
LEFT JOIN handover_photos n ON n.handover_id = hn.id AND n.angle = g.angle
WHERE hg.order_id = $1
ORDER BY g.angle;
```
{caption: Ràng buộc bảo vệ bộ ảnh hiện trạng và truy vấn ghép cặp ảnh trước với ảnh sau theo từng góc chụp.}

Mã băm không chứng minh ảnh phản ánh đúng sự thật, nó chỉ chứng minh ảnh chưa bị thay kể từ lúc ký biên bản. Nhóm nói rõ giới hạn này thay vì diễn đạt quá lời.

## Truy vấn hay dùng và chỉ mục cần có

Bốn truy vấn dưới đây chiếm gần hết tải đọc của hệ thống.

```sql
-- (1) Nhóm máy nào còn trống cho một ca thi. Chạy mỗi lần khách mở trang đặt.
SELECT m.id, m.name, count(d.id) AS so_may_ranh
FROM device_models m
JOIN devices d ON d.model_id = m.id AND d.status = 'ready'
WHERE NOT EXISTS (
      SELECT 1 FROM inventory_holds h
      WHERE h.device_id = d.id AND h.status <> 'cancelled'
        AND h.period && tstzrange($1, $2, '[)')
) AND m.exam_ready
GROUP BY m.id, m.name
HAVING count(d.id) > 0
ORDER BY m.name;

-- (2) Danh sách đơn của một ca thi. Màn hình điều phối của người trực sáng ngày thi.
SELECT o.code, u.student_code, u.email_fpt, m.name AS nhom_may,
       d.asset_tag, o.status, o.rent_fee + o.waiver_fee AS phai_thu
FROM orders o
JOIN users u        ON u.id = o.user_id
JOIN device_models m ON m.id = o.model_id
LEFT JOIN devices d  ON d.id = o.device_id
WHERE o.slot_id = $1 AND o.status <> 'hold_expired'
ORDER BY o.status, o.code;

-- (3) Máy đang cho thuê mà lỡ hai nhịp check-in MDM liên tiếp.
SELECT d.asset_tag, o.code, u.email_fpt, u.student_code,
       now() - d.last_checkin_at AS tre_bao_lau
FROM devices d
JOIN orders o ON o.device_id = d.id AND o.status IN ('renting','overdue')
JOIN users  u ON u.id = o.user_id
WHERE d.last_checkin_at < now() - interval '30 minutes'
ORDER BY d.last_checkin_at;

-- (4) Doanh thu theo tháng, tách rõ từng loại phí. Tiền cọc không phải doanh thu.
SELECT date_trunc('month', p.created_at AT TIME ZONE 'Asia/Ho_Chi_Minh') AS thang,
       count(DISTINCT p.order_id)                       AS so_luot,
       sum(p.amount) FILTER (WHERE p.kind = 'rent')     AS tien_thue,
       sum(p.amount) FILTER (WHERE p.kind = 'waiver')   AS phi_mien_tru,
       sum(p.amount) FILTER (WHERE p.kind = 'late_fee') AS phi_tra_tre
FROM payments p
WHERE p.status = 'succeeded' AND p.kind NOT IN ('deposit','refund')
GROUP BY 1
ORDER BY 1;
```
{caption: Bốn truy vấn chiếm phần lớn tải đọc của hệ thống, viết bằng SQL chạy được trên lược đồ đã mô tả.}

| Truy vấn | Chỉ mục phục vụ | Vì sao cần |
|---|---|---|
| (1) Máy trống theo ca | Chỉ mục GiST do `EXCLUDE USING gist (device_id, period)` tự sinh, cộng `devices (model_id, status)` | Ràng buộc chống trùng lịch đã tạo sẵn chỉ mục GiST trên cặp máy và khoảng thời gian, nên phép kiểm `&&` dùng lại được, không cần chỉ mục thứ hai |
| (2) Đơn của một ca | `orders (slot_id, status)` | Bảng `orders` lớn dần theo từng học kỳ, còn màn hình điều phối luôn lọc theo đúng một ca; chỉ mục ghép hai cột cho phép lấy và sắp xếp trong một lần quét |
| (3) Máy mất tín hiệu | `devices (last_checkin_at) WHERE status = 'rented'` | Chỉ mục bộ phận chỉ chứa vài máy đang cho thuê thay vì cả đội, nên nhỏ và luôn nằm trong bộ nhớ dù truy vấn chạy mỗi phút |
| (4) Doanh thu theo tháng | `payments (created_at) WHERE status = 'succeeded'` | Giao dịch thất bại và đang chờ chiếm phần không nhỏ nhưng không bao giờ vào báo cáo, loại chúng khỏi chỉ mục là loại khỏi mọi lần quét |
{caption: Bốn chỉ mục tương ứng bốn truy vấn nóng, kèm lý do chọn đúng dạng chỉ mục đó.}
{widths: 4,7,10}

:::note Ba con số quyết định thiết kế này
Đội máy năm đầu là 10 chiếc và 382 lượt thuê một năm, tức trung bình chưa tới hai lượt mỗi ngày, dồn vào sáu đợt cao điểm.
Ở quy mô đó, mọi truy vấn trên đều chạy dưới 10 mili giây, và lựa chọn kỹ thuật không nhằm chịu tải mà nhằm **không sai một lần nào** vào đúng sáng ngày thi.
Nhóm đặt mục tiêu số lần bán trùng một máy trong cả năm đầu là **không**, và đó là chỉ số duy nhất của chương này mà nhóm không chấp nhận sai số.
:::
