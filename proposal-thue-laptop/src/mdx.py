# -*- coding: utf-8 -*-
"""mdx.py — bộ dựng tài liệu DOCX từ Markdown mở rộng.

Hỗ trợ:
  # .. ###### đề mục (tự đánh số 1. / 1.1 / 1.1.1)
  **đậm**, *nghiêng*, `mã`, [chữ](url), [[n]] trích dẫn nguồn
  - gạch đầu dòng (lồng bằng 2 khoảng trắng), 1. danh sách số
  | bảng | pipe |    (dòng thứ 2 là ---)
  ![Chú thích](đường/dẫn.png){w=15}   ảnh + caption "Hình N."
  :::note Tiêu đề / nội dung / :::     khối chú ý
  ```lang ... ```                      khối mã
  <<<toc>>>  <<<pagebreak>>>  <<<cover>>>
"""
import re, os, copy
from docx import Document
from docx.shared import Pt, Cm, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK, WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn, nsmap
from docx.oxml import OxmlElement

# ----------------------------------------------------------------- bảng màu
NAVY   = RGBColor(0x14, 0x2C, 0x4A)
BLUE   = RGBColor(0x1B, 0x5E, 0x9E)
ACCENT = RGBColor(0xC2, 0x41, 0x1C)
GREY   = RGBColor(0x55, 0x5B, 0x63)
LIGHT  = "EEF2F7"
ZEBRA  = "F7F9FB"
NOTEBG = {"note": "EAF2FB", "warn": "FDF1E7", "ok": "EAF6EE", "risk": "FBEAEA"}
NOTEBR = {"note": "1B5E9E", "warn": "C2411C", "ok": "1E7A46", "risk": "B3261E"}
NOTETT = {"note": "GHI CHÚ", "warn": "LƯU Ý", "ok": "KẾT LUẬN", "risk": "RỦI RO"}

BODY_FONT = "Times New Roman"
HEAD_FONT = "Arial"
MONO_FONT = "Consolas"


def _shade(el, fill):
    sh = OxmlElement("w:shd"); sh.set(qn("w:val"), "clear")
    sh.set(qn("w:color"), "auto"); sh.set(qn("w:fill"), fill)
    el.append(sh)


_PPR_AFTER_PBDR = ["shd", "tabs", "suppressAutoHyphens", "kinsoku", "wordWrap",
                   "overflowPunct", "topLinePunct", "autoSpaceDE", "autoSpaceDN",
                   "bidi", "adjustRightInd", "snapToGrid", "spacing", "ind",
                   "contextualSpacing", "mirrorIndents", "suppressOverlap", "jc",
                   "textDirection", "textAlignment", "textboxTightWrap",
                   "outlineLvl", "divId", "cnfStyle", "rPr", "sectPr"]


def _borders(el, edges, sz=6, color="BFCBD8", val="single"):
    """el: phần tử <w:p>. Chèn <w:pBdr> đúng thứ tự lược đồ OOXML."""
    pPr = el.find(qn("w:pPr"))
    if pPr is None:
        pPr = OxmlElement("w:pPr"); el.insert(0, pPr)
    pbdr = pPr.find(qn("w:pBdr"))
    if pbdr is None:
        pbdr = OxmlElement("w:pBdr")
        anchor = None
        for child in pPr:
            tag = child.tag.split("}")[-1]
            if tag in _PPR_AFTER_PBDR:
                anchor = child; break
        if anchor is not None:
            anchor.addprevious(pbdr)
        else:
            pPr.append(pbdr)
    for e in edges:
        b = OxmlElement("w:" + e)
        b.set(qn("w:val"), val); b.set(qn("w:sz"), str(sz))
        b.set(qn("w:space"), "4"); b.set(qn("w:color"), color)
        pbdr.append(b)


def _fld(par, instr):
    r = par.add_run()._r
    f1 = OxmlElement("w:fldChar"); f1.set(qn("w:fldCharType"), "begin")
    it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = instr
    f2 = OxmlElement("w:fldChar"); f2.set(qn("w:fldCharType"), "separate")
    t  = OxmlElement("w:t"); t.text = "1"
    f3 = OxmlElement("w:fldChar"); f3.set(qn("w:fldCharType"), "end")
    r.append(f1); r.append(it); r.append(f2); r.append(t); r.append(f3)


