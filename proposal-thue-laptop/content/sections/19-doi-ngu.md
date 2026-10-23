## Cơ cấu nhóm

Chương 14 đã chia vai theo hạng mục lập trình. Bảng dưới chia vai theo trách nhiệm vận hành cả năm, phần còn lại sau khi phần mềm chạy xong. Mỗi vai có một người chịu trách nhiệm cuối cùng, vì sáu đợt thi mỗi năm rơi đúng lúc chính các thành viên cũng đang thi [[ref:https://www.facebook.com/university.fpt.edu.vn/posts/1183525043803905/]] [[ref:https://daihoc.fpt.edu.vn/lo-trinh-dao-tao-cua-truong-dai-hoc-fpt/]].

<<<landscape>>>

| Vai | Người | Trách nhiệm cuối cùng | Kỹ năng bắt buộc | Giờ/tuần thường | Giờ/tuần mùa thi |
|---|---|---|---|---|---|
| **V1 Điều phối vận hành** | …………… | Lịch thi và lịch trực, gán máy, điều phối giao nhận, quản 3 đến 5 cộng tác viên điểm; chịu trách nhiệm về cam kết giao trước giờ thi 30 phút | Lập lịch, xử lý tình huống gấp, nói chuyện được với khách đang hoảng | 10 | 25 |
| **V2 Kỹ thuật nền tảng** | …………… | Kho mã, module `booking/` và `billing/`, phát hành, máy chủ, sao lưu `pg_dump` hằng ngày, diễn tập khôi phục hằng tháng | PostgreSQL và SQL viết tay, một khung web phía máy chủ, Docker, GitHub Actions | 12 | 18 |
| **V3 Kỹ thuật thiết bị** | …………… | Ảnh hệ điều hành chuẩn có sẵn EOS Client và Safe Exam Browser, BitLocker, mật khẩu BIOS, chặn khởi động USB, MDM check-in mỗi 15 phút, kiểm 12 điểm, ghi `maintenance_logs` và `battery_health_pct` | Nhân bản Windows, phần cứng laptop doanh nghiệp, đo sức khoẻ pin, thay linh kiện cơ bản | 8 | 20 |
| **V4 Khách hàng và kênh** | …………… | Trực Zalo và điện thoại, khảo sát nhu cầu, nội dung, mã giới thiệu `orders.referral_code`, trả lời khiếu nại trong 24 giờ | Viết tiếng Việt gọn và lịch sự, chịu được tin nhắn lúc 23:00, đọc được số liệu phễu | 8 | 16 |
| **V5 Tài chính và kiểm soát** | …………… | Đối soát bảng `payments`, hoàn cọc, hợp đồng điện tử, hồ sơ hộ kinh doanh, rà `audit_logs`, giữ biểu phí khớp với `pricing_rules` | Kế toán cơ bản, đọc được hợp đồng, tính được điểm hoà vốn | 6 | 10 |
{caption: Năm vai vận hành, mỗi vai một người chịu trách nhiệm cuối cùng, kèm số giờ cam kết trong tuần thường và tuần thi.}
{widths: 3,2,8,6,2,2}
{right: 5,6}
{note: Tổng công cả nhóm khoảng **2.830 giờ mỗi năm**, bằng 40 tuần × 44 giờ cộng 12 tuần mùa thi × 89 giờ **[Ước lượng của nhóm]**.}

<<<portrait>>>

Phân quyền nằm trong cơ sở dữ liệu chứ không nằm trong trí nhớ. Nguyên tắc cứng ở Chương 6 là không ai tự mình khoá được máy đang ở trong tay khách, nên chỉ V1 và V5 giữ quyền duyệt, còn V3 là người thường phải xin lệnh.

```sql
-- Ghi phân công thành dữ liệu để kiểm toán được
INSERT INTO users (email, full_name, role) VALUES
  ('……………@fpt.edu.vn', '……………', 'owner'),   -- V1 điều phối vận hành
  ('……………@fpt.edu.vn', '……………', 'admin'),   -- V2 kỹ thuật nền tảng
  ('……………@fpt.edu.vn', '……………', 'staff'),   -- V3 kỹ thuật thiết bị
  ('……………@fpt.edu.vn', '……………', 'staff'),   -- V4 khách hàng và kênh
  ('……………@fpt.edu.vn', '……………', 'admin');   -- V5 tài chính và kiểm soát

-- Người xin lệnh khoá máy không bao giờ là người duyệt lệnh đó
ALTER TABLE device_lock_requests
  ADD CONSTRAINT lock_two_person_rule
  CHECK (approved_by IS NULL OR approved_by <> requested_by);

-- Bảng kiểm đầu mỗi tháng: ai đã duyệt bao nhiêu lệnh khoá
SELECT u.full_name, u.role, count(r.id) AS so_lenh_da_duyet
FROM users u
LEFT JOIN device_lock_requests r ON r.approved_by = u.id
WHERE u.role IN ('owner', 'admin')
GROUP BY u.full_name, u.role
ORDER BY so_lenh_da_duyet DESC;
```
{caption: Ba câu lệnh biến bảng phân công ở trên thành ràng buộc mà hệ thống tự bắt buộc thi hành.}

## Vì sao nhóm này làm được

Bốn lợi thế của nhóm đều kiểm chứng được. Một, nhóm thi chính kỳ thi đó: các thành viên đã cài EOS Client, đã tải Safe Exam Browser từ `exam.fpt.edu.vn`, đã tự gặp lỗi phần mềm thi. Hai, cam kết đổi máy trong 15 phút chỉ thực hiện được khi người và máy cùng đứng tại Hoà Hải, còn bảy đơn vị cho thuê hiện có đều cách 8 đến 15 km. Ba, nhóm vào được nhóm lớp và nhóm khu trọ, trong khi quy mô cần đạt chỉ khoảng 1,1% đến 1,4% sinh viên campus mỗi đợt [Ước lượng của nhóm]. Bốn, chi phí kho gần bằng không nếu dùng phòng trọ mà một thành viên đã thuê: phòng trọ quanh FPT City giá 3.200.000đ mỗi tháng [[ref:https://troplus.vn/phong-tro/cho-thue-phong-tro-full-noi-that-gan-fpt-city-hoa-hai-ngu-hanh-son-da-nang-gia-chi-32-trieuthang]] [[ref:https://phongtro123.com/tinh-thanh/da-nang/quan-ngu-hanh-son]], còn mặt bằng 30 m² tại Ngũ Hành Sơn tới 15.000.000đ [[ref:https://mogi.vn/da-nang/quan-ngu-hanh-son/thue-mat-bang-cua-hang-shop]]. Định phí toàn mô hình chỉ 2.800.000đ mỗi tháng, nên lợi thế thứ tư đồng thời là ràng buộc: thuê mặt bằng thương mại là làm sụp mô hình.

Chỗ thiếu cũng phải nói thẳng. Nhóm chưa từng vận hành dịch vụ có tài sản thật rời khỏi tay mình, nên bù bằng đợt chạy thử 3 máy giới hạn 12 đơn vào tháng 10/2026. Nhóm chưa có quan hệ nhà cung cấp, nên ba máy đầu mua ở hai cửa hàng khác nhau để so bảo hành, và điều kiện chọn nguồn chính là cam kết sửa trong 24 giờ bằng văn bản. Nhóm cũng chưa có vốn: 93.250.000đ chia đều năm người là **18.650.000đ mỗi người**, khoảng 84% một học kỳ học phí 22.120.000đ [[ref:https://baodanang.vn/hoc-phi-truong-dai-hoc-fpt-2025-2026-tai-cac-co-so-tren-ca-nuoc-3151966.html]].

Còn một con số không nên giấu. Quy 2.830 giờ công theo mức 25.000đ mỗi giờ, nằm trong dải lương bán thời gian tại Đà Nẵng [[ref:https://vn.joboko.com/blog/luong-part-time-nwi5750]] và trên sàn lương tối thiểu giờ vùng II năm 2026 là 22.700đ [[ref:https://luatvietnam.vn/lao-dong-tien-luong/muc-luong-toi-thieu-vung-tai-thanh-pho-da-nang-nam-2026-562-105277-article.html]] [[ref:https://thuvienphapluat.vn/phap-luat-doanh-nghiep/bai-viet/muc-luong-toi-thieu-vung-thanh-pho-da-nang-tu-01-01-2026-15957.html]], thì công nhóm năm đầu trị giá khoảng 70.700.000đ, gấp gần năm lần lợi nhuận sau thuế 14.442.672đ **[Ước lượng của nhóm]**, tức khoảng 5.100đ mỗi giờ. Nhóm chấp nhận vì đó là năm mua bằng chứng, nhưng không gọi nó là mô hình đã có lãi cho người làm.

## Nguồn lực đề nghị

| Nguồn lực | Quy mô đề nghị | Dùng vào việc gì | Nếu không có |
|---|---|---|---|
| Vốn cổng 1 | **3.550.000đ**, trần 5.000.000đ | Hồ sơ hộ kinh doanh, tên miền, một tháng máy chủ, in khảo sát | Năm thành viên tự góp, mỗi người 710.000đ |
| Vốn cổng 2 | **22.690.000đ** | 3 máy chạy thử, phụ kiện, ổ cứng lưu ảnh hệ điều hành chuẩn | Hoãn chạy thử sang đợt thi sau, mất một quý |
| Vốn cổng 3 | **68.010.000đ** | 7 máy còn lại, tủ sạc, bàn kiểm máy, bản quyền Windows 11 Pro, dự phòng 5% | Giữ 3 máy, chỉ bán gói tháng, tối đa 12 đơn mỗi đợt |
| Không gian trong trường | Tủ khoá khoảng 2 m² và một bàn kiểm máy, gần khu vực thi | Kho trung chuyển trong sáu đợt thi, rút thời gian đổi máy xuống dưới 15 phút | Dùng phòng trọ làm kho, thời gian đổi máy phụ thuộc quãng đường xe máy |
| Xác minh quy chế thi | Một văn bản trả lời hai câu hỏi, trước **30/09/2026** | Trường có bố trí máy dự phòng miễn phí ngày thi không; quy chế có cho thí sinh dùng máy không thuộc sở hữu mình không | Nhóm không được mở cổng 2. Đây là điều kiện dừng M1 và M2 ở Chương 18 |
| Cố vấn | Một giảng viên khối kinh doanh hoặc công nghệ, họp 60 phút mỗi tháng | Phản biện số liệu, chỉ đầu mối Phòng Công tác Sinh viên và Phòng Khảo thí | Nhóm tự đi hỏi, thời gian xin số liệu kéo dài |
{caption: Sáu nguồn lực nhóm đề nghị, xếp theo mức độ nhóm không thể tự lo được.}
{widths: 3,3,7,6}

Hai câu hỏi xác minh quy chế thi quan trọng hơn tiền. Đã có trường đại học tại Việt Nam cho sinh viên mượn máy tính miễn phí qua Phòng Công tác Sinh viên [[ref:https://ctsv.uit.edu.vn/bai-viet/chuong-trinh-cho-sinh-vien-muon-may-tinh-mien-phi]] [[ref:https://www.sggp.org.vn/cho-sinh-vien-muon-laptop-mien-phi-post566364.html]]. Nếu Đại học FPT Đà Nẵng đã có đủ máy dự phòng miễn phí cho ngày thi thì thị trường bán lẻ không tồn tại, và nhóm chuyển sang đề nghị vận hành chính đội máy đó cho nhà trường. Về vốn ngoài, nhóm nhắm vào bốn cuộc thi dưới đây, nhưng không kế hoạch nào ở Chương 18 phụ thuộc vào việc thắng giải.

<<<landscape>>>

| Cuộc thi | Đơn vị tổ chức | Giải thưởng đã công bố | Vì sao phù hợp | Nhãn |
|---|---|---|---|---|
| **FPT Biz Talent** | Trường Đại học FPT | Tổng **260.000.000đ** tiền mặt chia nhiều giải, kèm chuyến trải nghiệm Singapore cho quán quân mỗi bảng; bảng A dành cho sinh viên đại học và cao đẳng [[ref:https://daihoc.fpt.edu.vn/tin-noi-bat-muc-tin-tuc/fpt-biz-talent-2025-truong-dh-fpt-kien-tao-the-he-doanh-nhan-tre/]] [[ref:https://www.vista.gov.vn/vi/news/khoi-nghiep-doi-moi-sang-tao/khoi-dong-cuoc-thi-khoi-nghiep-quy-mo-toan-quoc-fpt-biz-talent-2025-uom-mam-tai-nang-doanh-nhan-doi-moi-sang-tao-tuong-lai-11452.html]] [[ref:https://mst.gov.vn/fpt-biz-talent-2025-tim-kiem-va-uom-mam-the-he-doanh-nhan-doi-moi-sang-tao-viet-nam-197250616201306032.htm]] | Sân nhà, chủ đề là mô hình kinh doanh ứng dụng công nghệ; quán quân 2025 là dự án giáo dục ứng dụng trí tuệ nhân tạo [[ref:https://vnexpress.net/sinh-vien-fptu-neu-thang-giai-khoi-nghiep-nho-ung-dung-ai-vao-giao-duc-4939846.html]] [[ref:https://chungta.vn/cong-nghe/du-an-giao-duc-ung-dung-tri-tue-nhan-tao-dang-quang-tai-fpt-biz-talent-2025-1140285.html]] | [Cần kiểm chứng] |
| **Startup Wheel** | BSSC | Giải Nhất tổng trị giá **400.000.000đ**, trong đó **hiện kim 150.000.000đ**; Top 5 được trưng bày miễn phí tại InnoEx, trị giá 2.000 USD [[ref:https://startupwheel.vn/vi/giai-thuong/]] [[ref:https://startupwheel.vn/vi/top-100-startup-wheel-2026/]] | Riêng phần hiện kim đủ mua 23 máy nhóm A theo đơn giá 6.500.000đ **[Ước lượng của nhóm]**, gần trọn đội máy năm thứ hai | [Cần kiểm chứng] |
| **SV-STARTUP lần VIII** | Bộ Giáo dục và Đào tạo | Cơ cấu 2026 gồm 15 giải Nhất, 30 giải Nhì, 55 giải Ba, 34 giải Khuyến khích [[ref:https://tuoitre.vn/15-du-an-khoi-nghiep-cua-hoc-sinh-sinh-vien-gianh-giai-nhat-sv-startup-2026-20260419203319353.htm]]; tiền thưởng 2026 chưa công bố, tham chiếu 2025 là 15.000.000đ cho giải Nhất mỗi lĩnh vực [[ref:https://www.vista.gov.vn/vi/news/cac-linh-vuc-khoa-hoc-va-cong-nghe/khoi-nguon-sang-tao-tre-tai-sv-startup-2025-11260.html]] | Lĩnh vực khuyến khích gồm giáo dục và kinh doanh tạo tác động xã hội; định hướng 2026 "Làm thật, Thi thật" ưu tiên đội đã có khách hàng thật [[ref:https://vjst.vn/sv-startup-2026-chuyen-bien-ro-net-tu-y-tuong-sang-san-pham-tu-phong-trao-sang-hieu-qua-thuc-chat-86335.html]] [[ref:https://doanhnhan.congly.vn/sv-startup-2026-lam-that-thi-that-hieu-qua-thuc-chat.html]] | [Cần kiểm chứng] |
| Tuổi Trẻ Startup Award | Báo Tuổi Trẻ | Cơ cấu giải chưa công bố tại thời điểm viết [[ref:https://daidoanket.vn/khoi-dong-giai-thuong-tuoi-tre-startup-award-2026.html]] | Giá trị truyền thông lớn hơn giá trị vốn | [Cần kiểm chứng] |
{caption: Bốn cuộc thi khởi nghiệp nhóm dự kiến nộp hồ sơ, kèm giá trị giải thưởng đúng như nguồn đã công bố.}
{widths: 3,3,10,8,2}

<<<portrait>>>

:::warn Điều nhóm chưa tra được
**Không tìm được hạn nộp hồ sơ của bất kỳ cuộc thi nào ở trên**; mọi nguồn thu được đều là tin đưa sau khi trao giải. Việc đầu tiên của vai V5 là hỏi Phòng Công tác Sinh viên campus Đà Nẵng. Chương trình hỗ trợ của Vườn ươm doanh nghiệp Đà Nẵng cũng chưa tra được.
Giải thưởng **không** nằm trong bảng dòng tiền ở Chương 15. Nếu thắng, tiền đi thẳng vào cổng 3 hoặc vào đội máy năm thứ hai.
:::

## Điều nhóm cam kết

Sáu cam kết dưới đây đều kiểm chứng được bằng một tài liệu hoặc một truy vấn.

1. **Chỉ mua máy sau khảo sát.** Cổng 2 chỉ mở khi có ít nhất 150 phản hồi từ email `@fpt.edu.vn` và 40 sinh viên vào danh sách chờ. Kiểm chứng: hoá đơn mua máy phải đề ngày sau ngày chốt khảo sát.
2. **Không giữ giấy tờ tuỳ thân của khách**, gồm căn cước, thẻ sinh viên và bằng lái. Kiểm chứng: điều khoản có trong mẫu hợp đồng ở phụ lục và trong biên bản bàn giao.
3. **Công khai biểu phí đầy đủ**, kể cả phí trả trễ 20.000đ mỗi 30 phút, trần 200.000đ mỗi ngày. Mỗi lần đổi giá ghi một dòng mới vào `pricing_rules` kèm `valid_from`, không sửa hồi tố.
4. **Hoàn tiền toàn bộ nếu giao trễ khiến khách lỡ thi**: 100% tiền thuê và toàn bộ tiền cọc, không trừ khoản nào. Kiểm chứng: so `handovers.signed_at` với mốc trước giờ thi 30 phút của ca thi đó.
5. **Không dùng tiền cọc của khách làm vốn lưu động.** Kiểm chứng: số dư tài khoản cọc luôn lớn hơn hoặc bằng tổng cọc đang giữ trong bảng `orders`.
6. **Công bố số thật sau mỗi đợt thi, kể cả số xấu**: lượt hoàn tất, lượt giao trễ, lượt đổi máy, số máy mất. Đội máy chỉ mở rộng khi các số đó đạt ngưỡng ở Chương 18.

## Kết luận

Vấn đề là có thật và đã được chứng minh tới một mức cụ thể. Đã xác minh được rằng kỳ thi cuối kỳ của Đại học FPT chạy bằng phần mềm EOS trên máy cá nhân của sinh viên, rằng phần mềm đó bắt buộc Windows, rằng MacBook chip M1 trở lên không cài được Bootcamp nên không thi được, và rằng phần thi nghe cần tai nghe có dây. Một môn thi trị giá khoảng 4.424.000đ **[Ước lượng của nhóm]**, suy từ học phí 22.120.000đ mỗi học kỳ [[ref:https://baodanang.vn/hoc-phi-truong-dai-hoc-fpt-2025-2026-tai-cac-co-so-tren-ca-nuoc-3151966.html]], nên một ca thuê 79.000đ đứng trước rủi ro đó theo tỉ lệ khoảng 1 trên 25 đến 1 trên 56. Điều **chưa** chứng minh được là tần suất: mỗi đợt thi có bao nhiêu sinh viên thực sự hỏng máy. Khảo sát ở cổng 1 phải trả lời câu đó trước khi tiêu đồng vốn thứ hai.

Giải pháp không phải là cho thuê laptop, vì bảy đơn vị tại Đà Nẵng đã làm việc đó, có nơi từ 29.000đ mỗi ngày. Thứ nhóm bán là **máy sẵn sàng thi**: máy Windows đã cài sẵn EOS Client và Safe Exam Browser, đã chạy thử, kèm tai nghe có dây, sạc đầy, dữ liệu người dùng trước đã xoá sạch. Ba điểm khác biệt đo được là giao trước giờ thi 30 phút, đổi máy trong 15 phút, hoàn cọc trong 5 phút, và cả ba chỉ khả thi khi người và máy đứng tại Hoà Hải. Đi kèm là nguyên tắc cọc thấp và danh tính mạnh: cọc 300.000đ, đổi lại bằng eKYC, email trường và năm lớp phòng thủ tài sản ở Chương 6.

Dự án đáng làm nếu bốn điều kiện cùng đúng: nhà trường không bố trí sẵn đủ máy dự phòng miễn phí, quy chế thi cho phép dùng máy không thuộc sở hữu thí sinh, khảo sát đạt ngưỡng cổng 1, và đợt chạy thử ba máy đạt ít nhất 9 lượt hoàn tất mà không lượt nào giao trễ. Điều kiện dừng cũng đã viết ra trước: nếu đến 30/04/2027, sau hai kỳ thi cuối kỳ, luỹ kế lợi nhuận sau thuế vẫn thấp hơn âm 1.491.528đ, nhóm thanh lý toàn bộ đội máy trong 60 ngày thay vì bơm thêm tiền. Kịch bản thận trọng cho âm 14.565.301đ, cơ sở cho 14.442.672đ, hoàn vốn toàn bộ ở tháng thứ 27. Đây là một dự án nhỏ, hoàn vốn chậm, sống nhờ việc nhóm đứng ngay tại chỗ.

:::ok Lời đề nghị của nhóm
Nhóm đề nghị ba việc, theo thứ tự thời gian.
**Một**, giúp nhóm có văn bản trả lời của Phòng Khảo thí cho hai câu hỏi ở mục Nguồn lực đề nghị, **trước 30/09/2026**; không có nó, nhóm tự dừng ở cổng 1.
**Hai**, chấp thuận cho nhóm dự thi FPT Biz Talent và SV-STARTUP lần VIII với hồ sơ này, kèm đầu mối để hỏi hạn nộp.
**Ba**, cấp một chỗ để khoảng 2 m² trong khuôn viên và một cố vấn họp 60 phút mỗi tháng.
Nhóm **không** xin cấp vốn: 93.250.000đ vốn đầu tư được giải ngân qua ba cổng ở Chương 18, cổng đầu 3.550.000đ do năm thành viên tự góp, và mỗi cổng sau chỉ mở khi cổng trước trả đủ số liệu đã định ngưỡng.
:::
