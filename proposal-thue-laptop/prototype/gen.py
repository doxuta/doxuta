# -*- coding: utf-8 -*-
"""Sinh các màn hình nguyên mẫu (HTML) của ExamLap để chụp ảnh minh hoạ."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "screens")
os.makedirs(OUT, exist_ok=True)

def page(name, body, title="ExamLap", width=1180):
    html = f"""<!doctype html><html lang="vi"><head><meta charset="utf-8">
<title>{title}</title><link rel="stylesheet" href="../app.css"></head>
<body>{body}</body></html>"""
    open(os.path.join(OUT, name + ".html"), "w", encoding="utf-8").write(html)
    return name

LOGO = '<div class="logo"><span class="mark">EL</span> ExamLap</div>'

def nav(active="Trang chủ"):
    items = ["Trang chủ", "Thuê máy", "Bảng giá", "Cách hoạt động", "Hỗ trợ"]
    links = "".join(f'<a class="{"on" if i==active else ""}">{i}</a>' for i in items)
    return f"""<header class="nav"><div class="wrap">{LOGO}<nav>{links}</nav>
<div class="center"><span class="tag ok"><span class="dot"></span>Còn 6/10 máy hôm nay</span>
<button class="btn pri sm">Đặt máy ngay</button></div></div></header>"""

def side(active):
    groups = [
      ("Vận hành", [("Bảng điều khiển","dash"),("Đơn thuê","orders"),("Lịch giao – nhận","cal"),("Sự cố &amp; bồi thường","inc")]),
      ("Tài sản", [("Kho máy","inv"),("Bảo trì","maint"),("Nhật ký thiết bị","log")]),
      ("Khách hàng", [("Người thuê","cus"),("Hồ sơ eKYC","kyc"),("Danh sách chặn","block")]),
      ("Khác", [("Báo cáo","rep"),("Cấu hình giá","price"),("Nhật ký kiểm toán","audit")]),
    ]
    out = [f'<aside class="side">{LOGO}']
    for g, items in groups:
        out.append(f'<div class="sec">{g}</div>')
        for label, key in items:
            out.append(f'<a class="{"on" if key==active else ""}">{label}</a>')
    out.append("</aside>")
    return "".join(out)

def topbar(title, right=""):
    return f"""<div class="topbar"><div><b style="color:#142C4A;font-size:15px">{title}</b>
<span class="sub" style="margin-left:10px">Kỳ thi FA26 · Tuần 3</span></div>
<div class="center">{right}<span class="tag blue">Ca thi 07:30 · 7 đơn</span>
<div class="avatar">QT</div></div></div>"""

def kpi(label, value, delta=None, up=True, note=None):
    d = f'<div class="d {"up" if up else "dn"}">{delta}</div>' if delta else ""
    n = f'<div class="xs" style="margin-top:2px">{note}</div>' if note else ""
    return f'<div class="kpi"><div class="l">{label}</div><div class="v">{value}</div>{d}{n}</div>'

def table(headers, rows, nums=()):
    th = "".join(f'<th class="{"num" if i in nums else ""}">{h}</th>' for i, h in enumerate(headers))
    tr = ""
    for r in rows:
        tds = "".join(f'<td class="{"num" if i in nums else ""}">{c}</td>' for i, c in enumerate(r))
        tr += f"<tr>{tds}</tr>"
    return f'<table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>'

def steps(cur, labels=("Chọn máy &amp; ca thi","Xác minh eKYC","Cọc &amp; thanh toán","Nhận máy")):
    out = ['<div class="steps">']
    for i, l in enumerate(labels):
        cls = "done" if i < cur else ("on" if i == cur else "")
        mark = "✓" if i < cur else str(i + 1)
        out.append(f'<div class="step {cls}"><span class="n">{mark}</span>{l}</div>')
        if i < len(labels) - 1:
            out.append('<div class="step-line"></div>')
    out.append("</div>")
    return "".join(out)


# =========================================================== 1. TRANG CHỦ
def s_landing():
    machines = [
        ("Dell Latitude 5400", "i5-8365U · 8GB · 256GB SSD · jack 3.5mm", "79.000", "3 máy", "Nhóm A · thi EOS"),
        ("Dell Latitude 5410", "i5-10310U · 16GB · 256GB SSD", "99.000", "2 máy", "Nhóm B · lập trình"),
        ("Lenovo ThinkPad T490", "i5-8265U · 16GB · 512GB SSD", "129.000", "1 máy", "Nhóm C · cấu hình cao"),
    ]
    cards = ""
    for n, sp, p, avail, kind in machines:
        cards += f"""<div class="card"><div class="thumb" style="height:120px;border-radius:14px 14px 0 0;border:0">
        <span>ảnh máy</span></div><div class="card-b" style="padding:15px 17px">
        <div class="between"><h3 style="font-size:14.5px">{n}</h3><span class="tag ok">{avail}</span></div>
        <div class="xs" style="margin:5px 0 11px">{sp}</div>
        <div class="between"><div><span class="price" style="font-size:20px">{p}đ</span>
        <span class="xs">/ ca thi 4 giờ</span></div><button class="btn pri sm">Chọn</button></div></div></div>"""

    how = [("1","Đặt trước 30 phút","Chọn ca thi trên web. Hệ thống giữ máy và báo điểm nhận."),
           ("2","Xác minh 1 phút","Quét CCCD + selfie, đối chiếu mã số sinh viên. Chỉ làm một lần."),
           ("3","Nhận máy tại sảnh","Quét QR, ký biên bản điện tử, máy đã cài sẵn phần mềm thi."),
           ("4","Trả sau giờ thi","Quét QR trả máy. Cọc hoàn tự động trong 5 phút.")]
    hw = "".join(f"""<div class="card pad"><div class="center" style="gap:11px;margin-bottom:9px">
      <span class="mark" style="width:28px;height:28px;border-radius:8px;background:var(--blue-50);
      color:var(--blue);display:grid;place-items:center;font-weight:800;font-size:13px">{n}</span>
      <b style="color:#142C4A;font-size:14.5px">{t}</b></div>
      <div class="sub" style="line-height:1.5">{d}</div></div>""" for n, t, d in how)

    trust = [("2 phút","thời gian bàn giao trung bình"),("100%","máy được xoá sạch dữ liệu trước mỗi lượt"),
             ("15 phút","cam kết đổi máy nếu lỗi giữa ca thi"),("0đ","phí huỷ trước 2 giờ")]
    tr = "".join(f'<div><div class="big" style="font-size:25px">{a}</div><div class="xs">{b}</div></div>' for a, b in trust)

    body = f"""{nav("Trang chủ")}
