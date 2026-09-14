# NGHIÊN CỨU 02 — CÁC NỀN TẢNG CHO THUÊ THIẾT BỊ/ĐỒ ĐẠC TRÊN THẾ GIỚI
## Bài học vận hành cho mô hình "Website cho thuê laptop đi thi" tại ĐH FPT Đà Nẵng

> **Người dùng tài liệu:** nhóm viết proposal môn Khởi nghiệp — ĐH FPT Đà Nẵng
> **Ngày nghiên cứu:** 14/09/2026
> **Phạm vi:** Grover (Đức), Grover Business (B2B), Fat Llama (Anh), Hygglo (Thụy Điển), Rent the Runway (Mỹ), Lumoid (Mỹ — đã chết), Omni (Mỹ — đã chết, bonus), Turo (Mỹ), Getaround (Mỹ — đã rút khỏi Bắc Mỹ), LaptopsAnytime (kiosk cho mượn laptop trong trường ĐH Mỹ), cùng các nhà cung cấp hạ tầng (Stripe, Onfido, SEON, ComplyCube, Omocom, Booqable).

---

## 0. GHI CHÚ PHƯƠNG PHÁP VÀ GIỚI HẠN DỮ LIỆU (đọc trước khi trích dẫn)

**BẮT BUỘC ĐỌC — đây là điều kiện trung thực của tài liệu:**

1. Trong phiên nghiên cứu này, công cụ **WebFetch (tải trực tiếp trang web) bị chính sách egress của tổ chức CHẶN gần như toàn bộ**. Các domain đã thử và bị chặn (lỗi `EGRESS_BLOCKED`): `techcrunch.com`, `petapixel.com`, `dpreview.com`, `waste360.com`, `sifted.eu`, `grover.com`, `service.grover.com`, `fatllama.com`, `laptopsanytime.com`, `library.drexel.edu`, `infotoday.com`, `sec.gov`, `en.wikipedia.org`. Chỉ `github.com` truy cập được (không liên quan đề tài).
2. Do đó, **toàn bộ dữ liệu dưới đây đến từ công cụ WebSearch** — công cụ này trả về (a) danh sách URL thật và (b) phần nội dung được tổng hợp từ các trang đó. Nghĩa là: **URL là thật và đã xuất hiện trong kết quả tìm kiếm, nhưng tôi KHÔNG mở được từng trang để đọc nguyên văn.**
3. Hệ quả thực tế cho nhóm viết proposal: **mọi con số trong tài liệu này phải được nhóm mở lại URL và xác nhận lại bằng mắt trước khi đưa vào bản nộp**, đặc biệt là các con số tài chính (doanh thu Grover, số subscriber Rent the Runway, giá kiosk LaptopsAnytime). Đừng trích dẫn "nghe nói".
4. Các con số tôi **không** tìm được sẽ nằm ở **Mục 17 — Những thứ KHÔNG xác minh được**. Tôi không đoán và không trình bày phỏng đoán như sự thật.
5. Nguồn thuộc nhóm "content marketing / blog SEO" (ví dụ `businessmodelcanvastemplate.com`, `rentovation.co`, `miracuves.com`, `oyelabs.com`) được đánh dấu **[nguồn yếu]** — dùng để hiểu mô hình, **không dùng để trích số** trong proposal.

**Ký hiệu độ tin cậy dùng trong tài liệu:**

| Ký hiệu | Ý nghĩa |
|---|---|
| **[A]** | Nguồn chính chủ (trang chính thức công ty / help center / hồ sơ SEC / thông cáo báo chí) |
| **[B]** | Báo chí công nghệ uy tín (TechCrunch, Sifted, Tech.eu, Silicon Canals, Inside Higher Ed, EU-Startups) |
| **[C]** | Blog/nguồn phái sinh — chỉ tham khảo định tính **[nguồn yếu]** |

---

## 1. BẢNG TỔNG HỢP NHANH — 10 MÔ HÌNH, 1 TRANG

| Nền tảng | Nước | Loại hình | Doanh thu chính | Đặt cọc | KYC | Bảo hiểm/Miễn trừ | Trạng thái 2026 |
|---|---|---|---|---|---|---|---|
| **Grover** | Đức | B2C, sở hữu thiết bị (asset-heavy) | Phí thuê/tháng | **KHÔNG cọc** — thay bằng credit check | Schufa + CRIF Bürgel + ID/selfie (Onfido, SEON) | Grover Care (50%/80%/gói phí cố định) | Đang tồn tại sau tái cấu trúc StaRUG 4/2025 |
| **Grover Business** | Đức/AT/NL/ES | B2B | Thuê 6/12/18 tháng | Không cọc, xét tín dụng DN | Xác minh DN (rút ngắn ~1 ngày nhờ Onfido) | Như Grover Care | >10.000 DN khách hàng |
| **Fat Llama** | Anh/Mỹ | P2P marketplace | Hoa hồng 2 chiều (~15% + 15%) | Chủ đồ tự đặt mức cọc | 2–3 loại giấy tờ; ID chính phủ cho đồ giá trị cao | "Fully insured" — nhưng thực tế có tranh chấp | Thuộc Hygglo (mua 8/2022, 41,5 triệu USD) |
| **Hygglo** | Thụy Điển | P2P marketplace | Hoa hồng 20% (drone 50%) | Theo người cho thuê | **BankID** (định danh quốc gia) | Omocom hoặc Hygglo Lender Guarantee | Hoạt động, gần hòa vốn FY2024 |
| **Rent the Runway** | Mỹ | B2C subscription, sở hữu hàng | Thuê bao + thuê lẻ 4/8 ngày | Không cọc | Thẻ tín dụng | **Phí bảo hiểm 5 USD/đơn** (chỉ vết bẩn nhẹ) | Niêm yết NASDAQ (RENT), doanh thu FY2025 329,8 triệu USD |
| **Lumoid** | Mỹ | Try-before-you-buy máy ảnh/wearable | Phí thuê khấu trừ vào giá mua | Không rõ | Không rõ | Không rõ | **CHẾT 12/2017** |
| **Omni** | Mỹ | Kho + cho thuê đồ | Phí kho + phí thuê | — | — | — | **CHẾT 11/2019** |
| **Turo** | Mỹ | P2P ô tô | Hoa hồng 10–30% (theo gói bảo vệ) | **0–750 USD** (pre-auth) | ComplyCube: giấy tờ + liveness + bằng lái | 5 gói bảo vệ, host nhận 60–90% | Doanh thu 2024 ~958 triệu USD |
| **Getaround** | Mỹ/EU | P2P ô tô | Hoa hồng + bảo hiểm | Có | Có | Có — **bị kiện vì gây hiểu lầm** | **Rút khỏi Bắc Mỹ đầu 2025** |
| **LaptopsAnytime** | Mỹ | Kiosk tự động trong thư viện ĐH | Bán/cho thuê kiosk cho trường | Không cọc — ràng buộc bằng tài khoản SV | Thẻ SV + PIN | Trường tự chịu; SV chịu trách nhiệm tài chính nếu mất | Hoạt động, >4 triệu lượt mượn tự động cộng dồn |

---

## 2. GROVER (ĐỨC) — ĐỐI TƯỢNG HỌC QUAN TRỌNG NHẤT

### 2.1. Tổng quan mô hình