def _bookmark(par, name, bid):
    s = OxmlElement("w:bookmarkStart"); s.set(qn("w:id"), str(bid)); s.set(qn("w:name"), name)
    e = OxmlElement("w:bookmarkEnd"); e.set(qn("w:id"), str(bid))
    par._p.insert(0, s); par._p.append(e)


def _hyperlink(par, text, url, doc):
    part = doc.part
    rid = part.relate_to(url,
        "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink",
        is_external=True)
    h = OxmlElement("w:hyperlink"); h.set(qn("r:id"), rid)
    r = OxmlElement("w:r"); rPr = OxmlElement("w:rPr")
    c = OxmlElement("w:color"); c.set(qn("w:val"), "1B5E9E")
    u = OxmlElement("w:u"); u.set(qn("w:val"), "single")
    rPr.append(c); rPr.append(u); r.append(rPr)
    t = OxmlElement("w:t"); t.set(qn("xml:space"), "preserve"); t.text = text
    r.append(t); h.append(r); par._p.append(h)


def _internal_link(par, text, anchor, color="1B5E9E"):
    h = OxmlElement("w:hyperlink"); h.set(qn("w:anchor"), anchor)
    r = OxmlElement("w:r"); rPr = OxmlElement("w:rPr")
    c = OxmlElement("w:color"); c.set(qn("w:val"), color)
    rPr.append(c); r.append(rPr)
    t = OxmlElement("w:t"); t.set(qn("xml:space"), "preserve"); t.text = text
    r.append(t); h.append(r); par._p.append(h)


# ----------------------------------------------------------------- inline
INLINE = re.compile(
    r"(\*\*.+?\*\*|(?<![\w*])\*[^*\n]+?\*(?![\w*])|`[^`]+?`|\[\[\d+(?:,\s*\d+)*\]\]|\[[^\]\[]+?\]\([^)\s]+?\))"
)


def add_inline(par, text, doc, base_size=None, bold=False, italic=False, color=None):
    """Ghi đoạn văn có định dạng nội tuyến vào paragraph."""
    for tok in INLINE.split(text):
        if not tok:
            continue
        if tok.startswith("**") and tok.endswith("**") and len(tok) > 4:
            r = par.add_run(tok[2:-2]); r.bold = True
        elif tok.startswith("*") and tok.endswith("*") and len(tok) > 2:
            r = par.add_run(tok[1:-1]); r.italic = True
        elif tok.startswith("`") and tok.endswith("`") and len(tok) > 2:
            r = par.add_run(tok[1:-1]); r.font.name = MONO_FONT
            r.font.size = Pt((base_size or 12) - 2.0)
            r.font.color.rgb = RGBColor(0x8A, 0x30, 0x12)
        elif tok.startswith("[[") and tok.endswith("]]"):
            nums = tok[2:-2]
            r = par.add_run("[" + nums + "]")
            r.font.superscript = True
            r.font.color.rgb = BLUE
            r.font.size = Pt((base_size or 12) - 1.5)
            continue
        else:
            m = re.match(r"\[([^\]]+?)\]\(([^)\s]+?)\)", tok)
            if m:
                _hyperlink(par, m.group(1), m.group(2), doc)
                continue
            r = par.add_run(tok)
        if base_size:
            r.font.size = Pt(base_size)
        if bold:
            r.bold = True
        if italic:
            r.italic = True
        if color is not None:
            r.font.color.rgb = color