<section style="background:linear-gradient(170deg,#fff 0%,#EAF1F9 100%);padding:56px 0 44px;
 border-bottom:1px solid var(--line)">
 <div class="wrap"><div class="row" style="gap:44px;align-items:center">
  <div style="flex:1.15">
   <div class="kicker">Dành riêng cho sinh viên Đại học FPT Đà Nẵng</div>
   <h1 style="margin:11px 0 15px">Máy hỏng sáng ngày thi<br>không còn là mất một môn.</h1>
   <p class="lead" style="max-width:530px">Thuê laptop theo <b>ca thi</b>, nhận máy ngay tại sảnh
   toà Alpha trước giờ thi 30 phút. Máy đã cài sẵn phần mềm thi, sạc đầy 100%, đã xoá sạch dữ liệu
   người dùng trước.</p>
   <div class="row" style="margin:24px 0 18px"><button class="btn acc lg">Đặt máy cho ca thi sắp tới</button>
   <button class="btn gho lg">Xem bảng giá</button></div>
   <div class="center" style="gap:8px"><span class="tag blue">Không giữ CCCD</span>
   <span class="tag blue">Cọc hoàn tự động</span><span class="tag blue">Hỗ trợ 07:00–21:00</span></div>
  </div>
  <div style="flex:.85"><div class="card pad" style="box-shadow:var(--sh)">
   <b style="color:#142C4A">Kiểm tra máy trống theo ca thi</b>
   <div class="hr" style="margin:13px 0"></div>
   <div class="field"><label>Ngày thi</label><div class="inp">Thứ Năm, 24/09/2026</div></div>
   <div class="field"><label>Ca thi</label><div class="inp">Ca 1 — 07:30 đến 09:30</div></div>
   <div class="field"><label>Nhu cầu</label><div class="inp ph">Thi trắc nghiệm / lập trình / đồ hoạ</div></div>
   <button class="btn pri blk lg">Tìm máy trống</button>
   <div class="xs" style="text-align:center;margin-top:10px">Miễn phí huỷ trước 2 giờ · Không cần thẻ tín dụng</div>
  </div></div>
 </div></div></section>

<section style="background:#fff;border-bottom:1px solid var(--line);padding:22px 0">
 <div class="wrap grid g4" style="text-align:center">{tr}</div></section>

<section class="wrap" style="padding:44px 0 10px">
 <div class="between" style="margin-bottom:18px"><h2>Máy sẵn sàng cho ca thi 24/09</h2>
 <a>Xem tất cả 10 máy →</a></div>
 <div class="grid g3">{cards}</div></section>

<section class="wrap" style="padding:38px 0 56px">
 <h2 style="margin-bottom:6px">Bốn bước, không giấy tờ thế chấp</h2>
 <p class="sub" style="margin-bottom:18px">Toàn bộ quy trình diễn ra trên điện thoại. Chúng tôi
 <b>không giữ CCCD</b> hay thẻ sinh viên của bạn.</p>
 <div class="grid g4">{hw}</div></section>"""
    return page("01-landing", body, "ExamLap — Thuê laptop đi thi")


# =========================================================== 2. DANH SÁCH MÁY
def s_catalog():
    rows = [
        ("Dell Latitude 5400","i5-8365U · 8GB · 256GB · jack 3.5mm","Nhóm A","79.000","Còn 3","ok"),
        ("ThinkPad T480","i5-8250U · 8GB · 256GB · jack 3.5mm","Nhóm A","79.000","Còn 2","ok"),
        ("Dell Latitude 5410","i5-10310U · 16GB · 256GB","Nhóm B","99.000","Còn 2","ok"),
        ("ThinkPad T480 16GB","i5-8350U · 16GB · 512GB","Nhóm B","99.000","Còn 1","warn"),
        ("ThinkPad T490","i5-8265U · 16GB · 512GB","Nhóm C","129.000","Đang bảo trì","risk"),
        ("Latitude 5400 (máy dự phòng)","i5-8365U · 8GB · 256GB","Nhóm A","79.000","Giữ cho hỗ trợ khẩn","warn"),
    ]
    cards = ""
    for n, sp, kind, price, avail, st in rows:
        dis = "opacity:.55;" if st == "risk" else ""
        btn = ('<button class="btn gho sm" style="pointer-events:none">Hết máy</button>' if st == "risk"
               else '<button class="btn pri sm">Chọn máy</button>')
        cards += f"""<div class="card" style="{dis}"><div class="row" style="padding:15px 17px;gap:15px;align-items:center">
        <div class="thumb" style="width:96px;height:66px;flex-shrink:0">ảnh</div>
        <div style="flex:1;min-width:0"><div class="center" style="gap:8px">
          <b style="color:#142C4A;font-size:14.5px">{n}</b><span class="pill">{kind}</span></div>
        <div class="xs" style="margin-top:4px">{sp}</div>
        <div class="center" style="gap:7px;margin-top:7px"><span class="tag {st}"><span class="dot"></span>{avail}</span>
        <span class="xs">Pin còn 92% · Đã kiểm 2 giờ trước</span></div></div>
        <div style="text-align:right"><div class="price" style="font-size:19px">{price}đ</div>
        <div class="xs" style="margin-bottom:8px">/ ca thi 4 giờ</div>{btn}</div></div></div>"""

    filt = """<div class="card pad" style="position:sticky;top:16px">
    <b style="color:#142C4A;font-size:14px">Bộ lọc</b><div class="hr" style="margin:12px 0"></div>
    <div class="field"><label>Ngày thi</label><div class="inp">24/09/2026</div></div>
    <div class="field"><label>Ca thi</label><div class="inp">Ca 1 · 07:30–09:30</div></div>
    <div class="field"><label>Điểm nhận máy</label><div class="inp">Sảnh toà Alpha — ĐH FPT ĐN</div></div>
    <div class="hr"></div>
    <label>Mục đích thi</label>
    <div class="col" style="gap:8px;margin-bottom:14px">
      <div class="center"><span class="ck on">✓</span><span class="sub">Trắc nghiệm / EOS</span></div>
      <div class="center"><span class="ck on">✓</span><span class="sub">Lập trình (IDE nặng)</span></div>
      <div class="center"><span class="ck"></span><span class="sub">Đồ hoạ / dựng hình</span></div>
      <div class="center"><span class="ck"></span><span class="sub">macOS bắt buộc</span></div>
    </div>
    <label>Giá mỗi ca</label><div class="inp">Dưới 60.000đ</div>
    <div class="hr"></div>
    <div class="note" style="font-size:12.5px">Hệ thống chỉ hiển thị máy <b>đã qua kiểm tra trong 24 giờ</b>
    và pin còn trên 80%.</div></div>"""

    body = f"""{nav("Thuê máy")}
