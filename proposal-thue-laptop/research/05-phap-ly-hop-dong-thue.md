# 05 — KHUNG PHÁP LÝ VIỆT NAM CHO MÔ HÌNH CHO THUÊ LAPTOP ĐI THI (quy mô nhỏ, quanh ĐH FPT Đà Nẵng)

> **Tài liệu nghiên cứu thô** phục vụ viết proposal môn Khởi nghiệp.
> Ngày lập: 14/09/2026. Ưu tiên văn bản còn hiệu lực tại thời điểm 2025–2026.

---

## 0. CẢNH BÁO VỀ NGUỒN — ĐỌC TRƯỚC KHI DÙNG

Trong phiên nghiên cứu này, **toàn bộ các cổng pháp luật Việt Nam thông dụng đều bị chặn bởi proxy mạng** của môi trường làm việc:

| Tên miền thử truy cập | Kết quả |
|---|---|
| `thuvienphapluat.vn` | EGRESS_BLOCKED |
| `vbpl.vn` | EGRESS_BLOCKED |
| `luatvietnam.vn` | EGRESS_BLOCKED |
| `moj.gov.vn` | EGRESS_BLOCKED |
| `xaydungchinhsach.chinhphu.vn` | EGRESS_BLOCKED |
| `lawnet.vn` | EGRESS_BLOCKED |
| `google.com`, `duckduckgo.com`, `wikipedia.org` | EGRESS_BLOCKED |

Ngoài ra, hạn mức WebSearch của phiên đã bị dùng hết (200/200) trước khi bắt đầu.

**Cách khắc phục đã dùng:** chỉ còn `github.com` và `raw.githubusercontent.com` truy cập được. Vì vậy toàn bộ văn bản luật trích dẫn dưới đây được lấy từ **các bản sao (mirror) nguyên văn đặt trên GitHub**, chủ yếu là:

