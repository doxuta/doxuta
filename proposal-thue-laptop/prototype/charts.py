# -*- coding: utf-8 -*-
"""Biểu đồ tài chính — thiết kế cho bản in: khổ hẹp, chữ lớn, nhãn trực tiếp."""
import os, sys
sys.path.insert(0, "/home/user/doxuta/proposal-thue-laptop/src")
import finmodel as F

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "figures")
os.makedirs(OUT, exist_ok=True)

CSS = """
:root{--s1:#1B5E9E;--s2:#C2411C;--s3:#1BAF7A;--ink:#111827;--ink2:#374151;
 --mut:#6B7280;--line:#DDE4EC;--grid:#EDF1F5;--navy:#142C4A}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:"Liberation Sans","Noto Sans",Arial,sans-serif;background:#fff;color:var(--ink);
 font-size:14px;line-height:1.4}
.w{padding:20px 22px 16px}
.t{font-size:17px;font-weight:800;color:var(--navy);letter-spacing:-.2px}
.st{font-size:13px;color:var(--mut);margin:3px 0 14px}
.lg{display:flex;gap:18px;font-size:13px;color:var(--ink2);margin-bottom:12px;align-items:center}
.lg i{width:12px;height:12px;border-radius:3px;display:inline-block;margin-right:6px;vertical-align:-2px}
.plot{position:relative}
.gl{position:absolute;left:0;right:0;border-top:1px solid var(--grid)}
.gl span{position:absolute;left:0;top:-9px;font-size:11.5px;color:var(--mut);background:#fff;padding-right:5px}
.cols{display:flex;align-items:flex-end;gap:0;position:relative;z-index:2}
.c{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:flex-end}
.bars{display:flex;gap:2px;align-items:flex-end}
.bar{border-radius:4px 4px 0 0}
.vl{font-size:11.5px;font-weight:700;color:var(--ink2);margin-bottom:3px;white-space:nowrap}
.xa{display:flex;border-top:1.5px solid var(--line);margin-top:0;padding-top:6px}
.xa div{flex:1;text-align:center;font-size:11.5px;color:var(--mut)}
.xa div b{display:block;color:var(--s2);font-size:10.5px;font-weight:700}
.note{margin-top:12px;font-size:12.5px;color:var(--ink2);background:#F6F9FC;
 border-left:3px solid var(--s1);padding:9px 12px;border-radius:0 7px 7px 0}
"""