<div class="wrap" style="padding:26px 0 44px">
 <div class="sub" style="margin-bottom:12px">Trang chủ › Thuê máy › Ca 1 ngày 24/09/2026</div>
 <div class="between" style="margin-bottom:16px"><div><h2>8 máy trống cho ca thi 07:30 – 09:30</h2>
 <div class="sub" style="margin-top:4px">Cập nhật lúc 21:14 · Giữ chỗ tự động 10 phút sau khi chọn</div></div>
 <div class="inp" style="width:auto">Sắp xếp: Giá thấp → cao</div></div>
 <div class="row" style="gap:20px;align-items:flex-start">
  <div style="width:266px;flex-shrink:0">{filt}</div>
  <div class="col" style="flex:1">{cards}</div>
 </div></div>"""
    return page("02-catalog", body, "Danh sách máy trống")


# =========================================================== 3. eKYC
def s_kyc():
    checks = [("Ảnh mặt trước CCCD","Đã đọc: số, họ tên, ngày sinh, quê quán","ok"),
              ("Ảnh mặt sau CCCD","Đã đọc mã MRZ, đối chiếu khớp mặt trước","ok"),
              ("Chống giả mạo (liveness)","Quay đầu trái – phải · điểm 0,96","ok"),
              ("So khớp khuôn mặt","Selfie ↔ ảnh CCCD · độ tương đồng 0,93","ok"),
              ("Đối chiếu mã số sinh viên","DE180xxx · Email @fpt.edu.vn đã xác thực OTP","ok"),
              ("Kiểm tra danh sách chặn","Không có lịch sử vi phạm","ok")]
    ck = "".join(f"""<div class="between" style="padding:11px 0;border-bottom:1px solid var(--line)">
      <div class="center" style="gap:11px"><span class="ck on">✓</span>
      <div><b style="font-size:13.5px;color:#142C4A">{a}</b><div class="xs" style="margin-top:2px">{b}</div></div></div>
      <span class="tag ok">Đạt</span></div>""" for a, b, s in checks)

    body = f"""{nav("Thuê máy")}
<div class="wrap" style="padding:26px 0 44px;max-width:960px">
 {steps(1)}
 <div class="row" style="gap:20px;align-items:flex-start">
  <div style="flex:1.35" class="col">
   <div class="card"><div class="card-h"><h3>Xác minh danh tính (eKYC)</h3>
     <span class="tag blue">Chỉ làm một lần duy nhất</span></div>
    <div class="card-b">
     <div class="note" style="margin-bottom:16px">Chúng tôi <b>không giữ CCCD bản cứng</b>. Ảnh chụp
     chỉ dùng để đối chiếu, được mã hoá và <b>tự động xoá sau 90 ngày</b> kể từ lần thuê cuối,
     theo Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân.</div>
     <div class="row" style="gap:14px;margin-bottom:16px">
       <div style="flex:1"><div class="thumb" style="height:118px">Mặt trước CCCD<br>(đã chụp)</div>
         <div class="xs" style="text-align:center;margin-top:6px">Chất lượng ảnh: tốt</div></div>
       <div style="flex:1"><div class="thumb" style="height:118px">Mặt sau CCCD<br>(đã chụp)</div>
         <div class="xs" style="text-align:center;margin-top:6px">Đọc được mã MRZ</div></div>
       <div style="flex:1"><div class="thumb" style="height:118px">Ảnh selfie<br>(liveness)</div>
         <div class="xs" style="text-align:center;margin-top:6px">Phát hiện người thật</div></div>
     </div>
     {ck}
     <div class="row" style="margin-top:18px;gap:10px">
       <button class="btn gho">Chụp lại</button>
       <button class="btn pri" style="flex:1">Xác nhận và sang bước cọc</button></div>
    </div></div>
   <div class="card pad"><b style="color:#142C4A;font-size:14px">Dữ liệu chúng tôi lưu và không lưu</b>
    <div class="hr" style="margin:11px 0"></div>
    <div class="grid g2" style="gap:12px">
      <div><div class="tag ok" style="margin-bottom:7px">CÓ LƯU</div>
        <div class="sub" style="line-height:1.7">• Số CCCD đã băm (hash)<br>• Họ tên, ngày sinh<br>
        • Mã số sinh viên<br>• Vector khuôn mặt (không phải ảnh)</div></div>
      <div><div class="tag risk" style="margin-bottom:7px">KHÔNG LƯU</div>
        <div class="sub" style="line-height:1.7">• Ảnh CCCD gốc quá 90 ngày<br>• Mật khẩu tài khoản trường<br>
        • Vị trí GPS của bạn<br>• Nội dung bài thi trên máy</div></div>
    </div></div>
  </div>
  <div style="width:296px;flex-shrink:0"><div class="card pad">
   <b style="color:#142C4A;font-size:14px">Đơn thuê của bạn</b><div class="hr" style="margin:11px 0"></div>
   <div class="row" style="gap:11px;margin-bottom:12px"><div class="thumb" style="width:72px;height:50px">ảnh</div>
    <div><b style="font-size:13.5px;color:#142C4A">Dell Latitude 5410</b>
    <div class="xs">Nhóm B · mã máy EL-5410-02</div></div></div>
   <div class="between" style="padding:5px 0"><span class="sub">Ca thi</span><b style="font-size:13px">24/09 · 07:30–09:30</b></div>
   <div class="between" style="padding:5px 0"><span class="sub">Nhận máy</span><b style="font-size:13px">07:00 · Sảnh Alpha</b></div>
   <div class="between" style="padding:5px 0"><span class="sub">Trả máy</span><b style="font-size:13px">10:00 · Sảnh Alpha</b></div>
   <div class="hr" style="margin:11px 0"></div>
   <div class="between" style="padding:4px 0"><span class="sub">Phí thuê ca thi 4 giờ</span><b>99.000đ</b></div>
   <div class="between" style="padding:4px 0"><span class="sub">Phí miễn trừ thiệt hại</span><b>15.000đ</b></div>
   <div class="between" style="padding:4px 0"><span class="sub">Tiền cọc (hoàn lại)</span><b>300.000đ</b></div>
   <div class="hr" style="margin:11px 0"></div>
   <div class="between"><b style="color:#142C4A">Cần thanh toán</b><span class="price" style="font-size:21px">414.000đ</span></div>
   <div class="xs" style="margin-top:9px">Trong đó <b>300.000đ tiền cọc được hoàn</b> tự động trong 5 phút sau khi trả máy nguyên vẹn.</div>
  </div></div>
 </div></div>"""
    return page("03-ekyc", body, "Xác minh eKYC")


# =========================================================== 4. CỌC & THANH TOÁN
def s_pay():
    body = f"""{nav("Thuê máy")}