# ----------------------------------------------------------------- styles
def setup(doc, body_pt=12.0):
    st = doc.styles["Normal"]
    st.font.name = BODY_FONT; st.font.size = Pt(body_pt)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), BODY_FONT)
    pf = st.paragraph_format
    pf.space_after = Pt(6); pf.space_before = Pt(0)
    pf.line_spacing = 1.35
    pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    spec = {
        "Heading 1": (16.5, NAVY, True, 18, 8),
        "Heading 2": (13.5, BLUE, True, 14, 6),
        "Heading 3": (12.0, NAVY, True, 11, 4),
        "Heading 4": (11.5, GREY, True, 9, 3),
    }
    for name, (sz, col, bold, sb, sa) in spec.items():
        s = doc.styles[name]
        s.font.name = HEAD_FONT; s.font.size = Pt(sz)
        s.font.bold = bold; s.font.color.rgb = col
        s.element.rPr.rFonts.set(qn("w:eastAsia"), HEAD_FONT)
        s.font.all_caps = False
        p = s.paragraph_format
        p.space_before = Pt(sb); p.space_after = Pt(sa)
        p.line_spacing = 1.15
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.keep_with_next = True

    for sec in doc.sections:
        sec.page_height = Cm(29.7); sec.page_width = Cm(21.0)
        sec.top_margin = Cm(2.2); sec.bottom_margin = Cm(2.2)
        sec.left_margin = Cm(2.6); sec.right_margin = Cm(2.0)
        sec.header_distance = Cm(1.2); sec.footer_distance = Cm(1.2)

    # ngôn ngữ mặc định: tiếng Việt (để Word không gạch đỏ toàn bộ)
    st_norm = doc.styles["Normal"].element.get_or_add_rPr()
    lang = OxmlElement("w:lang")
    lang.set(qn("w:val"), "vi-VN"); lang.set(qn("w:eastAsia"), "vi-VN"); lang.set(qn("w:bidi"), "ar-SA")
    st_norm.append(lang)

    # bật cập nhật trường khi mở bằng Word
    s = doc.settings.element
    uf = OxmlElement("w:updateFields"); uf.set(qn("w:val"), "true")
    s.append(uf)
    return doc


def thuoc_tinh(doc, meta):
    """Điền thuộc tính tài liệu để Word và trình đọc PDF hiển thị đúng."""
    cp = doc.core_properties
    cp.title = "%s — %s" % (meta.get("title", ""), meta.get("subtitle", ""))
    cp.subject = meta.get("kicker", "")
    cp.author = meta.get("org", "")
    cp.category = "Đề xuất dự án khởi nghiệp"
    cp.comments = meta.get("tagline", "")
    cp.keywords = "cho thuê laptop; kỳ thi; Đại học FPT Đà Nẵng; khởi nghiệp; ExamLap"
    cp.language = "vi-VN"
    return doc


def running_head(doc, left_text):
    sec = doc.sections[0]
    sec.different_first_page_header_footer = True
    h = sec.header.paragraphs[0]
    h.text = ""
    r = h.add_run(left_text)
    r.font.size = Pt(8.5); r.font.name = HEAD_FONT; r.font.color.rgb = GREY
    h.alignment = WD_ALIGN_PARAGRAPH.LEFT
    _borders(h._p, ["bottom"], sz=4, color="C9D3DE")

    f = sec.footer.paragraphs[0]
    f.text = ""
    f.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _fld(f, " PAGE ")
    for r in f.runs:
        r.font.size = Pt(9); r.font.name = HEAD_FONT; r.font.color.rgb = GREY


