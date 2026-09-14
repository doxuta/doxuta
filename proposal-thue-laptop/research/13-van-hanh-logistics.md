# 13 — QUY TRÌNH VẬN HÀNH (SOP) CHUẨN NGÀNH CHO THUÊ THIẾT BỊ
### Nguyên liệu thô cho Proposal Khởi nghiệp — Website cho thuê laptop đi thi, ĐH FPT Đà Nẵng (P. Hoà Hải)
**Ngày lập:** 14/09/2026 · **Phạm vi đội máy giả định:** 15–40 laptop · **Bối cảnh:** thi EOS Client + Safe Exam Browser, **bắt buộc Windows**

---

# ⚠️ CẢNH BÁO PHƯƠNG PHÁP — BẮT BUỘC ĐỌC TRƯỚC KHI DÙNG BẤT KỲ SỐ NÀO

> **Phiên nghiên cứu này KHÔNG thực hiện được một lần tìm kiếm web nào.**
> Ngân sách WebSearch của phiên (**200/200 lượt**) đã bị các nhiệm vụ nghiên cứu trước đó dùng hết trước khi nhiệm vụ số 13 bắt đầu. `WebFetch` và `curl` bị chặn hoàn toàn (mọi domain trả `EGRESS_BLOCKED`).
>
> **Hệ quả bắt buộc phải hiểu:**
> 1. **KHÔNG có một URL mới nào trong tài liệu này.** Mọi URL xuất hiện đều được **trích lại từ các file nghiên cứu anh em trong cùng thư mục** (`01`, `02`, `08`, `09`, `10`, `11`) — nơi chúng đã được WebSearch trả về thật ở phiên khác.
> 2. **Không bịa URL.** Với những tài liệu/tiêu chuẩn mà tài liệu này nhắc tới nhưng không có URL đã xác minh, tôi ghi **tên chính xác của tài liệu + câu lệnh tìm kiếm cụ thể** để nhóm tự tra, thay vì gán một đường link có thể sai.
> 3. Toàn bộ phần kiến thức chuyên môn (NIST SP 800-88, Clonezilla, `powercfg`, thang Grade A/B/C, chỉ số utilization, điều luật Việt Nam…) đến từ **kiến thức nội tại của mô hình, dữ liệu huấn luyện đến 05/2026**, **KHÔNG được xác minh trong phiên**. Nhóm **BẮT BUỘC** tra lại trước khi đưa vào bài nộp.

## Hệ thống nhãn dùng xuyên suốt tài liệu

| Nhãn | Ý nghĩa | Mức tin cậy | Nhóm phải làm gì |
|---|---|---|---|
| 🟢 **[XM]** | **Đã xác minh** — có URL thật do WebSearch trả về ở phiên nghiên cứu khác của chính dự án này; ghi rõ file nguồn | Cao (nhưng vẫn là snippet, chưa mở trang) | Mở URL xác nhận lại 1 lần |
| 🟡 **[KT-MH]** | **Kiến thức mô hình** — đúng theo hiểu biết chuyên ngành của mô hình (cutoff 05/2026), **không xác minh được trong phiên** | Trung bình — thường đúng về bản chất, **có thể sai về con số/số điều/phiên bản** | 🔴 **BẮT BUỘC tra lại**, có sẵn từ khoá tra ở cột bên |
| 🔵 **[TT]** | **Tính toán / thiết kế của người nghiên cứu** — không phải dữ liệu bên ngoài, là mô hình toán hoặc đề xuất quy trình | Là suy luận, minh bạch giả định | Kiểm tra lại giả định đầu vào |
| 🔴 **[KTĐ]** | **Không tra được** — phải khảo sát sơ cấp / hỏi trực tiếp | — | Đưa vào kế hoạch khảo sát |

---

# 1. TÓM TẮT ĐIỀU HÀNH — 12 QUYẾT ĐỊNH VẬN HÀNH CỐT LÕI

Nếu chỉ đọc một trang, đọc trang này.

| # | Quyết định | Con số / quy tắc đề xuất | Nhãn | Mục |
|---|---|---|---|---|
| 1 | **Biên bản bàn giao 2 chiều là biện pháp rẻ nhất, mạnh nhất** | 0 đồng chi phí; 8 ảnh + 1 video 30 giây mỗi chiều; không có nó thì **thua mọi tranh chấp** | 🟢 [XM] file 08 | §2 |
| 2 | **Thang tình trạng ngoại hình 4 cấp có định lượng** (A / B / C / D) | Định nghĩa bằng **số vết + kích thước mm**, không dùng từ mô tả cảm tính | 🔵 [TT] + 🟡 [KT-MH] | §3 |
| 3 | **Kiến trúc chuẩn bị máy: Golden Image + Deep Freeze** | Deep Freeze biến turnaround từ **~40 phút xuống ~3 phút** (chỉ cần reboot) | 🟡 [KT-MH] | §4 |
| 4 | **Thời gian tái chuẩn bị mỗi máy** | Mức 1 (Quick Turn) **~20 phút nhân công**; Mức 2 (Reimage) **~40 phút**; Mức 3 (Rebuild) **4–8 giờ** | 🔵 [TT] ước lượng kỹ thuật | §4.5 |
| 5 | **Chuẩn xoá dữ liệu: NIST SP 800-88 Rev.1 mức "Clear"** cho máy quay vòng nội bộ; mức **"Purge"** khi thanh lý máy ra khỏi đội | Rev.1 (12/2014) khẳng định **1 lượt ghi đè là đủ** với ổ hiện đại — không cần 7 hay 35 lượt | 🟡 [KT-MH] | §4.7 |
| 6 | **Ngưỡng pin nhận vào đội** | **SoH ≥ 80%** để nhận máy mới vào đội; **≥ 70%** để tiếp tục cho thuê ca thi; **< 70% → chỉ cho thuê tháng có ổ cắm hoặc thay pin** | 🔵 [TT] dựa trên 🟡 [KT-MH] | §5 |
| 7 | **Kiểm chứng pin bằng thời lượng thực đo, không chỉ bằng %** | Bắt buộc **≥ 3,5 giờ** chạy thực với SEB + màn hình 50% + Wi-Fi bật (dài hơn ca thi dài nhất) | 🔵 [TT] | §5.4 |
| 8 | **Hai loại utilization phải tách bạch** | **Time utilization** = ngày-máy cho thuê / ngày-máy khả dụng. **Dollar utilization** = doanh thu thuê 12 tháng / nguyên giá đội máy (OEC) | 🟡 [KT-MH] | §6 |
| 9 | **Mốc thực tế năm 1 của ngành cho thuê thiết bị: 35–45%**, KHÔNG phải 80% như nhà cung cấp quảng cáo | Đây là con số **duy nhất có nguồn** trong toàn bộ dự án về utilization | 🟢 [XM] file 02 | §6.2 |
| 10 | **Máy dự phòng nóng (hot spare)** | Fleet 20 máy → **2 máy**; 30 máy → **2–4 máy**; 40 máy → **3–5 máy**, tuỳ tỉ lệ hỏng ngày thi 2% hay 5%. Tính bằng phân phối nhị thức, không đoán | 🔵 [TT] | §7 |
| 11 | **Thang leo thang thu hồi 7 bước theo mốc T+0 → T+30**, chuyển trạng thái "trễ" → "mất" ở **T+7 ngày** | Chuẩn ngành thư viện ĐH: NIU 7 ngày, MIT 30 ngày, UConn 34 ngày | 🟢 [XM] file 10 | §8 |
| 12 | **SLA đổi máy trong ngày thi ≤ 15 phút trong khuôn viên** | Chuẩn tốt nhất Đà Nẵng hiện tại chỉ là **"trong ngày"**; nhanh nhất VN là **2 giờ** (Laptop SGN, TP.HCM) → khoảng trống cạnh tranh rõ ràng | 🟢 [XM] file 01 | §9 |

### Ba câu để đưa thẳng vào slide proposal

1. *"Chúng tôi không bán laptop theo giờ. Chúng tôi bán **một quy trình 20 bước đảm bảo máy vào được phòng thi** — và nếu nó sai, chúng tôi thay máy trong 15 phút."*
2. *"Đối thủ nhanh nhất Đà Nẵng cam kết 'giao trong ngày'. Với ca thi 7h30 sáng, 'trong ngày' là vô nghĩa."* 🟢 [XM] file 01
3. *"Mỗi máy có một hồ sơ đời máy: ảnh 8 góc mỗi lượt giao–nhận, nhật ký pin, số hiệu bản image, và chứng nhận xoá dữ liệu. Đó là thứ 'mượn máy của bạn' không bao giờ có."*

---

# 2. BIÊN BẢN BÀN GIAO THIẾT BỊ (HANDOVER / CHECK-OUT FORM)

## 2.1. Vì sao đây là tài liệu quan trọng nhất trong toàn bộ vận hành

Ba lý do, theo thứ tự quan trọng:

**(a) Pháp lý.** Không có văn bản ghi nhận **tình trạng tài sản tại thời điểm giao**, thì khi tranh chấp, bên cho thuê gần như **không có cơ sở chứng minh** hư hỏng phát sinh trong thời gian thuê.
> 🟢 [XM] — file `01-thi-truong-cho-thue-laptop-vn.md`: *"Startup bắt buộc phải có mẫu hợp đồng/phiếu thuê bằng văn bản (dù là e-contract ký trên web), ghi rõ: (a) tình trạng máy khi giao, (b) mức bồi thường cho từng loại hư hỏng, (c) giá trị đền bù khi mất máy. Không có văn bản → khi tranh chấp gần như không có cơ sở đòi bồi thường."* Căn cứ pháp lý được nêu: **Bộ luật Dân sự 2015** — nguồn [congchung247.com.vn – Thuê thiết bị làm hỏng: Bên thuê có phải bồi thường?](https://congchung247.com.vn/thue-thiet-bi-lam-hong-ben-thue-co-phai-boi-thuong/)
>
> 🔴 **MÂU THUẪN NGUỒN CẦN NHÓM GIẢI QUYẾT:** file `01` (theo snippet của trang trên) ghi điều luật là **Điều 554 và 557 BLDS 2015**. Theo 🟡 [KT-MH], **hợp đồng thuê tài sản** trong BLDS 2015 nằm ở khoảng **Điều 472–493**, trong đó điều trực tiếp liên quan là **Điều 479 (nghĩa vụ bảo quản tài sản thuê)** và **Điều 482 (trả lại tài sản thuê)**; Điều 554/557 thuộc chương khác. **Hai nguồn không khớp → nhóm BẮT BUỘC tra `thuvienphapluat.vn` và ghi đúng số điều trong hợp đồng mẫu.** Ghi sai số điều trong proposal môn Khởi nghiệp là lỗi bị trừ điểm nặng.

**(b) Chống gian lận thi cử.** Máy cho thuê đi thi khác mọi loại máy cho thuê khác ở một điểm: **nhà trường có quyền nghi ngờ máy chứa công cụ gian lận.** Biên bản bàn giao có mục "tình trạng phần mềm + mã bản image + niêm phong" chính là bằng chứng bảo vệ **cả sinh viên lẫn doanh nghiệp**.

**(c) Vận hành.** Biên bản là **nguồn dữ liệu gốc** để tính mọi chỉ số ở §6: turnaround time, tỉ lệ hư hỏng, tỉ lệ trả trễ, tuổi pin.

## 2.2. Danh mục trường bắt buộc — 11 nhóm, 58 trường

🔵 [TT] — tổng hợp từ thực hành ngành (🟡 [KT-MH]) + checklist Grover 5 điểm và quy trình 6 ảnh trong file `02`/`08` (🟢 [XM]).

### Nhóm 1 — Định danh giao dịch (5 trường)

| # | Trường | Kiểu | Bắt buộc | Vì sao |
|---|---|---|---|---|
| 1.1 | Mã đơn thuê (`RENT-YYYYMMDD-NNN`) | Text | ✅ | Khoá liên kết ảnh, hợp đồng, hoá đơn, log |
| 1.2 | Ngày giờ giao (chính xác đến phút) | Datetime | ✅ | Gốc để tính phí trễ theo giờ |
| 1.3 | Ngày giờ **cam kết trả** | Datetime | ✅ | Mốc T+0 của thang leo thang §8 |
| 1.4 | Địa điểm giao | Text | ✅ | Bằng chứng "giao trong khuôn viên" |
| 1.5 | Nhân viên giao (họ tên + chữ ký) | Text+Sign | ✅ | Quy trách nhiệm nội bộ |

### Nhóm 2 — Định danh bên thuê (8 trường)

| # | Trường | Kiểu | Bắt buộc | Ghi chú rủi ro |
|---|---|---|---|---|
| 2.1 | Họ tên đầy đủ | Text | ✅ | Phải khớp thẻ SV |
| 2.2 | **MSSV** | Text | ✅ | Tài sản thế chấp phi tiền tệ mạnh nhất của mô hình 🟢 [XM] file 02 |
| 2.3 | Email trường (`@fpt.edu.vn`) | Email | ✅ | Kênh gửi văn bản có dấu vết ở §8 |
| 2.4 | Số điện thoại + **Zalo** | Text | ✅ | Kênh nhắc nợ chính |
| 2.5 | Số CCCD (**chỉ ghi số + ảnh 2 mặt**) | Text+Img | ✅ | 🔴 **TUYỆT ĐỐI KHÔNG giữ bản gốc CCCD** 🟢 [XM] file 08 §10.2 |
| 2.6 | Ảnh chụp **người thuê cầm thẻ SV** | Image | ✅ | Chống mạo danh; mô phỏng selfie-with-ID của Grover 🟢 [XM] file 02 |
| 2.7 | Lớp / chuyên ngành / kỳ | Text | ⬜ | Dùng phân khúc, dự báo mùa vụ |
| 2.8 | Người bảo lãnh (nếu có) — tên + MSSV | Text | ⬜ | Cơ chế giảm cọc 🟢 [XM] file 02 (bài học #6) |

> ⚠️ **Về dữ liệu cá nhân:** phải có ô tick **đồng ý thu thập & xử lý dữ liệu**, ghi rõ **mục đích** và **thời hạn xoá** (đề xuất: xoá ảnh CCCD trong **07 ngày** sau khi kết thúc hợp đồng và hoàn cọc). 🟡 [KT-MH]: văn bản cần tra là **Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân**, và cần kiểm tra xem đến 2026 đã có **Luật Bảo vệ dữ liệu cá nhân** thay thế/bổ sung chưa. 🔴 **Bắt buộc tra** — từ khoá: `Nghị định 13/2023/NĐ-CP bảo vệ dữ liệu cá nhân`, `Luật Bảo vệ dữ liệu cá nhân 2025 hiệu lực`.

### Nhóm 3 — Định danh tài sản (9 trường) ← **nhóm dễ bị làm ẩu nhất**

| # | Trường | Kiểu | Bắt buộc | Vì sao quan trọng |
|---|---|---|---|---|
| 3.1 | Mã nội bộ (`FPT-LT-007`) | Text | ✅ | Dán nhãn ngoài + QR |
| 3.2 | Hãng / Model chính xác | Text | ✅ | Cơ sở định giá đền bù |
| 3.3 | **Serial Number / Service Tag** | Text | ✅ | 🟢 [XM] file 08: *"Ghi Service Tag/Serial vào hợp đồng; dán tem niêm phong có số — Cao: chống tráo máy, hỗ trợ trình báo công an"* |
| 3.4 | Cấu hình (CPU / RAM / SSD) | Text | ✅ | Khách phải biết mình thuê gì |
| 3.5 | Phiên bản Windows + trạng thái kích hoạt | Text | ✅ | Máy chưa kích hoạt = rủi ro lỗi giữa ca thi |
| 3.6 | **Mã bản Golden Image** (`IMG-2026-09-v3`) + **SHA-256 rút gọn 8 ký tự** | Text | ✅ | 🔵 [TT] — bằng chứng "máy sạch", dùng khi giám thị hỏi |
| 3.7 | **Số tem niêm phong** | Text | ✅ | Tem vỡ = có can thiệp phần cứng |
| 3.8 | **% pin lúc giao** (đọc từ Windows) | Number | ✅ | Chuẩn giao: **≥ 95%** |
| 3.9 | **SoH pin gần nhất** (%) + ngày đo | Number+Date | ✅ | §5 |

### Nhóm 4 — Phụ kiện đi kèm (7 trường, đếm từng món)

| # | Món | Bắt buộc | Giá đền bù niêm yết (VND) |
|---|---|---|---|
| 4.1 | Củ sạc + dây nguồn | ✅ | 🔴 [KTĐ] — nhóm khảo sát giá thị trường |
| 4.2 | Túi chống sốc | ✅ | 🔴 [KTĐ] |
| 4.3 | Chuột không dây + pin | ⬜ | 🔴 [KTĐ] |
| 4.4 | **Tai nghe có dây (jack 3.5mm)** | ✅ (môn thi nghe) | 🔴 [KTĐ] |
| 4.5 | Tem niêm phong (số hiệu) | ✅ | Phí bóc tem: đề xuất 100.000 |
| 4.6 | Phiếu hướng dẫn nhanh + hotline | ✅ | — |
| 4.7 | Cáp mạng LAN / USB-Ethernet (nếu phòng thi dùng dây) | ⬜ | 🔴 [KTĐ] |

> 🟢 [XM] file 10 — UConn tách bạch giá đền bù: **laptop 1.500 USD, dây sạc 30 USD**. Bài học: **phải niêm yết giá đền bù RIÊNG cho từng phụ kiện**, không gộp.

### Nhóm 5 — Tình trạng ngoại hình lúc giao (8 trường) → xem thang chi tiết §3

| # | Trường | Kiểu | Bắt buộc |
|---|---|---|---|
| 5.1 | **Xếp hạng tổng thể** A / B / C / D | Enum | ✅ |
| 5.2 | Mặt A (nắp lưng) — mô tả + số vết | Text+Num | ✅ |
| 5.3 | Mặt B (màn hình + viền) — số điểm chết, vết xước màn | Text+Num | ✅ |
| 5.4 | Mặt C (bàn phím + chiếu nghỉ tay + touchpad) | Text+Num | ✅ |
| 5.5 | Mặt D (đáy máy, chân đế, ốc) | Text+Num | ✅ |
| 5.6 | 4 góc/cạnh — móp, nứt | Text | ✅ |
| 5.7 | Bản lề — độ chắc, tiếng kêu | Enum | ✅ |
| 5.8 | Cổng kết nối — cong, gãy chân | Text | ✅ |

### Nhóm 6 — Kiểm tra chức năng 12 điểm (bắt buộc TICK TỪNG Ô)

🟢 [XM] — nền tảng là checklist 5 điểm mà Grover công bố (**màn hình / Bluetooth / loa / camera / bàn phím**), nguồn [Grover — Signs of use / asset condition](https://www.grover.com/at-en/g-about/asset-condition), và bài học #4 trong file `02`: *"cần bổ sung: pin (chu kỳ sạc + % health), cổng sạc, wifi, webcam (bắt buộc cho thi online), microphone, phím F, touchpad"*. 🔵 [TT] mở rộng thành 12 điểm cho bối cảnh EOS + SEB.

| # | Hạng mục | Cách test (làm được trong 30 giây) | Đạt/Không |
|---|---|---|---|
| 6.1 | **Màn hình** | Mở ảnh nền trắng toàn màn + đen toàn màn, soi điểm chết / hở sáng | ☐ |
| 6.2 | **Bàn phím** | Mở `keyboardtester` offline hoặc Notepad, gõ đủ A–Z, 0–9, **F1–F12**, Ctrl/Alt/Shift/Tab/Esc | ☐ |
| 6.3 | **Touchpad** | Di chuyển, click trái/phải, cuộn 2 ngón | ☐ |
| 6.4 | **Webcam** | Mở app Camera, thấy hình rõ | ☐ |
| 6.5 | **Micro** | Ghi âm 5 giây, phát lại nghe được | ☐ |
| 6.6 | **Loa** | Phát file test, nghe cả 2 loa | ☐ |
| 6.7 | **Jack 3.5mm** | Cắm tai nghe, nghe rõ 2 tai — 🔴 **critical cho môn thi nghe** | ☐ |
| 6.8 | **Wi-Fi** | Kết nối được mạng test, ping ra ngoài | ☐ |
| 6.9 | **Cổng USB (tất cả)** | Cắm USB, nhận ổ | ☐ |
| 6.10 | **Cổng sạc + củ sạc** | Cắm vào, Windows báo "đang sạc" | ☐ |
| 6.11 | **Pin** | `powercfg /batteryreport` → SoH ≥ ngưỡng (§5) | ☐ |
| 6.12 | 🔴 **Chạy thử EOS Client + SEB** | Khởi động SEB, vào được màn hình đăng nhập EOS, **thoát sạch** | ☐ |

> 🔑 **Điểm 6.12 là toàn bộ giá trị khác biệt của mô hình.** 🟢 [XM] file 02, bài học #11: Drexel Law **bắt buộc chạy thử bài thi trước khi được dùng máy mượn** → *"Khác biệt cốt lõi của dự án: cho thuê máy đã test với hệ thống thi của FPT, không phải một cái laptop."*
> Theo file `01`, cấu phần "máy sẵn sàng thi" gồm: SEB (`SEB_3.10.0.794_AutoSettings.msi` tải từ `exam.fpt.edu.vn`), **EOS Client cài đúng thư mục gốc** (nhà trường cảnh báo copy ra ngoài thư mục gốc → **không khởi động được**), tai nghe có dây, sạc, chuột.

### Nhóm 7 — Ảnh & video bằng chứng (bắt buộc)

🟢 [XM] file 08 quy định **6 ảnh**. 🔵 [TT] nâng lên **8 ảnh** để bao được điểm tranh chấp hay gặp nhất (cạnh máy và cổng sạc):

| # | Ảnh | Yêu cầu kỹ thuật |
|---|---|---|
| 7.1 | Mặt A — nắp lưng đóng | Đủ sáng, thấy trọn máy + nhãn mã máy |
| 7.2 | Mặt B — màn hình **đang bật** hiển thị ảnh nền trắng | Bắt buộc bật để lộ điểm chết |
| 7.3 | Mặt C — bàn phím, chiếu nghỉ tay | Chụp thẳng từ trên |
| 7.4 | Mặt D — đáy máy | Thấy rõ serial dán đáy |
| 7.5 | Cạnh trái (cổng) | Cận cảnh |
| 7.6 | Cạnh phải (cổng) | Cận cảnh |
| 7.7 | **Cận cảnh tem niêm phong** + số tem | Đọc được số |
| 7.8 | **Toàn bộ phụ kiện bày ra mặt bàn** | 1 khung hình đủ món |
| 7.9 | **Video 30 giây**: mở–gập máy, gõ thử bàn phím, xoay 360° | 🟢 [XM] file 08 |

> **Quy tắc lưu trữ:** tất cả upload lên Google Drive theo cấu trúc `/RENT-YYYYMMDD-NNN/giao/` và `/RENT-YYYYMMDD-NNN/nhan/`. 🟢 [XM] file 08. 🔵 [TT] bổ sung: **bật timestamp trên ảnh** (hoặc dựa vào EXIF, không xoá metadata), và **giữ tối thiểu 12 tháng** — dài hơn thời hiệu tranh chấp thực tế trong môi trường sinh viên.

### Nhóm 8 — Điều khoản khách phải đọc và ký riêng (5 ô tick)

🟢 [XM] file 02, bài học #8 (Getaround bị kiện vì **giấu điều khoản loại trừ**) → mục "KHÔNG ĐƯỢC MIỄN TRỪ" phải **in đậm, đặt ĐẦU trang**, ký xác nhận trước khi nhận máy.

| # | Nội dung ký riêng | Ô tick |
|---|---|---|
| 8.1 | Tôi **đã xem và đồng ý** với ảnh/video tình trạng máy lúc giao | ☐ |
| 8.2 | Tôi hiểu **gói miễn trừ KHÔNG bao gồm**: mất máy, trộm cắp, cố ý phá hoại, cho người khác thuê lại, tháo linh kiện, ngâm nước, cháy nổ | ☐ |
| 8.3 | Tôi cam kết **không tháo tem niêm phong**, không cài phần mềm bẻ khoá, **không cài phần mềm điều khiển từ xa** | ☐ |
| 8.4 | Tôi hiểu **máy sẽ được xoá sạch dữ liệu** sau khi trả — tôi **tự sao lưu**, bên cho thuê không chịu trách nhiệm mất dữ liệu | ☐ |
| 8.5 | Tôi hiểu bên cho thuê **không chịu trách nhiệm về kết quả thi**; trách nhiệm tối đa = hoàn tiền thuê + cấp máy thay thế | ☐ |

> 🔑 Điều 8.5 là 🟢 [XM] file 08 §10.3 điều khoản #11: *"nếu máy hỏng khiến sinh viên trượt môn, khách có thể đòi bồi thường học phí học lại (vài triệu đồng). Phải giới hạn rõ trách nhiệm."*
> 🔑 Điều 8.3 (cấm phần mềm điều khiển từ xa) 🔵 [TT]: đây vừa là điều khoản chống gian lận, vừa là điều khoản kỹ thuật — 🟡 [KT-MH] Safe Exam Browser có **danh sách tiến trình bị cấm** và sẽ **từ chối khởi động** nếu phát hiện phần mềm như TeamViewer/AnyDesk/UltraViewer đang chạy. **Cần nhóm tự kiểm chứng bằng cách cài thử và chạy SEB.**

### Nhóm 9 — Tài chính (6 trường)
Giá thuê · Phí gói miễn trừ (nếu mua) · Tiền cọc · Phương thức thanh toán · Đã thu (VND) · Điều kiện & thời điểm hoàn cọc.

### Nhóm 10 — Chữ ký (4 trường)
Bên thuê (ký + ghi rõ họ tên) · Nhân viên giao · Ngày giờ ký · **Ảnh chụp biên bản đã ký** (nếu ký giấy) hoặc mã e-sign.

### Nhóm 11 — Phần dành riêng cho lúc NHẬN LẠI máy (check-in) — 9 trường
Ngày giờ trả thực tế · Trễ bao nhiêu phút · Xếp hạng ngoại hình khi nhận (A/B/C/D) · **Chênh lệch hạng so với lúc giao** · Phát hiện hư hỏng (mô tả + ảnh) · Đủ/thiếu phụ kiện · % pin khi trả · Tem niêm phong còn nguyên? · Xử lý cọc (hoàn 100% / trừ bao nhiêu / lý do).

## 2.3. Mẫu biên bản in A4 — dùng được ngay (BM-01)

🔵 [TT]. Nhóm chỉ cần đổi tên thương hiệu và số điện thoại.

```
════════════════════════════════════════════════════════════════════
                    BIÊN BẢN BÀN GIAO LAPTOP CHO THUÊ
                         Mã đơn: RENT-________-____
════════════════════════════════════════════════════════════════════
Hôm nay, ngày ____ tháng ____ năm 20____, hồi ____ giờ ____ phút,
tại: ______________________________________________________________

BÊN CHO THUÊ (Bên A): ____________________________________________
  Người đại diện giao máy: _________________  SĐT: ________________

BÊN THUÊ (Bên B):
  Họ tên: _________________________________  MSSV: ________________
  Email trường: ___________________@fpt.edu.vn
  SĐT/Zalo: ____________________  Số CCCD: _________________________
  Lớp/Ngành: ______________________
  ☐ Đã chụp ảnh CCCD 2 mặt   ☐ Đã chụp ảnh người thuê cầm thẻ SV
  ☐ Bên B ĐỒNG Ý cho Bên A thu thập, lưu trữ ảnh giấy tờ nêu trên
     nhằm mục đích xác minh danh tính và thu hồi tài sản; Bên A cam
     kết XOÁ trong vòng 07 ngày sau khi thanh lý hợp đồng.

────────────────────── I. TÀI SẢN BÀN GIAO ─────────────────────────
Mã máy: ____________   Hãng/Model: ________________________________
Serial/Service Tag: _______________________________________________
Cấu hình: CPU ___________ RAM ______GB  SSD ______GB  Win ____
Bản image: IMG-________-v___   SHA-256 (8 ký tự đầu): ____________
Số tem niêm phong: ____________   % pin lúc giao: ______%
Sức khoẻ pin (SoH): ______%  (đo ngày ____/____/______)

Phụ kiện (đánh dấu món có giao, ghi giá đền bù):
  ☐ Củ sạc + dây .......... đền: ____________ VND
  ☐ Túi chống sốc ......... đền: ____________ VND
  ☐ Chuột + pin ........... đền: ____________ VND
  ☐ Tai nghe 3.5mm ........ đền: ____________ VND
  ☐ Khác: _______________   đền: ____________ VND

──────────────── II. TÌNH TRẠNG NGOẠI HÌNH LÚC GIAO ────────────────
XẾP HẠNG TỔNG THỂ:   ☐ A (Như mới)   ☐ B (Tốt)
                     ☐ C (Khá – có dấu hiệu dùng rõ)   ☐ D (Đã cũ)
  Mặt A (nắp):  số vết xước >5mm: ____   móp/nứt: ☐ Không ☐ Có: ____
  Mặt B (m.hình): điểm chết: ____  hở sáng: ☐ Không ☐ Có  xước: ____
  Mặt C (phím):  phím mòn chữ: ____  ố/bẩn: ☐ Không ☐ Có
  Mặt D (đáy):   ☐ Nguyên ốc   ☐ Thiếu ốc: ____   ☐ Móp
  Cạnh/góc:      ☐ Nguyên vẹn  ☐ Móp tại: _______________________
  Bản lề:        ☐ Chắc  ☐ Rơ nhẹ  ☐ Kêu       Cổng: ☐ OK ☐ Lỗi:___
  Ghi chú khác: ____________________________________________________

───────────── III. KIỂM TRA CHỨC NĂNG 12 ĐIỂM (Bên B chứng kiến) ────
☐1 Màn hình  ☐2 Bàn phím  ☐3 Touchpad  ☐4 Webcam  ☐5 Micro  ☐6 Loa
☐7 Jack 3.5  ☐8 Wi-Fi     ☐9 Cổng USB  ☐10 Sạc    ☐11 Pin
☐12 ★ ĐÃ CHẠY THỬ EOS CLIENT + SAFE EXAM BROWSER TRƯỚC MẶT BÊN B ★

─────────────────────── IV. BẰNG CHỨNG HÌNH ẢNH ────────────────────
☐ Đã chụp đủ 8 ảnh (A / B bật màn / C / D / cạnh trái / cạnh phải /
  tem niêm phong / phụ kiện)      ☐ Đã quay video 30 giây
Đường dẫn lưu trữ: /RENT-________-____/giao/

──────────────────── V. THỜI HẠN VÀ TÀI CHÍNH ──────────────────────
Giao lúc: ____h____ ngày ____/____/______
HẠN TRẢ:  ____h____ ngày ____/____/______   ← BÊN B GHI LẠI SỐ NÀY
Giá thuê: ____________ VND   Gói miễn trừ: ____________ VND
Tiền cọc: ____________ VND   Tổng đã thu: ____________ VND
Phí trả trễ: __________ VND/giờ, TỐI ĐA __________ VND/ngày
Quá hạn ____ ngày → coi như MẤT MÁY, thu giá trị thay thế
  = ____________ VND (đã trừ cọc)

────────────── VI. CAM KẾT CỦA BÊN THUÊ (ký từng dòng) ─────────────
1. Tôi đã xem ảnh/video tình trạng máy và ĐỒNG Ý. ......... Ký: ____
2. Tôi hiểu gói miễn trừ KHÔNG bao gồm: MẤT MÁY, trộm cắp,
   cố ý phá hoại, cho người khác thuê lại, tháo linh kiện,
   ngâm nước, cháy nổ. .................................... Ký: ____
3. Tôi KHÔNG tháo tem niêm phong, KHÔNG cài phần mềm bẻ khoá,
   KHÔNG cài phần mềm điều khiển từ xa. ................... Ký: ____
4. Tôi hiểu máy sẽ ĐƯỢC XOÁ SẠCH sau khi trả; tôi tự sao lưu
   dữ liệu của mình. ...................................... Ký: ____
5. Tôi hiểu Bên A KHÔNG chịu trách nhiệm về kết quả thi; trách
   nhiệm tối đa của Bên A = hoàn tiền thuê + cấp máy thay thế.
                                                            Ký: ____

Biên bản lập thành 02 bản (hoặc 01 bản điện tử có chữ ký số/ảnh),
mỗi bên giữ 01 bản, có giá trị như nhau.

    BÊN CHO THUÊ (A)                        BÊN THUÊ (B)
  (ký, ghi rõ họ tên)                   (ký, ghi rõ họ tên)



════════════════════════════════════════════════════════════════════
        ★★★ PHẦN DƯỚI CHỈ ĐIỀN KHI NHẬN LẠI MÁY (CHECK-IN) ★★★
════════════════════════════════════════════════════════════════════
Trả lúc: ____h____ ngày ____/____/______   Trễ: ______ phút
Xếp hạng ngoại hình khi NHẬN: ☐A ☐B ☐C ☐D   Chênh so với giao: ____
Tem niêm phong: ☐ Còn nguyên  ☐ Bị bóc/rách → LẬP BIÊN BẢN RIÊNG
Phụ kiện: ☐ Đủ   ☐ Thiếu: ______________________________________
% pin khi trả: ______%
Hư hỏng phát hiện: ______________________________________________
  ☐ Đã chụp 8 ảnh đối chiếu + đối chiếu trực tiếp với ảnh lúc giao
Xử lý cọc: ☐ Hoàn 100% = ________ VND
           ☐ Trừ ________ VND, lý do: __________________________
           ☐ Chuyển hồ sơ sang quy trình đền bù (SOP-06)

   Bên A nhận máy (ký)                 Bên B trả máy (ký)


════════════════════════════════════════════════════════════════════
```

## 2.4. Ba lỗi làm biên bản bàn giao trở nên vô dụng

🔵 [TT] — rút ra từ logic tranh chấp:

| Lỗi | Hậu quả | Cách chặn |
|---|---|---|
| **Ghi "tình trạng: bình thường"** thay vì đếm số vết xước | Khi khách trả về với vết mới, không chứng minh được vết nào là mới | Bắt buộc **điền SỐ**, ô trống = không hợp lệ |
| **Chụp ảnh khi màn hình tắt** | Điểm chết/hở sáng không thể hiện; khách trả về có điểm chết, không ai chứng minh được | Ảnh 7.2 **bắt buộc màn hình bật nền trắng** |
| **Khách ký một lần ở cuối** | Khách nói "tôi ký mà không đọc điều khoản loại trừ" | **Ký từng dòng** ở mục VI (5 chữ ký riêng) — mô phỏng bài học Getaround 🟢 [XM] file 02 |

---
# 3. THANG ĐÁNH GIÁ TÌNH TRẠNG NGOẠI HÌNH (COSMETIC GRADING)

## 3.1. Sự thật quan trọng nhất về grading: **KHÔNG có tiêu chuẩn quốc tế bắt buộc**

🟡 [KT-MH] — đây là điều nhóm cần nói thẳng trong proposal vì nó vừa là rủi ro vừa là cơ hội:

> Trong ngành **refurbished IT** (thiết bị tân trang), **không tồn tại một tiêu chuẩn pháp lý bắt buộc nào** định nghĩa "Grade A". Mỗi sàn, mỗi nhà tân trang **tự định nghĩa** thang của mình. Hệ quả: "Grade A" của người bán này có thể tương đương "Grade B" của người bán khác.

**Bằng chứng gián tiếp đã xác minh 🟢 [XM]** — file `02`, mô tả cách Grover tính giá hư hỏng: *"Dựa trên **market-standard grading guidelines** + database hàng nghìn ca sửa chữa để quyết định chi phí"* — nguồn [Grover Help — Repair and replacement costs](https://service.grover.com/hc/en-us/articles/19918338642578-Repair-and-replacement-costs). Cụm **"market-standard grading guidelines"** (hướng dẫn phân hạng theo chuẩn thị trường) xác nhận: có *thông lệ thị trường*, nhưng Grover **không nêu tên một tiêu chuẩn cụ thể nào** — đúng với nhận định "không có chuẩn bắt buộc".

**Suy ra cho proposal 🔵 [TT]:** vì không có chuẩn ép buộc, nhóm **PHẢI tự công bố thang của mình một cách định lượng**. Một thang định lượng tự công bố, in trên biên bản, còn mạnh hơn việc viện dẫn một chuẩn mà khách không đọc.

## 3.2. Các hệ thang đang tồn tại trên thị trường — bảng đối chiếu

🟡 [KT-MH] toàn bộ bảng này. **Không có URL nào được xác minh trong phiên.** Cột cuối là **câu lệnh tìm kiếm chính xác** để nhóm tự tra.

| Hệ thang | Ai dùng | Các cấp | Đặc điểm nhận dạng | Từ khoá để nhóm tự tra |
|---|---|---|---|---|
| **Grade A / B / C / D** (thông dụng nhất ngành refurb IT) | Đa số nhà tân trang, đại lý B2B, chợ hàng hoàn | A = như mới → D = cũ nặng nhưng chạy được | Chữ cái, đôi khi có **A+** ở trên A | `refurbished laptop grade A B C definition` |
| **Grade 1 / 2 / 3** | Một số nhà bán buôn châu Âu | 1 = tốt nhất | Số thay chữ | `refurbished grade 1 2 3 laptop grading` |
| **Excellent / Very Good / Good / Acceptable** | Sàn TMĐT lớn (chương trình hàng tân trang của eBay, Amazon) | 4 cấp mô tả bằng từ | Ngôn ngữ marketing, dễ hiểu với người tiêu dùng | `eBay Refurbished conditions excellent very good good`, `Amazon Renewed condition guidelines` |
| **Premium / Excellent / Good / Fair** | Back Market và các sàn refurb tiêu dùng | 3–4 cấp | Nhấn ngoại hình, cam kết chức năng như nhau ở mọi cấp | `Back Market grade Fair Good Excellent difference` |
| **"Certified Refurbished" không phân hạng** | Chương trình tân trang của chính hãng | 1 cấp duy nhất | Mọi máy đều **như mới**, thay vỏ/pin mới | `Apple Certified Refurbished condition standard` |
| **Không phân hạng, chỉ "signs of use"** | 🟢 [XM] **Grover** | Không có A/B/C công khai | *"Xước nhỏ và dấu hiệu sử dụng bình thường được làm sạch MIỄN PHÍ"* — [Grover asset condition](https://www.grover.com/at-en/g-about/asset-condition) | — (đã xác minh) |

> 🔑 **Bài học chiến lược từ Grover 🟢 [XM]:** Grover **không bắt khách hiểu thang A/B/C**. Grover chỉ tách làm **2 loại**: "hao mòn bình thường" (miễn phí) và "hư hỏng" (tính tiền). File `02` gọi đây là *"cách giảm tranh chấp mạnh nhất"*.
> → **Đề xuất kép cho nhóm 🔵 [TT]:** dùng **thang 4 cấp A/B/C/D cho NỘI BỘ** (định giá thuê, quyết định thanh lý), nhưng **chỉ giao tiếp 2 mức với khách** ("hao mòn bình thường — miễn phí" vs "hư hỏng — tính tiền theo bảng giá"). Khách không cần học thang của nhóm; nhóm cần thang để quản trị tài sản.

## 3.3. Định nghĩa từng cấp — bản mô tả ngành (🟡 [KT-MH])

Đây là **cách hiểu phổ biến** của các cấp trong ngành refurbished. **Không phải văn bản chuẩn — nhóm phải tự tra và có thể trích dẫn cụ thể trang nào định nghĩa như vậy.**

| Cấp | Tên thường gọi | Ngoại hình | Màn hình | Chức năng | Ghi chú thị trường |
|---|---|---|---|---|---|
| **A+ / Grade A+** | *Mint / Like New* | **Không thấy khuyết điểm** bằng mắt thường. Thường là máy trưng bày, máy hoàn trong thời hạn đổi trả, hoặc đã thay vỏ mới | Hoàn hảo, **không điểm chết** | 100% | Giá bán lại gần sát máy mới |
| **A / Grade A** | *Excellent* | Có thể có **1–2 vết xước rất nhẹ**, chỉ thấy khi soi nghiêng dưới ánh sáng; **không móp, không nứt** | Không điểm chết, không hở sáng đáng kể | 100% | Cấp phổ biến nhất được rao bán |
| **B / Grade B** | *Good* | **Xước nhìn thấy được** ở khoảng cách gần, có thể có **móp nhẹ** ở góc/cạnh; phím có thể mờ chữ nhẹ; **không nứt vỏ** | Có thể có **hở sáng nhẹ ở viền**; thường vẫn cam kết không điểm chết ở vùng trung tâm | 100% | Giá thấp hơn A khoảng một bậc |
| **C / Grade C** | *Fair / Acceptable* | **Xước/móp rõ ràng**, nhiều vị trí; có thể **ố vàng vỏ**, phím mòn chữ, chiếu nghỉ tay bóng mòn; có thể **nứt nhựa nhỏ** không ảnh hưởng kết cấu | Có thể có **điểm chết ở rìa**, hở sáng | 100% (đây là điểm mấu chốt: **C vẫn phải chạy đủ chức năng**) | Bán cho khách ưu tiên giá |
| **D / Grade D** | *Poor / Cosmetically damaged* | **Hư hại ngoại hình nặng**: nứt vỏ lớn, thiếu chi tiết trang trí, bản lề rơ, móp sâu | Có thể có điểm chết rõ | Vẫn hoạt động, nhưng thường **không được bán lẻ**, chỉ bán linh kiện/xác | Không phù hợp cho thuê |
| **F / "For parts"** | *Không hoạt động* | — | — | **Không hoạt động** | Ngoài phạm vi kinh doanh |

**Nguyên tắc chung của mọi thang (🟡 [KT-MH], nhất quán giữa các nguồn):**
1. **Grading chỉ nói về NGOẠI HÌNH.** Từ A đến C (đôi khi D), **chức năng phải là 100%**. Một máy đẹp nhưng bàn phím liệt 1 phím **không phải Grade A** — nó là **máy lỗi**, ra khỏi thang.
2. **Điểm chết màn hình thường được tách thành chính sách riêng** ("dead pixel policy"), không nằm trong grade chữ cái.
3. **Pin thường được tách riêng** khỏi cosmetic grade và mô tả bằng **% sức khoẻ** — xem §5.
4. Khoảng cách quan sát chuẩn hay được viện dẫn là **"chiều dài cánh tay" (~30 cm)** hoặc **"30 cm dưới ánh sáng phòng thông thường"**.

## 3.4. 🔵 [TT] THANG ĐỀ XUẤT CHO DỰ ÁN — **có định lượng, tick được trong 60 giây**

Vấn đề của thang ngành: **quá mơ hồ để một sinh viên trực quầy dùng lúc 7h sáng.** Dưới đây là bản đã định lượng hoá, thiết kế để **hai người khác nhau chấm cùng một máy sẽ ra cùng một hạng**.

**Điều kiện chấm chuẩn hoá:** ánh sáng phòng bình thường, **khoảng cách 30 cm**, máy đã lau sạch, màn hình bật nền trắng rồi nền đen.

| Hạng | Vết xước dài **> 5 mm** (đếm trên toàn máy) | Móp / nứt | Màn hình | Bàn phím & chiếu nghỉ tay | Bản lề | Dùng để làm gì |
|---|---|---|---|---|---|---|
| **A** | **0–2 vết**, không vết nào dài > 20 mm | Không có | 0 điểm chết, không hở sáng thấy được ở nền đen | Chữ phím rõ 100%, không bóng mòn | Chắc, không rơ | **Máy "tuyến đầu"** — ưu tiên giao cho khách lần đầu, khách VIP, gói giá cao |
| **B** | **3–8 vết**, hoặc có ≤ 2 vết dài 20–50 mm | Móp nhẹ ≤ 2 vị trí, đường kính < 5 mm, **không nứt** | ≤ 1 điểm chết **ngoài vùng trung tâm**; hở sáng nhẹ ở 1 góc | ≤ 3 phím mờ chữ; chiếu nghỉ tay hơi bóng | Chắc | **Máy chủ lực** — dùng bình thường cho mọi đơn |
| **C** | **> 8 vết**, hoặc có vết dài > 50 mm | Móp rõ ≥ 3 vị trí, hoặc **nứt nhựa < 10 mm không xuyên thấu** | ≤ 2 điểm chết ngoài trung tâm; hở sáng thấy rõ ở ≥ 2 góc | > 3 phím mờ; ố/bóng rõ | Rơ nhẹ nhưng giữ được góc mở | **Máy dự phòng / gói giá rẻ / cho thuê tháng**. 🔴 **KHÔNG dùng làm hot spare ngày thi** (đưa máy xấu cho khách đang hoảng loạn = trải nghiệm tệ nhất) |
| **D** | Không đếm nổi | Nứt xuyên thấu, thiếu chi tiết, móp sâu | > 2 điểm chết hoặc điểm chết ở trung tâm | Phím kẹt/liệt (→ thành máy lỗi) | Rơ, không giữ góc | 🔴 **RA KHỎI ĐỘI CHO THUÊ.** Chuyển sang: máy linh kiện, máy trưng bày, hoặc thanh lý (chạy SOP-08) |

### Quy tắc vận hành gắn với thang này (🔵 [TT])

| Quy tắc | Nội dung | Lý do |
|---|---|---|
| **R1 — Chấm 2 lần/lượt thuê** | Chấm lúc giao và lúc nhận, ghi cả hai vào biên bản | Chênh lệch hạng = bằng chứng hư hỏng phát sinh |
| **R2 — Tụt 1 hạng trong 1 lượt thuê = có sự kiện** | Tự động tạo hồ sơ "sự cố ngoại hình", chụp ảnh so sánh, quyết định có tính phí không | Ngăn "chết dần" không ai chịu trách nhiệm |
| **R3 — Hao mòn bình thường KHÔNG tính tiền** | Tụt hạng do dùng bình thường (thêm 1–2 vết xước nhỏ sau nhiều lượt) → **doanh nghiệp chịu** | 🟢 [XM] file 08 §10.3 điều khoản #8; 🟢 [XM] Grover miễn phí làm sạch dấu hiệu sử dụng bình thường |
| **R4 — Chỉ tính tiền khi có "sự kiện rời rạc"** | Móp mới, nứt mới, vết xước dài > 20 mm mới, vỡ màn, dính chất lỏng | Ranh giới rõ ràng = ít tranh chấp |
| **R5 — Giá thuê phân hạng** | A: giá niêm yết 100% · B: 100% (không giảm) · C: **giảm 15–20%**, ghi rõ "máy ngoại hình cũ, chức năng 100%" trên web | Bán được cả máy xấu mà không bị mang tiếng lừa |
| **R6 — Hạng vào đội** | 🔴 Chỉ **nhận máy hạng A hoặc B** vào đội ban đầu | Máy vào đội đã hạng C thì sau 20 lượt thuê sẽ là D — hết vòng đời quá sớm |
| **R7 — Công bố ảnh thật trên web** | Mỗi mã máy có **ảnh thật của chính máy đó**, không dùng ảnh catalogue | Chống khiếu nại "máy khác ảnh"; chi phí gần 0 |

### 🔵 [TT] Bảng giá đền bù gắn với mức tụt hạng — khung để nhóm điền số

Cột giá **phải do nhóm khảo sát thực tế** (🔴 [KTĐ]) — file `08` §8.1 đã có sẵn bảng khảo sát chi phí sửa chữa để dùng.

| Sự kiện | Mức tụt hạng điển hình | Ai chịu | Mức thu đề xuất |
|---|---|---|---|
| Thêm 1–2 vết xước < 20 mm | Không tụt hạng | 🟢 Doanh nghiệp | 0 đồng |
| Bẩn, dính thức ăn, vết tay | Không tụt | 🟢 Doanh nghiệp | 0 đồng (đã tính trong phí vệ sinh) |
| Xước dài > 20 mm mới | A→B | Khách | Phí thẩm mỹ cố định, đề xuất **50.000–100.000 VND** |
| Móp góc mới | B→C | Khách | 🔴 [KTĐ] khảo giá thay vỏ |
| Nứt vỏ / nứt viền màn | C→D | Khách | 🔴 [KTĐ] |
| Vỡ màn hình | Ra khỏi thang (máy lỗi) | Khách | 🔴 [KTĐ] khảo giá thay màn theo model |
| Vào nước | Máy lỗi, có thể chết | Khách | 🔴 [KTĐ] — thường là **loại trừ** khỏi gói miễn trừ 🟢 [XM] file 08 |
| Mất máy | — | Khách | **100% giá trị thay thế** đã niêm yết trong biên bản 🟢 [XM] file 08 |

> 🟢 [XM] Neo tham chiếu quốc tế từ file `02`: **Rent the Runway** thu **nguyên giá bán lẻ** khi mất/hỏng không sửa được ([RTR Terms of Service](https://www.renttherunway.com/pages/termsofservice)); **Grover** chỉ thu **20% giá bán lẻ đề xuất (RRP)** khi thiết bị hỏng không sửa được — nhưng đó là vì khách **đã mua gói Grover Care** ([Grover Help — Repair and replacement costs](https://service.grover.com/hc/en-us/articles/19918338642578-Repair-and-replacement-costs)).
> → 🔵 [TT] **Cấu trúc 2 tầng để sao chép:** không mua gói miễn trừ → **100% giá trị thay thế**; có mua gói → **trần trách nhiệm** (file `08` đề xuất tối đa 500.000đ/vụ cho hư hỏng, và **gói KHÔNG áp dụng cho mất máy**).

---

# 4. CHUẨN BỊ MÁY GIỮA CÁC LƯỢT THUÊ (TURNAROUND / REFRESH)

## 4.1. Nguyên tắc thiết kế: 3 mức xử lý, không phải một

🔵 [TT]. Sai lầm phổ biến nhất của đội mới là **reimage mọi máy sau mọi lượt thuê** → tốn 40 phút/máy × 30 máy = 20 giờ nhân công mỗi đợt thi, bất khả thi với đội 3–4 sinh viên. Giải pháp là **phân tầng**.

| Mức | Tên | Khi nào dùng | Nhân công/máy | Tỉ lệ áp dụng dự kiến |
|---|---|---|---|---|
| **L1** | **Quick Turn** (quay vòng nhanh) | Máy trả về đúng hạn, tem nguyên, không báo lỗi, **có Deep Freeze hoặc tương đương** | **~20 phút** | ~80% số lượt |
| **L2** | **Standard Reimage** (khôi phục bản chuẩn) | Không có cơ chế đóng băng; hoặc khách báo đã cài phần mềm; hoặc định kỳ (đề xuất **mỗi 5 lượt thuê**); hoặc **trước mọi đợt thi lớn** | **~40 phút** | ~18% |
| **L3** | **Deep Rebuild** (dựng lại từ đầu) | Nghi nhiễm mã độc; tem niêm phong bị bóc; máy lỗi lạ; **trước mỗi học kỳ**; **trước khi thanh lý máy** | **4–8 giờ** (phần lớn là chờ) | ~2% + 1–2 lần/năm toàn đội |

> 🔴 **NGOẠI LỆ TUYỆT ĐỐI:** với **bối cảnh thi cử**, 🔵 [TT] khuyến nghị **nâng chuẩn**: **mọi máy trước khi giao cho một ca thi PHẢI ở trạng thái image gốc đã xác thực hash** — nghĩa là L1 chỉ được coi là đủ **nếu và chỉ nếu** cơ chế đóng băng (Deep Freeze) đảm bảo phân vùng hệ thống đã trở về đúng bản gốc sau reboot. Nếu không có cơ chế đó, **bắt buộc L2**. Lý do: một cáo buộc gian lận thi cử liên quan đến máy thuê có thể **giết chết cả doanh nghiệp trong một ngày**.

## 4.2. Bảng so sánh công cụ — 10 lựa chọn

🟡 [KT-MH] **toàn bộ bảng**. Cột "Giá" và "Trạng thái phiên bản" là phần **dễ lỗi thời nhất** → nhóm bắt buộc tra lại.

| Công cụ | Bản chất | Giấy phép / Giá | Ưu điểm cho đội 15–40 máy | Nhược điểm | Phù hợp? |
|---|---|---|---|---|---|
| **Clonezilla** (Live) | Ảnh đĩa (disk imaging), boot từ USB | **Miễn phí, mã nguồn mở (GPL)** | Nhẹ, chạy từ USB, không cần hạ tầng; sao chép nguyên khối rất nhanh; hỗ trợ nhiều hệ tập tin | Giao diện dòng lệnh/ncurses xấu, dễ **chọn nhầm nguồn/đích → xoá nhầm ổ**; bản Live chỉ làm **1 máy 1 lúc** | 🟢 **Rất phù hợp** — nên là công cụ nền |
| **Clonezilla SE** (Server Edition, trong bộ **DRBL**) | Máy chủ ảnh đĩa, boot mạng PXE, **multicast** | Miễn phí, mã nguồn mở | **Bung ảnh cho hàng chục máy CÙNG LÚC** qua LAN — đúng nhu cầu "chuẩn bị cả đội trước đợt thi" | Cần dựng máy chủ Linux + cấu hình PXE/DHCP; **cần switch và mạng riêng** (không được cắm vào mạng trường → xung đột DHCP) | 🟡 Phù hợp **nếu** nhóm có 1 thành viên rành Linux |
| **FOG Project** | Máy chủ ảnh đĩa mã nguồn mở, có **giao diện web**, PXE, multicast, quản lý tồn kho, "snap-in" cài phần mềm | **Miễn phí, mã nguồn mở** | Giao diện web dễ hơn Clonezilla SE nhiều; có sẵn **quản lý tài sản, lịch sử tác vụ, đặt lịch** — trùng khớp nhu cầu quản trị đội máy | Cũng cần máy chủ Linux + mạng riêng; cài đặt ban đầu tốn 1 buổi | 🟢 **Lựa chọn tốt nhất nếu chọn hướng máy chủ ảnh** |
| **MDT — Microsoft Deployment Toolkit** | Bộ công cụ triển khai Windows theo **task sequence**, cài từ nguồn (thin image) | Miễn phí từ Microsoft | Cài Windows "sạch" + driver + phần mềm tự động, không cần ảnh đĩa; xử lý tốt máy khác model | 🔴 **Đã ở trạng thái bảo trì/di sản** — bản cuối 🟡 **MDT 8456 (2019)**; Microsoft đẩy sang Autopilot/Intune. Cấu hình phức tạp, chậm hơn ảnh đĩa | 🟠 **Không khuyến nghị** cho đội sinh viên — quá nặng so với lợi ích |
| **Windows Autopilot Reset** | Đặt lại máy về cấu hình doanh nghiệp ban đầu, **giữ máy đã tham gia Entra ID + đăng ký Intune** | 🔴 **Cần giấy phép Intune / Microsoft 365** (trả tiền theo người dùng/tháng) | Rất sạch về mặt quy trình; có thể kích hoạt **từ xa**; có **"Local Autopilot Reset"** bằng tổ hợp phím ở màn hình khoá | 🔴 **Chi phí giấy phép là rào cản chí mạng** với dự án sinh viên; cần hạ tầng Entra ID; máy phải luôn có mạng | 🔴 **Không phù hợp giai đoạn đầu.** Đưa vào slide "lộ trình mở rộng" |
| **Macrium Reflect** | Sao lưu & ảnh đĩa cho Windows, có giao diện đồ hoạ đẹp, tạo được **USB cứu hộ** | 🔴 🟡 **Bản Free đã bị khai tử (khoảng cuối 2023/đầu 2024)** — hiện là sản phẩm **trả phí** | Giao diện dễ dùng nhất trong nhóm; **Macrium reDeploy** giúp phục hồi ảnh sang phần cứng khác | Trả phí; hướng cá nhân/doanh nghiệp nhỏ hơn là đội máy | 🟠 Chỉ chọn nếu nhóm ngại dòng lệnh **và** chấp nhận trả phí |
| **Deep Freeze (Faronics)** | **"Khởi động lại là sạch"** — đóng băng phân vùng hệ thống; mọi thay đổi **biến mất sau mỗi lần reboot** | 🔴 **Trả phí theo máy/năm** (🔴 [KTĐ] — nhóm phải xin báo giá đại lý VN) | 🟢 **Thay đổi cuộc chơi:** turnaround từ ~40 phút xuống **1–3 phút**. Đúng bài toán "phòng máy/máy cho thuê dùng chung". Có phiên bản đám mây quản lý tập trung | Không xoá dữ liệu ghi vào **phân vùng dữ liệu/ThawSpace**; **không phải công cụ sanitization** theo NIST; cần cửa sổ "rã đông" để cập nhật Windows; chi phí giấy phép | 🟢 **Khuyến nghị mạnh** nếu chi phí giấy phép ≤ ~2–3% giá máy/năm |
| **"Reset this PC" của Windows** | Chức năng có sẵn: đặt lại Windows, có tuỳ chọn **"xoá sạch ổ đĩa" (clean the drive)** | Miễn phí, có sẵn | Không cần công cụ ngoài; tuỳ chọn "clean the drive" **ghi đè dữ liệu** (chậm hơn nhưng an toàn hơn) | Chậm (🟡 ~30–90 phút); **không khôi phục được phần mềm thi đã cài** → sau đó vẫn phải cài lại EOS/SEB | 🟠 Dùng làm **phương án dự phòng** khi ảnh đĩa hỏng |
| **Sysprep + DISM** | Công cụ Microsoft: `sysprep /generalize` để "tổng quát hoá" máy mẫu, `DISM /Capture-Image` & `/Apply-Image` để bắt/bung tệp WIM | Miễn phí, có sẵn trong Windows/ADK | **Bắt buộc phải hiểu** nếu tự tạo Golden Image: không chạy `sysprep /generalize` thì mọi máy trùng **SID** và trùng tên | Dòng lệnh; 🟡 có **giới hạn số lần chạy `sysprep /generalize` trên một bản cài (thường được nêu là 3 lần)** — cần tra lại | 🟢 **Bắt buộc học** — là nền của mọi hướng ảnh đĩa |
| **Rescuezilla** | Giao diện đồ hoạ "thân thiện" bọc ngoài Clonezilla, tương thích định dạng ảnh của Clonezilla | Miễn phí, mã nguồn mở | Dễ dùng hơn hẳn Clonezilla cho người mới; **ảnh dùng chung được với Clonezilla** | Ít tính năng nâng cao hơn; không có multicast | 🟢 **Rất hợp cho sinh viên mới bắt đầu** |

### 🔴 Cảnh báo về công cụ KHÔNG nên dùng

| Công cụ | Vì sao không | Nhãn |
|---|---|---|
| **DBAN (Darik's Boot and Nuke)** | 🔴 **KHÔNG xử lý đúng ổ SSD** — ghi đè theo địa chỉ logic không chạm tới các khối đã bị wear-leveling ánh xạ đi nơi khác; ngoài ra dự án **không còn được phát triển**. Với SSD phải dùng **ATA Secure Erase / NVMe Format NVM / crypto erase** | 🟡 [KT-MH] |
| **Ghi đè 7 lần / 35 lần ("chuẩn DoD", "Gutmann")** | 🔴 **Lỗi thời.** NIST SP 800-88 Rev.1 nêu rõ với ổ hiện đại **một lượt ghi đè là đủ** cho mức Clear. Ghi đè 7 lần chỉ **đốt thời gian và tuổi thọ ổ** | 🟡 [KT-MH] |

## 4.3. 🔵 [TT] KIẾN TRÚC KHUYẾN NGHỊ CHO ĐỘI 15–40 MÁY

**Nguyên tắc chọn: chi phí giấy phép thấp, một người vận hành được, không cần phòng máy chủ.**

```
┌──────────────────────────────────────────────────────────────────┐
│  TẦNG 1 — PHÒNG NGỪA (chạy hằng ngày, chi phí thời gian ~0)      │
│  • Deep Freeze bật trên phân vùng C: của MỌI máy cho thuê        │
│    → khách cài gì cũng biến mất sau reboot                       │
│  • Tài khoản Windows cục bộ tên "THISINH", KHÔNG tài khoản MS,   │
│    KHÔNG OneDrive, KHÔNG đăng nhập trình duyệt                   │
│  • BIOS/UEFI: đặt mật khẩu quản trị, TẮT boot USB & boot mạng,   │
│    bật Secure Boot  → khách không thể khởi động hệ điều hành lạ  │
│  • Tem niêm phong có số ở khe ốc đáy máy                         │
└──────────────────────────────────────────────────────────────────┘
                              ↓ (khi cần khôi phục thật)
┌──────────────────────────────────────────────────────────────────┐
│  TẦNG 2 — KHÔI PHỤC (định kỳ / khi có sự cố)                     │
│  • GOLDEN IMAGE lưu trên 2 ổ cứng di động (1 dùng, 1 dự phòng)   │
│    + 1 bản trên đám mây                                          │
│  • Bung bằng Clonezilla Live (hoặc Rescuezilla nếu ngại CLI)     │
│  • Đặt tên phiên bản: IMG-YYYYMM-vN + tệp SHA-256 + CHANGELOG.md │
│  • Giữ 2 phiên bản gần nhất, xoá phiên bản cũ hơn                │
└──────────────────────────────────────────────────────────────────┘
                              ↓ (khi chuẩn bị cả đội trước đợt thi)
┌──────────────────────────────────────────────────────────────────┐
│  TẦNG 3 — HÀNG LOẠT (1–2 lần/học kỳ, nếu quy mô > 25 máy)        │
│  • FOG Project trên 1 máy cũ + 1 switch gigabit riêng            │
│  • Bung multicast cho 10–20 máy song song                        │
│  • KHÔNG cắm vào mạng của trường (xung đột DHCP/PXE)             │
└──────────────────────────────────────────────────────────────────┘
```

### Cấu phần bắt buộc của Golden Image (🔵 [TT])

| # | Thành phần | Ghi chú |
|---|---|---|
| 1 | Windows 10/11 **đã kích hoạt**, đã cập nhật tới mốc ngày X | Ghi rõ mốc trong CHANGELOG |
| 2 | Toàn bộ driver đúng model | Nếu đội có nhiều model → **mỗi model 1 image riêng**, đừng cố dùng chung |
| 3 | **EOS Client + IT Client giải nén ĐÚNG THƯ MỤC GỐC** | 🟢 [XM] file 01: nhà trường cảnh báo copy ra ngoài thư mục gốc → **không khởi động được** |
| 4 | **Safe Exam Browser** (bản đúng, tải từ `exam.fpt.edu.vn`) | 🟢 [XM] file 01 nêu `SEB_3.10.0.794_AutoSettings.msi` — 🔴 nhóm phải kiểm tra bản mới nhất tại thời điểm triển khai |
| 5 | Trình duyệt sạch (không đăng nhập), bộ gõ tiếng Việt, trình đọc PDF | Không cài thừa |
| 6 | 🔴 **KHÔNG có**: phần mềm điều khiển từ xa, máy ảo, trình ghi màn hình, phần mềm chat | Rủi ro cáo buộc gian lận |
| 7 | Tài khoản cục bộ `THISINH`, không mật khẩu hoặc mật khẩu in trên phiếu | Không dùng tài khoản Microsoft |
| 8 | Đã chạy `sysprep /generalize /oobe` trước khi bắt ảnh | Tránh trùng SID |
| 9 | Tệp `C:\FLEET_INFO.txt` ghi mã máy, mã image, hotline | Kỹ thuật viên và cả sinh viên đều tra được nhanh |

## 4.4. Quy trình từng bước — 3 mức

### 🔧 L1 — QUICK TURN (mục tiêu: ~20 phút nhân công)

| Bước | Thao tác | Thời gian | Bằng chứng lưu |
|---|---|---|---|
| 1 | Nhận máy, đối chiếu **mã máy + serial + số tem** với biên bản | 1' | Tick biên bản |
| 2 | Đếm phụ kiện | 1' | Tick |
| 3 | Chụp **8 ảnh** đối chiếu | 3' | Ảnh vào `/nhan/` |
| 4 | **Chấm hạng ngoại hình** (§3.4), so với hạng lúc giao | 2' | Ghi biên bản |
| 5 | **Khởi động lại máy** → Deep Freeze khôi phục phân vùng hệ thống | 1–3' | — |
| 6 | Chạy **checklist 12 điểm** (§2.2 nhóm 6) | 5–7' | Tick 12 ô |
| 7 | **Chạy thử EOS + SEB**, thoát sạch | 3' | Tick |
| 8 | Lau máy (khăn microfiber + dung dịch chuyên dụng), lau bàn phím | 3' | — |
| 9 | Cắm sạc, để pin lên **≥ 95%** | *chạy song song* | Ghi % pin |
| 10 | Cập nhật **nhật ký máy** (số lượt +1, giờ sử dụng, sự cố nếu có) | 2' | Nhật ký |
| 11 | Đổi trạng thái trên web thành **"Sẵn sàng"** | 1' | Hệ thống |
| **Tổng nhân công** | | **~20–22'** | |
| **Tổng thời gian thực (wall clock)** | Bị chặn bởi thời gian sạc | **60–120'** | |

> 🔑 **Điểm mấu chốt về thời gian thực:** turnaround **không bị giới hạn bởi nhân công mà bởi PIN**. Đây là lý do §7 khuyến nghị hot spare — và là lý do phải có **ổ cắm nhiều cổng + nhiều củ sạc** tại điểm trực. 🔵 [TT]

### 🔧 L2 — STANDARD REIMAGE (mục tiêu: ~40 phút nhân công)

| Bước | Thao tác | SSD NVMe | SSD SATA | Ghi chú |
|---|---|---|---|---|
| 1–4 | Như L1 bước 1–4 | 7' | 7' | |
| 5 | Cắm USB Clonezilla, vào BIOS (mật khẩu quản trị), chọn boot USB | 3' | 3' | |
| 6 | **Bung Golden Image** (~30 GB nén) | **5–10'** | **8–15'** | 🔵 [TT] ước lượng; multicast qua LAN gigabit cho cả lô 20 máy: **15–25'/lô** |
| 7 | Khởi động lần đầu, OOBE, **đặt tên máy theo mã nội bộ** | 5–8' | 5–8' | |
| 8 | Kiểm tra kích hoạt Windows + driver | 3' | 3' | |
| 9 | Cập nhật SEB/EOS nếu trường ra bản mới | 0–15' | 0–15' | Chỉ khi cần |
| 10 | Bật lại **Deep Freeze** | 2' | 2' | 🔴 Rất hay quên — đặt vào checklist in ra dán tường |
| 11 | Checklist 12 điểm + chạy thử EOS/SEB | 8' | 8' | |
| 12 | Lau + sạc + ảnh + nhật ký | 6' | 6' | |
| **Tổng nhân công** | | **~39'** | **~45'** | |

### 🔧 L3 — DEEP REBUILD (4–8 giờ, phần lớn là chờ)

| Bước | Thao tác | Thời gian 🔵 [TT] |
|---|---|---|
| 1 | **Xoá dữ liệu theo NIST 800-88** (xem §4.7) | SSD (ATA Secure Erase / crypto erase): **1–5'** · SSD ghi đè 1 lượt 256 GB: **10–25'** · HDD 500 GB ghi đè 1 lượt: **60–120'** |
| 2 | Cài Windows sạch từ ISO chính thức | 15–25' |
| 3 | Cài driver theo model (từ trang hãng) | 20–40' |
| 4 | Windows Update tới hết | **30–120'** (chờ) |
| 5 | Cài bộ phần mềm thi + cấu hình + tài khoản | 20–40' |
| 6 | Kiểm thử đầy đủ + **chạy tải liên tục (burn-in) 2–4 giờ** | 2–4 giờ (chờ) |
| 7 | `sysprep /generalize /oobe` + bắt ảnh mới (nếu đây là máy mẫu) | 20–30' |
| 8 | Ghi CHANGELOG + tính SHA-256 của ảnh | 10' |
| **Tổng** | | **4–8 giờ** |

## 4.5. Bảng tổng hợp thời gian — dùng để lập kế hoạch nhân sự mùa thi

🔵 [TT]. Giả định: đội **30 máy**, mỗi máy quay vòng **1 lượt/ngày** trong tuần thi, phân bổ 80% L1 / 18% L2 / 2% L3.

| Kịch bản | Phép tính | Nhân công/ngày | Số người cần (ca 4 giờ) |
|---|---|---|---|
| **Có Deep Freeze** (80/18/2) | 24 máy × 20' + 5,4 máy × 40' + 0,6 máy × 300' | 480 + 216 + 180 = **876 phút ≈ 14,6 giờ** | **~4 người × 4 giờ** |
| **Không có Deep Freeze** (bắt buộc L2 mọi lượt) | 30 máy × 40' | **1.200 phút = 20 giờ** | **~5 người × 4 giờ** |
| **Chênh lệch** | | **−5,4 giờ/ngày** | **−1 người** |

> 🔑 **Đây là lập luận tài chính để mua Deep Freeze:** tiết kiệm ~5,4 giờ nhân công/ngày trong tuần thi. Nếu đội thi 5 ngày × 3 đợt/năm = 15 ngày → **~81 giờ nhân công/năm**. Nhân với đơn giá cộng tác viên trong file `11` (**25.000–30.000 VND/giờ** 🟢 [XM]) → **~2,0–2,4 triệu VND/năm tiết kiệm được**, chưa kể giảm rủi ro sai sót. Nhóm so con số này với báo giá giấy phép Deep Freeze cho 30 máy (🔴 [KTĐ] phải xin báo giá) để ra quyết định **có căn cứ, đưa thẳng vào proposal**.

## 4.6. Ghép quy trình vào bài toán đặt lịch của website

🟢 [XM] file `09-kien-truc-phan-mem-rental.md` đã giải quyết đúng vấn đề này ở tầng cơ sở dữ liệu:

> *"Giữa hai lượt thuê cần thời gian: kiểm tra máy, cài lại/kiểm tra EOS + Safe Exam Browser, sạc pin, lau máy. **Không nên** để hai đơn sát nhau 0 phút."* → kỹ thuật: cộng buffer vào khoảng thời gian giữ chỗ, ví dụ **60–120 phút** sau giờ trả.
> **Đối chiếu ngành:** Odoo Rental gọi khái niệm này là **"Security Time"** — *"the option to set a Security Time, expressed in hours, to make the rental product temporarily unavailable between two rental orders"* — [Odoo 18 Rental docs](https://www.odoo.com/documentation/18.0/applications/sales/rental.html)

🔵 [TT] **Đề xuất tham số Security Time cụ thể**, khớp với bảng thời gian ở §4.4:

| Trường hợp | Security Time nên đặt | Căn cứ |
|---|---|---|
| Quay vòng trong cùng một ngày thi (đơn ca sáng → ca chiều) | **90 phút** | 20' nhân công + đệm sạc pin + đệm rủi ro |
| Quay vòng qua đêm | **12 giờ** (chốt sổ cuối ngày) | Cho phép L2 nếu cần |
| Sau một lượt thuê ≥ 7 ngày | **24 giờ** | Bắt buộc L2 |
| Sau sự cố (khách báo lỗi) | **Khoá thủ công**, không tự mở lại | Bắt buộc L3 |

---
# 4.7. NIST SP 800-88 — CHUẨN XOÁ DỮ LIỆU (MEDIA SANITIZATION)

> 🟡 [KT-MH] **TOÀN BỘ MỤC NÀY.** Không xác minh được trong phiên (hết ngân sách tìm kiếm). Tài liệu gốc là công khai, miễn phí, do NIST (Viện Tiêu chuẩn và Công nghệ Quốc gia Hoa Kỳ) phát hành.
> **Tên chính xác để nhóm tra:** `NIST Special Publication 800-88 Revision 1 — Guidelines for Media Sanitization` (phát hành **tháng 12/2014**).
> **Câu tìm kiếm gợi ý:** `NIST SP 800-88 Rev 1 Guidelines for Media Sanitization PDF`, `NIST 800-88 Clear Purge Destroy definition`, `NIST 800-88 Appendix G certificate of sanitization`.

## 4.7.1. Vì sao một dự án cho thuê laptop cho sinh viên lại cần một chuẩn của Mỹ

Ba lý do rất thực tế, **nên viết thẳng vào proposal**:

1. **Bảo vệ khách.** Sinh viên đăng nhập email, Facebook, ngân hàng trên máy thuê. Nếu người thuê sau khôi phục được dữ liệu đó → khủng hoảng niềm tin, chấm dứt kinh doanh trong cộng đồng khép kín. 🟢 [XM] file `02` xác nhận Grover đặt **"Xoá sạch dữ liệu (data wipe)"** là **bước 2 trong 4 bước** quy trình tân trang của họ ([Grover asset condition](https://www.grover.com/at-en/g-about/asset-condition)).
2. **Nghĩa vụ pháp lý về dữ liệu cá nhân.** 🟡 [KT-MH] — cần tra **Nghị định 13/2023/NĐ-CP** và tình trạng **Luật Bảo vệ dữ liệu cá nhân** tại thời điểm 2026. Doanh nghiệp xử lý dữ liệu cá nhân có nghĩa vụ **xoá** khi hết mục đích.
3. **Sự khác biệt bán hàng.** Không đối thủ nào ở Đà Nẵng công bố quy trình xoá dữ liệu có chuẩn. Một dòng *"Mỗi máy được xoá dữ liệu theo mức Clear của NIST SP 800-88 Rev.1 và cấp Chứng nhận xoá dữ liệu"* là **điểm khác biệt gần như miễn phí**.

## 4.7.2. Ba mức sanitization của NIST SP 800-88 Rev.1

| Mức | Tên | Định nghĩa (diễn giải) | Chống được gì | Ví dụ kỹ thuật | Media còn dùng lại được? |
|---|---|---|---|---|---|
| **1** | **CLEAR** (Xoá) | Dùng **lệnh đọc/ghi thông thường** của thiết bị để ghi đè vùng người dùng truy cập được | Chống **khôi phục đơn giản, không xâm lấn** (phần mềm undelete, gắn ổ sang máy khác) | Ghi đè toàn ổ **1 lượt**; "Reset this PC" + tuỳ chọn *clean the drive*; `format /p:1` | ✅ Có |
| **2** | **PURGE** (Tẩy) | Kỹ thuật vật lý hoặc logic khiến việc khôi phục **bất khả thi với kỹ thuật phòng lab tiên tiến nhất** | Chống **khôi phục ở cấp phòng thí nghiệm** | **ATA Secure Erase / ATA Sanitize (block erase)**; **NVMe Format NVM**; **Cryptographic Erase** (xoá khoá của ổ tự mã hoá); **khử từ (degauss)** — chỉ cho ổ từ tính | ✅ Có (trừ degauss thường làm hỏng ổ cứng) |
| **3** | **DESTROY** (Huỷ) | Phá huỷ vật lý | Chống mọi khôi phục | Cắt vụn (shred), nghiền, đốt, biến dạng | ❌ Không |

## 4.7.3. Cây quyết định — chọn mức nào? (🟡 [KT-MH] diễn giải logic của tài liệu)

NIST quyết định dựa trên **2 câu hỏi**: (a) mức bí mật của dữ liệu, (b) **media có rời khỏi tầm kiểm soát của tổ chức không**.

```
      Máy chuẩn bị đi đâu?
              │
   ┌──────────┴───────────────────────────────┐
   │                                          │
Quay vòng NỘI BỘ                    RỜI khỏi tầm kiểm soát
(cho khách tiếp theo thuê,          (bán thanh lý, trả máy ký gửi,
 máy vẫn của mình)                   tặng, đem đi sửa ở ngoài)
   │                                          │
   ▼                                          ▼
  CLEAR là đủ                         PURGE (tối thiểu)
  (+ khôi phục Golden Image)          + Chứng nhận xoá dữ liệu
   │                                          │
   │                            Ổ hỏng không chạy được lệnh xoá?
   │                                          │
   │                                          ▼
   │                                      DESTROY
   ▼
  ⚠ NGOẠI LỆ: nếu khách báo đã đăng nhập
    ngân hàng / lưu tài liệu nhạy cảm
    → nâng lên PURGE dù là quay vòng nội bộ
```

🔵 [TT] **Áp dụng cho dự án:**

| Tình huống | Mức NIST | Việc phải làm | Thời gian |
|---|---|---|---|
| Quay vòng thường (L1/L2) | **Clear** *(đạt được gián tiếp qua việc bung đè Golden Image)* | Bung Golden Image ghi đè toàn bộ phân vùng | Đã tính ở §4.4 |
| Máy có nghi ngờ dữ liệu nhạy cảm / tem bị bóc / trước mỗi học kỳ (L3) | **Purge** | ATA Secure Erase hoặc NVMe Format NVM hoặc crypto erase | 1–5' (SSD) |
| **Thanh lý / bán máy / trả máy ký gửi** | **Purge + Chứng nhận** | Purge + xác minh + cấp **Chứng nhận xoá dữ liệu** (BM-07) | 10–20' |
| Ổ SSD hỏng không nhận lệnh | **Destroy** | Tháo ổ, phá vật lý, chụp ảnh làm bằng chứng | 10' |

> ⚠️ **Lưu ý quan trọng về "bung Golden Image = Clear":** 🔵 [TT] — bung ảnh đĩa **ghi đè toàn bộ phân vùng đích**, nên trên thực tế đạt được hiệu quả tương đương Clear **cho vùng bị ghi đè**. Nhưng nếu ảnh chỉ bung lên phân vùng C: mà máy còn phân vùng D: chứa dữ liệu khách thì **D: KHÔNG được xoá**. → **Quy tắc cứng: Golden Image phải bung ở mức TOÀN Ổ (whole disk), không phải mức phân vùng.**

## 4.7.4. Ba điểm kỹ thuật mà đội vận hành rất dễ làm sai

| # | Điểm | Giải thích 🟡 [KT-MH] | Hệ quả nếu sai |
|---|---|---|---|
| 1 | **SSD ≠ HDD.** Ghi đè theo địa chỉ logic **không chạm tới** các khối vật lý đã bị "san bằng hao mòn" (wear leveling) ánh xạ đi chỗ khác, cũng như vùng dự phòng (over-provisioning) | Với SSD phải dùng lệnh của chính firmware ổ: **ATA Secure Erase**, **ATA Sanitize**, **NVMe Format NVM** — hoặc crypto erase | Tưởng đã xoá mà vẫn còn dữ liệu ở khối ẩn |
| 2 | **Rev.1 đã bỏ học thuyết "ghi đè nhiều lượt"** | Với ổ ATA hiện đại, **một lượt ghi đè là đủ** cho mức Clear. Khuyến nghị ghi đè 7/35 lượt là **di sản từ thời ổ từ tính mật độ thấp** | Đốt hàng giờ vô ích, hao tuổi thọ SSD |
| 3 | **Crypto erase chỉ đáng tin nếu toàn bộ dữ liệu ĐÃ được mã hoá từ đầu** | Nếu bật BitLocker **sau khi** đã ghi dữ liệu ở trạng thái chưa mã hoá, xoá khoá **không** đảm bảo dữ liệu cũ biến mất | Chứng nhận xoá dữ liệu trở thành sai sự thật |

## 4.7.5. Xác minh (verification) — bước hay bị bỏ qua nhất

🟡 [KT-MH] — NIST nhấn mạnh **sanitization chưa hoàn tất nếu chưa xác minh**, và nêu hai cách: **xác minh toàn phần** hoặc **xác minh theo mẫu đại diện** (đọc ngẫu nhiên nhiều vùng trên ổ, gồm cả đầu, giữa, cuối, xác nhận chỉ còn mẫu ghi đè).

🔵 [TT] **Quy trình xác minh tối giản cho nhóm sinh viên (5 phút/máy):**
1. Sau khi Purge, boot bằng USB Linux (Ubuntu Live / Clonezilla).
2. Đọc mẫu ngẫu nhiên bằng công cụ dòng lệnh ở **≥ 5 vị trí** trên ổ (đầu, 25%, 50%, 75%, cuối).
3. Xác nhận toàn bộ là giá trị 0 (hoặc mẫu ghi đè đã dùng).
4. Chạy một công cụ khôi phục tệp miễn phí (ví dụ PhotoRec/TestDisk) trong **2 phút** — nếu không thấy tệp nào của người dùng cũ thì đạt.
5. Chụp màn hình kết quả → đính vào Chứng nhận xoá dữ liệu.

## 4.7.6. Chứng nhận xoá dữ liệu (Certificate of Sanitization) — BM-07

🟡 [KT-MH] — NIST SP 800-88 Rev.1 có **mẫu biểu ở phần phụ lục** (thường được nhắc là **Appendix G**) với các trường như dưới. 🔴 Nhóm phải mở PDF gốc để đối chiếu tên trường chính xác.

```
════════════════════════════════════════════════════════════════════
             CHỨNG NHẬN XOÁ DỮ LIỆU (CERTIFICATE OF SANITIZATION)
   Tham chiếu khung: NIST SP 800-88 Rev.1 (12/2014) — [cần nhóm tra lại]
════════════════════════════════════════════════════════════════════
Số chứng nhận: SAN-________-____        Ngày: ____/____/________

── A. THÔNG TIN THIẾT BỊ ───────────────────────────────────────────
Mã tài sản nội bộ: ____________   Hãng: ____________________
Model: ______________________   Serial của MÁY: __________________
Loại media:  ☐ SSD SATA  ☐ SSD NVMe  ☐ HDD  ☐ eMMC  ☐ Khác: ______
Dung lượng: ________ GB        Serial của Ổ ĐĨA: ________________
Nguồn gốc (ai dùng trước): _______________________________________
Phân loại dữ liệu:  ☐ Công khai  ☐ Nội bộ  ☐ Dữ liệu cá nhân KH

── B. PHƯƠNG PHÁP XOÁ ──────────────────────────────────────────────
Mức áp dụng:  ☐ CLEAR   ☐ PURGE   ☐ DESTROY
Kỹ thuật cụ thể: ☐ Ghi đè 1 lượt   ☐ ATA Secure Erase
                 ☐ ATA Sanitize (block erase)  ☐ NVMe Format NVM
                 ☐ Cryptographic Erase   ☐ Phá huỷ vật lý
Công cụ + phiên bản: ______________________________________________
Tham số/ghi chú: __________________________________________________
Bắt đầu: ____h____   Kết thúc: ____h____   Kéo dài: ______ phút

── C. XÁC MINH ─────────────────────────────────────────────────────
Cách xác minh: ☐ Toàn phần  ☐ Mẫu đại diện (số vị trí: ____)
Kết quả:  ☐ ĐẠT   ☐ KHÔNG ĐẠT → xử lý: ___________________________
Công cụ khôi phục đã thử: ________________  Tệp tìm thấy: ________
Ảnh chụp màn hình đính kèm:  ☐ Có

── D. ĐÍCH ĐẾN CỦA THIẾT BỊ ────────────────────────────────────────
☐ Quay lại đội cho thuê   ☐ Bán thanh lý   ☐ Trả chủ ký gửi
☐ Tặng   ☐ Tiêu huỷ/ thải bỏ   ☐ Khác: _________________________
Phân loại dữ liệu SAU khi xoá: ☐ Công khai

── E. XÁC NHẬN ─────────────────────────────────────────────────────
NGƯỜI THỰC HIỆN                     NGƯỜI KIỂM TRA ĐỘC LẬP
Họ tên: _______________________     Họ tên: _______________________
Vai trò: ______________________     Vai trò: ______________________
Ngày:  ____/____/______             Ngày:  ____/____/______
Ký:                                 Ký:

════════════════════════════════════════════════════════════════════
```

> 🔵 [TT] **Mẹo dùng cho marketing:** gửi bản PDF Chứng nhận này cho khách qua Zalo sau mỗi lượt thuê. Chi phí ~0 đồng, tạo cảm giác chuyên nghiệp vượt hẳn mọi đối thủ địa phương, và là **bằng chứng đã làm đúng nghĩa vụ dữ liệu cá nhân** nếu bị khiếu nại.

## 4.8. 🔴 Gói kiểm soát chống cáo buộc gian lận thi cử (đặc thù của dự án này)

🔵 [TT] — không tìm thấy tiền lệ trong các nguồn đã xác minh; đây là thiết kế riêng cho bối cảnh EOS + SEB.

| # | Biện pháp | Chi phí | Giá trị |
|---|---|---|---|
| 1 | **Mã bản image + SHA-256 in trên biên bản** | 0đ | Chứng minh máy ở đúng trạng thái đã công bố |
| 2 | **Tem niêm phong có số ở khe ốc đáy máy** | ~2.000đ/tem | 🟢 [XM] file 08: chống tráo máy, hỗ trợ trình báo |
| 3 | **BIOS có mật khẩu quản trị, tắt boot USB & boot mạng, bật Secure Boot** | 0đ | Khách không thể khởi động hệ điều hành khác để lách SEB |
| 4 | **Tài khoản Windows duy nhất `THISINH`**, không tài khoản quản trị cho khách | 0đ | Khách không cài được phần mềm mới |
| 5 | **Danh sách phần mềm cài sẵn công bố trên web** cho từng mã máy | 0đ | Minh bạch tuyệt đối |
| 6 | **"Giấy chứng nhận máy sạch"** 1 trang kèm mỗi lượt thuê ca thi, để sinh viên xuất trình nếu giám thị hỏi | ~500đ in | 🔑 **Đây có thể là tính năng bán hàng mạnh nhất của toàn dự án** |
| 7 | **Chủ động gửi quy trình cho Phòng Khảo thí xin ý kiến trước khi kinh doanh** | 0đ | 🟢 [XM] file 01/02 xếp đây là **rủi ro R6 phải xử lý TRƯỚC MỌI VIỆC KHÁC** |

---

# 5. SỨC KHOẺ PIN (BATTERY HEALTH)

## 5.1. Vì sao pin là rủi ro vận hành số 1 của mô hình này

🟢 [XM] file `01`: *"Pin đã kiểm tra — Cam kết pin trụ được trọn ca thi. **Phòng thi có thể thiếu ổ cắm.**"* và file `03`: yêu cầu tối thiểu của máy hạng A là **pin ≥ 3h**.

🔵 [TT] Pin là bộ phận **duy nhất** trên laptop **chắc chắn sẽ hỏng dần theo thời gian một cách không thể đảo ngược**, và là bộ phận **duy nhất** mà hỏng giữa ca thi = **khách trượt môn**. Mọi bộ phận khác hỏng thì có hot spare cứu được; pin chết lúc 8h15 trong phòng thi thì **không ai cứu được**.

## 5.2. Cách đo trên Windows — `powercfg /batteryreport`

🟡 [KT-MH]. Đây là công cụ **có sẵn trong Windows**, không cần cài gì.

### Lệnh chính xác

```powershell
:: Mở Command Prompt hoặc PowerShell với quyền Administrator, rồi:

powercfg /batteryreport /output "C:\pin\BAO-CAO-PIN.html"

:: Muốn lấy lịch sử dài hơn (mặc định thường là ~3 ngày gần nhất
:: cho phần "Recent usage", nhưng phần Capacity History dài hơn):
powercfg /batteryreport /output "C:\pin\BAO-CAO-PIN.html" /duration 14

:: Các lệnh liên quan hữu ích:
powercfg /energy  /output "C:\pin\energy.html"   :: quét lỗi tiết kiệm điện (~60 giây)
powercfg /sleepstudy /output "C:\pin\sleep.html" :: phân tích hao pin khi ngủ
powercfg /batteryreport                          :: xuất ra thư mục hiện tại
```

> 🔴 **Nhóm phải tự chạy thử một lần để xác nhận cú pháp và tên các trường** — tôi không mở được tài liệu Microsoft trong phiên này.

### Các trường quan trọng trong báo cáo HTML

| Trường (tiếng Anh trong báo cáo) | Ý nghĩa | Dùng để làm gì |
|---|---|---|
| **DESIGN CAPACITY** | Dung lượng thiết kế (mWh) — pin lúc mới xuất xưởng | Mẫu số của công thức SoH |
| **FULL CHARGE CAPACITY** | Dung lượng sạc đầy **hiện tại** (mWh) | Tử số của công thức SoH |
| **CYCLE COUNT** | Số chu kỳ sạc | ⚠️ **Rất nhiều laptop báo 0 hoặc để trống** — không phải lỗi của bạn, là do firmware không cung cấp |
| **Battery capacity history** | Bảng lịch sử dung lượng theo tuần | **Vàng ròng để quản trị đội máy** — thấy được tốc độ suy giảm |
| **Battery life estimates** | Ước tính thời lượng theo dung lượng thiết kế vs dung lượng thật | Cảnh báo sớm |
| **Recent usage / Usage history** | Lịch sử dùng pin/nguồn | Truy vết "khách nói pin tụt nhanh" |

### Công thức chuẩn

```
Sức khoẻ pin (SoH, State of Health) =
        FULL CHARGE CAPACITY  ÷  DESIGN CAPACITY  × 100%

Ví dụ:  38.500 mWh ÷ 52.000 mWh = 74,0%
```

### Công cụ bổ trợ (🟡 [KT-MH], đều miễn phí cho dùng cá nhân — nhóm tự kiểm tra giấy phép)

| Công cụ | Ưu điểm | Từ khoá tra |
|---|---|---|
| **BatteryInfoView** (NirSoft) | Xem nhanh, hiển thị wear level và cycle count | `NirSoft BatteryInfoView download` |
| **HWiNFO64** | Xem sâu cảm biến, xuất log | `HWiNFO battery wear level` |
| **BatteryBar** | Hiển thị thường trực trên thanh tác vụ | `BatteryBar Windows battery health` |

## 5.3. 🔵 [TT] NGƯỠNG SỨC KHOẺ PIN ĐỀ XUẤT CHO DỰ ÁN

**Bối cảnh ngành (🟡 [KT-MH], các mốc hay được nhắc — nhóm phải tự tra để trích dẫn được):**
- Mốc **80%** thường được dùng làm ranh giới "pin còn khoẻ" trong ngành thiết bị di động; nhiều hãng thiết kế pin để **giữ ~80% dung lượng sau một số chu kỳ nhất định** (con số chu kỳ thường được nhắc với máy tính xách tay hiện đại là khoảng **1.000 chu kỳ**).
- Mốc **50%** thường xuất hiện trong điều kiện **bảo hành**: pin tụt dưới ~50% dung lượng thiết kế trong thời hạn bảo hành mới được coi là lỗi được bảo hành.
- 🔴 **Cả hai mốc trên đều CHƯA XÁC MINH.** Từ khoá tra: `laptop battery health threshold 80 percent`, `Dell battery warranty capacity threshold`, `Apple battery 80% 1000 cycles`.

**Bảng ngưỡng đề xuất — thiết kế riêng cho mô hình cho thuê đi thi:**

| SoH đo được | Phân loại | Được làm gì | Hành động bắt buộc |
|---|---|---|---|
| **≥ 90%** | 🟢 **Xuất sắc** | Mọi gói, kể cả **hot spare ngày thi** | Đo lại mỗi 3 tháng |
| **80–89%** | 🟢 **Tốt** | Mọi gói thuê ca thi | Đo lại mỗi 2 tháng |
| **70–79%** | 🟡 **Chấp nhận có điều kiện** | Chỉ cho thuê ca thi **nếu** đã vượt bài đo thời lượng thực ở §5.4 | Đo lại **mỗi tháng**; lên kế hoạch thay pin |
| **60–69%** | 🟠 **Rút khỏi tuyến thi** | Chỉ cho thuê **theo tuần/tháng** (khách có ổ cắm); ghi rõ "pin yếu" trên web | Xin báo giá thay pin |
| **< 60%** | 🔴 **Dừng cho thuê** | Không giao cho khách | **Thay pin** hoặc chuyển sang máy trưng bày / thanh lý |

**🔴 Ngưỡng NHẬN MÁY VÀO ĐỘI: SoH ≥ 80%.** Lý do 🔵 [TT]: nếu mua máy cũ có pin 72%, sau ~6 tháng quay vòng cường độ cao pin sẽ xuống dưới 65% → phải thay pin ngay trong năm đầu, phá vỡ bài toán hoàn vốn ở file `11`. Chi phí thay pin phải được **đưa vào giá mua** khi đàm phán với cửa hàng máy cũ.

## 5.4. 🔵 [TT] Bài đo thời lượng thực — thứ quan trọng hơn cả con số %

**Vấn đề:** SoH 75% trên một máy pin thiết kế 70Wh vẫn cho thời lượng dài hơn SoH 90% trên máy pin thiết kế 38Wh. **% một mình là chỉ số gây hiểu nhầm.** Cái khách mua là **số giờ**, không phải %.

### Quy trình đo chuẩn hoá "Bài test ca thi" (chạy 1 lần khi nhận máy vào đội, sau đó mỗi 3 tháng)

| Bước | Thao tác | Tham số cố định |
|---|---|---|
| 1 | Sạc đầy 100%, rút sạc | — |
| 2 | Đặt **độ sáng màn hình 50%**, **bật Wi-Fi**, **âm lượng 30%**, cắm tai nghe | Phải giống nhau giữa các lần đo |
| 3 | Chế độ nguồn: **Balanced** (không dùng chế độ tiết kiệm tối đa — vì phòng thi thật khách không bật) | — |
| 4 | Mở **Safe Exam Browser** chạy một trang mô phỏng, để chạy liên tục | Mô phỏng tải thật |
| 5 | Bấm giờ từ 100% đến khi máy còn **20%** | 20% là ngưỡng an toàn, không đo tới 0% |
| 6 | Ghi kết quả vào nhật ký máy | |

### Tiêu chí đạt

| Kết quả đo (100% → 20%) | Kết luận | Gói được bán |
|---|---|---|
| **≥ 4,0 giờ** | 🟢 An toàn tuyệt đối | Mọi ca thi, kể cả ca dài + chờ |
| **3,5 – 3,9 giờ** | 🟢 Đạt chuẩn tối thiểu | Ca thi thường |
| **2,5 – 3,4 giờ** | 🟡 Có điều kiện | Chỉ ca thi ≤ 90 phút, **bắt buộc giao kèm củ sạc và dặn khách tìm ổ cắm** |
| **< 2,5 giờ** | 🔴 Không đạt | Rút khỏi tuyến thi |

> 🔵 [TT] **Vì sao chọn mốc 3,5 giờ:** phải dài hơn **ca thi dài nhất + thời gian chờ trước giờ thi + đệm an toàn**. Nhóm **phải thay con số này bằng thời lượng ca thi thực tế của ĐH FPT Đà Nẵng** — đây là dữ liệu nhóm có sẵn, và file `11` đã chỉ ra rằng **lịch thi thực của trường là số liệu thuyết phục nhất trong proposal**.

## 5.5. Quy tắc bảo quản pin cho đội máy (🟡 [KT-MH] — thực hành phổ biến, cần tra xác nhận)

| Quy tắc | Nội dung | Vì sao |
|---|---|---|
| **Không lưu kho ở 100%** | Máy nằm kho > 1 tuần → giữ pin ở **~50–60%**, rút sạc | Giữ pin ở điện áp cao lâu ngày làm suy giảm nhanh hơn |
| **Không lưu kho ở 0%** | Kiểm tra kho mỗi 4–6 tuần, sạc lên ~50% | Pin cạn kiệt lâu ngày có thể **chết vĩnh viễn, không sạc lại được** |
| **Chỉ sạc lên 100% ngay trước khi giao** | Sạc lên ≥95% trong cửa sổ chuẩn bị (§4.4 bước 9) | Vừa an toàn cho khách, vừa đỡ hại pin |
| **Tránh nhiệt** | Không để máy trong cốp xe máy, không sạc khi máy trong túi kín | Nhiệt là yếu tố làm hỏng pin nhanh nhất |
| **Bật giới hạn sạc của hãng nếu có** | Nhiều dòng doanh nghiệp (ThinkPad, Dell Latitude, HP EliteBook) có tuỳ chọn **giới hạn sạc ~80%** trong BIOS/phần mềm hãng | Rất hợp cho máy cho thuê tháng cắm điện liên tục |

## 5.6. 🔵 [TT] Nhật ký pin — bảng nhóm phải duy trì

| Mã máy | Pin thiết kế (mWh) | Lần đo 1 (ngày / mWh / SoH) | Lần đo 2 | Lần đo 3 | Tốc độ suy giảm (%/tháng) | Thời lượng thực đo (giờ) | Trạng thái |
|---|---|---|---|---|---|---|---|
| FPT-LT-001 | | | | | | | |
| FPT-LT-002 | | | | | | | |

**Công thức cảnh báo 🔵 [TT]:** nếu **tốc độ suy giảm > 1,5 %/tháng** liên tục 3 tháng → đặt lịch thay pin trước khi máy tụt xuống dưới 70%, thay vì đợi hỏng rồi mới xử lý. Chi phí thay pin: 🔴 [KTĐ] — nhóm dùng bảng khảo sát ở file `08` §8.1 để đi hỏi giá.

---

# 6. CHỈ SỐ NGÀNH CHO THUÊ THIẾT BỊ

## 6.1. Hai loại utilization — tuyệt đối không được nhầm

🟡 [KT-MH]. Đây là chỗ các bài proposal sinh viên hay sai nhất: nói "tỷ lệ sử dụng 60%" mà không nói là loại nào.

### (a) Time Utilization / Physical Utilization — "Tỷ lệ sử dụng theo thời gian"

```
Time Utilization (%) =    Số ngày-máy ĐANG CHO THUÊ
                        ──────────────────────────────────  × 100
                          Số ngày-máy KHẢ DỤNG trong kỳ

Ví dụ: đội 30 máy, tháng 30 ngày → 900 ngày-máy khả dụng.
Trong tháng cho thuê được tổng 270 ngày-máy.
→ Time Utilization = 270 / 900 = 30,0%
```

**Biến thể hay gặp:** một số nơi tính theo **số đơn vị đang trên tay khách / tổng số đơn vị trong đội** tại một thời điểm (chụp nhanh), thay vì tích luỹ theo ngày. 🔵 [TT] **Khuyến nghị dùng cách tích luỹ theo ngày-máy** vì nó chịu được tính mùa vụ.

**Bẫy 🔵 [TT]:** mẫu số là **"khả dụng"**, không phải "sở hữu". Máy đang chờ sửa 5 ngày thì 5 ngày đó phải **trừ khỏi mẫu số** — nếu không, một đội máy hỏng nhiều sẽ *trông có vẻ* utilization thấp vì nhu cầu thấp, trong khi thực ra là do **máy không sẵn sàng**. Phải tách riêng **Availability (tỷ lệ sẵn sàng)**:

```
Availability (%) = (Ngày-máy sở hữu − Ngày-máy hỏng/đang sửa/đang chuẩn bị)
                   ────────────────────────────────────────────────────── × 100
                                 Ngày-máy sở hữu
```

### (b) Dollar Utilization / Financial Utilization — "Tỷ lệ sử dụng theo tiền"

```
Dollar Utilization (%) =   Doanh thu CHO THUÊ 12 tháng gần nhất
                         ─────────────────────────────────────────  × 100
                           Nguyên giá đội thiết bị (OEC)

OEC = Original Equipment Cost = tổng giá mua ban đầu của đội máy
```

**Ví dụ 🔵 [TT] với số của dự án:** 30 máy × 6.200.000 VND (giá máy cũ tham chiếu ở file `11` 🟢 [XM]) = **OEC 186.000.000 VND**. Nếu doanh thu thuê 12 tháng là 74.400.000 VND → **Dollar Utilization = 40,0%**.

**Vì sao chỉ số này quan trọng hơn time utilization 🔵 [TT]:** nó trả lời trực tiếp câu *"mỗi 100 đồng bỏ vào máy, một năm thu về bao nhiêu đồng tiền thuê?"* → nghịch đảo của nó chính là **số năm hoàn vốn thô**. Dollar Utilization 40% ⇒ hoàn vốn thô **2,5 năm**. Dollar Utilization 100% ⇒ hoàn vốn thô **1 năm**.

### (c) Các chỉ số phụ trợ nên có

| Chỉ số | Công thức | Vì sao cần |
|---|---|---|
| **Doanh thu/máy/tháng** | Doanh thu thuê ÷ số máy ÷ số tháng | 🟢 [XM] file `11` đã dựng sẵn bảng độ nhạy theo chỉ số này |
| **Số lượt thuê/máy/tháng** | Tổng lượt ÷ số máy ÷ số tháng | 🟢 [XM] file `02` khuyến nghị đây là **"chỉ số Bắc Đẩu"**, không phải "số máy trong kho" |
| **Doanh thu trọn đời/máy** | Tổng doanh thu máy đó tạo ra từ khi vào đội | Đối chiếu với con số RTR: **445 → 536 USD/món** 🟢 [XM] |
| **Số lượt để hoà vốn** | Giá mua máy ÷ biên góp mỗi lượt | Đối chiếu RTR: **17–18 lượt**, thực tế đạt ~20 🟢 [XM] |
| **Tuổi trung bình đội máy** | Trung bình số tháng từ ngày vào đội | Cảnh báo cần tái đầu tư |

## 6.2. 🔴 BENCHMARK — PHẦN NGUY HIỂM NHẤT, ĐỌC KỸ

### Con số DUY NHẤT có nguồn trong toàn bộ dự án

> 🟢 [XM] — file `02-nen-tang-cho-thue-quoc-te.md`, rủi ro R2:
> *"tỷ lệ sử dụng thực tế **năm 1** của ngành cho thuê thiết bị thường **35–45%**, **không phải 80% như nhà cung cấp quảng cáo**"*
> Nguồn: [Nate Jones — Equipment rental business startup costs](https://www.natejonesentrepreneur.com/post/equipment-rental-business-startup-costs) — **đã được đánh dấu `[nguồn yếu]` / `[C]` ngay trong file gốc**, tức là blog cá nhân, không phải báo cáo ngành.

🔵 [TT] **Cách dùng đúng trong proposal:** trích con số **35–45%** kèm nguyên văn cảnh báo *"nguồn yếu, là blog khởi nghiệp chứ không phải báo cáo ngành"*, và dùng nó làm **kịch bản cơ sở thận trọng**, không làm mục tiêu. Việc **chủ động chỉ ra điểm yếu của chính nguồn mình dùng** là thứ ghi điểm trong một bài proposal môn Khởi nghiệp.

### Các mốc "nghe được trong ngành" — 🔴 TUYỆT ĐỐI KHÔNG TRÍCH NẾU CHƯA TỰ TRA

🟡 [KT-MH] — dưới đây là các khoảng số mà mô hình **nhớ mang máng** từ ngành cho thuê thiết bị xây dựng/công nghiệp Hoa Kỳ. **Tôi không thể xác minh bất kỳ con số nào trong phiên này. Nhóm KHÔNG được đưa vào bài nộp trước khi tra được nguồn gốc.**

| Chỉ số | Khoảng "được nhắc tới" | Độ tin cậy | Cách tra để có nguồn THẬT |
|---|---|---|---|
| Time utilization của đội cho thuê thiết bị lớn | ~65–72% được coi là tốt | 🔴 Thấp | Đọc báo cáo quý (10-Q) / năm (10-K) của **United Rentals**, **Herc Holdings**, **Ashtead/Sunbelt** — các công ty này công bố chỉ số này công khai. Từ khoá: `United Rentals time utilization quarterly results`, `Herc Holdings dollar utilization` |
| Dollar utilization | ~30–40% được coi là tốt | 🔴 Thấp | Như trên |
| Nguồn dữ liệu chuẩn của ngành | **Rouse Analytics**, **ARA (American Rental Association) Rental Market Monitor** | 🟡 Tên tổ chức thì đúng | `Rouse Analytics rental benchmarking`, `ARA Rental Market Monitor report` |

> 🔵 [TT] **Cảnh báo áp dụng quan trọng hơn cả con số:** các mốc trên là của **cho thuê thiết bị xây dựng, hợp đồng hàng tuần–hàng tháng, nhu cầu quanh năm**. Mô hình của nhóm là **cho thuê theo ca thi, nhu cầu dồn vào vài tuần/năm**. 🟢 [XM] file `11` cảnh báo rõ: *"tỉ lệ lấp đầy trung bình năm nhiều khả năng THẤP hơn nhiều so với 40–60%"*. **Lấy benchmark ngành xây dựng áp thẳng vào là sai về bản chất.**

### 🔵 [TT] Benchmark NỘI SINH — cách đúng đắn cho dự án này

Vì không có benchmark ngành đáng tin, hãy **tự dựng chuẩn từ chính cấu trúc mùa vụ của trường**:

```
Utilization trần lý thuyết  =  Số ngày CÓ THI trong năm × Số ca/ngày
                               ──────────────────────────────────────
                                  365 ngày × Số ca/ngày khả dụng

Ví dụ minh hoạ (SỐ GIẢ ĐỊNH — nhóm phải thay bằng lịch thi thật của trường):
  3 đợt thi/năm × 5 ngày/đợt = 15 ngày có thi
  → Trần lý thuyết của riêng sản phẩm "thuê theo ca thi" = 15/365 = 4,1%
```

> 🔴 **ĐÂY LÀ CON SỐ QUAN TRỌNG NHẤT CỦA CẢ PROPOSAL, VÀ NÓ RẤT XẤU.**
> Nó chứng minh bằng số học rằng **sản phẩm "thuê theo ca thi" MỘT MÌNH không thể nuôi nổi đội máy** — trùng khớp chính xác với kết luận đã có ở file `02` (*"mô hình 'thuê theo ngày đi thi' một mình KHÔNG đủ để hoàn vốn máy"*) và file `11` (*"gói tháng làm nền tảng doanh thu, gói ngày/ca thi làm biên lợi nhuận cao trong mùa thi"*).
> **Cách trình bày ăn điểm:** đừng giấu con số này. Đưa nó lên slide, rồi trình bày **danh mục sản phẩm 3 tầng** (thuê tháng nền tảng + thuê tuần đồ án + thuê ca thi biên cao) như là **lời giải** cho chính con số đó. Người chấm sẽ đánh giá cao việc nhóm tự tìm ra và tự giải được điểm yếu chí mạng của mô hình.

## 6.3. Turnaround Time (TAT) — thời gian quay vòng

### Định nghĩa 🔵 [TT]

```
TAT =  Thời điểm máy được đánh dấu "Sẵn sàng" trở lại
     − Thời điểm máy được khách trả về
```

**Phân rã TAT thành 5 cấu phần để biết phải cải thiện chỗ nào:**

| Cấu phần | Mô tả | Mục tiêu 🔵 [TT] |
|---|---|---|
| T1 — Chờ tiếp nhận | Máy đã trả nhưng chưa ai kiểm | ≤ 15 phút (trong giờ trực) |
| T2 — Kiểm tra & chấm hạng | Bước 1–4 của §4.4 | ≤ 7 phút |
| T3 — Khôi phục & kiểm thử | Bước 5–7 | ≤ 10 phút (L1) / ≤ 25 phút (L2) |
| T4 — **Sạc pin** | Từ mức trả về lên ≥95% | **30–90 phút** ← nút thắt |
| T5 — Vệ sinh, chụp ảnh, cập nhật hệ thống | Bước 8–11 | ≤ 8 phút |
| **TAT mục tiêu (L1)** | | **≤ 90 phút** |
| **TAT mục tiêu (L2)** | | **≤ 3 giờ** |

### Neo tham chiếu quốc tế 🟢 [XM]

> file `02`: **Rent the Runway** hướng tới **"zero-day turnaround"** — *món đồ về là đi tiếp trong ngày* — và duy trì **throughput dưới 1 tuần**, nhờ thu thập dữ liệu về thuộc tính vật lý của tài sản (đang ở đâu, có hỏng không, đang trong vòng quay không). Nguồn: [Harvard d3 — Rent the Runway Digitizes High-Fashion](https://d3.harvard.edu/platform-rctom/submission/rent-the-runway-digitizes-high-fashion/)
> file `02` cũng ghi: chi phí fulfillment của RTR chiếm **27,8% doanh thu (Q2/2025)** — *"gần một phần ba doanh thu bị 'ăn' bởi khâu giặt/kiểm/gửi"*.

🔵 [TT] **Bài học chuyển giao:** TAT không phải chỉ số kỹ thuật, nó là **chỉ số tài chính**. Mỗi giờ TAT là một giờ máy không sinh tiền. Với mô hình thi cử, TAT quan trọng gấp bội vì **toàn bộ nhu cầu dồn vào vài ngày** — một máy quay vòng được 2 ca/ngày thay vì 1 ca/ngày **nhân đôi công suất mà không cần mua thêm máy**.

**→ Gợi ý chiến lược 🔵 [TT]:** vì T4 (sạc pin) là nút thắt duy nhất không rút ngắn được bằng nhân lực, hãy **mua thêm củ sạc rời và pin dự phòng thay vì mua thêm máy** khi cần tăng công suất — chi phí thấp hơn nhiều lần.

## 6.4. Shrinkage / Loss Rate — tỷ lệ thất thoát

### 🔴 Không có số liệu ngành đáng tin

🟢 [XM] file `08` §8.4 đã thừa nhận thẳng: *"**KHÔNG CÓ SỐ LIỆU XÁC MINH**"* về tỷ lệ hư hỏng, và liệt kê sẵn các từ khoá cần tra: `equipment rental loss rate shrinkage percentage`, `tool rental industry loss ratio`.
🟢 [XM] file `02` §17: *"**Tỷ lệ hư hỏng (damage rate) của Grover: KHÔNG tìm được.** Grover không công bố... Mọi con số về tỷ lệ hư hỏng trong proposal phải ghi rõ là **giả định của nhóm**."*
🟢 [XM] file `10` §2.6: bài Code4Lib về chương trình cho mượn laptop của Đại học Arizona — *"**KHÔNG tìm thấy trong snippet: tỉ lệ mất máy / không trả máy. Cần mở bài đọc để lấy.**"* → 🔑 **Đây là việc dễ nhất và có giá trị cao nhất còn tồn đọng**: bài ở [journal.code4lib.org/articles/5876](https://journal.code4lib.org/articles/5876) là **truy cập mở, miễn phí**, nhóm chỉ cần mở đọc.

### 🟡 [KT-MH] Mốc tham chiếu từ ngành khác — dùng làm cận dưới, KHÔNG dùng làm dự báo

| Ngành | Chỉ số | Khoảng hay được nhắc | Cách tra nguồn thật |
|---|---|---|---|
| Bán lẻ (Mỹ) | "Shrink" = thất thoát tính trên doanh thu | ~1,4–1,6% doanh thu | `NRF National Retail Security Survey shrink rate` |
| Cho thuê thiết bị | "LDS" = Lost, Damaged & Stolen | 🔴 Không nhớ được con số đáng tin | `ARA Rental Market Monitor lost damaged stolen`, `equipment rental LDS percentage of fleet` |

> 🔴 **Tại sao không được áp shrink bán lẻ vào đây:** shrink bán lẻ tính trên **doanh thu**; thất thoát cho thuê phải tính trên **giá trị tài sản (OEC)** — hai mẫu số khác nhau hoàn toàn. Một đội máy 186 triệu tạo doanh thu 74 triệu/năm: mất 1 máy = 0,6% OEC nhưng = **8,3% doanh thu**. **Luôn ghi rõ mẫu số.**

### 🔵 [TT] Bộ công thức nhóm phải tự đo (đây mới là câu trả lời đúng)

```
(1) Tỷ lệ KHÔNG TRẢ (non-return rate)
    = Số lượt bị chuyển trạng thái "mất" ÷ Tổng số lượt thuê × 100

(2) Tỷ lệ hư hỏng có tính phí (chargeable damage rate)
    = Số lượt phát sinh hư hỏng phải tính tiền ÷ Tổng số lượt × 100

(3) Thất thoát theo GIÁ TRỊ TÀI SẢN
    = (Giá trị máy mất + Chi phí sửa chữa trong kỳ) ÷ OEC × 100

(4) Thất thoát theo DOANH THU
    = (Giá trị máy mất + Chi phí sửa chữa) ÷ Doanh thu thuê × 100

(5) Tỷ lệ trả trễ
    = Số lượt trả sau giờ cam kết ÷ Tổng số lượt × 100

(6) Trễ trung bình (chỉ tính các lượt bị trễ), đơn vị: PHÚT
```

**Quy tắc khai báo trong proposal 🔵 [TT]:** ghi nguyên văn *"Chúng tôi chưa có dữ liệu vận hành. Các tỷ lệ dưới đây là **giả định phục vụ mô hình tài chính**, kèm phân tích độ nhạy 3 kịch bản; sau 1 học kỳ vận hành sẽ thay bằng số thật."* — file `08` đã dựng sẵn 3 kịch bản độ nhạy để nhóm dùng lại.

## 6.5. 🔵 [TT] BẢNG ĐIỀU KHIỂN KPI — 12 chỉ số, có ngưỡng đèn giao thông

Đây là bảng nhóm in ra dán tường và cập nhật hằng tuần.

| # | Chỉ số | Công thức | Tần suất | 🟢 Tốt | 🟡 Cảnh báo | 🔴 Hành động ngay |
|---|---|---|---|---|---|---|
| 1 | **Time utilization** | ngày-máy thuê ÷ ngày-máy khả dụng | Tuần | ≥ 40% | 25–39% | < 25% |
| 2 | **Dollar utilization** | DT thuê 12T ÷ OEC | Quý | ≥ 50% | 30–49% | < 30% |
| 3 | **Availability** | ngày-máy sẵn sàng ÷ ngày-máy sở hữu | Tuần | ≥ 95% | 90–94% | < 90% |
| 4 | **Lượt thuê/máy/tháng** | tổng lượt ÷ số máy | Tháng | ≥ 4 | 2–3 | < 2 |
| 5 | **TAT trung bình (L1)** | trung bình thời gian quay vòng | Tuần | ≤ 90' | 91–150' | > 150' |
| 6 | **Tỷ lệ trả trễ** | lượt trễ ÷ tổng lượt | Tuần | ≤ 5% | 6–12% | > 12% |
| 7 | **Tỷ lệ không trả** | lượt "mất" ÷ tổng lượt | Tháng | 0% | > 0% | ≥ 2 vụ/học kỳ |
| 8 | **Tỷ lệ hư hỏng tính phí** | lượt hư hỏng ÷ tổng lượt | Tháng | ≤ 3% | 4–8% | > 8% |
| 9 | 🔴 **Tỷ lệ sự cố NGÀY THI** | ca thi có sự cố ÷ tổng ca thi phục vụ | **Mỗi đợt thi** | **0%** | ≥ 1 vụ | ≥ 2 vụ |
| 10 | **Đạt SLA đổi máy** | lần đổi đúng hạn ÷ tổng lần đổi | Mỗi đợt thi | 100% | 90–99% | < 90% |
| 11 | **SoH pin trung bình đội** | trung bình SoH | Quý | ≥ 85% | 75–84% | < 75% |
| 12 | **Tỷ lệ khách quay lại** | khách thuê ≥ 2 lần ÷ tổng khách | Học kỳ | ≥ 40% | 20–39% | < 20% |

> 🔑 **Chỉ số #9 phải là chỉ số Bắc Đẩu về chất lượng, và ngưỡng của nó là 0%.** Lý do 🔵 [TT]: sản phẩm nhóm bán không phải "một cái laptop" mà là **"chắc chắn vào thi được"** (🟢 [XM] định vị đã chốt ở file `01`: *"Không cho thuê laptop. Cho thuê một ca thi an toàn."*). Một sự cố ngày thi phá huỷ toàn bộ lời hứa đó — và trong một cộng đồng khép kín cỡ một campus, tin xấu lan nhanh hơn mọi hoạt động marketing.

---

# 7. BUFFER STOCK / HOT SPARE — ĐỂ BAO NHIÊU MÁY DỰ PHÒNG?

## 7.1. Ba khái niệm khác nhau, đừng gộp

🟡 [KT-MH] + 🔵 [TT]

| Khái niệm | Định nghĩa | Trong dự án này là gì |
|---|---|---|
| **Buffer / Safety stock** (tồn kho an toàn) | Máy giữ lại để hấp thụ **biến động NHU CẦU** (hôm nay đông hơn dự báo) | Máy chưa bán hết công suất trong tuần thi |
| **Hot spare** (dự phòng nóng) | Máy **đã sạc đầy, đã kiểm thử, đặt sẵn tại điểm trực**, giao được trong vài phút | Máy để trong balo trực tại sảnh toà nhà, mở nắp là chạy |
| **Cold spare** (dự phòng nguội) | Máy có trong kho nhưng **chưa chuẩn bị** — cần 40–90 phút mới giao được | Máy ở nhà trọ/kho |

> 🔴 **Sai lầm chết người:** đếm cold spare vào năng lực ứng cứu ngày thi. Máy cách 20 phút đi xe + 40 phút chuẩn bị = **60 phút** → khách đã thi xong hoặc đã trượt. **Chỉ hot spare mới cứu được ca thi.**

## 7.2. 🔵 [TT] Tính đúng số hot spare bằng phân phối nhị thức

**Bài toán:** có `n` máy đang trên tay khách trong một ngày thi; mỗi máy có xác suất `p` gặp sự cố cần thay trong ngày đó. Cần bao nhiêu hot spare để **xác suất thiếu máy dự phòng < 5%**?

**Công thức:** số máy hỏng `X ~ B(n, p)`. Cần `k` spare sao cho `P(X > k) < 5%`.

### Bảng kết quả (người nghiên cứu tự tính)

**Kịch bản A — tỷ lệ sự cố/ngày p = 2%** (máy được chuẩn bị tốt, đội trẻ, ít di chuyển)

| Số máy đang cho thuê (n) | P(≥1 hỏng) | P(≥2) | P(≥3) | P(≥4) | **Số hot spare cần** |
|---|---|---|---|---|---|
| 10 | 18,3% | 1,6% | 0,1% | — | **1** (rủi ro còn 1,6%) |
| 20 | 33,2% | 6,0% | 0,7% | 0,1% | **2** (rủi ro còn 0,7%) |
| 30 | 45,5% | 12,1% | 2,2% | 0,3% | **2** (rủi ro còn 2,2%) |
| 40 | 55,4% | 19,0% | 4,6% | 0,8% | **2** (4,6%) hoặc **3** (0,8%) |

**Kịch bản B — tỷ lệ sự cố/ngày p = 5%** (máy cũ hơn, pin yếu, hoặc mùa mưa Đà Nẵng)

| Số máy đang cho thuê (n) | P(≥1) | P(≥2) | P(≥3) | P(≥4) | P(≥5) | **Số hot spare cần** |
|---|---|---|---|---|---|---|
| 20 | 64,2% | 26,4% | 7,5% | 1,6% | — | **3** (rủi ro 1,6%) |
| 30 | 78,5% | 44,6% | 18,8% | 6,1% | 1,6% | **4** (rủi ro 1,6%) |
| 40 | 87,1% | 60,1% | 32,3% | 13,8% | 4,8% | **4** (4,8%) hoặc **5** (1,4%) |

> **Giả định phải nói rõ khi trình bày:** (i) các máy hỏng **độc lập** với nhau — không đúng nếu tất cả cùng dùng một bản image lỗi hoặc cùng một lô pin xấu (**rủi ro lỗi hệ thống**, xem dưới); (ii) `p` là **giả định của người nghiên cứu, KHÔNG CÓ NGUỒN** — file `08` đã xác nhận không tìm được tỷ lệ hư hỏng ngành; (iii) tính theo một ngày thi.

### 🔴 Rủi ro lỗi hệ thống — thứ mà phép tính trên KHÔNG bắt được

🔵 [TT] Nếu bản Golden Image có lỗi (ví dụ bản SEB sai phiên bản so với bản trường vừa cập nhật), thì **KHÔNG phải 2% máy hỏng — mà là 100% máy hỏng cùng lúc**, và hot spare cũng hỏng y hệt vì dùng chung image.

**Ba biện pháp chặn 🔵 [TT]:**
1. **Kiểm thử đầu ngày (smoke test):** trước giờ thi đầu tiên mỗi đợt, chạy EOS+SEB trên **2 máy ngẫu nhiên** — phát hiện lỗi hệ thống trước khi nó lan ra 30 khách.
2. **Giữ 1–2 hot spare dùng bản image PHIÊN BẢN TRƯỚC** (n−1). Nếu bản mới lỗi, vẫn còn đường lui.
3. **Theo dõi thông báo của Phòng Khảo thí/IT về cập nhật EOS/SEB**, và có quy trình cập nhật khẩn cấp trong 24 giờ.

## 7.3. 🔵 [TT] KHUYẾN NGHỊ CHỐT — quy tắc để đưa vào proposal

| Quy mô đội | Máy cho thuê tối đa cùng lúc | **Hot spare tại điểm trực** | **Cold spare ở kho** | Tổng máy cần sở hữu |
|---|---|---|---|---|
| **15 máy** | 12 | **2** | 1 | 15 |
| **25 máy** | 21 | **3** | 1 | 25 |
| **30 máy** | 25 | **3** | 2 | 30 |
| **40 máy** | 34 | **4** | 2 | 40 |

**Quy tắc rút gọn để nhớ và để nói trên slide:**
> **"Hot spare ≈ 10% số máy đang cho thuê, tối thiểu 2 máy. Cộng thêm 1 máy chạy bản image phiên bản trước."**

**Đối chiếu với thông lệ 🟡 [KT-MH]:** trong quản trị tài sản CNTT doanh nghiệp, tỷ lệ máy dự phòng cho sửa chữa/thay thế thường được nhắc ở mức **5–10% đội máy đang triển khai**. 🔴 Chưa xác minh — từ khoá tra: `IT asset management spare pool percentage`, `hot spare ratio laptop fleet break fix`.
🔵 [TT] Dự án này nên ở **cận trên hoặc cao hơn** khoảng đó, vì: (a) hậu quả của một lần thiếu máy là **khách trượt môn**, không phải "nhân viên chờ nửa ngày"; (b) nhu cầu **cực kỳ tập trung** — không thể mượn công suất từ ngày khác.

## 7.4. 🔵 [TT] Bố trí hot spare trong ngày thi

| Yếu tố | Khuyến nghị | Lý do |
|---|---|---|
| **Vị trí** | Ngay sảnh toà nhà có phòng thi (🟢 [XM] file `01` gợi ý **sảnh Alpha / Gamma** mùa thi) | Quyết định trực tiếp việc có đạt SLA 15 phút không |
| **Trạng thái** | Pin **100%**, đã bật sẵn, đã đăng nhập tài khoản `THISINH`, **đã chạy thử SEB sáng hôm đó** | Giao là dùng được ngay, không mất 5 phút khởi động |
| **Hạng ngoại hình** | 🔴 **Chỉ dùng máy hạng A hoặc B** | Khách đang hoảng loạn; đưa máy xấu = trải nghiệm tệ nhất có thể |
| **Đi kèm** | Củ sạc, tai nghe, chuột — đóng sẵn thành **"bộ ứng cứu"** trong 1 túi | Không mất thời gian gom đồ |
| **Nhân sự** | ≥ 1 người trực **suốt ca thi**, có số hotline in trên phiếu của mọi khách | Không có người trực = hot spare vô dụng |
| **Ghi nhận** | Mỗi lần đổi máy lập **biên bản đổi máy khẩn** (rút gọn, 1 mặt giấy) | Vẫn phải có bằng chứng, nhưng không được làm chậm |

---
# 8. REVERSE LOGISTICS — THU HỒI MÁY KHI KHÁCH TRẢ TRỄ

## 8.1. Nguyên tắc thiết kế: leo thang theo thời gian, chi phí tăng dần

🔵 [TT]. 95% các vụ trả trễ là **quên**, không phải **chiếm đoạt**. Thiết kế quy trình như đang đối phó với kẻ gian ngay từ phút đầu sẽ **làm mất khách tốt** và tạo tiếng xấu trong cộng đồng sinh viên. Ngược lại, không leo thang thì mất máy. Giải pháp: **thang leo thang có mốc thời gian rõ ràng, mỗi bước tốn kém hơn bước trước**.

### Neo tham chiếu quốc tế 🟢 [XM] — từ file `10-campus-laptop-loan.md`

| Trường | Phí trễ | Mốc coi là "MẤT" | Biện pháp kỹ thuật |
|---|---|---|---|
| **NIU** | 5,00 USD/ngày | **Quá hạn 7 ngày** | — |
| **KU** | 0,10 USD/phút, **trần 30 USD/máy** | — | — |
| **UConn** | 1,00 USD/giờ | Quá hạn > 34 ngày | — |
| **Stanford (The Hub)** | 5,00 USD/ngày | — | 🔑 **KHOÁ MÁY TỪ XA nếu quá hạn 2 ngày làm việc** |
| **MIT Libraries** | **Không thu phí trễ** | 30+ ngày → phí thay thế 135 USD | — |

Bốn nguyên tắc thiết kế đã được kiểm chứng ở nhiều trường (nguyên văn file `10` §2.2):
1. **Phí trễ tính theo GIỜ với hợp đồng ngắn** → dịch vụ thuê máy đi thi (ca thi 1–3 giờ) **phải tính theo giờ**.
2. **Luôn có TRẦN phạt trễ** (KU: trần 30 USD) — tránh phạt vô hạn gây tranh chấp.
3. **Có mốc chuyển trạng thái rõ ràng từ "trễ" sang "mất"**.
4. **Khoá máy từ xa là biện pháp đã được dùng thật** (Stanford: khoá sau 2 ngày làm việc).

## 8.2. 🔵 [TT] THANG LEO THANG 7 BƯỚC — bảng vận hành chi tiết

| Mốc | Bước | Hành động | Kênh | Ai làm | Bằng chứng phải lưu | Chi phí |
|---|---|---|---|---|---|---|
| **T−2 giờ** | 0 | **Nhắc trước hạn**: *"Bạn nhớ trả máy lúc __h nhé. Trả đúng giờ để hoàn cọc 100%."* | Zalo tự động | Hệ thống | Ảnh chụp tin nhắn / log | ~0 |
| **T+0** | 1 | Nhắc đến hạn, **nêu rõ mức phí trễ/giờ** | Zalo + SMS | Hệ thống | Log | ~0 |
| **T+2 giờ** | 2 | **Gọi điện thoại**. Hỏi lý do, **đề nghị gia hạn có phí** (biến vấn đề thành doanh thu) | Điện thoại | Trực ca | Ghi nhật ký: giờ gọi, nội dung, cam kết của khách | ~0 |
| **T+24 giờ** | 3 | **Gọi + nhắn cho người bảo lãnh** (nếu có). Gửi **thông báo vi phạm hợp đồng lần 1** qua **email trường**, nêu: số tiền nợ, hạn chót, hậu quả tiếp theo | Điện thoại + email | Trưởng nhóm | 🔑 **Email gửi từ hộp thư có lưu, KHÔNG xoá** | ~0 |
| **T+48 giờ** | 4 | 🔑 **KHOÁ MÁY TỪ XA** (nếu đã triển khai), gửi thông báo trước khi khoá | Kỹ thuật | Kỹ thuật | Ảnh màn hình lệnh khoá + giờ thực hiện | ~0 |
| **T+3 ngày** | 5 | **VĂN BẢN YÊU CẦU TRẢ LẠI TÀI SẢN** (BM-05) — gửi theo **cách có dấu vết**: email trường + Zalo + **thư bảo đảm qua bưu điện** đến địa chỉ đã khai | Văn bản | Trưởng nhóm | 🔑 **Giữ biên lai bưu điện** — đây là chứng cứ mạnh nhất cho mọi bước sau | ~30.000–50.000 VND 🔴 [KTĐ] |
| **T+5 ngày** | 6 | **Liên hệ nhà trường** (Phòng CTSV) — 🔴 chỉ khi hợp đồng có điều khoản khách **đồng ý trước** cho việc này. Nội dung **chỉ nêu sự kiện, không quy kết tội** | Chính thức | Trưởng nhóm | Bản sao công văn | ~0 |
| **T+7 ngày** | 7 | 🔴 **CHUYỂN TRẠNG THÁI "MẤT MÁY"** → trừ cọc, tính giá trị thay thế, và **khởi động quy trình pháp lý §8.4** | — | Trưởng nhóm | Hồ sơ đầy đủ | xem §8.4 |

> 🔵 [TT] **Vì sao chọn mốc T+7 ngày:** trùng với NIU (7 ngày) 🟢 [XM], và ngắn hơn nhiều so với MIT (30 ngày) / UConn (34 ngày) — hợp lý vì **vòng quay của dự án tính bằng giờ, không phải bằng học kỳ**; file `10` §9.1 cũng khuyến nghị *"đề xuất X = 3–7 ngày, ngắn vì vòng quay ngắn"*.

### Biểu phí trễ đề xuất (🔵 [TT], theo nguyên tắc đã kiểm chứng)

| Khoản | Mức đề xuất | Căn cứ |
|---|---|---|
| Phí trễ theo giờ | **20–30% giá thuê ngày, mỗi giờ bắt đầu** | KU/UConn tính theo giờ/phút cho hợp đồng ngắn 🟢 [XM] |
| **Trần phí trễ/ngày** | **150% giá thuê ngày** | 🟢 [XM] file `08` §10.3 đề xuất phí quá hạn 150% giá thuê ngày; KU có trần 🟢 [XM] |
| **Trần phí trễ tổng cộng** | **= tiền cọc** | 🔵 [TT] — vượt quá thì chuyển sang xử lý "mất máy", tránh tranh chấp vô tận |
| Miễn trễ lần đầu | **Ân hạn 30 phút, miễn phí, 1 lần/khách** | 🔵 [TT] — thiện chí, giữ khách tốt; MIT chọn hướng "không phạt trễ" 🟢 [XM] |

## 8.3. Biện pháp kỹ thuật hỗ trợ thu hồi

🟢 [XM] file `08` §9.3 đã liệt kê, trích lại nguyên vẹn và bổ sung đánh giá:

| Biện pháp | Hiệu quả (theo file 08) | Ghi chú bổ sung 🔵 [TT] |
|---|---|---|
| **Windows Find My Device** | Trung bình — hỗ trợ thu hồi | Miễn phí, nhưng cần máy online và đã bật trước |
| **Prey Project** (miễn phí tới 3 thiết bị) | Trung bình | 🔴 Với 15–40 máy phải trả phí — 🔴 [KTĐ] xin báo giá |
| **Ghi Serial/Service Tag + tem niêm phong có số** | **Cao — chống tráo máy, hỗ trợ trình báo công an** | 🔑 Bắt buộc, chi phí gần 0 |
| **BitLocker** | Bảo vệ dữ liệu, **không chống mất máy** | Đúng — đừng nhầm hai mục tiêu |
| **Hạn mức 1 máy/khách/lượt** | Chặn rủi ro mất nhiều máy cùng lúc | 🔑 Quy tắc cứng, không ngoại lệ |
| **Khoá máy từ xa** | — | 🟢 [XM] Stanford dùng thật (khoá sau 2 ngày làm việc). 🔴 Nhóm cần tra cách làm miễn phí: `Windows remote lock Find My Device`, `Intune remote lock free alternative` |

> ⚠️ 🔵 [TT] **Cảnh báo pháp lý về khoá máy từ xa:** phải có **điều khoản trong hợp đồng** nêu rõ bên cho thuê có quyền vô hiệu hoá thiết bị khi khách vi phạm nghĩa vụ trả, **và phải thông báo trước khi khoá**. Khoá máy mà không có điều khoản → có thể bị coi là hành vi gây thiệt hại. 🔴 Cần hỏi giảng viên Luật.

---

## 8.4. 🔴🔴 VIỆT NAM — TRÌNH TỰ ĐÒI TÀI SẢN HỢP PHÁP

> # ⚠️ CẢNH BÁO ĐỎ — ĐỌC TRƯỚC KHI DÙNG BẤT KỲ CHỮ NÀO Ở MỤC 8.4
>
> **Toàn bộ mục 8.4 là 🟡 [KT-MH] — kiến thức nội tại của mô hình, KHÔNG được xác minh bằng bất kỳ nguồn nào trong phiên này.**
>
> **Số điều luật, ngưỡng giá trị, thời hạn, tên cơ quan có thẩm quyền là những thứ DỄ SAI NHẤT và HẬU QUẢ NẶNG NHẤT.** Việt Nam vừa trải qua **cải cách hành chính và tư pháp lớn trong năm 2025** (xem cảnh báo 8.4.0) khiến nhiều thông tin trước 2025 **không còn đúng**.
>
> **BẮT BUỘC:** nhóm phải tra lại **từng dòng** trên [thuvienphapluat.vn](https://thuvienphapluat.vn) (URL này lấy từ file `08` 🟢 [XM]) và **nhờ giảng viên môn Luật rà soát** trước khi đưa vào bài nộp.
>
> Mục này viết ra để nhóm **biết phải tra cái gì**, không phải để chép thẳng.

### 8.4.0. 🔴 BỐN THAY ĐỔI THỂ CHẾ 2025 CÓ THỂ LÀM SAI MỌI TÀI LIỆU CŨ

🟡 [KT-MH] — bốn điểm dưới đây là **thay đổi lớn**, nếu nhóm tra tài liệu cũ (2020–2024) trên mạng sẽ ra thông tin **lỗi thời**. **Phải kiểm chứng trạng thái thực tế tại 09/2026.**

| # | Thay đổi | Ảnh hưởng trực tiếp đến dự án | Từ khoá tra |
|---|---|---|---|
| 1 | **Bỏ cấp huyện, chuyển sang chính quyền địa phương 2 cấp (tỉnh/thành — xã/phường)** từ giữa 2025 | Địa chỉ hành chính của trường: **"Ngũ Hành Sơn"** có thể **không còn là đơn vị hành chính**; chỉ còn **phường Hoà Hải, TP Đà Nẵng** | `chính quyền địa phương 2 cấp 2025 bỏ cấp huyện`, `phường Hoà Hải Đà Nẵng sau sáp nhập` |
| 2 | **Sáp nhập tỉnh: Đà Nẵng + Quảng Nam** | Tên cơ quan, thẩm quyền địa bàn thay đổi | `sáp nhập Đà Nẵng Quảng Nam 2025` |
| 3 | 🔑 **Không còn Công an cấp huyện/quận** — chuyển nhiệm vụ về **Công an xã/phường** và **Công an tỉnh/thành phố** | 🔴 **Nơi nộp đơn trình báo thay đổi.** Mọi hướng dẫn cũ ghi "nộp cho Công an quận" đều **có thể sai** | `bỏ công an cấp huyện 2025`, `thẩm quyền tiếp nhận tố giác công an xã phường` |
| 4 | **Tổ chức lại hệ thống Toà án — xuất hiện "Toà án nhân dân khu vực"** thay cho TAND cấp huyện | 🔴 **Nơi nộp đơn khởi kiện dân sự thay đổi** | `Toà án nhân dân khu vực 2025 thay toà án cấp huyện` |

> 🔵 [TT] **Cách xử lý thực dụng cho nhóm:** **gọi điện hoặc đến trực tiếp Công an phường Hoà Hải hỏi** *"Nếu cháu cho thuê laptop mà khách không trả, cháu nộp đơn ở đâu, cần giấy tờ gì?"*. **Một buổi đi hỏi trực tiếp có giá trị hơn 10 giờ tra mạng**, và **là dữ liệu sơ cấp — điểm cộng lớn trong bài proposal khởi nghiệp.**

### 8.4.1. Sơ đồ tổng thể — 3 con đường

```
                    KHÁCH KHÔNG TRẢ MÁY
                            │
              ┌─────────────┴─────────────┐
              │                           │
        Còn liên lạc được          MẤT LIÊN LẠC / BỎ TRỐN
        (chỉ là chây ì)                   │
              │                           │
              ▼                           ▼
   ┌──────────────────────┐    ┌──────────────────────────────┐
   │ ĐƯỜNG 1: THƯƠNG LƯỢNG│    │ ĐƯỜNG 3: TỐ GIÁC HÌNH SỰ     │
   │ • Nhắc nợ có bằng    │    │ • Nộp đơn tố giác tội phạm   │
   │   chứng              │    │ • Cơ quan Công an xác minh   │
   │ • Văn bản yêu cầu    │    │ • Dấu hiệu có thể liên quan: │
   │ • Hoà giải cơ sở     │    │   - Lạm dụng tín nhiệm       │
   │ Chi phí: gần 0       │    │     chiếm đoạt tài sản       │
   │ Thời gian: ngày–tuần │    │   - Lừa đảo chiếm đoạt TS    │
   └──────────┬───────────┘    │   - Chiếm giữ trái phép TS   │
              │ thất bại       │ Chi phí: 0 (không án phí)    │
              ▼                │ Thời gian: tháng             │
   ┌──────────────────────┐    └──────────────────────────────┘
   │ ĐƯỜNG 2: KHỞI KIỆN   │
   │        DÂN SỰ        │      ⚠ ĐƯỜNG 1 LÀ ĐIỀU KIỆN CẦN
   │ • Toà án nơi bị đơn  │      cho cả Đường 2 và Đường 3:
   │   cư trú             │      không có bằng chứng đã đòi
   │ • Phải nộp tạm ứng   │      mà khách vẫn không trả, thì
   │   án phí             │      rất khó chứng minh yếu tố
   │ Thời gian: nhiều     │      "cố tình không trả".
   │   tháng              │
   └──────────────────────┘
```

### 8.4.2. ĐƯỜNG 1 — Nhắc nợ và văn bản yêu cầu (bước bắt buộc, không được bỏ)

🔵 [TT] — **đây là bước quan trọng nhất về mặt chứng cứ**, và là bước duy nhất hoàn toàn nằm trong tầm kiểm soát của nhóm.

| Bước | Việc làm | Mục đích pháp lý | Bằng chứng tạo ra |
|---|---|---|---|
| 1.1 | Nhắn Zalo + gọi điện (đã làm ở §8.2 bước 1–3) | Chứng minh **đã yêu cầu** | Ảnh chụp tin nhắn có hiển thị ngày giờ; nhật ký cuộc gọi |
| 1.2 | Gửi **email từ hộp thư có thể truy xuất** tới email trường của khách | Chứng minh đã yêu cầu bằng văn bản | Email đã gửi (**không xoá**), có thể in ra kèm tiêu đề kỹ thuật |
| 1.3 | 🔑 **Gửi VĂN BẢN YÊU CẦU TRẢ LẠI TÀI SẢN (BM-05) bằng thư bảo đảm qua bưu điện** tới địa chỉ khách đã khai | 🔑 **Chứng cứ mạnh nhất.** Chứng minh: (a) đã yêu cầu chính thức, (b) đã ấn định thời hạn, (c) khách biết hoặc buộc phải biết | **Biên lai gửi + vận đơn + (nếu có) hồi báo** |
| 1.4 | Đề nghị **hoà giải ở cơ sở** qua tổ hoà giải của phường/khu dân cư | Miễn phí, nhanh, giữ quan hệ | Biên bản hoà giải (nếu tổ hoà giải lập) |

> 🟡 [KT-MH] Văn bản cần tra để viết đúng thuật ngữ: **Luật Hoà giải ở cơ sở 2013** (hoà giải qua tổ hoà giải thôn/tổ dân phố) và **Luật Hoà giải, đối thoại tại Toà án 2020** (hoà giải miễn phí tại Toà trước khi thụ lý vụ án). Từ khoá tra: `Luật Hoà giải ở cơ sở 2013`, `hoà giải đối thoại tại toà án miễn phí`.

### 8.4.3. ĐƯỜNG 2 — Khởi kiện dân sự

🟡 [KT-MH] **toàn bộ**. Bảng dưới là **danh sách việc cần tra**, không phải kết luận pháp lý.

| Nội dung | Thông tin theo 🟡 [KT-MH] | 🔴 Phải tra lại |
|---|---|---|
| **Loại tranh chấp** | Tranh chấp hợp đồng thuê tài sản / đòi lại tài sản | `tranh chấp hợp đồng thuê tài sản khởi kiện` |
| **Căn cứ nội dung** | **BLDS 2015** — chương hợp đồng thuê tài sản. 🟡 Mô hình cho rằng khoảng **Điều 472–493**, trong đó **Đ.479 (bảo quản tài sản thuê)** và **Đ.482 (trả lại tài sản thuê)**. 🔴 **Mâu thuẫn với file `01` (ghi Đ.554, 557)** | `Bộ luật Dân sự 2015 điều 472 hợp đồng thuê tài sản`, `điều 482 trả lại tài sản thuê` |
| **Nơi nộp đơn** | Toà án nơi **bị đơn cư trú/làm việc** | 🔴 **Tên cấp toà đã đổi năm 2025** — tra `Toà án nhân dân khu vực thẩm quyền dân sự` |
| **Hồ sơ khởi kiện** | Đơn khởi kiện; hợp đồng thuê + biên bản bàn giao (bản gốc/sao y); ảnh & video; bằng chứng đã yêu cầu trả (mục 8.4.2); giấy tờ tuỳ thân của người khởi kiện; tài liệu xác định nơi cư trú của bị đơn | `hồ sơ khởi kiện tranh chấp hợp đồng gồm những gì` |
| **Án phí** | 🟡 Với tranh chấp **có giá ngạch**, mức thường được nhắc: **giá trị ≤ 6 triệu → 300.000 đồng**; **trên 6 triệu đến 400 triệu → 5% giá trị tranh chấp**. Người khởi kiện nộp **tạm ứng án phí** trước; bên thua kiện chịu án phí | 🔴 **Rất có thể đã thay đổi** — tra `Nghị quyết 326/2016/UBTVQH14 án phí lệ phí toà án` **và** kiểm tra xem có nghị quyết mới thay thế chưa |
| **Thời hiệu khởi kiện** | 🟡 **3 năm** kể từ ngày biết quyền bị xâm phạm (với tranh chấp hợp đồng) | `thời hiệu khởi kiện tranh chấp hợp đồng 3 năm điều 429` |
| **Thủ tục rút gọn** | 🟡 BLTTDS 2015 có **thủ tục rút gọn** cho vụ án đơn giản, chứng cứ rõ ràng, bị đơn có địa chỉ xác định — **có thể phù hợp** với tình huống này | `thủ tục rút gọn bộ luật tố tụng dân sự điều kiện áp dụng` |

> 🔵 [TT] **Đánh giá thực tế — phải nói thẳng trong proposal:**
> Với một chiếc laptop trị giá ~6–12 triệu VND, khởi kiện dân sự là **lựa chọn kém hiệu quả về kinh tế**: tạm ứng án phí + thời gian nhiều tháng + công sức của một nhóm sinh viên. **Giá trị thực của Đường 2 không nằm ở việc thắng kiện, mà ở việc NÓ TỒN TẠI** — được nêu rõ trong hợp đồng và trong văn bản yêu cầu, nó tạo áp lực khiến hầu hết các vụ được giải quyết ở Đường 1.
> → **Chiến lược đúng: đầu tư vào PHÒNG NGỪA (sàng lọc, cọc, hạn mức 1 máy/khách, biên bản chặt) chứ không đầu tư vào năng lực kiện tụng.**

### 8.4.4. ĐƯỜNG 3 — Tố giác tội phạm (trình báo công an)

> 🔴🔴 **CẢNH BÁO ĐẶC BIỆT NGHIÊM TRỌNG:** phần này liên quan đến việc **cáo buộc một người phạm tội**. Trình báo sai sự thật, hoặc dùng việc doạ trình báo để ép người khác trả tiền, **có thể khiến chính nhóm vi phạm pháp luật**. Mọi nội dung dưới đây là 🟡 [KT-MH] và **PHẢI được luật sư/giảng viên Luật xác nhận trước khi sử dụng thật**.

#### (a) Các tội danh có thể liên quan — 🟡 [KT-MH], **phải tra lại từng điều**

| Tội danh 🟡 | Điều 🟡 | Dấu hiệu đặc trưng 🟡 | Ngưỡng giá trị hay được nhắc 🟡 | Liên quan thế nào đến dự án |
|---|---|---|---|---|
| **Lạm dụng tín nhiệm chiếm đoạt tài sản** | 🟡 Điều **175** BLHS 2015 (sửa đổi 2017) | 🔑 **Nhận tài sản một cách HỢP PHÁP (qua hợp đồng vay/mượn/THUÊ) rồi**: dùng thủ đoạn gian dối hoặc **bỏ trốn** để chiếm đoạt; **hoặc đến hạn trả mà CÓ ĐIỀU KIỆN, KHẢ NĂNG nhưng CỐ TÌNH KHÔNG TRẢ**; hoặc dùng tài sản vào mục đích bất hợp pháp dẫn đến mất khả năng trả | 🟡 Từ **4.000.000 đồng** trở lên (hoặc dưới mức đó nhưng thuộc trường hợp đặc biệt như đã bị xử phạt hành chính, đã có án tích…) | 🔑 **Đây là điều khoản khớp nhất với mô hình cho thuê** — từ "**thuê tài sản**" được nhắc trực tiếp trong cấu thành |
| **Lừa đảo chiếm đoạt tài sản** | 🟡 Điều **174** | **Thủ đoạn gian dối có TỪ ĐẦU** (dùng giấy tờ giả, thông tin giả để lấy được máy) | 🟡 Từ **2.000.000 đồng** trở lên (hoặc dưới mức đó + trường hợp đặc biệt) | Áp dụng khi khách dùng **thẻ SV giả / MSSV của người khác** |
| **Chiếm giữ trái phép tài sản** | 🟡 Điều **176** | Cố tình **không trả lại** tài sản cho chủ sở hữu **sau khi đã có yêu cầu nhận lại** | 🟡 Từ **10.000.000 đồng** trở lên | 🔑 Cho thấy vì sao **BM-05 (văn bản yêu cầu trả lại)** là bắt buộc — nó tạo ra chính cái "**yêu cầu nhận lại**" mà cấu thành đòi hỏi |

> 🔑 🔵 [TT] **Ba hệ quả thực tiễn cực kỳ quan trọng rút ra từ bảng trên:**
> 1. **Giá trị máy quyết định có ngưỡng hình sự hay không.** Ngưỡng được nhắc tới trải từ 2 đến 10 triệu đồng. Một chiếc laptop cũ 6,2 triệu (giá tham chiếu ở file `11` 🟢 [XM]) nằm **ngay vùng ranh giới**. → 🔵 [TT] **Gợi ý vận hành:** ghi **giá trị thay thế của máy trong biên bản bàn giao** (đã có ở BM-01), và với máy giá trị thấp, cân nhắc **cho thuê kèm phụ kiện để tổng giá trị tài sản giao cao hơn** — nhưng 🔴 **phải hỏi luật sư xem cách tính giá trị tài sản bị chiếm đoạt là theo từng món hay tổng lô.**
> 2. **"Bỏ trốn" và "cố tình không trả dù có điều kiện" là hai yếu tố phải CHỨNG MINH.** Chính vì thế thang leo thang §8.2 mới quan trọng: mỗi tin nhắn không hồi đáp, mỗi cuộc gọi không nghe, mỗi thư bảo đảm bị trả lại **đều là chứng cứ** cho yếu tố này.
> 3. **Không có hợp đồng và biên bản = không có "nhận tài sản qua hợp đồng" = rất khó xác định tội danh.** Đây là lập luận mạnh nhất để thuyết phục nhóm đầu tư công sức vào BM-01.

#### (b) 🔴 BA ĐIỀU TUYỆT ĐỐI KHÔNG ĐƯỢC LÀM

🔵 [TT] + 🟡 [KT-MH] — mỗi hành vi dưới đây **biến nạn nhân thành người vi phạm**:

| ❌ Hành vi | Vì sao nguy hiểm 🟡 | Điều luật có thể bị viện dẫn 🟡 |
|---|---|---|
| **Tự ý đến phòng trọ lấy lại máy, giữ đồ của khách, chặn đường đòi** | Tự xử lý tài sản không qua trình tự pháp luật | 🟡 Có thể liên quan **cưỡng đoạt tài sản (Đ.170)**, **xâm phạm chỗ ở**, gây rối trật tự công cộng |
| **Đe doạ "không trả thì tao cho nghỉ học / tao bêu lên mạng"** | Dùng vũ lực tinh thần để ép giao tài sản | 🟡 **Cưỡng đoạt tài sản (Đ.170)** |
| **Đăng ảnh, họ tên, MSSV khách lên Facebook để bêu riếu** | Xâm phạm danh dự, nhân phẩm + dữ liệu cá nhân | 🟡 **Làm nhục người khác (Đ.155)**, **Vu khống (Đ.156)** nếu quy kết sai; xử phạt hành chính về thông tin trên mạng; vi phạm bảo vệ dữ liệu cá nhân |

> 🔴 **Trong một cộng đồng khép kín như một campus đại học, cách xử lý sai còn nguy hiểm hơn số tiền bị mất.** Một bài đăng bêu riếu có thể chấm dứt doanh nghiệp nhanh hơn cả việc mất 5 máy.
> 🔵 [TT] **Đòn bẩy hợp pháp và hiệu quả nhất trong môi trường này không phải là pháp luật hình sự, mà là:** (i) **khoá tài khoản vĩnh viễn** trong hệ thống của nhóm (🟢 [XM] file `02` bài học #9: *"Thư viện ĐH: nợ phí → chặn mượn tiếp… Rẻ, mạnh, hiệu quả trong cộng đồng khép kín"*); (ii) thông báo cho nhà trường **theo đúng điều khoản khách đã ký đồng ý**, chỉ nêu sự kiện; (iii) **người bảo lãnh là sinh viên khác** — áp lực xã hội đồng đẳng.

#### (c) Hồ sơ trình báo cần chuẩn bị — 🔵 [TT] checklist

| # | Tài liệu | Bắt buộc | Ghi chú |
|---|---|---|---|
| 1 | **Đơn trình báo / Đơn tố giác tội phạm** (BM-06) | ✅ | Ký tên, ghi rõ họ tên, không viết ẩn danh nếu muốn được thông báo kết quả |
| 2 | **CCCD của người trình báo** (bản sao + mang bản gốc đối chiếu) | ✅ | |
| 3 | **Hợp đồng thuê + Biên bản bàn giao (BM-01)** có chữ ký khách | ✅ | 🔑 Tài liệu quan trọng nhất |
| 4 | **Toàn bộ ảnh 8 góc + video** lúc giao máy | ✅ | In ra kèm, và lưu USB |
| 5 | **Chứng từ chứng minh quyền sở hữu máy**: hoá đơn mua, giấy bán hàng, ảnh chụp serial | ✅ | 🔴 Rất hay bị thiếu — **phải lưu hoá đơn mua từng máy ngay từ đầu** |
| 6 | **Ảnh chụp toàn bộ tin nhắn, nhật ký cuộc gọi, email** đã nhắc | ✅ | Sắp xếp **theo thứ tự thời gian** |
| 7 | **Văn bản yêu cầu trả lại tài sản (BM-05) + biên lai bưu điện** | ✅ | 🔑 Chứng minh yếu tố "đã có yêu cầu nhận lại" |
| 8 | Bản sao **thẻ sinh viên / ảnh CCCD của khách** đã thu thập lúc giao | ✅ | |
| 9 | **Ảnh chụp người thuê cầm thẻ SV** | ✅ | Định danh người nhận máy |
| 10 | Thông tin nhận dạng máy: **hãng, model, serial, số tem niêm phong, giá trị** | ✅ | Ghi thành 1 trang riêng cho dễ tra |
| 11 | Thông tin người bảo lãnh (nếu có) | ⬜ | |
| 12 | **Bảng thời gian sự việc (timeline)** 1 trang | ⬜ | 🔵 [TT] Không bắt buộc nhưng **giúp cán bộ tiếp nhận rất nhiều** — nên có |

#### (d) Nơi nộp và những gì phải đòi khi nộp

| Nội dung | 🟡 [KT-MH] | 🔴 Phải xác minh |
|---|---|---|
| **Nơi nộp** | Công an **xã/phường nơi xảy ra sự việc** (nơi giao máy) hoặc nơi người bị hại cư trú; hoặc Cơ quan Cảnh sát điều tra Công an **tỉnh/thành phố** | 🔴 **Đã thay đổi năm 2025 do bỏ công an cấp huyện** — gọi hỏi Công an phường Hoà Hải |
| 🔑 **PHẢI ĐÒI: Giấy tiếp nhận tố giác, tin báo về tội phạm** | 🟡 Cơ quan tiếp nhận có nghĩa vụ **lập biên bản tiếp nhận và cấp giấy tiếp nhận**. **Không có giấy này thì coi như chưa nộp** | `giấy tiếp nhận tố giác tin báo về tội phạm điều 146 BLTTHS` |
| **Thời hạn giải quyết** | 🟡 Thường được nhắc: **20 ngày**, vụ phức tạp có thể **gia hạn tới 2 tháng**, trường hợp đặc biệt gia hạn thêm | `thời hạn giải quyết tố giác tin báo tội phạm điều 147 BLTTHS 2015` |
| **Kết quả** | Ra một trong các quyết định: khởi tố vụ án / không khởi tố / tạm đình chỉ. Người tố giác **được thông báo kết quả** | như trên |
| **Chi phí** | 🟡 **Không mất án phí** (khác với kiện dân sự) | — |

---

## 8.5. BM-05 — MẪU VĂN BẢN YÊU CẦU TRẢ LẠI TÀI SẢN

🔵 [TT]. Dùng ở bước 5 của thang leo thang (T+3 ngày). **Gửi đồng thời 3 kênh: email trường + Zalo + thư bảo đảm bưu điện.**

```
════════════════════════════════════════════════════════════════════
              CỘNG HOÀ XÃ HỘI CHỦ NGHĨA VIỆT NAM
                 Độc lập - Tự do - Hạnh phúc
                 ────────────────────────────
                                  Đà Nẵng, ngày ___ tháng ___ năm 20___

              VĂN BẢN YÊU CẦU TRẢ LẠI TÀI SẢN THUÊ
                        (Lần thứ: ____)

Kính gửi: Ông/Bà ______________________________________________
          MSSV: ________________  CCCD: _____________________
          Địa chỉ: ______________________________________________
          Email: _____________________  SĐT: ________________

Tôi tên là: __________________________________________________
Chức vụ: ________________ , đại diện cho: ____________________
Địa chỉ: _____________________________________________________
Điện thoại: __________________  Email: _______________________

              ─── I. CƠ SỞ CỦA YÊU CẦU ───

Ngày ___/___/20___, hai bên đã ký Biên bản bàn giao laptop cho
thuê số RENT-________-____ (đính kèm bản sao). Theo đó:

  • Tài sản bàn giao: laptop hiệu ____________ model ___________
    Số serial/Service Tag: _________________________________
    Số tem niêm phong: ______   Giá trị thay thế: _________ VND
  • Phụ kiện kèm theo: ___________________________________
  • Thời hạn thuê: từ ___h___ ngày ___/___/___
                   đến ___h___ ngày ___/___/___
  • Ông/Bà đã ký xác nhận nhận đủ tài sản nêu trên.

              ─── II. TÌNH TRẠNG HIỆN TẠI ───

Tính đến thời điểm lập văn bản này, đã quá hạn trả tài sản
______ ngày ______ giờ, nhưng Ông/Bà VẪN CHƯA trả lại tài sản.

Chúng tôi đã liên hệ với Ông/Bà qua các hình thức sau:
  1. Tin nhắn Zalo ngày ___/___  lúc ___h___ — ☐ Đã xem ☐ Chưa xem
  2. Gọi điện ngày ___/___ lúc ___h___ — ☐ Không nghe máy ☐ Đã nói chuyện
  3. Email gửi ___/___ tới ____________@fpt.edu.vn
  4. _____________________________________________________

Tổng số tiền phát sinh tính đến nay:
  • Phí thuê:                          ____________ VND
  • Phí trả trễ (____ giờ × ______):   ____________ VND
  • Cộng:                              ____________ VND
  • Trừ tiền cọc đã nhận:            (____________) VND
  • CÒN PHẢI THANH TOÁN:               ____________ VND

              ─── III. YÊU CẦU CỤ THỂ ───

Bằng văn bản này, chúng tôi CHÍNH THỨC YÊU CẦU Ông/Bà:

  1. TRẢ LẠI ngay lập tức toàn bộ tài sản nêu tại Mục I, bao gồm
     đầy đủ phụ kiện, trong tình trạng như khi nhận.
  2. THANH TOÁN số tiền còn phải trả nêu tại Mục II.

  THỜI HẠN CHÓT: trước ____h____ ngày ____/____/20____
  ĐỊA ĐIỂM TRẢ:  _____________________________________________
  LIÊN HỆ:       _____________________________________________

              ─── IV. HẬU QUẢ NẾU KHÔNG THỰC HIỆN ───

Nếu quá thời hạn nêu trên mà Ông/Bà không trả lại tài sản và
không thanh toán, chúng tôi sẽ:
  1. Ghi nhận tài sản vào trạng thái "bị chiếm giữ", ngừng cung
     cấp dịch vụ vĩnh viễn đối với Ông/Bà;
  2. Thực hiện các biện pháp thu hồi theo quy định của pháp luật,
     bao gồm nhưng không giới hạn ở việc đề nghị cơ quan có thẩm
     quyền giải quyết theo trình tự luật định.

Văn bản này được gửi qua: ☐ Thư bảo đảm (mã vận đơn: ___________)
                         ☐ Email  ☐ Zalo  ☐ Trao tay
Chúng tôi mong muốn giải quyết sự việc trên tinh thần thiện chí
và đề nghị Ông/Bà liên hệ ngay để thống nhất phương án.

                              ĐẠI DIỆN BÊN CHO THUÊ
                              (Ký, ghi rõ họ tên)


Tài liệu gửi kèm:
  ☐ Bản sao Biên bản bàn giao số RENT-________-____
  ☐ Ảnh chụp tài sản lúc bàn giao
════════════════════════════════════════════════════════════════════
```

> ⚠️ 🔵 [TT] **Lưu ý soạn thảo quan trọng ở Mục IV:** viết *"thực hiện các biện pháp thu hồi theo quy định của pháp luật"* — **KHÔNG viết** *"sẽ tố cáo bạn tội lạm dụng tín nhiệm chiếm đoạt tài sản"* hay *"sẽ đưa bạn ra công an"*. Lý do: (a) nhóm **không có thẩm quyền** xác định tội danh; (b) nêu đích danh tội danh kèm đòi tiền **có thể bị diễn giải là đe doạ nhằm chiếm đoạt tài sản**. Câu chữ trung tính vẫn tạo đủ áp lực mà **an toàn tuyệt đối cho nhóm**. 🔴 Nhờ giảng viên Luật duyệt câu chữ mục IV.

## 8.6. BM-06 — MẪU ĐƠN TRÌNH BÁO / TỐ GIÁC

> 🟡 [KT-MH] **Về "mẫu đơn chuẩn":** theo hiểu biết của mô hình, **không có một mẫu đơn tố giác bắt buộc duy nhất áp dụng cho công dân** — công dân có thể trình báo bằng đơn tự viết, trình báo trực tiếp (cơ quan lập biên bản), hoặc qua điện thoại. Một số cơ quan có mẫu riêng dán tại trụ sở.
> 🔴 **Nhóm phải hỏi trực tiếp Công an phường Hoà Hải xem có mẫu riêng không** — 5 phút hỏi thay cho hàng giờ tra cứu, và là **dữ liệu sơ cấp cho bài proposal**.

```
════════════════════════════════════════════════════════════════════
              CỘNG HOÀ XÃ HỘI CHỦ NGHĨA VIỆT NAM
                 Độc lập - Tự do - Hạnh phúc
                 ────────────────────────────
                                  Đà Nẵng, ngày ___ tháng ___ năm 20___

                    ĐƠN TRÌNH BÁO
          (Về việc chiếm giữ tài sản cho thuê không trả)

Kính gửi:  - CÔNG AN PHƯỜNG ______________________________
           - (Hoặc cơ quan có thẩm quyền: __________________)
           [🔴 XÁC MINH LẠI TÊN CƠ QUAN CÓ THẨM QUYỀN TRƯỚC KHI NỘP]

I. NGƯỜI TRÌNH BÁO
   Họ và tên: ________________________________________________
   Sinh ngày: ___/___/______   Giới tính: ____________________
   CCCD số: ______________ cấp ngày ___/___/____ tại _________
   Nơi ở hiện tại: ___________________________________________
   Điện thoại: ______________  Email: ________________________
   Tư cách:  ☐ Cá nhân   ☐ Đại diện hộ kinh doanh/tổ chức:
             _____________________________________________

II. NGƯỜI BỊ TRÌNH BÁO
   Họ và tên: ________________________________________________
   MSSV: __________________  Trường: _________________________
   CCCD số (nếu có): _________________________________________
   Địa chỉ đã khai: __________________________________________
   Điện thoại/Zalo: __________  Facebook: ____________________

III. TÀI SẢN LIÊN QUAN
   Loại tài sản: Máy tính xách tay (laptop)
   Hãng/Model: _______________________________________________
   Số serial / Service Tag: __________________________________
   Số tem niêm phong: ________________________________________
   Phụ kiện kèm theo: ________________________________________
   GIÁ TRỊ TÀI SẢN: ________________ VND
   Chứng từ chứng minh quyền sở hữu: _________________________

IV. NỘI DUNG SỰ VIỆC (trình bày theo trình tự thời gian)

   1. Ngày ___/___/20___, tại _______________________________,
      tôi đã cho Ông/Bà ______________________ thuê tài sản nêu
      tại Mục III theo Biên bản bàn giao số RENT-______-____,
      có chữ ký xác nhận của hai bên.

   2. Thời hạn trả tài sản theo thoả thuận là ___h___ ngày
      ___/___/20___.

   3. Đến hạn, Ông/Bà ________________ KHÔNG trả lại tài sản.

   4. Tôi đã liên hệ yêu cầu trả lại tài sản như sau:
      - Ngày ___/___: nhắn tin Zalo — kết quả: ________________
      - Ngày ___/___: gọi điện — kết quả: ____________________
      - Ngày ___/___: gửi email tới _________________________
      - Ngày ___/___: gửi VĂN BẢN YÊU CẦU TRẢ LẠI TÀI SẢN bằng
        thư bảo đảm, mã vận đơn ______________ — kết quả: ____
      - Ngày ___/___: ________________________________________

   5. Đến thời điểm làm đơn này, đã quá hạn ______ ngày, tài sản
      vẫn chưa được trả lại. Tình trạng liên lạc hiện nay:
      ☐ Không nghe máy   ☐ Chặn liên lạc   ☐ Không ở địa chỉ đã khai
      ☐ Có liên lạc nhưng từ chối trả   ☐ Khác: ______________

V. YÊU CẦU

   Tôi đề nghị Quý cơ quan:
   1. Tiếp nhận đơn trình báo và xác minh sự việc nêu trên theo
      thẩm quyền;
   2. Hỗ trợ tôi thu hồi tài sản hợp pháp của mình;
   3. Xử lý theo quy định của pháp luật nếu có dấu hiệu vi phạm.

VI. TÀI LIỆU GỬI KÈM
   ☐ 1. Bản sao CCCD của người trình báo
   ☐ 2. Biên bản bàn giao số RENT-________-____ (bản sao)
   ☐ 3. Ảnh chụp tài sản lúc bàn giao (___ ảnh) + video
   ☐ 4. Chứng từ chứng minh quyền sở hữu tài sản
   ☐ 5. Ảnh chụp tin nhắn, nhật ký cuộc gọi, email (___ trang)
   ☐ 6. Văn bản yêu cầu trả lại tài sản + biên lai bưu điện
   ☐ 7. Ảnh chụp thẻ sinh viên / giấy tờ của người thuê
   ☐ 8. Bảng thời gian sự việc
   ☐ 9. ________________________________________________

Tôi xin cam đoan những nội dung trình bày trên là ĐÚNG SỰ THẬT và
chịu trách nhiệm trước pháp luật về nội dung đã trình bày.

                                    NGƯỜI TRÌNH BÁO
                                    (Ký, ghi rõ họ tên)


────────────────────────────────────────────────────────────────────
🔑 KHI NỘP, PHẢI ĐỀ NGHỊ CƠ QUAN TIẾP NHẬN CẤP
   "GIẤY TIẾP NHẬN TỐ GIÁC, TIN BÁO VỀ TỘI PHẠM"
   (hoặc giấy biên nhận hồ sơ). KHÔNG CÓ GIẤY NÀY = CHƯA CÓ BẰNG
   CHỨNG ĐÃ NỘP. Chụp ảnh giấy ngay tại chỗ.
════════════════════════════════════════════════════════════════════
```

---
# 9. SLA — CAM KẾT MỨC DỊCH VỤ

## 9.1. Mặt bằng SLA thực tế tại Việt Nam (🟢 [XM] — số THẬT, dùng được ngay)

Trích từ file `01-thi-truong-cho-thue-laptop-vn.md` §7, Bảng 6:

| Đơn vị | Cam kết | Nguồn |
|---|---|---|
| **Laptop SGN** (TP.HCM) | ⭐ **Trong vòng 2 GIỜ** kể từ khi xác nhận đơn, nội thành TP.HCM — **SLA nhanh nhất tìm được trên toàn thị trường VN** | [laptopsgn.com](https://laptopsgn.com/tin-tuc/dich-vu-cho-thue-laptop-tphcm-gia-re-giao-2h/) |
| **Trường Giang** (Đà Nẵng) | **Giao hàng trong ngày** tại Đà Nẵng | [truonggiang.vn](https://truonggiang.vn/cho-thue-laptop.html) |
| **MiT Group** | **Giao trong ngày**, kèm lắp đặt và hỗ trợ kỹ thuật | [mitgroup.vn](https://mitgroup.vn/cho-thue-laptop/) |
| **Sky Computer** (Đà Nẵng) | Không nêu thời gian; **miễn phí giao chỉ từ 5 MÁY trở lên** | [skycomputer.vn](https://skycomputer.vn/dich-vu/cho-thue-may-tinh-laptop-tai-da-nang/) |
| **Đình Hậu Computer** (Đà Nẵng) | Không nêu thời gian; miễn phí vận chuyển & lắp đặt | [maytinhdinhhau.vn](https://maytinhdinhhau.vn/dich-vu-cho-thue-laptop-tai-da-nang/) |
| **DH Lend** (Đà Nẵng) | 🔑 Cam kết **"đổi máy nếu hư hỏng trong lúc sử dụng"** — **KHÔNG nêu thời gian** | [danang.plus/thue-laptop/](https://danang.plus/thue-laptop/) |
| **Laptop SGN / Đình Hậu** | Hỗ trợ kỹ thuật **24/7 miễn phí** trong thời gian thuê | nhiều nguồn |

**Ba kết luận đã được ghi trong file `01`, trích nguyên văn:**
1. *"SLA nhanh nhất toàn quốc là **2 giờ** (Laptop SGN, chỉ ở TP.HCM). Tại Đà Nẵng, cam kết tốt nhất chỉ là **'trong ngày'**."*
2. *"**'Trong ngày' là vô nghĩa với ca thi 7h30 sáng.** Nếu sinh viên đặt lúc 6h30, 'giao trong ngày' có thể là 15h chiều — đã thi xong từ lâu."*
3. *"**Không có bất kỳ đơn vị nào ở Đà Nẵng cam kết SLA tính bằng PHÚT.**"*

> 🟢 [XM] file `11` nhấn mạnh thêm: việc DH Lend cam kết đổi máy *"cho thấy **SLA đổi máy là kỳ vọng mặc định của thị trường** — mô hình của nhóm bắt buộc phải có, và nên nâng lên thành **SLA đổi máy trong X phút trong ngày thi** để tạo khác biệt."*
> 🔑 **Khoảng trống rõ ràng:** thị trường có **cam kết đổi máy** nhưng **không ai gắn số phút vào đó**. Gắn một con số phút là điều cạnh tranh rẻ nhất và mạnh nhất nhóm có thể làm.

## 9.2. Từ vựng SLA chuẩn — phải dùng đúng để không tự bẫy mình

🟡 [KT-MH] + 🔵 [TT]

| Thuật ngữ | Nghĩa | Bẫy phải tránh |
|---|---|---|
| **Response time** (thời gian phản hồi) | Từ lúc khách báo → lúc **có người trả lời** | Dễ cam kết, giá trị thấp với khách |
| **Restoration time** (thời gian khôi phục dịch vụ) | Từ lúc khách báo → lúc **khách có máy dùng được** (kể cả máy thay thế) | 🔑 **Đây mới là thứ khách quan tâm** |
| **Resolution time** (thời gian xử lý dứt điểm) | Đến khi sự cố gốc được sửa xong | Không nên cam kết với khách — đó là việc nội bộ |
| **Uptime / Availability** | % thời gian dịch vụ sẵn sàng | Không hợp mô hình này |
| **Service credit** (bồi hoàn) | Tiền/tín dụng trả lại khi vi phạm SLA | 🔑 SLA không có chế tài = lời hứa suông |
| **Advance Exchange** (đổi trước) | Gửi máy thay thế **trước khi** thu hồi máy lỗi | 🔑 Mô hình đúng cho ngày thi |
| **NBD / 4-hour response** | Các mức dịch vụ phổ biến của bảo hành doanh nghiệp (Ngày làm việc kế tiếp / phản hồi 4 giờ) | 🟡 Tên sản phẩm hay gặp: gói hỗ trợ doanh nghiệp của Dell/HP/Lenovo. 🔴 Tra: `Dell ProSupport next business day onsite SLA`, `HP Care Pack 4 hour onsite response` |

> 🔵 [TT] **Bẫy lớn nhất:** cam kết "**khắc phục** trong 15 phút" là tự sát — sửa một máy lỗi trong 15 phút là bất khả thi. Phải cam kết "**ĐỔI MÁY** trong 15 phút" (restoration bằng cách thay thế). Đây chính là lý do hot spare ở §7 là **điều kiện kỹ thuật bắt buộc** để dám hứa con số này.

## 9.3. 🔵 [TT] BỘ SLA ĐỀ XUẤT — 3 mức dịch vụ

| Cam kết | **Gói Thường** (thuê tuần/tháng) | **Gói NGÀY THI** ⭐ (sản phẩm lõi) | **Gói Giữ máy cả đợt thi** (bán cho lớp/CLB) |
|---|---|---|---|
| **Thời gian giao lần đầu** | Trong ngày, theo lịch hẹn | **≤ 20 phút** trong khuôn viên, khi đặt trước ≥ 2 giờ | Giao trước đợt thi 1 ngày |
| 🔑 **Thời gian ĐỔI MÁY khi máy lỗi** | ≤ 4 giờ trong giờ hành chính | 🔴 **≤ 15 phút** trong khuôn viên, **trong toàn bộ khung giờ thi** | **≤ 10 phút** (máy dự phòng đã đặt tại chỗ) |
| **Phản hồi hotline** | ≤ 30 phút | **≤ 3 phút** | ≤ 3 phút |
| **Khung giờ trực** | 8h–20h | 🔴 **Từ 1 giờ trước ca thi đầu đến 1 giờ sau ca thi cuối**, mọi ngày thi | Như gói ngày thi |
| **Máy đã chạy thử EOS+SEB** | ✅ | ✅ **có chạy thử trước mặt khách** | ✅ + smoke test đầu mỗi ngày |
| **Bồi hoàn nếu vi phạm** | Hoàn 50% tiền thuê | 🔴 **Hoàn 100% + 1 lượt thuê miễn phí** | Theo hợp đồng |
| **Cam kết "máy thi được"** | — | 🔴 **Nếu máy không chạy được EOS/SEB → hoàn 100% + đền bù** (🟢 [XM] đã nêu ở file `01` §10.2) | ✅ |

### Điều kiện để SLA 15 phút là KHẢ THI (🔵 [TT] — phải nói rõ trong proposal)

SLA không phải khẩu hiệu, nó là **hệ quả toán học của cách bố trí nguồn lực**. Muốn hứa 15 phút phải có đủ **5 điều kiện**:

| # | Điều kiện | Mục tham chiếu |
|---|---|---|
| 1 | **Có người trực tại chỗ** suốt khung giờ thi (không phải "gọi thì chạy tới") | §7.4 |
| 2 | **Hot spare đặt ngay sảnh**, pin 100%, đã smoke test sáng hôm đó | §7.3, §7.4 |
| 3 | **Phạm vi địa lý giới hạn trong khuôn viên** — 🔴 tuyệt đối không hứa 15 phút cho địa chỉ ngoài trường | — |
| 4 | **Hotline 1 số duy nhất**, in trên phiếu của mọi khách, có người cầm máy | §2.2 nhóm 4 |
| 5 | **Biên bản đổi máy khẩn rút gọn 1 mặt giấy** — ký trong 60 giây | §12 BM-08 |

> 🔵 [TT] **Cách trình bày ăn điểm trong proposal:** đừng chỉ viết *"chúng em cam kết đổi máy trong 15 phút"*. Hãy viết: *"Chúng tôi cam kết 15 phút vì chúng tôi bố trí X người trực + Y hot spare tại sảnh Z trong khung giờ W — và đây là bảng chi phí của việc đó."* **Cam kết có kèm cấu trúc chi phí mới là cam kết thật.**

## 9.4. 🔵 [TT] Bảng theo dõi SLA — mẫu để đo và báo cáo

| Mã sự cố | Ngày | Ca thi | Mã đơn | Giờ khách báo | Giờ phản hồi | Giờ khách có máy chạy | **Restoration (phút)** | Đạt SLA? | Nguyên nhân gốc | Bồi hoàn |
|---|---|---|---|---|---|---|---|---|---|---|
| INC-001 | | | | | | | | ☐Đ ☐K | | |

**Phân loại nguyên nhân gốc (để cải tiến, không để đổ lỗi):** ① Pin hết / pin chai · ② Lỗi phần mềm thi (EOS/SEB) · ③ Lỗi phần cứng (màn/phím/cổng) · ④ Lỗi mạng Wi-Fi · ⑤ Lỗi thao tác của khách · ⑥ **Lỗi khâu chuẩn bị của nhóm** · ⑦ Khác.

> 🔑 🔵 [TT] Nếu loại ⑥ chiếm > 20% sự cố → vấn đề không nằm ở máy mà ở **quy trình §4**. Đó là lý do phải phân loại nguyên nhân, không chỉ đếm số vụ.

---

# 10. BỘ SOP HOÀN CHỈNH — 8 QUY TRÌNH ĐÁNH SỐ

🔵 [TT] toàn bộ. Thiết kế để **in ra, dán tường, tick bằng bút**.

## SOP-01 — TIẾP NHẬN MÁY MỚI VÀO ĐỘI (Asset Intake)
**Khi nào:** mỗi lần mua/nhận ký gửi một máy. **Người làm:** Kỹ thuật. **Thời gian:** 4–8 giờ (chủ yếu chờ).

| # | Bước | Tiêu chí đạt | Không đạt thì sao |
|---|---|---|---|
| 1 | Kiểm tra ngoại hình, **chấm hạng §3.4** | 🔴 Chỉ nhận **hạng A hoặc B** | Từ chối nhận / đàm phán giảm giá |
| 2 | Ghi Serial/Service Tag, chụp 8 ảnh gốc | Đủ 8 ảnh | Làm lại |
| 3 | **Đo pin** `powercfg /batteryreport` | 🔴 **SoH ≥ 80%** | Đàm phán trừ tiền thay pin vào giá mua |
| 4 | Chạy **L3 Deep Rebuild** (§4.4) | Windows sạch, đã kích hoạt | — |
| 5 | Cài Golden Image, đặt tên máy = mã nội bộ | — | — |
| 6 | 🔴 **Chạy thử EOS Client + SEB** | Vào được màn hình đăng nhập EOS | 🔴 **KHÔNG NHẬN MÁY** — dù mọi thứ khác tốt |
| 7 | **Bài test thời lượng pin §5.4** | 🔴 **≥ 3,5 giờ** | Xếp vào nhóm cho thuê tháng, không cho thuê ca thi |
| 8 | Chạy tải liên tục (burn-in) 2–4 giờ | Không treo, không quá nhiệt | Trả lại / sửa |
| 9 | Đặt **mật khẩu BIOS**, tắt boot USB/mạng, bật Secure Boot | — | — |
| 10 | Bật **Deep Freeze** | Reboot thử, xác nhận thay đổi bị xoá | — |
| 11 | Dán **nhãn mã máy + QR + hotline**; dán **tem niêm phong** | — | — |
| 12 | Tạo hồ sơ máy trong hệ thống; **lưu hoá đơn mua** | 🔴 Không có hoá đơn = sau này không chứng minh được sở hữu khi trình báo | Xin bằng được giấy bán hàng |
| 13 | Đưa vào kho, trạng thái **"Sẵn sàng"** | — | — |

## SOP-02 — CHUẨN BỊ TRƯỚC ĐỢT THI (T−1 ngày)
**Người làm:** cả nhóm. **Thời gian:** nửa ngày.

☐ 1. Lấy **lịch thi chính thức** (ngày, ca, giờ bắt đầu/kết thúc, số môn)
☐ 2. Đối chiếu số đơn đã đặt với số máy sẵn sàng → xác định thiếu/đủ
☐ 3. 🔴 **Kiểm tra Phòng Khảo thí/IT có cập nhật EOS/SEB phiên bản mới không**
☐ 4. Nếu có bản mới → cập nhật Golden Image, **tăng số phiên bản**, ghi CHANGELOG
☐ 5. 🔴 **SMOKE TEST**: chạy EOS+SEB trên **2 máy ngẫu nhiên** → nếu lỗi, dừng toàn bộ và xử lý
☐ 6. Giữ **1–2 hot spare chạy image phiên bản TRƯỚC** (phòng bản mới lỗi)
☐ 7. Sạc đầy 100% toàn bộ máy sẽ giao + hot spare
☐ 8. Đóng **"bộ ứng cứu"**: máy + sạc + tai nghe + chuột trong 1 túi
☐ 9. In: biên bản BM-01 (số lượng = số đơn + 20%), BM-08 (đổi máy khẩn), phiếu hướng dẫn
☐ 10. Phân ca trực, xác nhận **ai cầm hotline** từng khung giờ
☐ 11. Kiểm tra ổ cắm điện nhiều cổng + dây nối dài tại điểm trực
☐ 12. Nhắn Zalo cho toàn bộ khách đã đặt: giờ nhận máy, địa điểm, cần mang gì

## SOP-03 — GIAO MÁY (Check-out) · mục tiêu **≤ 8 phút/khách**

| # | Bước | Thời gian |
|---|---|---|
| 1 | Kiểm tra **thẻ SV + đối chiếu MSSV** với đơn đặt | 1' |
| 2 | Chụp **ảnh khách cầm thẻ SV** | 30" |
| 3 | Mở máy, **chạy thử EOS+SEB TRƯỚC MẶT KHÁCH** | 2' |
| 4 | Cùng khách **xem 8 ảnh tình trạng**, khách xác nhận | 1' |
| 5 | Đếm phụ kiện cùng khách | 30" |
| 6 | Điền biên bản BM-01, **khách ký 5 dòng cam kết** | 2' |
| 7 | Thu tiền + cọc, xuất biên nhận | 1' |
| 8 | 🔑 **Nhắc miệng 3 điều**: giờ trả chính xác · số hotline · "có sự cố gọi ngay, đừng tự xử lý" | 30" |
| 9 | Cập nhật trạng thái máy trên web → "Đang cho thuê" | 30" |

## SOP-04 — ỨNG CỨU SỰ CỐ TRONG CA THI (Hot Swap) · mục tiêu **≤ 15 phút**

```
  Khách gọi hotline
        ↓ (≤ 60 giây bắt máy)
  Hỏi 3 CÂU, KHÔNG HỎI THÊM:
    1. "Bạn đang ở phòng nào?"
    2. "Máy bị gì? (không lên nguồn / SEB không chạy / hết pin / khác)"
    3. "Ca thi bắt đầu/kết thúc lúc mấy giờ?"
        ↓
  ┌── Lỗi có thể sửa tại chỗ < 3 phút? ────┐
  │ (cắm sạc, khởi động lại, kết nối wifi) │
  YES                                      NO
   ↓                                        ↓
 Hướng dẫn qua điện thoại          🔴 KHÔNG CỐ SỬA — MANG HOT SPARE ĐI NGAY
 Gọi lại xác nhận sau 2'             ↓
                              Cầm "bộ ứng cứu" chạy tới phòng thi
                                    ↓
                              Đổi máy, bật sẵn, mở SEB giúp khách
                                    ↓
                              Ký BM-08 (30 giây) — KHÔNG làm biên bản dài
                                    ↓
                              Mang máy lỗi về, KHOÁ trạng thái, chờ L3
                                    ↓
                              Ghi vào bảng theo dõi SLA §9.4
                                    ↓
                              Sau ca thi: gọi hỏi thăm kết quả + xin lỗi
                                    + áp dụng bồi hoàn đã cam kết
```

> 🔴 **Quy tắc vàng của SOP-04: KHÔNG SỬA MÁY TRONG GIỜ THI.** Khi đồng hồ đang chạy, mọi phút dùng để chẩn đoán là phút khách mất bài thi. **Đổi máy trước, sửa sau.** Đây là lý do duy nhất hot spare tồn tại.

## SOP-05 — NHẬN MÁY VỀ (Check-in) · mục tiêu **≤ 6 phút/khách**
☐ 1. Đối chiếu **mã máy + serial + số tem niêm phong**
☐ 2. Đếm phụ kiện
☐ 3. Chụp **8 ảnh** vào thư mục `/nhan/`
☐ 4. **Chấm hạng ngoại hình**, so với hạng lúc giao
☐ 5. Bật máy, chạy nhanh **checklist 12 điểm** (§2.2 nhóm 6)
☐ 6. Ghi % pin khi trả
☐ 7. Điền phần "CHECK-IN" của BM-01, khách ký
☐ 8. **Xử lý cọc ngay tại chỗ** — 🔑 hoàn cọc nhanh là yếu tố giữ khách số 1
☐ 9. Nếu có hư hỏng → 🔴 **KHÔNG tranh cãi tại chỗ**: lập biên bản, chụp ảnh, hẹn báo giá trong 24 giờ (SOP-06)

## SOP-06 — XỬ LÝ HƯ HỎNG & ĐỀN BÙ
☐ 1. Lập biên bản hư hỏng riêng + ảnh so sánh giao/nhận
☐ 2. Xác định: **hao mòn bình thường** (doanh nghiệp chịu, §3.4 R3) hay **sự kiện rời rạc** (khách chịu, R4)
☐ 3. Nếu khách chịu → **mang đi báo giá ở xưởng đối tác**, 🔑 **báo giá TRƯỚC khi sửa** (🟢 [XM] file `08` điều khoản #9)
☐ 4. Gửi khách: ảnh + báo giá + hoá đơn sửa chữa
☐ 5. Áp dụng gói miễn trừ nếu khách đã mua (trần trách nhiệm)
☐ 6. Thu phần chênh / trừ cọc, xuất biên nhận
☐ 7. Máy vào trạng thái "Đang sửa" — 🔑 **trừ khỏi mẫu số Availability** (§6.1)

## SOP-07 — XỬ LÝ TRẢ TRỄ → thực hiện đúng thang 7 bước §8.2, không tự ý rút gọn hay bỏ bước.
🔴 **Quy tắc cứng:** mọi bước từ T+24 giờ trở đi **phải do trưởng nhóm thực hiện**, không giao cộng tác viên — vì từ đây mọi câu chữ đều có thể trở thành chứng cứ.

## SOP-08 — THANH LÝ MÁY (Retire / Disposal)
☐ 1. Xác nhận lý do: hạng D · pin < 60% không đáng thay · hỏng nặng · hết vòng đời kinh tế
☐ 2. Sao lưu nhật ký máy (số lượt, doanh thu trọn đời) → **dữ liệu để tính lại unit economics**
☐ 3. 🔴 **Xoá dữ liệu mức PURGE** theo §4.7
☐ 4. 🔴 **Xác minh** (§4.7.5) + **cấp Chứng nhận xoá dữ liệu BM-07**
☐ 5. Gỡ nhãn nội bộ, gỡ tem, xoá mật khẩu BIOS
☐ 6. Bán/tặng/thải bỏ; **giữ chứng từ**
☐ 7. Cập nhật OEC của đội máy → tính lại Dollar Utilization (§6.1)

---

# 11. 🔵 [TT] TỔ CHỨC NHÂN SỰ — ĐỘI 3–4 SINH VIÊN

| Vai trò | Ai kiêm | Việc chính | Thời gian ngoài mùa thi | Trong tuần thi |
|---|---|---|---|---|
| **Quản lý đội máy** (*"laptop manager"*) | 1 người cố định | Nhật ký máy, đo pin, Golden Image, lên lịch bảo trì | ~4 giờ/tuần | ~4 giờ/ngày |
| **Trực giao–nhận** | Luân phiên | SOP-03, SOP-05 | Theo lịch hẹn | Toàn thời gian khung giờ thi |
| **Trực hotline/ứng cứu** | Luân phiên, ≥1 người | SOP-04 | Theo giờ hành chính | 🔴 Có mặt tại sảnh |
| **Trưởng nhóm** | 1 người | Trả trễ từ T+24 giờ, tranh chấp, quan hệ nhà trường | ~2 giờ/tuần | Trực gián tiếp |

> 🟢 [XM] **Có cơ sở ngành cho vai trò #1:** file `10` §2.6, bài Code4Lib về chương trình cho mượn laptop của Đại học Arizona (vận hành từ 2003, luân chuyển **trên 300 thiết bị**) nhấn mạnh việc **phân công một "laptop manager" chuyên trách** và lập bảng theo dõi thiết bị — [journal.code4lib.org/articles/5876](https://journal.code4lib.org/articles/5876). File `10` §9.1 cũng khuyến nghị: *"Có **1 người chuyên trách quản lý máy** + bảng theo dõi tồn kho từng máy"*.

**Ước tính nhân công tuần thi (đội 30 máy) 🔵 [TT], dựa trên §4.5:**

| Hạng mục | Giờ/ngày thi |
|---|---|
| Tái chuẩn bị máy (có Deep Freeze) | 14,6 |
| Giao máy (25 lượt × 8 phút) | 3,3 |
| Nhận máy (25 lượt × 6 phút) | 2,5 |
| Trực hotline/ứng cứu (chờ + xử lý) | 8,0 |
| Hành chính, thu tiền, đối soát | 2,0 |
| **Tổng** | **≈ 30,4 giờ/ngày thi** |
| **Quy ra người** (ca 6 giờ) | **≈ 5 ca người/ngày** |

🔴 **Hàm ý phải nêu trong proposal:** trong tuần thi, một đội **3 người là KHÔNG ĐỦ** cho 30 máy. Hoặc (a) tuyển cộng tác viên thời vụ đúng tuần thi (đơn giá 25.000–30.000 VND/giờ 🟢 [XM] file `11`), hoặc (b) **giảm quy mô đội máy xuống ~15–20 máy** ở giai đoạn đầu. **Đây là một ràng buộc thật, và việc nhóm tự nhận ra nó thể hiện độ chín của kế hoạch.**

---

# 12. DANH MỤC BIỂU MẪU

| Mã | Tên | Trạng thái | Ở đâu |
|---|---|---|---|
| **BM-01** | Biên bản bàn giao laptop cho thuê (2 chiều) | ✅ Đã soạn đầy đủ | §2.3 |
| **BM-02** | Checklist kiểm tra 12 điểm | ✅ | §2.2 nhóm 6 |
| **BM-03** | Nhật ký máy (asset log) | 🔶 Khung cột | §12.1 dưới |
| **BM-04** | Nhật ký pin | ✅ | §5.6 |
| **BM-05** | Văn bản yêu cầu trả lại tài sản | ✅ Đã soạn đầy đủ | §8.5 |
| **BM-06** | Đơn trình báo | ✅ Đã soạn — 🔴 cần luật sư duyệt | §8.6 |
| **BM-07** | Chứng nhận xoá dữ liệu | ✅ Đã soạn | §4.7.6 |
| **BM-08** | Biên bản đổi máy khẩn (1 mặt) | ✅ Dưới đây | §12.2 |
| **BM-09** | Bảng theo dõi SLA | ✅ | §9.4 |
| **BM-10** | Bảng điều khiển KPI 12 chỉ số | ✅ | §6.5 |

## 12.1. BM-03 — Nhật ký máy (mỗi máy một dòng, cập nhật sau mỗi lượt)

| Cột | Nội dung |
|---|---|
| Mã máy · Hãng/Model · Serial | Cố định |
| Ngày vào đội · Giá mua · Hạng lúc nhận | Cố định |
| **Số lượt thuê luỹ kế** | +1 mỗi lượt |
| **Số giờ cho thuê luỹ kế** | Tính utilization |
| **Doanh thu trọn đời** | Đối chiếu điểm hoà vốn (RTR: 17–18 lượt 🟢 [XM]) |
| Hạng ngoại hình hiện tại | Cập nhật mỗi check-in |
| SoH pin gần nhất · ngày đo · thời lượng thực đo | §5 |
| Mã Golden Image đang chạy | §4.3 |
| Lần L2 gần nhất · lần L3 gần nhất | Lên lịch bảo trì |
| Lịch sử sự cố (ngày, loại, chi phí sửa) | Quyết định thanh lý |
| Trạng thái | Sẵn sàng / Đang thuê / Đang chuẩn bị / Đang sửa / Hot spare / Đã thanh lý |

## 12.2. BM-08 — Biên bản đổi máy khẩn (ký trong 60 giây)

```
┌──────────────────────────────────────────────────────────────────┐
│           BIÊN BẢN ĐỔI MÁY KHẨN — TRONG CA THI                   │
│  Mã sự cố: INC-______   Đơn gốc: RENT-________-____              │
├──────────────────────────────────────────────────────────────────┤
│ Khách: ______________________ MSSV: ____________                 │
│ Phòng thi: __________  Ca thi: ____h____ – ____h____             │
│                                                                  │
│ Giờ khách báo:  ____h____     Giờ giao máy mới: ____h____        │
│ ► THỜI GIAN KHÔI PHỤC: ______ phút   ☐ ĐẠT SLA  ☐ KHÔNG ĐẠT     │
│                                                                  │
│ MÁY LỖI  — mã: __________ serial: ______________                 │
│   Triệu chứng: ☐ Không lên nguồn ☐ SEB không chạy ☐ Hết pin      │
│                ☐ Mất wifi ☐ Màn hình ☐ Khác: _______________     │
│ MÁY THAY — mã: __________ serial: ______________  Pin: ____%     │
│   ☐ Đã bật sẵn  ☐ Đã mở SEB giúp khách  ☐ Phụ kiện đủ           │
│                                                                  │
│ Phụ kiện: ☐ Giữ nguyên của khách  ☐ Đổi luôn: ______________     │
│                                                                  │
│ Khách xác nhận đã nhận máy thay thế và tiếp tục được ca thi:     │
│   Khách ký: ____________      Nhân viên ký: ____________         │
│                                                                  │
│ ► SAU CA THI PHẢI LÀM:  ☐ Gọi hỏi thăm kết quả + xin lỗi         │
│                         ☐ Áp dụng bồi hoàn đã cam kết            │
│                         ☐ Ghi vào bảng SLA  ☐ Máy lỗi → L3       │
└──────────────────────────────────────────────────────────────────┘
```

---

# 13. 🔴 NHỮNG ĐIỀU KHÔNG XÁC MINH ĐƯỢC — DANH SÁCH TRUNG THỰC

## A. Về giới hạn của phiên nghiên cứu
1. 🔴 **KHÔNG thực hiện được một lượt WebSearch nào** — ngân sách 200/200 đã cạn trước khi nhiệm vụ bắt đầu. WebFetch/curl bị chặn hoàn toàn.
2. 🔴 **Không có URL mới nào trong tài liệu.** Mọi URL đều trích lại từ file `01`, `02`, `08`, `09`, `10`, `11` cùng thư mục.
3. 🔴 Toàn bộ kiến thức chuyên môn là **kiến thức nội tại của mô hình (cutoff 05/2026)**, chưa kiểm chứng.

## B. Chuẩn & tài liệu kỹ thuật
4. 🔴 **NIST SP 800-88 Rev.1**: không mở được bản gốc. **Ba mức Clear/Purge/Destroy, nguyên tắc "1 lượt ghi đè là đủ", và mẫu Chứng nhận xoá dữ liệu ở phụ lục** — đúng theo hiểu biết của mô hình nhưng **chưa đối chiếu văn bản**. Số hiệu phụ lục (Appendix G) **đặc biệt cần kiểm tra**.
5. 🔴 **Không có tiêu chuẩn cosmetic grading nào được xác minh.** Định nghĩa Grade A/B/C/D ở §3.3 là **mô tả thông lệ**, không phải trích dẫn tiêu chuẩn.
6. 🔴 **Giá và tình trạng phiên bản của mọi công cụ ở §4.2 chưa kiểm chứng**, đặc biệt: Deep Freeze (giá 🔴 [KTĐ]), Macrium Reflect (bản Free được cho là đã khai tử — **phải xác nhận**), MDT (bản cuối 8456/2019 — **phải xác nhận**), yêu cầu giấy phép của Autopilot Reset.
7. 🔴 **Cú pháp `powercfg /batteryreport` và tên các trường trong báo cáo** — cần nhóm tự chạy thử một lần.
8. 🔴 **Ngưỡng pin 80% / 50%** (§5.3) chưa có nguồn. Ngưỡng đề xuất của dự án là **thiết kế của người nghiên cứu**, không phải chuẩn ngành.
9. 🔴 **Thời gian bung ảnh đĩa, thời gian sanitization** (§4.4) là **ước lượng kỹ thuật**, không phải đo thực. Nhóm phải bấm giờ thật trên máy thật.

## C. Chỉ số ngành
10. 🔴 **KHÔNG có benchmark utilization nào được xác minh.** Con số 35–45% là nguồn `[C]` yếu (blog cá nhân) đã được đánh dấu như vậy ngay trong file `02`. Các khoảng 65–72% / 30–40% ở §6.2 là **trí nhớ mơ hồ của mô hình — TUYỆT ĐỐI KHÔNG TRÍCH**.
11. 🔴 **KHÔNG có số liệu shrinkage/loss rate của ngành cho thuê thiết bị.** Xác nhận lại kết luận đã có ở file `08` §8.4 và file `02` §17.
12. 🔴 **Tỷ lệ hỏng máy trong ngày thi (p = 2% / 5%)** dùng để tính hot spare ở §7.2 là **giả định hoàn toàn của người nghiên cứu**. Phép toán nhị thức thì đúng; đầu vào thì chưa có căn cứ.
13. 🔴 **Tỷ lệ hot spare 5–10%** trong quản trị tài sản CNTT: chưa xác minh.
14. 🔴 **Chi phí fulfillment 27,8% doanh thu của RTR** — đã xác minh ở file `02` nhưng là **ngành thời trang**, không phải laptop. Không được áp thẳng.

## D. Pháp lý Việt Nam — 🔴🔴 rủi ro sai cao nhất
15. 🔴 **Mâu thuẫn chưa giải quyết về số điều BLDS 2015**: file `01` ghi **Đ.554, 557**; mô hình cho rằng hợp đồng thuê tài sản ở khoảng **Đ.472–493**. **Phải tra dứt điểm.**
16. 🔴 **Mọi số điều BLHS** (174 lừa đảo / 175 lạm dụng tín nhiệm / 176 chiếm giữ trái phép / 170 cưỡng đoạt / 155 làm nhục) **chưa xác minh**.
17. 🔴 **Mọi ngưỡng giá trị** (2 triệu / 4 triệu / 10 triệu đồng) **chưa xác minh** — và đây là con số **quyết định vụ việc có thuộc phạm vi hình sự hay không**.
18. 🔴 **Mọi thời hạn tố tụng** (20 ngày, gia hạn 2 tháng; thời hiệu 3 năm) **chưa xác minh**.
19. 🔴 **Mức án phí** (300.000 đồng / 5% giá trị tranh chấp) **chưa xác minh**, và nghị quyết viện dẫn có thể **đã bị thay thế**.
20. 🔴🔴 **Bốn thay đổi thể chế 2025** ở §8.4.0 (bỏ cấp huyện · sáp nhập Đà Nẵng–Quảng Nam · bỏ công an cấp huyện · Toà án nhân dân khu vực) — **chưa xác minh, nhưng nếu đúng thì làm sai lệch nơi nộp đơn**. 🔑 **Đây là việc cần tra ĐẦU TIÊN trong nhóm pháp lý.**
21. 🔴 **Không xác minh được có mẫu đơn tố giác bắt buộc cho công dân hay không.** BM-06 là mẫu tự soạn.
22. 🔴 **Nghị định 13/2023/NĐ-CP** và tình trạng Luật Bảo vệ dữ liệu cá nhân tại 2026: chưa xác minh.
23. 🔴 **Tính hợp pháp của việc khoá máy từ xa** theo pháp luật Việt Nam: chưa xác minh.

## E. Bối cảnh FPT Đà Nẵng
24. 🔴 **Chưa xác minh quy chế thi của ĐH FPT có CHO PHÉP dùng máy thuê ngoài hay không** — file `01`, `02`, `10` đều xếp đây là **rủi ro số 1, phải hỏi Phòng Khảo thí TRƯỚC MỌI VIỆC KHÁC**. **Nếu quy chế cấm, toàn bộ SOP này vô nghĩa.**
25. 🔴 **Chưa có lịch thi thực tế** (số đợt/năm, số ngày/đợt, số ca/ngày, độ dài ca) — dữ liệu này quyết định §5.4 (ngưỡng pin), §6.2 (trần utilization), §7 (số hot spare), §11 (nhân sự).
26. 🔴 **Phiên bản SEB/EOS hiện hành tại 09/2026** — file `01` nêu `SEB_3.10.0.794`, nhưng đó là dữ liệu từ phiên khác, có thể đã cũ.
27. 🔴 **Chi phí thay pin, sửa màn hình, thay vỏ theo model** — dùng bảng khảo sát sẵn có ở file `08` §8.1.

---

# 14. 🎯 VIỆC CẦN LÀM TIẾP — CÓ THỨ TỰ ƯU TIÊN

## Ưu tiên 1 — Chặn rủi ro sụp đổ mô hình (làm trong tuần này)

| # | Việc | Cách làm | Ai |
|---|---|---|---|
| 1 | 🔴 **Hỏi Phòng Khảo thí: quy chế thi có cho dùng máy thuê ngoài không?** | Đến hỏi trực tiếp, xin văn bản hoặc email trả lời | Trưởng nhóm |
| 2 | 🔴 **Lấy lịch thi chính thức** của campus Đà Nẵng | Phòng Đào tạo / FAP | Bất kỳ ai |
| 3 | 🔴 **Gọi/đến Công an phường Hoà Hải** hỏi nơi nộp đơn + mẫu đơn + giấy tờ cần thiết | Đi trực tiếp, ghi chép lại | Trưởng nhóm |

> 🔑 Việc #3 vừa giải quyết các điểm chưa xác minh 20–21, vừa tạo **dữ liệu sơ cấp** — thứ mà một bài proposal môn Khởi nghiệp được chấm điểm cao.

## Ưu tiên 2 — Tra cứu có câu lệnh sẵn (2–3 giờ)

| # | Cần tra | Từ khoá / nơi tra |
|---|---|---|
| 4 | Số điều BLDS 2015 về hợp đồng thuê tài sản | `thuvienphapluat.vn` → `Bộ luật Dân sự 2015 hợp đồng thuê tài sản điều 472` |
| 5 | Điều 174/175/176 BLHS + ngưỡng giá trị | `thuvienphapluat.vn` → `Điều 175 Bộ luật Hình sự 2015 lạm dụng tín nhiệm chiếm đoạt tài sản` |
| 6 | Bốn thay đổi thể chế 2025 | `chính quyền địa phương 2 cấp 2025`, `bỏ công an cấp huyện`, `Toà án nhân dân khu vực` |
| 7 | NIST SP 800-88 Rev.1 (PDF miễn phí) | `NIST SP 800-88 Rev 1 Guidelines for Media Sanitization PDF` |
| 8 | 🔑 **Bài Code4Lib về chương trình cho mượn laptop** — để lấy **tỷ lệ mất máy** | [journal.code4lib.org/articles/5876](https://journal.code4lib.org/articles/5876) — **truy cập mở, miễn phí, mở là đọc được ngay** |
| 9 | Benchmark utilization từ nguồn thật | Báo cáo quý của `United Rentals`, `Herc Holdings`, `Ashtead` |
| 10 | Định nghĩa Grade A/B/C của các sàn | `eBay Refurbished conditions`, `Back Market grade Fair Good Excellent` |

## Ưu tiên 3 — Tự đo, tự khảo sát (1 tuần)

| # | Việc | Sản phẩm đầu ra |
|---|---|---|
| 11 | Chạy `powercfg /batteryreport` trên 3–5 máy của chính nhóm | Xác nhận cú pháp + có số SoH thật đưa vào proposal |
| 12 | **Bấm giờ thật** quy trình L1 và L2 trên 1 máy | Thay các ước lượng ở §4.4 bằng số đo thật — **rất thuyết phục** |
| 13 | Xin báo giá **Deep Freeze** cho 30 máy (đại lý Faronics VN) | Ra quyết định mua/không có căn cứ (§4.5) |
| 14 | Khảo giá thay pin / thay màn theo model (bảng ở file `08` §8.1) | Điền bảng giá đền bù §3.4 |
| 15 | Khảo sát sinh viên: **mức cọc chấp nhận được** + **mức phí trễ chấp nhận được** | Hiệu chỉnh §8.2 |

---

# 15. DANH SÁCH URL ĐÃ DÙNG TRONG TÀI LIỆU NÀY

> 🔴 **Toàn bộ URL dưới đây được TRÍCH LẠI từ các file nghiên cứu khác của dự án, KHÔNG do phiên này tìm được.** Nhóm nên mở lại ít nhất một lần để xác nhận trước khi nộp.

| # | URL | Dùng ở mục | File nguồn |
|---|---|---|---|
| 1 | https://www.grover.com/at-en/g-about/asset-condition | §2.2 (checklist 5 điểm), §3.2, §4.7.1 | `02` |
| 2 | https://service.grover.com/hc/en-us/articles/19918338642578-Repair-and-replacement-costs | §3.1, §3.4 | `02` |
| 3 | https://www.renttherunway.com/pages/termsofservice | §3.4 | `02` |
| 4 | https://d3.harvard.edu/platform-rctom/submission/rent-the-runway-digitizes-high-fashion/ | §6.3 (zero-day turnaround) | `02` |
| 5 | https://www.natejonesentrepreneur.com/post/equipment-rental-business-startup-costs | §6.2 (35–45%) — **nguồn yếu** | `02` |
| 6 | https://www.odoo.com/documentation/18.0/applications/sales/rental.html | §4.6 (Security Time) | `09` |
| 7 | https://journal.code4lib.org/articles/5876 | §6.4, §11, §14 | `10` |
| 8 | https://laptopsgn.com/tin-tuc/dich-vu-cho-thue-laptop-tphcm-gia-re-giao-2h/ | §9.1 (SLA 2 giờ) | `01` |
| 9 | https://truonggiang.vn/cho-thue-laptop.html | §9.1 | `01` |
| 10 | https://mitgroup.vn/cho-thue-laptop/ | §9.1 | `01` |
| 11 | https://skycomputer.vn/dich-vu/cho-thue-may-tinh-laptop-tai-da-nang/ | §9.1 | `01` |
| 12 | https://maytinhdinhhau.vn/dich-vu-cho-thue-laptop-tai-da-nang/ | §9.1 | `01` |
| 13 | https://danang.plus/thue-laptop/ | §9.1 (DH Lend đổi máy) | `01`, `11` |
| 14 | https://congchung247.com.vn/thue-thiet-bi-lam-hong-ben-thue-co-phai-boi-thuong/ | §2.1 (BLDS) — **có mâu thuẫn số điều** | `01` |
| 15 | https://thuvienphapluat.vn | §8.4 (nơi tra luật) | `08` |
| 16 | https://library.niu.edu/university-libraries/about/policies/laptopcirculation.shtml | §8.1 (NIU: 5 USD/ngày, mốc 7 ngày) | `10` |
| 17 | https://services.ku.edu/TDClient/818/Portal/KB/Article/20717/KU-Libraries-Fines-Fees-Lost-Item-and-Damage-Charges-for-Library-Equipment-and-Accessories-Laptops-H | §8.1 (KU: 0,10 USD/phút, trần 30 USD) | `10` |
| 18 | https://library.uconn.edu/?p=967 | §8.1, §2.2 (UConn: laptop 1.500 USD, sạc 30 USD) | `10` |
| 19 | https://thehub.stanford.edu/borrow-equipment/loan-policies | §8.1, §8.3 (khoá máy từ xa sau 2 ngày) | `10` |
| 20 | https://libraries.mit.edu/borrow/ | §8.1 (MIT: không phạt trễ) | `10` |

---

**— HẾT TÀI LIỆU 13 —**
*Lập ngày 14/09/2026 · Nguyên liệu thô, chưa biên tập cho bài nộp · Mọi nhãn 🟡 và 🔴 phải được xử lý trước khi trích vào proposal*
