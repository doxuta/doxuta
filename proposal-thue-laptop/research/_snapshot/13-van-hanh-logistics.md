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