# ----------------------------------------------------------------- blocks
class Builder:
    def __init__(self, doc, figure_prefix="Hình", table_prefix="Bảng", body_pt=12.0):
        self.doc = doc
        self.body_pt = body_pt
        self.fig_n = 0
        self.tab_n = 0
        self.bid = 1000
        self.headings = []           # (level, number, text, anchor)
        self.figures = []            # (số, chú thích, anchor)
        self.tables = []             # (số, chú thích, anchor)
        self.counters = [0, 0, 0, 0, 0, 0]
        self.fig_prefix = figure_prefix
        self.tab_prefix = table_prefix
        self.numbering_from = 1      # chỉ đánh số từ H1 thứ n trở đi
        self.no_number = set()

    # ---------- đề mục
    def heading(self, level, text, numbered=True):
        if level == 1:
            self.h1_khong_so = not numbered     # chương này có đánh số hay không
        elif getattr(self, "h1_khong_so", False):
            numbered = False                    # mục con của chương không đánh số
        if numbered:
            self.counters[level - 1] += 1
            for i in range(level, 6):
                self.counters[i] = 0
            parts = [str(self.counters[i]) for i in range(level)]
            num = ".".join(parts)
            label = num + ". " if level == 1 else num + " "
        else:
            num, label = "", ""
        p = self.doc.add_paragraph(style="Heading %d" % min(level, 4))
        self.bid += 1
        anchor = ("sec%d" % len(self.headings)) if level <= 3 else ("h%d" % self.bid)
        if level == 1:
            p.paragraph_format.page_break_before = False
        if label:
            r = p.add_run(label); r.bold = True
        add_inline(p, text, self.doc)
        for r in p.runs:
            r.font.name = HEAD_FONT
        _bookmark(p, anchor, self.bid)
        if level <= 3:
            self.headings.append((level, num, text, anchor))
        if level == 1:
            _borders(p._p, ["bottom"], sz=8, color="1B5E9E")
        return p

    # ---------- đoạn văn
    def para(self, text, style=None, size=None, space_after=6, align=None, indent=None):
        p = self.doc.add_paragraph(style=style)
        add_inline(p, text, self.doc, base_size=size or self.body_pt)
        p.paragraph_format.space_after = Pt(space_after)
        if align == "center":
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        elif align == "left":
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        if indent:
            p.paragraph_format.left_indent = Cm(indent)
        return p

    # ---------- danh sách
    def bullet(self, text, level=0, ordered=False):
        style = "List Number" if ordered else "List Bullet"
        try:
            p = self.doc.add_paragraph(style=style)
        except KeyError:
            p = self.doc.add_paragraph()
        add_inline(p, text, self.doc, base_size=self.body_pt)
        pf = p.paragraph_format
        pf.left_indent = Cm(0.75 + 0.65 * level)
        pf.first_line_indent = Cm(-0.45)
        pf.space_after = Pt(3)
        pf.line_spacing = 1.28
        return p

    # ---------- bảng
    def table(self, rows, caption=None, widths=None, header=True, font_pt=None,
              align_right=None, note=None):
        fp = font_pt or (self.body_pt - 1.5)
        ncols = max(len(r) for r in rows)
        rows = [r + [""] * (ncols - len(r)) for r in rows]
        t = self.doc.add_table(rows=len(rows), cols=ncols)
        t.style = "Table Grid"
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        t.autofit = False
        tblPr = t._tbl.tblPr
        lay = OxmlElement("w:tblLayout"); lay.set(qn("w:type"), "fixed")
        tblPr.append(lay)
        total = self.doc.sections[0].page_width - self.doc.sections[0].left_margin - self.doc.sections[0].right_margin
        if widths:
            s = float(sum(widths))
            cw = [Emu(int(total * w / s)) for w in widths]
        else:
            cw = [Emu(int(total / ncols))] * ncols
        for ri, row in enumerate(rows):
            tr = t.rows[ri]
            if header and ri == 0:
                trPr = tr._tr.get_or_add_trPr()
                th = OxmlElement("w:tblHeader"); trPr.append(th)
            for ci, cell in enumerate(row):
                c = t.cell(ri, ci)
                c.width = cw[ci]
                p = c.paragraphs[0]
                p.paragraph_format.space_before = Pt(2)
                p.paragraph_format.space_after = Pt(2)
                p.paragraph_format.line_spacing = 1.12
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                if align_right and ci in align_right and not (header and ri == 0):
                    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
                txt = str(cell)
                is_head = header and ri == 0
                add_inline(p, txt, self.doc, base_size=fp,
                           bold=is_head, color=RGBColor(0xFF, 0xFF, 0xFF) if is_head else None)
                for r in p.runs:
                    r.font.name = HEAD_FONT
                if is_head:
                    _shade(c._tc.get_or_add_tcPr(), "1B5E9E")
                elif ri % 2 == 0:
                    _shade(c._tc.get_or_add_tcPr(), ZEBRA)
        if caption:
            self.tab_n += 1
            cp = self.doc.add_paragraph()
            self.bid += 1
            _bookmark(cp, "tab%d" % self.tab_n, self.bid)
            self.tables.append((self.tab_n, caption, "tab%d" % self.tab_n))
            cp.alignment = WD_ALIGN_PARAGRAPH.LEFT
            r = cp.add_run("%s %d. " % (self.tab_prefix, self.tab_n))
            r.bold = True; r.font.size = Pt(fp - 0.5); r.font.name = HEAD_FONT
            r.font.color.rgb = GREY
            add_inline(cp, caption, self.doc, base_size=fp - 0.5, italic=True, color=GREY)
            for r in cp.runs:
                r.font.name = HEAD_FONT
            cp.paragraph_format.space_before = Pt(3)
            cp.paragraph_format.space_after = Pt(10)
        if note:
            np_ = self.doc.add_paragraph()
            add_inline(np_, note, self.doc, base_size=fp - 1, italic=True, color=GREY)
            for r in np_.runs:
                r.font.name = HEAD_FONT
            np_.paragraph_format.space_after = Pt(10)
        return t



    # ---------- hình ảnh
    def figure(self, path, caption=None, width_cm=15.0, source=None):
        if not os.path.exists(path):
            self.para("*[thiếu hình: %s]*" % path, size=self.body_pt - 1)
            return
        p = self.doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(2)
        p.add_run().add_picture(path, width=Cm(width_cm))
        if caption:
            self.fig_n += 1
            cp = self.doc.add_paragraph()
            self.bid += 1
            _bookmark(cp, "fig%d" % self.fig_n, self.bid)
            self.figures.append((self.fig_n, caption, "fig%d" % self.fig_n))
            cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = cp.add_run("%s %d. " % (self.fig_prefix, self.fig_n))
            r.bold = True; r.font.size = Pt(self.body_pt - 2); r.font.name = HEAD_FONT
            r.font.color.rgb = GREY
            add_inline(cp, caption, self.doc, base_size=self.body_pt - 2, italic=True, color=GREY)
            for r in cp.runs:
                r.font.name = HEAD_FONT
            cp.paragraph_format.space_after = Pt(4)
        if source:
            sp = self.doc.add_paragraph()
            sp.alignment = WD_ALIGN_PARAGRAPH.CENTER
            add_inline(sp, source, self.doc, base_size=self.body_pt - 2.5, italic=True, color=GREY)
            for r in sp.runs:
                r.font.name = HEAD_FONT
            sp.paragraph_format.space_after = Pt(10)

    # ---------- khối chú ý
    def callout(self, kind, title, lines):
        fill = NOTEBG.get(kind, LIGHT); br = NOTEBR.get(kind, "1B5E9E")
        t = self.doc.add_table(rows=1, cols=1)
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = t.cell(0, 0)
        tcPr = cell._tc.get_or_add_tcPr()
        _shade(tcPr, fill)
        bd = OxmlElement("w:tcBorders")
        for e, w, col in (("left", 24, br), ("top", 2, fill), ("bottom", 2, fill), ("right", 2, fill)):
            x = OxmlElement("w:" + e); x.set(qn("w:val"), "single")
            x.set(qn("w:sz"), str(w)); x.set(qn("w:color"), col)
            bd.append(x)
        tcPr.append(bd)
        mar = OxmlElement("w:tcMar")
        for e, v in (("top", 140), ("bottom", 140), ("left", 200), ("right", 160)):
            x = OxmlElement("w:" + e); x.set(qn("w:w"), str(v)); x.set(qn("w:type"), "dxa")
            mar.append(x)
        tcPr.append(mar)
        p = cell.paragraphs[0]
        r = p.add_run((NOTETT.get(kind, "GHI CHÚ") + " — " if not title else NOTETT.get(kind, "GHI CHÚ") + " — ") + title)
        r.bold = True; r.font.size = Pt(self.body_pt - 1.5)
        r.font.name = HEAD_FONT; r.font.color.rgb = RGBColor.from_string(br)
        p.paragraph_format.space_after = Pt(3)
        for i, ln in enumerate(lines):
            q = cell.add_paragraph()
            add_inline(q, ln, self.doc, base_size=self.body_pt - 1)
            q.paragraph_format.space_after = Pt(2 if i < len(lines) - 1 else 0)
            q.paragraph_format.line_spacing = 1.25
            q.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        sp = self.doc.add_paragraph(); sp.paragraph_format.space_after = Pt(6)
        sp.paragraph_format.line_spacing = 1.0
        for r in sp.runs:
            r.font.size = Pt(2)
        return t

    # ---------- khối mã
    def code(self, text, caption=None):
        t = self.doc.add_table(rows=1, cols=1)
        cell = t.cell(0, 0)
        tcPr = cell._tc.get_or_add_tcPr()
        _shade(tcPr, "F4F6F8")
        bd = OxmlElement("w:tcBorders")
        for e in ("left", "top", "bottom", "right"):
            x = OxmlElement("w:" + e); x.set(qn("w:val"), "single")
            x.set(qn("w:sz"), "4"); x.set(qn("w:color"), "D5DCE4"); bd.append(x)
        tcPr.append(bd)
        first = True
        for ln in text.rstrip("\n").split("\n"):
            p = cell.paragraphs[0] if first else cell.add_paragraph()
            first = False
            r = p.add_run(ln if ln else " ")
            r.font.name = MONO_FONT; r.font.size = Pt(self.body_pt - 3.0)
            r.font.color.rgb = RGBColor(0x24, 0x2C, 0x34)
            pf = p.paragraph_format
            pf.space_after = Pt(0); pf.space_before = Pt(0); pf.line_spacing = 1.12
            pf.alignment = WD_ALIGN_PARAGRAPH.LEFT
        if caption:
            cp = self.doc.add_paragraph()
            add_inline(cp, caption, self.doc, base_size=self.body_pt - 2, italic=True, color=GREY)
            for r in cp.runs:
                r.font.name = HEAD_FONT
            cp.paragraph_format.space_after = Pt(8)
        else:
            sp = self.doc.add_paragraph(); sp.paragraph_format.space_after = Pt(6)
        return t

    def pagebreak(self):
        self.doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

    def spacer(self, pt=6):
        p = self.doc.add_paragraph()
        p.paragraph_format.space_after = Pt(pt)
        p.paragraph_format.line_spacing = 1.0
        return p

    def rule(self):
        p = self.doc.add_paragraph()
        p.paragraph_format.space_before = Pt(2); p.paragraph_format.space_after = Pt(8)
        _borders(p._p, ["bottom"], sz=6, color="C9D3DE")
        return p


