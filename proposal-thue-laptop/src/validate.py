# -*- coding: utf-8 -*-
"""Kiểm tra các chương đã soạn: đường dẫn hình, cú pháp, và tính xác thực của URL trích dẫn."""
import os, re, sys, glob, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEC = os.path.join(ROOT, "content", "sections")
RES = os.path.join(ROOT, "research")

def urls_trong_nghien_cuu():
    tap = set()
    for f in glob.glob(os.path.join(RES, "*.md")) + glob.glob(os.path.join(RES, "_snapshot", "*.md")):
        txt = open(f, encoding="utf-8").read()
        for u in re.findall(r"https?://[^\s\)\]\|<>\"']+", txt):
            tap.add(u.rstrip(").,;:'\"").rstrip("/"))
    return tap

def chuan(u):
    return u.rstrip(").,;:'\"").rstrip("/")

def kiem_tra(path, known):
    txt = open(path, encoding="utf-8").read()
    loi, canh = [], []
    name = os.path.basename(path)

    # 1) hình ảnh
    for cap, p in re.findall(r"!\[([^\]]*)\]\(([^)]+)\)", txt):
        fp = p if os.path.isabs(p) else os.path.join(ROOT, p)
        if not os.path.exists(fp):
            loi.append(f"thiếu hình: {p}")
        if not cap.strip():
            canh.append(f"hình không có chú thích: {p}")

    # 2) landscape / portrait cân bằng
    l = len(re.findall(r"<<<landscape>>>", txt)); pr = len(re.findall(r"<<<portrait>>>", txt))
    if l != pr:
        loi.append(f"landscape({l}) khác portrait({pr})")

    # 3) chỉ dấu bảng tài chính
    fin = os.path.join(ROOT, "content", "fin_tables.md")
    co = set(re.findall(r"^### (T-[A-Z0-9]+)", open(fin, encoding="utf-8").read(), re.M)) if os.path.exists(fin) else set()
    for m in re.findall(r"\{\{(T-[A-Z0-9]+)\}\}", txt):
        if m not in co:
            loi.append(f"chỉ dấu bảng không tồn tại: {{{{{m}}}}}")

    # 4) URL trích dẫn có thật trong nghiên cứu không
    refs = re.findall(r"\[\[ref:\s*(https?://[^\]\|\s]+)", txt)
    la = [u for u in refs if chuan(u) not in known]
    for u in sorted(set(la)):
        canh.append(f"URL không thấy trong file nghiên cứu: {u}")

    # 5) bảng: dòng phân cách
    for i, ln in enumerate(txt.split("\n")):
        if ln.strip().startswith("|") and ln.strip().endswith("|"):
            pass
    # 6) tiêu đề cấp 1 lọt vào file chương
    if re.search(r"^# [^#]", txt, re.M):
        loi.append("có tiêu đề cấp 1 (#) — chương chỉ được dùng ## trở xuống")

    # 7) tiền tệ sai định dạng
    for m in re.findall(r"\d[\d.,]*\s?VNĐ", txt):
        canh.append(f"dùng 'VNĐ' thay vì 'đ': {m}")

    return name, loi, canh, len(refs), len(txt.split())

if __name__ == "__main__":
    known = urls_trong_nghien_cuu()
    print("URL có thật trong kho nghiên cứu: %d\n" % len(known))
    tong_loi = tong_canh = 0
    for f in sorted(glob.glob(os.path.join(SEC, "*.md"))):
        name, loi, canh, nrefs, nw = kiem_tra(f, known)
        status = "LỖI" if loi else ("cảnh báo" if canh else "ok")
        print("%-26s %6d chữ %4d trích dẫn  [%s]" % (name, nw, nrefs, status))
        for x in loi:
            print("    ✗ " + x)
        for x in canh[:8]:
            print("    ! " + x)
        if len(canh) > 8:
            print("    ! ... và %d cảnh báo nữa" % (len(canh) - 8))
        tong_loi += len(loi); tong_canh += len(canh)
    print("\nTổng: %d lỗi, %d cảnh báo" % (tong_loi, tong_canh))
