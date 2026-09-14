## Sản phẩm: một chiếc máy đã sẵn sàng thi, không phải một chiếc laptop

ExamLap không bán quyền sử dụng một chiếc laptop trong một khoảng thời gian. ExamLap bán **một chiếc máy đã được đưa về đúng trạng thái để ngồi vào phòng thi EOS và bấm nộp bài**. Sự khác biệt này quyết định toàn bộ quy trình vận hành, cơ cấu giá và cả lý do khách chịu trả tiền.

Rào cản thật của "laptop đi thi" nằm ở phần mềm chứ không nằm ở phần cứng. Trường Đại học FPT hướng dẫn rõ rằng máy thi **bắt buộc chạy Windows** và sinh viên nên chạy thử phần mềm thi trước ngày thi [[ref:https://daihoc.fpt.edu.vn/tin-noi-bat-muc-tin-tuc/huong-dan-sinh-vien-su-dung-va-thi-tren-phan-mem-eos-tai-truong-dai-hoc-fpt/]]. Tài liệu hỗ trợ kỹ thuật còn cảnh báo file `EOSClient.exe` chỉ khởi động được khi nằm nguyên trong thư mục giải nén ban đầu [[ref:https://it.fpt.edu.vn/cantho/huong-dan-cai-dat-phan-mem-thi-eos-seb/]], còn máy Mac chip M1 trở lên không cài được Bootcamp nên không dự thi EOS được [[ref:https://hanoi.fpt.edu.vn/tin-tuc-su-kien/huong-dan-sinh-vien-su-dung-va-thi-tren-phan-mem-eos.html]].

Một chiếc laptop thuê "chung chung" giao lúc 06:30 sáng ngày thi vì thế vẫn có thể thi không được. Danh sách dưới đây là định nghĩa vận hành của cụm từ "máy sẵn sàng thi": mỗi máy phải qua đủ chín mục này trước khi được đưa vào trạng thái cho thuê.

| # | Hạng mục bắt buộc | Vì sao hạng mục này tồn tại |
|---|---|---|
| 1 | Windows bản quyền, đã tắt cập nhật tự động và lịch khởi động lại | EOS bắt buộc hệ điều hành Windows; máy Mac chip M1/M2/M3 không cài được Bootcamp nên không thi được [[ref:https://it.fpt.edu.vn/cantho/huong-dan-cai-windows-tren-mac-dung-bootcamp/]] |
| 2 | EOS Client nằm đúng thư mục giải nén gốc, không copy file ra ngoài | Nhà trường cảnh báo copy file ra khỏi thư mục ban đầu thì phần mềm thi không khởi động được [[ref:https://it.fpt.edu.vn/cantho/huong-dan-cai-dat-phan-mem-thi-eos-seb/]] |
| 3 | Safe Exam Browser đúng phiên bản, tải từ `exam.fpt.edu.vn` | Trường phát hành bản cài đặt riêng cho kỳ thi; cài bản tải trôi nổi trên mạng có thể không khớp cấu hình [[ref:https://lmsqn.fpt.edu.vn/hd/huong-dan-cai-dat-seb-tren-windows/]] |
| 4 | Đã chạy thử trọn một vòng EOS và SEB, có ghi ngày test trên nhãn máy | Trường khuyến cáo sinh viên chạy thử trước ngày thi; một máy chưa test mà hỏng vào giờ G còn tệ hơn không có máy [[ref:https://daihoc.fpt.edu.vn/tin-noi-bat-muc-tin-tuc/huong-dan-sinh-vien-su-dung-va-thi-tren-phan-mem-eos-tai-truong-dai-hoc-fpt/]] |
| 5 | Có jack 3.5mm và kèm sẵn tai nghe có dây | Phần thi nghe cần tai nghe có dây, trong khi nhiều laptop đời mới đã bỏ jack 3.5mm [[ref:https://daihoc.fpt.edu.vn/tin-noi-bat-muc-tin-tuc/huong-dan-sinh-vien-su-dung-va-thi-tren-phan-mem-eos-tai-truong-dai-hoc-fpt/]] |
| 6 | Webcam và micro đã kiểm tra hoạt động | Cần cho các ca thi có giám sát qua camera và các môn có phần nói |
| 7 | Pin trên 80% dung lượng thực, kèm sạc | Bài thi được lưu thành file trên ổ cứng máy sinh viên rồi mới nộp lên máy chủ, nên mất điện giữa chừng là rủi ro mất bài [[ref:https://daihoc.fpt.edu.vn/tin-tuc-chung-2/huong-dan-sinh-vien-su-dung-va-thi-tren-phan-mem-eos-tai-fptu-ha-noi/]] |
| 8 | Dữ liệu người dùng trước đã xoá sạch, không còn tài khoản cá nhân nào đăng nhập | Máy còn tài khoản cũ vừa vi phạm quyền riêng tư của khách trước, vừa có thể bị hiểu là dấu hiệu gian lận trong phòng thi |
| 9 | Đã kiểm tra kết nối wifi của trường, hướng dẫn sinh viên đăng nhập bằng tài khoản của chính mình | Hướng dẫn mượn máy nội bộ của trường yêu cầu ngắt WiFi_Student và WiFi_Exam rồi đăng nhập lại bằng tài khoản wifi của chính người thi [[ref:https://it-hcm.fpt.edu.vn/articles.php?news=huong-dan-muon-laptop-cua-sinh-vien-trong-truong&id=56]] |
{caption: Chín hạng mục bắt buộc của một máy sẵn sàng thi, kèm lý do tồn tại của từng hạng mục.}
{widths: 1,5,9}

Chín mục trên là bản địa hoá của một thông lệ đã có ở nơi khác. Trường Luật Drexel tại Mỹ chỉ cho sinh viên dùng máy mượn khi đã cài bản phần mềm khảo thí mới nhất **và đã nộp thành công một bài thi thử** [[ref:https://drexel.edu/law/studentLife/studentAffairs/policies_procedures/~/media/Files/law/Student%20Life/Office%20of%20Student%20Affairs/Policies%20and%20Procedures/Loaner-Laptop-Policies.ashx]]. Với họ, "máy chạy được" là điều kiện phải chứng minh trước, không phải điều mặc định.

:::note Nhãn "Đã test EOS và SEB ngày dd/mm/yyyy"
Mỗi máy mang một nhãn ghi ngày chạy thử gần nhất, hiển thị đồng thời trên trang chọn máy của website và trên tem dán mặt máy.
Đây là tín hiệu niềm tin mạnh nhất mà ExamLap có, vì không đơn vị cho thuê nào ở Đà Nẵng đang cung cấp thông tin này.
:::

![Vòng đời một thiết bị trong đội máy ExamLap, từ lúc nhập máy đến lúc thanh lý, trong đó bước chuẩn bị máy sẵn sàng thi là bước lặp lại sau mỗi lượt thuê.](assets/diagrams/03-vong-doi-thiet-bi.png){w=13}{src: Nguồn: nhóm tác giả.}

:::warn Giả định phải kiểm chứng trước khi triển khai
Nhóm chưa tìm được văn bản công khai nào của Trường Đại học FPT nói rõ sinh viên có được phép mang máy thuê từ bên ngoài vào phòng thi hay không.
Đây là giả định rủi ro nhất của toàn bộ mô hình. Việc đầu tiên phải làm là xin xác nhận bằng văn bản từ Phòng Khảo thí campus Đà Nẵng.
:::

## Đơn vị bán hàng là ca thi, không phải ngày

Toàn bộ thị trường cho thuê laptop Việt Nam bán theo ngày, tuần, tháng hoặc năm. Đơn vị thời gian ngắn nhất được niêm yết là **một ngày**, và nhóm không tìm được đơn vị nào có gói theo giờ hay theo buổi [[ref:https://skylap.vn/dich-vu-cho-thue/cho-thue-laptop-dell-van-phong/]] [[ref:https://ictsaigon.com.vn/cho-thue-laptop-hp-elitebook-9480m]]. Đơn vị gần nhất về mặt thông điệp là một trang "cho thuê laptop thi cử" ở Thành phố Hồ Chí Minh, nhưng ngay trong bài họ cũng viết là "thuê theo tuần, theo tháng hay trọn mùa thi đều được" [[ref:https://phuongnamco.com/cho-thue-laptop-thi-cu-giai-phap-huu-ich-cho-sinh-vien-mua-thi/]].

Cấu trúc giá của cả ngành được thiết kế để **thưởng cho khách thuê dài và phạt khách thuê ngắn**. Một bảng giá điển hình: 49.000đ một ngày, 300.000đ một tuần, 600.000đ một tháng [[ref:https://ictsaigon.com.vn/cho-thue-laptop-hp-elitebook-9480m]]. Quy về đơn giá ngày, gói tháng chỉ còn khoảng 41% đơn giá của gói một ngày.

| Gói của thị trường | Giá niêm yết | Quy về đơn giá mỗi ngày | Chỉ số so với gói 1 ngày |
|---|---|---|---|
| 1 ngày | 49.000đ | 49.000đ | 100% |
| 1 tuần | 300.000đ | khoảng 42.900đ | 87% |
| 1 tháng | 600.000đ | khoảng 20.000đ | 41% |
{caption: Cấu trúc giá điển hình của thị trường cho thuê laptop, tính lại về đơn giá mỗi ngày.}
{right: 2,3,4}
{note: Số liệu lấy từ bảng giá công bố của ICT Sài Gòn và SKYLAP. Phần quy đổi là tính toán của nhóm [Ước lượng của nhóm].}

Nhưng nhu cầu thật của sinh viên đi thi **không có hình dạng của một ngày**. Nó có hình dạng của một ca thi: một khung bốn giờ, xảy ra một hoặc hai lần trong kỳ, đã ghi sẵn trên lịch thi FAP từ nhiều tuần trước. Sinh viên biết chính xác mình cần máy vào 07:30 thứ Ba, không cần máy cả ngày thứ Ba, và tuyệt đối không cần máy cả tuần.

ExamLap vì vậy lấy **ca thi bốn giờ** làm đơn vị bán hàng cơ sở: 79.000đ cho nhóm máy thi tiêu chuẩn, 99.000đ cho nhóm máy lập trình, 129.000đ cho nhóm máy cấu hình cao. Các gói dài hơn được neo vào đơn vị này: ngày thi hai ca 129.000đ, ca thi khẩn cấp đặt dưới ba giờ và giao tận cổng 179.000đ, tuần thi bảy ngày 449.000đ, gói tháng cho sinh viên làm đồ án hoặc đi thực tập 849.000đ.

Lựa chọn này kéo theo ba hệ quả. Thứ nhất, tồn kho được cắt lát theo nhịp lịch thi, nên một máy phục vụ được hai sinh viên trong cùng một ngày thay vì nằm chết sau ca sáng. Thứ hai, giao diện đặt máy trở thành một lưới ca thi hiển thị số máy còn trống, thứ không website cho thuê laptop Việt Nam nào đang có vì cả ngành vẫn chốt đơn qua hotline và Zalo [[ref:https://thuelaptop.com.vn/dia-diem-cho-thue-laptop-tai-da-nang-gia-re.html]] [[ref:https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html]]. Thứ ba, nó khớp thông lệ quốc tế: các chương trình cho mượn laptop tại thư viện đại học Mỹ đều tính theo giờ, ví dụ Drexel cho mượn năm giờ một lượt và phạt 5 USD mỗi giờ quá hạn [[ref:https://library.drexel.edu/news-and-events/programs-and-initiatives/laptop-charger-lending-kiosks/]].

:::ok Kết luận của tiểu mục
Ca thi không phải một đơn vị tính tiền do nhóm nghĩ ra cho lạ. Nó là đơn vị tự nhiên của khách hàng, đã có sẵn trên lịch thi FAP, và là khoảng trống sản phẩm rõ rệt nhất của thị trường hiện nay.
:::

## Ba cam kết dịch vụ

ExamLap công bố đúng ba cam kết, đều đo được bằng đồng hồ và đều gắn với một cơ chế vận hành cụ thể. Nguyên tắc lấy từ Turo: mọi cam kết thời gian phải là một con số hiển thị ngay trên màn hình, vì Turo công khai giữ cọc 24 đến 48 giờ trước chuyến và tự hoàn cọc 80 giờ sau chuyến [[ref:https://help.turo.com/en_us/security-deposits-us-HkbE44lE9]]. Cách viết "hỗ trợ 24/7" hay "giao nhanh" mà các đơn vị trong nước đang dùng không kiểm chứng được nên không tạo được niềm tin.

| Cam kết | Nội dung | Nhóm làm được bằng cách nào | Chỉ số theo dõi |
|---|---|---|---|
| Giao trước giờ thi 30 phút | Máy có mặt tại điểm hẹn trong khuôn viên trước giờ vào phòng thi 30 phút | Điểm trực đặt ngay trong khu campus Hoà Hải, không phải cửa hàng ngoài phố; ca trực được xếp theo lịch thi FAP nên nhân viên giao nhận đã có mặt trước khi đơn phát sinh | Tỉ lệ giao đúng hẹn, mục tiêu từ 98% trở lên |
| Đổi máy trong 15 phút nếu máy lỗi giữa ca thi | Sinh viên báo giám thị, nhắn Zalo cho ExamLap, máy thứ hai được mang tới trong 15 phút | Luôn giữ **máy dự phòng nóng** tại điểm trực trong toàn bộ khung giờ thi, đã bật sẵn, đã đăng nhập tới màn hình EOS, đúng nhóm cấu hình với máy đang thuê | Số ca thi bị gián đoạn vì máy; thời gian đổi máy thực tế |
| Hoàn cọc tự động trong 5 phút | Trả máy nguyên vẹn thì tiền cọc quay lại tài khoản trong vòng 5 phút, không cần nhắn tin hỏi | **Đối soát tự động**: hệ thống so bộ 6 ảnh lúc giao với bộ 6 ảnh lúc trả cùng checklist phần cứng; khớp hết thì lệnh hoàn tiền được đẩy đi ngay, không chờ quản trị viên duyệt | Thời gian hoàn cọc trung bình; tỉ lệ đơn phải can thiệp thủ công |
{caption: Ba cam kết dịch vụ công khai của ExamLap và cơ chế vận hành đứng sau từng cam kết.}
{widths: 3,4,7,3}

Cam kết thứ nhất dựa hoàn toàn vào vị trí. Cam kết tốt nhất tại Đà Nẵng hiện nay là "giao hàng trong ngày" [[ref:https://truonggiang.vn/cho-thue-laptop.html]], còn kỷ lục nhanh nhất cả nước là hai giờ và chỉ áp dụng ở nội thành Thành phố Hồ Chí Minh [[ref:https://laptopsgn.com/tin-tuc/dich-vu-cho-thue-laptop-tphcm-gia-re-giao-2h/]]. Với ca thi bắt đầu lúc 07:30, "trong ngày" là vô nghĩa. ExamLap không nhanh hơn nhờ chạy xe nhanh hơn mà nhờ đứng sẵn ở đó: campus nằm tại khu đô thị FPT, phường Hoà Hải, quận Ngũ Hành Sơn [[ref:https://daihoc.fpt.edu.vn/da-nang/]], trong khi cụm cho thuê laptop của thành phố tập trung ở quận Liên Chiểu, cách 8 đến 15 km.

Cam kết thứ hai đắt nhất, vì buộc nhóm chấp nhận một tỉ lệ máy nằm không đúng giờ cao điểm. Thị trường đã có đơn vị hứa "đổi máy hoặc nâng cấu hình không mất thêm chi phí" [[ref:https://mitgroup.vn/cho-thue-laptop/]] và một đơn vị tại Đà Nẵng cam kết đổi máy nếu hỏng [[ref:https://danang.plus/thue-laptop/]], nhưng không ai gắn con số phút vào lời hứa đó. Ràng buộc 15 phút chỉ có nghĩa khi máy dự phòng đã ở trong bán kính đi bộ.

:::risk Giới hạn trung thực của cam kết đổi máy
Đổi máy trong 15 phút giải quyết việc **có máy thay thế**, không giải quyết việc **bài thi đang dở nằm trên ổ cứng máy cũ**.
Sinh viên phải báo giám thị trước; ExamLap chỉ cấp máy thay thế theo hướng dẫn của giám thị, còn phương án khôi phục bài do bộ phận khảo thí của trường quyết định.
Nhóm cam kết về thiết bị, không cam kết về kết quả xử lý học vụ. Điều này phải viết rõ trong điều khoản dịch vụ.
:::

Cam kết thứ ba phụ thuộc vào hạ tầng thanh toán. Nhóm **chưa xác minh được** các cổng thanh toán trong nước có hỗ trợ cơ chế giữ tiền tạm trên thẻ hay không [Cần kiểm chứng]. Nếu không, phương án dự phòng là thu cọc bằng chuyển khoản và hoàn bằng lệnh chi tự động, chấp nhận thời gian hoàn dài hơn ngoài giờ ngân hàng. Con số 5 phút phải được thử nghiệm thật trong kỳ thi đầu tiên trước khi in lên trang chủ.

## Không giữ giấy tờ tuỳ thân của khách

Cách làm phổ biến của thị trường là **cọc cao cộng danh tính yếu**. Một nguồn tổng hợp ngành mô tả rằng các đơn vị cho thuê tại Đà Nẵng đều đặt cọc bằng giá trị máy [[ref:https://thuelaptop.com.vn/dia-diem-cho-thue-laptop-tai-da-nang-gia-re.html]]. Đơn vị thân thiện với sinh viên nhất mà nhóm tìm được vẫn yêu cầu **căn cước công dân bản gốc**, kèm thẻ sinh viên, thông tin liên hệ gia đình, địa chỉ tạm trú và cọc từ 500.000đ đến 2.000.000đ [[ref:https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html]].

ExamLap làm ngược lại: **cọc thấp cộng danh tính mạnh**, và **không giữ căn cước công dân, thẻ sinh viên hay bất kỳ giấy tờ tuỳ thân nào của khách**. Cọc chuẩn 300.000đ, giảm còn 150.000đ với khách hạng B từ lượt thứ ba, bằng 0đ với khách hạng A từ lượt thứ sáu nếu không vi phạm. Thay cho việc cầm giấy tờ, hệ thống xác minh một lần bằng eKYC đối chiếu ảnh căn cước với khuôn mặt sống, bắt buộc email `@fpt.edu.vn` và mã số sinh viên.

Đây trước hết là một lập luận thương mại. Sinh viên phát hiện máy hỏng lúc 06:30 sáng thường không có hai triệu tiền mặt, và càng không muốn ngồi trong phòng thi khi giấy tờ tuỳ thân của mình đang nằm trong ngăn kéo một cửa hàng ở quận khác. Bỏ được hai rào cản đó là bỏ được phần lớn ma sát của giao dịch. Mô hình thay thế đã được kiểm chứng ở quy mô lớn: Grover không thu tiền cọc mà dựng một bức tường xác minh gồm kiểm tra tín dụng, đối chiếu giấy tờ và khớp thông tin giao hàng [[ref:https://service.grover.com/hc/en-us/articles/19920531898642-How-does-Grover-s-credit-check-work]], và báo cáo rút ngắn 60% thời gian onboarding sau khi tự động hoá khâu này [[ref:https://onfido.com/customer/grover/]]. Hygglo tại Thuỵ Điển đạt hiệu quả tương tự nhờ hệ thống định danh quốc gia BankID [[ref:https://www.circularx.eu/en/cases/75/hygglo-peer-to-peer-rental-instead-of-buying]].

Sinh viên Đại học FPT không có Schufa hay BankID, nhưng có thứ tương đương trong phạm vi campus: mã số sinh viên gắn với hồ sơ học vụ, tài khoản thư điện tử của trường, và chi phí rất cao nếu bị khoá dịch vụ giữa mùa thi. Đó là tài sản bảo đảm phi tiền mặt mà một cửa hàng ngoài trường không khai thác được, vì họ không biết người thuê là ai và còn mấy kỳ nữa mới ra trường.

:::note Căn cứ pháp lý nằm ở Chương 17
Không giữ giấy tờ tuỳ thân của khách vừa là lựa chọn thương mại vừa là yêu cầu pháp lý.
Phần phân tích căn cứ, gồm quy định về giữ giấy tờ tuỳ thân, bảo vệ dữ liệu cá nhân trong quy trình eKYC, và cơ sở đòi bồi thường theo hợp đồng thuê tài sản, được trình bày đầy đủ ở Chương 17.
Ở đây chỉ nêu nguyên tắc: ràng buộc khách bằng hợp đồng điện tử có chữ ký và bằng bằng chứng bàn giao, không ràng buộc bằng việc cầm giấy tờ của họ.
:::

## So sánh với các đơn vị cho thuê hiện có

Thị trường Đà Nẵng đã có ít nhất bảy đơn vị cho thuê laptop [[ref:https://danang.plus/thue-laptop/]]. Không đơn vị nào định vị chuyên cho sinh viên đi thi EOS và SEB, và không đơn vị nào đặt tại khu Hoà Hải.

<<<landscape>>>

| Tiêu chí | ExamLap | MIT Group | leminhSTORE | DH Lend | Trường Giang | Đình Hậu · Sky Computer |
|---|---|---|---|---|---|---|
| Vị trí so với campus Hoà Hải | Ngay trong khu campus | Không tìm được địa chỉ tại Đà Nẵng [Cần kiểm chứng] [[ref:https://mitgroup.vn/cho-thue-laptop/]] | Sơn Trà, khác quận, qua cầu [[ref:https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html]] | Đà Nẵng, chưa công bố địa chỉ cụ thể [[ref:https://danang.plus/thue-laptop/]] | 118 Hàm Nghi, gần như đầu kia thành phố [[ref:https://truonggiang.vn/cho-thue-laptop.html]] | Liên Chiểu và Cẩm Lệ, cách 8 đến 15 km [[ref:https://maytinhdinhhau.vn/dich-vu-cho-thue-laptop-tai-da-nang/]] |
| Chuẩn bị máy | Chín hạng mục sẵn sàng thi, có ghi ngày test EOS và SEB | Máy trắng, có đổi máy hoặc nâng cấu hình miễn phí [[ref:https://mitgroup.vn/cho-thue-laptop/]] | Máy học tập cơ bản, không cài phần mềm thi [[ref:https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html]] | Cài phần mềm theo yêu cầu [[ref:https://danang.plus/thue-laptop/]] | Máy văn phòng và sự kiện [[ref:https://truonggiang.vn/cho-thue-laptop.html]] | Hỗ trợ cài đặt, lắp đặt miễn phí [[ref:https://maytinhdinhhau.vn/dich-vu-cho-thue-laptop-tai-da-nang/]] |
| Giờ giao | Trước giờ thi 30 phút, phục vụ cả ca 07:30 | Giao trong ngày [[ref:https://mitgroup.vn/cho-thue-laptop/]] | Theo giờ mở cửa, sớm nhất 08:00 [[ref:https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html]] | Giao nhận tận nơi, không nêu thời gian [[ref:https://danang.plus/thue-laptop/]] | Giao trong ngày [[ref:https://truonggiang.vn/cho-thue-laptop.html]] | Không nêu thời gian; Sky Computer chỉ miễn phí giao từ 5 máy [[ref:https://skycomputer.vn/dich-vu/cho-thue-may-tinh-laptop-tai-da-nang/]] |
| Cách đặt | Website chọn ca thi, thấy số máy trống, không cần gọi điện | Hotline và inbox [[ref:https://mitgroup.vn/cho-thue-laptop/]] | Điện thoại, SMS, Zalo [[ref:https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html]] | Liên hệ trực tiếp [[ref:https://danang.plus/thue-laptop/]] | Hotline, Zalo, email [[ref:https://truonggiang.vn/cho-thue-laptop.html]] | Hai số điện thoại [[ref:https://maytinhdinhhau.vn/dich-vu-cho-thue-laptop-tai-da-nang/]] |
| Hiểu quy chế thi EOS | Sản phẩm được thiết kế quanh quy chế thi | Không đề cập | Có nêu phục vụ học tập, thi cử và thực tập, nhưng không cài phần mềm thi [[ref:https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html]] | Không đề cập | Phục vụ thi tuyển công chức, không phải thi EOS [[ref:https://truonggiang.vn/cho-thue-laptop.html]] | Không đề cập |
| Giá công bố | 79.000đ đến 179.000đ mỗi ca thi 4 giờ | Từ 29.000đ mỗi ngày, ưu đãi sinh viên từ 20.000đ [[ref:https://mitgroup.vn/cho-thue-laptop/]] | Từ 38.000đ mỗi ngày [[ref:https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html]] | 50.000đ mỗi ngày, 1.000.000đ mỗi tháng [[ref:https://danang.plus/thue-laptop/]] | Từ 50.000đ mỗi ngày [[ref:https://truonggiang.vn/cho-thue-laptop.html]] | Không công bố giá [[ref:https://skycomputer.vn/dich-vu/cho-thue-may-tinh-laptop-tai-da-nang/]] |
| Thế chấp và giấy tờ | Cọc 300.000đ, giảm dần về 0đ theo hạng tín nhiệm; không giữ giấy tờ tuỳ thân | Có gói không cọc [[ref:https://mitgroup.vn/thue-laptop-khong-coc/]] | Căn cước bản gốc, cọc 500.000đ đến 2.000.000đ [[ref:https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html]] | Không công bố | Không công bố | Mặt bằng chung là cọc bằng giá trị máy [[ref:https://thuelaptop.com.vn/dia-diem-cho-thue-laptop-tai-da-nang-gia-re.html]] |
{caption: So sánh ExamLap với các đơn vị cho thuê laptop đang phục vụ Đà Nẵng trên bảy tiêu chí quyết định mua.}
{note: Giá và điều kiện của các đơn vị là giá công bố trên website của họ tại thời điểm khảo sát [Cần kiểm chứng vì nhóm chưa gọi điện xác nhận từng đơn vị]. Cột ExamLap là thiết kế của nhóm.}

<<<portrait>>>

Bảng trên cho thấy ExamLap không thắng ở tiêu chí giá và không định thắng ở đó. ExamLap thắng ở những tiêu chí còn lại, và tất cả đều chỉ có giá trị vào đúng buổi sáng ngày thi.

## Vì sao giá của chúng tôi cao hơn — và vì sao khách vẫn trả

Đối thủ bán từ 29.000đ đến 50.000đ một ngày [[ref:https://mitgroup.vn/cho-thue-laptop/]] [[ref:https://truonggiang.vn/cho-thue-laptop.html]], ExamLap bán 79.000đ đến 179.000đ một ca bốn giờ. Tính theo giờ sử dụng máy, ExamLap đắt hơn nhiều lần. Đây là câu hỏi phản biện mà bất kỳ ai đọc proposal cũng sẽ đặt ra.

Câu trả lời là ExamLap **không bán thời gian sử dụng máy**. Cái được bán là **xác suất dự thi thành công**, và giá trị của nó phải đo bằng cái mất đi khi không dự thi được, chứ không đo bằng số giờ ngồi trước màn hình.

Học phí giai đoạn chuyên ngành tại campus Đà Nẵng là 22.120.000đ một học kỳ [[ref:https://baodanang.vn/hoc-phi-truong-dai-hoc-fpt-2025-2026-tai-cac-co-so-tren-ca-nuoc-3151966.html]]. Một học kỳ bốn tháng với khoảng năm môn thi, nên giá trị kinh tế của một môn thi vào khoảng **4.424.000đ** [Ước lượng của nhóm]. Đặt cạnh giá thuê một ca thi từ 79.000đ đến 179.000đ, tỉ lệ chi phí trên rủi ro nằm trong khoảng **1 trên 25 đến 1 trên 56**, chưa tính phần thiệt hại khó quy đổi thành tiền là một học kỳ chậm tiến độ và một môn tiên quyết bị lùi.

Nói cách khác, khách hàng không so 79.000đ với 38.000đ mà so 79.000đ với 4.424.000đ. Ở khung so sánh đó, chênh nhau vài chục nghìn đồng không còn là biến số quyết định; việc máy có chạy được EOS lúc 07:30 hay không mới là biến số duy nhất.

Chênh lệch giá cũng không phải phần lãi ròng. Nó trả cho những thứ đối thủ không làm: công chuẩn bị chín hạng mục sẵn sàng thi cho mỗi lượt giao, máy dự phòng nóng nằm chờ suốt khung giờ thi, nhân viên trực tại campus vào giờ mà cửa hàng ngoài phố chưa mở cửa, và quỹ rủi ro cho hư hỏng. Doanh thu bình quân mỗi lượt thuê sau khi trộn các gói là 144.100đ, vẫn nằm trong mặt bằng 80.000đ đến 200.000đ mỗi máy mỗi ngày mà chính các đơn vị Đà Nẵng ghi nhận cho thuê ngắn hạn [[ref:https://truonggiang.vn/cho-thue-laptop.html]].

:::risk Thừa nhận rủi ro: một bộ phận khách vẫn sẽ chọn giá rẻ
Sẽ có sinh viên chọn thuê 38.000đ một ngày ở Sơn Trà, hoặc mượn máy của bạn cùng phòng với giá 0đ. Nhóm không phủ nhận và không cạnh tranh với họ bằng giá. Cách xử lý gồm bốn hướng.
Một, giữ nguyên định vị và chấp nhận thị trường mục tiêu là nhóm rủi ro cao: sinh viên dùng Mac chip M-series, sinh viên có máy đang sửa đúng tuần thi, sinh viên hỏng máy đột ngột.
Hai, vẫn cung cấp gói ngày, tuần và tháng có giá cạnh tranh với mặt bằng để giữ nhóm nhạy giá và lấp công suất ngoài mùa thi.
Ba, hạ tổng chi phí của khách quen bằng hạng tín nhiệm, vì cọc giảm từ 300.000đ về 0đ có giá trị thực còn lớn hơn vài chục nghìn tiền thuê.
Bốn, không chạy theo quảng cáo giá mồi như một số trang niêm yết "từ 10k mỗi ngày" ngay trong đường dẫn [[ref:https://www.thuelaptop.vn/thue-laptop-da-nang-gia-re-chi-tu-10k/]], vì mất niềm tin ở lần gọi đầu tiên thì không có lần thứ hai.
:::

## Bài học từ các nền tảng cho thuê trên thế giới

Ngành cho thuê thiết bị đã có đủ cả trường hợp thành công lẫn trường hợp chết để rút kinh nghiệm. Sáu bài học dưới đây được chọn vì mỗi bài đổi được thành một quyết định thiết kế cụ thể của ExamLap.

**Bài học 1, từ Lumoid: mỗi khách hàng mới là một khoản đầu tư mới.** Lumoid là startup thuộc Y Combinator khoá S13, cho thuê máy ảnh và thiết bị đeo theo mô hình dùng thử trước khi mua [[ref:https://www.ycombinator.com/blog/lumoid-yc-s13-wants-to-rent-you-a-camera-now-and-everything-later]]. Họ ký được hợp đồng với Best Buy rồi đóng cửa tháng 12 năm 2017 vì không huy động đủ vốn để mua số thiết bị cần cho hợp đồng đó [[ref:https://techcrunch.com/2017/12/10/why-gear-rental-marketplace-lumoid-shut-down/]] [[ref:https://gizmodo.com/lumoid-best-buys-supposed-gear-rental-partner-shuts-d-1821165345]]. Lumoid không chết vì thiếu khách mà vì thừa khách so với số thiết bị mua nổi. ExamLap áp dụng bằng cách coi đội máy là trần công suất cứng: năm đầu 10 máy, mở đặt trước theo lịch thi để biết cầu trước khi phải có cung, và chỉ tăng lên 16 máy ở năm hai sau khi tỉ lệ khai thác thực tế đã được đo.

**Bài học 2, từ Rent the Runway: đếm hoà vốn theo số lượt, không theo doanh thu tháng.** Phân tích của một giáo sư Wharton cho thấy một món đồ giá vốn 85 đến 90 USD, cho thuê 25 đến 30 USD mỗi lượt, cần **17 đến 18 lượt** để hoà vốn trong khi thực tế chỉ đạt khoảng 20 lượt trên vòng đời [[ref:https://gadallon.substack.com/p/rent-the-runway-when-complexity-collides]]. Biên an toàn chỉ hai đến ba lượt. Công ty này mất tới năm tài chính 2025 mới có quý lãi, và ngay sau đó cắt đầu tư tài sản cho thuê từ 74,9 triệu USD xuống 45 đến 50 triệu USD [[ref:https://investors.renttherunway.com/news-releases/news-release-details/rent-runway-inc-announces-fourth-quarter-and-full-year-2025]]. ExamLap áp dụng bằng hai quyết định đã phản ánh trong mô hình tài chính: mua máy cũ giá 6.500.000đ đến 10.000.000đ thay vì máy mới, và lấy **số lượt thuê trên mỗi máy mỗi tháng** làm chỉ số Bắc Đẩu thay vì số máy trong kho.

**Bài học 3, từ Grover: tách bạch hao mòn thường với hư hỏng, và công khai bảng giá.** Grover tuyên bố xước nhỏ cùng dấu hiệu sử dụng bình thường được làm sạch miễn phí [[ref:https://www.grover.com/at-en/g-about/asset-condition]], đồng thời niêm yết rõ mức bồi thường khi thiết bị không sửa được và cả khoản phạt 49 EUR cho máy trả về còn đăng nhập tài khoản người dùng [[ref:https://service.grover.com/hc/en-us/articles/19918338642578-Repair-and-replacement-costs]]. ExamLap áp dụng bằng bảng giá đền bù công khai tách riêng máy, sạc và tai nghe, bằng phí miễn trừ thiệt hại tự chọn 15.000đ mỗi lượt hoặc 69.000đ mỗi tháng, và bằng việc đưa mục xoá sạch tài khoản người dùng thành hạng mục bắt buộc khi thu hồi máy.

**Bài học 4, từ Turo: cọc thay đổi theo hồ sơ rủi ro, và xác thực lại ở mỗi giao dịch.** Turo áp mức cọc từ 0 đến 750 USD tuỳ độ tuổi người thuê và hạng xe, giảm 250 USD nếu khách cung cấp thông tin bảo hiểm cá nhân, và xác thực danh tính lại ở mỗi giao dịch chứ không chỉ lúc đăng ký [[ref:https://help.turo.com/en_us/security-deposits-us-HkbE44lE9]] [[ref:https://www.complycube.com/en/customer/turo-strengthens-car-sharing-compliance/]]. ExamLap áp dụng bằng thang cọc ba bậc 300.000đ, 150.000đ và 0đ gắn với hạng tín nhiệm, và bằng việc mỗi lượt bàn giao đều chụp ảnh người nhận cùng máy có dấu thời gian.

**Bài học 5, từ Fat Llama và Hygglo: không làm sàn ngang hàng ở giai đoạn đầu.** Fat Llama từng bị ghi nhận nhiều vụ mất thiết bị, trong đó có vụ chủ đồ mất hơn 5.000 USD thiết bị máy ảnh [[ref:https://petapixel.com/2019/03/20/how-i-had-over-5000-in-camera-gear-stolen-through-fat-llama/]], cùng hàng loạt khiếu nại về việc từ chối bồi thường [[ref:https://www.trustpilot.com/review/fatllama.com]], và cuối cùng được Hygglo mua lại với giá 41,5 triệu USD năm 2022 [[ref:https://www.eu-startups.com/2022/08/sweden-based-hygglo-acquires-uk-based-fat-llama-in-e41-million-deal-to-create-worlds-biggest-peer-to-peer-rental-platform/]]. Với quy mô của ExamLap, một vụ mất máy đủ để xoá sạch lợi nhuận một mùa thi. Vì vậy giai đoạn một là mô hình tự sở hữu đội máy, giao nhận mặt đối mặt trong khuôn viên, không cho sinh viên cho thuê lại máy của nhau qua nền tảng. Phần đáng học của Hygglo là cách minh bạch khoản phí dùng để làm gì [[ref:https://help.hygglo.info/en/articles/10415333-how-hygglo-works]] và mô hình bảo hiểm nhúng theo giao dịch của Omocom, giá 2 đến 6 EUR cho hạn mức 1.000 EUR [[ref:https://www.vanameyde.com/stories/omocom-circular-economy/]], tức khoảng 0,2% đến 0,6% giá trị tài sản mỗi lượt. Đây là cơ sở định lượng để ExamLap tự lập quỹ rủi ro nội bộ khi chưa có sản phẩm bảo hiểm tương đương tại Việt Nam.

**Bài học 6, từ Getaround và Omni: sự mập mờ và sự phiền phức đều giết dịch vụ.** Getaround bị Tổng Chưởng lý Washington DC buộc hoàn tiền vì đưa thông tin sai lệch về mức độ an toàn của nền tảng và không công bố rõ các trường hợp loại trừ bảo hiểm [[ref:https://oag.dc.gov/release/attorney-general-schwalb-secures-refunds-dc]]. Omni đóng cửa năm 2019 một phần vì việc đi lấy và đi trả đồ phiền hơn là mua mới [[ref:https://techcrunch.com/2019/11/25/omni-shuts-down/]]. Gộp lại thành hai quy tắc thiết kế: khối "những trường hợp không được miễn trừ" nằm ở đầu trang điều khoản với ô tích riêng chứ không gộp chung với điều khoản dịch vụ, và toàn bộ thao tác nhận máy tại điểm hẹn phải gọn dưới 5 phút. Đối thủ thực sự của ExamLap không phải cửa hàng cho thuê ngoài phố mà là việc mượn máy của bạn cùng phòng với giá 0đ. Chỉ tốc độ và sự chắc chắn mới thắng được mức giá đó.

:::warn Bài học ngược từ Grover về cấu trúc vốn
Grover huy động hơn 600 triệu USD, phần lớn là nợ, để mở rộng đội thiết bị và đạt định giá kỳ lân, rồi vẫn phải tái cấu trúc theo luật StaRUG: tháng 4 năm 2025 toà án Charlottenburg phê chuẩn kế hoạch đổi 50% cổ phần lấy 30 triệu EUR vốn mới [[ref:https://hengeler-news.com/en/articles/hengeler-mueller-advises-grover-on-financial-restructuring-via-starug-proceedings]].
Kết luận cho ExamLap: không dùng vốn vay để mở rộng đội máy trước khi chứng minh được tỉ lệ khai thác thực tế.
:::

![Máy trạng thái của một đơn thuê, từ lúc đặt ca thi đến lúc trả máy và hoàn cọc, ánh xạ trực tiếp vào sáu giai đoạn của hành trình khách hàng.](assets/diagrams/02-trang-thai-don.png){w=13}{src: Nguồn: nhóm tác giả.}

## Bản đồ hành trình khách hàng

Sáu giai đoạn dưới đây mô tả một lượt thuê hoàn chỉnh nhìn từ phía sinh viên. Hàng "điểm đau hiện nay" ghi lại tình trạng khi chưa có ExamLap, dựa trên dữ kiện ở Chương 1 và khảo sát thị trường. Hàng "chỉ số theo dõi" là các số nhóm sẽ đo ngay từ mùa thi đầu tiên, vì một hành trình không có chỉ số thì không cải tiến được.

<<<landscape>>>

| Giai đoạn | 1. Phát sinh nhu cầu | 2. Tìm giải pháp | 3. Đặt máy | 4. Nhận máy | 5. Thi | 6. Trả máy |
|---|---|---|---|---|---|---|
| **Sinh viên làm gì** | Phát hiện máy hỏng, máy đang sửa, hoặc nhận ra máy Mac chip M không thi EOS được; xem lại lịch thi trên FAP | Hỏi bạn cùng phòng, tìm Google, hỏi nhóm Facebook của khoá, gọi vài cửa hàng | Mở website ExamLap, chọn ngày và ca thi, chọn nhóm máy, xác minh một lần bằng email trường và mã số sinh viên, thanh toán | Tới điểm hẹn trong campus trước giờ thi 30 phút, ký biên bản bàn giao có ảnh, nhận máy cùng sạc và tai nghe | Đăng nhập wifi bằng tài khoản của mình, mở EOS và SEB, làm bài, nộp bài | Mang máy về điểm trực, chụp đối chiếu 6 ảnh, nhận lại cọc |
| **Cảm xúc** | Hoảng, nghĩ ngay tới khả năng vắng thi | Lo và mất phương hướng vì không biết tin ai | Bớt lo dần khi thấy số máy còn trống hiển thị theo ca | Hồi hộp nhưng đã chủ động, còn thời gian làm quen máy | Tập trung vào bài thi, không nghĩ về thiết bị | Nhẹ nhõm, hoặc bực nếu phải chờ hoàn cọc |
| **Điểm đau hiện nay** | Không có phương án dự phòng nào trong bán kính đi bộ; cụm cho thuê của thành phố nằm cách 8 đến 15 km [[ref:https://danang.plus/thue-laptop/]] | Toàn bộ website cho thuê trong nước là trang giới thiệu kèm hotline, không đặt được online [[ref:https://thuelaptop.com.vn/dia-diem-cho-thue-laptop-tai-da-nang-gia-re.html]] | Quy trình chuẩn của thị trường là gọi, tư vấn, báo giá, ký hợp đồng, giao máy, mất từ vài giờ tới một ngày [[ref:https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html]] | Cam kết tốt nhất tại Đà Nẵng chỉ là giao trong ngày [[ref:https://truonggiang.vn/cho-thue-laptop.html]]; phải nộp căn cước bản gốc và cọc tới 2.000.000đ [[ref:https://leminhstore.vn/thue-laptop-sinh-vien-da-nang-104917u.html]] | Máy thuê không cài sẵn EOS và SEB, chưa test, có thể thiếu jack 3.5mm cho phần thi nghe [[ref:https://it.fpt.edu.vn/cantho/huong-dan-cai-dat-phan-mem-thi-eos-seb/]] | Không có mốc thời gian hoàn cọc công bố; tranh chấp hư hỏng không có bằng chứng hai chiều [[ref:https://congchung247.com.vn/thue-thiet-bi-lam-hong-ben-thue-co-phai-boi-thuong/]] |
| **ExamLap giải quyết** | Điểm trực nằm ngay trong khu campus, mở đúng khung giờ thi; nhắc đặt trước theo lịch thi | Một trang duy nhất trả lời đúng câu hỏi "bạn thi ca nào", dùng đúng từ vựng mà sinh viên đã quen từ hệ thống mượn máy của trường [[ref:https://it-hcm.fpt.edu.vn/articles.php?news=huong-dan-muon-laptop-cua-sinh-vien-trong-truong&id=56]] | Đặt xong dưới 2 phút, không cần gọi điện, chỉ hiển thị những máy thật sự còn trống của đúng ca đó | Giao trước giờ thi 30 phút; cọc 300.000đ giảm dần về 0đ theo hạng tín nhiệm; không giữ giấy tờ tuỳ thân | Máy đã qua chín hạng mục sẵn sàng thi; có máy dự phòng nóng đổi trong 15 phút nếu máy lỗi giữa ca | Đối soát tự động sáu ảnh trước và sau, hoàn cọc trong 5 phút; hao mòn thường không tính phí |
| **Chỉ số theo dõi** | Số lượt truy cập trong 48 giờ trước mỗi ca thi; tỉ lệ đơn đặt trước từ một ngày trở lên | Tỉ lệ khách tự tìm tới website so với khách qua giới thiệu; số câu hỏi phải trả lời thủ công qua Zalo | Thời gian hoàn tất đặt máy; tỉ lệ bỏ dở giữa luồng; tỉ lệ ca thi hết máy | Tỉ lệ giao đúng hẹn; thời gian bàn giao trung bình tại điểm hẹn | Số ca thi bị gián đoạn vì thiết bị; thời gian đổi máy thực tế | Thời gian hoàn cọc trung bình; tỉ lệ tranh chấp trên tổng lượt; tỉ lệ khách quay lại kỳ sau |
{caption: Bản đồ hành trình khách hàng ExamLap qua sáu giai đoạn, đối chiếu điểm đau hiện nay với cách giải quyết và chỉ số đo lường tương ứng.}
{note: Các điểm đau được dẫn từ khảo sát thị trường và tài liệu hướng dẫn của nhà trường. Cột ExamLap giải quyết và cột chỉ số theo dõi là thiết kế của nhóm [Ước lượng của nhóm].}

<<<portrait>>>

Đọc theo hàng "cảm xúc" sẽ thấy toàn bộ giá trị của dịch vụ nằm ở việc kéo đường cảm xúc từ "hoảng" về "tập trung vào bài thi" càng sớm càng tốt. Mọi quyết định thiết kế trong chương này, từ việc bán theo ca thi, tới ba cam kết đo bằng phút, tới việc không giữ giấy tờ tuỳ thân, đều phục vụ đúng mục tiêu đó.