# ----------------------------------------------------------------- mục lục
def toc(b, entries, page_map=None, title="MỤC LỤC"):
    """entries: [(level, num, text, anchor)] ; page_map: {anchor: '12'}"""
    doc = b.doc
    h = doc.add_paragraph()
    r = h.add_run(title)
    r.font.name = HEAD_FONT; r.font.size = Pt(16); r.bold = True; r.font.color.rgb = NAVY
    h.alignment = WD_ALIGN_PARAGRAPH.CENTER
    h.paragraph_format.space_after = Pt(14)
    right = doc.sections[0].page_width - doc.sections[0].left_margin - doc.sections[0].right_margin
    for lvl, num, text, anchor in entries:
        p = doc.add_paragraph()
        pf = p.paragraph_format
        pf.left_indent = Cm(0.0 + 0.7 * (lvl - 1))
        pf.space_after = Pt(2.5 if lvl == 1 else 1.5)
        pf.line_spacing = 1.12
        pf.alignment = WD_ALIGN_PARAGRAPH.LEFT
        pf.tab_stops.add_tab_stop(right - Cm(0.7 * (lvl - 1)),
                                  WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)
        label = (num + ". " if num else "")
        clean = re.sub(r"\[\[\d+(?:,\s*\d+)*\]\]", "", text)
        clean = re.sub(r"\*\*(.+?)\*\*", r"\1", clean)
        clean = re.sub(r"`([^`]+)`", r"\1", clean)
        _internal_link(p, label + clean, anchor, color="142C4A" if lvl == 1 else "333A42")
        for r in p.runs:
            r.font.name = HEAD_FONT
        for run_el in p._p.iter(qn("w:r")):
            for rPr in run_el.iter(qn("w:rPr")):
                pass
        _style_toc_runs(p, lvl)
        pg = (page_map or {}).get(anchor, "")
        tr = p.add_run("\t" + str(pg))
        tr.font.name = HEAD_FONT
        tr.font.size = Pt(11 if lvl == 1 else 10.5)
        tr.bold = (lvl == 1)
        tr.font.color.rgb = GREY


