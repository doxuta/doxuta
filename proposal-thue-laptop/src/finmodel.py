# -*- coding: utf-8 -*-
"""Mô hình tài chính ExamLap — mọi con số trong proposal đều sinh ra từ file này."""
import json, os

# ─────────────────────────────────────────── THAM SỐ ĐẦU VÀO
FLEET = [
    # (nhóm, số máy, đơn giá VND, mô tả)
    ("A — Máy thi tiêu chuẩn", 5, 6_500_000, "Dell Latitude 5400 / ThinkPad T480 — i5 gen 8, 8GB, SSD 256GB, jack 3.5mm"),
    ("B — Máy lập trình",      4, 7_500_000, "Dell Latitude 5410 / ThinkPad T480 16GB — i5 gen 10, 16GB, SSD 256GB"),
    ("C — Máy cấu hình cao",   1, 10_000_000, "ThinkPad T490 / T14s Gen 2 — i5–i7, 16GB, SSD 512GB"),
]
FLEET_N2 = 16          # quy mô đội máy năm thứ hai
GIA_MAY_BO_SUNG = 7_200_000
N = sum(n for _, n, _, _ in FLEET)

CAPEX_KHAC = [
    ("Phụ kiện theo máy (túi chống sốc, chuột, tai nghe có dây 3.5mm)", N, 300_000),
    ("Tem tài sản chống bóc + khắc laser mã máy",                        N,  30_000),
    ("Tủ sạc, kệ để máy, ổ cắm chống quá tải",                           1, 3_000_000),
    ("Bàn kiểm máy, đèn và phông chụp ảnh hiện trạng",                   1, 1_500_000),
    ("Ổ cứng ngoài lưu ảnh hệ điều hành chuẩn + sao lưu",                2, 1_200_000),
    ("Dự phòng bản quyền Windows 11 Pro cho máy thiếu OEM",              3, 1_200_000),
    ("Tên miền .com + .vn năm đầu",                                      1, 1_050_000),
    ("Chi phí đăng ký hộ kinh doanh, khắc dấu, giấy tờ",                 1, 1_500_000),
]

OPEX_CO_DINH = [
    ("Kho kiêm điểm giao nhận (phần đóng góp phòng trọ dùng chung)", 1_200_000),
    ("Điện, nước, internet",                                            450_000),
    ("Máy chủ, tên miền, email, dịch vụ đối soát VietQR",               450_000),
    ("Phần mềm quản lý thiết bị (MDM) — %d máy" % N,                    150_000),
    ("Truyền thông cơ bản (nội dung, in ấn, quà giới thiệu)",           400_000),
    ("Dịch vụ khác (lưu trữ ảnh, sao lưu, công cụ thiết kế)",           150_000),
]

GIA = {
    "ca_thi":    79_000,   # 4 giờ
    "ngay_thi":  129_000,  # 2 ca, 10 giờ
    "khan_cap":  179_000,  # đặt dưới 3 giờ, giao tận nơi
    "tuan_thi":  449_000,  # 7 ngày
    "thang":     849_000,  # 30 ngày
    "mien_tru":   15_000,  # phí miễn trừ thiệt hại mỗi lượt
    "mien_tru_thang": 69_000,
}
MIX = {"ca_thi": 0.55, "ngay_thi": 0.25, "khan_cap": 0.12, "tuan_thi": 0.08}
TY_LE_MUA_MIEN_TRU = 0.60
PHI_TRA_TRE_TB = 2_000          # bình quân trên mỗi lượt

# nhu cầu khi đã ổn định (số lượt thuê theo ca/ngày/tuần) và số máy-tháng cho thuê dài hạn
THANG = ["10/2026","11/2026","12/2026","01/2027","02/2027","03/2027",
         "04/2027","05/2027","06/2027","07/2027","08/2027","09/2027"]
SU_KIEN = ["Progress test Fall","Ngoài mùa thi","FINAL FALL","Đầu kỳ Spring","Tết Nguyên đán",
           "Progress test Spring","FINAL SPRING","Cuối Spring, đầu Summer","Progress test Summer",
           "Ngoài mùa thi","FINAL SUMMER","Cuối Summer, đầu Fall"]
NHU_CAU_ON_DINH = [30, 25, 70, 20, 22, 30, 62, 45, 30, 25, 65, 45]
MAY_THANG      = [ 2,  3,  1,  3,  3,  4,  2,  3,  5,  5,  2,  3]
RAMP           = [.30, .45, .60, .70, .75, .85, .90, .95, 1.0, 1.0, 1.0, 1.0]