<div class="wrap" style="padding:26px 0 44px;max-width:960px">
 {steps(2)}
 <div class="row" style="gap:20px;align-items:flex-start">
  <div style="flex:1.35" class="col">
   <div class="card"><div class="card-h"><h3>Đặt cọc và thanh toán</h3>
     <span class="tag warn">Giữ máy còn 08:42</span></div>
    <div class="card-b">
     <div class="row" style="gap:11px;margin-bottom:16px">
      <div class="card pad" style="flex:1;border-color:var(--blue);box-shadow:0 0 0 3px var(--blue-50)">
        <div class="center" style="gap:8px"><span class="ck on">✓</span>
        <b style="font-size:13.5px;color:#142C4A">Chuyển khoản VietQR</b></div>
        <div class="xs" style="margin-top:7px">Miễn phí · Đối soát tự động trong 5 giây</div></div>
      <div class="card pad" style="flex:1">
        <div class="center" style="gap:8px"><span class="ck"></span>
        <b style="font-size:13.5px;color:#142C4A">Ví MoMo</b></div>
        <div class="xs" style="margin-top:7px">Phí 1,5% · Hoàn cọc trong 24 giờ</div></div>
      <div class="card pad" style="flex:1;opacity:.6">
        <div class="center" style="gap:8px"><span class="ck"></span>
        <b style="font-size:13.5px;color:#142C4A">Trả sau (nợ cọc)</b></div>
        <div class="xs" style="margin-top:7px">Chỉ mở cho khách đã thuê ≥ 3 lần</div></div>
     </div>
     <div class="row" style="gap:22px;align-items:center;background:#FAFBFD;border:1px solid var(--line);
       border-radius:12px;padding:20px">
      <div class="qr"></div>
      <div style="flex:1">
       <div class="xs">Nội dung chuyển khoản bắt buộc</div>
       <div class="mono" style="font-size:17px;font-weight:700;color:#142C4A;margin:4px 0 12px">EL 8241 QR</div>
       <div class="between" style="padding:3px 0"><span class="sub">Ngân hàng</span><b style="font-size:13px">MB Bank</b></div>
       <div class="between" style="padding:3px 0"><span class="sub">Số tài khoản</span>
         <b class="mono" style="font-size:13px">0000 1234 5678</b></div>
       <div class="between" style="padding:3px 0"><span class="sub">Chủ tài khoản</span>
         <b style="font-size:13px">CTY TNHH EXAMLAP</b></div>
       <div class="between" style="padding:3px 0"><span class="sub">Số tiền</span>
         <b style="font-size:15px;color:var(--accent)">414.000đ</b></div>
      </div>
     </div>
     <div class="note ok" style="margin-top:16px"><b>Đang chờ tiền về…</b> Hệ thống nhận webhook từ
     cổng đối soát và tự động xác nhận đơn. Bạn không cần bấm gì thêm.</div>
     <div class="hr"></div>
     <b style="color:#142C4A;font-size:14px">Điều khoản bạn đang đồng ý</b>
     <div class="col" style="gap:9px;margin-top:11px">
      <div class="center" style="align-items:flex-start;gap:10px"><span class="ck on">✓</span>
        <span class="sub">Tôi đã đọc <a>Hợp đồng thuê tài sản điện tử</a> và <a>Biểu phí bồi thường</a>.</span></div>
      <div class="center" style="align-items:flex-start;gap:10px"><span class="ck on">✓</span>
        <span class="sub">Tôi đồng ý cho ExamLap xử lý dữ liệu cá nhân theo <a>Chính sách quyền riêng tư</a>
        cho mục đích xác minh và quản lý tài sản cho thuê.</span></div>
      <div class="center" style="align-items:flex-start;gap:10px"><span class="ck on">✓</span>
        <span class="sub">Tôi hiểu máy có cài phần mềm quản lý thiết bị (MDM) để định vị và khoá từ xa
        khi quá hạn trả, và phần mềm này <b>không đọc nội dung bài làm</b> của tôi.</span></div>
     </div>
    </div></div>
  </div>
  <div style="width:296px;flex-shrink:0" class="col">
   <div class="card pad">
    <b style="color:#142C4A;font-size:14px">Cơ chế cọc</b><div class="hr" style="margin:11px 0"></div>
    <div class="col" style="gap:11px">
     <div><div class="between"><span class="sub">Giá trị thay thế của máy</span><b style="font-size:13px">7.500.000đ</b></div>
      <div class="bar" style="margin-top:6px"><i style="width:100%"></i></div></div>
     <div><div class="between"><span class="sub">Cọc thu (4,0%)</span>
       <b style="font-size:13px;color:var(--accent)">300.000đ</b></div>
      <div class="bar" style="margin-top:6px"><i style="width:4%;background:var(--accent)"></i></div></div>
    </div>
    <div class="hr"></div>
    <div class="sub" style="line-height:1.65">Cọc thấp là <b>có chủ ý</b>. Rào cản chống mất máy của chúng tôi
    không nằm ở tiền cọc mà ở <b>danh tính đã xác minh</b>, <b>MDM khoá máy từ xa</b> và
    <b>hợp đồng có hiệu lực pháp lý</b>.</div>
   </div>
   <div class="card pad"><b style="color:#142C4A;font-size:14px">Hoàn cọc khi nào</b>
    <div class="hr" style="margin:11px 0"></div>
    <div class="col" style="gap:8px">
     <div class="between"><span class="sub">Trả đúng giờ, máy nguyên vẹn</span><span class="tag ok">100%</span></div>
     <div class="between"><span class="sub">Trả trễ dưới 60 phút</span><span class="tag warn">−20.000đ</span></div>
     <div class="between"><span class="sub">Xước vỏ nhẹ (cấp 1)</span><span class="tag warn">−50.000đ</span></div>
     <div class="between"><span class="sub">Mất sạc / chuột</span><span class="tag risk">−250.000đ</span></div>
     <div class="between"><span class="sub">Hỏng màn hình</span><span class="tag risk">Theo hoá đơn sửa</span></div>
    </div></div>
  </div>
 </div></div>"""
    return page("04-payment", body, "Đặt cọc và thanh toán")


# =========================================================== 5. VÉ NHẬN MÁY
def s_pass():
    tl = [("21:14 · 23/09","Đặt máy thành công","ok"),("21:15 · 23/09","Đã nhận cọc 300.000đ","ok"),
          ("06:40 · 24/09","Nhân viên đã chuẩn bị máy (wipe + sạc 100%)","ok"),
          ("07:00 · 24/09","Chờ bạn đến quét QR nhận máy","now"),
          ("10:00 · 24/09","Hạn trả máy","next"),("10:05 · 24/09","Hoàn cọc tự động","next")]
    items = ""
    for t, txt, st in tl:
        col = {"ok":"var(--ok)","now":"var(--accent)","next":"var(--line-2)"}[st]
        w = "700" if st == "now" else "400"
        items += f"""<div class="row" style="gap:13px;align-items:flex-start">
        <div style="width:11px;height:11px;border-radius:50%;background:{col};margin-top:4px;flex-shrink:0;
          box-shadow:0 0 0 3px {'#FDF1E7' if st=='now' else 'transparent'}"></div>
        <div style="flex:1;padding-bottom:15px;border-left:0"><div style="font-size:13.5px;font-weight:{w};
          color:{'#142C4A' if st!='next' else 'var(--muted)'}">{txt}</div>
        <div class="xs">{t}</div></div></div>"""

    body = f"""{nav("Thuê máy")}