def _style_toc_runs(p, lvl):
    for r in p._p.iter(qn("w:r")):
        rPr = r.find(qn("w:rPr"))
        if rPr is None:
            rPr = OxmlElement("w:rPr"); r.insert(0, rPr)
        sz = OxmlElement("w:sz"); sz.set(qn("w:val"), str(int(2 * (11 if lvl == 1 else 10.5))))
        rPr.append(sz)
        f = OxmlElement("w:rFonts"); f.set(qn("w:ascii"), HEAD_FONT); f.set(qn("w:hAnsi"), HEAD_FONT)
        rPr.append(f)
        if lvl == 1:
            bl = OxmlElement("w:b"); rPr.append(bl)


# ----------------------------------------------------------------- trang bìa
def cover(b, meta):
    doc = b.doc
    def line(text, size, bold=False, color=NAVY, space=6, font=HEAD_FONT, caps=False,
             align="center", italic=False, spacing=None):
        p = doc.add_paragraph()
        p.alignment = {"center": WD_ALIGN_PARAGRAPH.CENTER,
                       "left": WD_ALIGN_PARAGRAPH.LEFT}[align]
        r = p.add_run(text.upper() if caps else text)
        r.font.name = font; r.font.size = Pt(size); r.bold = bold
        r.font.color.rgb = color; r.italic = italic
        if spacing:
            sp = OxmlElement("w:spacing"); sp.set(qn("w:val"), str(spacing))
            r._r.get_or_add_rPr().append(sp)
        p.paragraph_format.space_after = Pt(space)
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.line_spacing = 1.12
        return p

    b.spacer(2)
    line(meta["org"], 11.5, True, GREY, 2, caps=True, spacing=30)
    line(meta["dept"], 10.5, False, GREY, 16)
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("━" * 14); r.font.color.rgb = RGBColor(0xC2, 0x41, 0x1C); r.font.size = Pt(9)
    p.paragraph_format.space_after = Pt(40)

    line(meta["kicker"], 11, False, ACCENT, 10, caps=True, spacing=40)
    line(meta["title"], 30, True, NAVY, 6)
    line(meta["subtitle"], 13.5, False, BLUE, 10, italic=True)
    line(meta["tagline"], 11.5, False, GREY, 34)

    if meta.get("logo") and os.path.exists(meta["logo"]):
        pp = doc.add_paragraph(); pp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        pp.add_run().add_picture(meta["logo"], width=Cm(9))
        pp.paragraph_format.space_after = Pt(28)

    t = doc.add_table(rows=len(meta["fields"]), cols=2)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    total = doc.sections[0].page_width - doc.sections[0].left_margin - doc.sections[0].right_margin
    for i, (k, v) in enumerate(meta["fields"]):
        for j, txt in enumerate((k, v)):
            c = t.cell(i, j)
            c.width = Emu(int(total * (0.33 if j == 0 else 0.67)))
            pp = c.paragraphs[0]
            rr = pp.add_run(txt)
            rr.font.name = HEAD_FONT; rr.font.size = Pt(10.5)
            rr.bold = (j == 0); rr.font.color.rgb = GREY if j == 0 else NAVY
            pp.paragraph_format.space_after = Pt(3)
            pp.paragraph_format.line_spacing = 1.2
    b.spacer(40)
    line(meta["place_date"], 10.5, False, GREY, 4, italic=True)
    line(meta.get("version", ""), 9.5, False, GREY, 0, italic=True)
    b.pagebreak()