CHI_PHI_BIEN = {
    "nhan_cong_moi_luot": 20_000,   # 0,6–0,7 giờ công × 30.000đ/giờ
    "ekyc_moi_luot":       1_600,   # 40% lượt là khách mới × 4.000đ
    "giao_hang_moi_luot":  3_000,   # 12% lượt là gói khẩn cấp × 25.000đ
    "vat_tu_moi_luot":     3_000,   # khăn, cồn, túi, in biên bản
    "nhan_cong_may_thang": 35_000,  # chuẩn bị + bàn giao cho một hợp đồng tháng
}
QUY_RUI_RO_PCT = 0.04       # % doanh thu trích quỹ hư hỏng, mất mát
THANG_KHAU_HAO = 30
GIA_TRI_THU_HOI = 0.35


# ─────────────────────────────────────────── TÍNH TOÁN
def capex():
    rows = [(f"{ten} — {n} máy × {gia:,.0f}đ".replace(",", "."), n * gia, mo_ta)
            for ten, n, gia, mo_ta in FLEET]
    tong_may = sum(n * g for _, n, g, _ in FLEET)
    khac = [(f"{ten} — {n} × {gia:,.0f}đ".replace(",", "."), n * gia, "")
            for ten, n, gia in CAPEX_KHAC]
    tong_khac = sum(n * g for _, n, g in CAPEX_KHAC)
    du_phong = round((tong_may + tong_khac) * 0.05 / 100_000) * 100_000
    return rows, tong_may, khac, tong_khac, du_phong, tong_may + tong_khac + du_phong


def doanh_thu_moi_luot():
    thue = sum(MIX[k] * GIA[k] for k in MIX)
    mien_tru = TY_LE_MUA_MIEN_TRU * GIA["mien_tru"]
    return thue, mien_tru, PHI_TRA_TRE_TB, thue + mien_tru + PHI_TRA_TRE_TB


def pnl():
    _, tong_may, _, _, _, tong_capex = capex()
    khau_hao = round(tong_may * (1 - GIA_TRI_THU_HOI) / THANG_KHAU_HAO / 1000) * 1000
    co_dinh = sum(v for _, v in OPEX_CO_DINH)
    dt_luot = doanh_thu_moi_luot()[3]
    dt_thang_may = GIA["thang"] + TY_LE_MUA_MIEN_TRU * GIA["mien_tru_thang"]

    rows, cum = [], 0
    for i, th in enumerate(THANG):
        luot = round(NHU_CAU_ON_DINH[i] * RAMP[i])
        mt = round(MAY_THANG[i] * RAMP[i])
        dt_ca = luot * dt_luot
        dt_dai = mt * dt_thang_may
        dt = dt_ca + dt_dai
        bien = (luot * sum(CHI_PHI_BIEN[k] for k in
                           ("nhan_cong_moi_luot", "ekyc_moi_luot", "giao_hang_moi_luot", "vat_tu_moi_luot"))
                + mt * CHI_PHI_BIEN["nhan_cong_may_thang"])
        quy = dt * QUY_RUI_RO_PCT
        loi_gop = dt - bien - quy
        ebitda = loi_gop - co_dinh
        ln = ebitda - khau_hao
        cum += ln
        # công suất: một máy phục vụ tối đa ~2 lượt/ngày × 26 ngày; tính đơn giản theo máy-ngày
        may_ngay_dung = luot * 1.4 + mt * 26
        cong_suat = may_ngay_dung / (N * 26)
        rows.append(dict(thang=th, su_kien=SU_KIEN[i], luot=luot, may_thang=mt,
                         doanh_thu=dt, dt_ca=dt_ca, dt_dai=dt_dai, bien=bien, quy=quy,
                         loi_gop=loi_gop, co_dinh=co_dinh, ebitda=ebitda,
                         khau_hao=khau_hao, ln=ln, luy_ke=cum, cong_suat=cong_suat))
    return rows, khau_hao, co_dinh, dt_luot, dt_thang_may, tong_capex


