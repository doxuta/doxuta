# -*- coding: utf-8 -*-
"""Đối chiếu các con số then chốt trong bài với hồ sơ dữ kiện chuẩn."""
import os, re, glob, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import finmodel as F

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEC = os.path.join(ROOT, "content", "sections")

# (mô tả, biểu thức tìm, giá trị đúng)
def vnd(x):
    return F.vnd(x)

pnl, kh, cd, dtl, dtm, capex = F.pnl()
r2, kh2, cd2, capex2 = F.nam2()
hv = F.diem_hoa_von()

CHUAN = {
    "tổng vốn đầu tư": vnd(capex),
    "định phí hằng tháng": vnd(cd),
    "khấu hao hằng tháng": vnd(kh),
    "doanh thu năm 1": vnd(sum(r["doanh_thu"] for r in pnl)),
    "LNST năm 1": vnd(sum(r["ln"] for r in pnl)),
    "EBITDA năm 1": vnd(sum(r["ebitda"] for r in pnl)),
    "doanh thu năm 2": vnd(sum(r["doanh_thu"] for r in r2)),
    "doanh thu mỗi lượt": vnd(dtl),
    "số lượt năm 1": str(sum(r["luot"] for r in pnl)),
    "giá ca thi": vnd(F.GIA["ca_thi"]),
    "giá ngày thi": vnd(F.GIA["ngay_thi"]),
    "giá khẩn cấp": vnd(F.GIA["khan_cap"]),
    "giá tuần": vnd(F.GIA["tuan_thi"]),
    "giá tháng": vnd(F.GIA["thang"]),
    "phí miễn trừ": vnd(F.GIA["mien_tru"]),
    "số máy năm 1": str(F.N),
    "số máy năm 2": str(F.FLEET_N2),
}

# các con số dễ bị viết sai (biến thể sai phổ biến)
NGHI_NGO = [
    (r"18 máy", "đội máy năm 1 là 10 máy, năm 2 là 16 máy — '18 máy' là số cũ"),
    (r"45\.000đ", "giá ca thi là 79.000đ, không phải 45.000đ"),
    (r"355\.000đ", "tổng đơn mẫu là 414.000đ"),
    (r"10\.000đ\s*(?:/|mỗi)\s*lượt", "phí miễn trừ thiệt hại là 15.000đ mỗi lượt"),
    (r"\bVNĐ\b", "dùng 'đ' thay cho 'VNĐ' trong thân bài"),
    (r"132\.000\.000", "vốn thiết bị là 72.500.000đ"),
    (r"159\.790\.000", "tổng vốn đầu tư là 93.250.000đ"),
]

if __name__ == "__main__":
    print("GIÁ TRỊ CHUẨN (sinh từ finmodel.py)")
    for k, v in CHUAN.items():
        print("  %-24s %s" % (k, v))
    print("\nQUÉT CÁC CHƯƠNG")
    tong = 0
    for f in sorted(glob.glob(os.path.join(SEC, "*.md"))):
        txt = open(f, encoding="utf-8").read()
        hits = []
        for pat, msg in NGHI_NGO:
            for m in re.finditer(pat, txt):
                ctx = re.sub(r"\s+", " ", txt[max(0, m.start() - 55):m.end() + 40])
                hits.append("%s → %s" % (msg, ctx))
        if hits:
            print("\n  %s" % os.path.basename(f))
            for h in hits[:6]:
                print("    ! " + h)
            if len(hits) > 6:
                print("    ! ... và %d chỗ nữa" % (len(hits) - 6))
            tong += len(hits)
    print("\nTổng số chỗ nghi ngờ: %d" % tong)
