## Hai loại dữ liệu, hai chế độ bảo vệ

ExamLap chạm vào hai loại dữ liệu hoàn toàn khác nhau. Nhầm lẫn giữa chúng là nguồn gốc của gần như mọi
sai lầm về quyền riêng tư trong ngành cho thuê thiết bị, nên chương này bắt đầu bằng việc tách bạch.

**Loại thứ nhất là dữ liệu về khách hàng do ExamLap giữ.** Gồm hồ sơ xác minh danh tính, ảnh giấy tờ chụp
lúc eKYC, họ tên, mã số sinh viên, email `@fpt.edu.vn`, số điện thoại, lịch sử thuê, lịch sử thanh toán và
biên bản bàn giao. Loại này nằm trên máy chủ của nhóm, do nhóm quyết định thu, lưu và xoá, và nhóm là bên
chịu trách nhiệm trước pháp luật về nó. Chế độ xử lý là: thu càng ít càng tốt, lưu càng ngắn càng tốt, mã
hoá khi lưu, và ghi nhật ký mọi lần đọc. Đây không phải sáng kiến riêng của nhóm mà là nguyên tắc thiết kế
mà chính các dự án đọc chip căn cước công dân tự khuyến cáo: ứng dụng xử lý thông tin cá nhân nhạy cảm thì
người tích hợp phải tự bảo đảm tuân thủ quy định bảo vệ dữ liệu [[ref:https://github.com/huyhuynh1905/flutter-cccd-nfc-reader]].
Tài liệu của các bộ công cụ eKYC thương mại thậm chí không nêu nghĩa vụ tuân thủ nào, nghĩa là nghĩa vụ rơi
trọn về phía bên tích hợp, tức là về phía ExamLap [[ref:https://pub.dev/packages/finos_ekyc_flutter]].

**Loại thứ hai là dữ liệu do chính khách tạo ra trên máy thuê.** Gồm bài làm, tệp tài liệu, phiên đăng nhập
Gmail hay Facebook, mật khẩu trình duyệt tự lưu, lịch sử duyệt web. Loại này không phải tài sản của ExamLap
và nhóm không có quyền đọc nó. Chế độ xử lý ngược hẳn: không thu thập, không sao lưu, không nhìn vào, và xoá
sạch trước khi máy sang tay người tiếp theo. Cam kết này đã thành điều khoản hợp đồng: phần mềm quản lý thiết
bị trên máy không đọc nội dung tệp, không ghi thao tác bàn phím, không chụp màn hình và không truy cập camera
(Phụ lục C, Điều 6). Ngay cả khi khách quá hạn không trả máy, lệnh cưỡng chế duy nhất nhóm dùng là khoá màn
hình, không phải xoá dữ liệu (Phụ lục B, mục B.4).

Việc tự giới hạn này dễ giữ hơn người ta tưởng, vì nền tảng Windows vốn không cho khoá máy từ xa qua MDM:
danh sách nền tảng hỗ trợ lệnh khoá từ xa của Microsoft Intune chỉ gồm Android, iOS/iPadOS, macOS và
visionOS [[ref:https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/intune/device-management/actions/remote-lock.md]].
Nhóm vì vậy dùng một tác nhân chống trộm riêng có hành động khoá và báo động [[ref:https://github.com/prey/prey-node-client]],
và chấp nhận rằng khả năng can thiệp từ xa của mình là hẹp. Một hệ thống có ít quyền lực hơn thì cũng ít
cách lạm quyền hơn.

## Ranh giới tin cậy của hệ thống

<<<landscape>>>

![Bốn vùng tin cậy của hệ thống ExamLap và những thứ được phép đi qua từng ranh giới.](assets/diagrams/10-ranh-gioi-tin-cay.png){w=0}{src: Nguồn: nhóm tác giả.}

<<<portrait>>>

Hình trên chia hệ thống thành bốn vùng, xếp theo mức độ tin cậy tăng dần từ trái sang phải.

**Vùng một, không tin cậy.** Gồm trình duyệt của sinh viên, điện thoại của nhân viên giao nhận, và chiếc
laptop đang nằm ngoài kho. Không tin bất cứ dữ liệu nào từ vùng này, kể cả dữ liệu do chính ứng dụng của
nhóm gửi lên; mọi kiểm tra nghiệp vụ đều lặp lại ở phía máy chủ. Chiếc laptop đang cho thuê chỉ được phép
đẩy lên đúng một thứ là tín hiệu báo còn sống và trạng thái máy, không phải nội dung gì trên ổ đĩa.

**Vùng hai, lớp biên.** Chỉ có ba việc: bắt buộc HTTPS, giới hạn tần suất gọi, và kiểm chữ ký HMAC của
webhook trước khi tin bất cứ điều gì trong nội dung. Quy tắc thứ ba là quan trọng nhất với luồng tiền, vì
webhook của cổng thanh toán là một kênh mà bất kỳ ai trên Internet cũng gửi vào được. Tài liệu về vận hành
webhook ở quy mô lớn nhấn mạnh việc ký nội dung và kiểm chữ ký là điều kiện tiên quyết, trước cả chuyện
thử lại và hàng đợi lỗi [[ref:https://matheuspalma.com/blog/outbound-webhook-delivery-signing-retries-dead-letters]] [[ref:https://www.educative.io/blog/webhook-system-design]].

**Vùng ba, ứng dụng.** Ba lớp lọc xếp chồng: phân quyền theo vai trò, quy tắc nghiệp vụ của máy trạng thái
đơn thuê, và nhật ký chỉ ghi thêm được chặn ở cả tầng ứng dụng lẫn tầng cơ sở dữ liệu
[[ref:https://www.designgurus.io/answers/detail/how-do-you-enforce-immutability-and-appendonly-audit-trails]].
Một yêu cầu hợp lệ về chữ ký vẫn bị chặn ở đây nếu nó đòi chuyển đơn sang trạng thái mà máy trạng thái không
cho phép.

**Vùng bốn, dữ liệu nhạy cảm.** Gồm số căn cước đã băm, ảnh eKYC có hạn xoá, vector đặc trưng khuôn mặt và
nhật ký của máy chủ quản lý thiết bị. Vùng này không có đường đi trực tiếp từ vùng một. Mọi truy cập đều
phải đi qua lớp nghiệp vụ ở vùng ba và đều để lại dấu vết. Đặc biệt, thông tin đăng nhập của dịch vụ eKYC
chỉ nằm ở máy chủ, không bao giờ đặt ở trình duyệt; kiến trúc proxy này là khuyến nghị rõ ràng của các bản
tích hợp eKYC tham chiếu, vì nếu gọi thẳng từ trình duyệt thì cả khoá bí mật lẫn ảnh giấy tờ đều lộ ra phía
người dùng [[ref:https://github.com/VNQuy94/vnpt-ekyc-poc]].

## Dữ liệu nào được thu thập, dữ liệu nào không

| Trường dữ liệu | Mục đích thu thập | Căn cứ | Nơi lưu | Thời hạn lưu | Ai xem được |
|---|---|---|---|---|---|
| Họ tên, số điện thoại | Đối chiếu khi bàn giao, liên lạc khi máy quá hạn | Thực hiện hợp đồng thuê | PostgreSQL, cột mã hoá | 24 tháng sau lượt thuê cuối | Khách, quản trị viên |
| Email `@fpt.edu.vn`, mã số sinh viên | Xác minh tư cách sinh viên, gửi thông báo đơn | Thực hiện hợp đồng thuê | `users`, `kyc_profiles` | 24 tháng sau lượt thuê cuối | Khách, quản trị viên |
| **Số căn cước dạng băm** | Chặn trùng tài khoản, đối chiếu danh sách chặn nội bộ | Lợi ích hợp pháp trong phòng chống gian lận | `kyc_profiles.id_number_hash`, `blocklist.id_number_hash` | Giữ lâu dài ở dạng băm, không đảo ngược được | Không ai đọc được số gốc; hệ thống chỉ so khớp băm |
| Ảnh hai mặt giấy tờ | Đối chiếu một lần khi mở tài khoản | Sự đồng ý riêng, tách khỏi điều khoản dịch vụ | Kho ảnh mã hoá khi lưu | **90 ngày** kể từ lượt thuê cuối, xoá tự động | Quản trị viên khi duyệt hồ sơ khó; mỗi lần mở đều vào nhật ký |
| **Vector đặc trưng khuôn mặt** | So khớp khuôn mặt sống với ảnh giấy tờ | Sự đồng ý riêng | `kyc_profiles.face_vector` | 90 ngày, xoá cùng ảnh giấy tờ | Chỉ máy chủ dùng để so khớp, không hiển thị cho người |
| Điểm so khớp, kết quả kiểm tra người sống | Bằng chứng đã xác minh đúng người | Sự đồng ý riêng | `kyc_profiles.match_score` | Theo hồ sơ khách hàng | Quản trị viên |
| Sáu ảnh hiện trạng máy kèm mã băm SHA-256 | Bằng chứng đối chiếu khi tranh chấp hư hỏng | Thực hiện hợp đồng, Phụ lục B | Kho ảnh | **12 tháng** rồi xoá | Khách với đơn của mình, nhân viên tại thời điểm bàn giao, quản trị viên |
| Chữ ký điện tử, địa chỉ IP, dấu thời gian ký | Chứng minh hợp đồng đã giao kết | Thực hiện hợp đồng | PostgreSQL, bản không sửa được | Theo thời hiệu khiếu nại **[Cần kiểm chứng]** | Khách với đơn của mình, quản trị viên |
| Lịch sử đơn thuê và giao dịch | Đối soát, hoàn cọc, kế toán | Nghĩa vụ kế toán và thuế | `orders`, `payments` | Theo quy định lưu trữ chứng từ **[Cần kiểm chứng]** | Khách với đơn của mình, quản trị viên |
| Trạng thái trực tuyến và vị trí gần đúng **của máy** | Chống mất tài sản của ExamLap | Lợi ích hợp pháp trên tài sản của chính mình | Máy chủ quản lý thiết bị | 90 ngày rồi ẩn danh hoá | Quản trị viên; mỗi lần tra vị trí đều vào nhật ký |
| Nhật ký kiểm toán | Bằng chứng thao tác, phát hiện lạm quyền | Lợi ích hợp pháp | `audit_logs` chỉ ghi thêm | Giữ lâu hơn các loại trên, sau 24 tháng thay dữ liệu nhận dạng bằng mã ẩn danh | Chỉ quản trị viên, và không ai được sửa |
{caption: Bảng kê dữ liệu cá nhân mà ExamLap xử lý, kèm mục đích, thời hạn và phạm vi truy cập.}
{widths: 2.6,3.1,2.4,2.7,2.8,3.0}
{note: Cột "Căn cứ" dùng cách diễn đạt thông dụng của pháp luật bảo vệ dữ liệu cá nhân. Việc ánh xạ từng dòng vào đúng khoản của văn bản hiện hành là việc nhóm phải làm với người có chuyên môn pháp lý trước khi vận hành thật, xem mục dưới.}

Hai chi tiết trong bảng đáng được nói rõ vì chúng là lựa chọn thiết kế, không phải mặc định kỹ thuật.

**Số căn cước được lưu dưới dạng băm, không lưu số gốc.** Hệ thống vẫn chặn được một người mở nhiều tài
khoản, vẫn đối chiếu được với danh sách chặn nội bộ, nhưng nếu cơ sở dữ liệu bị lộ thì thứ rò ra là một
chuỗi băm chứ không phải danh sách số căn cước của vài nghìn sinh viên. Cái giá phải trả là nhóm không tra
ngược được số căn cước từ hệ thống của mình, kể cả khi muốn.

**Khuôn mặt được lưu dưới dạng vector đặc trưng, kèm đúng một ảnh chân dung đã cắt ở độ phân giải thấp.** Vector là thứ dùng để so khớp tự động; ảnh chân dung độ phân giải thấp chỉ hiện trên màn hình bàn giao để nhân viên đối chiếu mặt người với hồ sơ, không tải xuống được và không phải ảnh giấy tờ. Đây là mức tối thiểu đủ để so
khớp một lần lúc mở tài khoản. Nhóm chọn các thư viện có giấy phép cho phép dùng trong dịch vụ có thu tiền,
cụ thể là `face_recognition` giấy phép MIT [[ref:https://github.com/ageitgey/face_recognition]] và DeepFace
cũng giấy phép MIT, có sẵn tuỳ chọn `anti_spoofing` [[ref:https://pypi.org/project/deepface/]], kèm mô hình
chống giả mạo giấy phép Apache 2.0 [[ref:https://github.com/minivision-ai/Silent-Face-Anti-Spoofing]]. Nhóm
chủ động **không dùng** các mô hình đã huấn luyện sẵn của InsightFace, vì tài liệu chính thức ghi rõ chúng
chỉ dành cho nghiên cứu phi thương mại [[ref:https://pypi.org/project/insightface/]]. Đây là loại ràng buộc
rất dễ bị bỏ qua trong một đồ án, nhưng một dịch vụ có thu tiền mà dùng sai giấy phép thì rủi ro là thật.

:::warn Bốn thứ ExamLap không thu thập
**Ảnh căn cước quá hạn lưu.** Sau 90 ngày kể từ lượt thuê cuối, ảnh bị xoá và không có bản sao lưu nào giữ lại.
**Mật khẩu tài khoản trường.** ExamLap không bao giờ hỏi mật khẩu `@fpt.edu.vn`; việc xác minh email làm bằng đường dẫn một lần gửi tới hộp thư, không qua đăng nhập uỷ quyền vào hệ thống của trường.
**Vị trí GPS của người dùng.** Hệ thống định vị gần đúng chiếc máy, không định vị con người; trên máy khách không cài ứng dụng theo dõi vị trí nào, và dữ liệu vị trí máy được ẩn danh hoá sau 90 ngày. Để so sánh, dữ liệu vị trí thiết bị trong Microsoft Intune chỉ lưu 24 giờ và không xoá thủ công được [[ref:https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/intune/device-management/actions/locate.md]].
**Nội dung bài thi.** Bài làm nằm trên ổ đĩa máy thuê cho tới khi được nộp lên máy chủ của trường. ExamLap không đọc, không sao chép, không sao lưu, và không có kênh kỹ thuật nào để làm việc đó.
:::

## Nguyên tắc tối thiểu hoá và thời hạn xoá

Nguyên tắc tối thiểu hoá dễ viết vào slide và rất khó giữ khi vận hành, vì áp lực luôn đẩy về phía "cứ lưu
thêm, biết đâu sau này cần". Nhóm chống lại bằng ba cơ chế kỹ thuật thay vì bằng lời hứa.

**Thứ nhất, hạn xoá là một cột trong cơ sở dữ liệu, không phải một dòng trong chính sách.** Mỗi hồ sơ xác
minh mang cột `images_purge_at`, đặt bằng ngày kết thúc lượt thuê cuối cộng 90 ngày. Mỗi bộ ảnh hiện trạng
mang hạn 12 tháng. Một tác vụ nền chạy hằng đêm quét các bản ghi quá hạn, xoá tệp trong kho ảnh, rồi ghi
một bản ghi kiểm toán nói rõ đã xoá cái gì vào lúc nào mà không giữ lại nội dung đã xoá. Bộ ba mã hoá khi
lưu, hạn xoá tự động và nhật ký truy cập chính là điều kiện tối thiểu mà các dự án xử lý dữ liệu giấy tờ tuỳ
thân tự đặt ra cho mình [[ref:https://github.com/huyhuynh1905/flutter-cccd-nfc-reader]], và cũng là phần mà
tài liệu của các bộ công cụ eKYC thương mại đẩy hoàn toàn về phía bên tích hợp [[ref:https://pub.dev/packages/finos_ekyc_flutter]].

**Thứ hai, việc xoá đi qua bảng hàng đợi có thể thử lại.** Xoá tệp trên kho ảnh là thao tác với dịch vụ bên
ngoài, có thể thất bại giữa chừng; nếu gọi trực tiếp trong giao dịch cơ sở dữ liệu thì hoặc là xoá rồi mà
bản ghi vẫn còn, hoặc là bản ghi mất mà tệp vẫn nằm đó. Mẫu hộp thư đi ghi việc cần làm vào một bảng trong
cùng giao dịch với dữ liệu nghiệp vụ, rồi một tiến trình nền đọc bảng đó và thực thi, là cách xử lý chuẩn cho
bài toán này [[ref:https://milanjovanovic.tech/blog/implementing-the-outbox-pattern]]. Hệ quả thực tế: một
lần xoá thất bại sẽ được thử lại chứ không im lặng biến mất.

**Thứ ba, có phép đo định kỳ chứng minh việc xoá đã xảy ra.** Mỗi tháng nhóm chạy một truy vấn liệt kê mọi
hồ sơ có `images_purge_at` đã qua mà vẫn còn tệp trong kho ảnh; kết quả phải bằng không, và con số này nằm
trong báo cáo vận hành hằng tháng. Một chính sách xoá không có phép đo thì không phân biệt được với một
chính sách xoá không được thực thi.

Nhật ký kiểm toán là ngoại lệ có chủ ý: nó được giữ lâu hơn mọi loại dữ liệu khác, vì đó là thứ duy nhất
chứng minh được ai đã làm gì khi có tranh chấp, và vì bản thân nó phải là một chuỗi liền mạch mới có giá trị
làm bằng chứng [[ref:https://dev.to/codemalasartes/an-immutable-audit-trail-for-ai-agent-actions-fastapi-async-sqlalchemy-4m4c]]. Nhưng sau 24 tháng, các trường nhận dạng trong nhật ký được
thay bằng mã ẩn danh, giữ lại chuỗi sự kiện mà bỏ đi khả năng quy về một con người cụ thể. Tính bất biến của
nhật ký là nền tảng của chuỗi bảo quản bằng chứng [[ref:https://www.locatorx.com/blog/the-truth-about-asset-records-why-immutability-is-the-foundation-of-a-verifiable-chain-of-custody]],
và việc ẩn danh hoá về sau là cách giữ được tính bất biến mà không giữ dữ liệu cá nhân vô thời hạn.

## Nghĩa vụ theo pháp luật Việt Nam về dữ liệu cá nhân

:::warn Giới hạn của phần này
Toàn bộ các cổng văn bản pháp luật Việt Nam đều không mở được trong phiên nghiên cứu của nhóm, nên các nghĩa
vụ dưới đây được trình bày ở dạng **danh mục cần kiểm chứng**, không phải trích dẫn nguyên văn. Nhóm phải mở
lại từng văn bản trên [thuvienphapluat.vn](https://thuvienphapluat.vn) [[ref:https://thuvienphapluat.vn]] hoặc
cơ sở dữ liệu quốc gia về văn bản pháp luật, và nhờ người có chuyên môn pháp lý rà soát trước khi vận hành
thật. Phân tích pháp lý đầy đủ của dự án nằm ở Chương 17; chương này chỉ nêu phần chạm tới thiết kế hệ thống.
:::

Khung pháp lý mà nhóm xác định được gồm **Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân**, cùng với
**Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15** được ghi nhận là có hiệu lực từ 01/01/2026 và **Nghị định
356/2025/NĐ-CP** hướng dẫn thi hành **[Cần kiểm chứng]**. Số hiệu và ngày hiệu lực của hai văn bản sau là
phần nhóm phải xác minh đầu tiên, vì nếu luật đã có hiệu lực thì nghĩa vụ nặng hơn nghị định cũ.

| Nghĩa vụ **[Cần kiểm chứng]** | ExamLap đáp ứng bằng cách nào |
|---|---|
| Dữ liệu sinh trắc học thuộc nhóm dữ liệu cá nhân nhạy cảm, có chế độ bảo vệ cao hơn | Không lưu ảnh giấy tờ quá hạn; lưu vector đặc trưng và một ảnh chân dung độ phân giải thấp dùng cho khâu bàn giao; mã hoá khi lưu; hạn xoá 90 ngày; mọi lần truy cập đều vào nhật ký; thông tin đăng nhập dịch vụ eKYC chỉ nằm ở máy chủ [[ref:https://github.com/VNQuy94/vnpt-ekyc-poc]] |
| Sự đồng ý phải rõ ràng, tách bạch, nêu rõ mục đích và thời hạn | Màn hình xác minh có ô tích riêng cho dữ liệu sinh trắc học, tách khỏi ô đồng ý điều khoản dịch vụ; nội dung ô ghi đúng ba điều: thu cái gì, để làm gì, xoá sau bao lâu; từ chối ô này vẫn thuê được máy, chỉ là phải xác minh tại quầy |
| Phải lập hồ sơ đánh giá tác động xử lý dữ liệu cá nhân | Bảng kê dữ liệu ở mục trên chính là bộ khung của hồ sơ này. Nhóm chưa có pháp nhân nên chưa nộp được; đây là mốc bắt buộc trước khi chuyển sang vận hành có thu tiền quy mô lớn |
| Chủ thể dữ liệu có quyền truy cập, xoá và rút lại sự đồng ý | Chức năng tự tải về toàn bộ dữ liệu cá nhân có sẵn trong tài khoản; yêu cầu xoá được xử lý trong 72 giờ và cần hai người duyệt; rút lại đồng ý sinh trắc học thì hồ sơ chuyển về chế độ xác minh tại quầy thay vì khoá tài khoản |
| Phải thông báo khi xảy ra sự cố lộ dữ liệu | Quy trình 24 giờ đầu ở mục cuối chương, gồm thời hạn thông báo cho khách bị ảnh hưởng và cho cơ quan có thẩm quyền. Mốc thời gian luật định là điểm **[Cần kiểm chứng]** quan trọng nhất trong bảng này |
| Hạn chế chuyển tiếp dữ liệu cho bên thứ ba | Nhóm không chia sẻ dữ liệu khách cho bất kỳ bên nào ngoài nhà cung cấp hạ tầng và cổng thanh toán. Có ghi nhận quy định từ 28/9/2026 không được chia sẻ tiếp cho bên thứ ba thông tin khai thác từ VNeID, trừ hai ngoại lệ [[ref:https://luatvietnam.vn/linh-vuc-khac/thong-tin-khai-thac-tu-vneid-co-duoc-chia-se-tiep-cho-ben-thu-ba-khong-883-111530-article.html]] **[Cần kiểm chứng]** |
{caption: Ánh xạ nghĩa vụ pháp lý về dữ liệu cá nhân sang biện pháp cụ thể của ExamLap.}
{widths: 5.5,10.5}

Một nghĩa vụ nữa nằm ngoài phạm vi bảo vệ dữ liệu nhưng liên quan trực tiếp tới thiết kế: ExamLap **không
giữ bản gốc căn cước công dân, thẻ sinh viên hay bất kỳ giấy tờ tuỳ thân nào** của khách (Phụ lục C, Điều 5).
Đây vừa là điểm khác biệt thương mại so với các cửa hàng cho thuê giữ giấy tờ làm tin, vừa là cách tránh
hoàn toàn vùng rủi ro liên quan tới hành vi bị nghiêm cấm trong Luật Căn cước 2023 **[Cần kiểm chứng]**. Về
mặt định danh điện tử, nhóm cũng **không tự xưng là dịch vụ xác thực điện tử**, vì đó là ngành nghề có điều
kiện theo Nghị định 69/2024/NĐ-CP [[ref:https://thuvienphapluat.vn/van-ban/Cong-nghe-thong-tin/Nghi-dinh-69-2024-ND-CP-quy-dinh-dinh-danh-xac-thuc-dien-tu-597437.aspx]] [[ref:https://vanban.chinhphu.vn/?pageid=27160&docid=210491]],
và việc kết nối vào cơ sở dữ liệu quốc gia về dân cư có điều kiện riêng dành cho tổ chức [[ref:https://bocongan.gov.vn/chinh-sach-phap-luat/bai-viet/nghi-dinh-quy-dinh-ve-dinh-danh-va-xac-thuc-dien-tu-d1-t1418]].
ExamLap chỉ đối chiếu ảnh giấy tờ với khuôn mặt sống cho mục đích nội bộ của mình, và nói đúng như vậy trên
giao diện.

## Xoá dữ liệu người dùng giữa hai lượt thuê

Đây là cam kết bán hàng, nên nó phải chứng minh được. Một sinh viên đăng nhập Gmail, Facebook và ứng dụng
ngân hàng trên máy thuê; nếu người thuê kế tiếp khôi phục được những thứ đó thì dịch vụ chấm dứt trong một
cộng đồng khép kín như khu ký túc xá. Các nền tảng cho thuê thiết bị lớn đặt xoá dữ liệu thành một bước riêng
trong quy trình tân trang, không phải việc làm kèm [[ref:https://www.grover.com/at-en/g-about/asset-condition]].

**Quy trình kỹ thuật.** Máy quay về không bao giờ được chuyển thẳng sang trạng thái *Sẵn sàng*. Nó phải đi
qua bước khôi phục ảnh hệ điều hành chuẩn ở mức toàn ổ, ghi đè toàn bộ phân vùng chứ không chỉ phân vùng hệ
thống, rồi mới được kiểm tra tiếp. Bước này là mục 3 trong danh mục mười hai mục ở **Phụ lục D**, mất khoảng
20 phút và phần mềm không cho phép bỏ qua: thiếu một mục là máy không xuất hiện trong danh sách cho thuê.
Về mức độ, nhóm đặt mục tiêu đạt mức "Clear" theo **NIST SP 800-88 Rev.1 — Guidelines for Media Sanitization**
cho máy quay vòng nội bộ, và mức "Purge" khi máy rời khỏi tầm kiểm soát, tức là khi thanh lý, bán lại hoặc
mang đi sửa ngoài. Tên và nội dung tài liệu này là **[Cần kiểm chứng]**, nhóm chưa mở được bản gốc.

**Công cụ.** Nền là ảnh đĩa toàn ổ bung bằng Clonezilla hoặc Rescuezilla, cả hai đều miễn phí và mã nguồn mở.
Với máy nghi có dữ liệu nhạy cảm, hoặc trước mỗi học kỳ, nhóm chạy thêm một lượt xoá ở tầng firmware của ổ,
là ATA Secure Erase với ổ SATA hoặc NVMe Format NVM với ổ NVMe, vì ghi đè theo địa chỉ logic không chạm tới
các khối vật lý mà cơ chế san bằng hao mòn của SSD đã ánh xạ đi chỗ khác **[Cần kiểm chứng]**. BitLocker được
bật ngay từ lúc nhập kho, trước khi có bất kỳ dữ liệu khách nào, đúng thứ tự cần thiết để việc xoá khoá mã
hoá thực sự có giá trị. BitLocker chỉ có ở Windows Pro trở lên [[ref:https://www.microsoft.com/en-us/windows/business/compare-windows-11]],
thuật toán mặc định là XTS-AES 128 bit [[ref:https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/intune/device-configuration/endpoint-security/ref-disk-encryption-settings.md]],
và khoá phục hồi được ký gửi vào kho khoá của nhóm chứ không để trên máy [[ref:https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/intune/device-configuration/endpoint-security/encrypt-bitlocker-windows.md]].
Nhóm cố ý **không bật xác thực TPM kèm mã PIN trước khi khởi động**: bắt một sinh viên nhập thêm PIN vào
buổi sáng đi thi là đánh đổi tồi.

Ở giai đoạn sau, khi đội máy đủ lớn để chịu được chi phí giấy phép, có hai lựa chọn rút ngắn thời gian quay
vòng. Chế độ máy dùng chung của Windows cho phép đặt mốc xoá tài khoản là *ngay sau khi đăng xuất*, tức dữ
liệu phiên của khách biến mất ngay khi họ thoát [[ref:https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/intune/device-configuration/templates/ref-shared-device-settings-windows.md]],
nhưng chỉ chạy trên bản Pro và Enterprise [[ref:https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/intune/device-configuration/templates/configure-shared-device.md]].
Autopilot Reset đưa máy về trạng thái sạch bằng tổ hợp phím ngay tại màn hình khoá mà vẫn giữ cấu hình quản
lý [[ref:https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/autopilot/windows-autopilot-reset.md]].
Nhóm chưa dùng cả hai vì đều cần hạ tầng và giấy phép trả tiền theo người dùng. Một cạm bẫy nữa: chế độ xoá
sạch kèm ghi đè vùng trống của Intune có thể khiến một số máy không khởi động lại được
[[ref:https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/intune/device-management/actions/wipe.md]],
nên nhóm không dùng nó cho đội máy đang khai thác.

**Cách chứng minh với khách.** Ba việc, theo thứ tự sức nặng tăng dần. Một, mỗi lần máy quay vòng, hệ thống
sinh một bản ghi xoá dữ liệu gắn với mã tài sản, ghi thời điểm bắt đầu và kết thúc, công cụ và phiên bản,
kèm mã băm của ảnh hệ điều hành gốc đã bung. Hai, khách nhận máy thấy ngay trên ứng dụng dòng trạng thái
"máy này đã được khôi phục về ảnh gốc lúc HH:MM ngày DD/MM", lấy trực tiếp từ bản ghi đó chứ không phải do
nhân viên gõ tay. Ba, với máy rời khỏi đội, nhóm cấp một chứng nhận xoá dữ liệu ghi rõ mức áp dụng, kỹ thuật
và kết quả xác minh, trong đó xác minh là đọc mẫu ngẫu nhiên ở ít nhất năm vị trí trên ổ và chạy thử một công
cụ khôi phục tệp miễn phí trong hai phút **[Cần kiểm chứng]**. Xoá mà không xác minh thì chưa gọi là đã xoá.

## Bảo mật ứng dụng

| Tầng | Biện pháp | Mối đe doạ bị chặn |
|---|---|---|
| Truyền tải | Bắt buộc HTTPS trên toàn bộ đường dẫn, chuyển hướng tự động, bật HSTS | Nghe lén trên mạng không dây dùng chung của trường, chiếm phiên bằng cách hạ cấp giao thức |
| Xác thực | Đường dẫn một lần gửi tới email `@fpt.edu.vn`, không dùng mật khẩu cho sinh viên; tài khoản quản trị bắt buộc hai lớp | Dò mật khẩu, dùng lại mật khẩu lộ từ nơi khác, chiếm tài khoản quản trị |
| Phân quyền | Kiểm tra theo vai trò ở phía máy chủ cho từng đường dẫn API, kèm kiểm tra quyền sở hữu đối tượng | Xem đơn của người khác bằng cách đổi mã trên thanh địa chỉ |
| Lưu trữ | Mã hoá khi lưu, băm số căn cước, tách kho ảnh khỏi cơ sở dữ liệu, tài khoản ứng dụng bị thu hồi quyền sửa và xoá trên bảng nhật ký | Lộ dữ liệu khi máy chủ bị chiếm, chèn câu lệnh SQL để xoá dấu vết |
| Tải tệp lên | Chỉ nhận ảnh, kiểm tra loại tệp thật chứ không tin phần mở rộng, giới hạn dung lượng, đổi tên tệp, phục vụ lại qua đường dẫn ký có hạn | Tải mã độc lên dưới dạng ảnh, đoán đường dẫn để xem ảnh giấy tờ của người khác |
| Webhook | Kiểm chữ ký của cổng thanh toán trước khi đọc nội dung, khoá duy nhất theo mã giao dịch, trả mã 200 trước và xử lý sau | Giả webhook báo đã thanh toán, ghi trùng một giao dịch nhiều lần |
| Nhật ký | Chỉ ghi thêm ở cả tầng ứng dụng lẫn tầng cơ sở dữ liệu, nối chuỗi băm giữa các dòng | Người có quyền cơ sở dữ liệu sửa lén lịch sử thao tác |
{caption: Biện pháp bảo mật ứng dụng theo tầng, kèm mối đe doạ tương ứng.}
{widths: 2,7,7}

Ba lỗi phổ biến của ứng dụng web mà nhóm phòng ngay từ thiết kế, vì chúng đúng với bối cảnh dự án hơn phần
còn lại. **Thứ nhất là xem trộm đối tượng của người khác bằng cách đổi mã định danh:** mọi truy vấn đơn thuê
đều kèm điều kiện chủ sở hữu, không chỉ kèm mã đơn. **Thứ hai là thanh toán bị ghi trùng:** bảng giao dịch có
ràng buộc duy nhất trên cặp nhà cung cấp và mã giao dịch, nên nhận cùng một sự kiện mười lần vẫn chỉ ghi một
dòng, và các thao tác tạo giữ chỗ, tạo đơn đều nhận tiêu đề khoá chống lặp theo mẫu của Stripe
[[ref:https://stripe.com/blog/idempotency]] [[ref:https://brandur.org/idempotency-keys]] [[ref:https://httptoolkit.com/blog/idempotency-keys/]].
**Thứ ba là rò rỉ khoá bí mật ra phía trình duyệt:** mọi lời gọi tới dịch vụ eKYC và cổng thanh toán đều đi
qua máy chủ của nhóm, không có ngoại lệ [[ref:https://github.com/VNQuy94/vnpt-ekyc-poc]]. Các đường dẫn nhạy
cảm còn bị giới hạn tần suất, để một tài khoản bị chiếm cũng không quét được cả cơ sở dữ liệu trong vài phút.

## Nhật ký kiểm toán và ai giám sát người quản trị

Quản trị viên là vai trò có quyền lớn nhất trong hệ thống: duyệt hồ sơ xác minh, xem dữ liệu cá nhân, cấu
hình giá, khoá máy từ xa. Câu hỏi "ai canh người canh" vì thế không phải câu hỏi lý thuyết, nhất là khi cả
ba quản trị viên đều là thành viên nhóm sáng lập và đều quen nhau. Nhóm trả lời bằng bốn cơ chế.

**Nhật ký chỉ ghi thêm, chặn ở hai tầng.** Ở tầng ứng dụng, mã nguồn chỉ có hàm chèn dòng mới, không có hàm
sửa hay xoá. Ở tầng cơ sở dữ liệu, bảng `audit_logs` gắn trigger chặn `UPDATE` và `DELETE`, đồng thời thu hồi
quyền của tài khoản ứng dụng. Hai tầng vì tầng ứng dụng chỉ bảo vệ được nhóm khỏi lỗi của chính mình, còn
tầng cơ sở dữ liệu mới chặn được cả trường hợp chèn câu lệnh SQL [[ref:https://www.designgurus.io/answers/detail/how-do-you-enforce-immutability-and-appendonly-audit-trails]].

**Nối chuỗi băm giữa các dòng.** Mỗi dòng nhật ký lưu số thứ tự tăng đơn điệu, mã băm của dòng trước và mã
băm của chính nó, tính bằng SHA-256 trên mã băm trước cộng số thứ tự cộng nội dung dòng ở dạng chuẩn hoá
[[ref:https://tracehold.ai/blog/immutable-audit-log-hmac-hash-chain/]]. Việc này giải quyết đúng điểm yếu mà
chỉ riêng cơ chế chỉ ghi thêm không xử lý được: chỉ ghi thêm bảo vệ được khỏi lỗi của chính mã nguồn, nhưng
tự nó không chứng minh được với bên thứ ba rằng không ai có quyền truy cập cơ sở dữ liệu đã lặng lẽ sửa một
dòng [[ref:https://medium.com/@veritaschain/append-only-is-the-easy-part-e25820208213]] [[ref:https://aesirx.io/blog/compliance-one/immutable-audit-trails-when-your-audit-log-becomes-cryptographic-proof]].
Một tác vụ chạy hằng đêm quét toàn chuỗi tìm dòng bị đứt; phát hiện một dòng đứt là căn cứ để dừng hệ thống.

**Nguyên tắc hai người duyệt cho thao tác nhạy cảm.** Năm thao tác không ai được tự mình thực hiện, đúng danh sách ở Chương 5: khoá màn hình máy của khách, **thêm** một người vào danh sách chặn nội bộ, hoàn tiền ngoài phạm vi tiền cọc, khấu trừ vượt biểu phí công khai, và xoá dữ liệu cá nhân theo yêu cầu. Cả người yêu cầu, người phê duyệt và lý do đều vào nhật ký. Chiều ngược lại — gỡ khoá màn hình và gỡ một khách khỏi danh sách chặn — chỉ cần một người, và sự bất đối xứng đó là cố ý theo nguyên tắc thất bại an toàn: gây hại cho khách phải khó hơn sửa sai. Việc kết xuất hồ sơ một đơn ra tệp không cần hai người duyệt nhưng luôn được ghi nhật ký kèm lý do.

**Rà soát định kỳ và thông báo cho khách.** Mỗi tháng, một thành viên không phải người thao tác nhiều nhất
trong tháng đọc lại nhật ký các thao tác nhạy cảm, đối chiếu với đơn thuê tương ứng, và ghi kết quả vào biên
bản họp vận hành. Song song, mỗi khi có thao tác nhạy cảm chạm vào tài khoản của một khách cụ thể, gồm mở hồ
sơ xác minh, khoá máy, thêm vào danh sách chặn hoặc kết xuất hồ sơ, hệ thống tự gửi thông báo cho chính khách
đó nói rõ đã có thao tác gì và vào lúc nào. Đây là cơ chế giám sát rẻ nhất và mạnh nhất, vì người bị ảnh
hưởng luôn có động lực kiểm tra cao nhất. Nguyên tắc chung là mọi thao tác có ý nghĩa đều sinh một bản ghi
nhật ký, đúng cách các hệ thống quản lý tài sản trưởng thành đang làm
[[ref:https://deepwiki.com/grokability/snipe-it/4.4-activity-logging]] [[ref:https://www.emergentmind.com/topics/immutable-audit-log]].

## Kế hoạch ứng phó sự cố

Nhóm không có đội an ninh thông tin và sẽ không giả vờ là có. Kế hoạch dưới đây được viết cho ba sinh viên,
với những việc ba sinh viên làm được trong 24 giờ đầu. Người chịu trách nhiệm điều phối là quản trị viên trực
tuần; nếu không liên lạc được trong 30 phút thì quyền điều phối chuyển sang người tiếp theo trong danh sách.
Ba công cụ dùng chung cho cả bốn kịch bản: nhật ký kiểm toán nối chuỗi băm để dựng lại trình tự sự việc
[[ref:https://tracehold.ai/blog/immutable-audit-log-hmac-hash-chain/]], mã hoá ổ đĩa đã bật sẵn trên mọi máy
để hạ mức thiệt hại khi mất thiết bị vật lý [[ref:https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/intune/device-configuration/endpoint-security/encrypt-bitlocker-windows.md]],
và tác nhân chống trộm có hành động báo động, khoá máy cùng lịch sử vị trí thiết bị
[[ref:https://raw.githubusercontent.com/prey/mcp-prey/main/README.md]]. Mốc thời gian phải thông báo cho cơ
quan có thẩm quyền là điểm nhóm bắt buộc tra lại trong văn bản pháp luật hiện hành
[[ref:https://thuvienphapluat.vn]] **[Cần kiểm chứng]**.

| Kịch bản | 0 đến 2 giờ | 2 đến 8 giờ | 8 đến 24 giờ |
|---|---|---|---|
| **Lộ cơ sở dữ liệu** | Người trực cắt truy cập từ bên ngoài vào cơ sở dữ liệu, đổi toàn bộ khoá bí mật, buộc đăng xuất mọi phiên; chụp lại nhật ký để giữ bằng chứng | Xác định phạm vi bằng cách đối chiếu nhật ký truy cập với bảng kê dữ liệu ở chương này; xác định có ảnh giấy tờ hay vector khuôn mặt trong phạm vi không | Thông báo cho từng khách trong phạm vi, nói rõ trường dữ liệu nào bị ảnh hưởng và khuyến nghị cụ thể; chuẩn bị thông báo cho cơ quan có thẩm quyền theo thời hạn luật định **[Cần kiểm chứng]** |
| **Mất thiết bị chứa dữ liệu** (máy của nhân viên, ổ cứng sao lưu) | Thu hồi phiên đăng nhập của thiết bị đó; kiểm tra thiết bị có bật mã hoá ổ đĩa không; nếu có thì rủi ro giảm mạnh | Kiểm tra thiết bị có chứa bản sao ảnh hiện trạng hay ảnh giấy tờ không; các thiết bị làm việc chỉ được phép truy cập qua trình duyệt, không giữ bản sao cục bộ | Nếu xác định có dữ liệu cá nhân trên thiết bị mất, xử lý như kịch bản lộ cơ sở dữ liệu với phạm vi tương ứng; rà lại quy định cấm giữ bản sao cục bộ |
| **Tài khoản quản trị bị chiếm** | Vô hiệu hoá tài khoản đó, đổi yếu tố xác thực hai lớp, buộc đăng xuất toàn hệ thống | Đọc lại nhật ký kiểm toán trong toàn bộ khoảng thời gian nghi ngờ, đặc biệt các thao tác hai người duyệt; kiểm tra chuỗi băm của nhật ký có đứt đoạn không | Hoàn tác các thao tác trái phép bằng bản ghi đính chính mới, không sửa bản ghi cũ; thông báo cho mọi khách có tài khoản bị thao tác |
| **Nhà cung cấp bên thứ ba bị tấn công** (hạ tầng, cổng thanh toán, dịch vụ eKYC) | Ngắt tích hợp bị ảnh hưởng, chuyển sang quy trình thủ công đã có sẵn: xác minh tại quầy, thu tiền chuyển khoản đối soát tay | Thu hồi và cấp lại toàn bộ khoá bí mật dùng với nhà cung cấp đó, việc này khả thi vì khoá chỉ nằm ở máy chủ [[ref:https://github.com/VNQuy94/vnpt-ekyc-poc]]; rà nhật ký webhook tìm nội dung giả mạo bằng kiểm chữ ký [[ref:https://matheuspalma.com/blog/outbound-webhook-delivery-signing-retries-dead-letters]] | Yêu cầu nhà cung cấp trả lời bằng văn bản về phạm vi; thông báo cho khách nếu dữ liệu của họ nằm trong phạm vi |
{caption: Bốn kịch bản sự cố và các bước xử lý trong 24 giờ đầu.}
{widths: 3,4.5,4.3,4.7}
{note: Mọi bước trong bảng đều ghi vào nhật ký kiểm toán ngay khi thực hiện. Thời hạn thông báo cho cơ quan có thẩm quyền là điểm phải xác minh trong văn bản pháp luật trước khi vận hành thật.}

Hai nguyên tắc chạy xuyên suốt bốn kịch bản. **Một, thông báo sớm và nói đúng phạm vi, kể cả khi chưa biết
hết:** một thông báo nói "chúng tôi đang xác định phạm vi, dưới đây là những gì đã biết" tốt hơn im lặng ba
ngày rồi công bố một báo cáo đầy đủ. **Hai, không bao giờ sửa dữ liệu cũ để làm đẹp hồ sơ:** mọi sửa chữa
đều làm bằng bản ghi mới tham chiếu tới bản ghi cũ. Đây là lý do toàn bộ thiết kế nhật ký ở mục trên tồn tại,
và nó chỉ có giá trị nếu nhóm giữ đúng nguyên tắc vào đúng ngày việc giữ nó khó nhất.

:::risk Điểm yếu nhóm tự nhận
Ba điểm. **Một**, nhóm chưa có pháp nhân nên chưa lập được hồ sơ đánh giá tác động xử lý dữ liệu cá nhân theo
đúng thủ tục, và đây là rào cản phải vượt trước khi thu dữ liệu sinh trắc học ở quy mô thật. **Hai**, toàn bộ
phần nghĩa vụ pháp lý trong chương này mang nhãn [Cần kiểm chứng] vì nhóm chưa mở được văn bản gốc; đây là
việc đầu tiên phải làm, không phải việc để sau. **Ba**, ba quản trị viên đều là người trong nhóm, nên nguyên
tắc hai người duyệt chỉ có giá trị chừng nào ba người không cùng đồng thuận làm sai. Cơ chế kỹ thuật không
giải quyết được điều đó; chỉ có nhật ký bất biến và việc thông báo cho khách là giữ lại được dấu vết.
:::