# ----------------------------------------------------------------- khổ giấy
def new_section(doc, landscape=False):
    """Mở một section mới; landscape=True để xoay ngang cho hình rộng."""
    from docx.enum.section import WD_ORIENT
    sec = doc.add_section(WD_SECTION.NEW_PAGE)
    if landscape:
        sec.orientation = WD_ORIENT.LANDSCAPE
        sec.page_width, sec.page_height = Cm(29.7), Cm(21.0)
        sec.top_margin = Cm(1.8); sec.bottom_margin = Cm(1.8)
        sec.left_margin = Cm(2.0); sec.right_margin = Cm(2.0)
    else:
        sec.orientation = WD_ORIENT.PORTRAIT
        sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
        sec.top_margin = Cm(2.2); sec.bottom_margin = Cm(2.2)
        sec.left_margin = Cm(2.6); sec.right_margin = Cm(2.0)
    sec.header_distance = Cm(1.2); sec.footer_distance = Cm(1.2)
    sec.different_first_page_header_footer = False
    return sec


# ----------------------------------------------------------------- trang phần
def part_divider(b, roman, title, blurb=""):
    doc = b.doc
    b.pagebreak()
    b.spacer(120)
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("PHẦN " + roman)
    r.font.name = HEAD_FONT; r.font.size = Pt(13); r.bold = True
    r.font.color.rgb = ACCENT
    sp = OxmlElement("w:spacing"); sp.set(qn("w:val"), "80")
    r._r.get_or_add_rPr().append(sp)
    p.paragraph_format.space_after = Pt(10)

    q = doc.add_paragraph(); q.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r2 = q.add_run(title.upper())
    r2.font.name = HEAD_FONT; r2.font.size = Pt(23); r2.bold = True
    r2.font.color.rgb = NAVY
    q.paragraph_format.space_after = Pt(14)

    u = doc.add_paragraph(); u.alignment = WD_ALIGN_PARAGRAPH.CENTER
    ru = u.add_run("━" * 12)
    ru.font.color.rgb = RGBColor(0xC9, 0xD3, 0xDE); ru.font.size = Pt(9)
    u.paragraph_format.space_after = Pt(16)

    if blurb:
        z = doc.add_paragraph(); z.alignment = WD_ALIGN_PARAGRAPH.CENTER
        z.paragraph_format.left_indent = Cm(3.0); z.paragraph_format.right_indent = Cm(3.0)
        add_inline(z, blurb, doc, base_size=b.body_pt - 0.5, italic=True, color=GREY)
        for rr in z.runs:
            rr.font.name = HEAD_FONT
        z.paragraph_format.line_spacing = 1.4
    b.pagebreak()