<div class="wrap" style="padding:26px 0 44px;max-width:960px">
 {steps(3)}
 <div class="row" style="gap:20px;align-items:flex-start">
  <div style="flex:1.3" class="col">
   <div class="card" style="border-color:var(--ok);box-shadow:0 0 0 3px var(--ok-50)">
    <div class="card-b" style="text-align:center;padding:26px">
     <div class="tag ok" style="font-size:12.5px;padding:5px 13px">ĐƠN ĐÃ XÁC NHẬN</div>
     <div class="big" style="margin:13px 0 4px">EL-8241</div>
     <div class="sub" style="margin-bottom:20px">Đưa mã QR này cho nhân viên tại Sảnh toà Alpha</div>
     <div style="display:flex;justify-content:center"><div class="qr" style="width:176px;height:176px"></div></div>
     <div class="mono" style="margin-top:14px;font-size:15px;font-weight:700;color:#142C4A">EL8241-5410-02</div>
     <div class="hr"></div>
     <div class="grid g3" style="text-align:left">
      <div><div class="xs">Máy được gán</div><b style="font-size:13.5px;color:#142C4A">Dell Latitude 5410 · EL-5410-02</b></div>
      <div><div class="xs">Nhận máy</div><b style="font-size:13.5px;color:#142C4A">07:00 · Sảnh Alpha</b></div>
      <div><div class="xs">Trả máy</div><b style="font-size:13.5px;color:#142C4A">10:00 · Sảnh Alpha</b></div>
     </div>
    </div></div>
   <div class="card"><div class="card-h"><h3>Máy đã được chuẩn bị những gì</h3></div><div class="card-b">
    <div class="grid g2" style="gap:10px">
     <div class="center" style="gap:9px"><span class="ck on">✓</span><span class="sub">Cài đặt gốc, xoá sạch tài khoản trước</span></div>
     <div class="center" style="gap:9px"><span class="ck on">✓</span><span class="sub">Sạc đầy 100% · pin còn 92% dung lượng</span></div>
     <div class="center" style="gap:9px"><span class="ck on">✓</span><span class="sub">Cài sẵn trình duyệt thi, Office, IDE</span></div>
     <div class="center" style="gap:9px"><span class="ck on">✓</span><span class="sub">Đã test bàn phím, chuột, Wi‑Fi eduroam</span></div>
     <div class="center" style="gap:9px"><span class="ck on">✓</span><span class="sub">Vệ sinh máy và túi đựng</span></div>
     <div class="center" style="gap:9px"><span class="ck on">✓</span><span class="sub">Kèm sạc + chuột không dây + túi chống sốc</span></div>
    </div></div></div>
  </div>
  <div style="width:310px;flex-shrink:0" class="col">
   <div class="card pad"><b style="color:#142C4A;font-size:14px">Tiến trình đơn thuê</b>
    <div class="hr" style="margin:13px 0"></div>{items}</div>
   <div class="card pad" style="background:var(--accent-50);border-color:#F0C9B6">
    <b style="color:var(--accent);font-size:13.5px">Máy trục trặc giữa ca thi?</b>
    <div class="sub" style="margin:7px 0 11px;line-height:1.6">Gọi hotline, chúng tôi mang máy dự phòng
    đến phòng thi trong <b>15 phút</b> và không tính thêm phí.</div>
    <button class="btn acc blk sm">Gọi hỗ trợ khẩn 0905 xxx xxx</button></div>
  </div>
 </div></div>"""
    return page("05-pass", body, "Vé nhận máy")


# =========================================================== 6. APP NHÂN VIÊN
def s_staff():
    ck = [("Vỏ máy – 4 mặt","Không móp, xước cấp 0",True),("Màn hình","Không điểm chết, không sọc",True),
          ("Bàn phím & touchpad","Đủ phím, không kẹt",True),("Cổng kết nối","USB×2, HDMI, jack 3.5 OK",True),
          ("Pin & sạc","Pin 92% · sạc chính hãng",True),("Phụ kiện","Chuột, túi, sạc – đủ",True),
          ("Ảnh hiện trạng","Đã chụp 4 mặt + màn hình",False)]
    rows = "".join(f"""<div class="between" style="padding:11px 0;border-bottom:1px solid var(--line)">
      <div><div style="font-size:14px;font-weight:700;color:#142C4A">{a}</div>
      <div class="xs" style="margin-top:2px">{b}</div></div>
      <span class="ck {'on' if d else ''}" style="width:22px;height:22px">{'✓' if d else ''}</span></div>"""
      for a, b, d in ck)

    body = f"""<div style="display:flex;justify-content:center;padding:28px;background:#E8EDF4">
<div class="phone"><div class="phone-h">ExamLap Staff · 06:58</div>
<div style="padding:16px;background:#F7F9FC">
 <div class="between" style="margin-bottom:13px"><div><div class="xs">Đơn EL-8241</div>
  <b style="font-size:17px;color:#142C4A">Bàn giao máy</b></div>
  <span class="tag blue">Ca 1 · 07:30</span></div>
 <div class="card pad" style="margin-bottom:13px;padding:14px">
  <div class="between"><div class="center" style="gap:10px">
    <div class="avatar" style="width:36px;height:36px;font-size:13px">NA</div>
    <div><b style="font-size:14px;color:#142C4A">Nguyễn Văn A</b>
    <div class="xs">DE180xxx · đã xác minh eKYC</div></div></div>
   <span class="tag ok">Khớp</span></div>
  <div class="hr" style="margin:11px 0"></div>
  <div class="between"><span class="sub">Máy gán</span><b style="font-size:13px">EL-5410-02</b></div>
  <div class="between" style="margin-top:4px"><span class="sub">Cọc đã thu</span><b style="font-size:13px">300.000đ</b></div>
 </div>
 <div class="card pad" style="padding:14px 16px">
  <div class="between" style="margin-bottom:4px"><b style="font-size:14px;color:#142C4A">Biên bản kiểm tra</b>
   <span class="tag warn">6/7</span></div>
  {rows}
  <button class="btn pri blk" style="margin-top:14px">Chụp ảnh hiện trạng (còn 1 mục)</button>
  <button class="btn gho blk sm" style="margin-top:8px">Khách ký điện tử &amp; giao máy</button>
 </div>
 <div class="note warn" style="margin-top:13px;font-size:12.5px">Chưa đủ mục kiểm tra. Hệ thống
 <b>không cho phép</b> chuyển đơn sang trạng thái <i>Đang thuê</i> khi biên bản chưa đủ ảnh.</div>
