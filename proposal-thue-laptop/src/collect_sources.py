# -*- coding: utf-8 -*-
"""Gom toàn bộ nguồn tham khảo từ các file nghiên cứu thành một danh mục duy nhất."""
import os, re, json, sys
from collections import OrderedDict

RES = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "research")
LINK = re.compile(r"\[([^\]\[]{3,200}?)\]\((https?://[^)\s]+)\)")

SKIP_HOST = ("localhost", "example.com")

def norm(url):
    u = url.rstrip(").,;")
    u = re.sub(r"#.*$", "", u)
    u = re.sub(r"\?utm_[^&]*(&|$)", "", u)
    return u.rstrip("/")

def collect():
    out = OrderedDict()
    for f in sorted(os.listdir(RES)):
        if not f.endswith(".md"):
            continue
        txt = open(os.path.join(RES, f), encoding="utf-8").read()
        for title, url in LINK.findall(txt):
            u = norm(url)
            if any(s in u for s in SKIP_HOST):
                continue
            t = re.sub(r"\s+", " ", title).strip()
            t = re.sub(r"^[\*_`]+|[\*_`]+$", "", t)
            if u not in out:
                out[u] = {"url": u, "titles": [], "files": []}
            if t and t not in out[u]["titles"]:
                out[u]["titles"].append(t)
            if f not in out[u]["files"]:
                out[u]["files"].append(f)
    # chọn tiêu đề dài nhất, gọn nhất làm tiêu đề chính
    for u, d in out.items():
        d["title"] = max(d["titles"], key=len) if d["titles"] else u
        host = re.sub(r"^https?://(www\.)?", "", u).split("/")[0]
        d["host"] = host
    return list(out.values())

if __name__ == "__main__":
    srcs = collect()
    srcs.sort(key=lambda d: (d["host"], d["title"]))
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "sources.json")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    json.dump(srcs, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("tổng số nguồn duy nhất: %d" % len(srcs))
    from collections import Counter
    c = Counter(d["host"] for d in srcs)
    for h, n in c.most_common(20):
        print("  %-42s %d" % (h, n))