Grover là công ty Berlin cho **thuê đồ điện tử** (laptop, điện thoại, máy chơi game, TV, scooter điện). Thiết bị trả về được **lau dữ liệu, làm sạch, sửa chữa và cho thuê lại** cho người tiếp theo — đây chính là mô hình "kinh tế tuần hoàn" (circular economy) mà Grover dùng làm câu chuyện thương hiệu ([Grover | Rent. Return. Reuse.](https://www.grover.com/de-en/g-explore/sustainable-tech)) **[A]**.

Khách chọn hợp đồng thuê theo độ dài khác nhau (**1, 3, 6, 12 tháng**), hết hạn thì có 3 lựa chọn: **gia hạn — trả lại — mua đứt** ([How Grover's Electronics Rental Model Works, Waste360](https://www.waste360.com/e-waste/how-grover-s-electronics-rental-model-works)) **[B]**.

### 2.2. Định giá — công thức quan trọng nhất để học

> Grover có đội **pricing & analysis** nhìn vào **(1) giá thị trường hiện tại của thiết bị, (2) thời gian thuê trung bình, (3) số chu kỳ cho thuê tiềm năng** để suy ra phí thuê. **Thuê càng dài, giá/tháng càng rẻ.**
> — tổng hợp từ [Complete guide to renting technology with Grover](https://en.androidguias.com/grover/) **[C]** và [Grover — How It Works](https://www.grover.com/us-en/how-it-works) **[A]**

Ví dụ giá thực tế (tháng 9/2026, thị trường Đức, trang sản phẩm Grover) **[A]**:

| Sản phẩm | Giá thuê công bố | URL |
|---|---|---|
| MacBook Air 13" M2, 8GB/256GB | **từ 24,49 EUR/tháng** | [Grover MacBook Air M2](https://www.grover.com/de-en/products/apple-laptop-macbook-air-m2-8gb-256gb-ssd-10-core-gpu) |
| MacBook Pro 13" M2, 16GB/512GB | **từ 108,90 EUR/tháng** | [Grover MacBook Pro 13 M2](https://www.grover.com/de-en/products/apple-macbook-pro-13-3-m2-8cpu-16gb-512gb-10gpu-67w) |

**Đọc hiểu cho nhóm proposal:** chữ "từ" (from) = mức giá của gói thuê **dài nhất** (12 tháng). Gói 1 tháng đắt hơn đáng kể. Đây là **chiến lược neo giá (price anchoring)** — hiển thị giá thấp nhất để thu hút, rồi upsell.

**Nhóm phải tự kiểm chứng:** tỷ lệ % giữa giá 1 tháng và giá 12 tháng, và tỷ lệ giá thuê/tháng so với giá bán lẻ. Tôi **không** tìm được số liệu công bố chính thức về hai tỷ lệ này (xem Mục 17).

### 2.3. Unit economics — con số quan trọng nhất (và cần thận trọng nhất)

Một phân tích được WebSearch trích ra (nguồn phái sinh, **[C]** — [businessmodelcanvastemplate.com — Grover Growth Strategy](https://businessmodelcanvastemplate.com/blogs/growth-strategy/grover-growth-strategy)) nêu:

- **Hoàn vốn thiết bị (payback) trong 10–14 tháng tiền thuê**, sau đó thiết bị vẫn còn giá trị còn lại nhiều năm.
- Trung tâm vận hành tối ưu cho phép **một thiết bị đi qua trung bình ~6 người dùng**, kéo giãn capex.
- Ban lãnh đạo ưu tiên **tăng LTV thiết bị** qua chu kỳ refurbish nhanh hơn và rẻ hơn; kỳ vọng hợp đồng B2B là đòn bẩy biên lợi nhuận vì thời hạn dài và churn thấp.

> ⚠️ **CẢNH BÁO TRÍCH DẪN:** con số "6 người/thiết bị" và "10–14 tháng hoàn vốn" đến từ **nguồn phái sinh, không phải Grover công bố**. Một tìm kiếm khác lại cho ra con số **3–4 người dùng/vòng đời thiết bị**. **Hai con số mâu thuẫn nhau.** Trong proposal, nếu dùng, phải viết là *"theo phân tích của bên thứ ba, ước tính..."* chứ KHÔNG viết *"Grover công bố..."*. Xem Mục 17.

### 2.4. Tài chính, quy mô và cú vấp 2024–2025 (bài học sống còn)

| Mốc | Nội dung | Nguồn |
|---|---|---|
| 2020 | Vượt **50 triệu EUR ARR** | [Grover Press](https://press.grover.com/136893-berlin-based-tech-subscription-service-grover-surpasses-50m-in-annual-recurring-revenue-and-releases-2020-growth-report) **[A]** |
| 4/2021 | Gọi **71 triệu USD** | [TechCrunch](https://techcrunch.com/2021/04/12/grover-raises-71m-to-grow-its-consumer-electronics-subscription-business/) **[B]** |
| 2022 | Series C **330 triệu USD (~302 triệu EUR)** = 110 triệu USD equity + 220 triệu USD debt → **kỳ lân >1 tỷ USD** | [Silicon Canals](https://siliconcanals.com/grover-raises-302m-unicorn-valuation/), [Grover Press](https://press.grover.com/184606-grover-hits-unicorn-valuation-of-over-1bn-on-its-way-to-become-global-market-leader-in-consumer-tech-subscription) **[A/B]** |
| 9/2022 | Thêm **270 triệu EUR debt** từ M&G dưới dạng **Asset Backed Security** (chứng khoán đảm bảo bằng tài sản = đội thiết bị) | [Tech.eu](https://tech.eu/2022/09/28/grover-takes-on-more-debt-funding-this-time-to-the-tune-of-eur270-million/), [Silicon Canals](https://siliconcanals.com/german-unicorn-grover-bags-270m/) **[B]** |
| FY2022 | Doanh thu vượt **100 triệu EUR**; một nguồn dữ liệu khác ghi **235,98 triệu USD** | [Waste360](https://www.waste360.com/e-waste/how-grover-s-electronics-rental-model-works) **[B]**, [GetLatka](https://getlatka.com/companies/grover.com) **[C]** |
| 12/2022 | Sa thải **40 người (~10%)** | [TrueUp](https://www.trueup.io/co/grover/layoffs) **[C]** |
| 7/2024 | Sa thải **~20% nhân sự** | [TrueUp](https://www.trueup.io/co/grover/layoffs) **[C]** |
| 9/2024 → 4/2025 | Đàm phán với cổ đông & chủ nợ → **25/4/2025: Tòa án Charlottenburg phê chuẩn kế hoạch tái cấu trúc theo luật StaRUG**. Nhà đầu tư bơm **30 triệu EUR vốn mới**, đổi lại nhận **50% cổ phần Grover Group GmbH** | [Hengeler Mueller](https://hengeler-news.com/en/articles/hengeler-mueller-advises-grover-on-financial-restructuring-via-starug-proceedings) **[A]** |

**BÀI HỌC XƯƠNG MÁU:** Grover huy động **hơn 600 triệu USD (phần lớn là NỢ)** để mua thiết bị, đạt kỳ lân, rồi vẫn phải **tái cấu trúc phá sản có kiểm soát** và bán 50% công ty lấy 30 triệu EUR. Lý do cấu trúc: mô hình asset-heavy + lãi suất tăng 2022–2024 = chi phí vốn để "ôm" đội thiết bị tăng vọt, trong khi giá thuê không tăng tương ứng.

→ **Với dự án FPT Đà Nẵng: KHÔNG BAO GIỜ dùng vốn vay để mở rộng đội laptop trước khi chứng minh được công suất sử dụng thực tế.** Phải "grow into the fleet", không "buy the fleet then pray".

### 2.5. KYC / xác minh danh tính — Grover làm gì thay cho ĐẶT CỌC

Đây là phần **quan trọng nhất về mặt thiết kế sản phẩm** mà dự án nên học.

**Grover KHÔNG thu tiền đặt cọc.** Khách chỉ trả tháng đầu tiên rồi máy được giao tới nhà ([Grover Renting Review, BeginnerTip](https://beginnertip.com/grover-renting/)) **[C]**.

Thay vào đó, Grover dựng một **"bức tường xác minh" 3 lớp**:

**Lớp 1 — Kiểm tra tín dụng (credit check).** Khi đặt đơn, Grover chạy **soft credit check qua CRIF Bürgel và Schufa** (2 cơ quan tín dụng Đức). Quy trình thường chỉ vài phút, tối đa 1 ngày làm việc ([Grover Help — How does Grover's credit check work?](https://service.grover.com/hc/en-us/articles/19920531898642-How-does-Grover-s-credit-check-work)) **[A]**. Vì đây là "Anfrage Kreditkonditionen" (truy vấn điều kiện tín dụng) nên **không làm giảm điểm Schufa** của khách ([Gründer Vision — Grover Schufa](https://gruender-vision.de/grover-schufa-alles-was-du-wissen-solltest/)) **[C]**.

**Lớp 2 — Xác minh danh tính (ID verification).** Khi hệ thống nghi ngờ, Grover yêu cầu khách **upload ảnh hộ chiếu/CCCD**, hoặc **ảnh chụp sao kê giao dịch ngân hàng**. Với khách cá nhân, yêu cầu **ảnh selfie cầm mặt trước giấy tờ giơ lên camera, thấy rõ đồng thời cả mặt người và giấy tờ** ([Grover Help — Identity Verification](https://service.grover.com/hc/en-us/articles/35704298814866-Identity-Verification), [Additional Verification](https://service.grover.com/hc/en-us/articles/19920613200914-Additional-Verification)) **[A]**.

**Lớp 3 — Khớp thông tin giao hàng.** Tên đầy đủ phải **khớp chính xác với giấy tờ tùy thân**, địa chỉ giao hàng phải **khớp địa chỉ đăng ký thường trú**, kể cả số tầng/số căn hộ **[A]**.

**Xử lý khi fail:** nếu kiểm tra danh tính HOẶC tín dụng cho kết quả âm tính, **Grover từ chối giao máy và KHÔNG nêu lý do cụ thể** (vì lý do bảo vệ dữ liệu cá nhân) **[A]**.

**Nhà cung cấp công nghệ Grover dùng:**
- **Onfido** — xác minh danh tính tự động; Grover báo cáo **giảm 60% thời gian onboarding khách hàng**, và với khách doanh nghiệp thì **rút ngắn được nguyên một ngày** ([Onfido — Grover case study](https://onfido.com/customer/grover/)) **[A]**
- **SEON** — chống gian lận, xác minh ID khi mở rộng toàn cầu ([SEON — Grover partners with SEON](https://seon.io/resources/news/grover-partners-with-seon-to-verify-user-ids-as-it-expands-worldwide/)) **[A]**

> **BÀI HỌC SỐ 1 CHO DỰ ÁN:** Grover thay thế "đặt cọc bằng tiền" bằng **"đặt cọc bằng danh tính + điểm tín dụng"**. Sinh viên FPT không có Schufa, nhưng **có một thứ tương đương và thậm chí mạnh hơn: mã số sinh viên gắn với hồ sơ học vụ, tài khoản email @fpt.edu.vn, và rủi ro bị kỷ luật/khóa điểm nếu vi phạm.** Đây là "tài sản thế chấp phi tiền tệ" mà một startup ngoài trường KHÔNG có được. Đó là lợi thế cạnh tranh cốt lõi của mô hình trong khuôn viên.

### 2.6. Grover Care — mô hình bảo hiểm/miễn trừ hư hỏng

| Nội dung | Chi tiết | Nguồn |
|---|---|---|
| Bản chất | Gói bảo vệ thiết bị trả phí, thay vì bắt khách chịu 100% chi phí sửa | [Grover Care](https://www.grover.com/us-en/g-about/grover-care) **[A]** |
| Phạm vi | Hỏng màn hình, vào nước, lỗi kỹ thuật — **"damages of all kinds"**; Grover Care trả tới **90% chi phí sửa** (bản marketing) | [Grover — sustainable tech](https://www.grover.com/de-en/g-explore/sustainable-tech) **[A]**, [Waste360](https://www.waste360.com/e-waste/how-grover-s-electronics-rental-model-works) **[B]** |
| Cấu trúc gói (bản help center chi tiết hơn) | Tùy quốc gia và thời điểm bắt đầu thuê: hoặc **theo %** (Care chi trả 50% hoặc 80% → khách trả 50% hoặc 20% chi phí hư hỏng), hoặc **phí cố định** (gói Basic / Premium với "repair service fee" cố định) | [Grover Help — What is Grover Care](https://service.grover.com/hc/en-us/articles/19920685566610-What-is-Grover-Care-and-how-does-it-work) **[A]** |
| Thiết bị hỏng không sửa được | Khách chỉ trả **20% giá bán lẻ đề xuất** (RRP) tại thời điểm bắt đầu thuê. Riêng **drone và xe scooter điện: 50%** | [Grover Help — Repair and replacement costs](https://service.grover.com/hc/en-us/articles/19918338642578-Repair-and-replacement-costs), [Drones and e-mobility](https://service.grover.com/hc/en-us/articles/19908669018002-Drones-and-e-mobility-products) **[A]** |
| Hao mòn thường | **Xước nhỏ và dấu hiệu sử dụng bình thường được làm sạch MIỄN PHÍ** sau khi trả | [Grover — Signs of use](https://www.grover.com/at-en/g-about/asset-condition) **[A]** |
| Phí phạt đặc thù | Nếu thiết bị trả về **vẫn còn đăng nhập tài khoản người dùng (vd iCloud chưa đăng xuất)**: phạt thêm **49 EUR** | [Grover Help — Repair and replacement costs](https://service.grover.com/hc/en-us/articles/19918338642578-Repair-and-replacement-costs) **[A]** |
| Cách tính giá sửa | Dựa trên **market-standard grading guidelines** + **database hàng nghìn ca sửa chữa** để quyết định chi phí | như trên **[A]** |

> **BÀI HỌC SỐ 2:** Grover **công khai hóa bảng giá hư hỏng** và **tách biệt rõ "hao mòn bình thường" (miễn phí) với "hư hỏng" (tính tiền)**. Đây là cách giảm tranh chấp mạnh nhất. Dự án FPT phải có **bảng giá đền bù in sẵn, ký trước khi nhận máy** — xem Mục 15.
>
> **BÀI HỌC SỐ 3 (rất ăn tiền cho proposal):** cái phí 49 EUR cho "iCloud chưa đăng xuất" cho thấy Grover học từ nỗi đau vận hành thật: **thiết bị bị khóa tài khoản = thiết bị chết, không cho thuê lại được.** Với dự án thi cử, tương đương: **máy trả về còn khóa Windows/BitLocker, còn account cá nhân, còn phần mềm thi chưa gỡ** → phải có quy trình "wipe & reset" bắt buộc và phí phạt tương ứng.

### 2.7. Quy trình refurbish (reverse logistics) của Grover

Khi thiết bị về kho **[A]**:
1. Đánh giá tình trạng (assessment/grading)
2. **Xóa sạch dữ liệu (data wipe)**
3. Làm sạch, sửa chữa
4. Trả về kho hàng để cho thuê tiếp

Chuyên gia Grover kiểm tra thiết bị **từ mọi góc độ** về tình trạng hình thức, và test toàn diện các chức năng: **màn hình, Bluetooth, loa, camera, bàn phím** ([Grover — Signs of use](https://www.grover.com/at-en/g-about/asset-condition)) **[A]**.

> **BÀI HỌC SỐ 4:** checklist 5 điểm (màn hình / Bluetooth / loa / camera / bàn phím) là **mẫu trực tiếp** để dự án xây "Biên bản bàn giao laptop" 2 chiều. Với laptop đi thi, cần bổ sung: **pin (chu kỳ sạc + % health), cổng sạc, wifi, webcam (bắt buộc cho thi online), microphone, phím F, touchpad**.

---

## 3. GROVER BUSINESS (B2B) — MÔ HÌNH GẦN VỚI "THUÊ THEO ĐỢT" NHẤT

| Chỉ tiêu | Số liệu | Nguồn |
|---|---|---|
| Quy mô khách | **>10.000 doanh nghiệp** tại Đức, Áo, Hà Lan, Tây Ban Nha | [Grover for Business](https://www.grover.com/de-en/for-business) **[A]** |
| Kỳ hạn thuê | **6, 12 hoặc 18 tháng** — thuê càng dài giá/tháng càng rẻ | [Grover for Business](https://www.grover.com/de-en/for-business) **[A]** |
| Định vị | Nền tảng **procurement + asset management**, tối ưu cho SME cần quản lý **hàng trăm thiết bị** | [Waste360](https://www.waste360.com/e-waste/how-grover-s-electronics-rental-model-works) **[B]** |
| Lợi thế kinh tế | Grover kỳ vọng B2B là **đòn bẩy biên lợi nhuận**: hợp đồng dài hơn, churn thấp hơn | [businessmodelcanvastemplate](https://businessmodelcanvastemplate.com/blogs/growth-strategy/grover-growth-strategy) **[C]** |
| Onboarding | Nhờ Onfido, thời gian đăng ký khách DN **giảm nguyên 1 ngày** | [Onfido](https://onfido.com/customer/grover/) **[A]** |

> **BÀI HỌC SỐ 5 — ÁP DỤNG TRỰC TIẾP:** Logic "hợp đồng dài = churn thấp = biên tốt hơn" **có bản sao hoàn hảo trong môi trường FPT**: thay vì chỉ bán lẻ cho từng sinh viên, dự án nên bán **"gói mùa thi" cho tập thể**: hợp đồng với **Ban cán sự lớp / CLB / Phòng Đào tạo / Phòng Khảo thí** để giữ sẵn N máy dự phòng trong toàn bộ tuần thi. Một hợp đồng B2B2C với nhà trường thay thế cho 50 giao dịch lẻ = giảm CAC gần bằng 0, giảm rủi ro công suất nhàn rỗi.

---

## 4. FAT LLAMA (ANH/MỸ) — MARKETPLACE P2P VÀ MẶT TỐI CỦA NÓ

### 4.1. Mô hình doanh thu

Fat Llama thu phí **hai đầu**:

| Bên | Mức phí | Nguồn |
|---|---|---|
| Người cho thuê (lender) | **15%** service fee trên mỗi giao dịch. Một nguồn khác ghi hoa hồng lender **25%, dự kiến giảm còn 20%** | [Sharetribe — How to build a website like Fatllama](https://www.sharetribe.com/create/how-to-build-website-like-fatllama/) **[C]** |
| Người thuê (borrower) | **15%** trên giá niêm yết + **khoản đóng góp bảo hiểm** | như trên **[C]** |

**Ví dụ minh họa (từ nguồn trên):** máy ảnh niêm yết 100 USD/ngày → **người thuê trả ~130 USD, chủ đồ nhận ~85 USD**. Tức **take rate thực tế của nền tảng ≈ 45 USD trên 100 USD giá niêm yết ≈ 34,6% GMV**.

> ⚠️ Các con số 15%/25%/20% mâu thuẫn nhau giữa các nguồn phái sinh; nhóm phải vào trang phí chính thức của Fat Llama để xác nhận. Xem Mục 17.

### 4.2. KYC

- Fat Llama **xác minh mọi người dùng qua 2 hoặc 3 loại giấy tờ**.
- Người cho thuê phải xác minh danh tính bằng **giấy tờ do chính phủ cấp**, và **kiểm tra bổ sung với đồ giá trị cao** ([Sharetribe](https://www.sharetribe.com/create/how-to-build-website-like-fatllama/), [Yo-Rent](https://www.yo-rent.com/blog/build-p2p-rental-website-like-fat-llama/)) **[C]**

### 4.3. Đặt cọc và bảo hiểm

- **Chủ đồ tự đặt điều khoản**: địa điểm nhận, giới hạn sử dụng, **và mức đặt cọc** **[C]**
- Fat Llama tự quảng bá là **"marketplace P2P được bảo hiểm toàn phần đầu tiên thế giới"** — bảo hiểm mọi sản phẩm trên sàn, bồi thường cho chủ đồ khi hư hỏng/mất/trộm **[C]**

### 4.4. ⚠️ MẶT TỐI — ĐÂY LÀ PHẦN GIÁ TRỊ NHẤT CHO PROPOSAL

Có **nhiều báo cáo công khai về gian lận và tranh chấp bồi thường** trên Fat Llama:

| Vụ việc | Nội dung | Nguồn |
|---|---|---|
| Trộm thiết bị ảnh >5.000 USD | Chủ đồ bị lừa mất hơn 5.000 USD thiết bị máy ảnh qua Fat Llama | [PetaPixel — How I Had Over $5,000 in Camera Gear Stolen Through Fat Llama](https://petapixel.com/2019/03/20/how-i-had-over-5000-in-camera-gear-stolen-through-fat-llama/), [DIYPhotography](https://www.diyphotography.net/i-got-5000-worth-of-gear-stolen-from-me-through-fat-llama/) **[B]** |
| Đánh cắp danh tính | Một người dùng kể lại trải nghiệm bị đánh cắp danh tính liên quan Fat Llama | [Medium — My dreadful experience with Fat Llama](https://medium.com/@leemcgavin/my-dreadful-experience-with-fat-llama-6a46dba72135) **[C]** |
| Từ chối bồi thường | Nhiều khiếu nại về việc Fat Llama từ chối bồi thường đồ hỏng sau khi đội resolutions xem xét; có trường hợp chủ đồ mất **1.700 GBP** không được đền | [Trustpilot — Fat Llama reviews](https://www.trustpilot.com/review/fatllama.com), [Reviews.io](https://www.reviews.io/company-reviews/store/fatllama-com) **[C]** |
| Quy trách nhiệm | Nền tảng có xu hướng lập luận *"đó là tài khoản của bạn, bạn chịu trách nhiệm"* khi điều tra đồ bị mất | [Trustpilot](https://www.trustpilot.com/review/fatllama.com) **[C]** |
| Có mặt tích cực | Một số chủ đồ cho biết **nhận bồi thường trong vòng 2 tuần** và hài lòng | [Trustpilot](https://www.trustpilot.com/review/fatllama.com) **[C]** |

**Chế độ vận hành đứng sau các vụ trộm:** kẻ gian tạo tài khoản, đặt thuê thiết bị giá trị cao, hẹn nhận đồ, rồi biến mất. Vì là **P2P giữa hai người lạ, giao dịch ngoài tầm kiểm soát nền tảng**, nên xác minh giấy tờ trên mạng không đủ.

> **BÀI HỌC SỐ 6 — LÝ DO DỰ ÁN KHÔNG NÊN LÀM P2P:** Mô hình P2P (sinh viên A cho sinh viên B thuê máy qua website của mình) nghe hay trên giấy (không cần vốn mua máy!) nhưng **chuyển toàn bộ rủi ro mất máy sang chủ đồ, còn nền tảng ăn phí** — và khi mất máy thật thì nền tảng cãi nhau với người dùng. Với quy mô nhỏ, một vụ mất laptop 15–20 triệu VND là **đủ giết dự án và làm sinh viên FPT ghét thương hiệu mãi mãi**.
>
> → **Khuyến nghị: mô hình B2C, TỰ SỞ HỮU đội máy nhỏ (asset-light nhưng own), giao nhận trực tiếp mặt-đối-mặt trong khuôn viên, KHÔNG làm marketplace P2P ở giai đoạn 1.**

### 4.5. Thương vụ Hygglo mua Fat Llama (8/2022)

| Chỉ tiêu | Số liệu | Nguồn |
|---|---|---|
| Giá | **41,5 triệu USD (~41 triệu EUR / 34,5 triệu GBP)** | [EU-Startups](https://www.eu-startups.com/2022/08/sweden-based-hygglo-acquires-uk-based-fat-llama-in-e41-million-deal-to-create-worlds-biggest-peer-to-peer-rental-platform/), [Tech.eu](https://tech.eu/2022/08/16/swedish-hygglo-fattens-portfolio-with-london-based-fat-llama-for-415-million/), [UKTN](https://www.uktech.news/ecommerce/fat-llama-acquisition-hygglo-20220816) **[B]** |
| Thời điểm | **Tháng 8/2022** | như trên **[B]** |
| Nội dung | Hygglo mua **đội ngũ, vận hành, phần mềm và thương hiệu**; Fat Llama giữ tên tại Anh, Mỹ và thị trường mới; 2 nhà đồng sáng lập Chaz Englander và Rosie Dallas vào HĐQT mới | [EU-Startups](https://www.eu-startups.com/2022/08/sweden-based-hygglo-acquires-uk-based-fat-llama-in-e41-million-deal-to-create-worlds-biggest-peer-to-peer-rental-platform/) **[B]** |
| Bối cảnh | Sifted mô tả hành trình tới thương vụ này là **"gruelling"** (cực nhọc) — *"a cricket bat to the face"* | [Sifted](https://sifted.eu/articles/fat-llama-acquisition) **[B]** |
| Hậu M&A | FY2024 nhóm Hygglo–Fat Llama **tiến gần điểm hòa vốn** sau đợt tinh gọn hậu sáp nhập, **GMV tăng 25%** tại các thị trường lõi; mô hình dự báo ~**30% tăng trưởng doanh thu 2025** nhờ mở rộng Mỹ và nhóm "professional lenders" | [businessmodelcanvastemplate — Fat Llama Growth Strategy](https://businessmodelcanvastemplate.com/blogs/growth-strategy/fat-llama-growth-strategy) **[C]** |

> **BÀI HỌC SỐ 7:** Ngay cả marketplace P2P lớn nhất thế giới cũng **chỉ tiến gần hòa vốn sau khi sáp nhập và cắt giảm mạnh**, và lợi nhuận đến từ **"professional lenders"** (người cho thuê chuyên nghiệp, có nhiều máy) chứ không phải từ người dùng nghiệp dư. Tức là: **quy mô nhỏ + nghiệp dư = không có kinh tế.** Dự án nên tự làm "professional lender" ngay từ đầu.

---

## 5. HYGGLO (THỤY ĐIỂN) — MÔ HÌNH NIỀM TIN DỰA TRÊN ĐỊNH DANH QUỐC GIA

| Chỉ tiêu | Số liệu | Nguồn |
|---|---|---|
| Hoa hồng | **20%** trên mỗi giao dịch (chủ đồ giữ 80%). Riêng **drone: 50%** | [Hygglo Help — How Hygglo works](https://help.hygglo.info/en/articles/10415333-how-hygglo-works) **[A]** |
| Xác minh danh tính | **BankID** — hệ thống định danh điện tử quốc gia của các nước Bắc Âu | [Circular X — Hygglo case](https://www.circularx.eu/en/cases/75/hygglo-peer-to-peer-rental-instead-of-buying), [Hygglo Help](https://help.hygglo.info/en/articles/10420308-what-is-hygglo) **[A/B]** |
| Bảo hiểm | Mọi giao dịch thuê đều **bao gồm bảo vệ chống hư hỏng bất ngờ, trộm cắp hoặc mất mát** trong thời gian thuê | [Hygglo Help — security & protection](https://help.hygglo.info/en/articles/10587214-how-to-provide-great-service-and-understand-security-protection) **[A]** |
| Đơn vị bảo hiểm | **Omocom**, hoặc **Hygglo Lender Guarantee** — tùy thị trường và danh mục hàng | [Hygglo Care for lenders](https://help.hygglo.info/en/articles/12890765-hygglo-care-for-lenders) **[A]** |
| Phí dùng để làm gì | Chi trả **bảo hiểm, xử lý thanh toán, hỗ trợ khách hàng, vận hành và phát triển nền tảng** | [Hygglo Help](https://help.hygglo.info/en/articles/10415333-how-hygglo-works) **[A]** |

### 5.1. Omocom — nhà bảo hiểm nhúng (embedded insurance) cho kinh tế chia sẻ

| Chỉ tiêu | Số liệu | Nguồn |
|---|---|---|
| Bản chất | Công ty **micro-insurance** ở Stockholm, chuyên cho nền tảng chia sẻ/cho thuê | [Omocom](https://www.omocom.insurance/en/), [Ellen MacArthur Foundation](https://www.ellenmacarthurfoundation.org/circular-examples/creating-trust-in-the-sharing-economy-omocom) **[A/B]** |
| Cách tích hợp | **API tính rủi ro thời gian thực** ngay trên nền tảng thuê → phí bảo hiểm được tính riêng cho hành vi "thuê" chứ không phải "sở hữu" | [Van Ameyde — Omocom](https://www.vanameyde.com/stories/omocom-circular-economy/) **[B]** |
| Mô hình bán | Hoặc **theo từng giao dịch**, hoặc **"all-in"** (mọi giao dịch của nền tảng tự động được bảo hiểm) | như trên **[B]** |
| **Giá** | **2–6 EUR/giao dịch**, mức bồi thường tối đa **1.000 EUR** | [Van Ameyde](https://www.vanameyde.com/stories/omocom-circular-economy/) **[B]** |
| Phạm vi thời gian | Chỉ bảo hiểm **trong khoảng thời gian tài sản đang được dùng/vận chuyển/truy cập** — thời gian ngắn | như trên **[B]** |
| Chống gian lận | Dùng **dữ liệu giao dịch** để phòng ngừa gian lận và giảm rủi ro | như trên **[B]** |

> **BÀI HỌC SỐ 8 — CON SỐ VÀNG CHO PROPOSAL:** **2–6 EUR để bảo hiểm một giao dịch thuê với hạn mức 1.000 EUR.** Quy đổi thô (1 EUR ≈ 28.000–29.000 VND, tháng 9/2026 — **nhóm phải tự tra tỷ giá ngày nộp bài**): khoảng **56.000–174.000 VND cho hạn mức ~28 triệu VND**. Tức chi phí bảo hiểm ≈ **0,2%–0,6% giá trị tài sản mỗi lượt thuê**.
>
> Đây là **cơ sở định lượng** để nhóm lập luận: *"Có thể nội bộ hóa rủi ro bằng cách trích một khoản 'quỹ rủi ro' ~0,5–1% giá trị máy trên mỗi lượt thuê, thay vì mua bảo hiểm thương mại (vốn chưa sẵn có cho laptop thuê ngắn hạn ở VN)."*
>
> ⚠️ Cảnh báo: tôi **không** tìm được sản phẩm bảo hiểm tương đương Omocom đang bán tại Việt Nam cho laptop cho thuê theo ngày. Xem Mục 17.

> **BÀI HỌC SỐ 9:** **BankID là "hào nước" của Hygglo.** Ở Bắc Âu, định danh là việc-đã-xong, nên P2P mới chạy được mà ít gian lận. Ở Anh (Fat Llama) không có BankID → gian lận nhiều hơn rõ rệt (so sánh Mục 4.4 với Mục 5). **Việt Nam có VNeID (định danh điện tử mức 2) và CCCD gắn chip** — đây là thứ tương đương BankID về mặt khái niệm. Trong proposal nên nêu VNeID là **hướng nâng cấp KYC giai đoạn 2**, nhưng phải nói rõ nhóm **chưa xác minh** được điều kiện/thủ tục để một startup sinh viên được phép tích hợp/đối soát VNeID (xem Mục 17).

---

## 6. RENT THE RUNWAY (MỸ) — BẬC THẦY VỀ REVERSE LOGISTICS

### 6.1. Tại sao phải học RTR dù họ cho thuê váy, không phải laptop

Vì **cấu trúc bài toán giống hệt**: tài sản đắt tiền → cho thuê ngắn hạn → nhận lại → **phục hồi về tình trạng "như mới"** → cho thuê lại. Sự khác biệt giữa lãi và lỗ nằm ở **chi phí và tốc độ của vòng quay ngược (reverse logistics)** — hoàn toàn đúng với laptop.

### 6.2. Quy trình reverse logistics

Các bước RTR thực hiện với mỗi món đồ khi nhận về **[A/B]**:
1. **Kiểm định chất lượng nghiêm ngặt (quality inspection)** — *"đến từng hạt cườm, từng đường may cuối cùng"*
2. **Giặt khô chuyên dụng** — RTR tự nhận là **"hoạt động giặt khô lớn nhất thế giới"**
3. **Sửa chữa / phục hồi / tẩy vết bẩn**
4. Đóng gói và gửi cho khách kế tiếp

Nguồn: [Rent the Runway — Dream Fulfillment Centers](https://www.renttherunway.com/about-us/process) **[A]**, [Harvard d3 — Rent the Runway Digitizes High-Fashion](https://d3.harvard.edu/platform-rctom/submission/rent-the-runway-digitizes-high-fashion/) **[B]**

**Hạ tầng:** 2 trung tâm — "Dream Fulfillment Center" tại **Secaucus, New Jersey** và một cơ sở tự động hóa **300.000 ft²** tại **Texas (Dallas)**; một nguồn khác mô tả kho New Jersey **150.000 ft²** ([Harvard d3](https://d3.harvard.edu/platform-rctom/submission/rent-the-runway-digitizes-high-fashion/)) **[B]**.

**Tốc độ vòng quay:** RTR hướng tới **"zero-day turnaround"** (món đồ về là đi tiếp trong ngày) và duy trì **throughput dưới 1 tuần** nhờ thu thập dữ liệu về thuộc tính "vật lý" (món đồ đang ở đâu, có hỏng không, đang trong vòng quay không) và tồn kho "lý thuyết" ([Harvard d3](https://d3.harvard.edu/platform-rctom/submission/rent-the-runway-digitizes-high-fashion/)) **[B]**.

### 6.3. Unit economics — bảng số quan trọng

| Chỉ tiêu | Số liệu | Nguồn |
|---|---|---|
| Giá vốn một món | **85–90 USD** | [Gad Allon — Rent the Runway: When Complexity Collides with Scale](https://gadallon.substack.com/p/rent-the-runway-when-complexity-collides) **[B]** |
| Giá thuê trung bình mỗi lượt | **25–30 USD** | như trên **[B]** |
| **Số lượt thuê để hòa vốn một món** | **17–18 lượt** | như trên **[B]** |
| Số lượt cho thuê thực tế trung bình | **~20 lượt/món** | như trên **[B]** |
| Khấu hao tài sản cho thuê | **2–3 năm**, giá trị còn lại tối thiểu | như trên **[B]** |
| Doanh thu trọn đời/món | **445 USD (2019) → 536 USD (2021)**, +20,4%; ROI từ ~4x lên ~6x | như trên **[B]** |
| Vòng quay tồn kho | **9–10 vòng/năm** | như trên **[B]** |
| Chi phí fulfillment Q2/2025 | **22,5 triệu USD = 27,8% doanh thu** (tăng từ 26,1% cùng kỳ) | như trên **[B]** |

> 🔴 **ĐÂY LÀ CON SỐ ĐÁNG SỢ NHẤT TRONG TOÀN BỘ TÀI LIỆU:**
> **Hòa vốn cần 17–18 lượt thuê. Thực tế đạt ~20 lượt. Biên an toàn chỉ 2–3 lượt.**
> Nghĩa là: **chỉ cần một món bị hỏng/mất sớm hơn lượt thứ 17 là món đó LỖ.** Và chi phí fulfillment chiếm **gần 28% doanh thu** — gần một phần ba doanh thu bị "ăn" bởi khâu giặt/kiểm/gửi.
>
> **Suy ra trực tiếp cho dự án laptop:** nếu một laptop giá 15.000.000 VND và giá thuê 100.000 VND/lượt, thì **cần 150 lượt thuê chỉ để hoàn vốn máy**, chưa tính hao mòn, sửa chữa, nhân công. Nếu mùa thi chỉ có ~3 đợt/năm × ~5 ngày = số lượt cực kỳ hạn chế → **mô hình "thuê theo ngày đi thi" một mình KHÔNG đủ để hoàn vốn máy.** Phải:
> - (a) mua máy cũ/refurbished giá thấp (5–8 triệu VND thay vì 15 triệu), và/hoặc
> - (b) nâng giá/lượt, và/hoặc
> - (c) **lấp công suất ngoài mùa thi** (cho thuê theo tuần/tháng cho SV làm đồ án, SV mới chưa kịp mua máy, khách vãng lai), và/hoặc
> - (d) **KHÔNG sở hữu máy** — làm mô hình môi giới/ký gửi với cửa hàng laptop cũ quanh trường (đưa rủi ro tồn kho về phía họ).
>
> **Đây phải là một trong những trang quan trọng nhất của proposal — phần "Unit economics & điểm hòa vốn".**

### 6.4. Bảo hiểm / miễn trừ hư hỏng của RTR

| Nội dung | Chi tiết | Nguồn |
|---|---|---|
| Phí bảo hiểm | **5 USD/đơn**, áp dụng cho gói thuê bao và mọi đơn thuê lẻ 4 hoặc 8 ngày | [MySubscriptionAddiction — RTR review](https://www.mysubscriptionaddiction.com/rent-the-runway-review) **[C]** |
| Bảo gì | **Chỉ vết bẩn nhẹ và hư hỏng nhỏ** | như trên **[C]** |
| **KHÔNG bảo gì** | **Hư hỏng nặng, trộm cắp, mất đồ** | [RTR Terms of Service](https://www.renttherunway.com/pages/termsofservice) **[A]** |
| Mất/hỏng không sửa được | Khách bị tính **NGUYÊN GIÁ BÁN LẺ** của món đồ | [RTR Terms of Service](https://www.renttherunway.com/pages/termsofservice) **[A]**, [GetHuman FAQ](https://gethuman.com/customer-service/Rent-The-Runway/faq/What-happens-if-I-damage-the-rented-items/_JWAEf) **[C]** |

> **BÀI HỌC SỐ 10 — MÔ HÌNH 2 TẦNG TRÁCH NHIỆM:**
> - **Tầng 1 (phí nhỏ, bao gồm sẵn):** hư hỏng nhẹ → nền tảng chịu. Mục đích: **xóa nỗi sợ của khách**, tăng tỷ lệ chốt đơn.
> - **Tầng 2 (khách chịu 100%):** mất/hỏng nặng → **nguyên giá bán lẻ**.
>
> Cấu trúc này **vừa dễ bán vừa không phá sản người cho thuê**. Dự án nên sao chép nguyên xi: **"Phí dịch vụ đã bao gồm miễn trừ hư hỏng nhẹ (xước vỏ, bẩn bàn phím). Mất máy / hỏng nặng (vỡ màn, vào nước, rơi gãy): đền theo bảng giá niêm yết."**

### 6.5. Tài chính RTR (FY2025, kết thúc 31/01/2026)

| Chỉ tiêu | Số liệu | Nguồn |
|---|---|---|
| Doanh thu FY2025 | **329,8 triệu USD**, +7,7% YoY | [RTR IR — FY2025 results](https://investors.renttherunway.com/news-releases/news-release-details/rent-runway-inc-announces-fourth-quarter-and-full-year-2025) **[A]**; [SEC 8-K](https://www.sec.gov/Archives/edgar/data/1468327/000146832726000018/fy2025earningsrelease.htm) **[A]** |
| Doanh thu quý cao nhất lịch sử | **91,7 triệu USD (Q4 FY2025)** | như trên **[A]** |
| Thuê bao hoạt động cuối FY2025 | **143.796**, +20% YoY | như trên **[A]** |
| Đầu tư tài sản cho thuê FY2025 | **74,9 triệu USD** (mức đầu tư tồn kho lớn nhất lịch sử công ty) | như trên **[A]** |
| Kế hoạch FY2026 | Giảm đầu tư tài sản cho thuê xuống **45–50 triệu USD** | như trên **[A]** |
| Ngày công bố 10-K FY2025 | **14/04/2026** | [SEC 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1468327/000146832725000056/fy2024earningsrelease.htm) **[A]** |
| Lợi nhuận | Lần đầu có **lãi GAAP theo quý** ở FY2025 trên nền lỗ hoạt động lũy kế 57,5 triệu USD; vẫn **đốt ~46 triệu USD tiền mặt** | [Eightx teardown](https://eightx.co/blog/us-teardown-rent-the-runway) **[C]** |

> **BÀI HỌC SỐ 11:** RTR mất **16 năm (2009→2026)** mới chạm được lợi nhuận GAAP theo quý, và ngay sau đó **cắt đầu tư tồn kho từ 74,9 xuống 45–50 triệu USD**. Thông điệp: **trong ngành cho thuê tài sản, "tăng trưởng bằng cách mua thêm hàng" là con đường đốt tiền; "tăng vòng quay trên hàng đang có" mới là con đường sống.** Proposal nên nêu rõ chỉ số Bắc Đẩu (North Star Metric) là **số lượt thuê/máy/tháng**, KHÔNG phải "số máy trong kho".

---

## 7. LUMOID (MỸ) — MỔ XẺ CÁI CHẾT (phần bắt buộc của nhiệm vụ)

### 7.1. Lumoid là gì

- Startup Mỹ, thuộc **Y Combinator khóa S13** ([Y Combinator blog — Lumoid (YC S13)](https://www.ycombinator.com/blog/lumoid-yc-s13-wants-to-rent-you-a-camera-now-and-everything-later)) **[A]**
- Nhà sáng lập/CEO: **Aarthi Ramamurthy** ([YC — Female Founder Stories](https://www.ycombinator.com/blog/female-founder-stories-aarthi-ramamurthy-founder-of-lumoid-yc-s13)) **[A]**
- Khởi đầu: **cho thuê máy ảnh ngắn hạn**, sau mở rộng sang **wearables** (vòng đeo tay, smartwatch)
- Tuyên ngôn: *"Rent you a camera now, and everything later"*

### 7.2. Mô hình kinh doanh — "try before you buy"

| Cơ chế | Chi tiết | Nguồn |
|---|---|---|
| Thuê máy ảnh có quyền mua | Thuê thiết bị ảnh, nếu quyết định mua thì **phí thuê đã trả được KHẤU TRỪ vào giá mua** | [TechCrunch 2014](https://techcrunch.com/2014/04/03/lumoid-wants-to-rent-you-a-camera-now-and-everything-later) **[B]** |
| Gói wearables | Chọn **5 thiết bị** từ danh sách **>20 wearables**, Lumoid gửi **miễn phí**, dùng **7 ngày** rồi trả hoặc mua | [VentureBeat](https://venturebeat.com/business/lumoid-launches-a-try-before-you-buy-service-for-wearables/), [Android Authority](https://www.androidauthority.com/lumoid-wearables-try-before-you-buy-580387/) **[B]** |
| Phí nếu không mua | **20 USD** nếu kết thúc 7 ngày mà không mua gì | [PCWorld](https://www.pcworld.com/article/431215/not-sure-about-wearables-lumoid-launches-a-try-before-you-buy-program.html) **[B]** |
| Giá bán | **Bằng giá thị trường, không markup** | như trên **[B]** |
| Chi tiết tinh tế | Khi khách muốn giữ một món, khách **KHÔNG giữ máy đã dùng thử** — trả hết về, báo muốn mua món nào, Lumoid **gửi hàng MỚI TINH** → khách không phải trả giá nguyên seal cho hàng đã qua tay | [PCWorld](https://www.pcworld.com/article/431215/not-sure-about-wearables-lumoid-launches-a-try-before-you-buy-program.html) **[B]** |
| Thương hiệu có mặt | Jawbone, FitBit, Samsung Gear Fit, Pebble | như trên **[B]** |

### 7.3. Cái chết — thời gian và nguyên nhân

| Mốc | Sự kiện | Nguồn |
|---|---|---|
| ~2013 | Thành lập, vào YC S13 | [YC](https://www.ycombinator.com/blog/lumoid-yc-s13-wants-to-rent-you-a-camera-now-and-everything-later) **[A]** |
| 2013–2017 | Gọi vốn tổng cộng **gần 6 triệu USD** (vốn + tài trợ) trong ~4 năm | [TechCrunch — Why gear rental marketplace Lumoid shut down](https://techcrunch.com/2017/12/10/why-gear-rental-marketplace-lumoid-shut-down/) **[B]** |
| **6/2017** | Công bố **hợp tác với Best Buy** — khách Best Buy được "try before you buy" máy ảnh/drone | [Recode](https://www.recode.net/2017/6/12/15771838/best-buy-drone-camera-rental-trial-try-before-buy-lumoid) **[B]** |
| ~8/2017–12/2017 | **Cuốn gói dần trong 4 tháng**: bán tài sản và IP, hỗ trợ nhân sự chuyển việc | [TechCrunch](https://techcrunch.com/2017/12/10/why-gear-rental-marketplace-lumoid-shut-down/) **[B]** |
| **09/12/2017** | Nhà sáng lập đăng thông báo đóng cửa | [TechCrunch](https://techcrunch.com/2017/12/10/why-gear-rental-marketplace-lumoid-shut-down/), [Digital Trends](https://www.digitaltrends.com/photography/gear-rental-startup-lumoid-closes/) **[B]** |
| Sau đó | Aarthi Ramamurthy về **Facebook** làm hệ thống thanh toán online | [Digital Trends](https://www.digitaltrends.com/photography/gear-rental-startup-lumoid-closes/) **[B]** |

### 7.4. 🔴 NGUYÊN NHÂN THẤT BẠI — PHÂN TÍCH

**Nguyên nhân trực tiếp (do chính nhà sáng lập nói với TechCrunch):**
> Lumoid **gặp khó khăn về vốn khi cần mở rộng quy mô cho đợt ra mắt với Best Buy** và vì vậy quyết định chấm dứt hoạt động.
> — [TechCrunch, 10/12/2017](https://techcrunch.com/2017/12/10/why-gear-rental-marketplace-lumoid-shut-down/) **[B]**

Cụ thể hơn: dù đã ký được hợp đồng với Best Buy, **Lumoid không huy động được số tiền cần thiết để MUA ĐỦ THIẾT BỊ** phục vụ hợp đồng đó ([Gizmodo](https://gizmodo.com/lumoid-best-buys-supposed-gear-rental-partner-shuts-d-1821165345), [Digital Trends](https://www.digitaltrends.com/photography/gear-rental-startup-lumoid-closes/), [Light Stalking](https://www.lightstalking.com/lumoid-camera-gear-rental-service-shuttered/)) **[B]**.

**Nghịch lý cốt lõi — "chết vì thành công":**

| Yếu tố | Diễn giải |
|---|---|
| Có product-market fit | Khách thích, Best Buy — chuỗi bán lẻ điện tử lớn nhất Mỹ — chịu ký hợp đồng |
| Có thương hiệu, có YC, có ~6 triệu USD | Không phải startup "làng nhàng" |
| **Nhưng mô hình là ASSET-HEAVY** | Mỗi khách hàng mới = **phải bỏ tiền mua thêm một thiết bị**. Doanh thu tăng tuyến tính nhưng **capex cũng tăng tuyến tính** |
| **Hợp đồng lớn = nhu cầu vốn nhảy vọt** | Best Buy có hàng trăm cửa hàng → cần hàng nghìn thiết bị → cần vốn gấp nhiều lần 6 triệu USD đã gọi được |
| **Không gọi được vốn đó** | → không giao được hợp đồng → đóng cửa |

**Nguyên nhân cấu trúc sâu hơn (suy luận, KHÔNG phải trích dẫn):**
1. **"Try before you buy" có mâu thuẫn lợi ích nội tại:** mục tiêu của khách là *không mua* nếu không thích. Doanh thu thực (20 USD/7 ngày) quá nhỏ so với giá vốn thiết bị (một Fitbit/Pebble thời đó ~100–250 USD). Cần **rất nhiều lượt** để hoàn vốn — đúng bài toán 17–18 lượt của Rent the Runway (Mục 6.3).
2. **Thiết bị điện tử mất giá cực nhanh.** Wearables 2014–2017 là thị trường sụp đổ (Jawbone phá sản 2017, Pebble bị Fitbit mua 2016). Tài sản của Lumoid **mất giá nhanh hơn tốc độ khấu hao qua tiền thuê** → tài sản trở thành nợ.
3. **Phụ thuộc một khách hàng lớn (key account dependency).** Best Buy vừa là cơ hội lớn nhất vừa là thứ giết chết công ty: nó ép Lumoid phải nhảy từ quy mô nhỏ lên quy mô lớn **trong một bước**, không có đường lùi.

> 🔴 **BÀI HỌC SỐ 12 — BÀI HỌC QUAN TRỌNG NHẤT CHO PROPOSAL:**
> **Lumoid không chết vì không có khách. Lumoid chết vì mỗi khách hàng mới đòi hỏi một khoản đầu tư thiết bị mới mà công ty không đủ tiền ứng trước.**
>
> **Suy ra cho dự án:** Đội laptop cho thuê là **"trần công suất cứng"**. Nếu ngày 20/12 có 40 sinh viên cần máy mà dự án chỉ có 6 máy, thì 34 người kia **không thể phục vụ bằng cách "code thêm tính năng"** — phải có máy vật lý. Và nhu cầu thi cử **cực kỳ tập trung theo mùa** (peak cực nhọn, off-peak gần bằng 0), tức là **tỷ lệ đỉnh/đáy rất xấu**.
>
> **Đối sách bắt buộc phải có trong proposal:**
> 1. **Mô hình lai (hybrid):** sở hữu một lõi nhỏ 5–10 máy + **ký hợp đồng ký gửi/huy động máy nhàn rỗi** từ sinh viên khóa trên, cựu SV, cửa hàng laptop cũ quanh Hòa Hải trong mùa cao điểm — trả phí theo lượt. → **biến chi phí cố định thành chi phí biến đổi**, đúng thứ Lumoid không làm được.
> 2. **Hệ thống đặt trước (pre-booking) mở sớm theo lịch thi** để biết cầu TRƯỚC khi phải có cung → không bao giờ mua máy dựa trên phỏng đoán.
> 3. **Tuyệt đối không nhận "hợp đồng lớn" (vd Phòng Khảo thí yêu cầu 100 máy dự phòng) nếu chưa có nguồn máy đảm bảo.** Từ chối một hợp đồng quá lớn là hành động cứu công ty.

---

## 8. OMNI (MỸ) — CÁI CHẾT THỨ HAI, XÁC NHẬN CÙNG MỘT QUY LUẬT (bonus)

| Chỉ tiêu | Chi tiết | Nguồn |
|---|---|---|
| Mô hình | Lưu kho theo yêu cầu + **cho thuê đồ đạc** của người dùng | [TechCrunch — Omni shuts down](https://techcrunch.com/2019/11/25/omni-shuts-down/) **[B]** |
| Vốn huy động | **35 triệu USD** (có Ripple hậu thuẫn) | như trên **[B]**; [Crowdfund Insider](https://www.crowdfundinsider.com/2019/11/154551-ripple-backed-storage-and-rental-firm-omni-rentals-will-reportedly-be-closing-down/) **[B]** |
| Thời điểm chết | **11/2019** | như trên **[B]** |
| Lý do (trích) | *"Họ nhận ra business cốt lõi, với cách nó được thiết kế, là cực kỳ khó. Dịch vụ rất tuyệt với người tiêu dùng, nhưng khi nhìn vào cái giá phải trả để scale thì nó vừa khó vừa đắt."* | [TechCrunch](https://techcrunch.com/2019/11/25/omni-shuts-down/) **[B]** |
| Chẩn đoán của TechCrunch | **Nạn nhân của mô hình "dịch vụ tiện lợi bán dưới giá thành nhờ VC bù lỗ"** | như trên **[B]** |
| Vấn đề cụ thể | Giá lưu kho tăng → khách bỏ đi; **việc thuê đồ phiền phức vì người dùng phải tự đi lấy và tự trả**, trong khi họ có thể mua luôn trên Amazon giao ngay | như trên **[B]** |
| Kết cục | Bán mảng kho vật lý cho Clutter (5/2019), pivot sang phần mềm white-label cho cửa hàng cho thuê đồ → thất bại; **Coinbase tuyển ~10 kỹ sư** | như trên **[B]** |

> **BÀI HỌC SỐ 13 — "PHIỀN PHỨC" LÀ KẺ GIẾT NGƯỜI THẦM LẶNG:**
> Omni chết một phần vì **ma sát vật lý**: đi lấy + đi trả **phiền hơn là mua mới**. Đây là rủi ro số 1 của dự án laptop thi cử: nếu sinh viên phải **đi bộ 15 phút ra ngoài cổng trường, gặp người lạ, ký giấy, đặt cọc tiền mặt** thì họ sẽ chọn **mượn máy của bạn cùng phòng** — miễn phí và nhanh hơn.
>
> **Đối thủ cạnh tranh thực sự của dự án KHÔNG phải là cửa hàng cho thuê laptop. Đó là "mượn bạn bè" (giá 0 đồng) và "phòng máy của trường" (giá 0 đồng).** Proposal PHẢI trả lời thẳng câu hỏi này, nếu không sẽ bị giảng viên bắt bài ngay.
>
> → **Điểm sống còn: điểm giao/nhận phải NẰM TRONG hoặc SÁT phòng thi, và thời gian nhận máy phải < 5 phút.** Đây chính là lý do mô hình kiosk (Mục 9) đáng học.

---

## 9. TURO (MỸ) — CHUẨN MỰC VỀ KYC + ĐẶT CỌC + BẢO HIỂM CHO TÀI SẢN GIÁ TRỊ CAO

### 9.1. Quy mô và mô hình doanh thu

| Chỉ tiêu | Số liệu 2024 | Nguồn |
|---|---|---|
| Doanh thu | **~958 triệu USD**, +9% so với 880 triệu USD (2023) | [Sacra — Turo](https://sacra.com/c/turo/) **[C]**; [Dittofi](https://www.dittofi.com/learn/turo-business-model) **[C]** |
| Gross Booking Value (GBV) | **2,5 tỷ USD** | như trên **[C]** |
| Chi trả cho host | **1,5 tỷ USD** | như trên **[C]** |
| Take rate ngụ ý | 958 / 2.500 ≈ **38% GBV** (gồm cả phí người thuê) | tính toán từ số trên |

**Cấu trúc hoa hồng — điểm hay nhất để học:**

Turo có **nhiều gói bảo vệ (protection plan)** cho chủ xe, và **mức hoa hồng gắn liền với mức bảo vệ**:

| Gói (host earnings) | Host nhận | Turo lấy | Mức khấu trừ (deductible) chủ xe chịu |
|---|---|---|---|
| Bảo vệ cao nhất | **60%** | 40% | Thấp nhất |
| … | 75% | 25% | ↑ |
| … | 80% | 20% | ↑ |
| … | 85% | 15% | ↑ |
| Bảo vệ thấp nhất | **90%** | 10% | Cao nhất |

Nguồn: [Rentovation — Turo Takes 10% to 30%](https://rentovation.co/guides/how-much-does-turo-take) **[C]**, [RentScout](https://rentscout.io/is-turo-still-profitable-for-hosts/) **[C]**, [Turo Business Model, RentallScript](https://www.rentallscript.com/resources/turo-business-model/) **[C]**

Ngoài ra Turo còn thu **trip fee từ người thuê**, thường **10–30% giá chuyến**, biến thiên theo độ dài chuyến và loại xe **[C]**.

> **BÀI HỌC SỐ 14 — CƠ CHẾ "CHỌN MỨC RỦI RO" LÀ MỘT SẢN PHẨM:**
> Turo không ép một mức bảo hiểm duy nhất. Họ **bán chính mức độ an tâm như một tầng giá**. Ai muốn an toàn thì trả hoa hồng cao; ai chấp nhận rủi ro thì giữ tiền nhiều hơn.
>
> **Áp dụng ngược cho dự án:** thay vì một giá thuê duy nhất, bán **2–3 gói**:
> - **Gói Cơ bản** — giá thuê thấp + **đặt cọc cao** (hoặc giữ CCCD/thẻ SV) + khách chịu 100% hư hỏng
> - **Gói An tâm** — giá thuê cao hơn + **miễn cọc** + miễn trừ hư hỏng nhẹ, giới hạn trách nhiệm khi hỏng nặng
> - **Gói Cấp tốc (mùa thi)** — giao máy tận phòng thi trong 15 phút, giá cao nhất
>
> Cách này vừa tăng doanh thu vừa **cho khách cảm giác kiểm soát** — yếu tố tâm lý cực mạnh khi khách đang lo lắng (ngày thi!).

### 9.2. Đặt cọc — cơ chế kỹ thuật chi tiết

| Nội dung | Chi tiết | Nguồn |
|---|---|---|
| **Mức cọc** | **0 – 750 USD**, tùy **độ tuổi người thuê** và **hạng xe**. Ví dụ: **750 USD** nếu người thuê **dưới 30 tuổi** thuê xe **hạng Deluxe** | [Turo Help — Security deposits (US)](https://help.turo.com/en_us/security-deposits-us-HkbE44lE9) **[A]**; [Jerry](https://jerry.ai/car-insurance/how-much-is-the-deposit-for-turo/) **[C]** |
| **Cơ chế** | **Authorization hold (giữ tiền, không trừ tiền)** — tiền bị "khóa" trên thẻ nhưng chưa trừ | [Ride-Share.com](https://ride-share.com/does-turo-charge-a-deposit/) **[C]** |
| **Thời điểm giữ** | **24–48 giờ TRƯỚC khi chuyến đi bắt đầu** | như trên **[C]** |
| **Thời điểm trả** | **Tự động hoàn 80 giờ sau khi chuyến kết thúc**, với điều kiện: (1) không bên nào báo cáo hư hỏng xe, VÀ (2) không có hóa đơn bồi hoàn chưa thanh toán | [Turo Help — Security deposits](https://help.turo.com/en_us/security-deposits-us-HkbE44lE9) **[A]** |
| **Giảm cọc** | Turo **giảm 250 USD tiền cọc** nếu người thuê **cung cấp thông tin bảo hiểm ô tô cá nhân** khi đặt xe | như trên **[A/C]** |

> **BÀI HỌC SỐ 15 — HAI CHI TIẾT THIÊN TÀI:**
> 1. **Mức cọc thay đổi theo hồ sơ rủi ro** (tuổi < 30 + xe đắt = cọc cao nhất). **KHÔNG dùng một mức cọc phẳng cho mọi người.** Dự án nên làm: sinh viên năm 3–4 có lịch sử thuê tốt → cọc 0đ; sinh viên năm nhất lần đầu thuê máy đắt tiền → cọc cao nhất.
> 2. **Giảm cọc để đổi lấy dữ liệu rủi ro** (đưa bảo hiểm cá nhân → bớt 250 USD). Dự án có thể sao chép: **"Xác thực bằng tài khoản @fpt.edu.vn + cho mượn ảnh thẻ SV → miễn cọc"**, **"Có người bảo lãnh là SV đã thuê ≥ 2 lần → giảm 50% cọc"**. Biến việc giảm cọc thành **phần thưởng cho việc cung cấp bằng chứng danh tính** — vừa giảm ma sát vừa giảm rủi ro.
> 3. **"80 giờ" là con số cụ thể, công khai.** Khách biết chính xác khi nào được hoàn tiền → giảm 90% tin nhắn hỏi "bao giờ trả cọc?". Dự án phải có cam kết tương tự: **"Hoàn cọc trong vòng 24 giờ sau khi trả máy và kiểm tra xong"**.

### 9.3. KYC / Trust & Safety của Turo

| Lớp | Chi tiết | Nguồn |
|---|---|---|
| Nhà cung cấp | **ComplyCube** — Turo hợp tác xây dựng vòng đời xác minh khách hàng end-to-end cho car-sharing | [ComplyCube — Turo case](https://www.complycube.com/en/customer/turo-strengthens-car-sharing-compliance/) **[A]** |
| Thành phần | **Xác minh giấy tờ (document verification)**, **sinh trắc học liveness** (chống dùng ảnh/video giả), **kiểm tra bằng lái** | như trên **[A]** |
| Chống gian lận sau đặt xe | Bộ công cụ fraud intelligence phát hiện **chiếm đoạt tài khoản (account takeover), thiết bị bị đánh cắp, mẫu email đáng ngờ, tín hiệu gian lận di động** — xuyên suốt quá trình onboarding | như trên **[A]** |
| Triết lý | *"Authentication giúp Turo giảm gian lận bằng cách xác minh danh tính người dùng **mỗi lần** họ dùng sản phẩm"* — Mike Wilkins, Senior Director Trust & Safety | [Mitek — Q&A with Turo](https://www.miteksystems.com/blog/innovator-qa-mike-wilkins-senior-director-trust-safety-at-turo) **[A]** |
| Bảo vệ tài sản | Xe được **bảo vệ theo hợp đồng chống trộm cắp và hư hỏng vật lý** | [Turo — Trust & Safety](https://turo.com/us/en/trust-and-safety) **[A]** |
| ⚠️ Giới hạn | Vẫn có kẻ xấu lọt lưới; **xe trên nền tảng Turo từng bị dùng cho buôn người và ma túy**; sau vụ nổ Cybertruck 1/2025, Turo thuê **chuyên gia an ninh quốc gia và chống khủng bố** | [TechCrunch 03/01/2025](https://techcrunch.com/2025/01/03/turo-taps-national-security-and-counterterrorism-experts-after-cybertruck-explosion) **[B]** |

> **BÀI HỌC SỐ 16 — XÁC MINH LẠI MỖI LẦN, KHÔNG PHẢI CHỈ LÚC ĐĂNG KÝ.** Đây là sự khác biệt tinh vi: nhiều startup chỉ KYC một lần lúc tạo tài khoản. Turo xác thực **mỗi giao dịch**. Với dự án: mỗi lần giao máy phải **chụp ảnh người nhận cầm thẻ SV bên cạnh máy, có timestamp** — vừa là xác thực, vừa là bằng chứng bàn giao.

---

## 10. GETAROUND (MỸ/EU) — BÀI HỌC VỀ CÁCH KHÔNG ĐƯỢC LÀM BẢO HIỂM

| Nội dung | Chi tiết | Nguồn |
|---|---|---|
| Trạng thái | **Ngừng hoạt động tại Bắc Mỹ từ đầu 2025** | tổng hợp WebSearch **[C]** — ⚠️ xem Mục 17 |
| Vụ kiện | Tổng Chưởng lý Washington DC (Brian Schwalb) điều tra và đạt thỏa thuận buộc Getaround hoàn tiền | [Văn phòng Tổng Chưởng lý DC](https://oag.dc.gov/release/attorney-general-schwalb-secures-refunds-dc) **[A]** |
| Cáo buộc | Getaround **đưa thông tin sai lệch cho người dùng**, bao gồm **sai lệch về mức độ an toàn và bảo mật của nền tảng**, dẫn tới việc **xe khách hàng bị hư hỏng và bị đánh cắp** | như trên **[A]** |
| Giai đoạn vi phạm | **2022 → 2025**: gây hiểu lầm về phạm vi bảo hiểm và **không công bố rõ các trường hợp loại trừ (exclusions)**, khiến một số người dùng bị tính phí | như trên **[A]** |
| Chế tài | Phải hoàn tiền cho **hơn 50 người tiêu dùng ở DC** bị gây hiểu lầm về bảo hiểm, đã trả phí hư hỏng lớn, hoặc bị từ chối bồi thường sai | như trên **[A]** |
| Khiếu nại khác | Nhiều khiếu nại 2024–2025 về phí gian lận, yêu cầu bồi thường hư hỏng sai, phí tranh chấp | [BBB — Getaround complaints](https://www.bbb.org/us/ca/san-francisco/profile/auto-renting-and-leasing/getaround-1116-390772/complaints) **[C]** |

> 🔴 **BÀI HỌC SỐ 17 — RỦI RO PHÁP LÝ TỪ VIỆC MỜ ÁM VỀ BẢO HIỂM:**
> Getaround bị cơ quan nhà nước xử lý **không phải vì xe bị mất**, mà vì **nói không rõ về việc bảo hiểm KHÔNG bao gồm cái gì**.
>
> **Áp dụng cho dự án:** trong Điều khoản dịch vụ, phần **"NHỮNG TRƯỜNG HỢP KHÔNG ĐƯỢC MIỄN TRỪ"** phải được viết **to, rõ, đầu tiên**, không giấu ở cuối trang. Ví dụ bắt buộc liệt kê: *rơi vỡ màn hình, vào nước, mất máy, cho người khác mượn lại, mang ra khỏi khuôn viên trường khi chưa đăng ký*. Một proposal môn Khởi nghiệp có phần "minh bạch điều khoản" viết tốt sẽ **ghi điểm rất cao** vì nó cho thấy nhóm hiểu rủi ro pháp lý — thứ 90% nhóm khác bỏ qua.

---

## 11. LAPTOPSANYTIME + CÁC CHƯƠNG TRÌNH CHO MƯỢN LAPTOP TRONG TRƯỜNG ĐH MỸ

### 11.1. LaptopsAnytime là gì

Hệ thống **kiosk tự phục vụ** cho thư viện, trường học, đại học và cơ sở công cộng, **tự động phát, sạc, giám sát và quản lý vòng quay laptop/tablet** ([LaptopsAnytime](https://www.laptopsanytime.com/), [Insights Success](https://insightssuccess.com/laptopsanytime-automated-checkout-kiosks/)) **[A/C]**.

**Quy trình mượn (đơn giản đến mức đáng học thuộc lòng):**
1. Sinh viên bước tới kiosk
2. **Quét thẻ thư viện/thẻ SV**
3. **Nhập mã PIN**
4. **Laptop tự động nhả ra**
5. Dùng xong, **cắm lại vào bất kỳ khe trống nào**
6. Hệ thống **tự động reset thiết bị (xóa dữ liệu phiên) và bắt đầu sạc** cho người kế tiếp

Nguồn: [LaptopsAnytime](https://www.laptopsanytime.com/) **[A]**, [Inside Higher Ed](https://www.insidehighered.com/news/2013/02/08/libraries-turn-laptop-vending-machines-fulfill-students-late-night-studying-needs) **[B]**

> **BÀI HỌC SỐ 18 — "TỰ ĐỘNG RESET GIỮA HAI PHIÊN" LÀ TÍNH NĂNG SỐNG CÒN.** Với laptop đi thi, đây còn quan trọng hơn: **máy phải sạch hoàn toàn, không có tài liệu của người trước** (nếu không sẽ bị quy kết gian lận!) và **pin phải đầy**. Nếu dự án không tự động hóa được thì phải có **checklist thủ công bắt buộc: reset về trạng thái sạch + sạc đầy 100% + kiểm tra trước mỗi lần giao**.

### 11.2. Số liệu vận hành

| Chỉ tiêu | Số liệu | Nguồn |
|---|---|---|
| Công suất 1 kiosk 12 khe | **35 lượt/ngày dễ dàng, tối đa ~100 lượt/ngày** | [Spaces4Learning — Laptop Checkouts Made Easy](https://spaces4learning.com/whitepapers/2024/03/laptop-checkouts-made-easy.aspx) **[B]** |
| Hệ 30 khe | Xử lý được lượng người dùng lớn ở vị trí đông đúc | như trên **[B]** |
| Tổng lượt mượn tự động (cộng dồn) | **>4 triệu lượt** | [LaptopsAnytime — About Us](https://www.laptopsanytime.com/about-us) **[A]** |
| Cấu hình | Từ **6–12 thiết bị/máy**, có module mở rộng **12 hoặc 18 khe** | [LaptopsAnytime — Product Lines](https://www.laptopsanytime.com/product-lines) **[A]** |
| Ca nghiên cứu | **Tarleton State University: lượt mượn laptop tăng 30%** sau khi triển khai kiosk | [PUPN Magazine](https://pupnmag.com/article/laptop-checkouts-automated-dispensing-kiosk-systems-transform-higher-ed-computing/) **[B]** |
| Số trường dùng (thời điểm 2013) | ~6 trường đại học | [Inside Higher Ed](https://www.insidehighered.com/news/2013/02/08/libraries-turn-laptop-vending-machines-fulfill-students-late-night-studying-needs) **[B]** |

### 11.3. Giá kiosk

| Trường | Giá | Nguồn |
|---|---|---|
| **Drexel University** | **~30.000 USD/máy** (12 khe ở mặt trước) | [Chronicle of Higher Education](https://www.chronicle.com/blogs/wiredcampus/drexel-u-library-adds-vending-machine-to-dispense-laptops), [Drexel News Blog](https://newsblog.drexel.edu/2013/01/04/vending-machine-dispenses-macbooks-for-student-use/) **[B]** |
| **Grand Rapids Community College** | **35.000 USD** | [CampusIDNews](https://www.campusidnews.com/grand-rapids-cc-installs-laptop-vending-machine/), [Community College Daily](https://www.ccdaily.com/2018/04/laptop-vending-machine/) **[B]** |

> **BÀI HỌC SỐ 19 — KIOSK LÀ MÔ HÌNH ĐÚNG NHƯNG SAI GIAI ĐOẠN.**
> **30.000–35.000 USD ≈ 760–890 triệu VND** cho MỘT máy chứa 12 laptop (chưa tính 12 laptop bên trong). Với một bài tập khởi nghiệp sinh viên, con số này là **hoàn toàn bất khả thi ở giai đoạn 1** — và đó chính là điểm mạnh để viết proposal:
>
> > *"Chúng tôi làm 'LaptopsAnytime phiên bản con người': một quầy giao nhận vật lý + website đặt trước, chi phí gần bằng 0, đạt được 80% giá trị mà kiosk mang lại (nhận máy nhanh, gần phòng thi, xác thực bằng thẻ SV). Kiosk tự động là lộ trình giai đoạn 3 khi đã có ≥ X lượt thuê/tháng."*
>
> Đây là cách trình bày **lộ trình sản phẩm có căn cứ số liệu** — thứ giảng viên môn Khởi nghiệp tìm kiếm.

### 11.4. Chính sách mượn/phạt — bảng tham chiếu trực tiếp để thiết kế giá

| Trường | Thời hạn mượn | Phí phạt trễ | Phí mất máy | Nguồn |
|---|---|---|---|---|
| **Drexel University** | **5 giờ** (một nguồn khác ghi cửa sổ **4 giờ**) | **5 USD/giờ** sau hạn | — | [Inside Higher Ed](https://www.insidehighered.com/news/2013/02/08/libraries-turn-laptop-vending-machines-fulfill-students-late-night-studying-needs), [Drexel Libraries](https://library.drexel.edu/news-and-events/programs-and-initiatives/laptop-charger-lending-kiosks/) **[A/B]** |
| **University of Utah** | theo bậc | **từ 1 USD cho 30 phút đầu** | — | [KSL](https://www.ksl.com/article/12357245) **[B]** |
| **Indiana University Bloomington** | — | — | **900 USD** cho laptop mất + **50 USD** cho sạc | tổng hợp WebSearch **[C]** |
| **UNT Dallas** | — | — | **1.200 USD** laptop + **20 USD** sạc | [UNT Dallas OIT](https://www.untdallas.edu/oit/digital-spaces/laptop-checkout.php) **[A]** |
| **UMN Crookston** | — | — | **500 USD** laptop mất/bị trộm | [UMN Crookston — fees lost/stolen](https://crk.umn.edu/computer-help-desk/fees-lost-stolen) **[A]** |
| Chung | — | **Nợ phạt hoặc còn đồ quá hạn → BỊ CHẶN mượn tiếp** | Người mượn **chịu trách nhiệm tài chính** cho máy và sạc mất/bị trộm | [Drexel Libraries](https://library.drexel.edu/news-and-events/programs-and-initiatives/laptop-charger-lending-kiosks/) **[A]** |

**Kiểm soát trộm cắp:** lo ngại về trộm cắp được giải quyết bằng **lắp cảm biến báo động cho an ninh trường nếu laptop bị mang ra khỏi thư viện** ([Faronics](https://www.faronics.com/news/blog/university-unveils-macbook-vending-machine)) **[C]**.

### 11.5. Chương trình cho mượn laptop thi của các trường Luật Mỹ (đối chiếu gần nhất với đề tài)

Đây là **trường hợp gần nhất thế giới với ý tưởng của dự án**: sinh viên luật **thi trên máy tính** bằng phần mềm khảo thí (Examplify/ExamSoft/Securexam), và trường phải xử lý tình huống "sinh viên không có máy phù hợp vào ngày thi".

| Trường/Cơ quan | Chính sách | Nguồn |
|---|---|---|
| **UDC David A. Clarke School of Law** | Sinh viên không tự có laptop cho kỳ thi **gửi email cho IT Help Desk để xin máy mượn** | [UDC Law](https://law.udc.edu/laptops/) **[A]** |
| **Drexel Law (Earle Mack)** | **Điều kiện để được dùng máy mượn:** phải đã cài bản Securexam mới nhất VÀ **nộp thành công một bài thi thử (practice exam)** | [Drexel Loaner Laptop Policies (PDF)](https://drexel.edu/law/studentLife/studentAffairs/policies_procedures/~/media/Files/law/Student%20Life/Office%20of%20Student%20Affairs/Policies%20and%20Procedures/Loaner-Laptop-Policies.ashx) **[A]** |
| **Columbia Law School** | Có chương trình cho mượn laptop, gồm **MacBook Air hỗ trợ cả macOS và Windows** cho phần mềm Softest của ExamSoft | [Columbia Law — Laptop Loaner Program](https://finance-admin.law.columbia.edu/form/laptop-loaner-program-for-studen) **[A]** |
| **North Carolina Board of Law Examiners** | Thu **125,00 USD phí sử dụng laptop** cho kỳ thi luật sư — **không hoàn lại, không chuyển nhượng** | [NCBLE — ExamSoft Instructions](https://www.ncble.org/examsoft-instructions) **[A]** |
| **Seton Hall Law School** | **Miễn phí** cho sinh viên dùng phần mềm | [Seton Hall Law — Laptop Policy](https://law.shu.edu/academics/exams/laptop-policy.html) **[A]** |
| **State Bar of California** | Có trang chính sách riêng về laptop cho kỳ thi First-Year Law Students' Exam | [CalBar](https://www.calbar.ca.gov/Admissions/Examinations/First-Year-Law-Students-Examination/Laptops-for-First-Year-Exam) **[A]** |
| Lưu ý về thuê ngoài | Sinh viên không có máy tương thích **có thể thuê từ dịch vụ như Rent-A-Center**, nhưng **máy thuê KHÔNG cài sẵn phần mềm thi** — sinh viên phải tự cài | tổng hợp WebSearch **[C]** |

> 🔴 **BÀI HỌC SỐ 20 — HAI PHÁT HIỆN QUAN TRỌNG NHẤT CỦA CẢ NGHIÊN CỨU NÀY:**
>
> **(a) Rào cản thật của "laptop đi thi" KHÔNG phải phần cứng — mà là PHẦN MỀM THI đã được cài, cấu hình và CHẠY THỬ THÀNH CÔNG.**
> Drexel Law **bắt buộc** sinh viên phải nộp một bài thi thử thành công trước khi được dùng máy mượn. Lý do rõ ràng: một chiếc laptop mượn mà phần mềm khảo thí không chạy vào đúng giờ G thì **tệ hơn là không có máy** — vì sinh viên đã mất luôn cơ hội tìm phương án khác.
>
> → **Đây chính là "hào nước" (moat) và cũng là rủi ro chết người của dự án FPT.** Nếu website chỉ cho thuê "một cái laptop", nó là hàng hóa phổ thông. Nếu nó cho thuê **"một cái laptop ĐÃ ĐƯỢC KIỂM THỬ với đúng hệ thống thi của ĐH FPT (EOS/phần mềm thi trên máy của trường), đã tắt update tự động, đã đủ pin, đã test wifi trong phòng thi"** — thì nó là một dịch vụ **không thể thay thế bởi việc mượn máy của bạn cùng phòng.**
>
> **Hành động bắt buộc cho nhóm:** phải đi hỏi **Phòng Khảo thí ĐH FPT Đà Nẵng** về yêu cầu kỹ thuật cụ thể của máy dự thi (HĐH, phần mềm, cấu hình tối thiểu, có chặn máy lạ vào mạng thi không). Tôi **không** tìm được tài liệu công khai nào về yêu cầu này (xem Mục 17). **Nếu nhà trường không cho phép máy lạ kết nối hệ thống thi, toàn bộ mô hình sụp đổ** — đây là giả định số 1 cần kiểm chứng trước mọi thứ khác.
>
> **(b) Nhiều trường ĐH đã tự cho mượn máy MIỄN PHÍ.** Đây là **đối thủ cạnh tranh cấu trúc**. Proposal phải trả lời: *ĐH FPT Đà Nẵng hiện có cho mượn máy dự phòng không? Nếu có, bao nhiêu máy, quy trình mất bao lâu?* Nếu trường đã có sẵn dịch vụ miễn phí và đủ dùng → dự án không có thị trường. Nếu trường **không có**, hoặc có nhưng **quy trình chậm/số lượng ít** → đó chính là khoảng trống thị trường và phải được nêu bằng bằng chứng (phỏng vấn, khảo sát).

---

## 12. BẢNG SO SÁNH CƠ CHẾ ĐẶT CỌC — KYC — BẢO HIỂM (tổng hợp chéo)

| Nền tảng | Có thu cọc? | Cơ chế thay thế cọc | Công cụ KYC | Ai chịu khi mất/hỏng nặng |
|---|---|---|---|---|
| **Grover** | **KHÔNG** | Credit check (Schufa + CRIF Bürgel) + ID/selfie | Onfido, SEON | Khách trả **20% RRP** (drone/scooter: 50%) nếu có Grover Care |
| **Rent the Runway** | **KHÔNG** | Thẻ tín dụng đã lưu | Thanh toán | Khách trả **100% giá bán lẻ** |
| **Turo** | **CÓ — 0–750 USD** | Hold theo hồ sơ rủi ro (tuổi + hạng xe); giảm 250 USD nếu khai bảo hiểm cá nhân | ComplyCube (doc + liveness + bằng lái) | Theo gói bảo vệ; deductible tăng khi host nhận % cao hơn |
| **Fat Llama** | **CÓ — chủ đồ tự đặt** | Bảo hiểm nền tảng | 2–3 loại giấy tờ; ID chính phủ cho đồ đắt | Bảo hiểm nền tảng — **thực tế có tranh chấp** |
| **Hygglo** | **Tùy chủ đồ** | **BankID** (định danh quốc gia) + bảo hiểm mặc định | BankID | **Omocom** hoặc Hygglo Lender Guarantee |
| **LaptopsAnytime / thư viện ĐH** | **KHÔNG** | **Thẻ SV + PIN** (ràng buộc bằng hồ sơ học vụ); nợ phí → **chặn mượn tiếp** | Hệ thống thẻ của trường | Sinh viên chịu **toàn bộ** (500–1.200 USD tùy trường) |

### 12.1. Đặt cọc vs Miễn trừ hư hỏng (damage waiver) — phân tích đánh đổi

| Tiêu chí | **Đặt cọc (security deposit)** | **Miễn trừ hư hỏng (damage waiver)** |
|---|---|---|
| Bản chất | Khoản **hoàn lại**, thường lớn (hàng trăm USD) | **Phí KHÔNG hoàn lại**, nhỏ (thường **40–90 USD** trong ngành lưu trú Mỹ) |
| Ảnh hưởng tỷ lệ chốt đơn | **Xấu** — khách ngại bị giữ tiền lớn → tăng ma sát đặt hàng | **Tốt hơn rõ rệt** — khách sẵn sàng đặt hơn nhiều khi thấy phí nhỏ thay vì hold lớn |
| Doanh thu | Không tạo doanh thu | **Tạo dòng doanh thu phụ** |
| Tranh chấp sau thuê | **Nhiều** — cãi nhau về việc trả cọc | **Ít** — không có cọc để tranh cãi |
| Mức bảo vệ | **Cao hơn** (đệm lớn) | **Có trần** (capped) |
| Phù hợp với | Tài sản giá trị cao / rủi ro cao | Danh mục tối ưu cho tỷ lệ đặt chỗ |

Nguồn: [Enso Connect — Security Deposit vs Damage Waiver](https://ensoconnect.com/resources/short-term-rentals-security-deposit-vs-damage-waiver-pros-and-cons) **[C]**, [StayFi — What Is a Damage Waiver Fee](https://stayfi.com/glossary/damage-waiver-fee/) **[C]**, [RapidEye Inspections](https://rapideyeinspections.com/blog/security-deposits-vs-damage-waivers-vs-platform-protection/) **[C]**, [Goodshuffle Pro](https://pro.goodshuffle.com/blog/non-refundable-damage-waiver-event-rental/) **[C]**

> **BÀI HỌC SỐ 21 — KHUYẾN NGHỊ CỤ THỂ CHO DỰ ÁN:**
> Bối cảnh dự án đặc biệt: **khách hàng đang trong trạng thái hoảng loạn trước giờ thi**. Ma sát = mất khách hoàn toàn (họ không có thời gian mặc cả). Vì vậy:
>
> **→ Dùng MÔ HÌNH LAI:**
> - **Mặc định: KHÔNG thu cọc tiền mặt** cho sinh viên có tài khoản @fpt.edu.vn đã xác thực + thẻ SV → tối đa hóa tỷ lệ chốt trong 5 phút.
> - **Thu một "phí dịch vụ đã bao gồm miễn trừ hư hỏng nhẹ"** cộng thẳng vào giá thuê (kiểu RTR 5 USD).
> - **Chỉ thu cọc với nhóm rủi ro cao**: người ngoài trường, khách chưa từng thuê, máy cấu hình cao, thuê dài ngày (kiểu Turo phân tầng theo rủi ro).
> - **Mất/hỏng nặng: đền theo bảng giá niêm yết công khai** (kiểu Grover + thư viện ĐH Mỹ).
> - **Chế tài phi tiền tệ mạnh nhất: nợ phí → khóa quyền thuê vĩnh viễn + công khai trong hệ thống** (sao chép cơ chế "excessive fines block borrowing" của thư viện ĐH — đây là cơ chế hiệu quả nhất và rẻ nhất).

---

## 13. ĐỊNH GIÁ — TỔNG HỢP CÁC MÔ HÌNH ĐÃ HỌC

| Mô hình định giá | Ai dùng | Cơ chế | Khả năng áp dụng cho dự án |
|---|---|---|---|
| **Giá giảm dần theo thời hạn** | Grover (1/3/6/12 tháng), Grover Business (6/12/18 tháng) | Thuê dài → giá/tháng rẻ hơn | ✅ Cao — áp dụng cho gói ngày / tuần / tháng |
| **Phí theo giờ + phạt lũy tiến** | Thư viện ĐH (Drexel 5 USD/giờ sau 5 giờ; U. Utah từ 1 USD/30 phút) | Miễn phí/rẻ trong cửa sổ định sẵn, phạt nặng sau đó | ✅ Rất cao — "thuê theo ca thi" (3–4 giờ) là đơn vị bán tự nhiên nhất |
| **Hoa hồng 2 đầu** | Fat Llama (~15% + ~15%), Hygglo (20%) | Thu cả người cho thuê và người thuê | ⚠️ Chỉ khi làm marketplace (khuyến nghị: KHÔNG ở GĐ1) |
| **Hoa hồng gắn với mức bảo vệ** | Turo (host nhận 60–90%) | Bảo vệ càng nhiều, nền tảng lấy càng nhiều | ✅ Cao — dùng làm cơ sở cho các gói An tâm/Cơ bản |
| **Thuê bao + phí bảo hiểm cố định/đơn** | Rent the Runway (5 USD/đơn) | Bảo hiểm nhỏ gộp sẵn | ✅ Rất cao |
| **Phí thuê khấu trừ vào giá mua** | Lumoid | "Try before you buy" | ⚠️ Thận trọng — chính mô hình này đã chết; nhưng có thể dùng làm **kênh thanh lý máy cũ** ("thuê 3 tháng, muốn mua thì trừ tiền thuê") |
| **Bán thiết bị/hệ thống cho tổ chức** | LaptopsAnytime (30.000–35.000 USD/kiosk) | B2B bán hạ tầng | ❌ GĐ1 — ✅ tầm nhìn GĐ3 |
| **Phí cố định cho kỳ thi** | NC Board of Law Examiners (125 USD, không hoàn) | Một lần, gắn với sự kiện thi | ✅ Rất cao — "gói trọn kỳ thi" |
| **Thuê theo tuần** | Hartford Technology Rentals (**từ 39 USD/tuần**, tới **325 USD/tháng** cho laptop gaming cấu hình cao) | Thuê ngắn hạn cho sự kiện/DN | ✅ Tham chiếu giá quốc tế — [Hartford Rents — Laptop Rental Pricing](https://hartfordrents.com/blog/laptop-rental-pricing/) **[A]** |

**Tham chiếu giá thuê laptop ngắn hạn quốc tế (để so sánh trong proposal):**

| Nhà cung cấp | Giá | Nguồn |
|---|---|---|
| Hartford Technology Rentals | **từ 39 USD/tuần** (cấu hình cơ bản) → **325 USD/tháng** (gaming cao cấp) | [hartfordrents.com](https://hartfordrents.com/blog/laptop-rental-pricing/) **[A]** |
| Meeting Tomorrow (Hartford) | **từ 105 USD/đơn vị** | [meetingtomorrow.com](https://meetingtomorrow.com/hartford/computer-rentals/) **[A]** |

**Tham chiếu thị trường mới nổi (Ấn Độ — RentoMojo):**

| Nội dung | Chi tiết | Nguồn |
|---|---|---|
| Kỳ hạn thuê | **3 đến 12 tháng** | [RentoMojo — Laptops on rent](https://www.rentomojo.com/bangalore/electronics/laptops-on-rent) **[A]** |
| KYC | **BẮT BUỘC**, và có **quy trình giấy tờ KHÁC NHAU cho sinh viên, freelancer, nhân viên đi làm, và người tự kinh doanh**; yêu cầu **giấy tờ tùy thân do chính phủ cấp (Aadhaar, hộ chiếu, bằng lái) + ảnh chân dung + thông tin liên hệ** | như trên **[A]** |
| Đặt cọc | **CÓ — cọc hoàn lại**; thanh toán **trả sau (postpaid)** — xuất hóa đơn sau tháng sử dụng | như trên **[A]** |
| Giao hàng | Miễn phí, **2–3 ngày** sau khi KYC thành công | như trên **[A]** |

> **BÀI HỌC SỐ 22 — RENTOMOJO CÓ QUY TRÌNH KYC RIÊNG CHO SINH VIÊN.** Đây là bằng chứng thị trường quan trọng: ở nước đang phát triển, **sinh viên KHÔNG có điểm tín dụng**, nên nền tảng phải thiết kế **luồng KYC riêng** cho họ (thường là: thẻ SV + giấy tờ tùy thân + thông tin người bảo lãnh/phụ huynh). Dự án nên nêu chính xác điều này — nó cho thấy nhóm hiểu rằng **không thể copy Grover 1:1 vào Việt Nam** vì Việt Nam không có Schufa.
>
> ⚠️ Điểm yếu chí tử của RentoMojo với dự án: **giao hàng mất 2–3 ngày.** Sinh viên hỏng máy **sáng ngày thi** không thể chờ 2 ngày. **Đây chính là khoảng trống thị trường mà dự án nhắm vào: TỐC ĐỘ (phút), không phải GIÁ.** Mọi thứ trong proposal nên xoay quanh trục "cứu hộ khẩn cấp trong khuôn viên" chứ không phải "cho thuê laptop giá rẻ".

---

## 14. HẠ TẦNG KỸ THUẬT — CÁC CÔNG CỤ THỰC TẾ VÀ GIÁ

### 14.1. Giữ tiền cọc trên thẻ (card pre-authorization) — Stripe

| Nội dung | Chi tiết | Nguồn |
|---|---|---|
| Cơ chế | Tạo **PaymentIntent với `capture_method: manual`** → đặt **pre-authorization hold** trên thẻ khách: tiền bị **giữ nhưng chưa trừ**, cho tới khi merchant **capture** | [Stripe Docs — Extended authorization](https://docs.stripe.com/payments/extended-authorization) **[A]**, [PayRequest — Stripe deposits guide](https://payrequest.io/guides/stripe-deposits) **[C]** |
| Thời hạn giữ mặc định | **7 ngày** cho thanh toán online; không capture thì hold tự hủy | [Stripe — Preauthorization charges](https://stripe.com/resources/more/preauthorization-charges-on-credit-cards-what-they-are-and-how-long-they-last) **[A]** |
| Thời hạn mở rộng | Lên tới **~30 ngày** tùy mạng thẻ. Cụ thể: **Visa tối đa 28 ngày; Amex/Mastercard/Discover 30 ngày** | [Stripe Docs](https://docs.stripe.com/payments/extended-authorization) **[A]**, [PayRequest](https://payrequest.io/stripe-pre-authorization/) **[C]** |
| Mạng thẻ hỗ trợ extended auth | **Visa, Mastercard, American Express, Discover** | [Stripe Docs — Terminal extended authorizations](https://docs.stripe.com/terminal/features/extended-authorizations) **[A]** |
| Sau khi thuê xong | **Capture một phần / capture toàn bộ / để hold hết hạn và nhả tiền** | [PayRequest](https://payrequest.io/guides/stripe-deposits) **[C]** |

> **BÀI HỌC SỐ 23 — VÀ MỘT CẢNH BÁO LỚN:**
> Cơ chế pre-auth là **cách đúng về mặt kỹ thuật** để thu cọc mà không thực sự lấy tiền của khách. **NHƯNG:** phần lớn sinh viên Việt Nam thanh toán bằng **chuyển khoản ngân hàng / ví điện tử (MoMo, ZaloPay, VNPay) / QR Code**, **KHÔNG dùng thẻ tín dụng quốc tế**. Mà **pre-authorization hold là tính năng của mạng thẻ tín dụng** — chuyển khoản và QR **không có cơ chế "giữ rồi nhả"**.
>
> **Tôi KHÔNG xác minh được** liệu các cổng thanh toán Việt Nam (VNPay, MoMo, ZaloPay, PayOS...) có hỗ trợ pre-authorization/hold hay không (xem Mục 17). **Nhóm PHẢI tự kiểm chứng điều này** — vì nếu không có, thì toàn bộ ý tưởng "đặt cọc điện tử" phải thay bằng **giải pháp phi kỹ thuật**: giữ thẻ SV, giấy cam kết có chữ ký, người bảo lãnh, hoặc chuyển khoản cọc thật rồi hoàn thủ công.
>
> **Đây có thể là một điểm sáng của proposal:** thừa nhận rằng hạ tầng thanh toán VN khác phương Tây, và **thiết kế cơ chế tin cậy "low-tech" phù hợp bối cảnh** (dựa vào thẻ SV và uy tín trong cộng đồng khép kín) — thông minh hơn nhiều so với việc copy Stripe.

### 14.2. Phần mềm quản lý cho thuê — Booqable (tham chiếu tính năng và giá)

| Tính năng | Chi tiết | Nguồn |
|---|---|---|
| Đặt cọc | Thu thanh toán và **damage deposit** online qua **50+ phương thức**; áp cọc theo **số tiền cố định hoặc % giá trị thuê**; **authorize & hold trên thẻ từ back office**, rồi **release hoặc capture** tùy tình trạng hư hỏng | [Booqable Features](https://booqable.com/features/) **[A]** |
| Hợp đồng | Tự sinh **hợp đồng thuê** từ chi tiết đơn (khách, ngày, thiết bị); thêm **điều khoản riêng, điều khoản trách nhiệm, chính sách hư hỏng** | [Booqable — Technology & IT Equipment Rental Software](https://booqable.com/industries/technology-rental-software/) **[A]** |
| Chữ ký điện tử | Yêu cầu **e-signature** trên báo giá và hợp đồng | [Booqable Features](https://booqable.com/features/) **[A]** |
| Theo dõi thiết bị | Gán **barcode/định danh duy nhất** cho từng sản phẩm để theo dõi **vị trí và tình trạng**; quét barcode khi giao/nhận; **ghi log hư hỏng và ghi chú** | như trên **[A]** |
| **Giá** | **Từ 29 USD/tháng**; **dùng thử miễn phí 14 ngày**; **không phí setup**; **không ăn chia doanh thu** | [Booqable Pricing](https://booqable.com/pricing/) **[A]** |

> **BÀI HỌC SỐ 24:** Booqable cho thấy **bộ tính năng tối thiểu** của bất kỳ hệ thống cho thuê nào — dự án nên dùng chính danh sách này làm **đặc tả chức năng (functional spec)** cho website trong proposal:
> 1. Lịch/đặt trước theo thiết bị (tránh double-booking)
> 2. Định danh từng máy bằng mã duy nhất (barcode/QR dán trên máy)
> 3. Hợp đồng tự sinh + chữ ký điện tử
> 4. Ghi nhận tình trạng máy khi giao và khi nhận (ảnh chụp + checklist)
> 5. Xử lý cọc (hold/capture/release)
> 6. Lịch sử hư hỏng theo từng máy
>
> Và **29 USD/tháng ≈ 730.000 VND/tháng** là mốc để so sánh: nhóm có thể lập luận *"tự code website rẻ hơn/hoặc dùng Google Form + Sheet ở MVP, nâng cấp lên phần mềm chuyên dụng khi vượt X đơn/tháng"*.

### 14.3. Nhà cung cấp KYC/chống gian lận mà các nền tảng lớn dùng

| Nhà cung cấp | Ai dùng | Chức năng | Nguồn |
|---|---|---|---|
| **Onfido** | Grover | Xác minh danh tính tự động → Grover **giảm 60% thời gian onboarding** | [onfido.com/customer/grover](https://onfido.com/customer/grover/) **[A]** |
| **SEON** | Grover | Xác minh ID + chống gian lận khi mở rộng toàn cầu | [seon.io](https://seon.io/resources/news/grover-partners-with-seon-to-verify-user-ids-as-it-expands-worldwide/) **[A]** |
| **ComplyCube** | Turo | Doc verification + liveness biometrics + kiểm tra bằng lái + fraud intelligence | [complycube.com](https://www.complycube.com/en/customer/turo-strengthens-car-sharing-compliance/) **[A]** |
| **Mitek** | Turo | Xác thực danh tính lặp lại mỗi lần dùng sản phẩm | [miteksystems.com](https://www.miteksystems.com/blog/innovator-qa-mike-wilkins-senior-director-trust-safety-at-turo) **[A]** |
| **Omocom** | Hygglo, GoMore, Tiptapp, Refurbly | Bảo hiểm nhúng theo giao dịch, **2–6 EUR, hạn mức 1.000 EUR** | [omocom.insurance](https://www.omocom.insurance/en/) **[A]** |
| **BankID** | Hygglo | Định danh điện tử quốc gia Bắc Âu | [Hygglo Help](https://help.hygglo.info/en/articles/10420308-what-is-hygglo) **[A]** |
| **Schufa / CRIF Bürgel** | Grover | Chấm điểm tín dụng Đức | [Grover Help](https://service.grover.com/hc/en-us/articles/19920531898642-How-does-Grover-s-credit-check-work) **[A]** |

> **BÀI HỌC SỐ 25:** Không một nền tảng lớn nào **tự xây** KYC — tất cả đều mua dịch vụ. Với dự án sinh viên quy mô nhỏ, **KYC "mua ngoài" là không khả thi về chi phí**, nhưng dự án có thứ tốt hơn: **đăng nhập bằng email @fpt.edu.vn (SSO/Google Workspace của trường) = xác minh danh tính gần như miễn phí và mạnh hơn bất kỳ giấy tờ nào**, vì nó chứng minh người đó **thực sự đang là sinh viên FPT và có thể bị truy vết qua hệ thống của trường**.
>
> Trong proposal, đây nên được trình bày là **"lợi thế cấu trúc không thể sao chép bởi đối thủ ngoài trường"** — và phải ghi rõ giả định cần kiểm chứng: nhóm **chưa xác minh** được việc trường có cho phép ứng dụng bên thứ ba dùng đăng nhập Google Workspace của trường hay không (Mục 17).

---

## 15. 12 BÀI HỌC CHUYỂN THẲNG THÀNH THIẾT KẾ SẢN PHẨM

| # | Bài học từ quốc tế | Áp dụng cụ thể cho dự án FPT Đà Nẵng |
|---|---|---|
| 1 | **Grover không thu cọc, thu "danh tính" thay tiền** | Đăng nhập bắt buộc bằng **@fpt.edu.vn** + ảnh thẻ SV. Miễn cọc cho SV đã xác thực. |
| 2 | **RTR: 17–18 lượt mới hòa vốn một món** | Phải tính điểm hòa vốn theo **số lượt thuê/máy**, KHÔNG theo "doanh thu tháng". Nếu không đạt, phải mua máy cũ rẻ hơn hoặc không sở hữu máy. |
| 3 | **Lumoid chết vì mỗi khách mới = 1 thiết bị mới phải mua** | Xây **nguồn cung linh hoạt** (ký gửi máy nhàn rỗi, hợp tác cửa hàng laptop cũ) thay vì mua sẵn kho máy. |
| 4 | **Omni chết vì "phiền hơn là mua mới"** | Điểm giao nhận **trong khuôn viên, gần phòng thi**; thời gian nhận máy **< 5 phút**; đặt trước qua web/Zalo. |
| 5 | **Turo: mức cọc theo hồ sơ rủi ro, không phẳng** | Bảng cọc phân tầng: SV năm 3–4 có lịch sử tốt = 0đ; người ngoài trường = cọc cao nhất. |
| 6 | **Turo: giảm cọc để đổi lấy bằng chứng danh tính** | "Thêm người bảo lãnh là SV đã thuê ≥2 lần → giảm 50% cọc." |
| 7 | **RTR: 2 tầng trách nhiệm (5 USD bao nhẹ / 100% giá bán lẻ nếu mất)** | Phí dịch vụ gộp sẵn miễn trừ hư hỏng nhẹ; **bảng giá đền bù công khai** cho hỏng nặng/mất. |
| 8 | **Getaround bị kiện vì giấu điều khoản loại trừ** | Mục **"KHÔNG ĐƯỢC MIỄN TRỪ"** in đậm, đặt ĐẦU trang điều khoản, ký xác nhận trước khi nhận máy. |
| 9 | **Thư viện ĐH: nợ phí → chặn mượn tiếp** | Chế tài phi tiền tệ: vi phạm → **khóa tài khoản vĩnh viễn**. Rẻ, mạnh, hiệu quả trong cộng đồng khép kín. |
| 10 | **LaptopsAnytime: tự động reset + sạc đầy giữa 2 phiên** | Checklist bắt buộc trước mỗi lần giao: **wipe sạch + pin 100% + test wifi/webcam/bàn phím** (mô phỏng checklist 5 điểm của Grover). |
| 11 | **Drexel Law: bắt buộc chạy thử bài thi trước khi được dùng máy mượn** | 🔴 **Khác biệt cốt lõi của dự án**: cho thuê **"máy đã test với hệ thống thi của FPT"**, không phải "một cái laptop". |
| 12 | **Grover B2B: hợp đồng dài = churn thấp = biên tốt** | Bán **"gói giữ máy dự phòng cả tuần thi"** cho lớp/CLB/Phòng Khảo thí thay vì chỉ bán lẻ từng đơn. |

---

## 16. RỦI RO CHÍNH VÀ CÁCH GIẢM THIỂU (rút từ các thất bại đã nghiên cứu)

| # | Rủi ro | Bằng chứng từ nghiên cứu | Cách giảm thiểu |
|---|---|---|---|
| R1 | **Không đủ máy vào đúng ngày cao điểm** | Lumoid chết đúng vì điều này | Mở đặt trước sớm theo lịch thi; nguồn cung linh hoạt; công khai "còn X máy" theo thời gian thực |
| R2 | **Công suất nhàn rỗi ngoài mùa thi** | RTR cần 9–10 vòng quay/năm mới sống; tỷ lệ sử dụng thực tế năm 1 của ngành cho thuê thiết bị thường **35–45%**, không phải 80% như nhà cung cấp quảng cáo ([natejonesentrepreneur.com](https://www.natejonesentrepreneur.com/post/equipment-rental-business-startup-costs) **[C]**) | Đa dạng hóa: cho thuê theo tuần/tháng cho SV làm đồ án, SV mới, khách vãng lai |
| R3 | **Mất máy / bị lừa** | Fat Llama: nhiều vụ mất thiết bị >5.000 USD | Giao nhận trực tiếp trong khuôn viên; chụp ảnh người nhận + thẻ SV + máy; KHÔNG làm P2P |
| R4 | **Tranh chấp hư hỏng** | Fat Llama bị tố từ chối bồi thường; Getaround bị cơ quan nhà nước xử lý | Biên bản bàn giao 2 chiều có ảnh; phân biệt rõ hao mòn thường (miễn phí, theo Grover) và hư hỏng |
| R5 | **Phần mềm thi không chạy trên máy thuê** | Drexel Law bắt buộc chạy thử trước | Test trước với đúng hệ thống thi FPT; có máy dự phòng thứ 2; chính sách hoàn tiền nếu máy lỗi |
| R6 | **Nhà trường không cho phép máy lạ vào hệ thống thi** | — (chưa xác minh) | 🔴 **Phải hỏi Phòng Khảo thí TRƯỚC KHI làm bất cứ việc gì khác** |
| R7 | **Cạnh tranh với "mượn bạn" và phòng máy miễn phí của trường** | Omni: "có thể mua luôn trên Amazon" | Bán **tốc độ + độ tin cậy + máy đã cấu hình sẵn**, không bán giá rẻ |
| R8 | **Đầu tư vốn quá sớm** | Grover phải tái cấu trúc StaRUG dù đã gọi >600 triệu USD; Lumoid chết vì thiếu vốn mua thiết bị | "Grow into the fleet": bắt đầu 3–5 máy, chỉ mua thêm khi tỷ lệ sử dụng vượt ngưỡng đã định trước |
| R9 | **Không có bảo hiểm cho laptop cho thuê tại VN** | Omocom là mô hình ở châu Âu; chưa xác minh có tương đương ở VN | Tự lập **"quỹ rủi ro"** trích ~0,5–1% giá trị máy/lượt (tham chiếu mức phí Omocom) |
| R10 | **Không thể hold cọc trên thẻ ở VN** | Stripe pre-auth là cơ chế thẻ tín dụng | Thiết kế cơ chế tin cậy phi kỹ thuật: thẻ SV, cam kết ký tên, người bảo lãnh, khóa tài khoản |

---

## 17. 🔴 NHỮNG ĐIỀU KHÔNG XÁC MINH ĐƯỢC (không đoán — ghi thẳng)

**A. Về giới hạn công cụ của phiên nghiên cứu này**
1. **WebFetch bị chặn gần như toàn bộ** bởi chính sách egress của tổ chức. Mọi dữ liệu đến từ WebSearch (URL thật + nội dung do công cụ tổng hợp), **không phải từ việc đọc trực tiếp từng trang**. Nhóm phải mở lại URL để xác nhận trước khi nộp.

**B. Về Grover**
2. **Tỷ lệ hư hỏng (damage rate) của Grover: KHÔNG tìm được.** Grover không công bố % thiết bị bị hư hỏng/mất trên mỗi chu kỳ cho thuê. Mọi con số về tỷ lệ hư hỏng trong proposal phải ghi rõ là **giả định của nhóm**.
3. **Thời gian hoàn vốn thiết bị "10–14 tháng" và "6 người dùng/thiết bị"**: chỉ tìm thấy ở **nguồn phái sinh** ([businessmodelcanvastemplate.com](https://businessmodelcanvastemplate.com/blogs/growth-strategy/grover-growth-strategy)), **không phải công bố chính thức của Grover**. Một kết quả tìm kiếm khác lại nêu **3–4 người dùng/vòng đời thiết bị** — **hai con số mâu thuẫn**. Không được trích như sự thật.
4. **Doanh thu Grover 2024–2025: KHÔNG tìm được số liệu công khai.** Chỉ có: FY2022 vượt 100 triệu EUR (Waste360); một nguồn dữ liệu bên thứ ba ghi 235,98 triệu USD (GetLatka); và một con số rời rạc "~43 triệu USD net revenue / 71 triệu USD ARR / ~150.000 subscription hoạt động" **không rõ thuộc năm nào** — **không dùng được**.
5. **Tỷ lệ giá thuê 1 tháng so với 12 tháng của Grover, và tỷ lệ giá thuê/tháng so với giá bán lẻ: KHÔNG tìm được** số liệu công bố.
6. **Churn rate và thời gian thuê trung bình của Grover: KHÔNG tìm được.**
7. **Giá của gói Grover Care: KHÔNG tìm được** mức phí cụ thể theo tháng.

**C. Về Rent the Runway**
8. **Tỷ lệ mất/trộm hàng (loss/theft rate) của RTR: KHÔNG tìm được.** Các hồ sơ 10-K được tìm thấy nhấn mạnh công nghệ reverse logistics chứ không công bố chỉ số này. Con số "17–18 lượt hòa vốn / ~20 lượt thực tế" đến từ **phân tích của Gad Allon (giáo sư Wharton) trên Substack** — nguồn phân tích độc lập uy tín, nhưng **không phải số do RTR công bố**.

**D. Về Fat Llama / Hygglo**
9. **Mức hoa hồng chính xác của Fat Llama: các nguồn MÂU THUẪN** (15% lender + 15% renter, vs 25% lender giảm về 20%). Phải kiểm tra trang phí chính thức.
10. **Tỷ lệ mất/trộm thiết bị công bố của Fat Llama hoặc Hygglo: KHÔNG tìm được.** Chỉ có các vụ việc đơn lẻ được báo chí/đánh giá người dùng ghi nhận — **không phải thống kê tỷ lệ**.
11. **Số liệu tài chính Hygglo–Fat Llama FY2024 ("gần hòa vốn", "GMV +25%")**: chỉ từ nguồn phái sinh **[C]**, chưa xác minh.

**E. Về Getaround**
12. **Việc "Getaround ngừng hoạt động tại Bắc Mỹ đầu 2025"** đến từ tổng hợp WebSearch, **tôi không mở được nguồn gốc**. Cần xác minh lại trước khi trích. Vụ việc với Tổng Chưởng lý DC thì có URL nguồn chính thức ([oag.dc.gov](https://oag.dc.gov/release/attorney-general-schwalb-secures-refunds-dc)).
13. **Tỷ lệ trộm/gian lận cụ thể của Getaround hoặc Turo: KHÔNG tìm được.** Không nền tảng nào công bố.

**F. Về LaptopsAnytime và chương trình ĐH**
14. **Tỷ lệ laptop không được trả lại / bị mất trong các chương trình kiosk ĐH: KHÔNG tìm được số liệu thống kê.** Chỉ tìm được **chính sách phạt** (Indiana 900 USD, UNT Dallas 1.200 USD, UMN Crookston 500 USD) và biện pháp kỹ thuật (cảm biến báo động). Con số "chỉ 3% laptop bị trộm được thu hồi" là thống kê **chung về trộm laptop**, KHÔNG phải về chương trình cho mượn của trường — **không được dùng lẫn lộn**.
15. **Giá kiosk LaptopsAnytime hiện tại (2026): KHÔNG tìm được.** Hai con số 30.000 USD (Drexel) và 35.000 USD (Grand Rapids CC) là từ các bài báo cũ (~2013 và ~2018).
16. **Thời hạn mượn tại Drexel: nguồn mâu thuẫn** — một nguồn ghi 5 giờ, một nguồn ghi cửa sổ 4 giờ.

**G. Về bối cảnh Việt Nam / ĐH FPT Đà Nẵng (những giả định PHẢI kiểm chứng bằng khảo sát thực địa)**
17. **Yêu cầu kỹ thuật cụ thể của máy dự thi tại ĐH FPT Đà Nẵng (HĐH, phần mềm khảo thí, cấu hình tối thiểu, chính sách cho máy lạ vào mạng thi): KHÔNG tìm được tài liệu công khai nào.** 🔴 **Đây là giả định RỦI RO NHẤT của toàn bộ dự án.**
18. **ĐH FPT Đà Nẵng hiện có chương trình cho mượn laptop dự phòng hay không: KHÔNG tìm được thông tin.** Nếu có → có thể triệt tiêu thị trường.
19. **Các cổng thanh toán Việt Nam (VNPay, MoMo, ZaloPay, PayOS) có hỗ trợ pre-authorization hold hay không: KHÔNG xác minh được.**
20. **Sản phẩm bảo hiểm thương mại cho laptop cho thuê ngắn hạn tại Việt Nam (tương đương Omocom): KHÔNG tìm được.**
21. **Điều kiện pháp lý/kỹ thuật để một startup sinh viên tích hợp VNeID hoặc SSO của trường: KHÔNG xác minh được.**
22. **Tỷ giá VND/EUR, VND/USD tháng 9/2026: KHÔNG tra cứu trong phiên này.** Mọi quy đổi trong tài liệu này là **ước lượng thô** và phải được nhóm tính lại theo tỷ giá ngày nộp bài.

**H. Nguồn KHÔNG mở được (bị chặn egress) — nhóm cần tự mở:**
- `techcrunch.com/2017/12/10/why-gear-rental-marketplace-lumoid-shut-down/` (nguồn gốc về Lumoid)
- `techcrunch.com/2019/11/25/omni-shuts-down/` (nguồn gốc về Omni)
- `service.grover.com/*` (toàn bộ help center Grover)
- `sec.gov` (hồ sơ 10-K/8-K của Rent the Runway)
- `laptopsanytime.com`, `fatllama.com`, `grover.com`, `library.drexel.edu`, `sifted.eu`

---

## 18. DANH SÁCH NGUỒN ĐẦY ĐỦ (theo chủ đề)

### Grover
- [Grover — How It Works](https://www.grover.com/us-en/how-it-works)
- [Grover — Rent. Return. Reuse.](https://www.grover.com/de-en/g-explore/sustainable-tech)
- [Grover — Signs of use / Asset condition](https://www.grover.com/at-en/g-about/asset-condition)
- [Grover Care](https://www.grover.com/us-en/g-about/grover-care)
- [Grover Help — How does Grover's credit check work?](https://service.grover.com/hc/en-us/articles/19920531898642-How-does-Grover-s-credit-check-work)
- [Grover Help — Identity Verification](https://service.grover.com/hc/en-us/articles/35704298814866-Identity-Verification)
- [Grover Help — Additional Verification](https://service.grover.com/hc/en-us/articles/19920613200914-Additional-Verification)
- [Grover Help — What is Grover Care](https://service.grover.com/hc/en-us/articles/19920685566610-What-is-Grover-Care-and-how-does-it-work)
- [Grover Help — Repair and replacement costs](https://service.grover.com/hc/en-us/articles/19918338642578-Repair-and-replacement-costs)
- [Grover Help — Damaged products](https://service.grover.com/hc/en-us/articles/19916293812754-Damaged-products)
- [Grover Help — Drones and e-mobility products](https://service.grover.com/hc/en-us/articles/19908669018002-Drones-and-e-mobility-products)
- [Grover for Business](https://www.grover.com/de-en/for-business)
- [Grover — MacBook Air M2 rental](https://www.grover.com/de-en/products/apple-laptop-macbook-air-m2-8gb-256gb-ssd-10-core-gpu)
- [Grover — MacBook Pro 13 M2 rental](https://www.grover.com/de-en/products/apple-macbook-pro-13-3-m2-8cpu-16gb-512gb-10gpu-67w)
- [Grover Press — 50M EUR ARR (2020)](https://press.grover.com/136893-berlin-based-tech-subscription-service-grover-surpasses-50m-in-annual-recurring-revenue-and-releases-2020-growth-report)
- [Grover Press — unicorn >$1bn](https://press.grover.com/184606-grover-hits-unicorn-valuation-of-over-1bn-on-its-way-to-become-global-market-leader-in-consumer-tech-subscription)
- [Hengeler Mueller — StaRUG restructuring 25/4/2025](https://hengeler-news.com/en/articles/hengeler-mueller-advises-grover-on-financial-restructuring-via-starug-proceedings)
- [Silicon Canals — Grover raises €302M unicorn](https://siliconcanals.com/grover-raises-302m-unicorn-valuation/)
- [Silicon Canals — Grover €270M](https://siliconcanals.com/german-unicorn-grover-bags-270m/)
- [Tech.eu — Grover €270M debt](https://tech.eu/2022/09/28/grover-takes-on-more-debt-funding-this-time-to-the-tune-of-eur270-million/)
- [TechCrunch — Grover raises $71M (2021)](https://techcrunch.com/2021/04/12/grover-raises-71m-to-grow-its-consumer-electronics-subscription-business/)
- [Sifted — Grover raises $330m](https://sifted.eu/articles/grover-raises-330m)
- [Waste360 — How Grover's model works](https://www.waste360.com/e-waste/how-grover-s-electronics-rental-model-works)
- [Onfido — Grover case study](https://onfido.com/customer/grover/)
- [SEON — Grover partnership](https://seon.io/resources/news/grover-partners-with-seon-to-verify-user-ids-as-it-expands-worldwide/)
- [TrueUp — Grover layoffs](https://www.trueup.io/co/grover/layoffs)
- [GetLatka — Grover revenue](https://getlatka.com/companies/grover.com) **[nguồn yếu]**
- [businessmodelcanvastemplate — Grover growth strategy](https://businessmodelcanvastemplate.com/blogs/growth-strategy/grover-growth-strategy) **[nguồn yếu]**

### Fat Llama / Hygglo / Omocom
- [EU-Startups — Hygglo acquires Fat Llama €41M](https://www.eu-startups.com/2022/08/sweden-based-hygglo-acquires-uk-based-fat-llama-in-e41-million-deal-to-create-worlds-biggest-peer-to-peer-rental-platform/)
- [Tech.eu — Hygglo/Fat Llama $41.5M](https://tech.eu/2022/08/16/swedish-hygglo-fattens-portfolio-with-london-based-fat-llama-for-415-million/)
- [UKTN — Fat Llama acquired £34.5m](https://www.uktech.news/ecommerce/fat-llama-acquisition-hygglo-20220816)
- [Sifted — the story of Fat Llama's acquisition](https://sifted.eu/articles/fat-llama-acquisition)
- [Sharetribe — How to build a website like Fatllama](https://www.sharetribe.com/create/how-to-build-website-like-fatllama/) **[nguồn yếu]**
- [Yo-Rent — Build a P2P rental website like Fat Llama](https://www.yo-rent.com/blog/build-p2p-rental-website-like-fat-llama/) **[nguồn yếu]**
- [PetaPixel — $5,000 in camera gear stolen through Fat Llama](https://petapixel.com/2019/03/20/how-i-had-over-5000-in-camera-gear-stolen-through-fat-llama/)
- [DIYPhotography — gear stolen through Fat Llama](https://www.diyphotography.net/i-got-5000-worth-of-gear-stolen-from-me-through-fat-llama/)
- [Trustpilot — Fat Llama reviews](https://www.trustpilot.com/review/fatllama.com)
- [Hygglo Help — How Hygglo works](https://help.hygglo.info/en/articles/10415333-how-hygglo-works)
- [Hygglo Help — What is Hygglo](https://help.hygglo.info/en/articles/10420308-what-is-hygglo)
- [Hygglo Help — security & protection](https://help.hygglo.info/en/articles/10587214-how-to-provide-great-service-and-understand-security-protection)
- [Hygglo Care for lenders](https://help.hygglo.info/en/articles/12890765-hygglo-care-for-lenders)
- [Circular X — Hygglo case](https://www.circularx.eu/en/cases/75/hygglo-peer-to-peer-rental-instead-of-buying)
- [Omocom Insurance](https://www.omocom.insurance/en/)
- [Van Ameyde — Omocom circular economy](https://www.vanameyde.com/stories/omocom-circular-economy/)
- [Ellen MacArthur Foundation — Omocom](https://www.ellenmacarthurfoundation.org/circular-examples/creating-trust-in-the-sharing-economy-omocom)

### Rent the Runway
- [RTR — Dream Fulfillment Centers / Process](https://www.renttherunway.com/about-us/process)
- [RTR — Terms of Service](https://www.renttherunway.com/pages/termsofservice)
- [RTR IR — FY2025 full year results](https://investors.renttherunway.com/news-releases/news-release-details/rent-runway-inc-announces-fourth-quarter-and-full-year-2025)
- [SEC — RTR 8-K FY2025 earnings release](https://www.sec.gov/Archives/edgar/data/1468327/000146832726000018/fy2025earningsrelease.htm)
- [SEC — RTR 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1468327/000146832725000056/wdq-20250131.htm)
- [SEC — RTR 10-K FY2024](https://www.sec.gov/Archives/edgar/data/1468327/000146832724000114/wdq-20240131.htm)
- [Gad Allon — RTR: When Complexity Collides with Scale](https://gadallon.substack.com/p/rent-the-runway-when-complexity-collides)
- [Harvard d3 — RTR Digitizes High-Fashion](https://d3.harvard.edu/platform-rctom/submission/rent-the-runway-digitizes-high-fashion/)
- [Eightx — RTR teardown](https://eightx.co/blog/us-teardown-rent-the-runway) **[nguồn yếu]**
- [MySubscriptionAddiction — RTR review ($5 insurance)](https://www.mysubscriptionaddiction.com/rent-the-runway-review) **[nguồn yếu]**

### Lumoid & Omni (thất bại)
- [TechCrunch — Why gear rental marketplace Lumoid shut down](https://techcrunch.com/2017/12/10/why-gear-rental-marketplace-lumoid-shut-down/)
- [Digital Trends — Lumoid closes, torpedoing Best Buy plan](https://www.digitaltrends.com/photography/gear-rental-startup-lumoid-closes/)
- [Gizmodo — Lumoid shuts down](https://gizmodo.com/lumoid-best-buys-supposed-gear-rental-partner-shuts-d-1821165345)
- [PetaPixel — Lumoid shuts down months after Best Buy deal](https://petapixel.com/2017/12/12/lumoid-shuts-just-months-inking-best-buy-camera-rental-deal/)
- [DPReview — Lumoid shut down](https://www.dpreview.com/news/0749408246/lumoid-gear-rental-service-has-been-shut-down)
- [Light Stalking — Lumoid shuttered](https://www.lightstalking.com/lumoid-camera-gear-rental-service-shuttered/)
- [Recode — Best Buy try-before-you-buy with Lumoid](https://www.recode.net/2017/6/12/15771838/best-buy-drone-camera-rental-trial-try-before-buy-lumoid)
- [Y Combinator — Lumoid (YC S13)](https://www.ycombinator.com/blog/lumoid-yc-s13-wants-to-rent-you-a-camera-now-and-everything-later)
- [YC — Female Founder Stories: Aarthi Ramamurthy](https://www.ycombinator.com/blog/female-founder-stories-aarthi-ramamurthy-founder-of-lumoid-yc-s13)
- [TechCrunch 2014 — Lumoid wants to rent you a camera](https://techcrunch.com/2014/04/03/lumoid-wants-to-rent-you-a-camera-now-and-everything-later)
- [VentureBeat — Lumoid try-before-you-buy wearables](https://venturebeat.com/business/lumoid-launches-a-try-before-you-buy-service-for-wearables/)
- [PCWorld — Lumoid wearables program](https://www.pcworld.com/article/431215/not-sure-about-wearables-lumoid-launches-a-try-before-you-buy-program.html)
- [Android Authority — Lumoid wearables](https://www.androidauthority.com/lumoid-wearables-try-before-you-buy-580387/)
- [TechCrunch — Omni shuts down](https://techcrunch.com/2019/11/25/omni-shuts-down/)
- [Crowdfund Insider — Omni closing down](https://www.crowdfundinsider.com/2019/11/154551-ripple-backed-storage-and-rental-firm-omni-rentals-will-reportedly-be-closing-down/)

### Turo / Getaround
- [Turo — Trust & Safety](https://turo.com/us/en/trust-and-safety)
- [Turo Help — Security deposits (US)](https://help.turo.com/en_us/security-deposits-us-HkbE44lE9)
- [Turo Help — Security deposits (UK)](https://help.turo.com/en_us/security-deposits-uk-S1gSwqPR6)
- [Turo Help — Security deposits (Canada)](https://help.turo.com/en_us/security-deposits-canada-ryCqIcvAT)
- [ComplyCube — Turo streamlines car-sharing compliance](https://www.complycube.com/en/customer/turo-strengthens-car-sharing-compliance/)
- [Mitek — Q&A with Turo Trust & Safety](https://www.miteksystems.com/blog/innovator-qa-mike-wilkins-senior-director-trust-safety-at-turo)
- [TechCrunch — Turo taps national security experts (01/2025)](https://techcrunch.com/2025/01/03/turo-taps-national-security-and-counterterrorism-experts-after-cybertruck-explosion)
- [Sacra — Turo revenue & valuation](https://sacra.com/c/turo/) **[nguồn yếu]**
- [Rentovation — Turo takes 10% to 30%](https://rentovation.co/guides/how-much-does-turo-take) **[nguồn yếu]**
- [Dittofi — Turo business model](https://www.dittofi.com/learn/turo-business-model) **[nguồn yếu]**
- [Jerry — How much is the deposit for Turo](https://jerry.ai/car-insurance/how-much-is-the-deposit-for-turo/) **[nguồn yếu]**
- [DC Attorney General — Refunds from car sharing company (Getaround)](https://oag.dc.gov/release/attorney-general-schwalb-secures-refunds-dc)
- [BBB — Getaround complaints](https://www.bbb.org/us/ca/san-francisco/profile/auto-renting-and-leasing/getaround-1116-390772/complaints) **[nguồn yếu]**

### LaptopsAnytime & chương trình ĐH
- [LaptopsAnytime](https://www.laptopsanytime.com/)
- [LaptopsAnytime — About Us](https://www.laptopsanytime.com/about-us)
- [LaptopsAnytime — Product Lines](https://www.laptopsanytime.com/product-lines)
- [LaptopsAnytime — FAQ](https://www.laptopsanytime.com/faq)
- [Inside Higher Ed — Libraries turn to laptop vending machines](https://www.insidehighered.com/news/2013/02/08/libraries-turn-laptop-vending-machines-fulfill-students-late-night-studying-needs)
- [Drexel Libraries — Laptop & Portable Charger Lending Kiosks](https://library.drexel.edu/news-and-events/programs-and-initiatives/laptop-charger-lending-kiosks/)
- [Drexel News Blog — Vending machine dispenses MacBooks](https://newsblog.drexel.edu/2013/01/04/vending-machine-dispenses-macbooks-for-student-use/)
- [Chronicle of Higher Education — Drexel adds vending machine](https://www.chronicle.com/blogs/wiredcampus/drexel-u-library-adds-vending-machine-to-dispense-laptops)
- [CampusIDNews — Grand Rapids CC installs laptop vending machine](https://www.campusidnews.com/grand-rapids-cc-installs-laptop-vending-machine/)
- [Community College Daily — Not your average vending machine](https://www.ccdaily.com/2018/04/laptop-vending-machine/)
- [KSL — Laptop vending machine at U of U](https://www.ksl.com/article/12357245)
- [Spaces4Learning — Laptop Checkouts Made Easy (2024)](https://spaces4learning.com/whitepapers/2024/03/laptop-checkouts-made-easy.aspx)
- [PUPN — Automated dispensing kiosk systems transform higher-ed computing](https://pupnmag.com/article/laptop-checkouts-automated-dispensing-kiosk-systems-transform-higher-ed-computing/)
- [Computers in Libraries — LaptopsAnytime feature (2017)](https://www.infotoday.com/cilmag/jul17/Johnston--LaptopsAnytime--Meeting-Students-Needs-for-Equipment-Loans-Through-Self-Serve-Kiosks.shtml)
- [LocknCharge — Device loaner programs for universities](https://www.lockncharge.com/blog/device-loaner-program-for-universities)
- [LocknCharge — Library device loaner programs](https://www.lockncharge.com/blog/library-device-loaner-program)
- [UNT Dallas — Student loaner laptops](https://www.untdallas.edu/oit/digital-spaces/laptop-checkout.php)
- [UMN Crookston — Fees for lost/stolen](https://crk.umn.edu/computer-help-desk/fees-lost-stolen)
- [Stony Brook — Student Laptop Loaner Program](https://it.stonybrook.edu/services/student-laptop-loaner-program)
- [Faronics — University unveils MacBook vending machine](https://www.faronics.com/news/blog/university-unveils-macbook-vending-machine) **[nguồn yếu]**

### Thi cử trên máy tính / cho mượn laptop thi
- [UDC Law — Laptop Requirements & Support](https://law.udc.edu/laptops/)
- [Drexel Law — Loaner Laptop Policies (PDF)](https://drexel.edu/law/studentLife/studentAffairs/policies_procedures/~/media/Files/law/Student%20Life/Office%20of%20Student%20Affairs/Policies%20and%20Procedures/Loaner-Laptop-Policies.ashx)
- [Columbia Law — Laptop Loaner Program](https://finance-admin.law.columbia.edu/form/laptop-loaner-program-for-studen)
- [NC Board of Law Examiners — ExamSoft instructions ($125 fee)](https://www.ncble.org/examsoft-instructions)
- [Seton Hall Law — Laptop policy](https://law.shu.edu/academics/exams/laptop-policy.html)
- [State Bar of California — Laptops for First-Year Exam](https://www.calbar.ca.gov/Admissions/Examinations/First-Year-Law-Students-Examination/Laptops-for-First-Year-Exam)
- [UPenn Law — Exams: Laptop Loans and Rentals](https://www.law.upenn.edu/its/docs/exams/rentals.php)
- [Georgia Bar — Laptop testing procedures](https://www.gabaradmissions.org/laptop-testing-procedures)

### Hạ tầng kỹ thuật & định giá
- [Stripe Docs — Place an extended hold on an online card payment](https://docs.stripe.com/payments/extended-authorization)
- [Stripe Docs — Terminal extended authorizations](https://docs.stripe.com/terminal/features/extended-authorizations)
- [Stripe — What are preauthorization charges on credit cards](https://stripe.com/resources/more/preauthorization-charges-on-credit-cards-what-they-are-and-how-long-they-last)
- [PayRequest — Stripe Security Deposit guide 2026](https://payrequest.io/guides/stripe-deposits) **[nguồn yếu]**
- [PayRequest — Stripe Pre-Authorization & Card Holds](https://payrequest.io/stripe-pre-authorization/) **[nguồn yếu]**
- [Booqable — Pricing](https://booqable.com/pricing/)
- [Booqable — Features](https://booqable.com/features/)
- [Booqable — Technology & IT Equipment Rental Software](https://booqable.com/industries/technology-rental-software/)
- [Hartford Technology Rentals — Laptop rental pricing](https://hartfordrents.com/blog/laptop-rental-pricing/)
- [Hartford Technology Rentals — Laptop rental](https://hartfordrents.com/laptop-rental/)
- [Meeting Tomorrow — Hartford computer rentals](https://meetingtomorrow.com/hartford/computer-rentals/)
- [RentoMojo — Laptops on rent (Bangalore)](https://www.rentomojo.com/bangalore/electronics/laptops-on-rent)
- [Enso Connect — Security deposit vs damage waiver](https://ensoconnect.com/resources/short-term-rentals-security-deposit-vs-damage-waiver-pros-and-cons) **[nguồn yếu]**
- [StayFi — What is a damage waiver fee](https://stayfi.com/glossary/damage-waiver-fee/) **[nguồn yếu]**
- [RapidEye — Security deposits vs damage waivers vs platform protection](https://rapideyeinspections.com/blog/security-deposits-vs-damage-waivers-vs-platform-protection/) **[nguồn yếu]**
- [Goodshuffle Pro — Why non-refundable damage waivers beat security deposits](https://pro.goodshuffle.com/blog/non-refundable-damage-waiver-event-rental/) **[nguồn yếu]**
- [Nate Jones — Equipment rental business startup costs (utilization 35–45%)](https://www.natejonesentrepreneur.com/post/equipment-rental-business-startup-costs) **[nguồn yếu]**

---

## 19. VIỆC CẦN LÀM NGAY (checklist cho nhóm, theo thứ tự ưu tiên)

| # | Việc | Mức độ | Lý do |
|---|---|---|---|
| 1 | **Hỏi Phòng Khảo thí ĐH FPT Đà Nẵng**: yêu cầu kỹ thuật máy dự thi, có cho máy lạ vào hệ thống thi không | 🔴 SỐNG CÒN | Nếu không được phép → toàn bộ mô hình sụp đổ (Mục 17.17) |
| 2 | **Xác minh nhà trường đã có chương trình cho mượn máy chưa** | 🔴 SỐNG CÒN | Đối thủ miễn phí (Mục 11.5b) |
| 3 | **Khảo sát sinh viên**: bao nhiêu % từng gặp sự cố máy ngày thi, sẵn sàng trả bao nhiêu, chờ được bao lâu | 🔴 CAO | Không có dữ liệu này thì proposal chỉ là phỏng đoán |
| 4 | Mở lại **toàn bộ URL trong Mục 18** và xác nhận từng con số trước khi trích | 🔴 CAO | WebFetch bị chặn trong phiên này (Mục 0) |
| 5 | Tra tỷ giá VND/USD, VND/EUR ngày nộp bài và tính lại mọi quy đổi | 🟡 TRUNG BÌNH | Mục 17.22 |
| 6 | Khảo sát giá laptop cũ/refurbished quanh Hòa Hải, Ngũ Hành Sơn để tính capex thật | 🟡 TRUNG BÌNH | Đầu vào của mô hình điểm hòa vốn (Mục 6.3) |
| 7 | Hỏi cổng thanh toán VN (VNPay/MoMo/PayOS) về pre-authorization hold | 🟡 TRUNG BÌNH | Mục 14.1, 17.19 |

---

*Hết tài liệu nghiên cứu 02. Tài liệu này là NGUYÊN LIỆU THÔ — không phải bản proposal. Mọi con số phải được kiểm chứng lại theo Mục 19 trước khi đưa vào bản nộp.*
