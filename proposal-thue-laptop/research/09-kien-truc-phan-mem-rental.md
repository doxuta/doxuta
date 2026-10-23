# 09 — KIẾN TRÚC PHẦN MỀM CHO HỆ THỐNG ĐẶT THUÊ LAPTOP (thiết bị định danh theo serial)

> **Dự án:** Website cho thuê laptop đi thi — quy mô 15–40 máy — quanh Đại học FPT Đà Nẵng (P. Hoà Hải, Ngũ Hành Sơn, Đà Nẵng)
> **Bối cảnh nghiệp vụ đã xác minh ở các file nghiên cứu khác:** SV FPT thi bằng máy cá nhân, phần mềm EOS + Safe Exam Browser, **bắt buộc Windows**; Mac chip M1/M2 không thi được.
> **Ngày nghiên cứu:** 14/09/2026
> **File này là NGUYÊN LIỆU THÔ** cho phần "Giải pháp công nghệ / Kiến trúc hệ thống" của proposal.

---

## 0. CÁCH ĐỌC FILE NÀY — MỨC ĐỘ TIN CẬY CỦA TỪNG SỐ LIỆU

Mỗi khối thông tin được gắn nhãn:

| Nhãn | Ý nghĩa |
|---|---|
| **[MÃ NGUỒN]** | Tôi đã **tải trực tiếp mã nguồn/schema thật** về máy và đọc. Tên bảng, tên cột, kiểu dữ liệu là **chính xác nguyên văn**. Độ tin cậy cao nhất. |
| **[REGISTRY]** | Lấy trực tiếp từ registry gói (npmjs.org, packagist.org, pypi.org, proxy.golang.org) — số phiên bản và ngày phát hành là thật. |
| **[SNIPPET]** | **Chỉ đọc được tiêu đề + đoạn trích của kết quả tìm kiếm, CHƯA mở được trang gốc** (môi trường nghiên cứu chặn truy cập web thường). **Nhóm SV BẮT BUỘC phải tự mở URL kiểm chứng lại trước khi trích vào proposal.** |
| **[SUY LUẬN]** | Là phân tích/khuyến nghị của tôi dựa trên các dữ kiện trên, **không phải trích dẫn**. Có thể tranh luận. |

> ⚠️ **Ghi chú quan trọng về công cụ:** trong môi trường nghiên cứu này, hầu hết domain web bị chặn (EGRESS_BLOCKED). Tuy nhiên `raw.githubusercontent.com`, `registry.npmjs.org`, `repo.packagist.org`, `pypi.org`, `proxy.golang.org` **truy cập được**. Vì vậy toàn bộ phần schema Snipe-IT, LibreBooking, Koha trong file này là **mã nguồn thật đã tải về**, còn phần bài viết kỹ thuật (blog, Stripe, Redis...) chỉ ở mức snippet.

---

## 1. TÓM TẮT ĐIỀU HÀNH — 10 KẾT LUẬN CHÍNH

1. **Bài toán của dự án KHÔNG phải "đặt phòng khách sạn" mà là "đặt một tài sản định danh trong khoảng thời gian".** Mỗi laptop có serial riêng, cấu hình khác nhau (i5 vs i7, 8GB vs 16GB), nên không thể coi là hàng hoá thay thế được hoàn toàn. **[SUY LUẬN]**

2. **Vũ khí kỹ thuật mạnh nhất và rẻ nhất: PostgreSQL `EXCLUDE USING gist` + `tstzrange` + extension `btree_gist`.** Nó biến "không được trùng lịch trên cùng một máy" thành một **ràng buộc cấp cơ sở dữ liệu**, giống hệt `UNIQUE`. Không code nào có thể phá vỡ được — kể cả khi lập trình viên quên check, kể cả khi sửa tay trong DB. **[SNIPPET — nhiều nguồn đồng thuận]**

3. **MySQL/MariaDB KHÔNG có `EXCLUDE` constraint và không có range type.** Đây là lý do kỹ thuật cụ thể, không phải "thích Postgres hơn", để chọn PostgreSQL cho dự án này. **[SUY LUẬN + xác nhận gián tiếp: Koha và LibreBooking đều chạy MySQL và đều phải kiểm tra trùng lịch ở tầng ứng dụng — bằng chứng mã nguồn ở mục 9.1, 14.1 và 16.1]**

4. **Mô hình dữ liệu chuẩn của ngành = tách 2 tầng: "loại" (model/type) và "cá thể" (unit/item/serial).** Khách đặt theo **loại**, hệ thống **gán máy cụ thể muộn nhất có thể** (late assignment). Koha làm đúng như vậy: bảng `bookings` có `biblio_id NOT NULL` (loại) và `item_id NULL` (cá thể). **[MÃ NGUỒN — Koha kohastructure.sql]**

5. **Snipe-IT là tham chiếu gần nhất về mô hình TÀI SẢN, nhưng KHÔNG phải hệ thống đặt trước.** Snipe-IT có `assets` / `models` / `status_labels` / `action_logs` / `checkout_requests` rất tốt, nhưng **`checkout_requests` chỉ là "xin mượn", không có `start_date`/`end_date`** → **không chống được double-booking theo thời gian**. Đây là khoảng trống mà sản phẩm của nhóm lấp vào. **[MÃ NGUỒN — đã đọc migration thật]**

6. **Snipe-IT dùng giấy phép AGPL-3.0-or-later.** Nếu nhóm fork Snipe-IT và chạy như dịch vụ web thương mại thì **bắt buộc phải công khai mã nguồn đã sửa đổi**. Đây là rủi ro pháp lý phải nêu trong proposal. **[MÃ NGUỒN — `composer.json` ghi rõ `"license": "AGPL-3.0-or-later"`]**

7. **Vòng đời đơn thuê nên được mô hình hoá bằng máy trạng thái (state machine) tường minh**, không dùng cột `status` tự do. Koha đã enum hoá sẵn: `enum('new','cancelled','issued','completed')`. **[MÃ NGUỒN]**

8. **Thanh toán/cọc bắt buộc phải có Idempotency-Key** để một cú bấm "Thanh toán" hai lần (mạng chậm, user bấm lại) không tạo hai đơn/hai lần trừ tiền. Đây là chuẩn công nghiệp của Stripe. **[SNIPPET — stripe.com/blog/idempotency]**

9. **Audit log phải append-only.** Với tài sản có giá trị (laptop 8–20 triệu VNĐ/máy) và tranh chấp "máy đã xước từ trước hay do khách làm", nhật ký bàn giao (chain of custody) là bằng chứng. Nên hash-chain (mỗi bản ghi chứa hash của bản ghi trước). **[SNIPPET]**

10. **Khuyến nghị stack cho nhóm SV FPT:** **Laravel 13 + PostgreSQL 16/17 + Livewire hoặc Blade**, deploy trên **VPS Việt Nam ~75.000–200.000 VNĐ/tháng**. Lý do chi tiết ở mục 16. **[SUY LUẬN + REGISTRY + SNIPPET]**

---

# PHẦN A — CHỐNG DOUBLE-BOOKING / OVERBOOKING

## 2. PHÂN BIỆT HAI BÀI TOÁN KHÁC NHAU (rất hay bị nhầm)

Đây là điểm mấu chốt kiến trúc. **[SUY LUẬN — nhưng là suy luận trực tiếp từ cơ chế của các kỹ thuật bên dưới]**

| | **Bài toán 1: TRÙNG LỊCH TRÊN 1 MÁY** | **Bài toán 2: BÁN QUÁ SỐ MÁY TRONG KHO (overselling pool)** |
|---|---|---|
| Câu hỏi | "Máy #LT-007 có bị đặt 2 lần trong cùng 8h–12h ngày 20/09 không?" | "Ngày 20/09 có 30 người đặt mà mình chỉ có 25 máy Windows i5 không?" |
| Bản chất | Ràng buộc **giữa 2 dòng dữ liệu cụ thể** | Ràng buộc **trên tổng số đếm (COUNT)** |
| `EXCLUDE USING gist` giải được? | ✅ **CÓ — giải triệt để** | ❌ **KHÔNG.** EXCLUDE không đếm được. |
| Cách giải | EXCLUDE constraint | Serializable / advisory lock / bảng đếm tồn kho có version |
| Khi nào gặp ở dự án này | Khi đã gán máy cụ thể cho đơn | Khi cho khách đặt "1 laptop Windows i5" chưa gán serial |

**Hệ quả thiết kế then chốt [SUY LUẬN]:**
> Nếu hệ thống **gán serial ngay khi đặt** → chỉ cần Bài toán 1 → EXCLUDE constraint là đủ, cực kỳ đơn giản, gần như không thể sai.
> Nếu hệ thống cho **đặt theo loại rồi gán muộn** → phải giải cả Bài toán 2 → phức tạp hơn nhiều.
>
> **Với 15–40 máy, khuyến nghị: GÁN SERIAL NGAY KHI ĐẶT** (early assignment) + cho phép admin đổi máy thủ công. Đánh đổi mất vài % hiệu suất lấp đầy kho, nhưng đổi lại độ đúng đắn được DB bảo đảm và code đơn giản hơn nhiều lần. Xem phân tích đánh đổi đầy đủ ở mục 10.

---

## 3. GIẢI PHÁP #1 (KHUYẾN NGHỊ CHÍNH): PostgreSQL `EXCLUDE USING gist` + `tstzrange` + `btree_gist`

### 3.1. Nguyên lý

**[SNIPPET]** Theo nhiều nguồn kỹ thuật tìm được, PostgreSQL có ràng buộc `EXCLUDE` biến quy tắc *"không hai booking nào chồng lịch trên cùng một tài nguyên"* thành một luật mà database tự thực thi **giống hệt cách nó thực thi `UNIQUE` hay `NOT NULL`**:

- Nguồn: [Postgres EXCLUDE Constraints for Overlaps – Chat2DB](https://chat2db.ai/resources/blog/postgres-exclusion-constraints-guide)
- Nguồn: [I Solved Double-Booking Without Locks — Using One PostgreSQL Constraint (dev.to)](https://dev.to/akincskn/i-solved-double-booking-without-locks-using-one-postgresql-constraint-209m)
- Nguồn: [PostgreSQL Range Types and Exclusion Constraints: Prevent Double-Booking at the Database Level (jusdb.com)](https://www.jusdb.com/blog/postgresql-range-types-exclusion-constraints)
- Nguồn: [PostgreSQL's GiST Exclusion Constraint: The Database-Level Answer to Double Bookings (amitavroy.com)](https://amitavroy.com/articles/postgresql-gist-exclusion-constraintthe-database-evel-answer-to-double-bookings)
- Nguồn: [Preventing Overlapping Data in PostgreSQL (blog.danielclayton.co.uk)](https://blog.danielclayton.co.uk/posts/overlapping-data-postgres-exclusion-constraints/)
- Nguồn: [PostgreSQL Range Overlap Queries: GiST Indexes, EXCLUDE Constraints... (Red-Gate Simple Talk)](https://www.red-gate.com/simple-talk/databases/postgresql/overlapping-ranges-in-subsets-in-postgresql/)
- Nguồn: [Avoiding range overlaps in PostgreSQL with EXCLUDE constraint, better than serializable (Franck Pachot, dev.to)](https://dev.to/franckpachot/postgresql-exclude-constraints-for-better-concurrency-than-serializable-pob)
- Nguồn: [Exclusion Constraints in Postgres (Medium)](https://java-jedi.medium.com/exclusion-constraints-b2cbd62b637a)
- Nguồn: [Arrays and range types in PostgreSQL: tags, bookings, EXCLUDE](https://vikulin-va.ru/en/postgres/arrays-ranges/)

**Trích dẫn cốt lõi từ snippet (chưa mở được trang, cần kiểm chứng):**
> *"It doesn't matter if the request comes from the API, a background job, or a manual database edit, Postgres itself refuses the insert if it overlaps. No application code has to remember to check anything, because it is physically impossible to violate."*
> — tạm dịch: *"Không quan trọng request đến từ API, từ background job, hay từ một lần sửa tay trong database — chính Postgres từ chối bản ghi nếu nó chồng lịch. Không dòng code ứng dụng nào phải nhớ kiểm tra gì cả, vì việc vi phạm là bất khả thi về mặt vật lý."*

Vai trò của `btree_gist`: **[SNIPPET]** extension này "dạy" cho chỉ mục GiST hiểu các toán tử kiểu B-tree thông thường — quan trọng nhất là toán tử `=` trên số nguyên/text/date — để nó có thể **nằm chung một chỉ mục GiST đa cột với cột range**. Không có `btree_gist` thì không thể viết `laptop_id WITH =` cạnh `period WITH &&`.

### 3.2. DDL cụ thể cho dự án cho thuê laptop

```sql
-- Bước 1: bật extension (chỉ chạy 1 lần cho mỗi database)
CREATE EXTENSION IF NOT EXISTS btree_gist;

-- Bước 2: bảng cá thể máy (mỗi dòng = 1 máy vật lý có serial)
CREATE TABLE laptops (
    id              bigserial PRIMARY KEY,
    asset_tag       text NOT NULL UNIQUE,        -- mã dán trên máy, vd 'FPTDN-LT-007'
    serial_number   text NOT NULL UNIQUE,        -- serial nhà sản xuất
    model_id        bigint NOT NULL REFERENCES laptop_models(id),
    status          text NOT NULL DEFAULT 'available',
                    -- available | maintenance | retired | lost
    condition_grade text,                        -- A / B / C
    notes           text,
    created_at      timestamptz NOT NULL DEFAULT now(),
    updated_at      timestamptz NOT NULL DEFAULT now()
);

-- Bước 3: bảng đơn thuê (header)
CREATE TABLE rentals (
    id              bigserial PRIMARY KEY,
    code            text NOT NULL UNIQUE,        -- mã đơn hiển thị cho khách, vd 'TL26-000123'
    customer_id     bigint NOT NULL REFERENCES customers(id),
    state           text NOT NULL DEFAULT 'draft',
    deposit_amount  numeric(12,0) NOT NULL DEFAULT 0,   -- VNĐ, không có phần lẻ
    total_amount    numeric(12,0) NOT NULL DEFAULT 0,   -- VNĐ
    created_at      timestamptz NOT NULL DEFAULT now()
);

-- Bước 4: BẢNG QUAN TRỌNG NHẤT — giữ chỗ 1 máy cụ thể trong 1 khoảng thời gian
CREATE TABLE rental_holds (
    id              bigserial PRIMARY KEY,
    rental_id       bigint NOT NULL REFERENCES rentals(id) ON DELETE CASCADE,
    laptop_id       bigint NOT NULL REFERENCES laptops(id),
    period          tstzrange NOT NULL,
    hold_state      text NOT NULL DEFAULT 'active',   -- active | cancelled
    created_at      timestamptz NOT NULL DEFAULT now(),

    -- ★★★ RÀNG BUỘC CHỐNG TRÙNG LỊCH ★★★
    CONSTRAINT rental_holds_no_overlap
      EXCLUDE USING gist (
          laptop_id WITH =,      -- cần btree_gist để dùng '=' trong index GiST
          period    WITH &&      -- && = toán tử "giao nhau" của range
      )
      WHERE (hold_state <> 'cancelled')   -- đơn đã huỷ không chặn đơn mới
);

CREATE INDEX ON rental_holds USING gist (period);
CREATE INDEX ON rental_holds (rental_id);
```

### 3.3. Ba chi tiết kỹ thuật dễ sai — phải nhớ

**(a) Kiểu biên `[)` (nửa mở) là mặc định của `tstzrange` và đúng cho bài toán này.**
`tstzrange('2026-09-20 08:00+07', '2026-09-20 12:00+07')` mặc định là `[)` — bao gồm 08:00, **không** bao gồm 12:00. Nhờ vậy một đơn kết thúc 12:00 và một đơn bắt đầu 12:00 **không bị coi là chồng lịch** → cho thuê nối tiếp được. Nếu dùng `[]` thì hai đơn liền kề sẽ va nhau. **[SUY LUẬN từ ngữ nghĩa range của PostgreSQL — nhóm nên tự chạy thử `SELECT tstzrange('...','...') && tstzrange('...','...')` để xác nhận]**

**(b) Phải cộng thêm "thời gian đệm" (buffer / turnaround) vào range.**
Giữa hai lượt thuê cần thời gian: kiểm tra máy, cài lại/kiểm tra EOS + Safe Exam Browser, sạc pin, lau máy. **Không nên** để hai đơn sát nhau 0 phút.
→ Kỹ thuật: khi ghi vào `period`, cộng thêm buffer, ví dụ 60–120 phút sau giờ trả:
```sql
INSERT INTO rental_holds (rental_id, laptop_id, period)
VALUES (
  :rental_id,
  :laptop_id,
  tstzrange(:start_at, :end_at + interval '90 minutes', '[)')
);
```
> **Đối chiếu ngành:** Odoo Rental gọi đúng khái niệm này là **"Security Time"** — *"the option to set a Security Time, expressed in hours, to make the rental product temporarily unavailable between two rental orders"*. **[SNIPPET — [Odoo 18 Rental docs](https://www.odoo.com/documentation/18.0/applications/sales/rental.html)]**

**(c) Ràng buộc partial (`WHERE`) để đơn huỷ không chiếm chỗ.**
**[SNIPPET]** Nguồn tìm được xác nhận: *"You can add a WHERE clause to make the constraint partial: `WHERE (status != 'cancelled')`, which allows cancelled reservations to not block new bookings."*
→ Cẩn thận: nếu dùng soft-delete thì `WHERE` phải bao gồm cả `deleted_at IS NULL`.

### 3.4. Xử lý lỗi ở tầng ứng dụng

Khi vi phạm, PostgreSQL ném lỗi **SQLSTATE `23P01` = `exclusion_violation`**. Ứng dụng phải bắt đúng mã này và trả về thông báo tiếng Việt thân thiện, ví dụ *"Máy này vừa có người khác đặt mất rồi, bạn chọn máy khác nhé"*.

> ⚠️ **CẦN NHÓM KIỂM CHỨNG:** mã lỗi `23P01` là kiến thức chuẩn của PostgreSQL nhưng tôi **không mở được** trang tài liệu chính thức (postgresql.org bị chặn trong môi trường này). Nhóm hãy tự chạy thử để xác nhận, hoặc tra "PostgreSQL Error Codes Appendix A".

Ví dụ Laravel (PHP):
```php
use Illuminate\Database\QueryException;

try {
    DB::transaction(function () use ($rental, $laptopId, $start, $end) {
        RentalHold::create([
            'rental_id' => $rental->id,
            'laptop_id' => $laptopId,
            'period'    => "[{$start},{$end})",
        ]);
    });
} catch (QueryException $e) {
    if ($e->getCode() === '23P01') {                 // exclusion_violation
        return back()->withErrors('Máy này vừa được người khác đặt. Vui lòng chọn máy khác.');
    }
    throw $e;
}
```

### 3.5. Ưu / nhược

| Ưu điểm | Nhược điểm |
|---|---|
| Đúng đắn 100%, không phụ thuộc code | Chỉ có trên PostgreSQL (MySQL không có) |
| Không cần lock thủ công → ít deadlock | Không giải được bài toán "bán quá tổng số máy trong pool" |
| Chống được cả khi sửa tay trong DB | Cần hiểu range type, hơi lạ với SV mới |
| Chỉ 1 dòng DDL | Thông báo lỗi thô, phải map sang tiếng Việt |
| Chỉ mục GiST cũng tăng tốc luôn truy vấn "máy nào rảnh ngày X" | Phải nhớ thêm `WHERE` cho trạng thái huỷ |

---

## 4. GIẢI PHÁP #2: PESSIMISTIC LOCK — `SELECT ... FOR UPDATE`

### 4.1. Nguyên lý & mẫu code

**[SNIPPET]** Khoá bi quan giành **khoá độc quyền trên dòng tài nguyên** ngay đầu giao dịch đặt chỗ; các request sau phải **chờ** cho tới khi khoá được nhả.

Mẫu chuẩn được nhiều nguồn nêu:
```sql
BEGIN;
  SELECT id FROM resources WHERE id = :resource_id FOR UPDATE;
  -- kiểm tra lại tình trạng còn trống NGAY TRONG transaction
  -- ghi booking nếu còn trống
COMMIT;
```
Nguồn: [Booking System with Pessimistic Locks (Javarevisited/Medium)](https://medium.com/javarevisited/booking-system-with-pessimistic-locks-4ec107e4bd5) · [When Millions Click at Once: How Pessimistic Locking Prevents Double Booking (Medium)](https://medium.com/@niketl16/when-millions-click-at-once-how-pessimistic-locking-prevents-double-booking-in-high-traffic-2e9d3b109b19) · [How to Build Pessimistic Locking Implementation (OneUptime, 30/01/2026)](https://oneuptime.com/blog/post/2026-01-30-pessimistic-locking-implementation/view) · [Handling the Double-Booking Problem in Databases (adamdjellouli.com)](https://adamdjellouli.com/articles/databases_notes/07_concurrency_control/04_double_booking_problem) · [How to Prevent Double Booking Under Concurrent Reservation Requests (clixo.sh)](https://clixo.sh/blog/prevent-double-booking-concurrent-reservation-requests)

**Khi nào nên dùng [SNIPPET]:** *"Pessimistic locking is the right call when conflicts are frequent and retries are expensive, such as for inventory systems, financial transactions, or booking platforms."*
**Nhược [SNIPPET]:** *"decreased throughput, increased deadlock risk, and reduced responsiveness."*
**Đối chiếu lưu lượng [SNIPPET]:** *"Low traffic scenarios favor pessimistic locks as simplest, while high traffic and micro-services scenarios benefit from optimistic retries which scale better."*

### 4.2. Áp dụng cho dự án

**[SUY LUẬN]** Với 15–40 máy và lưu lượng đỉnh chỉ vài chục request/phút vào mùa thi, **pessimistic lock là hoàn toàn đủ và đơn giản nhất để giải thích trong proposal**. Có thể dùng **kết hợp**: `FOR UPDATE` để tuần tự hoá logic nghiệp vụ, `EXCLUDE` làm lưới an toàn cuối cùng.

Mẫu Laravel:
```php
DB::transaction(function () use ($laptopId, $start, $end) {
    // khoá dòng máy — mọi request khác trên cùng máy phải xếp hàng
    $laptop = Laptop::where('id', $laptopId)->lockForUpdate()->firstOrFail();

    $conflict = RentalHold::where('laptop_id', $laptopId)
        ->where('hold_state', 'active')
        ->whereRaw("period && tstzrange(?, ?, '[)')", [$start, $end])
        ->exists();

    if ($conflict) {
        throw new \DomainException('Máy đã có người đặt trong khung giờ này.');
    }

    RentalHold::create([...]);   // EXCLUDE constraint vẫn là lưới an toàn cuối
});
```

### 4.3. Biến thể quan trọng: `FOR UPDATE SKIP LOCKED` — "lấy máy rảnh tiếp theo"

**[SUY LUẬN — kỹ thuật chuẩn, nhóm nên kiểm chứng thêm]** Khi cần **tự động chọn 1 máy bất kỳ còn rảnh** trong pool (late assignment) mà không để 2 request cùng chộp 1 máy:

```sql
BEGIN;
SELECT l.id
FROM laptops l
WHERE l.status = 'available'
  AND l.model_id = :model_id
  AND NOT EXISTS (
      SELECT 1 FROM rental_holds h
      WHERE h.laptop_id = l.id
        AND h.hold_state = 'active'
        AND h.period && tstzrange(:start_at, :end_at, '[)')
  )
ORDER BY l.id
FOR UPDATE OF l SKIP LOCKED     -- ★ bỏ qua máy đang bị request khác khoá
LIMIT 1;
-- rồi INSERT vào rental_holds với laptop_id vừa lấy
COMMIT;
```
`SKIP LOCKED` khiến request thứ hai **không phải chờ** mà nhảy sang máy kế tiếp → thông lượng tốt hơn hẳn `FOR UPDATE` thuần khi có nhiều máy giống nhau.

> ⚠️ **Chưa mở được trang tài liệu PostgreSQL để trích dẫn** (postgresql.org bị chặn). Nhóm tra: PostgreSQL docs → "SELECT" → "The Locking Clause" → `SKIP LOCKED`.

### 4.4. Biến thể: Advisory Lock (khoá theo khoá logic, không cần dòng dữ liệu)

**[SUY LUẬN]** Hữu ích khi phải khoá "cả pool của một model trong một ngày" (bài toán 2 ở mục 2):
```sql
-- khoá tự nhả khi COMMIT/ROLLBACK
SELECT pg_advisory_xact_lock( hashtext('pool:' || :model_id || ':' || :date) );
```
Ưu: không cần bảng đếm. Nhược: khoá là "quy ước" — mọi đường ghi phải cùng dùng nó, DB không ép buộc được.

---

## 5. GIẢI PHÁP #3: OPTIMISTIC LOCK VỚI CỘT `version`

**[SNIPPET]** Khoá lạc quan giả định va chạm hiếm. Thêm cột `version` kiểu integer; câu `UPDATE` chỉ thành công nếu `version` chưa đổi, và tăng `version` lên cho lần sau.

```sql
UPDATE inventory_counters
   SET available = available - 1,
       version   = version + 1
 WHERE model_id  = :model_id
   AND date      = :date
   AND version   = :version_da_doc   -- ★ nếu ai đó đã sửa, 0 dòng bị ảnh hưởng
   AND available > 0;
-- nếu affected_rows = 0 → đọc lại và thử lại (retry)
```

Nguồn: [Stop Double-Booking: Optimistic Locking in Laravel (dev.to)](https://dev.to/iprajapatiparesh/stop-double-booking-optimistic-locking-in-laravel-j5n) · [Optimistic Lock / Pessimistic Lock (dev.to)](https://dev.to/jacktt/optimistic-lock-pessimistic-lock-4h36) · [Hack 66. Use Optimistic Locking](https://flylib.com/books/en/2.196.1/hack_66_use_optimistic_locking.html)

**Cảnh báo rất quan trọng cho dự án có đặt cọc [SNIPPET]:**
> *"Optimistic locking cannot be used when waiting for payment since this will mean that several users may have time to pay for seats, but only the first of them will get it."*
> — tạm dịch: *"Không dùng được khoá lạc quan khi phải chờ thanh toán, vì như vậy nhiều người có thể kịp trả tiền nhưng chỉ người đầu tiên nhận được chỗ."*

**[SUY LUẬN]** → Với luồng "đặt máy → chuyển khoản cọc → xác nhận", **phải giữ chỗ (hold) TRƯỚC khi thanh toán**, có TTL hết hạn, chứ không phải "ai trả tiền trước được máy". Xem mục 11.4 (hold có TTL).

---

## 6. GIẢI PHÁP #4: REDIS DISTRIBUTED LOCK (và tại sao dự án này CHƯA cần)

**[SNIPPET]** Mẫu chuẩn: `SET lock_key <token> NX EX 10`
- `NX` = chỉ tạo nếu chưa tồn tại → bảo đảm loại trừ lẫn nhau
- `EX 10` = tự hết hạn sau 10 giây → tránh deadlock nếu tiến trình chết

Nguồn: [Building a Scalable Slot Booking System with Redis Distributed Locks (dev.to)](https://dev.to/abhivyaktii/building-a-scalable-slot-booking-system-with-redis-distributed-locks-4cf8) · [How to Implement Booking Lock System with Redis (OneUptime, 31/03/2026)](https://oneuptime.com/blog/post/2026-03-31-redis-booking-lock-system/view) · [How to Model Booking/Reservation Systems in Redis (OneUptime, 31/03/2026)](https://oneuptime.com/blog/post/2026-03-31-redis-how-to-model-bookingreservation-systems-in-redis/view) · [How to Implement Distributed Locks with Redis (Redlock) (OneUptime, 21/01/2026)](https://oneuptime.com/blog/post/2026-01-21-redis-distributed-locks/view) · [Redis Locks: Working, Failure Modes and Real-World Examples](https://engineeringatscale.substack.com/p/redis-distributed-locks-explained) · [Reserve inventory in real time with Redis using WATCH, MULTI, and audit streams (redis.io)](https://redis.io/tutorials/inventory-reservation-in-real-time-with-redis/) · [Avoiding Double Booking with Redis (Medium)](https://medium.com/@cgorale111/avoiding-double-booking-with-redis-aca66fefcce3)

**Chi tiết đáng học từ snippet:**
> *"A Redis booking lock system uses SET NX to atomically claim a resource in a single operation, **token-validated Lua scripts** to ensure only the lock holder can confirm or release, and **sorted resource-ID ordering to prevent multi-resource deadlocks**. Auto-expiring TTLs release abandoned holds without any cleanup job."*

Ba bài học áp dụng được ngay cả khi không dùng Redis **[SUY LUẬN]**:
1. **Token xác thực chủ khoá** — chỉ ai giữ khoá mới được nhả khoá (tránh nhả nhầm khoá của người khác).
2. **Sắp xếp ID tài nguyên trước khi khoá nhiều máy** — nếu đơn thuê 3 máy, luôn khoá theo thứ tự `laptop_id` tăng dần → **không bao giờ deadlock**. Áp dụng y hệt cho `SELECT FOR UPDATE` nhiều dòng.
3. **TTL tự hết hạn thay cho cron dọn dẹp.**

Khái niệm "reservation" trong Redis: **[SNIPPET]** *"Inventory reservation is a pattern that temporarily holds stock for a cart so no other order can claim the same units. The system moves units from an 'available' pool into a 'reserved' pool while the customer completes payment."*

### Kết luận cho dự án **[SUY LUẬN]**
❌ **KHÔNG khuyến nghị Redis lock cho MVP.** Lý do:
- Redis lock chỉ cần khi có **nhiều tiến trình/nhiều server** không chia sẻ transaction DB. Dự án 15–40 máy chạy 1 server → 1 database, `EXCLUDE` + `FOR UPDATE` đã đủ và **mạnh hơn** (Redis lock không có tính bền vững/ACID).
- Thêm Redis = thêm 1 thành phần phải cài, giám sát, tốn RAM VPS.
- ✅ **Nhưng NÊN nhắc trong proposal ở phần "Lộ trình mở rộng"**: nếu quy mô lên nhiều chi nhánh/nhiều instance, Redis lock (hoặc Redlock) là bước tiếp theo. Điều này cho thấy nhóm hiểu đường tiến hoá kiến trúc.

---

## 7. GIẢI PHÁP #5: SAGA PATTERN (và tại sao dự án này CHẮC CHẮN không cần)

**[SNIPPET]** Saga = chuỗi giao dịch phân tán; nếu một bước hỏng thì chạy **giao dịch bù trừ (compensating transaction)** để hoàn tác.

- Nguồn kinh điển: [microservices.io — Pattern: Saga](https://microservices.io/patterns/data/saga.html)
- [Saga Pattern in Microservices: A Mastery Guide (Temporal)](https://temporal.io/blog/mastering-saga-patterns-for-distributed-transactions-in-microservices)
- [Saga Pattern in Distributed Systems (Orkes)](https://orkes.io/blog/saga-pattern-in-distributed-systems)
- [Event-Driven Microservices for Booking Systems: Saga Patterns and Eventual Consistency in Travel Technology (dev.to)](https://dev.to/airtruffle/event-driven-microservices-for-booking-systems-saga-patterns-and-eventual-consistency-in-travel-5g9i)
- [How to Implement the Saga Pattern for Distributed Transactions (OneUptime, 20/02/2026)](https://oneuptime.com/blog/post/2026-02-20-microservices-saga-pattern/view)

Ví dụ kinh điển đúng ngành du lịch **[SNIPPET]**: *"If the car rental service is down, the system will execute compensating transactions to cancel the hotel room and flight booking."*

Hai kiểu **[SNIPPET]**: **Choreography** (phi tập trung, mỗi service nghe event) vs **Orchestration** (có một bộ điều phối trung tâm).

Nguyên tắc bắt buộc **[SNIPPET]**: *"Every step in a saga must be idempotent—executing it multiple times must produce the same result as executing it once."*

### Kết luận cho dự án **[SUY LUẬN]**
❌ **KHÔNG dùng Saga.** Saga sinh ra để giải bài toán *"không có transaction chung giữa nhiều database"*. Dự án này **chỉ có 1 database PostgreSQL** → một `BEGIN ... COMMIT` là đủ, đúng hơn và đơn giản hơn Saga rất nhiều.

✅ **Nhưng có MỘT chỗ dự án chạm vào tinh thần Saga**: khi tích hợp **cổng thanh toán bên ngoài (VNPay/MoMo/ZaloPay)** — cổng thanh toán nằm ngoài transaction của mình. Ở đó cần:
- **Giao dịch bù trừ**: nếu đã trừ tiền nhưng máy đã bị người khác lấy → phải **hoàn tiền tự động**.
- **Idempotency** ở mọi bước (mục 12).
- Trạng thái trung gian `pending_payment` với TTL.

Đây là cách nói về Saga **đúng mức, không khoe kiến thức thừa** trong proposal. **[SUY LUẬN]**

---

## 8. BẢNG SO SÁNH TỔNG HỢP — CHỌN GÌ CHO DỰ ÁN

| Kỹ thuật | Chống trùng 1 máy | Chống bán quá pool | Độ khó cài | Cần thêm hạ tầng | Khuyến nghị cho dự án 15–40 máy |
|---|---|---|---|---|---|
| **PostgreSQL `EXCLUDE` + `tstzrange`** | ✅ Tuyệt đối | ❌ | Thấp (1 dòng DDL) | Không | ⭐⭐⭐ **DÙNG — lớp bảo vệ cuối cùng** |
| **`SELECT FOR UPDATE`** | ✅ (nếu code đúng) | ✅ (nếu khoá dòng đếm) | Thấp | Không | ⭐⭐⭐ **DÙNG — logic nghiệp vụ chính** |
| **`FOR UPDATE SKIP LOCKED`** | ✅ | ✅ | Trung bình | Không | ⭐⭐ Dùng nếu làm late assignment |
| **Advisory lock** | ✅ | ✅ | Trung bình | Không | ⭐ Chỉ khi cần khoá pool |
| **Optimistic lock (`version`)** | ⚠️ Cần retry | ✅ | Trung bình | Không | ⭐ Không hợp với luồng chờ thanh toán |
| **Redis lock / Redlock** | ✅ | ✅ | Cao | **Có (Redis)** | ❌ Để phần "mở rộng tương lai" |
| **Saga** | — | — | Rất cao | **Có (queue/orchestrator)** | ❌ Chỉ nhắc khi nói về cổng thanh toán |
| **`SERIALIZABLE` isolation** | ✅ | ✅ | Thấp | Không | ⚠️ Đơn giản nhưng nhiều lỗi serialization phải retry |

**Kiến trúc phòng thủ 3 lớp khuyến nghị [SUY LUẬN]:**
```
Lớp 1 (UX)   : Giao diện chỉ hiển thị khung giờ còn trống  → giảm 95% va chạm
Lớp 2 (Logic): Transaction + SELECT ... FOR UPDATE          → tuần tự hoá, thông báo lỗi đẹp
Lớp 3 (DB)   : EXCLUDE USING gist                           → không bao giờ sai, kể cả có bug
```
Đây là một sơ đồ **rất "ăn điểm"** khi trình bày proposal: cho thấy tư duy defense-in-depth.

---

# PHẦN B — MÔ HÌNH DỮ LIỆU INVENTORY: ĐẶT THEO LOẠI vs GÁN MÁY CỤ THỂ

## 9. HAI TẦNG "LOẠI" VÀ "CÁ THỂ" — CHUẨN CHUNG CỦA CẢ NGÀNH

### 9.1. Bằng chứng từ mã nguồn thật: KOHA (thư viện mã nguồn mở, dùng ở hàng nghìn thư viện)

**[MÃ NGUỒN]** Đây là phát hiện giá trị nhất của nghiên cứu này. Tôi đã tải file schema thật:
`https://raw.githubusercontent.com/Koha-Community/Koha/master/installer/data/mysql/kohastructure.sql` (413.576 bytes, tải ngày 14/09/2026).

Koha có **bảng `bookings`** — đặt trước một tài liệu trong một khoảng thời gian — **chính xác là bài toán của dự án này**:

```sql
CREATE TABLE `bookings` (
  `booking_id`         int(11) NOT NULL AUTO_INCREMENT COMMENT 'primary key',
  `patron_id`          int(11) NOT NULL DEFAULT 0 COMMENT '... which patron this booking is for',
  `biblio_id`          int(11) NOT NULL DEFAULT 0 COMMENT '... which bib record this booking is on',
  `item_id`            int(11) DEFAULT NULL        COMMENT '... the specific item the patron has placed a booking for',
  `pickup_library_id`  varchar(10) NOT NULL COMMENT 'Identifier for booking pickup library',
  `start_date`         datetime DEFAULT NULL COMMENT 'the start date of the booking',
  `end_date`           datetime DEFAULT NULL COMMENT 'the end date of the booking',
  `creation_date`      timestamp NOT NULL DEFAULT current_timestamp(),
  `modification_date`  timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `status`             enum('new','cancelled','issued','completed') NOT NULL DEFAULT 'new'
                       COMMENT 'current status of the booking',
  `cancellation_reason` varchar(80) DEFAULT NULL COMMENT 'optional authorised value BOOKING_CANCELLATION',
  PRIMARY KEY (`booking_id`),
  ...
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

**Đọc ra được 4 bài học quan trọng [MÃ NGUỒN + SUY LUẬN]:**

| Quan sát trong schema Koha | Bài học cho dự án thuê laptop |
|---|---|
| `biblio_id int NOT NULL` (đầu sách = **LOẠI**) | Đơn thuê **luôn** phải chỉ rõ **loại máy** (vd "Laptop Windows i5/8GB") |
| `item_id int **DEFAULT NULL**` (bản sách cụ thể = **CÁ THỂ**) | Máy cụ thể (serial) **được phép để trống lúc đặt** → đây chính là **late assignment** ở dạng chuẩn nhất |
| `status enum('new','cancelled','issued','completed')` | **Chỉ 4 trạng thái**. Hệ thống hàng chục nghìn người dùng vẫn chỉ cần 4. Đừng thiết kế 15 trạng thái. |
| `start_date` / `end_date` là 2 cột `datetime` riêng | Koha chạy **MySQL** nên **không có range type và không có EXCLUDE** → **phải kiểm tra trùng lịch bằng code PHP**. Postgres cho phép làm tốt hơn. |

**[MÃ NGUỒN]** Bảng `items` của Koha còn có cột đáng chú ý:
```sql
`bookable` tinyint(1) DEFAULT NULL COMMENT 'nullable boolean value defining whether this this item is available for bookings or not',
`barcode`  varchar(20) DEFAULT NULL COMMENT 'item barcode (MARC21 952$p)',   -- UNIQUE KEY `itembarcodeidx`
`stocknumber` varchar(80) DEFAULT NULL COMMENT 'inventory number (MARC21 952$i)',
`onloan`   date DEFAULT NULL COMMENT 'defines if item is checked out (NULL for not checked out, and due date for checked out)',
`notforloan` tinyint(1) NOT NULL DEFAULT 0,
`damaged`  tinyint(1) NOT NULL DEFAULT 0,   `damaged_on` datetime DEFAULT NULL,
`itemlost` tinyint(1) NOT NULL DEFAULT 0,   `itemlost_on` datetime DEFAULT NULL,
`withdrawn` tinyint(1) NOT NULL DEFAULT 0,  `withdrawn_on` datetime DEFAULT NULL,
`datelastseen` datetime DEFAULT NULL COMMENT 'the date the item was last see (usually the last time the barcode was scanned...)',
`itype` varchar(10) DEFAULT NULL COMMENT 'foreign key from the itemtypes table defining the type for this item',
```
👉 **Bài học [SUY LUẬN]:** Koha **không** nhét mọi thứ vào một cột `status` duy nhất. Nó tách thành **các cờ độc lập** (`damaged`, `itemlost`, `withdrawn`, `notforloan`) **kèm mốc thời gian tương ứng** (`damaged_on`, `itemlost_on`, `withdrawn_on`). Dự án nên bắt chước: một máy có thể **vừa hỏng vừa đang được sửa** — hai chiều thông tin khác nhau.
👉 Cột `datelastseen` = "lần cuối quét mã vạch thấy máy" → chính là **kiểm kê (audit)**. Snipe-IT cũng có `last_audit_date` / `next_audit_date`.

### 9.2. Bằng chứng khác từ Koha: `reserves` — mẫu "giữ chỗ theo LOẠI, gán CÁ THỂ khi thực hiện"

**[MÃ NGUỒN]** Bảng `reserves` (đặt giữ sách) có hai cột nói lên toàn bộ triết lý late assignment:

```sql
`item_level_hold` tinyint(1) NOT NULL DEFAULT 0
     COMMENT 'Is the hold placed at item level',
`itemnumber` int(11) DEFAULT NULL
     COMMENT 'foreign key from the items table defining the specific item the patron has placed
              on hold OR THE ITEM THIS HOLD WAS FILLED WITH',
`itemtype`  varchar(10) DEFAULT NULL
     COMMENT 'If record level hold, the optional itemtype of the item the patron is requesting',
`priority`  smallint(6) NOT NULL DEFAULT 1 COMMENT 'where in the queue the patron sits',
`expirationdate` date DEFAULT NULL COMMENT 'the date the hold expires (calculated value)',
`found` varchar(1) DEFAULT NULL COMMENT 'a one letter code defining what the status is of the hold is after it has been confirmed',
`waitingdate` date DEFAULT NULL COMMENT 'the date the item was marked as waiting for the patron at the library',
```

👉 **Điểm tinh tế nhất [MÃ NGUỒN]:** comment của Koha ghi rõ `itemnumber` mang **hai nghĩa tuỳ ngữ cảnh**: (a) cá thể khách chỉ đích danh muốn, HOẶC (b) **"the item this hold was filled with"** = cá thể mà hệ thống **gán muộn** khi thực hiện đơn. Cột `item_level_hold` chính là cờ phân biệt hai chế độ.
👉 **Áp dụng trực tiếp [SUY LUẬN]:** dự án nên có cột `assignment_mode` = `'by_model'` | `'specific_unit'` và cột `laptop_id` nullable, đúng mẫu Koha.

### 9.3. Bằng chứng thứ ba: `issues` — "một máy chỉ được cho mượn cho MỘT người tại một thời điểm"

**[MÃ NGUỒN]** Bảng `issues` (đang cho mượn) của Koha:
```sql
CREATE TABLE `issues` (
  `issue_id`       int(11) NOT NULL AUTO_INCREMENT,
  `borrowernumber` int(11) NOT NULL,
  `issuer_id`      int(11) DEFAULT NULL COMMENT '... the user who checked out this item',
  `itemnumber`     int(11) NOT NULL,
  `booking_id`     int(11) DEFAULT NULL COMMENT 'foreign key linking this checkout to the booking it fulfills',
  `date_due`       datetime DEFAULT NULL,
  `issuedate`      datetime DEFAULT NULL,
  `returndate`     datetime DEFAULT NULL COMMENT 'date the item was returned, will be NULL until moved to old_issues',
  `renewals_count` tinyint(4) NOT NULL DEFAULT 0,
  ...
  UNIQUE KEY `itemnumber` (`itemnumber`),      -- ★★★ CHỈ 1 LƯỢT MƯỢN ĐANG HOẠT ĐỘNG / 1 CÁ THỂ
  CONSTRAINT `issues_booking_id_fk` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`booking_id`)
      ON DELETE SET NULL ON UPDATE CASCADE,
  ...
);
```

👉 **Ba bài học vàng [MÃ NGUỒN + SUY LUẬN]:**
1. **`UNIQUE KEY itemnumber`** — Koha ép ở cấp DB: một cá thể **không thể** đang được mượn bởi 2 người. Dự án nên có ràng buộc y hệt trên bảng "đang giao máy":
   `CREATE UNIQUE INDEX ON active_checkouts (laptop_id);`
2. **`booking_id` FK trên `issues`** — booking (đặt trước) và checkout (giao máy thật) là **hai bảng khác nhau**, nối với nhau bằng khoá ngoại. **Đừng gộp làm một.** Đặt trước có thể bị huỷ; giao máy là sự kiện vật lý đã xảy ra.
3. **`returndate ... will be NULL until moved to old_issues`** — Koha **chuyển bản ghi sang bảng lịch sử `old_issues`** khi trả. Đây là kỹ thuật giữ bảng "đang hoạt động" luôn nhỏ và nhanh. Với 15–40 máy thì chưa cần, nhưng nên biết.

---

### 9.4. Ngành khách sạn: "bán theo hạng phòng, gán phòng lúc check-in"

**[SNIPPET]** — Nguồn: [When it Comes to Room Assignments, Details Matter — Pierre Boettner, HospitalityNet](https://www.hospitalitynet.org/opinion/4074675.html) (và bản mirror [Hotel Online](https://www.hotel-online.com/news/when-it-comes-to-room-assignments-details-matter))

> *"Reservation agents shifted from selling individual rooms to selling room categories, which resulted in occupancies climbing upwards of 80 percent or higher."*
> — tạm dịch: *"Nhân viên đặt phòng chuyển từ bán từng phòng cụ thể sang bán theo hạng phòng, kết quả là công suất phòng leo lên trên 80%."*

**Đây là con số then chốt để biện luận trong proposal**: bán theo LOẠI thay vì theo CÁ THỂ **làm tăng công suất khai thác**.
> ⚠️ **[SNIPPET — chưa mở được trang gốc]** Con số "trên 80%" và bối cảnh của nó (thời điểm nào, mẫu khảo sát nào) **nhóm bắt buộc phải tự mở link kiểm chứng** trước khi đưa vào proposal.

**Mặt trái cũng được nêu trong cùng nguồn [SNIPPET]:**
> *"if the hotelier assigns a guest a room type prematurely, and later a rush of guests depletes inventory of a specific bed type, subsequent requesters must be turned away when at least one more room could have been sold while still satisfying all guests' requests."*
> — tạm dịch: gán quá sớm/quá cứng làm **mất doanh thu** vì phải từ chối khách trong khi thực ra vẫn còn phòng phù hợp.

Nguồn thiết kế CSDL: [Hotel Reservation System — ByteByteGo](https://bytebytego.com/courses/system-design-interview/hotel-reservation-system) nêu bảng **`room_type_inventory`** dùng để kiểm tra khách có đặt được một **hạng phòng** hay không. **[SNIPPET]**
Nguồn so sánh schema: [Hotel Booking: Schema Design Comparison (dev.to)](https://dev.to/sumedhbala/hotel-booking-schema-design-comparison-g3h) — snippet nêu một **thiết kế lai**: *"combine Schema 1 inventory with GiST room assignments to avoid room switching after check-in, though this creates more complex queries and requires deciding which available room to assign"*. **[SNIPPET]** Chính là mô hình lai mà tôi khuyến nghị bên dưới.

### 9.5. Ngành cho thuê xe

**[SNIPPET]** — Nguồn: [Car Rental Reservation System: Modules, Providers, and Implementation (AltexSoft)](https://www.altexsoft.com/blog/car-rental-reservation-system/) · [Vehicle reservation system guide for car rental businesses (Nomora)](https://www.nomora.io/blog/vehicle-reservation-system-guide-car-rental-businesses) · [Rental-Car-Company-SQL (GitHub)](https://github.com/ggeop/Rental-Car-Company-SQL) · [car-rental-database-sql (GitHub)](https://github.com/evagian/car-rental-database-sql-) · [US8160906B2 — System and method for improved rental vehicle reservation management (Google Patents)](https://patents.google.com/patent/US8160906)

Các ý rút được từ snippet:
- Xe được định danh bằng **VIN**, kèm mô tả/màu/hãng/model/ngày mua; mỗi xe thuộc **một hạng xe** (compact, economy, convertible) → **đúng mô hình 2 tầng LOẠI/CÁ THỂ**.
- Trong một số thiết kế, `Reservation_ID` mang các thuộc tính `Start_Date`, `End_Date`, **`VIN`** → đặt gắn thẳng vào xe cụ thể.
- Nhưng cũng có cơ chế linh hoạt: *"In case of any car problems, the system can automatically assign another available vehicle for the approved reservation"* — **tự động đổi xe khác** khi xe gặp sự cố, mà **giữ nguyên đơn đặt**.
- Tính năng vận hành: *"measure vehicle usage and distribute the load equally throughout the fleet"* — **phân bổ đều tải sử dụng trên toàn đội xe**.

👉 **Áp dụng cực kỳ trực tiếp cho dự án [SUY LUẬN]:**
1. Phải có nghiệp vụ **"đổi máy cho đơn đã xác nhận"** (máy chuẩn bị giao bị hỏng đột xuất). Đây là tính năng **sống còn** vì đúng ngày thi mà máy hỏng thì mất khách vĩnh viễn.
2. Nên có thuật toán **cân bằng số giờ sử dụng giữa các máy** (đừng luôn gán máy `id` nhỏ nhất). Gợi ý: `ORDER BY total_rented_hours ASC` khi chọn máy. Vừa kéo dài tuổi thọ pin đồng đều, vừa là một điểm "kỹ thuật có chiều sâu" trong proposal.

### 9.6. LibreBooking: cột `autoassign` — bằng chứng mã nguồn cho "gán tự động"

**[MÃ NGUỒN]** Trong `resources` của LibreBooking (tải từ `https://raw.githubusercontent.com/LibreBooking/app/master/database_schema/create-schema.sql`):
```sql
`autoassign`                  tinyint(1) unsigned NOT NULL default '1',
`requires_approval`           tinyint(1) unsigned NOT NULL,
`min_duration` int, `min_increment` int, `max_duration` int,
`min_notice_time` int, `max_notice_time` int,
`allow_multiday_reservations` tinyint(1) unsigned NOT NULL default '1',
`unit_cost`                   dec(7,2),
```
👉 Bộ cột này là **checklist tính năng miễn phí** cho dự án **[SUY LUẬN]**:

| Cột LibreBooking | Nghĩa | Dùng cho thuê laptop thi |
|---|---|---|
| `autoassign` | tự gán tài nguyên | Bật/tắt chế độ hệ thống tự chọn máy |
| `requires_approval` | cần duyệt tay | Đơn > 3 ngày hoặc khách mới → cần admin duyệt |
| `min_duration` / `max_duration` | thời lượng tối thiểu/tối đa | Tối thiểu 1 buổi (4h), tối đa 7 ngày |
| `min_increment` | bước thời gian | Đặt theo bước 30 phút hoặc theo ca thi |
| **`min_notice_time`** | báo trước tối thiểu | **Rất quan trọng**: không cho đặt trước < 2h vì nhân viên cần thời gian chuẩn bị máy |
| `max_notice_time` | đặt xa nhất | Không cho đặt trước quá 60 ngày |
| `unit_cost` | đơn giá | Giá thuê theo đơn vị thời gian (VNĐ) |

---

## 10. QUYẾT ĐỊNH KIẾN TRÚC: MÔ HÌNH LAI "ĐẶT THEO LOẠI — GIỮ CHỖ MỘT MÁY THẬT"

**[SUY LUẬN — đây là khuyến nghị của tôi, nhóm cân nhắc và có thể phản biện]**

### 10.1. Ba lựa chọn và đánh đổi

| | **(A) Gán serial ngay khi đặt** | **(B) Đặt theo loại, gán lúc giao máy** | **(C) LAI (khuyến nghị)** |
|---|---|---|---|
| Cách làm | Khách chọn đúng máy #LT-007 | Chỉ ghi `model_id`, đếm số lượng | Ghi `model_id` + hệ thống **âm thầm giữ 1 máy thật**, có quyền **hoán đổi** trước giờ giao |
| Chống double-booking | `EXCLUDE` giải triệt để | Phải đếm → cần lock/counter | `EXCLUDE` giải triệt để |
| Công suất lấp đầy kho | Thấp hơn (phân mảnh lịch) | Cao nhất | Cao (vì được hoán đổi để dồn lịch) |
| Độ phức tạp code | Thấp nhất | Cao nhất | **Trung bình** |
| Máy hỏng đột xuất | Phải đổi tay | Trong suốt với khách | Đổi bằng 1 lệnh `UPDATE laptop_id` |
| Khách muốn "đúng máy đó" | ✅ | ❌ | ✅ (cột `pinned_unit = true`) |
| Rủi ro với 15–40 máy | Chấp nhận được | Thừa phức tạp | Cân bằng tốt nhất |

### 10.2. Mô hình LAI hoạt động thế nào

1. Khách chọn **loại máy** + khung thời gian trên web.
2. Hệ thống chạy `SELECT ... FOR UPDATE SKIP LOCKED` chọn **một máy thật** còn rảnh trong loại đó (ưu tiên máy có **tổng giờ thuê thấp nhất** để cân bằng hao mòn).
3. Ghi 1 dòng `rental_holds(rental_id, laptop_id, period)` → `EXCLUDE` bảo đảm không trùng.
4. **Khách KHÔNG nhìn thấy serial** ở bước đặt — chỉ thấy "Laptop Windows i5/8GB — đã giữ chỗ". Nhờ vậy admin **tự do hoán đổi** máy bất cứ lúc nào trước giờ giao (chỉ cần `UPDATE rental_holds SET laptop_id = ...`), `EXCLUDE` tự kiểm tra hộ.
5. Khi giao máy: tạo bản ghi `checkouts` với `laptop_id` **cuối cùng** đã chốt + ảnh tình trạng máy + chữ ký.

### 10.3. Vì sao mô hình lai đặc biệt hợp với BỐI CẢNH THI CỬ **[SUY LUẬN]**

- **Rủi ro không được phép xảy ra:** khách đến nhận máy lúc 7h sáng ngày thi mà máy hỏng. Mô hình lai cho phép **đổi máy trong 5 giây** mà không phải huỷ/tạo lại đơn, không phải báo khách.
- **Yêu cầu Windows là bắt buộc** → mọi máy trong kho đều Windows, nên khả năng thay thế giữa các máy rất cao → mô hình pooling phát huy tối đa.
- **Nhu cầu dồn cực mạnh vào mùa thi** (nhiều SV thi cùng ca) → cần công suất lấp đầy cao → không nên gán cứng.
- Vẫn giữ được `pinned_unit` cho khách VIP/khách quen muốn đúng máy đã dùng lần trước (đã quen bàn phím, đã cài sẵn).

---

# PHẦN C — STATE MACHINE CHO VÒNG ĐỜI ĐƠN THUÊ

## 11. MÁY TRẠNG THÁI (FINITE STATE MACHINE)

### 11.1. Tại sao KHÔNG dùng cột `status` kiểu chuỗi tự do

**[SUY LUẬN]** Nếu chỉ có `status varchar(20)`, code sẽ đầy `if ($order->status == 'paid' && ...)` rải rác khắp nơi, và sớm muộn sẽ có bug kiểu: đơn **đã trả máy** vẫn bị chuyển sang **đã huỷ**, hoặc đơn **chưa cọc** vẫn được giao máy. Máy trạng thái làm cho **các chuyển trạng thái hợp lệ trở thành dữ liệu tường minh**, kiểm thử được.

Đối chiếu thực tế **[MÃ NGUỒN]**: Koha dùng `enum('new','cancelled','issued','completed')` cho `bookings.status` — enum ở cấp DB, không phải varchar tự do.

### 11.2. Vòng đời đơn thuê đề xuất cho dự án **[SUY LUẬN]**

```
                     ┌──────────────────────────────────────────┐
                     ▼                                          │
  [draft] ──submit──> [pending_payment] ──payment_ok──> [confirmed] ──handover──> [active]
     │                     │                                │                        │
     │                     │ timeout (TTL 30–60')           │ cancel                 │ return
     │                     ▼                                ▼                        ▼
     └──abandon──────> [expired]                       [cancelled]              [returned]
                                                                                     │
                                                                        inspection   │
                                                                    ┌────────────────┴────────────────┐
                                                                    ▼                                 ▼
                                                              [completed]                        [disputed]
                                                                                                      │
                                                                                                  resolve
                                                                                                      ▼
                                                                                                [completed]

  Nhánh bất thường từ [active]:
     [active] ──quá hạn chưa trả──> [overdue] ──return──> [returned]
     [active] ──báo mất/hỏng nặng──> [incident] ──đền bù xong──> [completed]
```

### 11.3. Bảng chuyển trạng thái (dùng làm phụ lục proposal)

| Từ | Sự kiện | Đến | Điều kiện bảo vệ (guard) | Hiệu ứng phụ (side effect) |
|---|---|---|---|---|
| `draft` | `submit` | `pending_payment` | Còn máy trống trong khung giờ | **Tạo `rental_holds` (giữ chỗ)**, đặt `hold_expires_at = now() + 45 phút` |
| `pending_payment` | `payment_succeeded` | `confirmed` | Webhook cổng TT hợp lệ, số tiền khớp | Gửi email/Zalo xác nhận, xoá `hold_expires_at` |
| `pending_payment` | `timeout` | `expired` | `now() > hold_expires_at` | **Huỷ hold → trả máy về kho** (`hold_state='cancelled'`) |
| `pending_payment` | `cancel` | `cancelled` | Khách tự huỷ | Huỷ hold |
| `confirmed` | `swap_unit` | `confirmed` | Máy mới rảnh cùng khung giờ | `UPDATE rental_holds SET laptop_id=...` (EXCLUDE tự kiểm) |
| `confirmed` | `handover` | `active` | Đã ký biên bản + đã thu cọc + đã chụp ảnh máy | Tạo `checkouts`, `laptops.status='rented'`, ghi `action_logs` |
| `confirmed` | `cancel` | `cancelled` | Theo chính sách hoàn cọc | Huỷ hold, hoàn tiền (có thể trừ phí) |
| `active` | `return` | `returned` | Máy đã về tay nhân viên | Ghi giờ trả thực tế, chụp ảnh tình trạng |
| `active` | `due_passed` | `overdue` | `now() > period.upper` | Bắt đầu tính phí trễ, gửi nhắc |
| `active` | `report_incident` | `incident` | NV/khách báo mất/hỏng nặng | Khoá máy khỏi kho (`laptops.status='lost'`/`'maintenance'`) |
| `returned` | `inspect_ok` | `completed` | Kiểm tra không phát sinh | Hoàn cọc, `laptops.status='available'` |
| `returned` | `inspect_issue` | `disputed` | Có hư hỏng/thiếu phụ kiện | Giữ cọc, mở hồ sơ tranh chấp (kèm ảnh trước/sau) |
| `disputed` | `resolve` | `completed` | Hai bên thống nhất | Hoàn phần cọc còn lại |

> **Nguyên tắc [SUY LUẬN]:** trạng thái `expired` và `cancelled` là **hai thứ khác nhau** (một do hệ thống, một do người) — quan trọng khi làm báo cáo tỉ lệ rơi rớt (drop-off) để tối ưu chuyển đổi. Đừng gộp.

### 11.4. Cơ chế "hold có TTL" — chi tiết triển khai

**[SUY LUẬN — lấy cảm hứng từ mẫu Redis inventory reservation, mục 6]**

Vấn đề: giữa lúc khách bấm "Đặt" và lúc tiền về tài khoản (chuyển khoản QR có thể mất vài phút), **phải giữ máy cho khách** nhưng **không được giữ mãi**.

```sql
ALTER TABLE rental_holds ADD COLUMN expires_at timestamptz;
CREATE INDEX ON rental_holds (expires_at) WHERE hold_state = 'active';
```
Job dọn dẹp chạy mỗi phút:
```sql
UPDATE rental_holds
   SET hold_state = 'cancelled'
 WHERE hold_state = 'active'
   AND expires_at IS NOT NULL
   AND expires_at < now();
```
Vì `EXCLUDE` có `WHERE (hold_state <> 'cancelled')`, chỉ cần đổi cờ là máy **tự động** rảnh lại. **Không cần xoá dòng** → giữ được lịch sử.

> **Con số đề xuất [SUY LUẬN — nhóm tự chọn theo thực tế]:** TTL **45 phút** cho chuyển khoản thủ công; **15 phút** nếu tích hợp cổng thanh toán tự động. Cần cân bằng: TTL dài quá thì khoá kho vô ích trong mùa cao điểm; ngắn quá thì khách chuyển khoản chậm bị mất chỗ.

### 11.5. Thư viện state machine theo ngôn ngữ — PHIÊN BẢN THẬT (kiểm tra ngày 14/09/2026)

**[REGISTRY]** Số liệu dưới đây lấy trực tiếp từ registry gói, **không phải snippet**:

| Ngôn ngữ | Thư viện | Phiên bản mới nhất | Ngày phát hành | Giấy phép | Ghi chú |
|---|---|---|---|---|---|
| TypeScript/JS | **`xstate`** | **5.33.0** | 2026-09-12 | MIT | Mạnh nhất: statechart phân cấp, song song, actor model. Có công cụ vẽ trực quan Stately. |
| TypeScript/JS | **`robot3`** | **1.2.0** | 2025-09-20 | BSD-2-Clause | Rất nhẹ (~1KB), FSM phẳng. Đủ cho vòng đời đơn thuê. |
| PHP / Laravel | **`spatie/laravel-model-states`** | **2.14.2** | 2026-07-22 | MIT | Gắn state machine trực tiếp vào Eloquent Model. **Phù hợp nhất nếu chọn Laravel.** |
| Go | **`github.com/looplab/fsm`** | **v1.0.4** | 2026-08-27 | (xem repo) | FSM phổ biến nhất của Go. |
| Python | **`transitions`** (pytransitions) | **0.9.3** | (xem PyPI) | MIT | Chuẩn de-facto của Python; có vẽ đồ thị bằng graphviz. |

Nguồn tham khảo XState **[SNIPPET]**: [Tài liệu XState (Stately)](https://stately.ai/docs/xstate) · [Trang "State machines" (Stately)](https://stately.ai/docs/machines) · [GitHub statelyai/xstate](https://github.com/statelyai/xstate)
Snippet ghi: *"XState v5 requires TypeScript version 5.0 or greater"* và *"The best way to provide strong typing for your machine is to use the setup(...) function and/or the .types property."*
Snippet so sánh: *"robot3 (~1KB minified) gives you a finite-state-machine API with batteries but will not give you XState's hierarchical states; for flat machines like the order lifecycle, robot3's API is the one to reach for if you would rather not maintain the engine yourself."*

### 11.6. Khuyến nghị **[SUY LUẬN]**

- **Nếu chọn Laravel** → dùng `spatie/laravel-model-states` (2.14.2). Mỗi trạng thái là 1 class PHP, chuyển trạng thái không hợp lệ **ném exception**. Rất dễ demo trong proposal.
- **Nếu chọn Next.js/Node** → **KHÔNG cần XState cho backend**. XState mạnh nhưng học phí cao và hợp với UI phức tạp hơn là vòng đời đơn hàng. Với 12 trạng thái phẳng, một **bảng chuyển trạng thái trong DB** là đủ và dễ bảo vệ trước hội đồng hơn:
```sql
CREATE TABLE rental_state_transitions (
    from_state  text NOT NULL,
    event       text NOT NULL,
    to_state    text NOT NULL,
    PRIMARY KEY (from_state, event)
);
-- và ràng buộc trên bảng rentals:
ALTER TABLE rentals ADD CONSTRAINT rentals_state_valid
  CHECK (state IN ('draft','pending_payment','confirmed','active','overdue',
                   'returned','completed','cancelled','expired','incident','disputed'));
```
- **Bắt buộc:** mọi lần chuyển trạng thái phải ghi 1 dòng vào bảng lịch sử `rental_state_log(rental_id, from_state, to_state, event, actor_id, reason, created_at)`. Đây vừa là audit, vừa là dữ liệu để tính KPI (thời gian trung bình từ đặt tới nhận máy).

---

# PHẦN D — IDEMPOTENCY, WEBHOOK, OUTBOX

## 12. XỬ LÝ THANH TOÁN AN TOÀN

### 12.1. Idempotency Key — chuẩn Stripe

**[SNIPPET]** — Nguồn gốc: [Designing robust and predictable APIs with idempotency — Stripe Blog](https://stripe.com/blog/idempotency) · [Implementing Stripe-like Idempotency Keys in Postgres — brandur.org](https://brandur.org/idempotency-keys) (bài này là tài liệu tham khảo kinh điển, **nhóm nên đọc kỹ**) · [Working with the new Idempotency Keys RFC (HTTP Toolkit)](https://httptoolkit.com/blog/idempotency-keys/) · [How Stripe Prevents Double Payment Using Idempotent API](https://newsletter.systemdesign.one/p/idempotent-api) · [Designing Idempotent Payment APIs (Arpit Bhayani)](https://arpit.substack.com/p/designing-idempotent-payment-apis) · [Idempotency in Payment APIs: Prevent Double Charges with Stripe, Omise, and 2C2P (Simplico, 04/04/2026)](https://simplico.net/2026/04/04/idempotency-in-payment-apis-prevent-double-charges-with-stripe-omise-and-2c2p/)

Cơ chế **[SNIPPET]**:
> *"The Stripe API implements idempotency keys on mutating endpoints (i.e. anything under POST) by allowing clients to pass a unique value in with the special `Idempotency-Key` header. The client makes up a token, usually a UUID... First time the server sees the key, it does the work and stores the result against that key. Every subsequent request carrying the same key gets the stored result handed back, untouched, no matter how many times it shows up."*

**Số liệu đáng chú ý từ snippet (CẦN KIỂM CHỨNG):**
| Số liệu | Giá trị | Nguồn snippet |
|---|---|---|
| Thời gian Stripe giữ idempotency key | **24 giờ** | *"Stripe removes the idempotency keys from the in-memory database after 24 hours."* |
| Chi phí overhead của bảng khử trùng lặp | **< 2 ms/request** (1 lần tra chỉ mục) | *"The deduplication table pattern adds less than 2ms overhead per request (a single indexed lookup)"* |

> ⚠️ Cả hai con số này **chỉ đọc được từ snippet, chưa mở được trang gốc**. Nhóm phải tự mở [stripe.com/blog/idempotency](https://stripe.com/blog/idempotency) và [brandur.org/idempotency-keys](https://brandur.org/idempotency-keys) để xác minh trước khi trích.

**Khuyến nghị dùng bảng riêng [SNIPPET]:** *"It is recommended to use a separate database or table to store idempotency keys to ensure that the server can quickly validate the processing status and load isolation."*

### 12.2. Schema idempotency đề xuất **[SUY LUẬN — dựa trên mẫu Stripe/brandur]**

```sql
CREATE TABLE idempotency_keys (
    id              bigserial PRIMARY KEY,
    key             text        NOT NULL,          -- UUID do client sinh
    user_id         bigint      NOT NULL,
    request_path    text        NOT NULL,          -- vd 'POST /api/rentals'
    request_hash    text        NOT NULL,          -- SHA-256 của body, chống dùng lại key với body khác
    state           text        NOT NULL DEFAULT 'in_progress',  -- in_progress | succeeded | failed
    response_code   int,
    response_body   jsonb,
    locked_at       timestamptz,
    created_at      timestamptz NOT NULL DEFAULT now(),
    expires_at      timestamptz NOT NULL DEFAULT now() + interval '24 hours',
    UNIQUE (user_id, key)                          -- ★ ràng buộc chống chạy 2 lần
);
CREATE INDEX ON idempotency_keys (expires_at);
```

Luồng xử lý:
1. Client gửi `Idempotency-Key: <uuid>` trên mọi `POST` tạo đơn / tạo thanh toán.
2. Server `INSERT ... ON CONFLICT (user_id, key) DO NOTHING`.
   - Nếu **chèn được** → là lần đầu → xử lý bình thường, xong thì lưu `response_body`, `state='succeeded'`.
   - Nếu **không chèn được** → đã có → nếu `state='succeeded'` thì **trả lại y nguyên `response_body` cũ**; nếu `state='in_progress'` thì trả HTTP **409 Conflict** ("đang xử lý, đừng bấm nữa").
3. So sánh `request_hash`: nếu cùng key nhưng body khác → trả **422** (client dùng sai).

**Vì sao dự án này BẮT BUỘC phải có [SUY LUẬN]:** SV bấm nút "Đặt máy" trên điện thoại, mạng 4G trong khuôn viên trường chập chờn → bấm lại 2–3 lần → nếu không có idempotency thì tạo 2–3 đơn, giữ 2–3 máy, thu 2–3 lần cọc. Đây là lỗi **rất dễ xảy ra thật** và **rất dễ demo** khi bảo vệ đồ án.

### 12.3. Webhook từ cổng thanh toán — nhận và xử lý an toàn

**[SNIPPET]** — Nguồn: [Outbound webhook delivery at scale: signing payloads, retry budgets, and dead-letter operations (Matheus Palma)](https://matheuspalma.com/blog/outbound-webhook-delivery-signing-retries-dead-letters) · [Webhook System Design (Educative)](https://www.educative.io/blog/webhook-system-design)

Quy tắc rút ra được **[SNIPPET]**:

| Vấn đề | Cách xử lý theo nguồn |
|---|---|
| Lịch retry | *"use exponential backoff and a hard cap—for example: 1 minute, 2 minutes, 4 minutes, 8 minutes, then stop (or keep going with a maximum delay like 15 minutes)"* |
| Backoff có jitter | *"delay = random(0, min(cap, base * 2^attempt))"*, ví dụ `base=60s`, `cap=24h` → trải khoảng **2 ngày** |
| Mã lỗi **NÊN** retry | timeout mạng, connection reset, lỗi DNS, HTTP **429**, HTTP **5xx** |
| Mã lỗi **KHÔNG** retry | HTTP **400** (bad request), **401/403** (auth), **404** (sai endpoint), lỗi validation |
| Nhiều worker cùng chạy | *"Use `FOR UPDATE SKIP LOCKED` when claiming pending deliveries so multiple workers scale horizontally without double-sending the same attempt row."* |
| Chống lấy sớm | *"Consider including a `retry_after` column and skip rows where `retry_after > NOW()`."* |

**[SUY LUẬN]** Áp dụng cho phía **NHẬN** webhook từ VNPay/MoMo/ZaloPay, ba việc bắt buộc:
1. **Xác thực chữ ký** của cổng thanh toán trước khi tin bất cứ điều gì.
2. **Idempotent**: cổng thanh toán **sẽ gửi lại** cùng một sự kiện nhiều lần. Dùng `transaction_id` của cổng làm khoá duy nhất:
   ```sql
   CREATE TABLE payment_events (
       id              bigserial PRIMARY KEY,
       provider        text NOT NULL,               -- 'vnpay' | 'momo' | 'zalopay' | 'manual'
       provider_txn_id text NOT NULL,
       rental_id       bigint REFERENCES rentals(id),
       amount          numeric(12,0) NOT NULL,      -- VNĐ
       raw_payload     jsonb NOT NULL,
       processed_at    timestamptz,
       created_at      timestamptz NOT NULL DEFAULT now(),
       UNIQUE (provider, provider_txn_id)           -- ★ nhận 10 lần cũng chỉ ghi 1
   );
   ```
3. **Trả HTTP 200 thật nhanh, xử lý sau**: ghi payload vào bảng rồi trả 200 ngay; việc chuyển trạng thái đơn để job nền làm. Nếu xử lý chậm, cổng thanh toán sẽ timeout và gửi lại → nhân bản tải.

### 12.4. Transactional Outbox Pattern

**[SNIPPET]** — Nguồn: [Implementing the Outbox Pattern (Milan Jovanović)](https://milanjovanovic.tech/blog/implementing-the-outbox-pattern) · [Transactional Outbox Pattern in Go with PostgreSQL (glukhov.org)](https://www.glukhov.org/app-architecture/integration-patterns/transactional-outbox-pattern-go/) · [pg-transactional-outbox (npm)](https://www.npmjs.com/package/pg-transactional-outbox) · [Zehelein/pg-transactional-outbox (GitHub)](https://github.com/Zehelein/pg-transactional-outbox) · [zeybek/ulak — PostgreSQL extension for reliable async message delivery (GitHub)](https://github.com/zeybek/ulak) · [Outbox pattern in PostgreSQL for reliable API integrations (AppMaster)](https://appmaster.io/blog/outbox-pattern-postgresql-integrations)

Nguyên lý **[SNIPPET]**: *"writing an event record into an outbox table **in the same database transaction** as the business data, and then a separate background process – the relay – reads from the outbox table and publishes."*
Về exactly-once **[SNIPPET]**: *"The transactional outbox and inbox patterns are used to ensure exactly-once processing... guaranteeing that a message is **sent at least once but processed exactly once**."*

👉 **Câu này rất đáng nhớ và nên đưa vào proposal [SNIPPET]:** *"exactly-once delivery"* trên mạng là **bất khả thi**; thứ đạt được là **"at-least-once delivery + idempotent processing = effectively exactly-once"**.

**Bài toán cụ thể của dự án [SUY LUẬN]:** khi đơn chuyển sang `confirmed`, phải gửi email/SMS/Zalo xác nhận. Nếu gọi API gửi mail **bên trong** transaction:
- Transaction rollback nhưng mail đã gửi → khách nhận xác nhận cho đơn không tồn tại. ❌
- Gọi mail **sau** commit nhưng server sập giữa chừng → đơn có mà không ai báo khách. ❌

Outbox giải cả hai:
```sql
CREATE TABLE outbox_messages (
    id            bigserial PRIMARY KEY,
    topic         text        NOT NULL,      -- 'rental.confirmed' | 'rental.reminder' ...
    payload       jsonb       NOT NULL,
    created_at    timestamptz NOT NULL DEFAULT now(),
    processed_at  timestamptz,
    attempts      int         NOT NULL DEFAULT 0,
    retry_after   timestamptz NOT NULL DEFAULT now(),
    last_error    text
);
CREATE INDEX ON outbox_messages (retry_after) WHERE processed_at IS NULL;
```
Worker lấy việc (an toàn với nhiều worker song song):
```sql
BEGIN;
SELECT * FROM outbox_messages
 WHERE processed_at IS NULL AND retry_after <= now()
 ORDER BY id
 FOR UPDATE SKIP LOCKED
 LIMIT 20;
-- gửi mail/Zalo ... rồi UPDATE processed_at = now()
-- nếu lỗi: attempts = attempts + 1,
--          retry_after = now() + (interval '1 minute' * power(2, attempts))
COMMIT;
```

> **[SUY LUẬN] Đánh giá mức độ cần thiết cho MVP:** Outbox là "nice to have", **không bắt buộc cho bản MVP 15–40 máy**. Nhưng chi phí thêm rất thấp (1 bảng + 1 worker ~50 dòng code) và nó là **điểm cộng lớn khi bảo vệ**, vì cho thấy nhóm hiểu vấn đề nhất quán dữ liệu giữa DB và dịch vụ ngoài. Đề xuất: **làm, nhưng để ở Sprint 3**.

---

# PHẦN E — SNIPE-IT: NGHIÊN CỨU SÂU (THAM CHIẾU GẦN NHẤT)

## 13. SNIPE-IT — MÔ HÌNH DỮ LIỆU, TÍNH NĂNG, CÀI ĐẶT, GIẤY PHÉP

> **Nguồn cho toàn mục này:** tôi đã **clone mã nguồn thật** từ `https://github.com/grokability/snipe-it` (commit `16362cc6a5cf54a77acbb0ab3cbaac79b75d85f6`, ngày 13/09/2026) và đọc trực tiếp các file Model + migration. Vì vậy **[MÃ NGUỒN]** ở đây là chính xác nguyên văn.
> Trang chủ: https://snipeitapp.com/ · Tài liệu: https://snipe-it.readme.io/docs/overview

### 13.1. Thông tin cơ bản (đã xác minh)

| Mục | Giá trị | Nguồn |
|---|---|---|
| Phiên bản hiện tại | **v8.7.2** (`full_app_version: v8.7.2 - build 24589-gf0bd1f8d76`) | **[MÃ NGUỒN]** `config/version.php` |
| Các tag gần nhất | v8.6.1, v8.6.2, v8.6.3, v8.7.0, v8.7.1, **v8.7.2** | **[MÃ NGUỒN]** `git ls-remote --tags` |
| **Giấy phép** | **`AGPL-3.0-or-later`** | **[MÃ NGUỒN]** `composer.json` → `"license": "AGPL-3.0-or-later"` |
| Ngôn ngữ / framework | PHP, **Laravel `^12.0`** | **[MÃ NGUỒN]** `composer.json` |
| PHP tối thiểu | **`^8.2`** | **[MÃ NGUỒN]** `composer.json` → `"php": "^8.2"` |
| Extension PHP bắt buộc | `curl`, `exif`, `fileinfo`, `iconv`, `json`, `mbstring`, `pdo` | **[MÃ NGUỒN]** `composer.json` |
| CSDL | MySQL/MariaDB (migration ghi `$table->engine = 'InnoDB'`) | **[MÃ NGUỒN]** |
| Thư viện đáng chú ý | `laravel/passport ^12.0` (OAuth API), `bacon/bacon-qr-code ^2.0` (**QR code**), `tecnickcom/tc-lib-barcode ^1.15` (**mã vạch**), `spatie/laravel-backup ^9.0`, `pragmarx/google2fa-laravel` (2FA), `onelogin/php-saml`, `livewire/livewire ^4.0` | **[MÃ NGUỒN]** |
| Số migration | **484 file** trong `database/migrations` | **[MÃ NGUỒN]** |

### 13.2. ⚠️ CẢNH BÁO PHÁP LÝ VỀ AGPL — PHẢI NÊU TRONG PROPOSAL

**[MÃ NGUỒN + SNIPPET]** `composer.json` ghi rõ `AGPL-3.0-or-later`. Snippet từ [snipeitapp.com/faq](https://snipeitapp.com/faq) xác nhận: *"Because Snipe-IT is licensed under the AGPL, any code that gets written has to be made available to the community."* Và: *"AGPL-3.0 is OSI-approved with a network use clause: modifying Snipe-IT and running it as a network service requires releasing modifications under the same licence."*

👉 **Hệ quả cho dự án khởi nghiệp [SUY LUẬN]:**
- ✅ **Dùng Snipe-IT NGUYÊN BẢN** cho nội bộ quản lý kho (không sửa code) → hoàn toàn ổn, không phải công khai gì.
- ⚠️ **Fork rồi sửa Snipe-IT thành website cho thuê công khai** → điều khoản "network use" của AGPL kích hoạt → **bắt buộc công khai toàn bộ mã nguồn đã sửa**. Với một startup, đây là bất lợi cạnh tranh nghiêm trọng.
- ✅ **Khuyến nghị: tự viết hệ thống đặt thuê, HỌC mô hình dữ liệu của Snipe-IT** (ý tưởng/thiết kế không bị bản quyền, chỉ mã nguồn mới bị). Có thể **tích hợp qua REST API** của Snipe-IT — dùng API không làm tác phẩm của mình thành "derivative work".
> ⚠️ Đây là **phân tích của tôi, KHÔNG PHẢI tư vấn pháp lý**. Nhóm nên ghi rõ trong proposal là "cần tham vấn thêm" nếu đi theo hướng fork.

### 13.3. Bảng `assets` — cột thật (đã xác minh)

**[MÃ NGUỒN]** `app/Models/Asset.php` → `protected $table = 'assets';`

`$fillable` (nguyên văn):
```php
'asset_tag', 'company_id', 'image', 'location_id', 'model_id', 'name', 'notes',
'order_number', 'purchase_cost', 'purchase_date', 'rtd_location_id', 'serial',
'status_id', 'supplier_id', 'warranty_months', 'requestable', 'last_checkout',
'expected_checkin', 'byod', 'asset_eol_date', 'eol_explicit', 'last_audit_date',
'next_audit_date', 'last_checkin',
```

Migration gốc **[MÃ NGUỒN]** `database/migrations/2013_11_15_190327_create_assets_table.php`:
```php
Schema::create('assets', function ($table) {
    $table->increments('id');
    $table->string('name')->nullable();
    $table->string('asset_tag')->nullable();
    $table->integer('model_id')->nullable();
    $table->string('serial')->nullable();
    $table->date('purchase_date')->nullable();
    $table->decimal('purchase_cost', 8, 2)->nullable();
    $table->string('order_number')->nullable();
    $table->integer('assigned_to')->nullable();
    $table->text('notes')->nullable();
    $table->integer('user_id')->nullable();
    $table->timestamps();
    $table->boolean('physical')->default(1);
    $table->engine = 'InnoDB';
});
```
> *(Các cột `status_id`, `assigned_type`, `byod`, `checkout_counter`, `last_checkin`, `asset_eol_date`... được thêm dần qua 484 migration về sau — ví dụ `2023_01_18_122534_add_byod_to_assets.php`, `2023_08_17_202638_add_last_checkin_to_assets.php`, `2026_07_17_000002_change_expected_checkin_to_datetime.php`.)*

Kiểu dữ liệu (`$casts`) **[MÃ NGUỒN]**:
```php
'purchase_date' => 'date',        'eol_explicit'    => 'boolean',
'last_checkout' => 'datetime',    'last_checkin'    => 'datetime',
'expected_checkin' => 'datetime', 'last_audit_date' => 'datetime',
'next_audit_date' => 'datetime:m-d-Y',
'model_id' => 'integer', 'status_id' => 'integer', 'company_id' => 'integer',
'location_id' => 'integer', 'rtd_company_id' => 'integer', 'supplier_id' => 'integer',
'created_at' => 'datetime', 'updated_at' => 'datetime', 'deleted_at' => 'datetime',
```

### 13.4. Cơ chế "checkout đa hình" — điểm thiết kế đáng học nhất

**[MÃ NGUỒN]** Snipe-IT cho phép giao tài sản cho **3 loại đối tượng khác nhau**: người dùng, địa điểm, hoặc **một tài sản khác** (vd: gán chuột cho laptop). Thực hiện bằng quan hệ đa hình (polymorphic) 2 cột:

```php
// app/Models/Asset.php
public function assignedTo()
{
    return $this->morphTo('assigned', 'assigned_type', 'assigned_to')->withTrashed();
}

// quy tắc validate
'assigned_to'   => ['nullable', 'integer', 'required_with:assigned_type'],
'assigned_type' => ['nullable', 'required_with:assigned_to',
                    'in:'.User::class.','.Location::class.','.Asset::class],
```
→ Hai cột `assigned_to` (int) + `assigned_type` (string tên class) tạo thành khoá ngoại "mềm".

**Hàm kiểm tra máy có cho thuê được không [MÃ NGUỒN]** — nguyên văn:
```php
public function availableForCheckout()
{
    // This asset is not currently assigned to anyone and is not deleted...
    if ((! $this->assigned_to) && (! $this->deleted_at)) {
        // The asset status is not archived and is deployable
        if (($this->status) && ($this->status->archived == '0')
            && ($this->status->deployable == '1')) {
            return true;
        }
        return false;
    }
    return false;
}
```
👉 **Bài học [SUY LUẬN]:** điều kiện "cho thuê được" = **chưa gán ai** ∧ **chưa xoá mềm** ∧ **status không archived** ∧ **status deployable**. Dự án nên có đúng một hàm tập trung như vậy, **không rải rác điều kiện khắp code**.
⚠️ **Nhưng chú ý:** Snipe-IT **không** có yếu tố **thời gian** ở đây — chỉ biết "đang rảnh **NGAY BÂY GIỜ**" chứ không trả lời được "máy này có rảnh **thứ Ba tuần sau 8h–12h** không". **Đó chính là khoảng trống mà sản phẩm của nhóm lấp vào.**

Hàm `checkOut()` **[MÃ NGUỒN]** — các bước thật:
```php
public function checkOut($target, $admin = null, $checkout_at = null, $expected_checkin = null,
                         $note = null, $name = null, $location = null, bool $signInPlace = false)
{
    if (! $target) { return false; }
    if ($this->is($target)) { throw new CheckoutNotAllowed('You cannot check an asset out to itself.'); }
    if ($expected_checkin) { $this->expected_checkin = $expected_checkin; }
    $this->last_checkout = $checkout_at;
    $this->name = $name;
    $this->assignedTo()->associate($target);
    // ... gán location_id theo target
    if ($this->save()) {
        // ...
        event(new CheckoutableCheckedOut($this, $target, $checkedOutBy, $note, $originalValues, 1, $signInPlace));
        $this->increment('checkout_counter', 1);
        return true;
    }
    return false;
}
```
👉 Đáng chú ý: **`checkout_counter`** — đếm số lần máy đã được giao. Dự án nên có cột tương tự (`total_rentals`, `total_rented_hours`) để: (a) tính hao mòn, (b) **cân bằng tải giữa các máy** khi tự động gán (xem mục 9.5).
👉 Snipe-IT **phát event** `CheckoutableCheckedOut` → listener ghi log + gửi mail. Đây là mẫu tách biệt tốt.

### 13.5. `status_labels` — mô hình trạng thái 3 cờ boolean (rất tinh tế)

**[MÃ NGUỒN]** `app/Models/Statuslabel.php` → `protected $table = 'status_labels';`

Snipe-IT **không** dùng một cột enum. Nó dùng **3 cờ boolean** `deployable`, `pending`, `archived` và **tổ hợp** ra 4 "kiểu" trạng thái:

```php
public function getStatuslabelType()
{
    if (($this->pending == '1') && ($this->archived == '0') && ($this->deployable == '0')) {
        return 'pending';
    } elseif (($this->pending == '0') && ($this->archived == '1') && ($this->deployable == '0')) {
        return 'archived';
    } elseif (($this->pending == '0') && ($this->archived == '0') && ($this->deployable == '0')) {
        return 'undeployable';
    }
    return 'deployable';
}
```

Bảng tra cứu **[MÃ NGUỒN — trích từ scope cache trong Statuslabel.php]**:

| Kiểu | `deployable` | `pending` | `archived` | Nghĩa | Tương ứng ở dự án thuê laptop |
|---|---|---|---|---|---|
| `deployable` | **1** | 0 | 0 | Sẵn sàng giao | Máy sẵn sàng cho thuê (Ready to Deploy) |
| `pending` | 0 | **1** | 0 | Đang chờ xử lý | Máy mới nhập / đang cài Windows + kiểm tra SEB |
| `undeployable` | 0 | 0 | 0 | Không giao được | Máy đang sửa / hỏng / chờ linh kiện |
| `archived` | 0 | 0 | **1** | Đã lưu trữ | Máy đã thanh lý / bán / mất |

Các cột khác của `status_labels` **[MÃ NGUỒN]**: `name` (varchar 100), `deployable`, `pending`, `archived`, `color` (thêm ở migration `2016_08_02_124944_add_color_to_statuslabel.php`), `show_in_nav` (`2016_08_23_145619`), `default_label` (`2018_03_06_054937`), `notes`, `deleted_at` (soft delete), `created_at`, `updated_at`.

👉 **Đây là mẫu thiết kế đáng học nhất của Snipe-IT [SUY LUẬN]:** thay vì hard-code enum trong code, Snipe-IT cho admin **tự tạo nhãn trạng thái** ("Đang cài SEB", "Chờ thay pin", "Cho mượn nội bộ") và chỉ cần **đánh 3 cờ** để hệ thống biết cách ứng xử. Cực kỳ linh hoạt mà logic vẫn đơn giản. Dự án nên copy nguyên mô hình này cho bảng `laptop_status_labels`.
👉 Snippet từ [DeepWiki – Asset Checkout & Checkin](https://deepwiki.com/grokability/snipe-it/2.5-asset-checkout-and-checkin) bổ sung **[SNIPPET]**: *"The checkout form restricts status selection to deployable labels only, while checkin allows any status to accommodate maintenance, repair, or retirement workflows."* — form **giao máy** chỉ cho chọn nhãn `deployable`, còn form **nhận máy về** cho chọn mọi nhãn (để đưa vào bảo trì/sửa/thanh lý). Rất hợp lý, nên bắt chước.

### 13.6. `models` (asset models) — tầng "LOẠI"

**[MÃ NGUỒN]** `app/Models/AssetModel.php` → `protected $table = 'models';` (chú ý: tên bảng là **`models`**, không phải `asset_models`).

`$fillable`:
```php
'category_id', 'depreciation_id', 'eol', 'fieldset_id', 'image',
'manufacturer_id', 'min_amt', 'model_number', 'name', 'notes',
'requestable', 'require_serial',
```
Migration gốc **[MÃ NGUỒN]** `2013_11_13_075318_create_models_table.php`: `id`, `name`, `modelno`, `manufacturer_id`, `category_id`, `timestamps`.

👉 Hai cột đáng chú ý cho dự án **[SUY LUẬN]**:
- **`min_amt`** = ngưỡng tồn kho tối thiểu → cảnh báo khi số máy loại này còn quá ít. Dự án nên có: *"Loại 'Windows i5/8GB' chỉ còn 2 máy rảnh cho ngày 20/09 — cân nhắc thuê thêm/dời lịch bảo trì."*
- **`fieldset_id`** → Snipe-IT hỗ trợ **trường tuỳ biến (custom fields)** theo từng loại máy. Với laptop thi, các trường quan trọng riêng là: `windows_version`, `ram_gb`, `cpu`, `da_cai_EOS` (bool), `da_test_SafeExamBrowser` (bool), `thoi_luong_pin_phut`. **Đây là điểm khác biệt cốt lõi của sản phẩm** — máy phải được **chứng nhận là đã test với phần mềm thi**.

Cấu trúc phân cấp **[SNIPPET — [DeepWiki](https://deepwiki.com/grokability/snipe-it/2.3-asset-models-and-relationships)]**: *"asset models serve as intermediaries between high-level categories and individual asset instances"* → `categories` → `models` → `assets`. Ba tầng.

### 13.7. `action_logs` — nhật ký hoạt động (audit trail)

**[MÃ NGUỒN]** `app/Models/Actionlog.php` → `protected $table = 'action_logs';`, `public $timestamps = true;`

`$fillable`:
```php
'created_at', 'item_type', 'created_by', 'item_id', 'action_type',
'note', 'order_item_id', 'target_id', 'target_type', 'stored_eula',
```

Migration **[MÃ NGUỒN]** `2016_09_04_180400_create_actionlog_table.php` — nguyên văn kèm comment của tác giả:
```php
Schema::create('action_logs', function (Blueprint $table) {
    $table->increments('id');
    $table->integer('user_id')->nullable();
    $table->string('action_type');
    $table->integer('target_id')->nullable();   // Was checkedout_to
    $table->string('target_type')->nullable();  // For polymorphic thingies
    $table->integer('location_id')->nullable();
    $table->text('note')->nullable();
    $table->text('filename')->nullable();
    $table->string('item_type');
    $table->integer('item_id');                 // Replaces asset_id, accessory_id, etc.
    $table->date('expected_checkin')->nullable()->default(null);
    $table->integer('accepted_id')->nullable();
    $table->timestamps();
    $table->softDeletes();
    $table->integer('thread_id')->nullable()->default(null);
    $table->index('thread_id');
});
```

👉 **Ba điểm thiết kế đáng học [MÃ NGUỒN + SUY LUẬN]:**
1. **Đa hình kép**: `(item_type, item_id)` = *đối tượng bị tác động*; `(target_type, target_id)` = *đối tượng nhận*. Một bảng log duy nhất cho **mọi** loại tài sản. Comment gốc ghi rõ: `// Replaces asset_id, accessory_id, etc.`
2. **`action_type`** là chuỗi tự do — trong code thấy các giá trị: `'accepted'`, `'declined'`, `'audit'` (và checkout/checkin/update).
3. **`filename`** để đính kèm (ảnh biên bản, file ký) và **`stored_eula`** lưu bản điều khoản khách đã đồng ý **tại thời điểm đó** — **rất quan trọng về pháp lý**: nếu sau này sửa điều khoản thuê, bản ghi cũ vẫn giữ nguyên bản khách đã ký.

Snippet bổ sung **[SNIPPET — [DeepWiki – Activity Logging](https://deepwiki.com/grokability/snipe-it/4.4-activity-logging)]**: *"every significant action performed in Snipe-IT creates an actionlog entry, providing a complete audit trail"*, và *"The Actionlog model uses polymorphic relationships to track actions on any type of entity."*

⚠️ **Điểm YẾU của `action_logs` cần biết [MÃ NGUỒN]:** bảng có `softDeletes()` → **log CÓ THỂ bị xoá mềm**. Nó **không** phải append-only thực sự, **không** có hash chain. Với tài sản giá trị cao và tranh chấp, dự án nên làm **tốt hơn Snipe-IT** ở điểm này (xem mục 15).

### 13.8. `checkout_requests` — VÌ SAO SNIPE-IT KHÔNG THAY THẾ ĐƯỢC SẢN PHẨM CỦA NHÓM

**[MÃ NGUỒN]** — đây là phát hiện quan trọng nhất về Snipe-IT. Migration `2016_09_02_001448_create_checkout_requests_table.php`, **nguyên văn toàn bộ**:

```php
Schema::create('checkout_requests', function (Blueprint $table) {
    $table->increments('id');
    $table->integer('user_id');
    $table->integer('requestable_id');
    $table->string('requestable_type');
    $table->integer('quantity')->default(1);
    $table->timestamps();
    $table->unique(['user_id', 'requestable_id', 'requestable_type']);
});
```
*(về sau thêm `canceled_at`, `fulfilled_at` ở migration `2018_03_29_053618_add_canceled_at_and_fulfilled_at_in_requests.php`)*

🔴 **KHÔNG CÓ `start_date`. KHÔNG CÓ `end_date`. KHÔNG CÓ khoảng thời gian nào cả.**

👉 **Kết luận rất mạnh cho proposal [MÃ NGUỒN + SUY LUẬN]:**
> Snipe-IT quản lý tài sản theo mô hình **"đang ở đâu, ai đang giữ"** (state hiện tại), **không** theo mô hình **"ai sẽ giữ, từ lúc nào tới lúc nào"** (lịch tương lai). Bảng `checkout_requests` chỉ là *"tôi muốn mượn cái này"* — một hàng đợi yêu cầu, **không phải đặt lịch**.
> ⇒ **Snipe-IT hoàn toàn không chống được double-booking theo thời gian.** Hai sinh viên đều "request" cùng một máy cho ngày 20/09 thì Snipe-IT vui vẻ nhận cả hai (chỉ chặn khi **cùng một user** request **cùng một** tài sản 2 lần, do `unique(['user_id','requestable_id','requestable_type'])`).
> ⇒ Đây là **lý do kỹ thuật chính đáng, có bằng chứng mã nguồn**, để nhóm tự xây hệ thống đặt lịch thay vì dùng Snipe-IT.

Bảng bổ trợ đáng học **[MÃ NGUỒN]** `2018_07_28_023826_create_checkout_acceptances_table.php`:
```php
Schema::create('checkout_acceptances', function (Blueprint $table) {
    $table->increments('id');
    $table->morphs('checkoutable');                    // -> checkoutable_type + checkoutable_id
    $table->integer('assigned_to_id')->nullable();
    $table->string('signature_filename')->nullable();  // ★ CHỮ KÝ ĐIỆN TỬ
    $table->timestamp('accepted_at')->nullable();
    $table->timestamp('declined_at')->nullable();
    $table->timestamps();
    $table->softDeletes();
});
```
*(về sau thêm `eula` ở `2022_03_09_001334_add_eula_to_checkout_acceptance.php`, `note` ở `2024_03_18_164714`, `qty` ở `2025_08_12_225214`)*

👉 **`signature_filename` + `accepted_at` / `declined_at` = biên bản bàn giao có chữ ký.** Dự án **bắt buộc** phải có tính năng này: khách ký nhận máy trên màn hình điện thoại, hệ thống lưu ảnh chữ ký + timestamp + ảnh tình trạng máy. Đây là **bằng chứng khi tranh chấp** (mục 15).

### 13.9. Tổng hợp: những gì NÊN LẤY và KHÔNG NÊN LẤY từ Snipe-IT

**[SUY LUẬN]**

| Lấy ✅ | Không lấy ❌ |
|---|---|
| Mô hình 3 tầng `categories` → `models` → `assets` | Toàn bộ codebase (rào cản AGPL) |
| `status_labels` với 3 cờ `deployable`/`pending`/`archived` | MySQL (dự án nên dùng PostgreSQL) |
| `action_logs` đa hình `(item_type,item_id)` + `(target_type,target_id)` | `softDeletes()` trên bảng log |
| `checkout_acceptances` với `signature_filename` + `eula` | `checkout_requests` (không có thời gian) |
| Cột `last_audit_date` / `next_audit_date` (kiểm kê định kỳ) | 484 migration + hàng chục tích hợp không cần (SAML, LDAP, SCIM, Rollbar…) |
| Cột `checkout_counter` (đếm lượt sử dụng) | Custom fieldset engine phức tạp (làm đơn giản hơn) |
| Custom fields theo model (để lưu `da_test_SEB`) | |
| QR code / barcode cho tài sản (thư viện `bacon/bacon-qr-code`) | |

---

# PHẦN F — CÁC HỆ THỐNG MỞ / THƯƠNG MẠI KHÁC

## 14. KHẢO SÁT SO SÁNH

### 14.1. LibreBooking (tên cũ: Booked Scheduler) — MÃ NGUỒN MỞ

**[MÃ NGUỒN + SNIPPET]** Repo: https://github.com/LibreBooking/app — tôi đã tải `README.md`, `doc/INSTALLATION.md` và `database_schema/create-schema.sql` thật.

| Mục | Giá trị | Nguồn |
|---|---|---|
| Giấy phép | **GPLv3** | **[MÃ NGUỒN]** README: *"This is a community effort to keep the OpenSource [GPLv3] LibreBooking alive"* |
| Yêu cầu | **PHP 8.1+**, **MySQL 5.5+**, web server (Apache/IIS) | **[MÃ NGUỒN]** README mục "Prerequisites" |
| Bản phát hành gần nhất ghi trong README | **2.8.6.2 — 18/08/2024** | **[MÃ NGUỒN]** README "Release Notes" |
| Công nghệ | PHP + Smarty template | **[SNIPPET]** |
| Docker | Có repo riêng `github.com/LibreBooking/docker` | **[MÃ NGUỒN]** README |

🔴 **CẢNH BÁO QUAN TRỌNG VỀ SỨC KHOẺ DỰ ÁN [MÃ NGUỒN]** — README mở đầu bằng nguyên văn:
> *"As some are aware, due to a chronic lack of time and health issues, I haven't been the fastest to answer, implement new features or fix bugs... At the moment my health is not the strongest... in the coming months I won't be able to do much, besides fixing breaking bugs or merge pull requests."*

👉 Dự án gần như **chỉ còn một người bảo trì và đang tạm dừng phát triển**; bản phát hành cuối ghi trong README là **18/08/2024** (cách thời điểm nghiên cứu ~2 năm). **[SUY LUẬN] KHÔNG nên xây sản phẩm khởi nghiệp trên nền này.** Nhưng **schema của nó là tài liệu tham khảo miễn phí rất tốt.**

**Schema thật của LibreBooking [MÃ NGUỒN]** — danh sách bảng đầy đủ:
`announcements, layouts, time_blocks, schedules, groups, roles, group_roles, user_statuses, users, user_groups, resources, user_resource_permissions, group_resource_permissions, reservation_types, reservation_statuses, reservation_users, reservation_resources, user_email_preferences, quotas, accessories, reservation_accessories, reservation_series, reservation_instances`

Ba bảng cốt lõi (nguyên văn):
```sql
CREATE TABLE `reservation_series` (
  `series_id` int unsigned NOT NULL auto_increment,
  `date_created` datetime NOT NULL,
  `last_modified` datetime,
  `title` varchar(85) NOT NULL,
  `description` text,
  `allow_participation` tinyint(1) unsigned NOT NULL,
  `allow_anon_participation` tinyint(1) unsigned NOT NULL,
  `type_id` tinyint(2) unsigned NOT NULL,
  `status_id` tinyint(2) unsigned NOT NULL,
  `repeat_type` varchar(10) default NULL,          -- lặp: daily/weekly/monthly
  `repeat_options` varchar(255) default NULL,
  `owner_id` mediumint(8) unsigned NOT NULL,
  ...
);

CREATE TABLE `reservation_instances` (
  `reservation_instance_id` int unsigned NOT NULL auto_increment,
  `start_date` datetime NOT NULL,
  `end_date`   datetime NOT NULL,
  `reference_number` varchar(50) NOT NULL,
  `series_id`  int unsigned NOT NULL,
  PRIMARY KEY (`reservation_instance_id`),
  KEY `start_date` (`start_date`), KEY `end_date` (`end_date`),
  KEY `reference_number` (`reference_number`), KEY `series_id` (`series_id`),
  ...
);

CREATE TABLE `reservation_resources` (
  `series_id`         int unsigned NOT NULL,
  `resource_id`       smallint(5) unsigned NOT NULL,
  `resource_level_id` tinyint(2) unsigned NOT NULL,   -- 1 = tài nguyên chính, 2 = phụ
  PRIMARY KEY (`series_id`, `resource_id`),
  ...
);
```

👉 **Ba bài học [MÃ NGUỒN + SUY LUẬN]:**
1. **Tách `series` và `instance`** — một đơn "lặp lại hằng tuần" là **1 series** sinh ra **N instance**. Nếu dự án muốn hỗ trợ *"thuê mỗi thứ Ba trong 6 tuần thi cuối kỳ"* thì đây là mô hình đúng. Với MVP thì chưa cần, nhưng nên biết để không phải đập đi làm lại.
2. **`reservation_resources` là bảng nối N-N** — một đơn có thể giữ **nhiều tài nguyên**. Áp dụng: khách thuê 1 laptop + 1 chuột + 1 túi chống sốc.
3. 🔴 **KHÔNG CÓ ràng buộc chống trùng lịch nào ở cấp DB** — chỉ có `KEY start_date`, `KEY end_date` (index cho tốc độ, không phải constraint). Vì chạy MySQL nên **buộc phải kiểm tra trùng lịch bằng code PHP**. **Đây là bằng chứng cụ thể cho luận điểm "chọn PostgreSQL để có `EXCLUDE`"** trong proposal của nhóm.

Nguồn snippet bổ sung **[SNIPPET]**: [List: Open source software for resource scheduling and booking (Edgeryders)](https://edgeryders.eu/t/list-open-source-software-for-resource-scheduling-and-booking/6629) · [Best Open Source Scheduling Software in 2026 (Booknetic)](https://www.booknetic.com/blog/best-open-source-scheduling-software) — snippet nêu: *"LibreBooking is the best open source option for organizations managing shared resources. If your goal is booking rooms, equipment, or spaces, it is more purpose-built than any other free tool."* · Hướng dẫn dùng thực tế tại một phòng lab đại học: [Guide for the Booked Reservation System — University of Washington Sociology Lab](https://depts.washington.edu/sociolab/labfacilities/equipmentguide.php)

### 14.2. LibCal (Springshare) — THƯƠNG MẠI, chuyên cho thư viện

**[SNIPPET]** — Nguồn: [springshare.com/libcal](https://www.springshare.com/libcal) · [LibCal for Academic Libraries](https://www.springshare.com/academic-libraries/libcal) · [LibCal for Public Libraries](https://www.springshare.com/public-libraries/libcal)

Tính năng liên quan trực tiếp (theo snippet):
- Đặt **không gian, thiết bị, lịch hẹn** từ điện thoại.
- **Đồng bộ 2 chiều** với Outlook, Google Calendar, LibStaffer để chặn khung giờ bận.
- **Cho mượn thiết bị**: *"Establish a lending program for equipment, technology and makerspace tools, Library of Things collections, and museum passes and tickets."*
- **Thanh toán**: *"If you charge for events, space, or equipment rentals, LibCal makes it easy to collect payments quickly and securely during the registration or booking process."*
- **API đầy đủ** đọc và ghi.

⚠️ **Không tìm thấy giá công khai** trong kết quả tìm kiếm. **[UNCERTAIN]**
👉 **[SUY LUẬN]** Giá trị của LibCal với nhóm: **danh sách tính năng chuẩn ngành cho thuê thiết bị**, dùng làm checklist đối chiếu MVP. Đặc biệt ý *"đồng bộ 2 chiều với lịch"* — dự án nên cho khách **thêm lịch nhận/trả máy vào Google Calendar** (xuất file `.ics`), rất rẻ để làm mà giảm hẳn tỉ lệ khách quên.

### 14.3. Koha — MÃ NGUỒN MỞ (đã phân tích sâu ở mục 9)

Repo: https://github.com/Koha-Community/Koha · Schema đã đọc: `installer/data/mysql/kohastructure.sql`
Xem lại **mục 9.1 – 9.3** để có schema `bookings` / `reserves` / `issues` / `items` nguyên văn.

### 14.4. Odoo Rental Module — ERP, có bản Community mã nguồn mở

**[SNIPPET]** — Nguồn: [Rental — Odoo 18.0 documentation](https://www.odoo.com/documentation/18.0/applications/sales/rental.html) · [Rental — Odoo 17.0](https://www.odoo.com/documentation/17.0/applications/sales/rental.html) · [Rental — Odoo 19.0](https://www.odoo.com/documentation/19.0/applications/sales/rental.html) · [Rental | Features | Odoo](https://www.odoo.com/app/rental-features) · [Exploring the Rental Module in Odoo 18 (ERPGap)](https://www.erpgap.com/blog/exploring-rental-module-odoo-18)

Tính năng (theo snippet) — **đây là checklist nghiệp vụ tốt nhất tìm được**:

| Tính năng Odoo Rental | Trích snippet | Áp dụng cho thuê laptop |
|---|---|---|
| **Bảng giá nhiều bậc thời gian** | *"choose a unit of time (hours, days, weeks, or months), a duration, and a price, and add as many price lines as necessary, usually to give out discounts for longer rental durations"* | Giá theo **ca thi (4h)** / ngày / tuần; thuê dài giảm giá |
| **Quy tắc tính giá** | *"Odoo always uses two rules... only one price line is used, and the cheapest line is selected"* | Luôn tự chọn **dòng giá rẻ nhất** cho khách — thuật toán đơn giản, minh bạch |
| **Phí đặt chỗ** | *"establish reservation fees"* | Phí giữ chỗ không hoàn lại nếu khách bỏ đơn |
| **Phạt trả trễ** | *"configure additional fines for any extra hour or extra day that the customer takes to return a rental"* | Phí trễ giờ tính theo giờ (VNĐ/giờ) |
| **Security Time** ⭐ | *"set a Security Time, expressed in hours, to make the rental product temporarily unavailable between two rental orders"* | **Thời gian đệm giữa 2 lượt thuê** để cài lại/kiểm tra EOS + SEB — xem mục 3.3(b) |
| **Lịch trực quan** | *"a user-friendly calendar view that enables users to monitor the availability of rental items in real time, helping prevent double bookings"* | Màn hình admin dạng Gantt: trục Y = máy, trục X = thời gian |
| **Đặt/thanh toán trên web** | *"Customers can shop available products, reserve their selected dates, and checkout right on the website"* | Luồng đặt online |
| **Cọc & thanh toán từng phần** | *"manage payments effortlessly - including partial payments and deposits"* | Cọc trước + thanh toán phần còn lại khi nhận máy |

👉 **[SUY LUẬN]** Odoo Community là mã nguồn mở (LGPL-3) nhưng **quá nặng** cho một dự án 15–40 máy (ERP đầy đủ, cần nhiều RAM, đường học dốc). **Không khuyến nghị dùng, nhưng RẤT nên copy danh sách tính năng làm backlog.**
⚠️ **[UNCERTAIN]** Không xác minh được module `sale_renting` nằm ở bản Community hay chỉ Enterprise. Nhóm cần tự kiểm tra nếu định dùng.

### 14.5. EZRentOut — SaaS thương mại

**[SNIPPET]** — Nguồn: [ezo.io/ezrentout](https://ezo.io/ezrentout/) · [Pricing Plans for Rental Businesses — EZRentOut](https://ezo.io/ezrentout/pricing/) · [EZRentOut Software Pricing, Alternatives & More 2026 — Capterra](https://www.capterra.com/p/134914/EZRentOut/) · [EZRentOut 2026 Pricing, Features, Reviews — GetApp](https://www.getapp.com/industries-software/a/ezrentout/) · [EZRentOut Reviews — SoftwareConnect](https://softwareconnect.com/reviews/ezrentout/)

| Mục | Giá trị | Ghi chú |
|---|---|---|
| **Giá khởi điểm** | **50 USD / 2 người dùng / tháng** | **[SNIPPET — CẦN KIỂM CHỨNG]** *"The starting price of EZRentOut is $50/2 Users/Month."* Quy đổi thô ~**1,3 triệu VNĐ/tháng** (tỉ giá tham chiếu ~26.000 VNĐ/USD — **nhóm phải tra tỉ giá thật tại thời điểm viết**) |
| Tính năng lõi | reservations, recurring rentals, order management, inventory tracking với **quét barcode/QR** | **[SNIPPET]** |
| Bảo trì | *"Preventive maintenance scheduling with alerts and service history keeps equipment safe and rentable"* | **[SNIPPET]** |
| Thuê lại (sub-rental) | *"sub-rental tracking covers demand that exceeds owned stock"* | **[SNIPPET]** — rất đáng học: khi cháy kho thì đi thuê lại của bên khác |
| Báo cáo | *"utilization, revenue, and asset reports help teams set pricing, plan purchases, and **cut idle stock**"* | **[SNIPPET]** |
| App di động | iOS + Android native | **[SNIPPET]** |

👉 **[SUY LUẬN] Ba ý dùng được ngay trong proposal:**
1. **Chỉ số utilization (tỉ lệ khai thác)** = tổng giờ cho thuê / tổng giờ khả dụng. Đây là **KPI số 1** của mọi mô hình cho thuê. Proposal **bắt buộc** phải có chỉ số này trong phần tài chính.
2. **Sub-rental** — mùa thi cháy kho thì thuê lại máy của tiệm khác / của SV khoá trên. Là chiến lược mở rộng chi phí thấp, rất hợp cảnh sinh viên khởi nghiệp.
3. **Preventive maintenance** — lên lịch bảo trì **chủ động** (vệ sinh quạt, thay pin, cập nhật Windows) thay vì đợi hỏng. Rất quan trọng khi hỏng đúng ngày thi = mất khách vĩnh viễn.
4. **So sánh chi phí:** 50 USD/tháng ≈ 15,6 triệu VNĐ/năm. Nếu nhóm tự viết, tiền hosting chỉ ~2,1–5,7 triệu VNĐ/năm (mục 16.3). **Đây là con số biện minh cho việc tự phát triển** — nhưng nhớ tính cả **chi phí cơ hội thời gian** của nhóm.

### 14.6. Rentman — SaaS thương mại, chuyên thiết bị AV có serial

**[SNIPPET]** — Nguồn: [Equipment Check-In & Check-Out Software for Rental Warehouses — Rentman](https://rentman.io/solutions/rental-equipment-tracking-software)

> *"Rentman tracks individual serial numbers across concurrent productions, manages sub-rentals from suppliers, and gives warehouse teams digital packing slips that validate every item. Scan serialized AV equipment in and out with QR codes."*

👉 **[SUY LUẬN]** Rentman là bằng chứng ngành cho **mô hình theo dõi từng serial qua nhiều đơn thuê song song** — đúng bài toán của dự án. Ý **"digital packing slips that validate every item"** = **phiếu bàn giao số kiểm đếm từng món**. Áp dụng: khi giao máy, nhân viên quét QR của laptop + sạc + chuột + túi → hệ thống tự tick đủ món; khi nhận về quét lại → phát hiện ngay thiếu sạc.

### 14.7. Bảng so sánh tổng hợp các hệ thống

| Hệ thống | Mã nguồn mở? | Giấy phép | Có đặt lịch theo thời gian? | Theo dõi từng serial? | Chống trùng lịch ở cấp DB? | Phù hợp làm nền cho dự án? |
|---|---|---|---|---|---|---|
| **Snipe-IT v8.7.2** | ✅ | **AGPL-3.0-or-later** | ❌ (`checkout_requests` không có ngày) | ✅ (`assets.serial`) | ❌ | ❌ (rào cản AGPL + thiếu đặt lịch) |
| **Koha** | ✅ | GPL | ✅ (`bookings.start_date/end_date`) | ✅ (`items.barcode`) | ❌ (MySQL, check ở code) | ❌ (là ILS thư viện, quá đồ sộ) |
| **LibreBooking** | ✅ | **GPLv3** | ✅ (`reservation_instances`) | ⚠️ (`resources`, không có serial) | ❌ (MySQL) | ❌ (gần như dừng phát triển) |
| **Odoo Rental** | ⚠️ (Community LGPL) | LGPL-3 | ✅ | ✅ (lot/serial) | ❌ | ❌ (quá nặng) |
| **LibCal** | ❌ | Thương mại | ✅ | ✅ | n/a | ❌ (SaaS, không rõ giá) |
| **EZRentOut** | ❌ | Thương mại (~50 USD/th) | ✅ | ✅ | n/a | ❌ (đắt so với 15–40 máy) |
| **Rentman** | ❌ | Thương mại | ✅ | ✅ | n/a | ❌ |
| **TỰ XÂY (khuyến nghị)** | — | — | ✅ | ✅ | ✅ **`EXCLUDE`** | ✅ |

👉 **Kết luận có sức nặng cho proposal [SUY LUẬN]:** *"Chúng tôi đã khảo sát 7 hệ thống quản lý tài sản/đặt thuê. **Không hệ thống mã nguồn mở nào vừa (a) đặt lịch theo thời gian, vừa (b) theo dõi từng serial, vừa (c) chống trùng lịch ở cấp cơ sở dữ liệu.** Các hệ thương mại có đủ nhưng chi phí ~50 USD/tháng, không kinh tế ở quy mô 15–40 máy. Vì vậy chúng tôi tự phát triển, kế thừa mô hình dữ liệu đã được kiểm chứng của Snipe-IT (tài sản) và Koha (đặt lịch)."*

---

# PHẦN G — AUDIT LOG BẤT BIẾN & CHAIN OF CUSTODY

## 15. NHẬT KÝ KHÔNG THỂ SỬA — BẰNG CHỨNG KHI TRANH CHẤP

### 15.1. Vì sao dự án này ĐẶC BIỆT cần

**[SUY LUẬN]** Ba tình huống tranh chấp gần như chắc chắn sẽ xảy ra:
1. *"Máy đã xước/nứt viền màn hình từ trước khi tôi thuê"* → cần ảnh + timestamp tại thời điểm giao.
2. *"Tôi trả máy lúc 17h chứ không phải 19h, sao tính phí trễ 2 tiếng?"* → cần log thời điểm nhận máy về.
3. *"Tôi có trả cả sạc mà"* → cần phiếu kiểm đếm từng món có chữ ký.

Giá trị tài sản **8–20 triệu VNĐ/máy** (con số tham khảo — **nhóm lấy từ file nghiên cứu giá thiết bị**), nên tranh chấp có thể lên tới vài triệu đồng. Nhật ký phải **đủ tin cậy để làm bằng chứng**.

### 15.2. Bốn mức độ bất biến

**[SNIPPET]** — Nguồn: [How to build an immutable audit log with HMAC hash chaining (Tracehold)](https://tracehold.ai/blog/immutable-audit-log-hmac-hash-chain/) · [How do you enforce immutability and append-only audit trails? (DesignGurus)](https://www.designgurus.io/answers/detail/how-do-you-enforce-immutability-and-appendonly-audit-trails) · [Immutable Audit Trails: From Logs to Cryptographic Proof (AesirX)](https://aesirx.io/blog/compliance-one/immutable-audit-trails-when-your-audit-log-becomes-cryptographic-proof) · [Making an Audit Trail Immutable Is Easy. Operating One Is Not. (Medium/VeritasChain, 05/2026)](https://medium.com/@veritaschain/append-only-is-the-easy-part-e25820208213) · [An immutable audit trail for AI agent actions (dev.to)](https://dev.to/codemalasartes/an-immutable-audit-trail-for-ai-agent-actions-fastapi-async-sqlalchemy-4m4c) · [Immutable Audit Log Architecture (EmergentMind)](https://www.emergentmind.com/topics/immutable-audit-log)

| Mức | Kỹ thuật | Chống được gì | Chi phí | Khuyến nghị cho dự án |
|---|---|---|---|---|
| **1. Append-only ở tầng ứng dụng** | Chỉ có hàm `INSERT`, không viết `UPDATE`/`DELETE` | Bug của chính mình | ~0 | ✅ **Bắt buộc** |
| **2. Append-only ở tầng DB** | `REVOKE UPDATE, DELETE ON audit_log FROM app_user;` + trigger `BEFORE UPDATE/DELETE → RAISE EXCEPTION` | Bug + SQL injection | Rất thấp | ✅ **Bắt buộc — chỉ vài dòng SQL** |
| **3. Hash chain** | Mỗi dòng chứa hash của dòng trước | Sửa lén bởi người có quyền DB (**phát hiện được**) | Thấp | ✅ **Nên làm — điểm cộng lớn** |
| **4. Neo ra ngoài (anchoring)** | Định kỳ ký/công bố hash gốc ra hệ thống ngoài | Chứng minh với **bên thứ ba** | Trung bình–cao | ❌ Quá mức cho MVP |

**Cảnh báo quan trọng từ nguồn [SNIPPET]:**
> *"Append-only protects you from your own code. It does not, on its own, prove to a third party that no one with database access quietly edited a row."*
> — tạm dịch: *"Append-only bảo vệ bạn khỏi chính code của bạn. Tự nó **không** chứng minh được với bên thứ ba rằng không ai có quyền truy cập database đã lặng lẽ sửa một dòng."*
> → Đây chính là lý do cần **mức 3 (hash chain)**.

Mô tả hash chain **[SNIPPET]**:
> *"each row stores a monotonic sequence number, the hash of the previous row, and its own hash, computed as the SHA-256 digest of the previous hash, the sequence number, and a canonical JSON encoding of the row's semantic fields."*

### 15.3. Schema audit log đề xuất **[SUY LUẬN — dựa trên mẫu snippet ở trên + mô hình đa hình của Snipe-IT]**

```sql
CREATE TABLE audit_log (
    seq          bigserial PRIMARY KEY,          -- số thứ tự đơn điệu tăng
    occurred_at  timestamptz NOT NULL DEFAULT now(),
    actor_type   text NOT NULL,                  -- 'staff' | 'customer' | 'system'
    actor_id     bigint,
    action       text NOT NULL,                  -- 'rental.handover' | 'laptop.status_changed' ...
    subject_type text NOT NULL,                  -- 'laptop' | 'rental' | 'payment'   (mẫu Snipe-IT: item_type)
    subject_id   bigint NOT NULL,                --                                    (mẫu Snipe-IT: item_id)
    target_type  text,                           -- đối tượng nhận  (mẫu Snipe-IT: target_type)
    target_id    bigint,
    payload      jsonb NOT NULL DEFAULT '{}'::jsonb,   -- giá trị trước/sau, ghi chú, đường dẫn ảnh
    ip_address   inet,
    user_agent   text,
    prev_hash    text NOT NULL,                  -- hash của dòng seq-1  (dòng đầu tiên = 64 số 0)
    row_hash     text NOT NULL                   -- sha256(prev_hash || seq || canonical_json(payload_fields))
);

-- ★ CHẶN SỬA/XOÁ Ở CẤP DATABASE
CREATE OR REPLACE FUNCTION audit_log_immutable() RETURNS trigger AS $$
BEGIN
    RAISE EXCEPTION 'audit_log la append-only: khong duoc UPDATE hoac DELETE';
END; $$ LANGUAGE plpgsql;

CREATE TRIGGER audit_log_no_update BEFORE UPDATE ON audit_log
    FOR EACH ROW EXECUTE FUNCTION audit_log_immutable();
CREATE TRIGGER audit_log_no_delete BEFORE DELETE ON audit_log
    FOR EACH ROW EXECUTE FUNCTION audit_log_immutable();

-- ★ và thu hồi quyền ở cấp vai trò
REVOKE UPDATE, DELETE, TRUNCATE ON audit_log FROM app_user;
```

Câu lệnh kiểm tra toàn vẹn chuỗi (chạy định kỳ, ví dụ hằng đêm):
```sql
-- Trả về các dòng bị đứt chuỗi (nếu có dòng nào => đã bị can thiệp)
SELECT a.seq
FROM audit_log a
JOIN audit_log b ON b.seq = a.seq - 1
WHERE a.prev_hash <> b.row_hash;
```

> ⚠️ **[SUY LUẬN]** Lưu ý thực tế: dòng `bigserial` có thể **nhảy số** khi transaction rollback. Nếu muốn chuỗi liền mạch tuyệt đối, phải sinh `seq` trong cùng transaction bằng `SELECT max(seq)+1 ... FOR UPDATE` — nhưng như vậy sẽ tuần tự hoá toàn bộ ghi log. **Với dự án nhỏ, chấp nhận được**; nhóm nên nêu rõ đánh đổi này nếu bị hỏi.

### 15.4. Chain of custody cho laptop — thiết kế nghiệp vụ

**[SNIPPET]** — Nguồn: [The Truth About Asset Records: Why Immutability Is the Foundation of a Verifiable Chain of Custody (LocatorX)](https://www.locatorx.com/blog/the-truth-about-asset-records-why-immutability-is-the-foundation-of-a-verifiable-chain-of-custody)
Snippet ghi: *"An immutable chain of custody system is append-only by architecture, uses cryptographic integrity checks such as hash-chaining, and is designed so that any attempt to change past events becomes evident during verification."*

**[SUY LUẬN]** Mỗi lần laptop đổi tay phải sinh **một bản ghi bàn giao** kèm bằng chứng:

```sql
CREATE TABLE custody_events (
    id              bigserial PRIMARY KEY,
    laptop_id       bigint NOT NULL REFERENCES laptops(id),
    rental_id       bigint REFERENCES rentals(id),
    direction       text NOT NULL,     -- 'out' (giao khách) | 'in' (nhận về)
    from_party      text NOT NULL,     -- 'warehouse' | 'customer:123' | 'repair_shop'
    to_party        text NOT NULL,
    occurred_at     timestamptz NOT NULL DEFAULT now(),
    staff_id        bigint NOT NULL REFERENCES staff(id),
    -- bằng chứng
    photo_urls      jsonb NOT NULL DEFAULT '[]'::jsonb,   -- ảnh 4 mặt máy + màn hình đang bật
    signature_url   text,                                  -- ảnh chữ ký (mẫu Snipe-IT: signature_filename)
    accessories     jsonb NOT NULL DEFAULT '{}'::jsonb,    -- {"sac":true,"chuot":true,"tui":false}
    condition_notes text,
    battery_health  int,                                   -- % pin, đo tại thời điểm bàn giao
    -- xác nhận sẵn sàng thi (ĐẶC THÙ CỦA DỰ ÁN NÀY)
    os_version         text,        -- vd 'Windows 11 Pro 24H2'
    eos_installed      boolean NOT NULL DEFAULT false,
    seb_tested         boolean NOT NULL DEFAULT false,
    seb_tested_at      timestamptz,
    eula_snapshot      text         -- bản điều khoản tại thời điểm ký (mẫu Snipe-IT: stored_eula)
);
```

👉 **`eos_installed` / `seb_tested` / `seb_tested_at` là điểm khác biệt cạnh tranh của sản phẩm [SUY LUẬN]:** không tiệm cho thuê laptop thông thường nào chứng nhận *"máy này đã được kiểm tra chạy được EOS + Safe Exam Browser lúc HH:MM ngày DD/MM"*. Đây vừa là **tính năng bán hàng**, vừa là **lá chắn pháp lý** khi khách khiếu nại "máy không thi được".
👉 **Ảnh bằng chứng:** nên bắt buộc **tối thiểu 4 ảnh** khi giao và 4 ảnh khi nhận (mặt A, bàn phím, màn hình đang bật hiển thị màn hình desktop, đáy máy). Lưu ảnh kèm timestamp trong `audit_log`.

---

# PHẦN H — CHỌN STACK CÔNG NGHỆ & HOSTING

## 16. KHUYẾN NGHỊ STACK CHO NHÓM SINH VIÊN

### 16.1. PostgreSQL vs MySQL — quyết định QUAN TRỌNG NHẤT

**[SUY LUẬN — có bằng chứng gián tiếp mạnh từ mã nguồn]**

| Tiêu chí | PostgreSQL | MySQL / MariaDB |
|---|---|---|
| **`EXCLUDE` constraint** | ✅ **CÓ** | ❌ **KHÔNG CÓ** |
| **Range type (`tstzrange`)** | ✅ CÓ, kèm toán tử `&&` | ❌ KHÔNG CÓ |
| **`btree_gist`** | ✅ CÓ | ❌ Không áp dụng |
| `FOR UPDATE SKIP LOCKED` | ✅ | ✅ (MySQL 8.0+) |
| `jsonb` có chỉ mục GIN | ✅ Rất mạnh | ⚠️ JSON có nhưng yếu hơn |
| Advisory lock | ✅ `pg_advisory_lock` | ⚠️ `GET_LOCK()` (hạn chế hơn) |
| Hosting VN hỗ trợ | Phổ biến | Phổ biến hơn (shared hosting) |
| SV FPT quen thuộc | Trung bình | Cao hơn |

🔴 **Bằng chứng thực nghiệm mạnh nhất [MÃ NGUỒN]:**
> **Cả Koha và LibreBooking đều là hệ thống đặt lịch trưởng thành, cả hai đều chạy MySQL, và cả hai đều KHÔNG có ràng buộc chống trùng lịch nào ở cấp cơ sở dữ liệu** — đã kiểm chứng bằng cách đọc trực tiếp `kohastructure.sql` và `create-schema.sql`. Cả hai buộc phải kiểm tra trùng lịch bằng code ứng dụng. **Đây không phải lựa chọn thiết kế của họ — đó là giới hạn của MySQL.**

👉 **QUYẾT ĐỊNH: PostgreSQL (bản 16 hoặc 17).** Đây là lý lẽ kỹ thuật cụ thể, có bằng chứng, chứ không phải "vì Postgres xịn hơn". **Rất ăn điểm khi bảo vệ.**

### 16.2. Next.js vs Laravel vs Go

**[REGISTRY]** Phiên bản mới nhất kiểm tra ngày 14/09/2026:
- `next` = **16.3.5** (phát hành 2026-09-11, MIT)
- `laravel/framework` = **v13.31.0** (2026-09-08, MIT)
- `prisma` = 8.0.0-rc.15 (2026-09-14) · `drizzle-orm` = 0.45.2 (2026-03-27) · `bullmq` = 6.3.6 (2026-09-14)

**[SNIPPET]** — Nguồn so sánh: [Next.js 15 vs Laravel: when to choose what in 2025 (nihardaily.com)](https://nihardaily.com/56-nextjs-15-vs-laravel-when-to-choose-what-in-2025) · [Laravel vs Next.js: Full-Stack Framework Showdown 2025 (Wishtree)](https://wishtreetech.com/blogs/tech-stack/laravel-vs-next-js-which-framework-should-you-choose-for-your-full-stack-web-app/) · [Best Web Frameworks 2026: 10 Compared (adriano-junior.com)](https://www.adriano-junior.com/best-web-frameworks-2026) · [Next.js vs Laravel for SaaS Development (getnextkit.com)](https://getnextkit.com/blog/next-js-vs-laravel-for-saas-development-a-developer-s-honest-comparison-2025) · [Next.js vs. Laravel: Which Framework Is Better in 2025? (VeltScale)](https://sveltelaunch.io/next-js-vs-laravel-which-framework-is-better-in-2025/)

Trích snippet đáng chú ý:
> *"Laravel is the fastest full-stack build with one developer and offers the strongest scalability-to-cost ratio for SMB web apps."*
> *"Laravel provides an unfair advantage for solo developers or small teams because they can move fast with built-in tools."*
> *"Next.js offers the fastest path to a production SaaS with a huge hiring pool and is the default pick for React-first teams."*
> *"A popular architecture in 2025 is using Laravel as the backend API and Next.js as the frontend."*

⚠️ **Không tìm được nguồn so sánh nào có Go** trong 3 vế. Phân tích Go dưới đây là **[SUY LUẬN]** của tôi.

### Bảng quyết định **[SUY LUẬN]**

| Tiêu chí (trọng số) | **Laravel 13 + Livewire** | **Next.js 16 + Drizzle/Prisma** | **Go + templ/HTMX** |
|---|---|---|---|
| Tốc độ ra MVP (⭐⭐⭐) | 🟢 **Rất nhanh** — có sẵn auth, migration, queue, mail, cron, admin | 🟡 Nhanh nếu đã quen React | 🔴 Chậm — phải tự viết nhiều |
| Hỗ trợ Postgres nâng cao (⭐⭐⭐) | 🟢 `DB::raw` dễ dùng cho `tstzrange`, migration `->rawIndex()` | 🟡 Prisma **chưa hỗ trợ tốt** range type & EXCLUDE → phải viết SQL thô trong migration | 🟢 `pgx` hỗ trợ range type native, kiểm soát tuyệt đối |
| SV FPT quen? (⭐⭐⭐) | 🟢 PHP/Laravel là môn học phổ biến ở FPT | 🟢 JS/React cũng rất phổ biến | 🔴 Ít SV học Go |
| State machine sẵn có (⭐⭐) | 🟢 `spatie/laravel-model-states` 2.14.2 | 🟡 XState 5.33.0 (nặng) hoặc tự viết | 🟡 `looplab/fsm` v1.0.4 |
| Job nền / cron (⭐⭐) | 🟢 Queue + Scheduler có sẵn | 🟡 Cần BullMQ + Redis, hoặc dịch vụ cron ngoài | 🟡 Tự viết goroutine |
| Hosting rẻ ở VN (⭐⭐) | 🟢 Chạy tốt trên VPS 1–2GB RAM | 🟡 Node ngốn RAM hơn | 🟢 Nhị phân đơn, RAM cực thấp |
| Bảng điều khiển admin (⭐⭐) | 🟢 Filament / Nova / Backpack có sẵn | 🔴 Phải tự dựng | 🔴 Phải tự dựng |
| SEO trang giới thiệu (⭐) | 🟢 Blade SSR | 🟢 SSR/SSG tốt nhất | 🟢 |
| Hiệu năng thô (⭐) | 🟡 | 🟡 | 🟢 |
| **TỔNG** | 🥇 **KHUYẾN NGHỊ** | 🥈 | 🥉 |

### 🎯 KHUYẾN NGHỊ CUỐI **[SUY LUẬN]**

```
Backend + Frontend : Laravel 13.x  (PHP 8.3+)
UI động            : Livewire 4  (hoặc Blade + Alpine.js nếu muốn nhẹ hơn)
CSDL               : PostgreSQL 16/17  + extension btree_gist
State machine      : spatie/laravel-model-states 2.14.2
Job nền + cron     : Laravel Queue (database driver — KHÔNG cần Redis cho MVP) + Scheduler
Admin panel        : Filament  (dựng CRUD kho máy trong vài giờ)
Lưu ảnh            : Cloudflare R2 hoặc thư mục local + backup (spatie/laravel-backup)
Thanh toán         : QR chuyển khoản (VietQR) cho MVP → VNPay/MoMo ở giai đoạn 2
Thông báo          : Email (SMTP) + Zalo OA / Zalo ZNS ở giai đoạn 2
Triển khai         : VPS Việt Nam (Ubuntu 22.04/24.04) + Nginx + Coolify hoặc deploy tay
```

**Ba lý do chốt [SUY LUẬN]:**
1. **Laravel là framework mà Snipe-IT dùng** (`laravel/framework ^12.0` — **[MÃ NGUỒN]**). Nhóm đọc mã nguồn Snipe-IT sẽ hiểu ngay và học được rất nhanh — một lợi thế học tập cụ thể.
2. **Rủi ro lớn nhất của đồ án SV là không kịp deadline**, không phải hiệu năng. Laravel tối đa hoá tốc độ ra sản phẩm.
3. **Vẫn dùng được đầy đủ sức mạnh PostgreSQL**: migration Laravel cho phép chạy SQL thô, nên `EXCLUDE USING gist` viết bình thường:
```php
// database/migrations/xxxx_add_exclude_constraint.php
public function up(): void
{
    DB::statement('CREATE EXTENSION IF NOT EXISTS btree_gist');
    DB::statement("
        ALTER TABLE rental_holds
        ADD CONSTRAINT rental_holds_no_overlap
        EXCLUDE USING gist (laptop_id WITH =, period WITH &&)
        WHERE (hold_state <> 'cancelled')
    ");
}
```

⚠️ **Nếu nhóm mạnh JS/React hơn PHP** thì chọn Next.js 16 vẫn hoàn toàn ổn — nhưng **dùng Drizzle ORM thay vì Prisma**, vì Prisma xử lý range type PostgreSQL kém hơn. **[SUY LUẬN — nhóm nên tự kiểm chứng tình trạng hỗ trợ range type của Prisma 8 tại thời điểm làm]**

### 16.3. Hosting — chi phí thật

**[SNIPPET]** — Nguồn: [Bảng giá thuê VPS 2025 — HostingViet](https://hostingviet.vn/chi-phi-thue-may-chu-ao-vps-bao-nhieu-tien-hien-nay) · [Thuê VPS Giá Rẻ — HostingViet](https://hostingviet.vn/en/cheap-vps) · [Cài Coolify trên VPS: self-host PaaS thay Heroku và Vercel (TND)](https://www.tnd.vn/cai-coolify-vps-self-host-paas-thay-heroku-12058/) · [Vercel Netlify Railway So Sánh Hosting Free (phamhai.com)](https://phamhai.com/vercel-netlify-railway-so-sanh-hosting-free/) · [Next.js Hosting Cost Calculator: Vercel vs VPS (temps.sh)](https://temps.sh/blog/nextjs-deployment-cost-calculator) · [Free Next.js Hosting Providers in 2025 (dev.to)](https://dev.to/joodi/free-nextjs-hosting-providers-in-2025-pros-and-cons-2a0e) · [Best Vercel Alternatives for Next.js Hosting in 2025 (DanubeData)](https://danubedata.ro/blog/best-vercel-alternatives-nextjs-hosting-2025)

| Phương án | Chi phí (theo snippet) | Nhãn | Ghi chú |
|---|---|---|---|
| **VPS Việt Nam (HostingViet)** | **từ 75.000 VNĐ/tháng**, có 3 ngày dùng thử miễn phí | **[SNIPPET — CẦN KIỂM CHỨNG]** | *"VPS from just 75,000₫/month with 3 days free trial"*. Độ trễ thấp cho người dùng VN. |
| Vercel Free (Hobby) | 100 GB băng thông/tháng, 6.000 phút build, 100 GB-giờ serverless | **[SNIPPET — CẦN KIỂM CHỨNG]** | Chỉ hợp Next.js; **không chạy được PostgreSQL**, phải thuê DB riêng |
| Netlify Free | 100 GB băng thông/tháng | **[SNIPPET]** | |
| Railway | **5 USD tín dụng dùng thử 30 ngày** (không có free tier vĩnh viễn) | **[SNIPPET — CẦN KIỂM CHỨNG]** | *"Railway offers $5 trial credit for 30 days instead of permanent free tier"* |
| Coolify tự host trên VPS | Rẻ hơn **50–70%** khi chạy nhiều app | **[SNIPPET — CẦN KIỂM CHỨNG]** | Snippet nêu Coolify *"offers latency advantages for Vietnam users"* |
| Oracle Cloud / Render free tier | Miễn phí (có giới hạn) | **[SNIPPET]** | *"not as instant as frontend hosting"* cho Laravel |

⚠️ **Toàn bộ giá trên chỉ từ snippet, CHƯA mở được trang.** Nhóm **bắt buộc** vào thẳng hostingviet.vn / vercel.com/pricing / railway.com để lấy giá thật tại thời điểm viết proposal.

### 🎯 Đề xuất chi phí hạ tầng cho proposal **[SUY LUẬN — dựa trên mức 75.000 VNĐ/tháng ở trên]**

| Hạng mục | Cấu hình | Chi phí/tháng (VNĐ) | Chi phí/năm (VNĐ) |
|---|---|---|---|
| VPS (app + PostgreSQL cùng máy) | 2 vCPU / 2–4 GB RAM / 40 GB SSD | 150.000 – 300.000 | 1.800.000 – 3.600.000 |
| Tên miền `.com` hoặc `.vn` | | ~25.000 – 70.000 | 300.000 – 850.000 |
| Chứng chỉ SSL | Let's Encrypt | **0** | **0** |
| Lưu ảnh (Cloudflare R2) | < 10 GB | ~0 (trong free tier) | ~0 |
| Email giao dịch | Resend/Brevo free tier hoặc SMTP Gmail | 0 – 100.000 | 0 – 1.200.000 |
| Sao lưu ra ngoài | Google Drive / R2 | ~0 | ~0 |
| **TỔNG dự kiến** | | **≈ 175.000 – 470.000** | **≈ 2.100.000 – 5.650.000** |

👉 **So sánh với EZRentOut** (~50 USD/tháng ≈ 1.300.000 VNĐ/tháng ≈ **15.600.000 VNĐ/năm**): tự xây **tiết kiệm khoảng 10–13,5 triệu VNĐ/năm**. **[SUY LUẬN — cần kiểm chứng lại tỉ giá USD/VNĐ và giá EZRentOut thật]**
⚠️ **Nhưng phải trung thực trong proposal:** con số này **chưa tính chi phí cơ hội thời gian** của nhóm (ước ~200–400 giờ phát triển). Với đồ án môn Khởi nghiệp thì thời gian đó là **học phí đã trả**, nhưng nếu tính theo giá thị trường thì tự xây **không** rẻ hơn.

### 16.4. Ba rủi ro kỹ thuật phải nêu trong proposal **[SUY LUẬN]**

| Rủi ro | Mức độ | Giảm thiểu |
|---|---|---|
| **VPS chết đúng mùa thi** — cao điểm mà web sập là mất khách | 🔴 Cao | Sao lưu DB **hằng ngày** ra Google Drive/R2; có **quy trình dự phòng thủ công** (Google Sheet + Zalo) để vẫn nhận đơn được |
| **Mất dữ liệu do lỗi** | 🟠 Trung bình | `pg_dump` tự động + audit log append-only; test khôi phục ít nhất 1 lần trước khi vận hành |
| **Nhóm không kịp deadline** | 🔴 Cao | Cắt phạm vi: MVP **chỉ cần** đặt lịch + chống trùng + biên bản bàn giao. Thanh toán online, app di động, sub-rental để giai đoạn 2 |

---

## 17. SCHEMA ĐỀ XUẤT ĐẦY ĐỦ (tổng hợp mọi mục trên)

**[SUY LUẬN — tổng hợp từ Snipe-IT (assets/status/log), Koha (bookings/issues), LibreBooking (resource rules), Odoo (pricing/security time)]**

```
┌────────────────────┐        ┌──────────────────────┐
│ laptop_categories  │        │ laptop_status_labels │   ← mô hình 3 cờ của Snipe-IT
│ id, name           │        │ id, name, color      │
└─────────┬──────────┘        │ deployable  bool     │
          │                   │ pending     bool     │
          ▼                   │ archived    bool     │
┌────────────────────┐        │ default_label bool   │
│ laptop_models      │  LOẠI  └──────────┬───────────┘
│ id, category_id    │                   │
│ name, model_number │                   │
│ manufacturer       │                   │
│ cpu, ram_gb        │                   │
│ os_version         │                   │
│ min_amt (ngưỡng)   │                   │
│ base_price_per_day │                   │
└─────────┬──────────┘                   │
          │                              │
          ▼                              ▼
┌─────────────────────────────────────────────────────┐
│ laptops                              CÁ THỂ (serial)│
│ id, model_id, status_label_id                       │
│ asset_tag UNIQUE, serial_number UNIQUE              │
│ condition_grade, battery_health_pct                 │
│ eos_installed bool, seb_tested_at timestamptz       │  ← ĐẶC THÙ DỰ ÁN
│ purchase_date, purchase_cost (VNĐ)                  │
│ checkout_counter int, total_rented_hours numeric    │  ← để cân bằng tải
│ last_audit_date, next_audit_date                    │  ← kiểm kê, mẫu Snipe-IT
│ location, notes, created_at, updated_at, deleted_at │
└─────────┬───────────────────────────────────────────┘
          │
          ▼
┌───────────────────────────────────────────────────────────────┐
│ rental_holds            ★ BẢNG CHỐNG TRÙNG LỊCH ★             │
│ id, rental_id, laptop_id                                      │
│ period tstzrange   (đã cộng buffer / "Security Time")         │
│ hold_state ('active'|'cancelled'), expires_at                 │
│ assignment_mode ('by_model'|'specific_unit')   ← mẫu Koha     │
│ EXCLUDE USING gist (laptop_id WITH =, period WITH &&)         │
│     WHERE (hold_state <> 'cancelled')                         │
└─────────┬─────────────────────────────────────────────────────┘
          │
          ▼
┌──────────────────────┐      ┌─────────────────────┐
│ rentals              │─────▶│ customers           │
│ id, code UNIQUE      │      │ id, full_name, phone│
│ customer_id          │      │ email, student_id   │
│ state (FSM 11 giá trị)│      │ id_card_number      │
│ deposit_amount VNĐ   │      │ id_card_photo_url   │
│ total_amount   VNĐ   │      │ trust_score         │
│ created_at           │      └─────────────────────┘
└─────────┬────────────┘
          │
    ┌─────┴──────┬──────────────┬──────────────┐
    ▼            ▼              ▼              ▼
┌─────────┐ ┌──────────┐ ┌─────────────┐ ┌──────────────────┐
│checkouts│ │payments  │ │custody_      │ │rental_state_log  │
│(giao máy│ │+ payment_│ │events        │ │from_state        │
│ thật)   │ │  events  │ │(ảnh, chữ ký,│ │to_state, event   │
│UNIQUE   │ │UNIQUE    │ │ phụ kiện)   │ │actor_id, reason  │
│(laptop) │ │(provider,│ └─────────────┘ └──────────────────┘
│ ← Koha  │ │ txn_id)  │
└─────────┘ └──────────┘

  + audit_log        (append-only, hash chain, trigger chặn UPDATE/DELETE)
  + idempotency_keys (UNIQUE(user_id, key))
  + outbox_messages  (gửi mail/Zalo tin cậy)
```

**Danh sách bảng — 15 bảng cho MVP:**

| # | Bảng | Vai trò | Mẫu tham chiếu |
|---|---|---|---|
| 1 | `laptop_categories` | Phân loại cấp cao | Snipe-IT `categories` |
| 2 | `laptop_models` | **LOẠI** máy | Snipe-IT `models` |
| 3 | `laptop_status_labels` | Nhãn trạng thái 3 cờ | Snipe-IT `status_labels` |
| 4 | `laptops` | **CÁ THỂ** có serial | Snipe-IT `assets` + Koha `items` |
| 5 | `customers` | Khách thuê | — |
| 6 | `rentals` | Đơn thuê (header + FSM) | Koha `bookings` |
| 7 | **`rental_holds`** | **Giữ chỗ theo thời gian — EXCLUDE** | Koha `bookings` + Postgres |
| 8 | `checkouts` | Giao máy thật (UNIQUE laptop_id) | Koha `issues` |
| 9 | `custody_events` | Bàn giao có ảnh + chữ ký | Snipe-IT `checkout_acceptances` |
| 10 | `payments` | Cọc & thanh toán (VNĐ) | — |
| 11 | `payment_events` | Webhook cổng TT (UNIQUE txn) | — |
| 12 | `idempotency_keys` | Chống bấm 2 lần | Stripe/brandur |
| 13 | `rental_state_log` | Lịch sử chuyển trạng thái | — |
| 14 | `audit_log` | Append-only + hash chain | Snipe-IT `action_logs` (cải tiến) |
| 15 | `outbox_messages` | Gửi thông báo tin cậy | Outbox pattern |

**Truy vấn cốt lõi: "loại máy nào còn rảnh khung giờ này"** **[SUY LUẬN]**
```sql
SELECT m.id, m.name, count(l.id) AS so_may_ranh
FROM laptop_models m
JOIN laptops l ON l.model_id = m.id
JOIN laptop_status_labels s ON s.id = l.status_label_id
WHERE l.deleted_at IS NULL
  AND s.deployable = true AND s.archived = false
  AND NOT EXISTS (
      SELECT 1 FROM rental_holds h
      WHERE h.laptop_id = l.id
        AND h.hold_state = 'active'
        AND h.period && tstzrange($1::timestamptz, $2::timestamptz, '[)')
  )
GROUP BY m.id, m.name
HAVING count(l.id) > 0
ORDER BY m.name;
```
*(Chỉ mục GiST tạo cho `EXCLUDE` cũng phục vụ luôn truy vấn này → không cần chỉ mục thêm.)*

---

## 18. CHECKLIST KIỂM CHỨNG BẮT BUỘC CHO NHÓM SINH VIÊN

> **Đây là danh sách những thứ tôi KHÔNG mở được trang gốc hoặc KHÔNG chắc chắn. Nhóm phải tự kiểm tra trước khi đưa vào proposal.**

### 18.1. Số liệu từ snippet — phải mở link xác minh

| # | Số liệu / khẳng định | Nguồn cần mở | Vì sao quan trọng |
|---|---|---|---|
| 1 | Công suất khách sạn *"climbing upwards of 80 percent or higher"* khi bán theo hạng phòng | [hospitalitynet.org/opinion/4074675.html](https://www.hospitalitynet.org/opinion/4074675.html) | Là con số duy nhất định lượng lợi ích của inventory pooling trong file này |
| 2 | Stripe giữ idempotency key **24 giờ** | [stripe.com/blog/idempotency](https://stripe.com/blog/idempotency) | Quyết định TTL bảng `idempotency_keys` |
| 3 | Bảng khử trùng lặp thêm **< 2 ms/request** | (nguồn snippet chưa rõ trang chính xác) | Dùng để biện luận "chi phí không đáng kể" |
| 4 | EZRentOut **50 USD / 2 người dùng / tháng** | [ezo.io/ezrentout/pricing](https://ezo.io/ezrentout/pricing/) | Là mốc so sánh chi phí "mua vs tự xây" |
| 5 | VPS HostingViet **từ 75.000 VNĐ/tháng** | [hostingviet.vn/chi-phi-thue-may-chu-ao-vps-bao-nhieu-tien-hien-nay](https://hostingviet.vn/chi-phi-thue-may-chu-ao-vps-bao-nhieu-tien-hien-nay) | Toàn bộ bảng chi phí hạ tầng dựa vào đây |
| 6 | Vercel Free: 100 GB băng thông, 6.000 phút build, 100 GB-giờ | vercel.com/pricing | Nếu chọn Next.js |
| 7 | Railway: 5 USD tín dụng 30 ngày, không có free tier vĩnh viễn | railway.com/pricing | |
| 8 | Coolify rẻ hơn **50–70%** | [tnd.vn/cai-coolify-vps-self-host-paas-thay-heroku-12058](https://www.tnd.vn/cai-coolify-vps-self-host-paas-thay-heroku-12058/) | |
| 9 | Lịch retry webhook 1'/2'/4'/8' và backoff có jitter | [matheuspalma.com/blog/outbound-webhook-delivery-signing-retries-dead-letters](https://matheuspalma.com/blog/outbound-webhook-delivery-signing-retries-dead-letters) | |
| 10 | Tỉ giá USD/VNĐ dùng để quy đổi | vietcombank.com.vn hoặc SBV | Mọi con số quy đổi trong file này |

### 18.2. Kỹ thuật — phải tự chạy thử để xác nhận

| # | Việc cần làm | Cách kiểm tra |
|---|---|---|
| 1 | `EXCLUDE USING gist` chặn thật hai INSERT chồng lịch | Mở 2 phiên `psql`, cả hai `BEGIN`, cùng INSERT khoảng thời gian giao nhau, xem phiên thứ hai có lỗi không |
| 2 | Mã lỗi PostgreSQL khi vi phạm EXCLUDE có đúng là **`23P01`** không | Bắt exception và in `SQLSTATE` ra |
| 3 | Ngữ nghĩa biên `[)` của `tstzrange` | `SELECT tstzrange('2026-09-20 08:00+07','2026-09-20 12:00+07') && tstzrange('2026-09-20 12:00+07','2026-09-20 16:00+07');` → kỳ vọng `false` |
| 4 | `btree_gist` có sẵn trên VPS/hosting đã chọn không | `CREATE EXTENSION IF NOT EXISTS btree_gist;` — một số hosting quản trị hạn chế extension |
| 5 | Phiên bản PostgreSQL nhà cung cấp hỗ trợ | `SELECT version();` |
| 6 | `FOR UPDATE SKIP LOCKED` hoạt động như mong đợi | Chạy 2 phiên song song, xem có lấy 2 máy khác nhau không |
| 7 | Prisma (nếu chọn Next.js) có xử lý được `tstzrange` không | Thử tạo model có cột range; nếu không, dùng Drizzle hoặc `$queryRaw` |
| 8 | Trigger chặn UPDATE/DELETE trên `audit_log` hoạt động | Thử `UPDATE audit_log SET note='x' WHERE seq=1;` → phải báo lỗi |

### 18.3. Nghiệp vụ — cần khảo sát thực tế, không tra web được

| # | Câu hỏi | Ai trả lời |
|---|---|---|
| 1 | Số ca thi/ngày và khung giờ ca thi thực tế ở FPT ĐN | Phòng khảo thí / lịch thi công khai |
| 2 | Thời gian thật để cài + kiểm tra EOS + Safe Exam Browser trên 1 máy sạch → quyết định **Security Time** | Nhóm tự bấm giờ làm thử |
| 3 | Giá thuê hợp lý (VNĐ/ca, VNĐ/ngày) | Khảo sát SV + đối chiếu file nghiên cứu giá |
| 4 | Mức cọc chấp nhận được (VNĐ) và hình thức đảm bảo (CCCD/thẻ SV) | Khảo sát + tham khảo tiệm cho thuê khác |
| 5 | Có được đặt bàn giao máy trong khuôn viên trường không | Phòng Công tác sinh viên |
| 6 | Tỉ lệ máy hỏng thực tế theo tháng | Chỉ biết sau khi vận hành — đặt giả định và ghi rõ là giả định |

---

## 19. TỔNG HỢP NGUỒN

### 19.1. Mã nguồn / schema đã TẢI VÀ ĐỌC TRỰC TIẾP (độ tin cậy cao nhất)

| Nguồn | URL | Ghi chú |
|---|---|---|
| Snipe-IT — repo chính | https://github.com/grokability/snipe-it | Clone tại commit `16362cc6a5cf54a77acbb0ab3cbaac79b75d85f6` (13/09/2026), v8.7.2 |
| Snipe-IT — `Asset.php` | https://raw.githubusercontent.com/grokability/snipe-it/master/app/Models/Asset.php | 2.340 dòng |
| Snipe-IT — `Statuslabel.php` | https://raw.githubusercontent.com/grokability/snipe-it/master/app/Models/Statuslabel.php | 242 dòng |
| Snipe-IT — `Actionlog.php` | https://raw.githubusercontent.com/grokability/snipe-it/master/app/Models/Actionlog.php | 728 dòng |
| Snipe-IT — `AssetModel.php` | https://raw.githubusercontent.com/grokability/snipe-it/master/app/Models/AssetModel.php | 473 dòng |
| Snipe-IT — `composer.json` | https://raw.githubusercontent.com/grokability/snipe-it/master/composer.json | Giấy phép + yêu cầu PHP |
| Snipe-IT — migration `assets` | https://github.com/grokability/snipe-it/blob/master/database/migrations/2013_11_15_190327_create_assets_table.php | |
| Snipe-IT — migration `action_logs` | https://github.com/grokability/snipe-it/blob/master/database/migrations/2016_09_04_180400_create_actionlog_table.php | |
| Snipe-IT — migration `checkout_requests` | https://github.com/grokability/snipe-it/blob/master/database/migrations/2016_09_02_001448_create_checkout_requests_table.php | **Bằng chứng không có start/end date** |
| Snipe-IT — migration `checkout_acceptances` | https://github.com/grokability/snipe-it/blob/master/database/migrations/2018_07_28_023826_create_checkout_acceptances_table.php | Chữ ký điện tử |
| Snipe-IT — thư mục migrations | https://github.com/grokability/snipe-it/tree/master/database/migrations | 484 file |
| **Koha — schema đầy đủ** | https://raw.githubusercontent.com/Koha-Community/Koha/master/installer/data/mysql/kohastructure.sql | 413.576 bytes; nguồn của `bookings`/`reserves`/`issues`/`items` |
| Koha — repo | https://github.com/Koha-Community/Koha | |
| **LibreBooking — schema** | https://raw.githubusercontent.com/LibreBooking/app/master/database_schema/create-schema.sql | 14.163 bytes |
| LibreBooking — README | https://raw.githubusercontent.com/LibreBooking/app/master/README.md | Giấy phép GPLv3, PHP 8.1+, MySQL 5.5+, tình trạng dự án |
| LibreBooking — hướng dẫn cài | https://raw.githubusercontent.com/LibreBooking/app/master/doc/INSTALLATION.md | |
| LibreBooking — repo | https://github.com/LibreBooking/app | |

### 19.2. Registry gói (phiên bản & ngày phát hành là thật, kiểm tra 14/09/2026)

`registry.npmjs.org`: `xstate` 5.33.0 (2026-09-12, MIT) · `robot3` 1.2.0 (2025-09-20, BSD-2-Clause) · `next` 16.3.5 (2026-09-11, MIT) · `prisma` 8.0.0-rc.15 (2026-09-14) · `drizzle-orm` 0.45.2 (2026-03-27) · `bullmq` 6.3.6 (2026-09-14)
`repo.packagist.org`: `laravel/framework` v13.31.0 (2026-09-08, MIT) · `spatie/laravel-model-states` 2.14.2 (2026-07-22, MIT) · `spatie/laravel-activitylog` 5.1.1 (2026-09-08, MIT) · `owen-it/laravel-auditing` v14.0.6 (2026-06-20, MIT)
`pypi.org`: `transitions` 0.9.3 (MIT) — https://github.com/pytransitions/transitions
`proxy.golang.org`: `github.com/looplab/fsm` v1.0.4 (2026-08-27)

### 19.3. Nguồn CHỈ ĐỌC ĐƯỢC SNIPPET (⚠️ nhóm phải tự mở kiểm chứng)

**PostgreSQL EXCLUDE / range types**
- https://chat2db.ai/resources/blog/postgres-exclusion-constraints-guide
- https://dev.to/akincskn/i-solved-double-booking-without-locks-using-one-postgresql-constraint-209m
- https://dev.to/franckpachot/postgresql-exclude-constraints-for-better-concurrency-than-serializable-pob
- https://www.jusdb.com/blog/postgresql-range-types-exclusion-constraints
- https://www.red-gate.com/simple-talk/databases/postgresql/overlapping-ranges-in-subsets-in-postgresql/
- https://amitavroy.com/articles/postgresql-gist-exclusion-constraintthe-database-evel-answer-to-double-bookings
- https://blog.danielclayton.co.uk/posts/overlapping-data-postgres-exclusion-constraints/
- https://java-jedi.medium.com/exclusion-constraints-b2cbd62b637a
- https://vikulin-va.ru/en/postgres/arrays-ranges/

**Khoá bi quan / lạc quan**
- https://medium.com/@niketl16/when-millions-click-at-once-how-pessimistic-locking-prevents-double-booking-in-high-traffic-2e9d3b109b19
- https://medium.com/javarevisited/booking-system-with-pessimistic-locks-4ec107e4bd5
- https://oneuptime.com/blog/post/2026-01-30-pessimistic-locking-implementation/view
- https://adamdjellouli.com/articles/databases_notes/07_concurrency_control/04_double_booking_problem
- https://clixo.sh/blog/prevent-double-booking-concurrent-reservation-requests
- https://brijesh.work/system-design/booking-management/
- https://dev.to/iprajapatiparesh/stop-double-booking-optimistic-locking-in-laravel-j5n
- https://dev.to/jacktt/optimistic-lock-pessimistic-lock-4h36
- https://flylib.com/books/en/2.196.1/hack_66_use_optimistic_locking.html

**Redis lock / inventory reservation**
- https://redis.io/tutorials/inventory-reservation-in-real-time-with-redis/
- https://oneuptime.com/blog/post/2026-03-31-redis-booking-lock-system/view
- https://oneuptime.com/blog/post/2026-03-31-redis-how-to-model-bookingreservation-systems-in-redis/view
- https://oneuptime.com/blog/post/2026-01-21-redis-distributed-locks/view
- https://engineeringatscale.substack.com/p/redis-distributed-locks-explained
- https://dev.to/abhivyaktii/building-a-scalable-slot-booking-system-with-redis-distributed-locks-4cf8
- https://medium.com/@cgorale111/avoiding-double-booking-with-redis-aca66fefcce3

**Idempotency / webhook / outbox**
- https://stripe.com/blog/idempotency ← **ưu tiên đọc**
- https://brandur.org/idempotency-keys ← **ưu tiên đọc**
- https://httptoolkit.com/blog/idempotency-keys/
- https://newsletter.systemdesign.one/p/idempotent-api
- https://arpit.substack.com/p/designing-idempotent-payment-apis
- https://simplico.net/2026/04/04/idempotency-in-payment-apis-prevent-double-charges-with-stripe-omise-and-2c2p/
- https://medium.com/@akash22675/designing-idempotent-api-endpoints-for-payments-16845cc1079e
- https://www.kore1.com/idempotency-integration-design/
- https://milanjovanovic.tech/blog/implementing-the-outbox-pattern
- https://www.glukhov.org/app-architecture/integration-patterns/transactional-outbox-pattern-go/
- https://www.npmjs.com/package/pg-transactional-outbox
- https://github.com/Zehelein/pg-transactional-outbox
- https://github.com/zeybek/ulak
- https://appmaster.io/blog/outbox-pattern-postgresql-integrations
- https://matheuspalma.com/blog/outbound-webhook-delivery-signing-retries-dead-letters
- https://www.educative.io/blog/webhook-system-design
- https://dev.to/sagarmaheshwary/transactional-outbox-with-rabbitmq-part-1-building-reliable-event-publishing-in-microservices-2of

**Saga**
- https://microservices.io/patterns/data/saga.html
- https://temporal.io/blog/mastering-saga-patterns-for-distributed-transactions-in-microservices
- https://orkes.io/blog/saga-pattern-in-distributed-systems
- https://dev.to/airtruffle/event-driven-microservices-for-booking-systems-saga-patterns-and-eventual-consistency-in-travel-5g9i
- https://oneuptime.com/blog/post/2026-02-20-microservices-saga-pattern/view
- https://www.systemdesignacademy.com/blog/saga-pattern-distributed-transactions
- https://thecodeman.net/posts/saga-orchestration-pattern

**Mô hình inventory: khách sạn & cho thuê xe**
- https://www.hospitalitynet.org/opinion/4074675.html
- https://www.hotel-online.com/news/when-it-comes-to-room-assignments-details-matter
- https://bytebytego.com/courses/system-design-interview/hotel-reservation-system
- https://dev.to/sumedhbala/hotel-booking-schema-design-comparison-g3h
- https://checklist.com/hotel/front-office/room-assignment
- https://www.altexsoft.com/blog/car-rental-reservation-system/
- https://www.nomora.io/blog/vehicle-reservation-system-guide-car-rental-businesses
- https://github.com/ggeop/Rental-Car-Company-SQL
- https://github.com/evagian/car-rental-database-sql-
- https://patents.google.com/patent/US8160906

**State machine**
- https://stately.ai/docs/xstate
- https://stately.ai/docs/machines
- https://github.com/statelyai/xstate
- https://xstate.js.org/
- https://dev.to/gabrielanhaia/state-machines-in-typescript-a-60-line-type-safe-engine-1jbf
- https://dev.to/ibedwi/create-a-finite-state-machine-using-xstate-4g71

**Snipe-IT (tài liệu, không phải mã nguồn)**
- https://snipeitapp.com/ · https://snipeitapp.com/product · https://snipeitapp.com/faq
- https://snipe-it.readme.io/docs/overview · https://snipe-it.readme.io/docs/architecture · https://snipe-it.readme.io/docs/managing-assets · https://snipe-it.readme.io/docs/importing-assets
- https://deepwiki.com/grokability/snipe-it/2.3-asset-models-and-relationships
- https://deepwiki.com/grokability/snipe-it/2.5-asset-checkout-and-checkin
- https://deepwiki.com/grokability/snipe-it/4.4-activity-logging
- https://drawsql.app/templates/snipe-it (sơ đồ ERD trực quan — rất tiện để chèn vào proposal)
- http://snipe.github.io/snipe-it-devdocs/class_app_1_1_models_1_1_asset.html
- https://railway.com/deploy/snipe-it (deploy 1 chạm để dùng thử)

**Các hệ mở / thương mại khác**
- https://www.springshare.com/libcal · https://www.springshare.com/academic-libraries/libcal
- https://edgeryders.eu/t/list-open-source-software-for-resource-scheduling-and-booking/6629
- https://www.booknetic.com/blog/best-open-source-scheduling-software
- https://depts.washington.edu/sociolab/labfacilities/equipmentguide.php
- https://www.odoo.com/documentation/18.0/applications/sales/rental.html
- https://www.odoo.com/documentation/17.0/applications/sales/rental.html
- https://www.odoo.com/documentation/19.0/applications/sales/rental.html
- https://www.odoo.com/app/rental-features
- https://www.erpgap.com/blog/exploring-rental-module-odoo-18
- https://ezo.io/ezrentout/ · https://ezo.io/ezrentout/pricing/
- https://www.capterra.com/p/134914/EZRentOut/ · https://www.getapp.com/industries-software/a/ezrentout/ · https://softwareconnect.com/reviews/ezrentout/
- https://rentman.io/solutions/rental-equipment-tracking-software

**Audit log bất biến**
- https://tracehold.ai/blog/immutable-audit-log-hmac-hash-chain/
- https://www.designgurus.io/answers/detail/how-do-you-enforce-immutability-and-appendonly-audit-trails
- https://aesirx.io/blog/compliance-one/immutable-audit-trails-when-your-audit-log-becomes-cryptographic-proof
- https://medium.com/@veritaschain/append-only-is-the-easy-part-e25820208213
- https://dev.to/codemalasartes/an-immutable-audit-trail-for-ai-agent-actions-fastapi-async-sqlalchemy-4m4c
- https://www.emergentmind.com/topics/immutable-audit-log
- https://www.locatorx.com/blog/the-truth-about-asset-records-why-immutability-is-the-foundation-of-a-verifiable-chain-of-custody

**Stack & hosting**
- https://nihardaily.com/56-nextjs-15-vs-laravel-when-to-choose-what-in-2025
- https://wishtreetech.com/blogs/tech-stack/laravel-vs-next-js-which-framework-should-you-choose-for-your-full-stack-web-app/
- https://www.adriano-junior.com/best-web-frameworks-2026
- https://getnextkit.com/blog/next-js-vs-laravel-for-saas-development-a-developer-s-honest-comparison-2025
- https://sveltelaunch.io/next-js-vs-laravel-which-framework-is-better-in-2025/
- https://hostingviet.vn/chi-phi-thue-may-chu-ao-vps-bao-nhieu-tien-hien-nay · https://hostingviet.vn/en/cheap-vps
- https://www.tnd.vn/cai-coolify-vps-self-host-paas-thay-heroku-12058/
- https://phamhai.com/vercel-netlify-railway-so-sanh-hosting-free/
- https://temps.sh/blog/nextjs-deployment-cost-calculator
- https://danubedata.ro/blog/best-vercel-alternatives-nextjs-hosting-2025
- https://dev.to/joodi/free-nextjs-hosting-providers-in-2025-pros-and-cons-2a0e

---

## 20. NHỮNG ĐIỀU TÔI KHÔNG TÌM ĐƯỢC / KHÔNG CHẮC CHẮN

1. **Không mở được tài liệu chính thức PostgreSQL** (postgresql.org bị chặn) → mọi khẳng định về cú pháp `EXCLUDE`, `SKIP LOCKED`, mã lỗi `23P01`, ngữ nghĩa biên `[)` **cần nhóm tự kiểm chứng bằng cách chạy thử**.
2. **Không tìm được nguồn so sánh Go vs Laravel vs Next.js** trong cùng một bài. Phần đánh giá Go là suy luận của tôi.
3. **Không tìm được giá công khai của LibCal.**
4. **Không xác minh được** module Rental của Odoo có trong bản Community hay chỉ Enterprise.
5. **Không tìm được benchmark hiệu năng** của `EXCLUDE USING gist` ở quy mô lớn — nhưng với 15–40 máy thì hoàn toàn không phải vấn đề.
6. **Không tìm được ví dụ mã nguồn mở thực tế** nào dùng `EXCLUDE` cho thuê thiết bị (chỉ có bài blog). Đây là khoảng trống — nhóm có thể coi đó là điểm mới của mình.
7. **Không tìm được số liệu thị trường cho thuê laptop tại Việt Nam/Đà Nẵng** trong phạm vi nhiệm vụ này (thuộc file nghiên cứu khác).
8. **Snipe-IT có API REST** (`laravel/passport ^12.0` trong composer.json) nhưng **tôi chưa đọc tài liệu endpoint cụ thể** — nếu nhóm định tích hợp Snipe-IT làm hệ quản lý kho phía sau thì cần nghiên cứu thêm tại https://snipe-it.readme.io/.
9. **Số dòng/số sao GitHub của các repo** không lấy được (GitHub API bị chặn cho session này) — chỉ có phiên bản và commit hash.
10. **Chi phí cơ hội thời gian phát triển** (ước 200–400 giờ) là **con số tôi đoán**, chưa có căn cứ. Nhóm nên tự ước lượng dựa trên năng lực thật.

---

*Kết thúc file nghiên cứu 09. Soạn ngày 14/09/2026.*