</div></div></div>"""
    return page("06-staff", body, "App nhân viên — bàn giao")


# =========================================================== 7. BẢNG ĐIỀU KHIỂN
def s_dash():
    k = (kpi("Đơn đang thuê", "7", "▲ 3 so với ca trước", True, "2 đơn sắp đến hạn trả") +
         kpi("Tỉ lệ khai thác máy", "70%", "▲ 9 điểm tuần này", True, "7/10 máy đang ra khỏi kho") +
         kpi("Doanh thu tháng 9", "9,2 tr", "▲ 13% so tháng 8", True, "Kế hoạch 9,2 triệu") +
         kpi("Sự cố mở", "1", "▼ 2 so tuần trước", True, "1 vụ trả trễ đang xử lý"))

    orders = table(
      ["Mã đơn","Khách","Máy","Ca thi","Trạng thái","Cọc","Hạn trả"],
      [["<b>EL-8241</b>","Nguyễn Văn A","EL-5410-02","24/09 · Ca 1",'<span class="tag blue">Đang thuê</span>',"300.000đ","10:00"],
       ["<b>EL-8240</b>","Trần Thị B","EL-5400-01","24/09 · Ca 1",'<span class="tag blue">Đang thuê</span>',"300.000đ","10:00"],
       ["<b>EL-8239</b>","Lê Minh C","EL-5400-02","24/09 · Ca 1",'<span class="tag risk">Quá hạn 45′</span>',"300.000đ","09:15"],
       ["<b>EL-8238</b>","Phạm D","EL-5400-03","24/09 · Ca 2",'<span class="tag warn">Chờ nhận máy</span>',"300.000đ","14:00"],
       ["<b>EL-8237</b>","Vũ Thu E","chưa gán","24/09 · Ca 2",'<span class="tag ok">Đã thanh toán</span>',"150.000đ","14:00"],
       ["<b>EL-8236</b>","Đỗ Quang F","EL-T480-01","23/09 · Ca 3",'<span class="tag grey">Đã trả · hoàn cọc</span>',"—","đã xong"]],
      nums=())

    alerts = [("risk","Đơn EL-8239 quá hạn 45 phút","Đã gửi 2 tin nhắn. Bước tiếp theo: khoá máy từ xa lúc 10:15."),
              ("warn","Máy EL-T490-01 pin còn 71%","Dưới ngưỡng 80% — đã đưa vào bảo trì, thay pin trước kỳ thi cuối kỳ."),
              ("warn","Ca 2 ngày 25/09 sắp kín","Còn 2 máy trống trên 14 lượt đặt. Cân nhắc mở bán máy dự phòng."),
              ("note","3 hồ sơ eKYC chờ duyệt tay","Ảnh CCCD mờ, điểm so khớp 0,78–0,84.")]
    al = "".join(f"""<div class="note {t}" style="margin-bottom:9px"><b>{a}</b>
      <div class="xs" style="margin-top:3px;color:var(--ink-2)">{b}</div></div>""" for t, a, b in alerts)

    body = f"""<div class="admin">{side("dash")}<div class="main">
{topbar("Bảng điều khiển vận hành")}
<div class="page">
 <div class="grid g4" style="margin-bottom:18px">{k}</div>
 <div class="row" style="gap:16px;align-items:flex-start">
  <div style="flex:1.6" class="col">
   <div class="card"><div class="card-h"><h3>Đơn thuê hôm nay</h3>
     <div class="center" style="gap:8px"><span class="pill">24/09/2026</span>
     <button class="btn gho sm">Xuất CSV</button></div></div>{orders}</div>
   <div class="card"><div class="card-h"><h3>Lịch khai thác theo ca (7 ngày tới)</h3>
    <span class="xs">ô đậm = số máy đã đặt</span></div><div class="card-b">
    <div style="display:grid;grid-template-columns:70px repeat(7,1fr);gap:6px;font-size:11.5px">
     <div></div>""" + "".join(f'<div class="xs" style="text-align:center">{d}</div>'
       for d in ["24/09","25/09","26/09","27/09","28/09","29/09","30/09"]) + "".join(
      f'<div class="xs" style="line-height:26px">{ca}</div>' + "".join(
        f'<div style="height:26px;border-radius:5px;background:rgba(27,94,158,{v/10:.2f});'
        f'display:grid;place-items:center;color:{"#fff" if v>6 else "#1B5E9E"};font-weight:700">{v}</div>'
        for v in vals)
      for ca, vals in [("Ca 1",[7,8,5,9,10,2,1]),("Ca 2",[5,6,7,9,10,2,1]),
                       ("Ca 3",[3,4,4,7,8,1,0])]) + """
    </div></div></div>
  </div>
  <div style="width:320px;flex-shrink:0" class="col">
   <div class="card pad"><b style="color:#142C4A;font-size:14px">Cảnh báo cần xử lý</b>
    <div class="hr" style="margin:12px 0"></div>""" + al + """</div>
   <div class="card pad"><b style="color:#142C4A;font-size:14px">Tình trạng kho máy</b>
    <div class="hr" style="margin:12px 0"></div>
    <div class="col" style="gap:10px">
     <div><div class="between"><span class="sub">Đang cho thuê</span><b style="font-size:13px">4 máy</b></div>
      <div class="bar" style="margin-top:5px"><i style="width:40%"></i></div></div>
     <div><div class="between"><span class="sub">Sẵn sàng trong kho</span><b style="font-size:13px">3 máy</b></div>
      <div class="bar" style="margin-top:5px"><i style="width:30%;background:var(--ok)"></i></div></div>
     <div><div class="between"><span class="sub">Cho thuê theo tháng</span><b style="font-size:13px">1 máy</b></div>
      <div class="bar" style="margin-top:5px"><i style="width:10%;background:#4E86BC"></i></div></div>
     <div><div class="between"><span class="sub">Đang bảo trì</span><b style="font-size:13px">1 máy</b></div>
      <div class="bar" style="margin-top:5px"><i style="width:10%;background:var(--warn)"></i></div></div>
     <div><div class="between"><span class="sub">Dự phòng nóng (hot spare)</span><b style="font-size:13px">1 máy</b></div>
      <div class="bar" style="margin-top:5px"><i style="width:10%;background:var(--accent)"></i></div></div>
    </div></div>
  </div>
 </div></div></div></div>"""
    return page("07-dashboard", body, "Bảng điều khiển quản trị")


# =========================================================== 8. KHO MÁY
def s_inv():
    rows = [
     ["EL-5410-02","Dell Latitude 5410","9HTQ4T3","<span class='tag blue'>Đang thuê</span>","B","88%","EL-8241","Bật · 10:03","12",""],
     ["EL-5400-01","Dell Latitude 5400","8KRP2M1","<span class='tag blue'>Đang thuê</span>","A","94%","EL-8240","Bật · 10:02","19",""],
     ["EL-5400-02","Dell Latitude 5400","8KRP2M4","<span class='tag risk'>Quá hạn trả 45 phút</span>","A","61%","EL-8239","Bật · 10:05","9",""],
     ["EL-5400-03","Dell Latitude 5400","8KRP2M9","<span class='tag warn'>Chờ giao ca 2</span>","A","100%","EL-8238","Bật · 10:04","11",""],
     ["EL-T480-01","Lenovo ThinkPad T480","PF-2XK77C","<span class='tag ok'>Sẵn sàng</span>","A","97%","—","Bật · 09:58","22",""],
     ["EL-T480-02","Lenovo ThinkPad T480","PF-2XK81D","<span class='tag ok'>Sẵn sàng</span>","A","95%","—","Bật · 10:01","17",""],
     ["EL-T480-03","ThinkPad T480 16GB","PF-2XK83B","<span class='tag blue'>Đang thuê tháng</span>","B","91%","EL-8201","Bật · 09:47","6",""],
     ["EL-5410-01","Dell Latitude 5410","9HTQ4T8","<span class='tag ok'>Sẵn sàng</span>","B","96%","—","Bật · 10:00","14",""],
     ["EL-T490-01","Lenovo ThinkPad T490","PF-2XK91A","<span class='tag warn'>Bảo trì · thay pin</span>","C","71%","—","Tắt · 08:12","7",""],
     ["EL-5400-04","Dell Latitude 5400","8KRP2N2","<span class='tag grey'>Dự phòng nóng</span>","A","99%","—","Bật · 10:05","3",""],
    ]
    for r in rows:
        r[9] = '<button class="btn gho sm">Chi tiết</button>'
    t = table(["Mã tài sản","Kiểu máy","Số sê‑ri","Trạng thái","Nhóm","Pin","Đơn hiện tại","MDM check‑in","Lượt thuê",""],
              rows)
    body = f"""<div class="admin">{side("inv")}<div class="main">
{topbar("Kho máy — 10 thiết bị")}
<div class="page">
 <div class="row" style="gap:12px;margin-bottom:16px">
  <div class="inp" style="max-width:290px" ><span style="color:var(--muted-2)">Tìm theo mã tài sản / sê‑ri…</span></div>
  <div class="inp" style="width:auto">Trạng thái: Tất cả</div>
  <div class="inp" style="width:auto">Kiểu máy: Tất cả</div>
  <div style="flex:1"></div>
  <button class="btn gho">Nhập kho hàng loạt</button>
  <button class="btn pri">+ Thêm thiết bị</button>
 </div>
 <div class="card">{t}</div>
 <div class="note" style="margin-top:14px">Cột <b>MDM check‑in</b> lấy từ tác nhân quản lý thiết bị cài trên máy.
 Máy không check‑in quá <b>30 phút</b> trong thời gian thuê sẽ tự sinh cảnh báo và chặn các lượt đặt kế tiếp.</div>
