# -*- coding: utf-8 -*-
"""Kết xuất toàn bộ sơ đồ mermaid ra PNG và báo cáo khả năng đọc khi in."""
import os, re, sys, subprocess, json
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "diagrams")
OUT = os.path.join(os.path.dirname(HERE), "assets", "diagrams")
CFG = os.path.join(HERE, "mermaid-config.json")
PPT = os.path.join(HERE, "puppeteer.json")
FONT_PX = json.load(open(CFG))["themeVariables"]["fontSize"]
FONT_PX = float(re.sub(r"[^\d.]", "", FONT_PX))
os.makedirs(OUT, exist_ok=True)

def natural(mmd):
    svg = "/tmp/_nat.svg"
    subprocess.run(["mmdc", "-i", mmd, "-o", svg, "-p", PPT, "-c", CFG, "-b", "white"],
                   capture_output=True, timeout=420)
    s = open(svg, encoding="utf-8").read()[:1200]
    vb = re.search(r'viewBox="([-\d.]+) ([-\d.]+) ([\d.]+) ([\d.]+)"', s)
    if not vb:
        return None, None
    return float(vb.group(3)), float(vb.group(4))

def pt_fit(css_w, css_h, page_w_cm, page_h_cm):
    """Cỡ chữ in thực tế khi hình được thu vừa khung trang."""
    eff_w = min(page_w_cm, page_h_cm * css_w / css_h)
    return FONT_PX / css_w * eff_w / 2.54 * 72

def build(names=None):
    files = sorted(f for f in os.listdir(SRC) if f.endswith(".mmd"))
    if names:
        files = [f for f in files if any(n in f for n in names)]
    rows = []
    for f in files:
        stem = f[:-4]
        mmd = os.path.join(SRC, f)
        w, h = natural(mmd)
        if not w:
            print("LỖI dựng:", stem); continue
        # kết xuất PNG ở độ phân giải cao: 2.5x kích thước tự nhiên
        png = os.path.join(OUT, stem + ".png")
        r = subprocess.run(["mmdc", "-i", mmd, "-o", png, "-p", PPT, "-c", CFG,
                            "-b", "white", "-w", str(int(w * 2.5)), "-s", "1"],
                           capture_output=True, timeout=420)
        ok = os.path.exists(png)
        rows.append((stem, w, h, w / h, pt_fit(w, h, 16.0, 23.0), pt_fit(w, h, 25.4, 16.2), ok))
    print("%-26s %7s %7s %6s %9s %9s  %s" % ("sơ đồ", "rộng", "cao", "tỉ lệ", "pt|dọc", "pt|ngang", "kết luận"))
    for stem, w, h, r, p16, p25, ok in rows:
        if p16 >= 7.6:   flag = "ĐẠT — trang dọc"
        elif p25 >= 7.6: flag = "ĐẠT — cần TRANG NGANG"
        else:            flag = "*** CHƯA ĐẠT: phải tách nhỏ hoặc rút gọn chữ ***"
        print("%-26s %7.0f %7.0f %6.2f %9.1f %9.1f  %s" % (stem, w, h, r, p16, p25, flag))

if __name__ == "__main__":
    build(sys.argv[1:] or None)
