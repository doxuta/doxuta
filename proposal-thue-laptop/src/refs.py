# -*- coding: utf-8 -*-
"""Xử lý trích dẫn: [[ref:URL]] hoặc [[ref:URL|Tiêu đề]] -> số [[n]] + sinh danh mục."""
import os, re, json

REF = re.compile(r"\[\[ref:\s*(https?://[^\]\|\s]+)\s*(?:\|\s*([^\]]+?)\s*)?\]\]")
HOSTNAME = re.compile(r"^https?://(www\.)?")


def load_titles(path):
    if not os.path.exists(path):
        return {}
    data = json.load(open(path, encoding="utf-8"))
    out = {}
    for d in data:
        out[d["url"].rstrip("/")] = d.get("title") or d["url"]
    return out


def resolve(src, sources_json=None):
    """Trả về (văn bản đã thay số, danh sách nguồn theo thứ tự xuất hiện)."""
    titles = load_titles(sources_json) if sources_json else {}
    order, meta = [], {}

    def sub(m):
        url = m.group(1).rstrip(").,;").rstrip("/")
        title = m.group(2)
        if url not in meta:
            order.append(url)
            meta[url] = {
                "url": url,
                "title": title or titles.get(url) or HOSTNAME.sub("", url),
                "n": len(order),
            }
        elif title and not meta[url].get("explicit"):
            meta[url]["title"] = title
            meta[url]["explicit"] = True
        return "[[%d]]" % meta[url]["n"]

    text = REF.sub(sub, src)
    return text, [meta[u] for u in order]


def bibliography_md(items, per_group=None):
    """Sinh khối markdown cho mục Tài liệu tham khảo."""
    lines = []
    for it in items:
        host = HOSTNAME.sub("", it["url"]).split("/")[0]
        lines.append("| **%d** | %s | [%s](%s) |" % (
            it["n"], it["title"].replace("|", "-").replace("[", "(").replace("]", ")"),
            host, it["url"]))
    head = ["| # | Tiêu đề nguồn | Nguồn trực tuyến |", "|---|---|---|"]
    return "\n".join(head + lines)
