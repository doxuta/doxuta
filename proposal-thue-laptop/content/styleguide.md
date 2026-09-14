# QUY TẮC VIẾT — bắt buộc đọc trước khi soạn bất kỳ phần nào

## Giọng văn
- Viết bằng **tiếng Việt**, văn xuôi mạch lạc, câu vừa phải, không sáo rỗng.
- Không dùng lối viết quảng cáo. Không dùng các cụm rỗng như "giải pháp toàn diện", "đột phá",
  "tối ưu hoá trải nghiệm", "cách mạng hoá". Nói thẳng dịch vụ làm gì và không làm gì.
- Không dùng dấu — (em dash) quá ba lần trong một trang. Ưu tiên dấu phẩy và dấu chấm.
- Khi nêu một con số, luôn cho biết nó **từ đâu ra**: nguồn ngoài (trích dẫn) hay giả định của nhóm (nhãn).
- Được phép nêu điểm yếu của dự án. Một bản proposal thừa nhận rủi ro đúng chỗ thì thuyết phục hơn.
- Không xưng "chúng em". Xưng **"nhóm"** hoặc **"chúng tôi"**, nhất quán trong cả bài.

## Cú pháp soạn thảo (đây KHÔNG phải Markdown chuẩn — chỉ dùng đúng những cú pháp dưới đây)
```
## Tiêu đề mục cấp 2          → viết ## (hệ thống tự đánh số 1.1, 1.2…)
### Tiêu đề mục cấp 3         → viết ###
Đoạn văn bình thường, có thể **in đậm**, *in nghiêng*, `mã lệnh`, [chữ hiển thị](https://url).

- gạch đầu dòng
  - gạch đầu dòng lồng (thụt 2 khoảng trắng)
1. danh sách đánh số

| Cột A | Cột B |
|---|---|
| dữ liệu | dữ liệu |
{caption: Chú thích bảng, viết như một câu hoàn chỉnh}
{widths: 3,2}
{right: 1}
{note: Ghi chú nhỏ dưới bảng nếu cần}

![Chú thích hình viết như một câu](assets/diagrams/ten-file.png){w=16}{src: Nguồn: nhóm tác giả.}

:::note Tiêu đề khối
Dòng nội dung thứ nhất.
Dòng nội dung thứ hai.
:::
(bốn loại khối: note = ghi chú, warn = lưu ý, ok = kết luận, risk = rủi ro)

```sql
SELECT ...
```
{caption: Chú thích khối mã}

<<<pagebreak>>>     → sang trang mới
<<<landscape>>>     → chuyển sang trang NGANG (dùng cho hình rộng)
<<<portrait>>>      → quay lại trang DỌC (phải luôn đóng lại sau khi dùng landscape)
```

## Trích dẫn nguồn — quy tắc quan trọng nhất
Viết `[[ref:https://url-that]]` ngay sau mệnh đề cần dẫn nguồn. Hệ thống sẽ tự đánh số thành `[12]`
và tự dựng danh mục tài liệu tham khảo ở cuối bài. Ví dụ:

> Học phí giai đoạn chuyên ngành tại campus Đà Nẵng là 22.120.000đ một học kỳ [[ref:https://baodanang.vn/hoc-phi-truong-dai-hoc-fpt-2025-2026-tai-cac-co-so-tren-ca-nuoc-3151966.html]].

- Chỉ dùng **URL có thật, lấy nguyên văn từ các file trong thư mục `research/`**. Tuyệt đối không bịa URL.
- Muốn đặt tên hiển thị riêng: `[[ref:https://url|Tên nguồn]]`.
- Mỗi tiểu mục nên có **ít nhất 2–4 trích dẫn** ở những chỗ nêu số liệu hoặc quy định.
- Với văn bản pháp luật, dẫn tên đầy đủ trong câu (ví dụ *Điều 175 Bộ luật Hình sự 2015*) rồi thêm `[[ref:...]]`.

## Chỉ dấu bảng tài chính
Khi cần chèn một bảng tài chính, viết đúng một dòng chỉ dấu, không viết lại bảng:
`{{T-CAPEX}}` `{{T-OPEX}}` `{{T-GIA}}` `{{T-PNL}}` `{{T-HOAVON}}` `{{T-KICHBAN}}` `{{T-NAM2}}`
Hệ thống sẽ thay bằng bảng sinh ra từ mô hình tài chính.

## Định dạng số và đơn vị
- Tiền: `93.250.000đ` (dấu chấm phân cách nghìn, chữ `đ` liền sau, không viết "VNĐ" trong thân bài).
- Số thập phân dùng dấu phẩy: `17,7%`.
- Giờ: `07:30`. Ngày: `24/09/2026`.
- Viết "Đại học FPT" (không viết "ĐH FPT" trong thân bài, trừ trong bảng cho gọn).

## Điều cấm
- Không bịa số liệu, không bịa URL, không bịa tên công ty hay tên người thật.
- Không khẳng định điều mà nghiên cứu ghi là chưa kiểm chứng được. Dùng nhãn ở mục 0 của `facts.md`.
- Không viết lại các bảng tài chính bằng tay.
- Không tự đổi giá, đổi số máy, đổi tên thương hiệu so với `facts.md`.
- Không mở đầu phần viết bằng câu tóm tắt kiểu "Trong phần này, chúng ta sẽ...". Vào thẳng nội dung.
