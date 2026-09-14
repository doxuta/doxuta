## Laptop cá nhân là thiết bị dự thi bắt buộc

Ở phần lớn trường đại học Việt Nam, chiếc laptop là công cụ học tập: thiếu nó thì bất tiện, nhưng sinh viên vẫn ngồi vào phòng thi được với giấy và bút. Ở Đại học FPT thì không. Kỳ thi cuối kỳ chạy trên phần mềm **EOS (Exam Online System)**, và phần mềm đó chạy trên **chính máy tính cá nhân của sinh viên**. Nhà trường không cấp máy cho kỳ thi; sinh viên tự mang máy tới phòng thi và tự chịu trách nhiệm về việc máy chạy được hay không [[ref:https://daihoc.fpt.edu.vn/tin-noi-bat-muc-tin-tuc/huong-dan-sinh-vien-su-dung-va-thi-tren-phan-mem-eos-tai-truong-dai-hoc-fpt/]] [[ref:https://it.fpt.edu.vn/cantho/huong-dan-cai-dat-phan-mem-thi-eos-seb/]]. Đây là dữ kiện F1 và là gốc của toàn bộ vấn đề mà ExamLap muốn giải.

Trên nền dữ kiện đó, hướng dẫn chính thức của trường đặt thêm một chuỗi ràng buộc kỹ thuật. Mỗi ràng buộc đứng riêng chỉ là một dòng hướng dẫn cài đặt; cộng lại, chúng biến chiếc laptop thành điều kiện cần tuyệt đối để dự thi.

**Bắt buộc Windows (F2).** EOS chỉ chạy trên hệ điều hành Windows; tài liệu Helpdesk khuyến cáo dùng Windows 10 để tương thích tốt nhất với phần mềm thi. Máy Mac muốn thi phải cài Windows song song bằng Bootcamp [[ref:https://it.fpt.edu.vn/cantho/huong-dan-cai-dat-phan-mem-thi-eos-seb/]] [[ref:https://it.fpt.edu.vn/cantho/huong-dan-cai-windows-tren-mac-dung-bootcamp/]].

**MacBook chip M1, M2, M3 không thi được (F3).** Bootcamp không hỗ trợ các dòng Mac chip Apple Silicon, và hướng dẫn của trường nêu thẳng rằng Mac chip M1, M2 không được hỗ trợ. Với sinh viên đã bỏ hơn hai mươi triệu mua MacBook đời mới, đây không phải bất tiện khắc phục được bằng vài thao tác cài đặt: chiếc máy đắt tiền đó đơn giản là không dùng để thi được [[ref:https://hanoi.fpt.edu.vn/tin-tuc-su-kien/huong-dan-sinh-vien-su-dung-va-thi-tren-phan-mem-eos.html]] [[ref:https://daihoc.fpt.edu.vn/tin-noi-bat-muc-tin-tuc/huong-dan-sinh-vien-su-dung-va-thi-tren-phan-mem-eos-tai-truong-dai-hoc-fpt/]].

**Safe Exam Browser, đúng phiên bản (F4).** Kỳ thi dùng kèm Safe Exam Browser, trình duyệt khoá máy trong lúc làm bài. Bản cài tải từ cổng `exam.fpt.edu.vn` và phải đúng phiên bản trường công bố; hướng dẫn còn dặn khi tìm phần mềm trong máy phải gõ từ khoá "Safe" chứ không phải "SEB" [[ref:https://it.fpt.edu.vn/cantho/huong-dan-cai-dat-phan-mem-thi-eos-seb/]] [[ref:https://lmsqn.fpt.edu.vn/hd/huong-dan-cai-dat-seb-tren-windows/]].

**Phần mềm thi phải nằm đúng thư mục (F5).** File `EOSClient.exe` chỉ khởi động được khi còn nằm trong thư mục giải nén ban đầu; kéo hoặc chép nó ra chỗ khác là phần mềm không chạy [[ref:https://it.fpt.edu.vn/cantho/huong-dan-cai-dat-phan-mem-thi-eos-seb/]] [[ref:https://it-hcm.fpt.edu.vn/articles.php?id=18]]. *[Cần kiểm chứng]* Đây là loại lỗi mà một sinh viên bình tĩnh cũng mất mười lăm phút để hiểu ra, và mười lăm phút đó thường không có vào lúc 07:20 ngày thi.

**Bài làm nằm trên ổ cứng máy sinh viên trước khi lên máy chủ (F6).** Luồng dữ liệu của EOS đi theo một chiều: đề tải từ máy chủ trường về máy cá nhân, sinh viên làm bài ở trạng thái ngoại tuyến, bài được lưu thành file trên ổ cứng máy mình, rồi mới nộp lên máy chủ ở bước cuối [[ref:https://www.studocu.vn/vn/document/truong-dai-hoc-fpt/quan-tri-kinh-doanh/huong-dan-lam-bai-thi-cuoi-ky-tren-eos-client/27055728]] [[ref:https://hanoi.fpt.edu.vn/huong-dan-sinh-vien-su-dung-va-thi-tren-phan-mem-eos.html]]. *[Cần kiểm chứng]* Tài liệu hướng dẫn của trường cũng cảnh báo rằng nếu không giải nén đúng phần mềm thi trước khi thi thì có thể gặp lỗi và mất bài, và khi máy gặp sự cố giữa ca thi thì sinh viên phải báo ngay giám thị [[ref:https://daihoc.fpt.edu.vn/tin-tuc-chung-2/huong-dan-sinh-vien-su-dung-va-thi-tren-phan-mem-eos-tai-fptu-ha-noi/]].

```
Máy chủ trường  ──(tải đề)──►  LAPTOP CÁ NHÂN của sinh viên
                                        │
                                 làm bài ngoại tuyến
                                        │
                             bài lưu thành file TRÊN Ổ CỨNG
                                 máy của sinh viên
                                        │
                                 ──(nộp bài)──►  Máy chủ trường
```
{caption: Luồng dữ liệu của một ca thi EOS. Bài làm tồn tại vật lý trên máy sinh viên trong suốt thời gian thi, nên máy hỏng giữa chừng không chỉ làm gián đoạn mà còn có nguy cơ mất bài.}

**Tai nghe có dây (F7).** Phần thi nghe của các môn tiếng Anh yêu cầu tai nghe có dây, trong khi nhiều laptop đời mới đã bỏ jack 3.5mm [[ref:https://daihoc.fpt.edu.vn/tin-tuc-chung-2/huong-dan-sinh-vien-k18-su-dung-va-thi-tren-phan-mem-eos-ky-thi-kiem-tra-tieng-anh/]]. Một chiếc máy "mượn tạm" hoàn toàn có thể qua được vòng cài đặt rồi vẫn hỏng việc ở đúng phần nghe.

Gộp bảy dữ kiện trên lại, kết luận rất gọn: **chiếc laptop là điểm chết đơn lẻ (single point of failure) của việc dự thi**. Trong kỹ thuật hệ thống, điểm chết đơn lẻ là thành phần mà khi nó hỏng thì cả hệ thống dừng, vì không có thành phần nào khác gánh thay. Ca thi EOS đúng là một hệ thống như vậy: không có máy dự phòng đặt sẵn trong phòng thi, không có phương án thi trên giấy, không có cách nào lấy bài đang làm dở ra khỏi một chiếc máy đã tắt ngóm. Sinh viên có thể học thuộc bài, có thể đến sớm ba mươi phút, có thể mang đủ giấy tờ tuỳ thân, nhưng nếu cái máy không lên nguồn thì mọi chuẩn bị đó bằng không.

:::note Cách đọc nhãn độ tin cậy
Nhóm nghiên cứu trong điều kiện chỉ truy cập được công cụ tìm kiếm, không mở trực tiếp được từng trang gốc. Vì vậy mỗi dữ kiện đều gắn nhãn: *[Đã xác minh]*, *[Cần kiểm chứng]*, *[Ước lượng của nhóm]*. Con số không nhãn trong chương này thuộc nhóm *[Đã xác minh]*.
:::

## Sáu kịch bản khiến sinh viên mất buổi thi

Từ các ràng buộc kỹ thuật ở trên, nhóm liệt kê sáu kịch bản hỏng việc. Cả sáu đều dẫn tới cùng một kết cục nếu không có máy thay thế. Cột "tần suất chủ quan" là **[Ước lượng của nhóm]**, xếp hạng tương đối theo quan sát của các thành viên nhóm đang học tại campus Đà Nẵng, **chưa có số liệu khảo sát**. Nhóm cố tình không gán tỉ lệ phần trăm cho cột này, vì gán số vào một thứ chưa đo được là bịa số.

| Kịch bản | Tần suất chủ quan | Sinh viên hiện xử lý thế nào | Kết cục |
|---|---|---|---|
| Máy hỏng đột ngột sát giờ thi (màn hình, bàn phím, ổ cứng, bo mạch) | Trung bình | Hỏi khắp nhóm chat lớp xem ai có máy rảnh; chạy ra tiệm sửa gần nhất | Không kịp. Tiệm sửa cần vài giờ đến vài ngày; nhóm chat thường trả lời sau giờ thi |
| Pin chai kèm hỏng sạc, phòng thi không đủ ổ cắm | Cao | Mượn sạc của bạn cùng dòng máy, ngồi cạnh ổ điện, vừa làm bài vừa canh pin | Thi được nhưng rủi ro cao; máy sập nguồn giữa ca thi là mất bài đang lưu trên ổ cứng |
| MacBook chip M1, M2, M3 | Cao trong nhóm dùng Mac | Mượn máy Windows của bạn cho từng ca thi, lặp lại mỗi kỳ | Phụ thuộc vào lòng tốt và lịch thi của người khác; chỉ là hoãn vấn đề, không phải giải pháp |
| Máy quá yếu hoặc lỗi hệ điều hành, không cài được Safe Exam Browser hoặc EOS | Trung bình | Gỡ ra cài lại, hỏi Helpdesk IT, cài lại Windows đêm trước ngày thi | Rủi ro cao nhất: cài lại Windows đêm trước có thể làm máy không dùng được sáng hôm sau |
| Quên mang máy hoặc mang nhầm sạc | Thấp nhưng luôn có | Chạy về phòng trọ lấy | Chỉ cứu được nếu trọ gần campus; quá 15 phút là hết cơ hội |
| Máy đang ở tiệm sửa đúng tuần thi | Trung bình, dồn vào mùa thi | Giục tiệm trả máy sớm, hoặc mượn bạn suốt tuần thi | Khó nhất trong sáu kịch bản vì cần một người bạn rảnh máy nhiều ngày liên tiếp |
{caption: Sáu kịch bản khiến sinh viên Đại học FPT không dự thi được và cách xử lý hiện nay.}
{widths: 3,2,4,4}
{note: Cột tần suất là [Ước lượng của nhóm], chưa có khảo sát. Mục tiêu của Phụ lục A là thay cột này bằng số thật.}

Điểm chung của cả sáu dòng: **cách xử lý hiện nay đều là phương án cá nhân, không có bảo đảm về thời gian**. Không kịch bản nào có một dịch vụ đứng ra cam kết "có máy chạy được trước giờ thi". Đó là khoảng trống ExamLap nhắm vào, với ba cam kết công khai: giao trước giờ thi 30 phút, đổi máy trong 15 phút nếu máy lỗi giữa ca thi, hoàn cọc tự động trong 5 phút sau khi trả máy nguyên vẹn.

## Cái giá của một buổi thi bị lỡ

Để định giá có căn cứ, nhóm phải trả lời được: mất một buổi thi thì sinh viên mất bao nhiêu tiền? Phép tính dưới đây trình bày đầy đủ để người đọc tự kiểm tra từng bước.

Học phí giai đoạn chuyên ngành tại campus Đà Nẵng là **22.120.000đ một học kỳ**, áp dụng cho cả năm học 2025–2026 và 2026–2027 [[ref:https://baodanang.vn/hoc-phi-truong-dai-hoc-fpt-2025-2026-tai-cac-co-so-tren-ca-nuoc-3151966.html]] [[ref:https://jobtest.vn/hrblog/hoc-phi-dai-hoc-fpt]]. Một học kỳ ở Đại học FPT kéo dài **4 tháng**, tương đương 15 đến 16 tuần [[ref:https://www.facebook.com/university.fpt.edu.vn/posts/1183525043803905/]] [[ref:https://hanoi.fpt.edu.vn/tu-van/thoi-gian-hoc-dai-hoc-fpt.html]]. Từ hai con số đó:

1. Chi phí học tập mỗi tuần: 22.120.000đ chia cho 16 tuần, bằng khoảng **1.383.000đ một tuần**.
2. Chi phí học tập mỗi ngày, tính theo tuần 7 ngày: 1.383.000đ chia 7, bằng khoảng **198.000đ một ngày**.
3. Giả định một học kỳ có khoảng **5 môn thi cuối kỳ**: 22.120.000đ chia 5, bằng **4.424.000đ cho một môn thi**. Đây là dữ kiện F9, nhãn **[Ước lượng của nhóm]**, và giả định "5 môn một kỳ" là giả định duy nhất trong phép tính. Nếu một sinh viên học 4 môn thì giá trị một môn tăng lên khoảng 5.530.000đ; nếu học 6 môn thì giảm còn khoảng 3.687.000đ (cả hai đều là **[Ước lượng của nhóm]**, tính bằng cách chia học phí một kỳ cho số môn). Kết luận không đổi theo hướng bất lợi cho lập luận.

Con số 4.424.000đ mới là phần tiền nhìn thấy được. Thiệt hại phi tiền tệ thường nặng hơn:

- **Chậm tiến độ và học lại.** Môn trượt phải học lại ở kỳ sau, mà mỗi năm chỉ có ba học kỳ Fall, Spring và Summer [[ref:https://daihoc.fpt.edu.vn/lo-trinh-dao-tao-cua-truong-dai-hoc-fpt/]]. Một môn học lại kéo lùi cả chuỗi môn phụ thuộc phía sau, xấu nhất là lùi thời điểm tốt nghiệp một học kỳ, đồng thời phải trả thêm tiền cho nội dung đã học.
- **Ảnh hưởng học bổng và xếp loại.** Điểm môn và điểm trung bình tích luỹ là căn cứ xét học bổng và xếp loại tốt nghiệp theo quy chế đào tạo tín chỉ của trường [[ref:https://daihoc.fpt.edu.vn/quy-che-dao-tao-dai-hoc-chinh-quy/]]. Một điểm 0 vì lý do thiết bị nằm lại trong bảng điểm suốt phần còn lại của khoá học.
- **Chi phí tâm lý.** Sinh viên mất buổi thi vì máy hỏng phải làm đơn, giải trình, chờ xét, trong lúc vẫn phải thi các môn còn lại của cùng tuần thi.

Đặt cạnh nhau, tỉ số trở nên rất chênh lệch. Một ca thi 4 giờ trên máy nhóm A của ExamLap có giá **79.000đ**; gói ngày thi hai ca là **129.000đ**; gói khẩn cấp đặt dưới 3 giờ, giao tận cổng là **179.000đ**. So với thiệt hại 4.424.000đ:

- 4.424.000đ chia 179.000đ, bằng khoảng **25 lần**.
- 4.424.000đ chia 79.000đ, bằng khoảng **56 lần**.

:::ok Tỉ lệ chi phí trên rủi ro
Thuê một máy sẵn sàng thi tốn từ **79.000đ đến 179.000đ**. Trượt một môn vì hỏng máy mất khoảng **4.424.000đ** học phí, cộng một học kỳ chậm tiến độ.
Tỉ lệ chi phí trên rủi ro nằm trong khoảng **1 : 25 đến 1 : 56**.
Một sinh viên đã chấp nhận trả 22.120.000đ mỗi học kỳ thì quyết định chi thêm 79.000đ để chắc chắn vào được phòng thi là quyết định dễ, không cần cân nhắc lâu.
:::

Cần nói rõ để lập luận không bị thổi phồng: **không phải cứ lỡ một buổi thi là mất trắng 4.424.000đ**. Sổ tay sinh viên cho biết sinh viên được thi tối đa hai lần theo lịch của trường, điểm lần một là điểm chính thức, điểm lần hai dùng khi lần một không đạt [[ref:https://daihoc.fpt.edu.vn/en/wp-content/uploads/2017/06/So-tay-sinh-vien-FUG-2016.doc]]. *[Cần kiểm chứng]* Vì vậy con số 4.424.000đ nên được hiểu là **giá trị kinh tế tối đa của một môn thi**, tức mức trần thiệt hại khi sinh viên dùng hết cơ hội thi mà vẫn không có máy. Ngay cả khi chỉ hiện thực hoá một phần, tỉ lệ vẫn nghiêng hẳn về phía thuê máy.

## Vì sao các phương án hiện có không giải quyết được

Sinh viên gặp sự cố máy vào ngày thi hiện có bốn lối thoát. Nhóm đã xem xét từng lối và thấy cả bốn đều hỏng ở một khâu.

### Mượn bạn

Đây là phương án phổ biến nhất, và bằng chứng mạnh nhất cho thấy nó phổ biến lại đến từ chính nhà trường: Đại học FPT đã xây một quy trình chính thức cho sinh viên mượn laptop của sinh viên khác **"để dùng hoặc đi thi"**, có module "ĐK Mượn máy" trên hệ thống IT của campus, sinh viên đăng nhập bằng tài khoản nội bộ, nhập mã số sinh viên của chủ máy, và **chủ máy phải đăng nhập xác nhận**; thời gian mượn tối thiểu là 60 phút [[ref:https://it-hcm.fpt.edu.vn/articles.php?news=huong-dan-muon-laptop-cua-sinh-vien-trong-truong&id=56]]. *[Cần kiểm chứng]* Không tổ chức nào bỏ công xây một module phần mềm, một quy trình xác nhận hai bước và một bài hướng dẫn riêng cho nhu cầu hiếm gặp. Sự tồn tại của quy trình này là bằng chứng nội bộ rằng **nhu cầu mượn máy để đi thi là có thật và đủ thường xuyên**.

Nhưng nguồn cung của phương án này là bạn bè, và nó đòi hỏi ba điều kiện cùng đúng một lúc: phải quen một người có máy Windows chạy được EOS, người đó không thi cùng ca, và người đó đồng ý giao chiếc máy chứa toàn bộ dữ liệu cá nhân cho người khác mang vào phòng thi. Vào mùa thi, điều kiện thứ hai gần như luôn sai vì cả lớp thi cùng lịch. Hướng dẫn còn nêu một ràng buộc vận hành: dù dùng máy người khác, thí sinh vẫn phải ngắt WiFi_Student và WiFi_Exam rồi đăng nhập lại bằng tài khoản WiFi của chính mình [[ref:https://it-hcm.fpt.edu.vn/articles.php?news=huong-dan-muon-laptop-cua-sinh-vien-trong-truong&id=56]]. *[Cần kiểm chứng]* Trang hướng dẫn này thuộc campus TP.HCM; **nhóm chưa xác minh được campus Đà Nẵng có quy trình tương đương hay không**.

### Ra tiệm cho thuê trong nội thành

Đà Nẵng đã có ít nhất bảy đơn vị cho thuê laptop [[ref:https://danang.plus/thue-laptop/]], nhưng không đơn vị nào đặt tại khu Hoà Hải. Cụm cho thuê laptop sinh viên của thành phố nằm ở Liên Chiểu, quanh Làng Đại học Đà Nẵng, cách campus Đại học FPT khoảng 8 đến 15 km [[ref:https://maytinhdinhhau.vn/dich-vu-cho-thue-laptop-tai-da-nang/]] [[ref:https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html]]. Giá công bố dao động từ 29.000đ một ngày của MIT Group [[ref:https://mitgroup.vn/cho-thue-laptop/]], 38.000đ một ngày của leminhSTORE [[ref:https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html]], đến 50.000đ một ngày của Trường Giang Computer [[ref:https://truonggiang.vn/cho-thue-laptop.html]], trong khi DH Lend công bố 50.000đ một ngày và 1.000.000đ một tháng kèm cam kết đổi máy nếu hỏng [[ref:https://danang.plus/thue-laptop/]]. Giá rẻ hơn ExamLap, nhưng ba rào cản khiến các mức giá đó vô nghĩa với tình huống sáng ngày thi:

1. **Giờ mở cửa.** leminhSTORE mở cửa từ 08:00 các ngày trong tuần [[ref:https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html]]. Ca thi sáng bắt đầu trước đó. Một sinh viên phát hiện máy hỏng lúc 06:30 không có cửa hàng nào để gõ.
2. **Giấy tờ và tiền cọc.** Mặt bằng chung của thị trường Đà Nẵng là đặt cọc bằng giá trị máy [[ref:https://thuelaptop.com.vn/dia-diem-cho-thue-laptop-tai-da-nang-gia-re.html]]; nơi thân thiện với sinh viên nhất vẫn yêu cầu cọc từ 500.000đ đến 2.000.000đ kèm căn cước công dân bản gốc, có thể kèm thẻ sinh viên, thông tin liên hệ gia đình và địa chỉ tạm trú [[ref:https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html]]. Một sinh viên năm nhất hiếm khi có sẵn hai triệu tiền mặt vào 06:30 sáng.
3. **Máy giao ra là máy trắng.** Quy trình thuê tiêu chuẩn của thị trường gồm năm bước, từ liên hệ hotline, chọn cấu hình, nộp giấy tờ, ký hợp đồng và đặt cọc, tới kiểm tra máy khi nhận [[ref:https://maytinhdinhhau.vn/dich-vu-cho-thue-laptop-tai-da-nang/]] [[ref:https://skycomputer.vn/dich-vu/cho-thue-may-tinh-laptop-tai-da-nang/]]. Không bước nào nói tới việc cài sẵn EOS Client và Safe Exam Browser đúng phiên bản rồi chạy thử. Một chiếc máy thuê "chung chung" giao cho sinh viên Đại học FPT vào ngày thi vẫn có thể không thi được.

### Mua máy mới gấp

Đây là phương án đắt nhất và chậm nhất. Chính nhà trường tư vấn cấu hình cho tân sinh viên ở mức RAM 16GB và SSD 512GB, với ví dụ máy giá hơn 12 triệu đồng và dải máy phổ biến 15 đến 25 triệu đồng [[ref:https://daihoc.fpt.edu.vn/goi-y-cau-hinh-laptop-cho-tan-sinh-vien-dai-hoc-fpt/]]. Rất ít sinh viên bỏ được khoản tiền đó trong vài giờ để cứu một ca thi, và kể cả có tiền vẫn phải tính thời gian mua máy, cài Windows, cài EOS và Safe Exam Browser, chạy thử. Mua máy là quyết định đầu tư dài hạn, không phải công cụ xử lý sự cố khẩn cấp.

### Nhà trường cho mượn máy dự phòng

Đây là phương án mà nhóm **chưa xác minh được**, và cũng là rủi ro giả định lớn nhất của toàn bộ dự án. Nhóm không tìm được tài liệu công khai nào cho biết Phòng Khảo thí hoặc Phòng IT campus Đà Nẵng có giữ máy dự phòng cho sinh viên gặp sự cố hay không. **Nếu trường đã có sẵn máy dự phòng và cho mượn miễn phí, nhu cầu thương mại mà ExamLap nhắm tới sẽ thu hẹp rất nhiều.**

Kinh nghiệm quốc tế cho thấy đây là khả năng có thật. Hầu hết đại học lớn ở nước ngoài đều vận hành chương trình cho mượn laptop với biểu phí công khai: Northern Illinois University phạt trễ 5 USD một ngày và thu 1.100 USD khi máy mất hoặc hỏng không sửa được [[ref:https://library.niu.edu/university-libraries/about/policies/laptopcirculation.shtml]]; University of Connecticut phạt 1 USD một giờ với thiết bị mượn dưới một ngày và thu 1.500 USD cho một laptop bị mất [[ref:https://library.uconn.edu/?p=967]]; MIT thu toàn bộ giá trị thay thế với thiết bị không trả [[ref:https://ist.mit.edu/loaner-equipment]]. University of Arizona Libraries luân chuyển hơn 300 thiết bị cho mượn từ năm 2003, với một nhân sự chuyên trách quản lý đội máy [[ref:https://journal.code4lib.org/articles/5876]], còn University of Michigan chạy song song ba chương trình, trong đó có chương trình cho mượn đúng bằng thời gian sửa máy cá nhân [[ref:https://its.umich.edu/computing/computers-software/tech-help/laptop-loaner-program]] [[ref:https://its.umich.edu/computing/computers-software/sites-at-home]]. Toàn bộ số liệu nhóm nước ngoài này mang nhãn *[Cần kiểm chứng]*.

Nhưng chính các chương trình đó chỉ ra vì sao một dịch vụ thương mại vẫn còn chỗ đứng. Thứ nhất, chúng **giới hạn đối tượng rất hẹp**: Stanford chỉ cho mượn với sinh viên hiện không sở hữu laptop và đang trong quá trình mua, hoặc đang sửa máy cá nhân [[ref:https://thehub.stanford.edu/borrow-equipment/loan-policies]] [[ref:https://thehub.stanford.edu/borrow-equipment/loan-process]]. Thứ hai, chúng **chạy theo lịch đặt chỗ**, không theo tình huống khẩn cấp lúc 06:30, dù các trường thừa nhận tình huống khẩn cấp là có thật: University of Michigan Flint đặt tên hẳn một chương trình là "Emergency Laptop Loan Program" [[ref:https://www.umflint.edu/ellp/]], còn RMIT xếp "laptop hỏng đột ngột mà cần cho việc học" vào danh mục đủ điều kiện nhận hỗ trợ khó khăn tài chính [[ref:https://www.rmit.edu.au/students/support-services/financial-legal-support/hardship-assistance-grants]]. Thứ ba, **không chương trình nào bảo đảm máy chạy được EOS và Safe Exam Browser**, vì đó là ràng buộc riêng của Đại học FPT.

Ở Việt Nam, mô hình gần nhất là Quỹ máy tính "Bank of Laptop" của Quỹ Dariu, cho sinh viên hoàn cảnh khó khăn mượn laptop mới trị giá khoảng 10.000.000đ trong tối đa 24 tháng, có xét duyệt hồ sơ [[ref:https://ctsv.uit.edu.vn/bai-viet/chuong-trinh-cho-sinh-vien-muon-may-tinh-mien-phi]] [[ref:https://www.sggp.org.vn/cho-sinh-vien-muon-laptop-mien-phi-post566364.html]]. Mô hình đó miễn phí, dài hạn, có xét duyệt, phục vụ tình trạng thiếu máy kinh niên. ExamLap có phí, siêu ngắn hạn theo ca thi, không xét duyệt, phục vụ sự cố đột xuất mùa thi. Hai mô hình bổ sung cho nhau chứ không cạnh tranh.

:::risk Rủi ro giả định lớn nhất phải kiểm chứng trước khi rót vốn
Nhóm **chưa xác minh được** hai điều, và cả hai đều có thể làm thay đổi căn bản mô hình kinh doanh:
1. Campus Đà Nẵng có máy dự phòng cho sinh viên mượn khi gặp sự cố ngày thi hay không.
2. Quy chế thi của Đại học FPT có cho phép mang máy thuê từ bên ngoài vào phòng thi hay không.
Cách kiểm chứng: gửi văn bản hỏi Phòng Khảo thí và Phòng IT campus Đà Nẵng, đưa văn bản trả lời vào phụ lục proposal. Đây là việc phải làm **trước** khi mua máy.
:::

## Nhu cầu này lớn tới đâu — và chỗ nào nhóm chưa biết

Nhóm không có số liệu thật về tỉ lệ sinh viên gặp sự cố máy vào ngày thi. Đây là con số quan trọng nhất của cả bản proposal, và nhóm nêu thẳng rằng nó đang là **giả định cốt lõi chưa được đo**. Mọi ước lượng doanh thu ở các chương sau đều đứng trên giả định này; nếu nó sai thì mô hình tài chính sai theo.

Thứ nhóm có hiện nay là bằng chứng gián tiếp. Chúng không thay thế được số liệu sơ cấp, nhưng cùng chỉ về một hướng:

| Bằng chứng gián tiếp | Nó nói lên điều gì |
|---|---|
| Đại học FPT xây hệ thống "ĐK Mượn máy" cho sinh viên mượn máy của nhau "để dùng hoặc đi thi" [[ref:https://it-hcm.fpt.edu.vn/articles.php?news=huong-dan-muon-laptop-cua-sinh-vien-trong-truong&id=56]] | Nhu cầu mượn máy đi thi đủ phổ biến để nhà trường phải quản lý bằng phần mềm |
| University of Michigan Flint đặt tên chương trình là "Emergency Laptop Loan Program" [[ref:https://www.umflint.edu/ellp/]] | Sự cố thiết bị đột xuất là một hạng mục nhu cầu riêng, được đặt tên và cấp ngân sách riêng |
| RMIT xếp "laptop hỏng đột ngột" vào diện được cấp hỗ trợ khó khăn [[ref:https://www.rmit.edu.au/students/support-services/financial-legal-support/hardship-assistance-grants]] | Một đại học lớn chính thức coi hỏng laptop giữa kỳ là cú sốc đủ nghiêm trọng để can thiệp tài chính |
| Stanford giới hạn cho mượn đúng hai nhóm: chưa có máy và đang sửa máy [[ref:https://thehub.stanford.edu/borrow-equipment/loan-policies]] | Xác nhận đúng hai phân khúc khách hàng mà ExamLap nhắm tới |
| Đà Nẵng đã có ít nhất bảy đơn vị cho thuê laptop [[ref:https://danang.plus/thue-laptop/]] | Có người sẵn sàng trả tiền để thuê máy; điều còn thiếu là một đơn vị định vị đúng cho sinh viên đi thi |
{caption: Năm bằng chứng gián tiếp cho thấy nhu cầu là có thật, trong khi chưa có số liệu sơ cấp.}
{widths: 5,4}

Quy mô thị trường cũng đang dựa trên ước lượng. Nhóm ước tính Đại học FPT Đà Nẵng có khoảng **4.500 đến 6.000 sinh viên**, nhãn **[Ước lượng của nhóm]**, tam giác hoá từ ba cách tính độc lập cho kết quả nhất quán; trường không công bố số sinh viên theo từng campus. Toàn hệ thống Đại học FPT có khoảng 30.000 sinh viên năm 2024, chỉ tiêu tuyển sinh 2025 là 13.677, nhãn **[Cần kiểm chứng]**. Mỗi năm học có ba học kỳ, kéo theo ba đỉnh thi cuối kỳ và ba đợt progress test, tức khoảng sáu đợt cao điểm [[ref:https://daihoc.fpt.edu.vn/lo-trinh-dao-tao-cua-truong-dai-hoc-fpt/]] [[ref:https://www.facebook.com/university.fpt.edu.vn/posts/1183525043803905/]]. Nhóm chưa lấy được lịch thi cuối kỳ chính thức của campus Đà Nẵng; cách lấy là chụp màn hình mục "Xem lịch thi" trên cổng FAP của chính thành viên nhóm [[ref:https://it.fpt.edu.vn/cantho/huong-dan-he-thong-academic-portal-fap/]].

Vì vậy, trước khi rót 93.250.000đ vốn đầu tư ban đầu, nhóm đề xuất chạy **khảo sát sơ cấp 150 đến 200 sinh viên** Đại học FPT Đà Nẵng. Với cỡ mẫu 200 trên quy mô ước tính 5.000 sinh viên, sai số khoảng ±7% ở độ tin cậy 95% **[Ước lượng của nhóm]**. Bộ câu hỏi đầy đủ, cách chọn mẫu và ngưỡng ra quyết định nằm ở **Phụ lục A**. Ba câu chốt: bạn dùng máy gì để thi EOS; trong 12 tháng qua bạn có gặp sự cố máy trong vòng 48 giờ trước giờ thi không; bạn sẵn sàng trả bao nhiêu cho một ca thi với máy đã bảo đảm chạy được.

Nhóm đặt sẵn ngưỡng ra quyết định để khảo sát không thành thủ tục hình thức: nếu tỉ lệ sinh viên từng gặp sự cố máy sát giờ thi trong 12 tháng qua **dưới 5%**, nhóm sẽ thu hẹp đội máy năm đầu hoặc chuyển trọng tâm sang gói thuê tháng cho đồ án và thực tập, thay vì giữ nguyên kế hoạch 10 máy.

:::warn Bốn giả định phải kiểm chứng trước khi triển khai
1. **Tỉ lệ sinh viên gặp sự cố máy ngày thi.** Hiện là giả định thuần tuý, chưa có số. Khắc phục bằng khảo sát 150–200 sinh viên (Phụ lục A).
2. **Trường có máy dự phòng cho mượn hay không.** Nếu có, nhu cầu thương mại thu hẹp mạnh. Khắc phục bằng văn bản hỏi Phòng Khảo thí campus Đà Nẵng.
3. **Quy chế thi có cho phép dùng máy thuê ngoài hay không.** Nếu cấm, mô hình phải điều chỉnh căn bản. Khắc phục bằng xác nhận bằng văn bản từ Phòng Khảo thí.
4. **Số sinh viên thật của campus Đà Nẵng.** Con số 4.500–6.000 là ước lượng của nhóm. Khắc phục bằng cách xin số liệu từ Phòng Công tác Sinh viên campus Đà Nẵng.
Bốn việc trên đều làm được trong vòng hai đến ba tuần và tốn gần như không đồng nào. Nhóm coi đây là điều kiện tiên quyết, không phải việc làm thêm cho đẹp hồ sơ.
:::
