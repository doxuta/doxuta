# -*- coding: utf-8 -*-
"""Sinh các hình minh hoạ (không phải ảnh chụp màn hình) cho bản proposal."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "figures")
os.makedirs(OUT, exist_ok=True)

def fig(name, title, sub, body, width=1240):
    html = f"""<!doctype html><html lang="vi"><head><meta charset="utf-8">
<link rel="stylesheet" href="../fig.css"><style>body{{width:{width}px}}</style></head>
<body><div class="fig"><div class="fig-t">{title}</div><div class="fig-s">{sub}</div>
{body}</div></body></html>"""
    open(os.path.join(OUT, name + ".html"), "w", encoding="utf-8").write(html)
    return name


# ---------------------------------------------------- F1: bản đồ hành trình
def f_journey():
    phases = ["1 · NHẬN RA VẤN ĐỀ<br><span style='font-weight:400;opacity:.8'>tối hôm trước / sáng ngày thi</span>",
              "2 · TÌM GIẢI PHÁP<br><span style='font-weight:400;opacity:.8'>5 phút sau đó</span>",
              "3 · ĐẶT MÁY<br><span style='font-weight:400;opacity:.8'>dưới 3 phút</span>",
              "4 · NHẬN MÁY<br><span style='font-weight:400;opacity:.8'>trước giờ thi 30 phút</span>",
              "5 · THI<br><span style='font-weight:400;opacity:.8'>trong ca thi</span>",
              "6 · TRẢ MÁY<br><span style='font-weight:400;opacity:.8'>ngay sau ca thi</span>"]
    rows = [
      ("Sinh viên làm gì",
       ["Bật máy, thấy máy không lên nguồn / EOS báo lỗi / quên sạc",
        "Hỏi bạn cùng lớp, tìm Google, hỏi group Facebook lớp",
        "Mở web, chọn ca thi, chọn máy, xác minh, chuyển khoản",
        "Đến sảnh, quét QR, kiểm tra máy cùng nhân viên, ký nhận",
        "Đăng nhập EOS, làm bài, nộp bài",
        "Quay lại sảnh, quét QR trả, nhận lại tiền cọc"]),
      ("Cảm xúc",
       ["😰 <span class='pain'>Hoảng</span>", "😟 <span class='pain'>Lo, vội</span>",
        "🤔 <span class='mut'>Nghi ngờ: có kịp không, có bị lừa không</span>",
        "😌 <span class='gain'>Nhẹ nhõm</span>", "🙂 <span class='gain'>Tập trung</span>",
        "😄 <span class='gain'>Hài lòng</span>"]),
      ("Điểm đau hiện nay<br><span class='sm mut' style='font-weight:400'>khi CHƯA có dịch vụ</span>",
       ["<span class='pain'>Không có phương án B.</span> Sửa máy mất vài ngày, mua máy mới không kịp",
        "<span class='pain'>Cửa hàng cho thuê chỉ tính theo ngày/tháng</span>, cần giấy tờ thế chấp, không mở lúc 6 giờ sáng",
        "<span class='pain'>Phải gọi điện, trả giá, chờ báo giá</span>, không biết còn máy hay không",
        "<span class='pain'>Phải đi xa lấy máy</span>, máy chưa cài EOS và SEB",
        "<span class='pain'>Máy lạ, chưa test</span> — rủi ro lỗi ngay giữa giờ thi",
        "<span class='pain'>Giữ CCCD/thẻ sinh viên</span> nên phải quay lại lấy"]),
      ("ExamLap giải quyết",
       ["<b>Có phương án B hiển thị ngay</b> khi tìm kiếm, biết còn máy hay không trong 5 giây",
        "<b>Thuê theo CA THI</b> (4 giờ), giá bằng một bữa ăn trưa; đặt được lúc 5 giờ sáng",
        "<b>Đặt online hoàn toàn</b>, giá niêm yết, tồn kho thời gian thực, giữ chỗ 10 phút",
        "<b>Nhận ngay tại sảnh</b>, máy đã cài sẵn EOS + SEB và đã chạy thử",
        "<b>Cam kết đổi máy trong 15 phút</b> nếu máy lỗi giữa ca thi",
        "<b>Không giữ giấy tờ</b>; cọc hoàn tự động trong 5 phút"]),
      ("Chỉ số theo dõi",
       ["Lượt tìm kiếm theo từ khoá khẩn cấp", "Tỉ lệ vào trang → bắt đầu đặt",
        "Tỉ lệ hoàn tất đặt · thời gian đặt trung bình", "Thời gian bàn giao · tỉ lệ đúng giờ",
        "Số sự cố giữa ca thi / 100 lượt", "Tỉ lệ hoàn cọc đúng hạn · điểm hài lòng"]),
    ]
    cells = ""
    for p in phases:
        cells += f'<div class="hd">{p}</div>'
    grid = f'<div class="jm" style="grid-template-columns:132px repeat(6,1fr)"><div class="hd"></div>{cells}'
    for label, vals in rows:
        grid += f'<div class="rl">{label}</div>'
        for v in vals:
            grid += f'<div class="cell">{v}</div>'
    grid += "</div>"
    return fig("f1-hanh-trinh", "Bản đồ hành trình khách hàng",
               "Sinh viên Đại học FPT Đà Nẵng gặp sự cố máy tính trước ca thi — so sánh hiện trạng và sau khi có ExamLap",
               grid, width=1560)


# ---------------------------------------------------- F2: canvas mô hình kinh doanh
def f_bmc():
    def c(title, items, cls="", span=""):
        li = "".join(f"<li>{i}</li>" for i in items)
        return f'<div class="c {cls}" style="{span}"><h5>{title}</h5><ul>{li}</ul></div>'
    body = '<div class="bmc">'
    body += c("Đối tác chính", ["Cửa hàng laptop cũ tại Đà Nẵng (nguồn máy, bảo hành)",
        "Tiệm sửa laptop (SLA sửa trong 24 giờ)", "Cổng đối soát VietQR (SePay/Casso)",
        "Nhà cung cấp eKYC", "CLB sinh viên, Phòng Công tác sinh viên",
        "Quán cà phê/ký túc xá làm điểm nhận máy phụ"], span="grid-row:span 2")
    body += c("Hoạt động chính", ["Chuẩn bị máy chuẩn thi (EOS + SEB, chạy thử)",
        "Bàn giao và thu hồi đúng giờ", "Xác minh danh tính người thuê",
        "Bảo trì, thay pin, vệ sinh máy", "Vận hành phần mềm đặt thuê"])
    body += c("Giá trị mang lại", ["<b>Máy sẵn sàng thi</b>, không phải máy chung chung",
        "<b>Thuê theo ca thi</b> — đơn vị thời gian đúng với nhu cầu",
        "<b>Đặt được lúc 5 giờ sáng</b>, giữ chỗ tức thì",
        "<b>Không giữ giấy tờ tuỳ thân</b>",
        "<b>Đổi máy trong 15 phút</b> nếu hỏng giữa ca thi",
        "<b>Hoàn cọc tự động</b> trong 5 phút"], span="grid-row:span 2")
    body += c("Quan hệ khách hàng", ["Tự phục vụ hoàn toàn trên web",
        "Hỗ trợ người thật qua Zalo trong giờ thi", "Điểm tín nhiệm: thuê nhiều → cọc thấp dần",
        "Nhắc lịch thi chủ động theo học kỳ"])
    body += c("Phân khúc khách hàng", ["<b>Chính:</b> sinh viên ĐH FPT Đà Nẵng có ca thi trong 48 giờ tới",
        "Sinh viên làm đồ án cần máy cấu hình cao ngắn hạn",
        "Sinh viên năm nhất chưa kịp mua máy",
        "<b>Mở rộng:</b> sinh viên các trường khác ở Đà Nẵng, thí sinh thi chứng chỉ"], span="grid-row:span 2")
    body += c("Nguồn lực chính", ["Đội 18 laptop đã chuẩn hoá cấu hình thi",
        "Ảnh hệ điều hành chuẩn (golden image) cài sẵn EOS/SEB",
        "Phần mềm đặt thuê tự xây", "Kho nhỏ + tủ sạc gần cổng trường",
        "Uy tín trong cộng đồng sinh viên"])
    body += c("Kênh phân phối", ["Website (là sản phẩm, không chỉ là kênh)",
        "Group Facebook và confession sinh viên FPT", "Đại sứ sinh viên mỗi khoá",
        "Booth trước tuần thi", "Giới thiệu truyền miệng"])
    body += c("Cơ cấu chi phí", ["<b>Vốn đầu tư:</b> mua 18 máy (~150 triệu), phụ kiện, tủ sạc",
        "<b>Cố định/tháng:</b> kho, hosting, tên miền, phần mềm MDM",
        "<b>Biến đổi:</b> công part-time theo ca thi, phí đối soát, chi phí sửa chữa",
        "<b>Dự phòng:</b> quỹ rủi ro hư hỏng và mất máy"], "money", "grid-column:span 2")
    body += c("Dòng doanh thu", ["<b>Phí thuê theo ca thi</b> (nguồn chính)",
        "<b>Phí miễn trừ thiệt hại</b> tự chọn (biên cao)",
        "Gói thuê tuần/tháng cho mùa đồ án (làm phẳng doanh thu ngoài mùa thi)",
        "Phí trả trễ", "Thanh lý máy sau 24–30 tháng"], "money", "grid-column:span 3")
    body += "</div>"
    return fig("f2-bmc", "Canvas mô hình kinh doanh (Business Model Canvas)",
               "Chín ô theo khung Osterwalder, áp dụng cho ExamLap giai đoạn khởi động 18 máy", body, width=1560)


# ---------------------------------------------------- F3: lớp phòng thủ
def f_layers():
    L = [("1","Sàng lọc đầu vào — ai được thuê",
          "eKYC đối chiếu ảnh CCCD với khuôn mặt sống; bắt buộc email <b>@fpt.edu.vn</b> và mã số sinh viên; đối chiếu danh sách chặn nội bộ. Người không phải sinh viên của trường không thuê được ở giai đoạn đầu."),
         ("2","Ràng buộc kinh tế — mất gì nếu gian",
          "Tiền cọc 250.000–400.000đ (3–5% giá trị máy) cộng phí miễn trừ thiệt hại. Quan trọng hơn tiền: <b>mất quyền dùng dịch vụ cho toàn bộ kỳ thi còn lại</b> và mất điểm tín nhiệm đã tích luỹ."),
         ("3","Bằng chứng — chứng minh được chuyện gì đã xảy ra",
          "Hợp đồng thuê tài sản điện tử có chữ ký; biên bản bàn giao kèm 6 ảnh hiện trạng có mã băm SHA-256; nhật ký hệ thống chỉ ghi thêm, không sửa được. Đây là hồ sơ dùng được khi phải làm việc với cơ quan chức năng."),
         ("4","Kiểm soát kỹ thuật — làm cho việc chiếm đoạt trở nên vô ích",
          "Tác nhân MDM check-in mỗi 15 phút; khoá màn hình từ xa khi quá hạn (cần hai người duyệt); BitLocker + mật khẩu BIOS + chặn khởi động từ USB; khắc laser mã tài sản lên vỏ và tem niêm phong vỡ. Máy bị khắc mã rất khó bán lại."),
         ("5","Pháp lý — đường cuối cùng",
          "Nhắc nợ bằng văn bản, sau đó trình báo theo <b>Điều 175 Bộ luật Hình sự 2015</b> (lạm dụng tín nhiệm chiếm đoạt tài sản). Ngưỡng giá trị của một chiếc laptop nằm trong phạm vi xử lý hình sự, và sinh viên chịu thêm chế tài của nhà trường.")]
    body = ""
    for n, t, d in L:
        body += f'<div class="layer"><div class="n">{n}</div><div class="b"><h5>{t}</h5><p>{d}</p></div></div>'
    body += """<div class="box soft" style="margin-top:13px">
    <h4>Nguyên tắc thiết kế</h4>
    <p style="font-size:12.5px;color:#374151">Không lớp nào trong năm lớp trên là tuyệt đối. Mục tiêu không phải là
    làm cho việc lấy cắp trở nên <i>bất khả thi</i> — điều đó không tồn tại với một tài sản di động — mà là làm cho
    <b>kỳ vọng lợi ích của kẻ gian thấp hơn hẳn chi phí và rủi ro</b>, đồng thời giữ trải nghiệm của 99% khách
    hàng trung thực ở mức nhẹ nhàng. Đây là lý do chúng tôi chọn <b>cọc thấp + danh tính mạnh</b> thay vì
    <b>cọc cao + danh tính yếu</b> như phần lớn cửa hàng cho thuê hiện nay.</p></div>"""
    return fig("f3-phong-thu", "Năm lớp phòng thủ chống thất thoát tài sản",
               "Mỗi lớp xử lý một loại rủi ro khác nhau; kẻ gian phải vượt qua cả năm", body, width=1240)
