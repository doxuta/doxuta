# 10 — Mô hình cho mượn / cho thuê laptop trong trường đại học (thế giới & Việt Nam)

**Ngày nghiên cứu:** 14/09/2026
**Phục vụ:** Proposal khởi nghiệp — Website cho thuê laptop đi thi, quy mô 15–40 máy, quanh ĐH FPT Đà Nẵng (P. Hoà Hải, Ngũ Hành Sơn, Đà Nẵng)
**Bối cảnh đã xác minh (do nhóm cung cấp):** SV FPT thi trên máy cá nhân bằng EOS + Safe Exam Browser, bắt buộc Windows; Mac M1/M2 không thi được.

---

## ⚠️ CẢNH BÁO PHƯƠNG PHÁP — ĐỌC TRƯỚC KHI DÙNG SỐ LIỆU

1. **WebFetch/curl bị chặn hoàn toàn (EGRESS_BLOCKED)** trong phiên nghiên cứu này. **100% số liệu dưới đây rút từ TIÊU ĐỀ + ĐOẠN TRÍCH (snippet) do WebSearch trả về**, KHÔNG mở được trang gốc để đối chiếu. Mọi con số phải được nhóm tự mở URL kiểm chứng lại trước khi đưa vào proposal nộp.
2. **Ngân sách WebSearch của phiên đã cạn (200/200 lượt)** sau ~9 truy vấn của nhiệm vụ này. Vì vậy **nhiều mục trong đề bài CHƯA nghiên cứu được** — xem mục [11. Khoảng trống chưa nghiên cứu](#11-khoảng-trống-chưa-nghiên-cứu--việc-cần-làm-tiếp).
3. Ký hiệu dùng trong tài liệu:
   - `[S]` = lấy từ snippet, **chưa mở trang gốc** → cần kiểm chứng.
   - `[S-CŨ]` = snippet, và nguồn có dấu hiệu là bài cũ (trước 2024) → cần kiểm chứng cả số liệu lẫn tính thời sự.
   - Không có ký hiệu = suy luận/diễn giải của người nghiên cứu, **không phải dữ liệu**.

---

## 1. Tóm tắt điều hành (dành cho phần "Vấn đề & Cơ hội" của proposal)

Ba phát hiện mạnh nhất, xếp theo mức độ hữu dụng cho proposal:

| # | Phát hiện | Vì sao quan trọng với proposal |
|---|---|---|
| **1** | **ĐH FPT ĐÃ có quy trình chính thức cho SV mượn laptop của SV khác "để dùng hoặc ĐI THI"**, có hệ thống IT ("ĐK Mượn máy"), chủ máy phải xác nhận, thời gian mượn **tối thiểu 60 phút** `[S]` | Đây là **bằng chứng nội bộ mạnh nhất**: nhà trường công nhận nhu cầu "mượn máy để đi thi" là có thật và đủ phổ biến để phải xây hệ thống quản lý. Nhưng nguồn cung là **peer-to-peer, phụ thuộc lòng tốt bạn bè, không đảm bảo** → chính là KHOẢNG TRỐNG cho dịch vụ cho thuê chuyên nghiệp. |
| **2** | Các ĐH lớn thế giới **đều** vận hành chương trình cho mượn laptop, với **biểu phí phạt trễ và phí thay thế được công bố công khai** (từ 1 USD/giờ đến 5 USD/ngày; thay thế 1.100–2.000 USD/máy) `[S]` | Cho phép proposal **copy quy trình & khung phí đã được kiểm chứng 20+ năm**, thay vì tự nghĩ. Đây là phần "Vận hành" và "Quản trị rủi ro" của proposal. |
| **3** | Thị trường có **kiosk tự động cho mượn laptop** (LaptopsAnytime), giá **~30.000 USD cho 1 kiosk kèm 12 máy** `[S-CŨ]` | Là **mốc so sánh chi phí**: mô hình tự động hoá tốn ~2.500 USD/slot. Quy mô 15–40 máy của nhóm nếu làm thủ công + web đặt lịch sẽ rẻ hơn nhiều lần → luận điểm "vì sao mô hình của chúng tôi khả thi ở VN". |

---

## 2. Chương trình cho mượn laptop tại ĐH nước ngoài — biểu phí cụ thể

### 2.1. Bảng tổng hợp phí phạt trễ & phí thay thế `[S]`

Đây là phần **có giá trị nhất để sao chép vào quy chế thuê máy** của nhóm.

| Trường | Thời hạn mượn | Phí phạt TRỄ | Phí MẤT / thay thế | Mốc coi là "mất máy" | Nguồn |
|---|---|---|---|---|---|
| **Northern Illinois University (NIU)** | (chưa rõ) | **5,00 USD / NGÀY** | **1.100,00 USD** (mất, trộm, hỏng không sửa được) | **Quá hạn 7 ngày** | [library.niu.edu](https://library.niu.edu/university-libraries/about/policies/laptopcirculation.shtml) |
| **University of Kansas (KU)** | 4 giờ (ngắn hạn) | **0,10 USD / PHÚT** (= 6 USD/giờ), trần **30 USD/máy** | (chưa rõ trong snippet) | (chưa rõ) | [services.ku.edu](https://services.ku.edu/TDClient/818/Portal/KB/Article/20717/KU-Libraries-Fines-Fees-Lost-Item-and-Damage-Charges-for-Library-Equipment-and-Accessories-Laptops-H) |
| **University of Connecticut (UConn)** | < 1 ngày (thiết bị công nghệ) | **1,00 USD / GIỜ** | **1.500 USD** (laptop); **30 USD** (dây sạc) | **Quá hạn > 34 ngày** | [library.uconn.edu](https://library.uconn.edu/?p=967) |
| **Sacramento State (CSUS)** | (chưa rõ) | (chưa rõ) | **tối thiểu 2.000 USD** (không trả hoặc hỏng) | (chưa rõ) | [library.csus.edu](https://library.csus.edu/loan-limits-policies-fines) |
| **Stanford — The Hub @ Lathrop** | (chưa rõ) | **5,00 USD / NGÀY**, tính từ đúng ngày đến hạn | (chưa rõ) | **Khoá máy từ xa nếu quá hạn 2 ngày làm việc** | [thehub.stanford.edu](https://thehub.stanford.edu/borrow-equipment/loan-policies) |
| **MIT Libraries** (tài liệu nói chung) | — | **KHÔNG thu phí phạt theo ngày** với tài liệu MIT | **135 USD** phí thay thế khi mất (quá hạn 30+ ngày); có quyền thu cao hơn nếu giá thay thế thực tế cao hơn | Quá hạn 30+ ngày | [libraries.mit.edu/borrow](https://libraries.mit.edu/borrow/) |
| **MIT IS&T** (thiết bị máy tính cho mượn) | — | (chưa rõ) | **Thu toàn bộ giá trị thay thế** thiết bị không trả (tính vào cost object của khoa/phòng) | (chưa rõ) | [ist.mit.edu/loaner-equipment](https://ist.mit.edu/loaner-equipment) |

> **Lưu ý kiểm chứng:** cả 7 dòng trên đều từ snippet. Đặc biệt cần kiểm chứng lại: mốc "34 ngày" của UConn (con số lạ), và việc phí 135 USD của MIT là cho **sách** hay bao gồm **laptop**.

### 2.2. Bài học rút ra cho quy chế thuê máy của nhóm

Từ bảng trên, có **4 nguyên tắc thiết kế** đã được kiểm chứng ở nhiều trường:

1. **Phí trễ tính theo GIỜ với hợp đồng ngắn, theo NGÀY với hợp đồng dài.** KU/UConn cho mượn 4 giờ → phạt theo phút/giờ. NIU/Stanford cho mượn dài → phạt theo ngày. Dịch vụ thuê máy đi thi (ca thi 1–3 giờ) → **phải tính theo giờ**.
2. **Luôn có TRẦN phạt trễ** (KU: trần 30 USD). Tránh phạt vô hạn gây tranh chấp; sau trần thì chuyển sang xử lý "mất máy".
3. **Có mốc chuyển trạng thái rõ ràng từ "trễ" sang "mất"** (NIU: 7 ngày; UConn: 34 ngày; MIT: 30 ngày). → Quy chế của nhóm nên ghi rõ, ví dụ: quá hạn X ngày = coi như mất, thu giá trị thay thế.
4. **Khoá máy từ xa là biện pháp đã được dùng thật** (Stanford: khoá sau 2 ngày làm việc quá hạn). → Rất đáng đưa vào proposal như biện pháp chống mất máy (MDM / Windows Intune / phần mềm quản lý thiết bị).

### 2.3. Mô hình eligibility (điều kiện được mượn) — Stanford `[S]`

Stanford (The Hub @ Lathrop) giới hạn đối tượng rất hẹp, chỉ cho mượn nếu SV thuộc một trong hai nhóm `[S]`:
- **hiện KHÔNG sở hữu laptop và đang trong quá trình mua**, hoặc
- **đang sửa laptop cá nhân**.

Ngoài ra: chỉ SV Stanford **đang đăng ký học** mới được đặt chỗ `[S]`.

> **Ý nghĩa cho proposal:** đây chính xác là **2 phân khúc khách hàng** của dịch vụ cho thuê máy đi thi: (a) chưa/không có máy chạy Windows, (b) máy đang hỏng/đang sửa đúng mùa thi. Stanford — một trường giàu — vẫn phải giải bài toán này, chứng minh nhu cầu không phải đặc thù nghèo.

Nguồn: [thehub.stanford.edu/borrow-equipment/loan-process](https://thehub.stanford.edu/borrow-equipment/loan-process), [thehub.stanford.edu/borrow-equipment/loan-policies](https://thehub.stanford.edu/borrow-equipment/loan-policies)

### 2.4. University of Michigan — mô hình 3 tầng `[S]`

U-M vận hành **3 chương trình song song**, là mô hình phân tầng đáng học:

| Chương trình | Mục đích | Thời hạn | Ghi chú |
|---|---|---|---|
| **Sites @ Home** | Cho mượn DÀI HẠN | **1–2 học kỳ**, gia hạn được **nhiều học kỳ** nếu còn đang học | Mọi SV Ann Arbor đang theo học đều đủ điều kiện; máy cấu hình tốt: **laptop Windows i7** hoặc **MacBook Air M2**; số lượng có hạn `[S]` |
| **Laptop Loaner Program** | Cho mượn khi máy cá nhân **đang sửa** | **Bằng thời gian sửa máy** | Điều kiện: máy đã check-in dịch vụ Tech Repair `[S]` |
| **Michigan Undergraduate Laptop Program (ULP)** | **TẶNG** laptop miễn phí | vĩnh viễn | Cho SV năm nhất đủ điều kiện (hỗ trợ tài chính) `[S]` |

Nguồn: [its.umich.edu — Sites @ Home](https://its.umich.edu/computing/computers-software/sites-at-home) · [its.umich.edu — Laptop Loaner Program](https://its.umich.edu/computing/computers-software/tech-help/laptop-loaner-program) · [finaid.umich.edu — ULP](https://finaid.umich.edu/types-aid/michigan-undergraduate-laptop-program) · [teamdynamix.umich.edu — tổng hợp các chương trình](https://teamdynamix.umich.edu/TDClient/30/Portal/KB/Article/9921/Laptop-Equipment-Loan-Programs-at-U-M)

U-M Flint còn có riêng **"Emergency Laptop Loan Program"** (chương trình cho mượn laptop KHẨN CẤP) — [umflint.edu/ellp](https://www.umflint.edu/ellp/) `[S]`.

> **Ý nghĩa cho proposal:** tên gọi "**Emergency** Laptop Loan" xác nhận rằng **tình huống khẩn cấp về thiết bị** (hỏng máy sát ngày thi/nộp bài) là một hạng mục nhu cầu riêng, được các trường đặt tên và cấp ngân sách riêng. Đây là đúng thị trường ngách của nhóm.

### 2.5. MIT `[S]`

- **MIT IS&T Computing Equipment Loan Program** — [ist.mit.edu/loaner-equipment](https://ist.mit.edu/loaner-equipment); có trang điều khoản riêng cho SV: [ist.mit.edu/loaner-equipment/student-terms](https://ist.mit.edu/loaner-equipment/student-terms) `[S]`.
- Điều khoản đáng chú ý: **thiết bị không trả sẽ bị thu toàn bộ giá trị thay thế** `[S]`.
- MIT Libraries: **không thu phí phạt theo ngày** với tài liệu MIT, thay bằng **phí thay thế 135 USD** khi quá hạn 30+ ngày `[S]`.

> **Ý nghĩa:** MIT chọn mô hình **"không phạt trễ, chỉ phạt mất"** — đơn giản hoá vận hành, giảm xung đột. Đây là một lựa chọn thiết kế thay thế đáng cân nhắc cho nhóm (nhất là với khách hàng SV, việc thu phí phạt nhỏ lẻ rất tốn công và gây mất thiện cảm).

### 2.6. Nghiên cứu vận hành — Code4Lib Journal

**"Best Practices for a University Laptop Lending Program"** (Buzzard & Teetor), Code4Lib Journal — [journal.code4lib.org/articles/5876](https://journal.code4lib.org/articles/5876)

- Mô tả chương trình cho mượn laptop của **University of Arizona Libraries**, vận hành **từ năm 2003** `[S]`.
- Quy mô: **luân chuyển trên 300 thiết bị** `[S]`.
- Nội dung tập trung vào **quy trình làm việc (workflow) và quản lý tồn kho**: lập bảng theo dõi thiết bị, **phân công một "laptop manager" chuyên trách** `[S]`.
- Bản ghi trên Semantic Scholar: [semanticscholar.org](https://www.semanticscholar.org/paper/Best-Practices-for-a-University-Laptop-Lending-Buzzard-Teetor/8b7f1dc9fdbef414e23e22a6683844bb1204a640)

> **Đây là tài liệu học thuật duy nhất tìm được trực tiếp về vận hành chương trình cho mượn laptop.** Rất đáng để nhóm mở đọc full-text (miễn phí, open access) và trích vào phần "Quy trình vận hành" của proposal.
> **KHÔNG tìm thấy trong snippet:** tỉ lệ mất máy / không trả máy. Cần mở bài đọc để lấy.

Tài liệu liên quan khác tìm thấy:
- **"Device Loaner Programs for Universities: Setup, Policies, and ROI"** — [lockncharge.com/blog/device-loaner-program-for-universities](https://lockncharge.com/blog/device-loaner-program-for-universities) — bài của nhà cung cấp (LocknCharge), có thể có số liệu ROI. `[S]` **Chưa đọc được nội dung.**
- **"Laptop Theft in a University Setting can be Avoided with Warnings"** — arXiv preprint, [arxiv.org/pdf/1907.08083](https://arxiv.org/pdf/1907.08083) `[S-CŨ]` (số arXiv 1907 = tháng 7/2019). Liên quan đến rủi ro mất trộm laptop trong môi trường ĐH. **Chưa đọc được nội dung.**

---

## 3. Kiosk tự động cho mượn laptop (laptop vending machine)

### 3.1. LaptopsAnytime

| Hạng mục | Thông tin | Nguồn |
|---|---|---|
| Công ty | LaptopsAnytime, trụ sở **Dallas** (Mỹ), sản xuất máy bán/cho mượn laptop tự động `[S]` | [laptopsanytime.com/product-lines](https://www.laptopsanytime.com/product-lines) |
| **Giá kiosk** | **~30.000 USD cho 1 kiosk ĐÃ BAO GỒM 12 chiếc MacBook 15-inch** (case Drexel University) → **~2.500 USD/slot** `[S-CŨ]` | [insidehighered.com (2013)](https://www.insidehighered.com/news/2013/02/08/libraries-turn-laptop-vending-machines-fulfill-students-late-night-studying-needs) |
| Cách hoạt động | Hoạt động như máy bán hàng tự động: SV thao tác **màn hình cảm ứng**, hệ thống **xác thực danh tính**, rồi **nhả ra một máy đã sạc đầy** `[S]` | như trên |
| Quy mô triển khai | **Khoảng 6 trường ĐH đang dùng**, thêm **~6 trường đang triển khai** `[S-CŨ]` (số liệu tại thời điểm bài 2013 — **chắc chắn đã lạc hậu**) | như trên |
| Chính sách tại Drexel | Máy **phải ở trong thư viện**, **phải trả về đúng khe trong vòng 5 GIỜ** `[S-CŨ]` | như trên |
| Tuỳ chọn thiết bị | Trường được chọn loại thiết bị: Drexel chọn MacBook, trường khác chọn **tablet hoặc PC** `[S]` | như trên |

Nguồn khác về LaptopsAnytime / kiosk:
- Chronicle of Higher Education — [Drexel U. Library Adds Vending Machine to Dispense Laptops](https://www.chronicle.com/blogs/wiredcampus/drexel-u-library-adds-vending-machine-to-dispense-laptops) `[S-CŨ]`
- PUPN Magazine — [Laptop Checkouts: Automated Dispensing Kiosk Systems Transform Higher-ed Computing](https://pupnmag.com/article/laptop-checkouts-automated-dispensing-kiosk-systems-transform-higher-ed-computing/) `[S]`
- Insights Success — [Automated Checkout Kiosks - LaptopsAnytime](https://insightssuccess.com/laptopsanytime-automated-checkout-kiosks/) `[S]`
- Trend Hunter — [Computer Vending Machines: Laptops Anytime](https://www.trendhunter.com/trends/laptops-anytime) `[S-CŨ]`
- University of Washington — hồ sơ đề xuất quỹ công nghệ liên quan kiosk: [techfee.uw.edu/proposal/2021-37](https://techfee.uw.edu/proposal/2021-37/) `[S]` (2021 — có thể chứa **dự toán chi phí chi tiết**, rất đáng mở)

### 3.2. Phân tích chi phí — so sánh với mô hình của nhóm

| Mô hình | Chi phí hạ tầng cho ~12–15 máy | Ghi chú |
|---|---|---|
| **Kiosk tự động (LaptopsAnytime, case Drexel)** | **~30.000 USD** (≈ 780 triệu VND theo tỷ giá tham chiếu ~26.000 VND/USD — **tỷ giá do người nghiên cứu giả định, cần nhóm chốt lại**) — đã gồm 12 MacBook | Tự động 24/7, không cần nhân sự trực; nhưng vốn đầu tư ban đầu rất lớn, và **chi phí kiosk tách riêng khỏi máy chưa xác định được** |
| **Mô hình của nhóm: web đặt lịch + giao/nhận thủ công** | Chi phí = giá 15–40 laptop cũ/refurbished + website + nhân công | **KHÔNG có chi phí kiosk**. Đây là luận điểm cạnh tranh: đạt cùng chức năng "SV có máy khi cần" với vốn thấp hơn nhiều bậc |

> **Cách dùng trong proposal:** đưa con số 30.000 USD/kiosk vào slide để chứng minh (a) **thị trường này tồn tại thật và có người trả tiền rất nhiều cho nó** ở nước ngoài, (b) **mô hình nhẹ vốn của nhóm phù hợp với bối cảnh VN**.
> **CẢNH BÁO:** số 30.000 USD là từ bài năm **2013**, đã 13 năm. Phải ghi rõ năm trong proposal, hoặc liên hệ LaptopsAnytime xin báo giá mới.

### 3.3. D-Tech và CSI — CHƯA NGHIÊN CỨU ĐƯỢC

Đề bài yêu cầu tìm hiểu **D-Tech** và **CSI** (Computer Systems Innovations?) nhưng **ngân sách WebSearch đã cạn trước khi thực hiện**. Xem mục 11.

---

## 4. Việt Nam — trường nào cho mượn laptop/thiết bị?

### 4.1. 🔑 ĐH FPT — ĐÃ CÓ quy trình mượn laptop ĐỂ ĐI THI (phát hiện quan trọng nhất)

**Nguồn:** [it-hcm.fpt.edu.vn — "Hướng dẫn mượn laptop của sinh viên trong trường"](https://it-hcm.fpt.edu.vn/articles.php?news=huong-dan-muon-laptop-cua-sinh-vien-trong-truong&id=56) (Phòng IT, ĐH FPT campus TP.HCM) `[S]`

Nội dung rút từ snippet:

| Yếu tố | Chi tiết `[S]` |
|---|---|
| **Bản chất** | SV mượn laptop **của SINH VIÊN KHÁC** trong trường, **"để dùng hoặc ĐI THI"** — peer-to-peer, KHÔNG phải trường cho mượn máy của trường |
| **Thời gian mượn tối thiểu** | **60 phút** |
| **Hệ thống** | Website IT campus (it-hcm.fpt.edu.vn), đăng nhập bằng **tài khoản nội bộ (tài khoản WiFi)**, chọn **"ĐK Mượn máy"** trên Dashboard |
| **Thao tác đăng ký** | Nhập **MSSV của chủ máy cho mượn** |
| **Xác nhận** | **Chủ máy phải đăng nhập hệ thống để xác nhận** cho mượn; mỗi lần mượn/trả đều phải thao tác trên hệ thống |
| **Trả máy** | Về Dashboard bấm **"Trả máy"** |
| **Lưu ý phòng thi** | Dù mượn máy người khác, SV **phải ngắt kết nối WiFi_Student và WiFi_Exam, rồi đăng nhập lại bằng tài khoản WiFi của CHÍNH MÌNH** |

**Vì sao đây là bằng chứng mạnh nhất trong toàn bộ nghiên cứu:**

1. **Chứng minh nhu cầu là THẬT và đủ lớn để nhà trường phải xây hệ thống.** Không trường nào bỏ công lập module IT, quy trình xác nhận 2 bước, và hướng dẫn riêng cho một nhu cầu hiếm gặp.
2. **Chứng minh nhu cầu gắn ĐÚNG với việc ĐI THI** — đúng thị trường ngách của nhóm. Bài hướng dẫn nêu thẳng cụm "để dùng hoặc đi thi" và có lưu ý riêng về **WiFi_Exam** (mạng phòng thi).
3. **Chỉ ra KHOẢNG TRỐNG mà startup lấp vào:** nguồn cung hiện tại là **bạn bè** — nghĩa là SV phải (a) quen ai đó có máy Windows rảnh, (b) người đó không thi cùng ca, (c) người đó đồng ý đưa máy cá nhân có toàn bộ dữ liệu riêng tư cho người khác mang vào phòng thi. Cả 3 điều kiện đều mong manh. **Dịch vụ cho thuê máy chuyên nghiệp giải quyết cả 3.**
4. **Cho thấy rào cản kỹ thuật cần xử lý:** máy cho thuê phải tương thích quy trình đăng nhập WiFi_Exam bằng tài khoản cá nhân của người thi. Nhóm nên kiểm tra xem quy trình "ĐK Mượn máy" này có áp dụng/bắt buộc với **máy thuê từ bên ngoài trường** hay không — đây là **rủi ro pháp lý/vận hành số 1** của mô hình.

> ⚠️ **BẮT BUỘC KIỂM CHỨNG:** trang này là của **campus TP.HCM**. Nhóm **phải xác minh campus Đà Nẵng (Hoà Hải) có quy trình tương tự không**, và quan trọng hơn: **quy chế thi của ĐH FPT có CHO PHÉP dùng máy thuê từ bên ngoài trong phòng thi không**. Nếu quy chế cấm, toàn bộ mô hình kinh doanh phải điều chỉnh. Nên hỏi trực tiếp Phòng Khảo thí / Phòng IT campus Đà Nẵng.

Các trang FPT liên quan khác tìm thấy:
- [it.fpt.edu.vn — Helpdesk ĐH FPT (hướng dẫn hệ thống FAP)](https://it.fpt.edu.vn/cantho/huong-dan-he-thong-academic-portal-fap/) `[S]`
- [it-hcm.fpt.edu.vn — trang chủ IT ĐH FPT HCM](https://it-hcm.fpt.edu.vn/) `[S]`
- [caodang.fpt.edu.vn — Sổ tay sinh viên FPT Polytechnic](https://caodang.fpt.edu.vn/thong-tin/sinh-vien/so-tay-sinh-vien/so-tay-sinh-vien.html) `[S]` — nên tra mục quy định thiết bị/thi cử

### 4.2. Quỹ Dariu — "Bank of Laptop" (chương trình VN quy mô nhất tìm được)

**Dự án "Quỹ máy tính – Bank of Laptop – cho Sinh viên có hoàn cảnh khó khăn"** `[S]`

| Yếu tố | Chi tiết `[S]` |
|---|---|
| Đơn vị | **Quỹ Dariu** (The Dariu Foundation) |
| Mục tiêu | Hỗ trợ SV khó khăn **mượn laptop** để duy trì học tập, đáp ứng yêu cầu học trực tuyến |
| **Giá trị máy** | Laptop **mới 100%**, giá trị **10.000.000 VND/máy** |
| **Thời hạn mượn** | **Tối đa 24 tháng** |
| Ràng buộc | **Chỉ dùng cho mục đích học tập** |
| Đối tượng | SV **năm 2 trở đi** (CĐ/ĐH); SV **năm nhất** (trung cấp); hoàn cảnh khó khăn **+ thành tích học tập tốt** |

Nguồn: [ctsv.uit.edu.vn — "Chương trình cho sinh viên mượn máy tính miễn phí" (Phòng CTSV, ĐH CNTT – ĐHQG TP.HCM)](https://ctsv.uit.edu.vn/bai-viet/chuong-trinh-cho-sinh-vien-muon-may-tinh-mien-phi) · [sggp.org.vn — "Cho sinh viên mượn laptop miễn phí"](https://www.sggp.org.vn/cho-sinh-vien-muon-laptop-mien-phi-post566364.html)

> **Ý nghĩa cho proposal:**
> - **Mốc giá tham chiếu nội địa: 10 triệu VND/laptop** — rất hữu ích để dự toán vốn đầu tư 15–40 máy của nhóm (15 máy × 10tr = 150 triệu; 40 máy × 10tr = 400 triệu). Lưu ý đây là **máy MỚI**; nếu nhóm mua **máy cũ/refurbished** thì suất đầu tư sẽ thấp hơn.
> - **Chứng minh mô hình "cho mượn laptop" đã tồn tại và vận hành được ở VN** — giảm rủi ro "ý tưởng chưa ai làm vì không khả thi".
> - **Định vị khác biệt:** Dariu = **miễn phí, dài hạn (24 tháng), cho SV nghèo học giỏi, xét duyệt**. Nhóm = **có phí, siêu ngắn hạn (theo ca thi), cho MỌI SV, đặt là có ngay**. Hai mô hình **không cạnh tranh mà bổ sung** → điểm mạnh khi trả lời câu hỏi "đã có chương trình miễn phí rồi sao còn thuê?"

### 4.3. ĐH Văn Hiến

Snippet cho biết SV có hoàn cảnh khó khăn hoặc **thiếu phương tiện học tập (không có smartphone hay laptop)** được nhà trường **hỗ trợ mua TRẢ GÓP hoặc CHO MƯỢN** để học online `[S]`.

Nguồn: [giaoduc247.vn — "Sinh viên Trường ĐH Văn Hiến được trường cho mượn máy tính, smartphone để học Online"](https://giaoduc247.vn/giao-duc-24h/sinh-vien-truong-dh-van-hien-duoc-truong-cho-muon-may-tinh-smartphone-de-hoc-online) `[S-CŨ]` (nội dung nói về học online → nhiều khả năng là bài thời COVID 2021–2022, cần kiểm chứng còn hiệu lực không)

> Đáng chú ý: đây là ví dụ VN về việc trường **kết hợp cả 2 hình thức** — cho mượn **và** hỗ trợ mua trả góp.

### 4.4. ĐH CNTT (UIT) – ĐHQG TP.HCM

Có trang chính thức của Phòng Công tác Sinh viên về **"Chương trình cho sinh viên mượn máy tính miễn phí"** — [ctsv.uit.edu.vn](https://ctsv.uit.edu.vn/bai-viet/chuong-trinh-cho-sinh-vien-muon-may-tinh-mien-phi) `[S]`. Đây là kênh triển khai chương trình Dariu tại UIT (xem 4.2).

### 4.5. RMIT Việt Nam

Kết quả tìm được **KHÔNG xác nhận** RMIT Việt Nam có chương trình cho mượn laptop chuyên biệt. Chỉ tìm thấy `[S]`:

| Nội dung | Thuộc campus | Nguồn |
|---|---|---|
| Thư viện RMIT VN cho mượn tài liệu (cựu SV: **tối đa 25 tài liệu, 1 tháng**) — **là SÁCH, không phải laptop** | **RMIT Việt Nam** | [rmit.edu.vn/libraryvn/borrowing-and-resources](https://www.rmit.edu.vn/libraryvn/borrowing-and-resources) |
| **Student Hardship Assistance Grants** — **"laptop hỏng đột ngột mà cần cho việc học" được liệt kê là tình huống ĐỦ ĐIỀU KIỆN nhận hỗ trợ** | RMIT Australia | [rmit.edu.au — hardship grants](https://www.rmit.edu.au/students/support-services/financial-legal-support/hardship-assistance-grants) |
| **RMIT Equity Notebook Grant** — giúp SV có laptop riêng | RMIT Australia | [rmit.edu.au — Equity Notebook](https://www.rmit.edu.au/students/careers-opportunities/scholarships/coursework/rmit-notebook) |
| Diễn đàn SV hỏi **"Can we borrow Laptop from school?"** | RMIT (myCommunity) | [community.rmit.edu.au](https://community.rmit.edu.au/t5/All-other-technology/Can-we-borrow-Laptop-from-school/td-p/5782) |

> 🔑 **Điểm trích dẫn cực tốt cho proposal:** RMIT chính thức xếp **"laptop hỏng đột ngột"** vào danh mục **khó khăn tài chính khẩn cấp được nhà trường cấp tiền hỗ trợ** `[S]`. Đây là một tổ chức giáo dục lớn **chính thức thừa nhận** rằng hỏng laptop giữa kỳ học là một cú sốc đủ nghiêm trọng để cần can thiệp. Dùng làm luận cứ cho phần "Vấn đề".
> Lưu ý: trang này là **RMIT Australia**, không phải RMIT VN — phải ghi rõ khi trích.

### 4.6. VinUni, ĐH Bách khoa, Fulbright — CHƯA NGHIÊN CỨU ĐƯỢC

Ngân sách WebSearch cạn trước khi tra. Xem mục 11.

---

## 5. FPT — chương trình trả góp / hỗ trợ mua laptop cho SV

**Trạng thái: CHƯA NGHIÊN CỨU ĐẦY ĐỦ.** Chỉ có 2 manh mối từ snippet, **không có số liệu lãi suất, kỳ hạn hay điều kiện**:

| Manh mối | Nguồn | Ghi chú |
|---|---|---|
| Bài đăng: **"Tân sinh viên - Học sinh Bình Dương được ưu đãi khi mua laptop tại FPT Shop"** | [facebook.com/24hbinhduong.vn](https://www.facebook.com/24hbinhduong.vn/posts/t%C3%A2n-sinh-vi%C3%AAn-h%E1%BB%8Dc-sinh-b%C3%ACnh-d%C6%B0%C6%A1ng-%C4%91%C6%B0%E1%BB%A3c-%C6%B0u-%C4%91%C3%A3i-khi-mua-laptop-t%E1%BA%A1i-fpt-shop-th%E1%BB%9Di-%C4%91/901636838663781/) `[S]` | Xác nhận **FPT Shop CÓ chương trình ưu đãi laptop cho tân SV**, nhưng snippet không nêu chi tiết ưu đãi |
| Bài của **ĐH FPT Cần Thơ: "Kinh nghiệm chọn laptop cho sinh viên"** | [facebook.com/daihocfptcantho](https://www.facebook.com/daihocfptcantho/posts/-kinh-nghi%E1%BB%87m-ch%E1%BB%8Dn-laptop-cho-sinh-vi%C3%AAn-l%C3%AAn-%C4%91%E1%BA%A1i-h%E1%BB%8Dc-b%C3%AAn-c%E1%BA%A1nh-deadline-th%C3%AC-laptop-/902098058625391/) `[S]` | Xác nhận **chính ĐH FPT phải chủ động tư vấn SV chọn laptop** → gián tiếp cho thấy laptop là điều kiện bắt buộc và là gánh nặng đầu vào |
| ĐH Văn Hiến hỗ trợ SV **mua trả góp** laptop/smartphone | (xem 4.3) `[S-CŨ]` | Tiền lệ VN về mô hình trả góp qua trường |

> **KHÔNG tìm được:** chương trình trả góp chính thức của ĐH FPT, hợp tác FE Credit, lãi suất 0%, kỳ hạn. **Tuyệt đối không được bịa các con số này.** Xem mục 11.

---

## 6. Nghiên cứu học thuật — digital divide / device access gap

**Trạng thái: CHƯA NGHIÊN CỨU ĐƯỢC.** Ngân sách WebSearch cạn trước khi thực hiện nhóm truy vấn này.

Chỉ có 1 tài liệu học thuật liên quan gián tiếp tìm thấy được:
- **"Laptop Theft in a University Setting can be Avoided with Warnings"** — [arxiv.org/pdf/1907.08083](https://arxiv.org/pdf/1907.08083) `[S-CŨ]` (2019) — về **mất trộm laptop** trong môi trường ĐH, phục vụ phần quản trị rủi ro chứ không phải phần nhu cầu.

**KHÔNG có số liệu nào về:** % SV thiếu thiết bị học tập, tác động đến kết quả học, khảo sát VN/Đông Nam Á. **Tuyệt đối không bịa.** Xem mục 11 để biết truy vấn cần chạy.

---

## 7. Trường hợp SV lỡ thi vì hỏng máy

**Trạng thái: CHƯA NGHIÊN CỨU ĐƯỢC.** Ngân sách WebSearch cạn.

Bằng chứng **gián tiếp** duy nhất thu được (nhưng khá mạnh) — cả 3 đều từ snippet:

| Bằng chứng gián tiếp | Ý nghĩa |
|---|---|
| **ĐH FPT xây hệ thống IT riêng cho việc "mượn laptop để đi thi"** (mục 4.1) | Nếu không ai từng thiếu máy lúc thi, hệ thống này không tồn tại |
| **RMIT xếp "laptop hỏng đột ngột" vào diện được cấp hỗ trợ khó khăn** (mục 4.5) | Một trường ĐH lớn chính thức coi đây là sự cố nghiêm trọng cần can thiệp tài chính |
| **U-M Flint đặt tên chương trình là "EMERGENCY Laptop Loan Program"** (mục 2.4) | Từ "khẩn cấp" trong tên chương trình = sự cố thiết bị đột xuất là hạng mục nhu cầu có thật, định kỳ |
| **Stanford giới hạn cho mượn đúng 2 nhóm: chưa có máy & đang sửa máy** (mục 2.3) | Xác nhận "máy đang sửa" là một trong hai nguyên nhân chính khiến SV thiếu thiết bị |

> **Khuyến nghị mạnh:** vì không tra được báo chí/forum, nhóm nên **tự thu thập bằng chứng sơ cấp** — đây thực ra là bằng chứng **thuyết phục hơn** cho một proposal khởi nghiệp sinh viên: khảo sát Google Form trong các group Facebook SV ĐH FPT Đà Nẵng với câu hỏi trực tiếp ("Bạn đã từng phải mượn máy người khác để đi thi chưa?", "Máy bạn từng hỏng/hết pin/lỗi SEB sát ngày thi chưa?"). Xem gợi ý ở mục 10.

---

## 8. Bảng tổng hợp mọi con số thu được (để tra nhanh)

| Con số | Đơn vị | Ngữ cảnh | Mốc thời gian | Độ tin cậy |
|---|---|---|---|---|
| 5,00 | USD/ngày | Phí trễ laptop, NIU | (không rõ năm) | `[S]` |
| 1.100,00 | USD | Phí thay thế laptop mất/hỏng, NIU | (không rõ năm) | `[S]` |
| 7 | ngày | NIU: quá hạn bao lâu thì coi là mất | (không rõ năm) | `[S]` |
| 0,10 | USD/phút | Phí trễ laptop mượn 4 giờ, KU | (không rõ năm) | `[S]` |
| 30 | USD | Trần phí trễ/máy, KU | (không rõ năm) | `[S]` |
| 4 | giờ | Thời hạn mượn ngắn hạn, KU | (không rõ năm) | `[S]` |
| 1,00 | USD/giờ | Phí trễ thiết bị mượn <1 ngày, UConn | (không rõ năm) | `[S]` |
| 1.500 | USD | Phí thay thế laptop, UConn | (không rõ năm) | `[S]` |
| 30 | USD | Phí thay thế dây sạc, UConn | (không rõ năm) | `[S]` |
| 34 | ngày | UConn: quá hạn bao lâu thì coi là mất | (không rõ năm) | `[S]` ⚠️ con số lạ, cần kiểm chứng |
| 2.000 | USD (tối thiểu) | Phí thay thế laptop, Sac State | (không rõ năm) | `[S]` |
| 5,00 | USD/ngày | Phí trễ, Stanford The Hub | (không rõ năm) | `[S]` |
| 2 | ngày làm việc | Stanford: quá hạn bao lâu thì KHOÁ MÁY TỪ XA | (không rõ năm) | `[S]` |
| 135 | USD | Phí thay thế tài liệu mất, MIT Libraries | (không rõ năm) | `[S]` |
| 30+ | ngày | MIT: quá hạn bao lâu thì tính phí thay thế | (không rõ năm) | `[S]` |
| 0 | USD/ngày | MIT Libraries KHÔNG thu phí trễ theo ngày | (không rõ năm) | `[S]` |
| 1–2 | học kỳ | Thời hạn mượn Sites @ Home, U-M | (không rõ năm) | `[S]` |
| 300+ | thiết bị | Quy mô luân chuyển, U. of Arizona Libraries | từ 2003 | `[S]` |
| ~30.000 | USD | Giá 1 kiosk LaptopsAnytime **kèm 12 MacBook**, Drexel | **2013** | `[S-CŨ]` |
| ~2.500 | USD/slot | Suy ra từ 30.000/12 | 2013 | tính toán |
| 12 | máy/kiosk | Sức chứa kiosk Drexel | 2013 | `[S-CŨ]` |
| 5 | giờ | Thời hạn giữ máy từ kiosk, Drexel | 2013 | `[S-CŨ]` |
| ~6 (+~6) | trường ĐH | Số trường dùng (và đang triển khai) kiosk LaptopsAnytime | **2013** | `[S-CŨ]` ⚠️ chắc chắn lạc hậu |
| **10.000.000** | **VND/máy** | **Giá trị laptop mới Quỹ Dariu cho mượn, VN** | (không rõ năm) | `[S]` |
| **24** | **tháng** | **Thời hạn mượn tối đa, Quỹ Dariu, VN** | (không rõ năm) | `[S]` |
| **60** | **phút** | **Thời gian mượn laptop TỐI THIỂU, hệ thống ĐH FPT** | (không rõ năm) | `[S]` |
| 25 | tài liệu / 1 tháng | Hạn mức mượn của cựu SV, Thư viện RMIT VN (**sách, không phải laptop**) | (không rõ năm) | `[S]` |

---

## 9. Khuyến nghị áp dụng trực tiếp vào proposal

### 9.1. Khung quy chế thuê máy đề xuất (tổng hợp best practice từ mục 2)

| Hạng mục | Đề xuất | Căn cứ |
|---|---|---|
| Đơn vị tính | **Theo CA THI / theo GIỜ** (không theo ngày) | KU & UConn dùng đơn vị giờ/phút cho hợp đồng ngắn `[S]` |
| Phí trả trễ | Tính **theo giờ**, có **TRẦN** rõ ràng | KU đặt trần 30 USD `[S]` |
| Mốc "mất máy" | Quá hạn **X ngày** → thu giá trị thay thế (đề xuất X = 3–7 ngày, ngắn vì vòng quay ngắn) | NIU: 7 ngày `[S]`; MIT: 30 ngày `[S]` |
| Phí thay thế | **Ghi rõ SỐ TIỀN CỤ THỂ cho từng model** trong hợp đồng, kèm phí phụ kiện (sạc) riêng | UConn tách riêng: laptop 1.500 USD, sạc 30 USD `[S]` |
| Chống mất máy | **Khoá máy từ xa / MDM** khi quá hạn | Stanford khoá sau 2 ngày làm việc `[S]` |
| Nhân sự | Có **1 người chuyên trách quản lý máy** + bảng theo dõi tồn kho từng máy | Code4Lib / U. of Arizona `[S]` |
| Đặt chỗ trước | Bắt buộc **đặt trước** theo lịch thi | Stanford dùng hệ thống reservation `[S]` |
| Sàng lọc | Ràng buộc **chỉ SV đang theo học**, xác thực bằng thẻ SV/email trường | Stanford yêu cầu SV đang đăng ký học `[S]` |

### 9.2. Định vị so với các chương trình hiện có ở VN

| | Quỹ Dariu / trường cho mượn | **Dịch vụ của nhóm** |
|---|---|---|
| Chi phí | Miễn phí | Có phí |
| Thời hạn | Dài (24 tháng) | Siêu ngắn (theo ca thi) |
| Đối tượng | SV nghèo + học giỏi, phải xét duyệt | Mọi SV, không xét duyệt |
| Tốc độ | Chậm (đợt xét, hồ sơ) | **Tức thời / trong ngày** |
| Tình huống phục vụ | Thiếu máy kinh niên | **Sự cố đột xuất mùa thi** |
| Cấu hình | Máy phổ thông | **Windows đã cài/kiểm thử sẵn cho EOS + Safe Exam Browser** ← khác biệt lõi |

> **Khác biệt lõi nên nhấn mạnh trong proposal:** không ai trong các chương trình trên **đảm bảo máy chạy được EOS + Safe Exam Browser**. Đó mới là giá trị nhóm bán — không phải "một cái laptop", mà là "**một cái máy CHẮC CHẮN VÀO THI ĐƯỢC**".

---

## 10. Gợi ý khảo sát sơ cấp (bù cho phần chưa tra được)

Vì mục 6 và 7 chưa có dữ liệu thứ cấp, đề xuất nhóm chạy khảo sát nhanh (Google Form, mục tiêu 100–200 phản hồi trong group Facebook SV ĐH FPT Đà Nẵng). Các câu hỏi nên có, để tạo ra **chính số liệu mà proposal đang thiếu**:

1. Máy tính bạn dùng để thi là: Windows / MacBook Intel / **MacBook M1-M2-M3** / không có máy riêng
2. Bạn đã từng **mượn máy người khác để đi thi** chưa? (Chưa / 1 lần / 2–3 lần / trên 3 lần) — *đối chiếu trực tiếp với hệ thống "ĐK Mượn máy" ở mục 4.1*
3. Bạn đã từng gặp sự cố máy (hỏng, hết pin, lỗi SEB, máy quá yếu) **trong vòng 48 giờ trước giờ thi** chưa?
4. Nếu có sự cố, bạn đã xử lý bằng cách nào? (mượn bạn / mượn phòng IT / hoãn thi / vẫn thi với máy lỗi / **không thi được**)
5. Bạn **đã từng lỡ/hoãn một ca thi** vì lý do thiết bị chưa? ← *câu chốt, tạo ra con số "% SV từng lỡ thi vì máy"*
6. Bạn sẵn sàng trả bao nhiêu để thuê một máy **đảm bảo thi được** trong 1 ca thi? (mức giá: <50k / 50–100k / 100–150k / 150–200k / >200k VND)
7. Bạn cần máy trước ca thi bao lâu để yên tâm? (1 giờ / nửa ngày / 1 ngày / vài ngày)

---

## 11. Khoảng trống chưa nghiên cứu — việc cần làm tiếp

**Nguyên nhân:** ngân sách WebSearch của phiên cạn (200/200) sau ~9 truy vấn. Các mục sau trong đề bài **hoàn toàn chưa có dữ liệu**:

| # | Nội dung đề bài | Trạng thái | Truy vấn gợi ý cho phiên sau |
|---|---|---|---|
| 1 | **UBC, NUS, University of Melbourne, các trường Hàn Quốc** — chương trình laptop loan | ❌ Chưa tra | `NUS library laptop loan overdue fine replacement`; `UBC laptop loan program library fine`; `University of Melbourne laptop loan students`; `Korean university laptop rental students` |
| 2 | **Tỉ lệ KHÔNG TRẢ MÁY / thất thoát** nếu trường nào công bố | ❌ Chưa có số nào | Mở full-text [journal.code4lib.org/articles/5876](https://journal.code4lib.org/articles/5876); `university laptop lending program loss rate percentage not returned` |
| 3 | **Kiosk D-Tech** | ❌ Chưa tra | `D-Tech laptop locker kiosk library university`; `D-Tech International laptop dispenser` |
| 4 | **Kiosk CSI** | ❌ Chưa tra | `CSI laptop kiosk university library vending` |
| 5 | **Giá kiosk cập nhật 2024–2026** | ❌ Chỉ có số 2013 | `laptop kiosk cost 2025 university library`; mở [techfee.uw.edu/proposal/2021-37](https://techfee.uw.edu/proposal/2021-37/) (có thể có dự toán) |
| 6 | **VinUni** cho mượn laptop/thiết bị | ❌ Chưa tra | `VinUni laptop loan student device borrow`; `VinUni cho sinh viên mượn laptop` |
| 7 | **ĐH Bách khoa (HN/HCM/ĐN)** | ❌ Chưa tra | `Đại học Bách khoa cho sinh viên mượn laptop thư viện` |
| 8 | **Fulbright University Vietnam** | ❌ Chưa tra | `Fulbright University Vietnam laptop loan student` |
| 9 | **FPT trả góp laptop: FPT Shop / FE Credit / chương trình của trường** | ❌ Chỉ có 1 manh mối FB, không có số | `FPT Shop trả góp laptop sinh viên lãi suất 0%`; `Đại học FPT hỗ trợ sinh viên mua laptop trả góp`; `FE Credit trả góp laptop sinh viên` |
| 10 | **Digital divide / device access gap — số liệu học thuật** | ❌ Chưa tra | `digital divide university students device access survey Vietnam`; `percentage students lack laptop for online learning Southeast Asia study`; `device access gap academic performance students research 2024` |
| 11 | **Ca SV lỡ thi vì hỏng máy (báo/forum/reddit/FB)** | ❌ Chưa tra | `sinh viên hỏng laptop không thi được`; `reddit student laptop broke during exam missed`; `Safe Exam Browser laptop failed exam student`; `EOS Safe Exam Browser lỗi không thi được FPT` |
| 12 | **Quy chế thi ĐH FPT có cho dùng máy thuê ngoài không** | ❌ CHƯA XÁC MINH — **RỦI RO LỚN NHẤT** | Hỏi trực tiếp Phòng Khảo thí/IT campus Đà Nẵng; tra `quy chế thi Đại học FPT máy tính cá nhân Safe Exam Browser` |
| 13 | **Giá thuê laptop thị trường Đà Nẵng** (để định giá) | ❌ Ngoài phạm vi nhiệm vụ này | `cho thuê laptop Đà Nẵng giá theo ngày`; `dịch vụ cho thuê laptop sinh viên giá` |

---

## 12. Danh sách nguồn đầy đủ

### Chương trình cho mượn — ĐH nước ngoài
1. [NIU — Laptop Circulation Policy](https://library.niu.edu/university-libraries/about/policies/laptopcirculation.shtml)
2. [KU Libraries — Fines, Fees, Lost Item, and Damage Charges for Library Equipment](https://services.ku.edu/TDClient/818/Portal/KB/Article/20717/KU-Libraries-Fines-Fees-Lost-Item-and-Damage-Charges-for-Library-Equipment-and-Accessories-Laptops-H)
3. [UConn Library — fines/fees](https://library.uconn.edu/?p=967)
4. [Sac State Library — Loan Limits, Policies & Fines](https://library.csus.edu/loan-limits-policies-fines)
5. [Stanford The Hub — Loan Policies](https://thehub.stanford.edu/borrow-equipment/loan-policies)
6. [Stanford The Hub — Loan Process](https://thehub.stanford.edu/borrow-equipment/loan-process)
7. [Stanford Libraries — Borrow](https://library.stanford.edu/using/borrow-renew-return/borrow)
8. [Stanford UIT — Travel Loaner Program](https://uit.stanford.edu/service/travelloaner)
9. [Stanford SoE IT — Loaner Equipment](https://soeithelp.stanford.edu/services/loaner-equipment)
10. [MIT Libraries — Borrow & request](https://libraries.mit.edu/borrow/)
11. [MIT IS&T — Computing Equipment Loan Program](https://ist.mit.edu/loaner-equipment)
12. [MIT IS&T — Student Laptop Loan Terms](https://ist.mit.edu/loaner-equipment/student-terms)
13. [U-M ITS — Sites @ Home (Loaner Laptop Program)](https://its.umich.edu/computing/computers-software/sites-at-home)
14. [U-M ITS — Sites @ Home FAQ](https://its.umich.edu/computing/computers-software/sites-at-home/faq)
15. [U-M ITS — Laptop Loaner Program](https://its.umich.edu/computing/computers-software/tech-help/laptop-loaner-program)
16. [U-M — Michigan Undergraduate Laptop Program](https://finaid.umich.edu/types-aid/michigan-undergraduate-laptop-program)
17. [U-M TeamDynamix — Laptop & Equipment Loan Programs at U-M](https://teamdynamix.umich.edu/TDClient/30/Portal/KB/Article/9921/Laptop-Equipment-Loan-Programs-at-U-M)
18. [U-M Flint — Emergency Laptop Loan Program](https://www.umflint.edu/ellp/)
19. [CUNY City Tech — Laptop Loan Policy](https://library.citytech.cuny.edu/about/policies/laptop.html)
20. [UCLA Library — Fines and Fees for Borrowed Materials](https://www.library.ucla.edu/about/policies/fines-and-fees-for-borrowed-materials/)
21. [UGA Libraries — Technology Lending](https://libraries.uga.edu/user-services/tech-loans)
22. [KU — Student Laptop Loan Program](https://arcd.ku.edu/student-laptop-loan-program)
23. [Boston University Medical Campus — Laptop & Equipment Loaning](https://www.bumc.bu.edu/medlib/computing/loaning/)
24. [UW–Madison — Student Loaner Laptop](https://kb.wisc.edu/cdisit/155863)
25. [LMU Library — Replacement and Fees Policy 2024 (PDF)](https://library.lmu.edu/media/lmulibrary/forms-documents/107-Replacement%20and%20Fees%20Policy%202024.pdf)

### Nghiên cứu / tài liệu vận hành
26. [Code4Lib Journal — Best Practices for a University Laptop Lending Program](https://journal.code4lib.org/articles/5876)
27. [Semantic Scholar — bản ghi bài trên](https://www.semanticscholar.org/paper/Best-Practices-for-a-University-Laptop-Lending-Buzzard-Teetor/8b7f1dc9fdbef414e23e22a6683844bb1204a640)
28. [LocknCharge — Device Loaner Programs for Universities: Setup, Policies, and ROI](https://lockncharge.com/blog/device-loaner-program-for-universities)
29. [arXiv — Laptop Theft in a University Setting can be Avoided with Warnings (2019)](https://arxiv.org/pdf/1907.08083)

### Kiosk tự động
30. [Inside Higher Ed — Libraries turn to laptop vending machines (2013)](https://www.insidehighered.com/news/2013/02/08/libraries-turn-laptop-vending-machines-fulfill-students-late-night-studying-needs)
31. [Chronicle — Drexel U. Library Adds Vending Machine to Dispense Laptops](https://www.chronicle.com/blogs/wiredcampus/drexel-u-library-adds-vending-machine-to-dispense-laptops)
32. [LaptopsAnytime — Product Lines](https://www.laptopsanytime.com/product-lines)
33. [PUPN Magazine — Automated Dispensing Kiosk Systems Transform Higher-ed Computing](https://pupnmag.com/article/laptop-checkouts-automated-dispensing-kiosk-systems-transform-higher-ed-computing/)
34. [Insights Success — Automated Checkout Kiosks: LaptopsAnytime](https://insightssuccess.com/laptopsanytime-automated-checkout-kiosks/)
35. [Trend Hunter — Laptops Anytime](https://www.trendhunter.com/trends/laptops-anytime)
36. [UW Tech Fee — proposal 2021-37](https://techfee.uw.edu/proposal/2021-37/)

### Việt Nam
37. 🔑 [IT ĐH FPT HCM — Hướng dẫn mượn laptop của sinh viên trong trường](https://it-hcm.fpt.edu.vn/articles.php?news=huong-dan-muon-laptop-cua-sinh-vien-trong-truong&id=56)
38. [IT ĐH FPT HCM — trang chủ](https://it-hcm.fpt.edu.vn/)
39. [Helpdesk ĐH FPT — hướng dẫn FAP](https://it.fpt.edu.vn/cantho/huong-dan-he-thong-academic-portal-fap/)
40. [FPT Polytechnic — Sổ tay sinh viên](https://caodang.fpt.edu.vn/thong-tin/sinh-vien/so-tay-sinh-vien/so-tay-sinh-vien.html)
41. [UIT CTSV — Chương trình cho sinh viên mượn máy tính miễn phí (Quỹ Dariu)](https://ctsv.uit.edu.vn/bai-viet/chuong-trinh-cho-sinh-vien-muon-may-tinh-mien-phi)
42. [SGGP — Cho sinh viên mượn laptop miễn phí](https://www.sggp.org.vn/cho-sinh-vien-muon-laptop-mien-phi-post566364.html)
43. [Giaoduc247 — SV ĐH Văn Hiến được mượn máy tính, smartphone học Online](https://giaoduc247.vn/giao-duc-24h/sinh-vien-truong-dh-van-hien-duoc-truong-cho-muon-may-tinh-smartphone-de-hoc-online)
44. [RMIT Vietnam Library — Borrowing and resources](https://www.rmit.edu.vn/libraryvn/borrowing-and-resources)
45. [RMIT — Student Hardship Assistance Grants (laptop hỏng = tình huống đủ điều kiện)](https://www.rmit.edu.au/students/support-services/financial-legal-support/hardship-assistance-grants)
46. [RMIT — Equity Notebook Grant](https://www.rmit.edu.au/students/careers-opportunities/scholarships/coursework/rmit-notebook)
47. [RMIT myCommunity — "Can we borrow Laptop from school?"](https://community.rmit.edu.au/t5/All-other-technology/Can-we-borrow-Laptop-from-school/td-p/5782)
48. [Facebook — Tân sinh viên được ưu đãi khi mua laptop tại FPT Shop](https://www.facebook.com/24hbinhduong.vn/posts/t%C3%A2n-sinh-vi%C3%AAn-h%E1%BB%8Dc-sinh-b%C3%ACnh-d%C6%B0%C6%A1ng-%C4%91%C6%B0%E1%BB%A3c-%C6%B0u-%C4%91%C3%A3i-khi-mua-laptop-t%E1%BA%A1i-fpt-shop-th%E1%BB%9Di-%C4%91/901636838663781/)
49. [Facebook ĐH FPT Cần Thơ — Kinh nghiệm chọn laptop cho sinh viên](https://www.facebook.com/daihocfptcantho/posts/-kinh-nghi%E1%BB%87m-ch%E1%BB%8Dn-laptop-cho-sinh-vi%C3%AAn-l%C3%AAn-%C4%91%E1%BA%A1i-h%E1%BB%8Dc-b%C3%AAn-c%E1%BA%A1nh-deadline-th%C3%AC-laptop-/902098058625391/)

---

*Tài liệu lập bằng WebSearch (chỉ snippet, WebFetch bị chặn). Mọi số liệu cần nhóm mở URL kiểm chứng trước khi đưa vào bản nộp.*