- Kho [`newnol/vn-legal-corpus`](https://raw.githubusercontent.com/newnol/vn-legal-corpus/main/README.md) — theo README, đây là dataset văn bản pháp luật VN thu thập từ **https://vbpl.moj.gov.vn/** (Cơ sở dữ liệu quốc gia về văn bản pháp luật, Bộ Tư pháp), có đầy đủ metadata gốc (số hiệu, ngày ban hành, ngày hiệu lực, tình trạng hiệu lực, cơ quan ban hành).
- Kho [`diepxuan/diepxuan.github.io`](https://github.com/diepxuan/diepxuan.github.io/blob/main/van-ban/dan-su/dan-su.md) — bản **Bộ pháp điển** đề mục "Dân sự" (ký hiệu điều dạng `9.1.LQ.xxx`), nguồn ghi là Cổng thông tin điện tử Chính phủ / vanban.chinhphu.vn.
- Kho [`kohaku4869/Vietnam-legal-assistant`](https://raw.githubusercontent.com/kohaku4869/Vietnam-legal-assistant/main/vectorstore/civil_law/texts.txt) — BLDS 2015 Điều 1–364, có dấu vết **Công báo số 1243 + 1244 ngày 28-12-2015**.
- Kho [`caubetotbunggg/BTTH3`](https://raw.githubusercontent.com/caubetotbunggg/BTTH3/main/data/processed/text/26-2023-QH15.txt) — Luật Căn cước số 26/2023/QH15 nguyên văn.

**Hệ quả:** số điều, số văn bản, ngày hiệu lực và nội dung điều khoản dưới đây **đã được đối chiếu chéo giữa nhiều nguồn khi có thể**, nhưng khi nộp proposal, nhóm **PHẢI kiểm tra lại trên thuvienphapluat.vn hoặc vbpl.moj.gov.vn** và thay URL trích dẫn bằng URL chính thống. Đây là yêu cầu học thuật bắt buộc, không phải khuyến nghị.

Một dataset bị **loại bỏ** vì phát hiện **nội dung bịa (LLM-generated)**: `TienLee989/Legal_QA_HRAG_Project/dataset/dan-su-2015/*.csv` ghi "Điều 451 BLDS 2015 quy định: Hợp đồng mua bán tài sản là..." trong khi Điều 451 BLDS 2015 thực tế là "Bán đấu giá tài sản". **Không dùng nguồn này.**

---

## 1. BẢN ĐỒ PHÁP LÝ TỔNG QUAN

Mô hình "website cho thuê laptop để đi thi" chạm vào **7 nhóm quy phạm**:

| # | Nhóm | Văn bản trụ cột | Mức độ rủi ro với dự án |
|---|---|---|---|
| 1 | Hợp đồng thuê tài sản (động sản) | Bộ luật Dân sự 2015 (Luật 91/2015/QH13), Điều 472–482 | Trung bình — cần soạn hợp đồng đúng |
| 2 | Biện pháp bảo đảm (cọc / ký cược) | BLDS 2015 Điều 309, 317, **328, 329** | **Cao** — rất dễ chọn sai công cụ |
| 3 | Chế tài khi khách không trả máy | BLHS 2015 Điều 174, **175**, 176, 178; NĐ 282/2025/NĐ-CP Điều 18 | Trung bình |
| 4 | Đăng ký kinh doanh + thuế | NĐ 01/2021/NĐ-CP Ch.VIII; NĐ 125/2025/NĐ-CP Đ.33; Luật 48/2024/QH15; NQ 198/2025/QH15 | Trung bình |
| 5 | Bảo vệ dữ liệu cá nhân | NĐ 13/2023/NĐ-CP; **Luật 91/2025/QH15 (hiệu lực 01/01/2026)**; **NĐ 356/2025/NĐ-CP** | **RẤT CAO** |
| 6 | Giữ giấy tờ tùy thân của khách | **Luật Căn cước 2023 (26/2023/QH15) Điều 7**; NĐ 282/2025/NĐ-CP Điều 11 | **RẤT CAO — có hành vi bị nghiêm cấm** |
| 7 | Tránh bị coi là cầm đồ; giao dịch điện tử; bảo vệ NTD | NĐ 96/2016/NĐ-CP (sửa bởi NĐ 56/2023); Luật 20/2023/QH15; Luật 19/2023/QH15 | Trung bình |

---

## 2. BỘ LUẬT DÂN SỰ 2015 — HỢP ĐỒNG THUÊ TÀI SẢN (Điều 472–482)

**Văn bản:** Bộ luật Dân sự số **91/2015/QH13**, Quốc hội khóa XIII thông qua 24/11/2015, **có hiệu lực thi hành từ 01/01/2017**.
**Nguồn nguyên văn đã fetch:** [Bộ pháp điển – đề mục Dân sự (diepxuan.github.io mirror)](https://raw.githubusercontent.com/diepxuan/diepxuan.github.io/main/van-ban/dan-su/dan-su.md) — mỗi điều được gắn nhãn `Điều 9.1.LQ.<số điều>` kèm dòng "(Điều xxx Bộ luật số 91/2015/QH13, có hiệu lực thi hành kể từ ngày 01/01/2017)".

### 2.1 Bảng tra nhanh Điều 472–482

| Điều | Tên điều | Nội dung cốt lõi (nguyên văn rút gọn) | Ý nghĩa với dự án cho thuê laptop |
|---|---|---|---|
| **472** | Hợp đồng thuê tài sản | "Hợp đồng thuê tài sản là sự thỏa thuận giữa các bên, theo đó **bên cho thuê giao tài sản cho bên thuê để sử dụng trong một thời hạn, bên thuê phải trả tiền thuê**." | Đây chính là bản chất pháp lý của dịch vụ. **Không phải** mua bán, **không phải** cầm đồ, **không phải** tín dụng. |
| **473** | Giá thuê | "1. Giá thuê do các bên **thoả thuận** hoặc do người thứ ba xác định theo yêu cầu của các bên, trừ trường hợp luật có quy định khác. 2. Trường hợp không có thỏa thuận hoặc thỏa thuận không rõ ràng thì giá thuê được xác định theo **giá thị trường** tại địa điểm và thời điểm giao kết." | Giá thuê laptop do 2 bên tự thỏa thuận — **nhà nước không áp trần giá**. Nhưng phải ghi giá rõ ràng trên website và trong hợp đồng, nếu không sẽ bị áp "giá thị trường". |
| **474** | Thời hạn thuê | "1. Thời hạn thuê do các bên thoả thuận; nếu không có thoả thuận thì **được xác định theo mục đích thuê**. 2. Trường hợp các bên không thoả thuận về thời hạn thuê và thời hạn thuê không thể xác định được theo mục đích thuê thì mỗi bên có quyền chấm dứt hợp đồng bất cứ lúc nào, nhưng phải **thông báo cho bên kia trước một thời gian hợp lý**." | Với mô hình "thuê theo ca thi", **bắt buộc ghi rõ giờ nhận – giờ trả** (ví dụ: 07:00 – 12:00 ngày 15/09/2026). Nếu không, "mục đích thuê" = buổi thi sẽ được dùng để suy ra thời hạn, gây tranh chấp. |
| **475** | Cho thuê lại | "Bên thuê có quyền cho thuê lại tài sản mà mình đã thuê, **nếu được bên cho thuê đồng ý**." | Phải có điều khoản **cấm cho thuê lại** (hoặc yêu cầu đồng ý bằng văn bản). Nếu im lặng, luật không tự động cấm — nhưng mặc định vẫn cần "được bên cho thuê đồng ý". Nên ghi rõ để triệt tiêu tranh cãi. |
| **476** | Giao tài sản thuê | "1. Bên cho thuê phải giao tài sản cho bên thuê **đúng số lượng, chất lượng, chủng loại, tình trạng, thời điểm, địa điểm đã thoả thuận và cung cấp thông tin cần thiết về việc sử dụng tài sản đó**. 2. Trường hợp bên cho thuê **chậm giao tài sản** thì bên thuê có thể gia hạn giao tài sản hoặc **hủy bỏ hợp đồng và yêu cầu bồi thường thiệt hại**; nếu tài sản thuê **không đúng chất lượng** như thoả thuận thì bên thuê có quyền yêu cầu sửa chữa, **giảm giá thuê** hoặc hủy bỏ hợp đồng và yêu cầu bồi thường thiệt hại." | **Rủi ro lớn nhất về phía startup.** Giao máy trễ hoặc máy lỗi trong ngày thi → khách có quyền đòi **bồi thường thiệt hại**. Thiệt hại của sinh viên trượt môn rất khó định lượng nhưng về nguyên tắc vẫn phát sinh trách nhiệm. → Phải có **máy dự phòng**, **biên bản bàn giao tình trạng máy có ảnh**, và **giới hạn trách nhiệm ở mức hợp lý & hợp pháp** (xem mục 8 về Luật BVQLNTD). |
| **477** | Nghĩa vụ bảo đảm giá trị sử dụng của tài sản thuê | "1. Bên cho thuê phải bảo đảm tài sản thuê **trong tình trạng như đã thoả thuận, phù hợp với mục đích thuê trong suốt thời gian cho thuê**; phải sửa chữa những hư hỏng, khuyết tật của tài sản thuê, **trừ hư hỏng nhỏ mà theo tập quán bên thuê phải tự sửa chữa**. 2. Trường hợp tài sản thuê bị giảm sút giá trị sử dụng mà **không do lỗi của bên thuê** thì bên thuê có quyền yêu cầu: a) Sửa chữa tài sản; b) **Giảm giá thuê**; c) **Đổi tài sản khác hoặc đơn phương chấm dứt** thực hiện hợp đồng và yêu cầu bồi thường thiệt hại, nếu tài sản thuê có khuyết tật mà bên thuê không biết hoặc không thể sửa chữa được mà do đó mục đích thuê không đạt được. 3. Trường hợp bên cho thuê đã được thông báo mà không sửa chữa hoặc sửa chữa không kịp thời thì bên thuê có quyền **tự sửa chữa với chi phí hợp lý** … và yêu cầu bên cho thuê thanh toán chi phí sửa chữa." | Đây là điều luật buộc startup phải **bảo trì máy, sạc pin đầy, cài sẵn phần mềm thi, test trước mỗi lượt cho thuê**. "Mục đích thuê" ở đây là **đi thi** → máy phải chạy được phần mềm thi. Nếu máy sập giữa ca thi mà không do lỗi khách → khách có quyền đòi giảm giá/đổi máy/chấm dứt + bồi thường. |
| **478** | Nghĩa vụ bảo đảm quyền sử dụng tài sản cho bên thuê | "1. Bên cho thuê phải bảo đảm **quyền sử dụng tài sản ổn định** cho bên thuê. 2. Trường hợp có **tranh chấp về quyền sở hữu** đối với tài sản thuê mà bên thuê không được sử dụng ổn định thì bên thuê có quyền đơn phương chấm dứt và yêu cầu bồi thường thiệt hại." | Laptop cho thuê **phải thuộc sở hữu hợp pháp** của startup (có hóa đơn mua). Nếu dùng máy đi mượn / máy trả góp đang thế chấp → rủi ro. |
| **479** | Nghĩa vụ bảo quản tài sản thuê | "1. Bên thuê phải bảo quản tài sản thuê, phải bảo dưỡng và sửa chữa nhỏ; **nếu làm mất, hư hỏng thì phải bồi thường**. **Bên thuê không chịu trách nhiệm về những hao mòn tự nhiên do sử dụng tài sản thuê.** 2. Bên thuê có thể tu sửa và làm tăng giá trị tài sản thuê, nếu được bên cho thuê đồng ý và có quyền yêu cầu bên cho thuê thanh toán chi phí hợp lý." | **Cơ sở pháp lý để đòi tiền khi khách làm vỡ màn hình / mất máy.** Nhưng chú ý vế sau: **không được bắt khách đền hao mòn tự nhiên** (bàn phím mòn, pin chai theo thời gian, xước nhẹ do sử dụng bình thường). Nếu hợp đồng quy định khách phải đền cả hao mòn tự nhiên → điều khoản đó trái luật. |
| **480** | Nghĩa vụ sử dụng tài sản thuê đúng công dụng, mục đích | "1. Bên thuê phải sử dụng tài sản thuê theo đúng công dụng của tài sản và **đúng mục đích đã thoả thuận**. 2. Trường hợp bên thuê sử dụng tài sản không đúng mục đích, không đúng công dụng thì bên cho thuê có quyền **đơn phương chấm dứt thực hiện hợp đồng và yêu cầu bồi thường thiệt hại**." | Nên ghi trong hợp đồng: "Mục đích thuê: **phục vụ làm bài thi tại cơ sở của Trường ĐH FPT Đà Nẵng**". Khi đó, nếu khách mang máy đi đào coin / cài phần mềm lậu / mang ra khỏi khuôn viên → có quyền chấm dứt + đòi bồi thường. |
| **481** | Trả tiền thuê | "1. Bên thuê phải trả đủ tiền thuê đúng thời hạn đã thoả thuận; nếu không có thoả thuận … thì bên thuê phải **trả tiền khi trả lại tài sản thuê**. 2. Trường hợp các bên thoả thuận việc trả tiền thuê theo kỳ hạn thì bên cho thuê có quyền đơn phương chấm dứt thực hiện hợp đồng, nếu bên thuê **không trả tiền trong ba kỳ liên tiếp**…" | Với thuê ngắn (theo ca/ngày) nên **thu tiền trước khi giao máy** và ghi rõ trong hợp đồng, tránh rơi vào mặc định "trả tiền khi trả máy". |
| **482** | Trả lại tài sản thuê | "1. Bên thuê phải trả lại tài sản thuê **trong tình trạng như khi nhận, trừ hao mòn tự nhiên** hoặc theo đúng như tình trạng đã thoả thuận; nếu **giá trị của tài sản thuê bị giảm sút** so với tình trạng khi nhận thì bên cho thuê có quyền **yêu cầu bồi thường thiệt hại, trừ hao mòn tự nhiên**. 2. Trường hợp tài sản thuê là **động sản** thì địa điểm trả lại tài sản thuê là **nơi cư trú hoặc trụ sở của bên cho thuê**, trừ trường hợp có thoả thuận khác. … 4. Khi bên thuê **chậm trả** tài sản thuê thì bên cho thuê có quyền yêu cầu bên thuê **trả lại tài sản thuê, trả tiền thuê trong thời gian chậm trả và phải bồi thường thiệt hại**; bên thuê **phải trả tiền phạt vi phạm do chậm trả tài sản thuê, nếu có thoả thuận**." | **Điều quan trọng bậc nhất cho vận hành.** Khoản 2: laptop là động sản → **địa điểm trả mặc định là trụ sở của startup** (không phải chỗ khách). Khoản 4 cho phép **3 khoản cộng dồn khi trả trễ**: (i) tiền thuê của thời gian chậm trả, (ii) bồi thường thiệt hại, (iii) **phạt vi phạm — nhưng CHỈ KHI CÓ THỎA THUẬN**. → Bắt buộc phải viết điều khoản "phạt chậm trả … VND/giờ" vào hợp đồng, nếu không sẽ **mất quyền phạt**. |

### 2.2 Ba "bẫy" hay gặp khi soạn hợp đồng thuê laptop

1. **Không ghi điều khoản phạt chậm trả** → theo Điều 482 khoản 4, chỉ đòi được tiền thuê + bồi thường thiệt hại thực tế, **không phạt được**. Phải viết rõ.
2. **Bắt đền hao mòn tự nhiên** → vi phạm Điều 479 khoản 1 và Điều 482 khoản 1 (cả hai đều có mệnh đề "trừ hao mòn tự nhiên").
3. **Không mô tả tình trạng máy khi giao** → Điều 482 khoản 1 đòi so sánh "tình trạng như khi nhận"; không có biên bản/ảnh ⇒ không chứng minh được giảm sút giá trị ⇒ không đòi được bồi thường.

### 2.3 Các điều BLDS bổ trợ cần trích trong proposal

| Điều | Tên | Nội dung (nguyên văn rút gọn) | Dùng để làm gì |
|---|---|---|---|
| **117** | Điều kiện có hiệu lực của giao dịch dân sự | "1. Giao dịch dân sự có hiệu lực khi có đủ các điều kiện sau đây: a) **Chủ thể có năng lực pháp luật dân sự, năng lực hành vi dân sự phù hợp** với giao dịch dân sự được xác lập; b) Chủ thể tham gia giao dịch dân sự **hoàn toàn tự nguyện**; c) **Mục đích và nội dung** của giao dịch dân sự **không vi phạm điều cấm của luật, không trái đạo đức xã hội**. 2. Hình thức của giao dịch dân sự là điều kiện có hiệu lực … trong trường hợp luật có quy định." | Điểm a rất quan trọng: sinh viên **dưới 18 tuổi** (có thật ở FPT, nhiều em vào ĐH lúc 17) chưa có năng lực hành vi dân sự đầy đủ → hợp đồng thuê giá trị lớn có thể bị vô hiệu. → Quy trình phải **kiểm tra ngày sinh**, với khách <18 tuổi cần người đại diện theo pháp luật đồng ý. |
| **119** | Hình thức giao dịch dân sự | "1. Giao dịch dân sự được thể hiện **bằng lời nói, bằng văn bản hoặc bằng hành vi cụ thể**." (kèm quy định giao dịch qua phương tiện điện tử dưới hình thức thông điệp dữ liệu được coi là giao dịch bằng văn bản) | Cơ sở để **ký hợp đồng điện tử trên website** thay vì giấy. Kết hợp với Luật Giao dịch điện tử 2023 (mục 8). |
| **401** | Hiệu lực của hợp đồng | "1. Hợp đồng được giao kết hợp pháp **có hiệu lực từ thời điểm giao kết**, trừ trường hợp có thỏa thuận khác hoặc luật liên quan có quy định khác." | Xác định thời điểm phát sinh nghĩa vụ (bấm "Xác nhận thuê" trên web). |
| **351** | Trách nhiệm dân sự do vi phạm nghĩa vụ | "1. Bên có nghĩa vụ mà vi phạm nghĩa vụ thì phải chịu trách nhiệm dân sự … **Vi phạm nghĩa vụ là việc bên có nghĩa vụ không thực hiện nghĩa vụ đúng thời hạn, thực hiện không đầy đủ nghĩa vụ hoặc thực hiện không đúng nội dung của nghĩa vụ.** 2. Trường hợp bên có nghĩa vụ không thực hiện đúng nghĩa vụ do **sự kiện bất khả kháng** thì **không phải chịu trách nhiệm dân sự**, trừ trường hợp có thoả thuận khác … 3. Bên có nghĩa vụ **không phải chịu trách nhiệm** nếu chứng minh được nghĩa vụ không thực hiện được là **hoàn toàn do lỗi của bên có quyền**." | Khoản 2 & 3 là **lá chắn của startup**: mất điện toàn khu vực, thiên tai (Đà Nẵng hay bão/lụt) = bất khả kháng. Khách tự cài phần mềm lạ làm hỏng máy = lỗi bên có quyền. |
| **360** | Trách nhiệm bồi thường thiệt hại do vi phạm nghĩa vụ | "Trường hợp có thiệt hại do vi phạm nghĩa vụ gây ra thì bên có nghĩa vụ phải **bồi thường toàn bộ thiệt hại**, trừ trường hợp có thỏa thuận khác hoặc luật có quy định khác." | Nguyên tắc bồi thường toàn bộ — nhưng cho phép **thỏa thuận khác** ⇒ có thể thỏa thuận giới hạn/định mức bồi thường trong hợp đồng (miễn không vi phạm Luật BVQLNTD Điều 25). |
| **419** | Thiệt hại được bồi thường do vi phạm hợp đồng | "1. Thiệt hại được bồi thường … xác định theo khoản 2 Điều này, Điều 13 và Điều 360 … 2. Người có quyền có thể yêu cầu bồi thường thiệt hại cho **lợi ích mà lẽ ra mình sẽ được hưởng** do hợp đồng mang lại. Người có quyền còn có thể yêu cầu … **chi phí phát sinh do không hoàn thành nghĩa vụ hợp đồng** mà không trùng lặp … 3. Theo yêu cầu của người có quyền, Tòa án có thể buộc người có nghĩa vụ **bồi thường thiệt hại về tinh thần** …" | Khoản 3 là rủi ro đuôi: sinh viên trượt thi vì máy hỏng có thể yêu cầu bồi thường tổn thất tinh thần (mức do Tòa quyết). → Lý do phải có **SLA + máy dự phòng + bảo hiểm rủi ro nội bộ**. |
| **584** | Căn cứ phát sinh trách nhiệm BTTH (ngoài hợp đồng) | "1. Người nào có hành vi xâm phạm … **tài sản** … của người khác mà gây thiệt hại thì phải bồi thường … 2. Người gây thiệt hại **không phải chịu trách nhiệm** … do **sự kiện bất khả kháng** hoặc **hoàn toàn do lỗi của bên bị thiệt hại** … 3. Trường hợp **tài sản gây thiệt hại** thì **chủ sở hữu, người chiếm hữu tài sản** phải chịu trách nhiệm bồi thường …" | Khoản 3: nếu **pin laptop phát nổ** gây thương tích cho khách → **chủ sở hữu (startup)** chịu trách nhiệm. ⇒ Không mua máy trôi nổi, không thay pin lô. |
| **585** | Nguyên tắc bồi thường thiệt hại | "1. Thiệt hại thực tế phải được **bồi thường toàn bộ và kịp thời**. Các bên **có thể thoả thuận về mức bồi thường, hình thức bồi thường** … 2. Người chịu trách nhiệm … **có thể được giảm mức bồi thường** nếu không có lỗi hoặc có lỗi vô ý và thiệt hại quá lớn so với khả năng kinh tế của mình. … 4. Khi bên bị thiệt hại **có lỗi** trong việc gây thiệt hại thì **không được bồi thường phần thiệt hại do lỗi của mình** gây ra. 5. Bên có quyền, lợi ích bị xâm phạm **không được bồi thường** nếu thiệt hại xảy ra do **không áp dụng các biện pháp cần thiết, hợp lý để ngăn chặn, hạn chế thiệt hại cho chính mình**." | Khoản 2 rất hữu ích khi **sinh viên làm mất máy**: em sinh viên có thể xin giảm mức bồi thường vì "thiệt hại quá lớn so với khả năng kinh tế". ⇒ Thu hồi 100% giá máy không phải lúc nào cũng khả thi ⇒ củng cố lý do dùng **ký cược** (mục 3). |
| **589** | Thiệt hại do tài sản bị xâm phạm | "Thiệt hại do tài sản bị xâm phạm bao gồm: 1. Tài sản **bị mất, bị huỷ hoại hoặc bị hư hỏng**; 2. **Lợi ích gắn liền với việc sử dụng, khai thác tài sản bị mất, bị giảm sút**; 3. **Chi phí hợp lý để ngăn chặn, hạn chế và khắc phục thiệt hại**; 4. Thiệt hại khác do luật quy định." | **Công thức tính tiền đòi khách làm hỏng/mất máy:** giá trị máy + **doanh thu cho thuê bị mất trong thời gian máy nằm xưởng** (khoản 2) + chi phí sửa/định giá (khoản 3). Đây là căn cứ để đưa "phí ngừng khai thác … VND/ngày" vào hợp đồng. |
| **597** | BTTH do người của pháp nhân gây ra | "Pháp nhân phải bồi thường thiệt hại do người của mình gây ra trong khi thực hiện nhiệm vụ được pháp nhân giao; nếu pháp nhân đã bồi thường … thì có quyền yêu cầu người có lỗi … **hoàn trả** …" | Nếu lập công ty và thuê cộng tác viên giao máy: công ty chịu trách nhiệm trước khách, rồi truy đòi CTV. |

