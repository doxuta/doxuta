# ExamLap — Đề xuất dự án khởi nghiệp: cho thuê laptop đi thi

Bản proposal cho môn Khởi nghiệp, Đại học FPT Đà Nẵng. Toàn bộ tài liệu, sơ đồ, nguyên mẫu giao diện
và mô hình tài chính đều được sinh ra từ mã nguồn trong thư mục này.

## Bản nộp

| File | Nội dung |
|---|---|
| `dist/Proposal-ExamLap.docx` | Bản Word, có mục lục đánh số trang thật |
| `dist/Proposal-ExamLap.pdf` | Bản PDF xuất từ chính file Word đó |

## Cấu trúc thư mục

| Thư mục | Nội dung |
|---|---|
| `content/` | Nội dung tài liệu. `proposal.md` là file gốc, các chương nằm trong `sections/` |
| `content/facts.md` | Hồ sơ dữ kiện chuẩn — mọi con số trong bài phải khớp file này |
| `content/styleguide.md` | Quy tắc viết và cú pháp soạn thảo |
| `research/` | Toàn bộ ghi chép nghiên cứu nền, kèm đường dẫn nguồn |
| `src/` | Bộ dựng tài liệu: `mdx.py` (DOCX), `render.py` (điều phối), `refs.py` (trích dẫn), `finmodel.py` (mô hình tài chính), `build_diagrams.py` (sơ đồ) |
| `src/diagrams/` | Mã nguồn Mermaid của 12 sơ đồ |
| `prototype/` | Nguyên mẫu giao diện bằng HTML dùng để chụp ảnh minh hoạ, và bộ sinh biểu đồ |
| `assets/` | Ảnh đã kết xuất: sơ đồ, biểu đồ, ảnh giao diện |

## Dựng lại tài liệu

```bash
pip install python-docx pillow playwright
npm i -g @mermaid-js/mermaid-cli
apt-get install -y libreoffice-writer poppler-utils

python3 src/build_diagrams.py                 # sơ đồ Mermaid -> PNG
python3 prototype/gen.py && python3 prototype/charts.py
python3 src/finmodel.py                       # xem mô hình tài chính
python3 src/collect_sources.py                # gom danh mục nguồn
cd src && python3 render.py ../content/proposal.md Proposal-ExamLap
```

`render.py` chạy hai lượt: lượt đầu đo số trang thật của từng đề mục trong PDF, lượt sau ghi số trang đó
vào mục lục rồi xuất bản cuối.

## Lưu ý về dữ liệu

Nghiên cứu nền được thực hiện trong môi trường **chỉ truy cập được công cụ tìm kiếm**, không mở trực tiếp
được từng trang web. Mọi số liệu trong tài liệu đều mang một trong ba nhãn: *[Đã xác minh]*,
*[Cần kiểm chứng]*, *[Ước lượng của nhóm]*. Phụ lục E liệt kê những gì nhóm phải tự đi kiểm chứng trước
khi dùng bản này để ra quyết định tài chính.