def diem_hoa_von():
    _, khau_hao, co_dinh, dt_luot, _, _ = pnl()
    bien_luot = sum(CHI_PHI_BIEN[k] for k in
                    ("nhan_cong_moi_luot", "ekyc_moi_luot", "giao_hang_moi_luot", "vat_tu_moi_luot"))
    dong_gop = dt_luot * (1 - QUY_RUI_RO_PCT) - bien_luot
    return dict(dong_gop_moi_luot=dong_gop,
                hoa_von_tien_mat=co_dinh / dong_gop,
                hoa_von_ke_toan=(co_dinh + khau_hao) / dong_gop,
                bien_luot=bien_luot)


def kich_ban():
    base_rows, khau_hao, co_dinh, dt_luot, dt_thang_may, capex_tong = pnl()
    out = {}
    for ten, hs_cau, hs_gia in (("Thận trọng", 0.65, 0.90), ("Cơ sở", 1.00, 1.00), ("Thuận lợi", 1.35, 1.05)):
        dt = ln = 0
        for i, r in enumerate(base_rows):
            luot = round(r["luot"] * hs_cau); mt = round(r["may_thang"] * hs_cau)
            d = luot * dt_luot * hs_gia + mt * dt_thang_may * hs_gia
            b = (luot * sum(CHI_PHI_BIEN[k] for k in
                            ("nhan_cong_moi_luot", "ekyc_moi_luot", "giao_hang_moi_luot", "vat_tu_moi_luot"))
                 + mt * CHI_PHI_BIEN["nhan_cong_may_thang"])
            dt += d
            ln += d - b - d * QUY_RUI_RO_PCT - co_dinh - khau_hao
        dong_tien_nam = ln + khau_hao * 12
        out[ten] = dict(doanh_thu=dt, loi_nhuan=ln, bien_ln=ln / dt if dt else 0,
                        dong_tien=dong_tien_nam,
                        thang_hoan_von=(capex_tong / (dong_tien_nam / 12)) if dong_tien_nam > 0 else None)
    return out


def nam2():
    """Năm thứ hai: đội máy %d, nhu cầu tăng 1,6 lần nhờ nhận biết và mở rộng sang FPT Polytechnic."""
    rows1, khau_hao1, co_dinh1, dt_luot, dt_thang_may, capex1 = pnl()
    them = FLEET_N2 - N
    capex2 = them * GIA_MAY_BO_SUNG + them * 330_000          # máy + phụ kiện, tem
    _, tong_may1, _, _, _, _ = capex()
    khau_hao2 = round((tong_may1 + them * GIA_MAY_BO_SUNG) * (1 - GIA_TRI_THU_HOI)
                      / THANG_KHAU_HAO / 1000) * 1000
    co_dinh2 = co_dinh1 + 900_000        # thêm MDM, kho rộng hơn, truyền thông
    HS = 1.6
    out, cum = [], 0
    for i, th in enumerate(THANG):
        luot = round(NHU_CAU_ON_DINH[i] * HS)
        mt = round(MAY_THANG[i] * HS)
        dt = luot * dt_luot + mt * dt_thang_may
        bien = (luot * sum(CHI_PHI_BIEN[k] for k in
                ("nhan_cong_moi_luot", "ekyc_moi_luot", "giao_hang_moi_luot", "vat_tu_moi_luot"))
                + mt * CHI_PHI_BIEN["nhan_cong_may_thang"])
        quy = dt * QUY_RUI_RO_PCT
        ebitda = dt - bien - quy - co_dinh2
        ln = ebitda - khau_hao2
        cum += ln
        cs = (luot * 1.4 + mt * 26) / (FLEET_N2 * 26)
        th2 = th.replace("/2026", "/2027") if th.endswith("2026") else th.replace("/2027", "/2028")
        out.append(dict(thang=th2, luot=luot, may_thang=mt, doanh_thu=dt,
                        ebitda=ebitda, ln=ln, luy_ke=cum, cong_suat=cs))
    return out, khau_hao2, co_dinh2, capex2


def hoan_von_luy_ke():
    """Dòng tiền luỹ kế theo tháng qua 24 tháng, xác định tháng hoàn vốn."""
    r1, kh1, _, _, _, capex1 = pnl()
    r2, kh2, _, capex2 = nam2()
    dong = -capex1
    moc = []
    for i, r in enumerate(r1):
        dong += r["ln"] + kh1
        moc.append(("N1-%02d" % (i + 1), r1[i]["thang"], dong))
    dong -= capex2
    for i, r in enumerate(r2):
        dong += r["ln"] + kh2
        moc.append(("N2-%02d" % (i + 1), r2[i]["thang"], dong))
    for i, r in enumerate(r2):          # năm 3: giữ nguyên quy mô, không đầu tư thêm
        dong += r["ln"] + kh2
        th3 = r["thang"].replace("/2027", "/2028") if r["thang"].endswith("2027") else r["thang"].replace("/2028", "/2029")
        moc.append(("N3-%02d" % (i + 1), th3, dong))
    thang_hv = next((m for m in moc if m[2] >= 0), None)
    return moc, thang_hv, capex1, capex2