# ----------------------------------------------------------------- danh mục hình, bảng
def muc_luc_phu(b, items, tieu_de, tien_to, page_map=None):
    """Danh mục hình hoặc bảng: items = [(số, chú thích, anchor)]"""
    doc = b.doc
    h = doc.add_paragraph()
    r = h.add_run(tieu_de)
    r.font.name = HEAD_FONT; r.font.size = Pt(14); r.bold = True; r.font.color.rgb = NAVY
    h.alignment = WD_ALIGN_PARAGRAPH.CENTER
    h.paragraph_format.space_after = Pt(12)
    right = doc.sections[0].page_width - doc.sections[0].left_margin - doc.sections[0].right_margin
    for num, cap, anchor in items:
        p = doc.add_paragraph()
        pf = p.paragraph_format
        pf.left_indent = Cm(1.9); pf.first_line_indent = Cm(-1.9)
        pf.space_after = Pt(2); pf.line_spacing = 1.12
        pf.alignment = WD_ALIGN_PARAGRAPH.LEFT
        pf.tab_stops.add_tab_stop(right, WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)
        clean = re.sub(r"\[\[\d+(?:,\s*\d+)*\]\]", "", cap)
        clean = re.sub(r"\*\*(.+?)\*\*", r"\1", clean)
        clean = re.sub(r"`([^`]+)`", r"\1", clean)
        clean = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", clean)
        clean = re.sub(r"\s+", " ", clean).strip()
        if len(clean) > 120:
            clean = clean[:117].rstrip() + "…"
        _internal_link(p, "%s %d. %s" % (tien_to, num, clean), anchor, color="333A42")
        for rr in p.runs:
            rr.font.name = HEAD_FONT
        for run_el in p._p.iter(qn("w:r")):
            rPr = run_el.find(qn("w:rPr"))
            if rPr is None:
                rPr = OxmlElement("w:rPr"); run_el.insert(0, rPr)
            sz = OxmlElement("w:sz"); sz.set(qn("w:val"), "20"); rPr.append(sz)
        pg = (page_map or {}).get(anchor, "")
        tr = p.add_run("\t" + str(pg))
        tr.font.name = HEAD_FONT; tr.font.size = Pt(10); tr.font.color.rgb = GREY