</div></div></div>"""
    return page("08-inventory", body, "Kho máy")


# =========================================================== 9. CHI TIẾT ĐƠN
def s_order():
    states = [("Nháp","done"),("Chờ thanh toán","done"),("Đã giữ máy","done"),("Đã gán máy","done"),
              ("Đang thuê","now"),("Chờ kiểm tra trả","next"),("Đã hoàn cọc","next"),("Đóng","next")]
    chain = ""
    for i, (s, st) in enumerate(states):
        col = {"done":"var(--ok)","now":"var(--accent)","next":"#CBD5E1"}[st]
        bg = {"done":"var(--ok-50)","now":"var(--accent-50)","next":"#F1F5F9"}[st]
        chain += f"""<div style="display:flex;align-items:center;gap:0">
          <div style="background:{bg};color:{col};border:1.5px solid {col};border-radius:8px;padding:7px 11px;
          font-size:12px;font-weight:700;white-space:nowrap">{s}</div>"""
        if i < len(states) - 1:
            chain += '<div style="width:14px;height:2px;background:#D9E1EA"></div>'
        chain += "</div>"

    log = [("21:14:02","order.created","Khách EL-U-1042 tạo đơn cho ca 1 ngày 24/09","sys"),
           ("21:14:03","inventory.held","Giữ 1 suất kiểu máy T490 · hết hạn giữ 21:24","sys"),
           ("21:15:41","payment.received","Webhook đối soát: +414.000đ · nội dung EL 8241 QR","pay"),
           ("21:15:41","order.confirmed","Xác nhận đơn, gửi email + Zalo cho khách","sys"),
           ("06:40:12","device.assigned","Gán máy EL-5410-02 (ưu tiên máy pin cao nhất)","ops"),
           ("06:52:30","device.prepared","Wipe + reimage xong · checklist 7/7 · nhân viên: Trần K.","ops"),
           ("07:02:18","handover.signed","Khách ký điện tử, 6 ảnh hiện trạng, IP 10.20.x.x","ops"),
           ("07:02:19","order.active","Đơn chuyển trạng thái Đang thuê · MDM bật theo dõi","sys")]
    lg = "".join(f"""<tr><td class="mono xs" style="white-space:nowrap">{t}</td>
      <td><span class="pill mono" style="font-size:11.5px">{e}</span></td>
      <td class="sub">{d}</td><td><span class="tag grey">{w}</span></td></tr>""" for t, e, d, w in log)

    body = f"""<div class="admin">{side("orders")}<div class="main">
{topbar("Đơn thuê EL-8241", '<button class="btn gho sm" style="margin-right:8px">In biên bản</button>')}
<div class="page">
 <div class="card pad" style="margin-bottom:16px;overflow-x:auto">
  <div class="between" style="margin-bottom:13px"><b style="color:#142C4A;font-size:14px">Vòng đời đơn thuê</b>
  <span class="xs">Mọi chuyển trạng thái đều ghi nhật ký bất biến (append‑only)</span></div>
  <div style="display:flex;align-items:center;flex-wrap:wrap;gap:0">{chain}</div>
 </div>
 <div class="row" style="gap:16px;align-items:flex-start">
  <div style="flex:1.6" class="col">
   <div class="card"><div class="card-h"><h3>Nhật ký sự kiện (audit log)</h3>
     <span class="tag blue">8 sự kiện</span></div>
    <table><thead><tr><th>Thời điểm</th><th>Sự kiện</th><th>Diễn giải</th><th>Nguồn</th></tr></thead>
    <tbody>{lg}</tbody></table></div>
   <div class="card"><div class="card-h"><h3>Ảnh hiện trạng lúc bàn giao</h3>
     <span class="xs">Chụp lúc 07:01 · lưu kèm mã băm SHA‑256</span></div>
    <div class="card-b"><div class="grid g3" style="gap:11px">""" + "".join(
      f'<div class="thumb" style="height:92px">{x}</div>' for x in
      ["Mặt A (nắp)","Mặt B (màn hình)","Mặt C (bàn phím)","Mặt D (đáy)","Cạnh trái/phải","Phụ kiện kèm theo"]
    ) + """</div></div></div>
  </div>
  <div style="width:330px;flex-shrink:0" class="col">
   <div class="card pad"><b style="color:#142C4A;font-size:14px">Người thuê</b>
    <div class="hr" style="margin:12px 0"></div>
    <div class="center" style="gap:11px;margin-bottom:13px"><div class="avatar" style="width:40px;height:40px">NA</div>
     <div><b style="font-size:14px;color:#142C4A">Nguyễn Văn A</b>
     <div class="xs">EL-U-1042 · DE180xxx</div></div></div>
    <div class="between" style="padding:4px 0"><span class="sub">eKYC</span><span class="tag ok">Đã xác minh 12/09</span></div>
    <div class="between" style="padding:4px 0"><span class="sub">Số lần thuê</span><b style="font-size:13px">4</b></div>
    <div class="between" style="padding:4px 0"><span class="sub">Lần trả trễ</span><b style="font-size:13px">0</b></div>
    <div class="between" style="padding:4px 0"><span class="sub">Điểm tín nhiệm</span>
      <span class="tag ok">A · cọc giảm 30%</span></div>
   </div>
   <div class="card pad"><b style="color:#142C4A;font-size:14px">Thiết bị đang gán</b>
    <div class="hr" style="margin:12px 0"></div>
    <div class="between" style="padding:4px 0"><span class="sub">Mã tài sản</span><b class="mono" style="font-size:13px">EL-5410-02</b></div>
    <div class="between" style="padding:4px 0"><span class="sub">MDM check‑in</span><span class="tag ok">2 phút trước</span></div>
    <div class="between" style="padding:4px 0"><span class="sub">Mã hoá ổ đĩa</span><span class="tag ok">BitLocker bật</span></div>
    <div class="between" style="padding:4px 0"><span class="sub">Vị trí gần nhất</span><span class="sub">Toà Alpha (Wi‑Fi)</span></div>
    <div class="hr"></div>
    <button class="btn gho blk sm">Gửi nhắc trả máy</button>
    <button class="btn blk sm" style="margin-top:8px;background:var(--risk-50);color:var(--risk);
      border:1px solid #E9BDBA">Khoá máy từ xa (cần 2 người duyệt)</button>
   </div>
  </div>
 </div></div></div></div>"""
    return page("09-order", body, "Chi tiết đơn thuê")