def vnd(x):
    return f"{round(x):,}".replace(",", ".") + "đ"

def tr(x):
    return f"{x/1_000_000:.1f}".replace(".", ",")


if __name__ == "__main__":
    rows, tong_may, khac, tong_khac, du_phong, tong = capex()
    print("=== VỐN ĐẦU TƯ ===")
    for t, v, _ in rows: print(f"  {t:<70} {vnd(v):>15}")
    print(f"  {'Cộng thiết bị':<70} {vnd(tong_may):>15}")
    for t, v, _ in khac: print(f"  {t:<70} {vnd(v):>15}")
    print(f"  {'Dự phòng 5%':<70} {vnd(du_phong):>15}")
    print(f"  {'TỔNG VỐN ĐẦU TƯ':<70} {vnd(tong):>15}")

    t, m, l, tot = doanh_thu_moi_luot()
    print(f"\n=== DOANH THU BÌNH QUÂN MỖI LƯỢT ===\n  thuê {vnd(t)} + miễn trừ {vnd(m)} + trễ {vnd(l)} = {vnd(tot)}")

    pr, kh, cd, dtl, dtm, cap = pnl()
    print(f"\n=== P&L 12 THÁNG (khấu hao {vnd(kh)}/tháng, định phí {vnd(cd)}/tháng) ===")
    print(f"{'Tháng':<9}{'Sự kiện':<26}{'Lượt':>5}{'M-th':>5}{'Doanh thu':>13}{'Lợi gộp':>13}{'EBITDA':>13}{'LNST':>13}{'Luỹ kế':>14}{'CS':>7}")
    for r in pr:
        print(f"{r['thang']:<9}{r['su_kien']:<26}{r['luot']:>5}{r['may_thang']:>5}"
              f"{vnd(r['doanh_thu']):>13}{vnd(r['loi_gop']):>13}{vnd(r['ebitda']):>13}"
              f"{vnd(r['ln']):>13}{vnd(r['luy_ke']):>14}{r['cong_suat']*100:>6.0f}%")
    print(f"{'CẢ NĂM':<40}{sum(r['luot'] for r in pr):>5}{sum(r['may_thang'] for r in pr):>5}"
          f"{vnd(sum(r['doanh_thu'] for r in pr)):>13}{vnd(sum(r['loi_gop'] for r in pr)):>13}"
          f"{vnd(sum(r['ebitda'] for r in pr)):>13}{vnd(sum(r['ln'] for r in pr)):>13}")

    hv = diem_hoa_von()
    print(f"\n=== HOÀ VỐN ===")
    print(f"  Đóng góp mỗi lượt: {vnd(hv['dong_gop_moi_luot'])}")
    print(f"  Hoà vốn tiền mặt : {hv['hoa_von_tien_mat']:.0f} lượt/tháng")
    print(f"  Hoà vốn kế toán  : {hv['hoa_von_ke_toan']:.0f} lượt/tháng")

    r2, kh2, cd2, capex2 = nam2()
    print(f"\n=== NĂM THỨ HAI (đội {FLEET_N2} máy, nhu cầu ×1,6; đầu tư thêm {vnd(capex2)}) ===")
    print(f"  Doanh thu {vnd(sum(r['doanh_thu'] for r in r2))} · EBITDA {vnd(sum(r['ebitda'] for r in r2))}"
          f" · LNST {vnd(sum(r['ln'] for r in r2))}"
          f" · công suất bình quân {sum(r['cong_suat'] for r in r2)/12*100:.0f}%")

    moc, hv, c1, c2 = hoan_von_luy_ke()
    print(f"\n=== DÒNG TIỀN LUỸ KẾ ===")
    for k, t, v in moc:
        if k.endswith(("03", "06", "09", "12")) or (hv and k == hv[0]):
            print(f"  {k} ({t}): {vnd(v)}")
    print(f"  → Hoàn vốn tại {hv[0]} ({hv[1]})" if hv else "  → Chưa hoàn vốn trong 24 tháng")

    print(f"\n=== KỊCH BẢN ===")
    for k, v in kich_ban().items():
        hv_t = f"{v['thang_hoan_von']:.0f} tháng" if v["thang_hoan_von"] else "không hoàn vốn"
        print(f"  {k:<12} DT {vnd(v['doanh_thu']):>14}  LN {vnd(v['loi_nhuan']):>14}  biên {v['bien_ln']*100:>6.1f}%  hoàn vốn {hv_t}")


