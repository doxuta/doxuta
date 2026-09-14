# -*- coding: utf-8 -*-
"""render.py — dựng DOCX + PDF từ file nội dung Markdown mở rộng.

Chạy 2 lượt: lượt 1 đo số trang của từng đề mục trong PDF, lượt 2 ghi
số trang thật vào Mục lục rồi xuất PDF cuối cùng.
"""
import os, re, sys, json, subprocess, shutil
from docx import Document
import mdx
import refs as refmod
from mdx import Builder, setup, running_head, cover, toc, new_section, part_divider, muc_luc_phu

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOFFICE = "soffice"


# --------------------------------------------------------------- phân tích
def parse(src):
    lines = src.split("\n")
    blocks, i, n = [], 0, len(lines)
    while i < n:
        ln = lines[i]
        s = ln.strip()

        if not s:
            i += 1; continue

        m = re.match(r"^<<<part:(.*?)>>>$", s)
        if m:
            parts = [x.strip() for x in m.group(1).split("|")]
            while len(parts) < 3:
                parts.append("")
            blocks.append(("part", tuple(parts[:3]))); i += 1; continue

        m = re.match(r"^<<<(\w+)>>>$", s)
        if m:
            blocks.append(("cmd", m.group(1))); i += 1; continue

        if s.startswith(":::") and len(s) > 3:
            head = s[3:].strip()
            kind, _, title = head.partition(" ")
            body = []
            i += 1
            while i < n and lines[i].strip() != ":::":
                body.append(lines[i].strip()); i += 1
            i += 1
            blocks.append(("callout", (kind, title.strip(), [x for x in body if x])))
            continue

        if s.startswith("```"):
            lang = s[3:].strip()
            body = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                body.append(lines[i]); i += 1
            i += 1
            opts, i = _opts(lines, i, n)
            blocks.append(("code", ("\n".join(body), opts.get("caption"))))
            continue

        m = re.match(r"^(#{1,4})(!?)\s+(.*)$", s)
        if m:
            lvl = len(m.group(1))
            blocks.append(("h", (lvl, m.group(3).strip(), m.group(2) != "!")))
            i += 1; continue

        m = re.match(r"^!\[(.*?)\]\((.*?)\)(.*)$", s)
        if m:
            rest = m.group(3)
            w = re.search(r"\{w=([\d.]+)\}", rest)
            srcn = re.search(r"\{src:\s*(.*?)\}", rest)
            blocks.append(("fig", (m.group(2), m.group(1),
                                   float(w.group(1)) if w else 15.0,
                                   srcn.group(1) if srcn else None)))
            i += 1; continue

        if s.startswith("|") and i + 1 < n and re.match(r"^\|[\s\-:|]+\|$", lines[i + 1].strip()):
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                raw = lines[i].strip()
                if not re.match(r"^\|[\s\-:|]+\|$", raw):
                    cells = [c.strip() for c in raw.strip("|").split("|")]
                    rows.append(cells)
                i += 1
            opts, i = _opts(lines, i, n)
            blocks.append(("table", (rows, opts)))
            continue

        m = re.match(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$", ln)
        if m:
            indent = len(m.group(1)) // 2
            ordered = not m.group(2) in ("-", "*", "+")
            text = m.group(3).strip()
            j = i + 1
            while j < n and lines[j].strip() and not re.match(r"^(\s*)([-*+]|\d+[.)])\s+", lines[j]) \
                  and not lines[j].strip().startswith(("#", "|", "!", ":::", "```", "<<<")):
                text += " " + lines[j].strip(); j += 1
            blocks.append(("li", (text, indent, ordered)))
            i = j; continue

        buf = [s]
        j = i + 1
        while j < n and lines[j].strip() and not re.match(
                r"^(#{1,4}[!\s]|\||!\[|:::|```|<<<|\s*[-*+]\s|\s*\d+[.)]\s)", lines[j]):
            buf.append(lines[j].strip()); j += 1
        blocks.append(("p", " ".join(buf)))
        i = j
    return blocks


def _opts(lines, i, n):
    o = {}
    while i < n and lines[i].strip().startswith("{") and lines[i].strip().endswith("}"):
        body = lines[i].strip()[1:-1]
        k, _, v = body.partition(":")
        o[k.strip()] = v.strip()
        i += 1
    return o, i



def tinh_hinh_bang(blocks):
    """Đếm trước hình và bảng có chú thích, theo đúng thứ tự xuất hiện."""
    figs, tabs = [], []
    for kind, val in blocks:
        if kind == "fig":
            path, cap, w, srcn = val
            fp = path if os.path.isabs(path) else os.path.join(ROOT, path)
            if cap and os.path.exists(fp):
                figs.append((len(figs) + 1, cap, "fig%d" % (len(figs) + 1)))
        elif kind == "table":
            rows, o = val
            if o.get("caption"):
                tabs.append((len(tabs) + 1, o["caption"], "tab%d" % (len(tabs) + 1)))
    return figs, tabs


def tinh_de_muc(blocks):
    """Tính trước danh sách đề mục và số thứ tự — dùng chung cho mục lục và cho lần dựng."""
    heads, c, h1_khong_so = [], [0] * 6, False
    for kind, val in blocks:
        if kind != "h":
            continue
        lvl, text, numbered = val
        if lvl == 1:
            h1_khong_so = not numbered
        elif h1_khong_so:
            numbered = False
        if numbered:
            c[lvl - 1] += 1
            for k in range(lvl, 6):
                c[k] = 0
            num = ".".join(str(c[k]) for k in range(lvl))
        else:
            num = ""
        if lvl <= 3:
            heads.append((lvl, num, text))
    return heads


# --------------------------------------------------------------- dựng file
def build(blocks, meta, out_docx, page_map=None, body_pt=11.5):
    doc = Document()
    setup(doc, body_pt=body_pt)
    b = Builder(doc, body_pt=body_pt)

    heads = tinh_de_muc(blocks)

    toc_entries = None
    hi = 0
    b.counters = [0] * 6

    for kind, val in blocks:
        if kind == "cmd":
            if val == "cover":
                cover(b, meta)
            elif val == "pagebreak":
                b.pagebreak()
            elif val == "toc":
                ents = [(lvl, num, text, "sec%d" % idx)
                        for idx, (lvl, num, text) in enumerate(heads)]
                toc(b, ents, page_map=page_map)
                toc_entries = ents
                b.pagebreak()
            elif val == "figindex":
                figs, _ = tinh_hinh_bang(blocks)
                muc_luc_phu(b, figs, "DANH MỤC HÌNH", "Hình", page_map=page_map)
                b.pagebreak()
            elif val == "tabindex":
                _, tabs = tinh_hinh_bang(blocks)
                muc_luc_phu(b, tabs, "DANH MỤC BẢNG", "Bảng", page_map=page_map)
                b.pagebreak()
            elif val == "landscape":
                new_section(doc, landscape=True)
                b.landscape = True
            elif val == "portrait":
                new_section(doc, landscape=False)
                b.landscape = False
            elif val == "rule":
                b.rule()
        elif kind == "part":
            part_divider(b, val[0], val[1], val[2])
        elif kind == "h":
            lvl, text, numbered = val
            b.heading(lvl, text, numbered=numbered)
        elif kind == "p":
            b.para(val)
        elif kind == "li":
            text, indent, ordered = val
            b.bullet(text, level=indent, ordered=ordered)
        elif kind == "table":
            rows, o = val
            widths = [float(x) for x in o["widths"].split(",")] if o.get("widths") else None
            right = set(int(x) for x in o["right"].split(",")) if o.get("right") else None
            b.table(rows, caption=o.get("caption"), widths=widths,
                    align_right=right, note=o.get("note"),
                    font_pt=float(o["fs"]) if o.get("fs") else None)
        elif kind == "fig":
            path, cap, w, srcn = val
            p = path if os.path.isabs(path) else os.path.join(ROOT, path)
            if w == 0:
                w = 25.4 if getattr(b, "landscape", False) else 16.0
            b.figure(p, caption=cap, width_cm=w, source=srcn)
        elif kind == "callout":
            k, t, body = val
            b.callout(k, t, body)
        elif kind == "code":
            txt, cap = val
            b.code(txt, caption=cap)

    running_head(doc, meta["running"])
    doc.save(out_docx)
    return b, toc_entries


# --------------------------------------------------------------- pdf
def to_pdf(docx_path, outdir):
    env = dict(os.environ, HOME="/root")
    subprocess.run([SOFFICE, "-env:UserInstallation=file:///tmp/lo_render",
                    "--headless", "--norestore", "--convert-to", "pdf",
                    "--outdir", outdir, docx_path],
                   check=True, capture_output=True, env=env, timeout=900)
    return os.path.join(outdir, os.path.splitext(os.path.basename(docx_path))[0] + ".pdf")


def _la_trang_muc_luc(txt):
    if "MỤC LỤC" in txt:
        return True
    return len(re.findall(r"\.{8,}\s*\d+\s*$", txt, re.M)) >= 4


def caption_pages(pdf, n_fig, n_tab, bo_qua):
    txt = subprocess.run(["pdftotext", "-layout", pdf, "-"],
                         capture_output=True, text=True, timeout=300).stdout
    pages = [re.sub(r"\s+", " ", p) for p in txt.split("\f")]
    out = {}
    for tien_to, khoa, n in (("Hình", "fig", n_fig), ("Bảng", "tab", n_tab)):
        start = bo_qua
        for i in range(1, n + 1):
            needle = "%s %d." % (tien_to, i)
            found = None
            for pi in range(start, len(pages)):
                if needle in pages[pi]:
                    found = pi + 1; start = pi; break
            out["%s%d" % (khoa, i)] = str(found or (bo_qua + 1))
    return out


def so_trang_bo_qua(pdf):
    txt = subprocess.run(["pdftotext", "-layout", pdf, "-"],
                         capture_output=True, text=True, timeout=300).stdout
    pages = txt.split("\f")
    bo_qua = 0
    for i, pg in enumerate(pages[:14]):
        if _la_trang_muc_luc(pg):
            bo_qua = i + 1
    return bo_qua


def heading_pages(pdf, heads):
    """Dò số trang của từng đề mục, bỏ qua trang bìa và các trang mục lục."""
    txt = subprocess.run(["pdftotext", "-layout", pdf, "-"],
                         capture_output=True, text=True, timeout=300).stdout
    pages = txt.split("\f")
    bo_qua = 0
    for i, pg in enumerate(pages[:8]):
        if _la_trang_muc_luc(pg):
            bo_qua = i + 1
    norm = [re.sub(r"\s+", " ", p) for p in pages]
    out, start = [], bo_qua
    for lvl, num, text in heads:
        clean = re.sub(r"\[\[\d+(?:,\s*\d+)*\]\]", "", text)
        clean = re.sub(r"[*`]", "", clean)
        clean = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", clean)
        clean = re.sub(r"\s+", " ", clean).strip()
        needle = re.sub(r"\s+", " ", (num + ". " if num else "") + clean)
        found = None
        for pi in range(start, len(norm)):
            if needle[:70] in norm[pi]:
                found = pi + 1; start = pi; break
        if found is None:
            for pi in range(start, len(norm)):
                if clean[:55] in norm[pi]:
                    found = pi + 1; start = pi; break
        out.append(found or (out[-1] if out else bo_qua + 1))
    return out


# --------------------------------------------------------------- điều phối
def main():
    content = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "content", "proposal.md")
    name = sys.argv[2] if len(sys.argv) > 2 else "Proposal-Thue-Laptop-Di-Thi"
    outdir = os.path.join(ROOT, "dist")
    os.makedirs(outdir, exist_ok=True)
    src = open(content, encoding="utf-8").read()

    # chèn nội dung các chương rời
    def _inc(m):
        rel = m.group(1).strip()
        fp = rel if os.path.isabs(rel) else os.path.join(ROOT, "content", rel)
        if not os.path.exists(fp):
            print("THIẾU FILE CHƯƠNG:", fp)
            return "*[chưa có nội dung: %s]*" % rel
        return open(fp, encoding="utf-8").read().strip()
    for _ in range(3):
        src, n = re.subn(r"<<<include:([^>]+)>>>", _inc, src)
        if not n:
            break

    # chèn các bảng tài chính sinh từ mô hình
    fin_path = os.path.join(ROOT, "content", "fin_tables.md")
    if os.path.exists(fin_path):
        blocks, cur = {}, None
        for line in open(fin_path, encoding="utf-8"):
            if line.startswith("### "):
                cur = line[4:].strip(); blocks[cur] = []
            elif cur:
                blocks[cur].append(line.rstrip("\n"))
        for k, v in blocks.items():
            src = src.replace("{{%s}}" % k, "\n".join(x for x in v).strip())
        con_lai = re.findall(r"\{\{T-[A-Z0-9]+\}\}", src)
        if con_lai:
            print("CẢNH BÁO: chỉ dấu bảng không nhận ra:", set(con_lai))

    sjson = os.path.join(ROOT, "content", "sources.json")
    src, bib = refmod.resolve(src, sjson if os.path.exists(sjson) else None)
    print("trích dẫn: %d nguồn" % len(bib))
    src = src.replace("<<<references>>>", refmod.bibliography_md(bib)
                      + "\n{caption: Danh mục tài liệu tham khảo, đánh số theo thứ tự xuất hiện trong bài}"
                      + "\n{widths: 0.6,7,3.2}\n{fs: 9}")
    meta = json.load(open(os.path.join(ROOT, "content", "meta.json"), encoding="utf-8"))
    blocks = parse(src)
    print("khối nội dung: %d" % len(blocks))

    heads = tinh_de_muc(blocks)
    print("đề mục vào mục lục: %d" % len(heads))

    docx_path = os.path.join(outdir, name + ".docx")
    page_map, prev = None, None
    for attempt in range(3):
        build(blocks, meta, docx_path, page_map=page_map)
        pdf = to_pdf(docx_path, outdir)
        pages = heading_pages(pdf, heads)
        new_map = {"sec%d" % i: str(pages[i]) for i in range(len(heads))}
        figs, tabs = tinh_hinh_bang(blocks)
        new_map.update(caption_pages(pdf, len(figs), len(tabs), so_trang_bo_qua(pdf)))
        print("lượt %d: trang cuối = %s" % (attempt + 1, pages[-1] if pages else "?"))
        if new_map == prev:
            print("số trang đã ổn định."); break
        prev = new_map
        page_map = new_map
    build(blocks, meta, docx_path, page_map=page_map)
    pdf = to_pdf(docx_path, outdir)
    npages = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout
    m = re.search(r"Pages:\s+(\d+)", npages)
    print("XONG → %s" % docx_path)
    print("XONG → %s  (%s trang)" % (pdf, m.group(1) if m else "?"))


if __name__ == "__main__":
    main()