def page(name, title, sub, body, note=None, width=800):
    n = f'<div class="note">{note}</div>' if note else ""
    html = f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><style>{CSS}
    body{{width:{width}px}}</style></head><body><div class="w">
    <div class="t">{title}</div><div class="st">{sub}</div>{body}{n}</div></body></html>"""
    open(os.path.join(OUT, name + ".html"), "w", encoding="utf-8").write(html)
    return name


def gridlines(maxv, steps, h, fmt):
    out = ""
    for i in range(steps + 1):
        v = maxv * i / steps
        out += f'<div class="gl" style="bottom:{v/maxv*h:.1f}px"><span>{fmt(v)}</span></div>'
    return out


# ── C1: doanh thu và chi phí theo tháng, năm 1
def c1():
    rows, kh, cd, _, _, _ = F.pnl()
    H = 210
    mx = max(r["doanh_thu"] for r in rows) * 1.18
    cols = ""
    for r in rows:
        chi = r["bien"] + r["quy"] + r["co_dinh"] + r["khau_hao"]
        h1 = r["doanh_thu"] / mx * H; h2 = chi / mx * H
        cols += (f'<div class="c"><div class="vl">{F.tr(r["doanh_thu"])}</div>'
                 f'<div class="bars"><div class="bar" style="width:16px;height:{h1:.0f}px;background:var(--s1)"></div>'
                 f'<div class="bar" style="width:16px;height:{h2:.0f}px;background:#C3D3E3"></div></div></div>')
    peak = {"12/2026": "thi Fall", "04/2027": "thi Spring", "08/2027": "thi Summer"}
    xa = "".join(f'<div>{r["thang"][:3]}{r["thang"][-2:]}'
                 f'{"<b>"+peak[r["thang"]]+"</b>" if r["thang"] in peak else ""}</div>'
                 for r in rows)
    body = (f'<div class="lg"><span><i style="background:var(--s1)"></i>Doanh thu</span>'
            f'<span><i style="background:#C3D3E3"></i>Tổng chi phí (gồm khấu hao)</span>'
            f'<span style="color:var(--mut)">đơn vị: triệu đồng</span></div>'
            f'<div class="plot" style="height:{H+26}px">{gridlines(mx, 4, H, lambda v: F.tr(v))}'
            f'<div class="cols" style="height:{H+26}px">{cols}</div></div><div class="xa">{xa}</div>')
    return page("c1-doanh-thu-thang", "Doanh thu và chi phí theo tháng — năm vận hành thứ nhất",
                "Đội 10 máy · giá bình quân 144.100đ mỗi lượt thuê · ba đỉnh trùng ba kỳ thi cuối kỳ của Đại học FPT",
                body,
                "Ba cột cao nhất rơi đúng vào tháng 12, tháng 4 và tháng 8 — ba kỳ thi cuối kỳ. "
                "Doanh thu tháng thấp nhất chỉ bằng <b>khoảng 20%</b> tháng cao nhất. Đây là rủi ro dòng tiền lớn nhất "
                "của mô hình và là lý do chúng tôi bổ sung gói thuê tháng cho sinh viên làm đồ án và thực tập.")


# ── C2: dòng tiền luỹ kế 36 tháng
def c2():
    moc, hv, c1_, c2_ = F.hoan_von_luy_ke()
    H = 200
    vals = [m[2] for m in moc]
    lo, hi = min(vals) * 1.12, max(vals) * 1.12
    rng = hi - lo
    zero = (0 - lo) / rng * H
    cols = ""
    for i, (k, t, v) in enumerate(moc):
        y = (v - lo) / rng * H
        col = "var(--s3)" if v >= 0 else "var(--s2)"
        top = max(y, zero); bot = min(y, zero)
        lbl = ""
        if hv and k == hv[0]:
            lbl = f'<div style="position:absolute;bottom:{top+8:.0f}px;left:50%;transform:translateX(-50%);white-space:nowrap;font-size:11.5px;font-weight:700;color:var(--s3)">hoàn vốn</div>'
        cols += (f'<div class="c" style="position:relative;justify-content:flex-start;height:{H}px">'
                 f'{lbl}<div style="position:absolute;bottom:{bot:.0f}px;height:{max(top-bot,1.5):.0f}px;'
                 f'width:9px;background:{col};border-radius:2px"></div></div>')
    xa = "".join(f'<div>{m[1][3:] if m[0].endswith("12") else ("" if i%3 else "")}</div>' for i, m in enumerate(moc))
    ticks = ""
    step = 25_000_000
    v = -int(abs(lo) // step) * step
    while v <= hi:
        y = (v - lo) / rng * H
        style = "border-top:1.5px solid #9AA6B2" if v == 0 else "border-top:1px solid var(--grid)"
        ticks += f'<div class="gl" style="bottom:{y:.0f}px;{style}"><span>{F.tr(v) if v else "0"}</span></div>'
        v += step
    xa = "".join(f'<div>{("10/26" if i==0 else "10/27" if i==12 else "10/28" if i==24 else "")}</div>'
                 for i in range(len(moc)))
    body = (f'<div class="lg"><span><i style="background:var(--s2)"></i>Còn âm (chưa thu hồi vốn)</span>'
            f'<span><i style="background:var(--s3)"></i>Đã dương</span>'
            f'<span style="color:var(--mut)">đơn vị: triệu đồng · trục ngang: 36 tháng liên tiếp</span></div>'
            f'<div class="plot" style="height:{H}px;padding-left:44px">{ticks}'
            f'<div class="cols" style="height:{H}px;align-items:flex-start">{cols}</div></div>'
            f'<div class="xa" style="padding-left:44px">{xa}</div>')
    return page("c2-dong-tien", "Dòng tiền luỹ kế 36 tháng",
                f"Vốn ban đầu {F.vnd(c1_)} · đầu tư mở rộng năm hai {F.vnd(c2_)} · mỗi cột là một tháng",
                body,
                f"Điểm hoàn vốn rơi vào <b>tháng thứ 27</b> ({hv[1] if hv else '—'}). "
                "Con số này dài hơn kỳ vọng thông thường của một dự án sinh viên, và chúng tôi trình bày đúng như vậy: "
                "đây là mô hình <b>thâm dụng tài sản</b>. Bù lại, tại thời điểm hoàn vốn đội máy vẫn còn "
                "giá trị thanh lý ước tính khoảng 35% giá mua, nên vị thế kinh tế thực tế dương sớm hơn con số kế toán.",
                width=880)


# ── C3: công suất khai thác theo tháng
def c3():
    rows = F.pnl()[0]
    H = 175
    cols = ""
    for r in rows:
        v = r["cong_suat"] * 100
        h = v / 100 * H
        col = "var(--s1)" if v >= 42 else "var(--s2)"
        cols += (f'<div class="c"><div class="vl" style="color:{col}">{v:.0f}%</div>'
                 f'<div class="bar" style="width:26px;height:{h:.0f}px;background:{col}"></div></div>')
    xa = "".join(f'<div>{r["thang"][:3]}{r["thang"][-2:]}</div>' for r in rows)
    hv_line = 42 / 100 * H
    body = (f'<div class="lg"><span><i style="background:var(--s1)"></i>Trên ngưỡng hoà vốn</span>'
            f'<span><i style="background:var(--s2)"></i>Dưới ngưỡng hoà vốn</span></div>'
            f'<div class="plot" style="height:{H+22}px">{gridlines(100, 4, H, lambda v: "%.0f%%" % v)}'
            f'<div class="gl" style="bottom:{hv_line:.0f}px;border-top:2px dashed #C2411C">'
            f'<span style="left:auto;right:0;color:#C2411C;font-weight:700">ngưỡng hoà vốn 42%</span></div>'
            f'<div class="cols" style="height:{H+22}px">{cols}</div></div><div class="xa">{xa}</div>')
    return page("c3-cong-suat", "Tỉ lệ khai thác đội máy theo tháng — năm thứ nhất",
                "Số máy-ngày thực sự cho thuê chia cho tổng máy-ngày sẵn có (10 máy × 26 ngày)",
                body,
                "Bốn tháng đầu nằm dưới ngưỡng hoà vốn — đây là giai đoạn xây dựng nhận biết, đã được tính vào kế hoạch vốn. "
                "Từ tháng thứ năm trở đi, đội máy vượt ngưỡng và duy trì mức 44–66%. "
                "Khi tỉ lệ khai thác cả quý vượt <b>60%</b>, đó là tín hiệu để mua thêm máy.")


# ── C4: cơ cấu chi phí năm 1
def c4():
    rows, kh, cd, _, _, _ = F.pnl()
    bien = sum(r["bien"] for r in rows); quy = sum(r["quy"] for r in rows)
    codinh = cd * 12; khau = kh * 12
    dt = sum(r["doanh_thu"] for r in rows)
    ln = dt - bien - quy - codinh - khau
    items = [("Khấu hao đội máy", khau, "#1B5E9E"),
             ("Định phí (kho, hạ tầng, truyền thông)", codinh, "#4E86BC"),
             ("Chi phí biến đổi (công, eKYC, giao nhận, vật tư)", bien, "#8FB3D2"),
             ("Quỹ dự phòng hư hỏng, mất mát (4% doanh thu)", quy, "#C2411C"),
             ("Lợi nhuận sau thuế", ln, "#1BAF7A")]
    rowsh = ""
    for ten, v, col in items:
        pct = v / dt * 100
        rowsh += (f'<div style="display:flex;align-items:center;gap:12px;margin-bottom:9px">'
                  f'<div style="width:290px;font-size:13px;color:var(--ink2)">{ten}</div>'
                  f'<div style="flex:1;height:22px;background:#F1F5F9;border-radius:5px;overflow:hidden">'
                  f'<div style="height:100%;width:{pct:.1f}%;background:{col};border-radius:5px"></div></div>'
                  f'<div style="width:150px;text-align:right;font-size:13px;font-weight:700;color:var(--navy)">'
                  f'{F.tr(v)} tr · {pct:.0f}%</div></div>')
    body = rowsh
    return page("c4-co-cau-chi-phi", "Một đồng doanh thu đi về đâu — năm thứ nhất",
                f"Tổng doanh thu {F.tr(dt)} triệu đồng",
                body,
                "Khấu hao là khoản lớn nhất — đúng bản chất của mô hình cho thuê tài sản. "
                "Nó cũng là khoản <b>không phải chi tiền mặt</b>, nên dòng tiền hoạt động dương sớm hơn nhiều so với lợi nhuận kế toán.",
                width=920)


if __name__ == "__main__":
    for f in (c1, c2, c3, c4):
        print("đã sinh:", f())