# ─────────────────────────────────────────── XUẤT BẢNG MARKDOWN
def md_tables():
    o = []
    rows, tong_may, khac, tong_khac, du_phong, tong = capex()
    o.append("### T-CAPEX\n")
    o.append("| Hạng mục | Số lượng | Thành tiền | Ghi chú |")
    o.append("|---|---|---|---|")
    for ten, n, gia, mo_ta in FLEET:
        o.append(f"| {ten} | {n} máy × {vnd(gia)} | {vnd(n*gia)} | {mo_ta} |")
    o.append(f"| **Cộng thiết bị** | **{N} máy** | **{vnd(tong_may)}** | |")
    for ten, n, gia in CAPEX_KHAC:
        o.append(f"| {ten} | {n} × {vnd(gia)} | {vnd(n*gia)} | |")
    o.append(f"| Dự phòng 5% | | {vnd(du_phong)} | biến động giá máy cũ |")
    o.append(f"| **TỔNG VỐN ĐẦU TƯ BAN ĐẦU** | | **{vnd(tong)}** | |")

    o.append("\n### T-OPEX\n")
    o.append("| Khoản định phí hằng tháng | Số tiền | Cơ sở ước tính |")
    o.append("|---|---|---|")
    ghi = ["phòng trọ 40 m² khu Hoà Hải, phần diện tích dùng làm kho",
           "ước tính theo mức sinh hoạt của một phòng trọ dùng chung",
           "VPS Việt Nam + tên miền + dịch vụ đối soát biến động số dư",
           "gói quản lý thiết bị tính theo đầu máy",
           "in ấn, quà giới thiệu, chi phí nội dung",
           "lưu trữ ảnh hiện trạng, sao lưu, công cụ thiết kế"]
    for (ten, v), g in zip(OPEX_CO_DINH, ghi):
        o.append(f"| {ten} | {vnd(v)} | {g} |")
    o.append(f"| **Cộng định phí** | **{vnd(sum(v for _, v in OPEX_CO_DINH))}** | |")

    o.append("\n### T-GIA\n")
    o.append("| Gói dịch vụ | Giá bán | Điều kiện | Neo thị trường |")
    o.append("|---|---|---|---|")
    o.append(f"| Ca thi (4 giờ) | {vnd(GIA['ca_thi'])} | đặt trước ≥ 12 giờ | đối thủ Đà Nẵng 38.000–50.000đ/ngày |")
    o.append(f"| Ngày thi (2 ca, 10 giờ) | {vnd(GIA['ngay_thi'])} | đặt trước ≥ 12 giờ | |")
    o.append(f"| Ca thi khẩn cấp | {vnd(GIA['khan_cap'])} | đặt dưới 3 giờ, giao tận cổng trường | không đơn vị nào bán |")
    o.append(f"| Tuần thi (7 ngày) | {vnd(GIA['tuan_thi'])} | | |")
    o.append(f"| Tháng (đồ án, thực tập) | {vnd(GIA['thang'])} | | DH Lend 1.000.000đ/tháng |")
    o.append(f"| Phí miễn trừ thiệt hại | {vnd(GIA['mien_tru'])}/lượt · {vnd(GIA['mien_tru_thang'])}/tháng | tự chọn | |")
    o.append(f"| Tiền cọc | 300.000đ · 150.000đ hạng B · 0đ hạng A | hoàn trong 5 phút | |")

    pr, kh, cd, dtl, dtm, cap = pnl()
    o.append("\n### T-PNL\n")
    o.append("| Tháng | Bối cảnh | Lượt thuê | Máy-tháng | Doanh thu | Lợi nhuận gộp | EBITDA | LNST | Luỹ kế |")
    o.append("|---|---|---|---|---|---|---|---|---|")
    for r in pr:
        o.append("| {t} | {s} | {l} | {m} | {dt} | {lg} | {eb} | {ln} | {lk} |".format(
            t=r["thang"], s=r["su_kien"], l=r["luot"], m=r["may_thang"],
            dt=vnd(r["doanh_thu"]), lg=vnd(r["loi_gop"]), eb=vnd(r["ebitda"]),
            ln=vnd(r["ln"]), lk=vnd(r["luy_ke"])))
    o.append("| **CẢ NĂM** | | **{l}** | **{m}** | **{dt}** | **{lg}** | **{eb}** | **{ln}** | |".format(
        l=sum(r["luot"] for r in pr), m=sum(r["may_thang"] for r in pr),
        dt=vnd(sum(r["doanh_thu"] for r in pr)), lg=vnd(sum(r["loi_gop"] for r in pr)),
        eb=vnd(sum(r["ebitda"] for r in pr)), ln=vnd(sum(r["ln"] for r in pr))))

    hv = diem_hoa_von()
    o.append("\n### T-HOAVON\n")
    o.append("| Chỉ tiêu | Giá trị |")
    o.append("|---|---|")
    o.append(f"| Doanh thu bình quân mỗi lượt thuê | {vnd(dtl)} |")
    o.append(f"| Chi phí biến đổi mỗi lượt | {vnd(hv['bien_luot'])} |")
    o.append(f"| Số dư đóng góp mỗi lượt | **{vnd(hv['dong_gop_moi_luot'])}** |")
    o.append(f"| Định phí hằng tháng | {vnd(cd)} |")
    o.append(f"| Khấu hao hằng tháng | {vnd(kh)} |")
    o.append(f"| **Hoà vốn tiền mặt** | **{hv['hoa_von_tien_mat']:.0f} lượt/tháng** |")
    o.append(f"| **Hoà vốn kế toán** | **{hv['hoa_von_ke_toan']:.0f} lượt/tháng** |")

    o.append("\n### T-KICHBAN\n")
    o.append("| Kịch bản | Giả định | Doanh thu năm 1 | LNST năm 1 | Biên LN | Hoàn vốn |")
    o.append("|---|---|---|---|---|---|")
    gt = {"Thận trọng": "nhu cầu bằng 65% dự báo, giá giảm 10%",
          "Cơ sở": "đúng dự báo ở Bảng T-PNL",
          "Thuận lợi": "nhu cầu bằng 135% dự báo, giá tăng 5%"}
    for k, v in kich_ban().items():
        hvt = f"{v['thang_hoan_von']:.0f} tháng" if v["thang_hoan_von"] else "không hoàn vốn"
        o.append(f"| **{k}** | {gt[k]} | {vnd(v['doanh_thu'])} | {vnd(v['loi_nhuan'])} | "
                 f"{v['bien_ln']*100:.1f}% | {hvt} |")

    r2, kh2, cd2, capex2 = nam2()
    moc, hvm, c1_, c2_ = hoan_von_luy_ke()
    o.append("\n### T-NAM2\n")
    o.append("| Chỉ tiêu | Năm 1 (10 máy) | Năm 2 (16 máy) |")
    o.append("|---|---|---|")
    o.append(f"| Số lượt thuê theo ca/ngày/tuần | {sum(r['luot'] for r in pr)} | {sum(r['luot'] for r in r2)} |")
    o.append(f"| Số máy-tháng cho thuê dài hạn | {sum(r['may_thang'] for r in pr)} | {sum(r['may_thang'] for r in r2)} |")
    o.append(f"| Doanh thu | {vnd(sum(r['doanh_thu'] for r in pr))} | {vnd(sum(r['doanh_thu'] for r in r2))} |")
    o.append(f"| EBITDA | {vnd(sum(r['ebitda'] for r in pr))} | {vnd(sum(r['ebitda'] for r in r2))} |")
    o.append(f"| Lợi nhuận sau thuế | {vnd(sum(r['ln'] for r in pr))} | {vnd(sum(r['ln'] for r in r2))} |")
    o.append(f"| Tỉ lệ khai thác bình quân | {sum(r['cong_suat'] for r in pr)/12*100:.0f}% | {sum(r['cong_suat'] for r in r2)/12*100:.0f}% |")
    o.append(f"| Vốn đầu tư trong năm | {vnd(c1_)} | {vnd(c2_)} |")
    o.append(f"| **Điểm hoàn vốn** | | **tháng thứ {moc.index(hvm)+1} ({hvm[1]})** |")
    return "\n".join(o)