# =========================================================== 10. BÁO CÁO
def s_report():
    months = [("T12",6.9,5.8),("T1",3.8,4.9),("T2",4.1,5.0),("T3",6.4,5.4),
              ("T4",9.9,6.4),("T5",8.9,6.0),("T6",8.8,5.7),("T7",8.1,5.6),("T8",11.1,6.6)]
    mx = 12.5
    bars = ""
    for m, rev, cost in months:
        h1 = int(rev / mx * 150); h2 = int(cost / mx * 150)
        bars += f"""<div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:6px">
        <div style="display:flex;gap:4px;align-items:flex-end;height:150px">
          <div style="width:17px;height:{h1}px;background:var(--blue);border-radius:3px 3px 0 0"></div>
          <div style="width:17px;height:{h2}px;background:#C9D6E4;border-radius:3px 3px 0 0"></div></div>
        <div class="xs">{m}</div></div>"""

    util = [("Nhóm A — Latitude 5400 (4 máy)",71),("Nhóm A — ThinkPad T480 (2 máy)",66),
            ("Nhóm B — Latitude 5410 (2 máy)",58),("Nhóm B — ThinkPad T480 16GB (1 máy)",52),
            ("Nhóm C — ThinkPad T490 (1 máy)",34)]
    ut = "".join(f"""<div style="margin-bottom:11px"><div class="between">
      <span class="sub">{a}</span><b style="font-size:13px">{b}%</b></div>
      <div class="bar" style="margin-top:5px"><i style="width:{b}%;background:{'var(--blue)' if b>=60 else 'var(--warn)'}"></i></div></div>"""
      for a, b in util)

    body = f"""<div class="admin">{side("rep")}<div class="main">
{topbar("Báo cáo kinh doanh")}
<div class="page">
 <div class="grid g4" style="margin-bottom:16px">
  {kpi("Doanh thu luỹ kế","55,6 tr", "▲ 21%", True, "9 tháng vận hành")}
  {kpi("Biên lợi nhuận gộp","63%", "▲ 4 điểm", True, "sau khấu hao máy")}
  {kpi("Doanh thu / máy / tháng","763.000đ", "▲ 12%", True, "10 máy trong đội")}
  {kpi("Tỉ lệ hư hỏng / lượt","1,7%", "▼ 0,6 điểm", True, "5 vụ / 296 lượt thuê")}
 </div>
 <div class="row" style="gap:16px;align-items:flex-start">
  <div style="flex:1.5" class="col">
   <div class="card"><div class="card-h"><h3>Doanh thu và chi phí theo tháng (triệu đồng)</h3>
     <div class="center" style="gap:12px"><span class="center" style="gap:5px"><span style="width:10px;height:10px;
     background:var(--blue);border-radius:2px"></span><span class="xs">Doanh thu</span></span>
     <span class="center" style="gap:5px"><span style="width:10px;height:10px;background:#C9D6E4;
     border-radius:2px"></span><span class="xs">Chi phí</span></span></div></div>
    <div class="card-b"><div style="display:flex;gap:10px;align-items:flex-end">{bars}</div>
    <div class="note" style="margin-top:15px">Hai đỉnh <b>tháng 12</b>, <b>tháng 4</b> và <b>tháng 8</b> trùng ba kỳ thi cuối kỳ.
    Doanh thu ngoài mùa thi chỉ bằng 30% đỉnh — đây là rủi ro dòng tiền lớn nhất của mô hình và là lý do
    chúng tôi bổ sung gói thuê tháng cho đồ án.</div></div></div>
  </div>
  <div style="width:340px;flex-shrink:0" class="col">
   <div class="card pad"><b style="color:#142C4A;font-size:14px">Tỉ lệ khai thác theo dòng máy</b>
    <div class="hr" style="margin:12px 0"></div>{ut}
    <div class="xs">Ngưỡng hoà vốn của đội máy là <b>42%</b> khai thác. Hai dòng dưới ngưỡng đang được cân nhắc
    thanh lý.</div></div>
   <div class="card pad"><b style="color:#142C4A;font-size:14px">Nguồn đơn</b>
    <div class="hr" style="margin:12px 0"></div>
    <div class="col" style="gap:9px">
     <div class="between"><span class="sub">Giới thiệu từ bạn bè</span><b style="font-size:13px">41%</b></div>
     <div class="between"><span class="sub">Group Facebook sinh viên</span><b style="font-size:13px">27%</b></div>
     <div class="between"><span class="sub">Đại sứ trong lớp</span><b style="font-size:13px">18%</b></div>
     <div class="between"><span class="sub">Tìm kiếm Google</span><b style="font-size:13px">9%</b></div>
     <div class="between"><span class="sub">Khác</span><b style="font-size:13px">5%</b></div>
    </div></div>
  </div>
 </div></div></div></div>"""
    return page("10-report", body, "Báo cáo kinh doanh")


if __name__ == "__main__":
    for f in (s_landing, s_catalog, s_kyc, s_pay, s_pass, s_staff, s_dash, s_inv, s_order, s_report):
        print("đã sinh:", f())
