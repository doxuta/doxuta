# 07 — THANH TOÁN, ĐẶT CỌC VÀ HOÀN CỌC TẠI VIỆT NAM
## Hồ sơ nghiên cứu cho ExamLap (cho thuê laptop đi thi — ĐH FPT Đà Nẵng)

> **Quy mô tham chiếu:** 10 máy · ~400 lượt thuê/năm · doanh thu năm đầu ~82.000.000 đ
> **Ngày lập:** 14/09/2026
> **File:** `/home/user/doxuta/proposal-thue-laptop/research/07-thanh-toan-vn.md`

---

# ⛔ CẢNH BÁO BẮT BUỘC ĐỌC TRƯỚC — TÌNH TRẠNG NGUỒN CỦA TÀI LIỆU NÀY

**Tài liệu này được viết TRONG ĐIỀU KIỆN KHÔNG TRA CỨU ĐƯỢC WEB.**

| Hạng mục | Tình trạng thực tế trong phiên làm việc |
|---|---|
| `WebFetch` / `curl` | 🔴 **BỊ CHẶN HOÀN TOÀN** (`EGRESS_BLOCKED`). Kiểm chứng thực tế: `curl https://sepay.vn/bang-gia` → `curl: (56) CONNECT tunnel failed, response 403`; `curl https://www.google.com` → cùng lỗi 403. |
| `WebSearch` | 🔴 **ĐÃ HẾT HẠN MỨC TRƯỚC KHI TÁC VỤ NÀY BẮT ĐẦU** — ngân sách phiên 200/200 lượt đã bị các tác vụ nghiên cứu trước đó (file 01–16 trong cùng thư mục) dùng hết. Tác vụ này thực hiện **0 (KHÔNG) lượt tìm kiếm thành công**. |
| Nguồn URL kiểm chứng được | 🟡 Chỉ một số ít URL **kế thừa** từ các file nghiên cứu anh em trong cùng workflow (những URL đó *đã* do WebSearch trả về ở phiên trước). |

### Hệ quả — đọc kỹ:

1. **KHÔNG có một con số giá nào trong tài liệu này được xác minh.** Toàn bộ bảng giá SePay / Casso / PayOS / VNPay / MoMo / ZaloPay / OnePay / Payoo / Baokim đều ở trạng thái `[CHƯA CÓ]`. **Tuyệt đối không copy số vào bản proposal tài chính.**
2. **Không có URL nào bị bịa.** Nơi nào không có URL thật, tài liệu ghi tên nguồn ở dạng chữ thường và gắn nhãn *"phải tự tra"*, **không** tạo link giả.
3. Phần có giá trị nhất và đáng tin nhất của tài liệu này là: **(a) phân tích pháp lý mục 5 và mục 4**, **(b) đặc tả kỹ thuật VietQR mục 1**, **(c) kế hoạch kiểm chứng mục 10**. Đây là phần dựa trên **văn bản luật và tiêu chuẩn kỹ thuật** — loại kiến thức ổn định, không phải giá cả biến động.

### Hệ thống nhãn độ tin cậy dùng xuyên suốt

| Nhãn | Ý nghĩa | Được phép dùng trong proposal? |
|---|---|---|
| `[XM]` | **Đã xác minh** — có URL thật do WebSearch trả về (kế thừa từ file anh em) | ✅ Có, kèm trích dẫn |
| `[KT-C]` | Kiến thức nền **độ tin cậy CAO** — điều luật cụ thể, nguyên lý kỹ thuật chuẩn hoá, có thể tự kiểm chứng offline | ⚠️ Dùng được nhưng **phải đối chiếu văn bản gốc** trước khi nộp |
| `[KT-TB]` | Kiến thức nền **độ tin cậy TRUNG BÌNH** — nhớ được nội dung nhưng không chắc số hiệu/ngày tháng | ❌ Không dùng trước khi tra |
| `[KT-T]` | Kiến thức nền **độ tin cậy THẤP** | ❌ Không dùng |
| `[CHƯA CÓ]` | **Không có dữ liệu.** Phải tra mới có | ❌ Không dùng |
| `[SL]` | **Suy luận** của người viết từ các dữ kiện trên, không phải sự kiện | ⚠️ Ghi rõ là suy luận |

---

# MỤC LỤC

1. [VietQR & chuyển khoản nhanh NAPAS 24/7 — đặc tả kỹ thuật](#1)
2. [Dịch vụ đối soát biến động số dư (SePay, Casso, PayOS, Bizfly, WeOne)](#2)
3. [Cổng thanh toán (VNPay, MoMo, ZaloPay, OnePay, Payoo, Baokim)](#3)
4. [GIỮ CỌC: Việt Nam có pre-authorization hold không?](#4)
5. [⭐ PHÁP LÝ: giữ tiền của khách có phải là trung gian thanh toán không? (CÂU HỎI QUAN TRỌNG NHẤT)](#5)
6. [Hoá đơn điện tử cho hộ kinh doanh](#6)
7. [Mua trước trả sau (Fundiin, Kredivo, Home PayLater)](#7)
8. [Khuyến nghị cụ thể cho nhóm sinh viên](#8)
9. [Rủi ro và điểm chết](#9)
10. [Kế hoạch kiểm chứng — truy vấn tìm kiếm chính xác cần chạy](#10)
11. [Danh sách điều chưa biết](#11)

---

<a name="1"></a>
# 1. VietQR VÀ CHUYỂN KHOẢN NHANH NAPAS 24/7

## 1.1. Bức tranh tổng thể — ai là ai

| Thành phần | Vai trò | Độ tin cậy |
|---|---|---|
| **NAPAS** (CTCP Thanh toán Quốc gia Việt Nam) | Đơn vị **chuyển mạch tài chính và bù trừ điện tử** duy nhất của VN. Vận hành hạ tầng **chuyển khoản nhanh 24/7** giữa các ngân hàng và sở hữu thương hiệu **VietQR** | `[KT-C]` |
| **VietQR** | **Thương hiệu + bộ quy tắc trình bày** mã QR chuyển khoản do NAPAS công bố, đặt trên nền tiêu chuẩn kỹ thuật QR của NHNN | `[KT-C]` |
| **Tiêu chuẩn kỹ thuật nền** | **TCCS 03:2018/NHNNVN** — "Tiêu chuẩn cơ sở về đặc tả kỹ thuật QR Code hiển thị từ phía đơn vị chấp nhận thanh toán tại Việt Nam", do Ngân hàng Nhà nước ban hành **2018**. Bản chất là bản địa hoá của **EMVCo QR Code Specification for Payment Systems — Merchant-Presented Mode (EMV MPM)** | `[KT-TB]` số hiệu tiêu chuẩn; `[KT-C]` việc nó dựa trên EMV MPM |
| **VietQR.io** | Dịch vụ **của bên thứ ba** (không phải NAPAS) cung cấp API sinh ảnh QR nhanh. Tiện nhưng **không phải chuẩn chính thức** | `[KT-TB]` |

> ⚠️ **Phân biệt quan trọng:** "VietQR" ≠ "cổng thanh toán". VietQR **chỉ là cách mã hoá thông tin tài khoản thụ hưởng vào một ảnh QR**. Bản thân nó **không** báo cho bạn biết tiền đã về hay chưa. Việc "biết tiền đã về" là bài toán hoàn toàn khác → xem **Mục 2**.

## 1.2. Mã QR TĨNH vs MÃ QR ĐỘNG

| Tiêu chí | QR **tĩnh** | QR **động** |
|---|---|---|
| Tag `01` (Point of Initiation Method) | `11` | `12` | 
| Số tiền nhúng sẵn (tag `54`) | Không | **Có** |
| Nội dung CK nhúng sẵn (tag `62` → `08`) | Không | **Có** |
| Dùng lại được nhiều lần | Có | Về lý thuyết có, nhưng **phải coi là dùng 1 lần cho 1 đơn** |
| Đối soát tự động | ❌ Rất khó — khách gõ tay nội dung, sai chính tả là hỏng | ✅ Dễ — nội dung là mã đơn hàng do hệ thống sinh |

**→ ExamLap BẮT BUỘC dùng QR ĐỘNG.** Lý do: mỗi lượt thuê cần một **mã tham chiếu duy nhất** (ví dụ `EXL7K2M9`) nằm trong nội dung chuyển khoản, để hệ thống tự khớp tiền vào đúng đơn mà không cần con người nhìn bằng mắt. `[SL]`

## 1.3. Cấu trúc chuỗi VietQR — đặc tả TLV

Chuỗi QR là chuỗi **TLV (Tag–Length–Value)** nối liền nhau, mỗi phần tử: `[Tag 2 ký tự][Length 2 ký tự][Value]`. `[KT-C]`

### Các tag cấp 1

| Tag | Tên | Giá trị cho ExamLap | Bắt buộc |
|---|---|---|---|
| `00` | Payload Format Indicator | `01` | ✅ |
| `01` | Point of Initiation Method | **`12`** (động) | ✅ (cho QR động) |
| `38` | Merchant Account Information — VietQR | *xem bảng con dưới* | ✅ |
| `52` | Merchant Category Code (MCC) | `0000` nếu không phân loại | Tuỳ |
| `53` | Transaction Currency | **`704`** (VND, theo ISO 4217) | ✅ |
| `54` | **Transaction Amount** | VD `150000` — **không dấu phân cách, không số thập phân với VND** | ✅ cho QR động |
| `58` | Country Code | **`VN`** | ✅ |
| `59` | Merchant Name | Tên tài khoản thụ hưởng | Tuỳ |
| `60` | Merchant City | VD `DA NANG` | Tuỳ |
| `62` | Additional Data Field Template | *xem bảng con dưới* | ✅ cho QR động |
| `63` | **CRC** | 4 ký tự hex | ✅ (luôn ở CUỐI) |

### Tag `38` — Merchant Account Information (lồng nhau)

| Sub-tag | Tên | Giá trị |
|---|---|---|
| `00` | GUID | **`A000000727`** — định danh hệ thống VietQR của NAPAS |
| `01` | Beneficiary Organization | Chứa 2 sub-tag con: |
| `01`→`00` | **Acquirer ID / BIN ngân hàng** | 6 chữ số, VD `970436` |
| `01`→`01` | **Merchant/Consumer ID** | **Số tài khoản ngân hàng** người nhận |
| `02` | Service Code | **`QRIBFTTA`** = chuyển khoản đến **tài khoản**<br>**`QRIBFTTC`** = chuyển khoản đến **thẻ** |

`[KT-C]` về cấu trúc lồng; `[KT-TB]` về chuỗi GUID `A000000727` — **phải xác minh**.

### Tag `62` — Additional Data Field Template

| Sub-tag | Tên | Dùng cho gì |
|---|---|---|
| `01` | Bill Number | Số hoá đơn |
| `05` | Reference Label | Mã tham chiếu |
| `08` | **Purpose of Transaction** | ⭐ **ĐÂY LÀ "NỘI DUNG CHUYỂN KHOẢN"** — chỗ nhét mã đơn `EXL7K2M9` |

`[KT-C]` — sub-tag `08` là trường nội dung. Đây là trường ExamLap quan tâm nhất.

### Tag `63` — CRC

- Thuật toán: **CRC-16/CCITT-FALSE** `[KT-C]`
- Polynomial `0x1021`, giá trị khởi tạo `0xFFFF`, không reflect input/output, không XOR out `[KT-C]`
- **Cách tính:** nối chuỗi bao gồm cả `6304` (tag 63 + length 04) rồi tính CRC trên **toàn bộ chuỗi đó**, kết quả in ra **4 ký tự hex viết HOA** `[KT-C]`

### ⚠️ Giới hạn ký tự của nội dung chuyển khoản

| Ràng buộc | Ghi chú |
|---|---|
| **Không dấu tiếng Việt** | Nhiều ngân hàng tự bỏ dấu hoặc từ chối. **Luôn dùng ASCII không dấu** `[KT-C]` |
| Độ dài | Mỗi ngân hàng một khác; nhiều nơi cắt còn ~**25–50 ký tự**. `[KT-TB]` — **phải tự test** |
| Ký tự đặc biệt | Tránh hoàn toàn `- _ . , / \ # &`. Chỉ dùng **[A-Z0-9]** | 

> 💡 **Khuyến nghị thiết kế mã đơn ExamLap:** `EXL` + 6 ký tự Base32 (bỏ các ký tự dễ nhầm `I O 0 1`) → ví dụ `EXL7K2M9`. Tổng 9 ký tự, an toàn với mọi ngân hàng, chống gõ nhầm. `[SL]`

## 1.4. Mã BIN ngân hàng (Acquirer ID) — cần xác minh lại

| Ngân hàng | BIN (6 số) | Độ tin cậy |
|---|---|---|
| Vietcombank | `970436` | `[KT-TB]` |
| VietinBank | `970415` | `[KT-TB]` |
| BIDV | `970418` | `[KT-TB]` |
| Agribank | `970405` | `[KT-TB]` |
| Techcombank | `970407` | `[KT-TB]` |
| MB Bank | `970422` | `[KT-TB]` |
| ACB | `970416` | `[KT-TB]` |
| VPBank | `970432` | `[KT-TB]` |
| TPBank | `970423` | `[KT-TB]` |
| Sacombank | `970403` | `[KT-TB]` |

> 🔴 **Toàn bộ bảng BIN trên ở mức `[KT-TB]`.** Sai 1 chữ số = tiền vào tài khoản người lạ. **BẮT BUỘC** đối chiếu danh sách BIN chính thức do NAPAS công bố **trước khi viết một dòng code nào**. Cách kiểm chứng rẻ nhất: quét thử QR bằng app ngân hàng, xem tên người thụ hưởng hiện ra có đúng không, **trước khi** chuyển tiền thật.

## 1.5. Sinh QR động — hai con đường

### Cách A — Tự sinh chuỗi TLV + render QR offline ✅ **KHUYẾN NGHỊ**

**Chi phí: 0 đồng. Không phụ thuộc bên thứ ba. Không rò rỉ dữ liệu. Chạy được offline.** `[SL]`

```python
# Sinh chuỗi VietQR động — thuần Python, không cần thư viện ngoài
# ⚠️ ĐÂY LÀ CODE THAM CHIẾU DỰA TRÊN [KT-C] VỀ TLV/EMV MPM.
#    PHẢI TEST BẰNG APP NGÂN HÀNG THẬT TRƯỚC KHI DÙNG.

def tlv(tag: str, value: str) -> str:
    """Đóng gói một phần tử TLV: tag(2) + length(2, zero-pad) + value"""
    return f"{tag}{len(value):02d}{value}"

def crc16_ccitt_false(data: str) -> str:
    """CRC-16/CCITT-FALSE: poly=0x1021, init=0xFFFF, no reflect, no xorout"""
    crc = 0xFFFF
    for ch in data.encode("ascii"):
        crc ^= ch << 8
        for _ in range(8):
            crc = ((crc << 1) ^ 0x1021) & 0xFFFF if (crc & 0x8000) else (crc << 1) & 0xFFFF
    return f"{crc:04X}"

def build_vietqr(bank_bin: str, account_no: str, amount: int,
                 content: str, merchant_name: str = "", city: str = "") -> str:
    # Tag 38 — Merchant Account Information
    beneficiary = tlv("00", bank_bin) + tlv("01", account_no)
    tag38 = tlv("00", "A000000727") + tlv("01", beneficiary) + tlv("02", "QRIBFTTA")

    # Tag 62 — Additional Data: sub-tag 08 = nội dung chuyển khoản
    tag62 = tlv("08", content)

    payload = (
        tlv("00", "01")            # Payload Format Indicator
        + tlv("01", "12")          # 12 = QR ĐỘNG (11 = tĩnh)
        + tlv("38", tag38)
        + tlv("53", "704")         # VND
        + tlv("54", str(amount))   # số nguyên, không phân cách
        + tlv("58", "VN")
    )
    if merchant_name:
        payload += tlv("59", merchant_name[:25])
    if city:
        payload += tlv("60", city[:15])
    payload += tlv("62", tag62)

    payload += "6304"                       # tag 63 + length, TRƯỚC khi tính CRC
    return payload + crc16_ccitt_false(payload)


# --- Ví dụ dùng cho ExamLap ---
qr_string = build_vietqr(
    bank_bin="970436",          # ⚠️ XÁC MINH LẠI BIN
    account_no="1234567890",
    amount=150000,              # 150.000 đ
    content="EXL7K2M9",         # mã đơn — ASCII, không dấu, không ký tự đặc biệt
    merchant_name="EXAMLAP",
    city="DA NANG",
)
# Render thành ảnh: pip install qrcode[pil]
#   import qrcode; qrcode.make(qr_string).save("qr.png")
```

#### ✅ Đoạn code trên ĐÃ ĐƯỢC CHẠY THỬ VÀ KIỂM CHỨNG OFFLINE

Đây là **thứ duy nhất trong tài liệu này được kiểm chứng bằng thực nghiệm** (vì nó không cần mạng):

| Phép kiểm | Kết quả |
|---|---|
| **CRC-16/CCITT-FALSE với vector chuẩn** `"123456789"` | Trả về **`29B1`** — **khớp đúng** giá trị chuẩn quốc tế `0x29B1` ✅ |
| Sinh chuỗi QR mẫu | `00020101021238540010A00000072701240006970436011012345678900208QRIBFTTA530370454061500005802VN5907EXAMLAP6007DA NANG62120808EXL7K2M96304823E` (139 ký tự) |
| Parse ngược chuỗi theo TLV | Tách sạch thành các tag `00`,`01`,`38`,`53`,`54`,`58`,`59`,`60`,`62`,`63` ✅ |
| Kiểm tra CRC round-trip | `823E` == `823E` ✅ |
| Tag `54` (số tiền) | `150000` ✅ |
| Tag `62`→`08` (nội dung) | `EXL7K2M9` ✅ |

> ⚠️ **Kiểm chứng này chỉ chứng minh code ĐÚNG VỀ MẶT THUẬT TOÁN** (TLV hợp lệ, CRC chuẩn). Nó **KHÔNG** chứng minh mã BIN `970436` đúng, cũng **KHÔNG** chứng minh app ngân hàng Việt Nam sẽ chấp nhận chuỗi này. **Vẫn phải test bằng app ngân hàng thật** theo 4 bước ở dưới.

**Kiểm thử bắt buộc trước khi chạy thật** `[SL]`:
1. Sinh QR với số tiền **2.000 đ**
2. Quét bằng **ít nhất 4 app ngân hàng khác nhau** (VCB, MB, Techcombank, MoMo)
3. Xác nhận **cả 3 thứ** tự động điền đúng: tên người nhận · số tiền · nội dung
4. Chuyển thật 2.000 đ, kiểm tra nội dung ở sao kê có giữ nguyên `EXL7K2M9` không (một số ngân hàng **thêm tiền tố** kiểu `CT DEN:xxx EXL7K2M9` → parser phải dùng **regex tìm kiếm trong chuỗi**, không so sánh bằng `==`)

### Cách B — Gọi API ảnh của VietQR.io

Dịch vụ bên thứ ba, trả về ảnh PNG qua một URL có tham số `amount` và `addInfo`.
- **Chi phí:** `[CHƯA CÓ]` — có tầng miễn phí nhưng hạn mức và điều kiện **chưa xác minh**
- **Nhược điểm:** phụ thuộc mạng, phụ thuộc bên thứ ba, lộ số tài khoản qua URL, có thể bị rate-limit đúng lúc cao điểm mùa thi `[SL]`
- **Kết luận:** ❌ **Không khuyến nghị** khi Cách A tốn 0 đồng và ~40 dòng code.

## 1.6. Chuyển khoản nhanh NAPAS 24/7 — điều ảnh hưởng đến vận hành

| Yếu tố | Nội dung | Độ tin cậy |
|---|---|---|
| Thời gian ghi có | Gần **tức thì** (vài giây), hoạt động **24/7 kể cả lễ Tết** | `[KT-C]` |
| Phí với người chuyển | **Hầu hết ngân hàng bán lẻ đã miễn phí** chuyển khoản 24/7 cho khách cá nhân | `[KT-C]` xu hướng; `[CHƯA CÓ]` cho từng ngân hàng cụ thể |
| **Xác thực sinh trắc học** | Theo **Quyết định 2345/QĐ-NHNN**, giao dịch chuyển tiền **trên 10 triệu đ/lần** hoặc **tổng trên 20 triệu đ/ngày** phải xác thực bằng **khuôn mặt khớp với dữ liệu CCCD gắn chip**. Áp dụng từ **01/7/2024** | `[KT-TB]` số hiệu và ngưỡng — **phải xác minh** |
| Ảnh hưởng tới ExamLap | Giao dịch của ExamLap (thuê ~150–300k, cọc ~2–3 triệu) **đều dưới 10 triệu** → **không vướng** xác thực sinh trắc học | `[SL]` |

> ⚠️ **Rủi ro vận hành thật:** ngày cao điểm mùa thi, nếu nhiều sinh viên cùng chuyển khoản trong 5 phút, hệ thống ngân hàng **thỉnh thoảng vẫn trễ 1–3 phút**. Quy trình bàn giao máy **không được** chặn cứng ở bước "chờ tiền về" — cần nút **"xác nhận thủ công"** cho nhân sự trực. `[SL]`

---

<a name="2"></a>
# 2. DỊCH VỤ ĐỐI SOÁT BIẾN ĐỘNG SỐ DƯ

## 2.1. Bài toán thật sự là gì

Khi khách quét VietQR và chuyển tiền, **tiền vào thẳng tài khoản ngân hàng của bạn** — không đi qua ai cả. Nhưng **phần mềm của bạn không hề biết**. Đây gọi là bài toán **"biến động số dư"** (bank transaction notification / balance change webhook).

Ba cách giải, xếp theo chi phí: `[SL]`

| # | Cách | Chi phí | Độ trễ | Độ tin cậy | Phù hợp ExamLap? |
|---|---|---|---|---|---|
| **0** | **Người trực nhìn app ngân hàng rồi bấm xác nhận** | **0 đ** | ~10–60 giây | Cao (có mắt người) | ✅ **Rất phù hợp ở quy mô 400 lượt/năm** |
| **1** | Dịch vụ đối soát (SePay/Casso/PayOS…) đẩy **webhook** về hệ thống | `[CHƯA CÓ]` | vài giây–1 phút | Trung bình–cao | ⚠️ Cân nhắc ở năm 2 |
| **2** | Cổng thanh toán đầy đủ (VNPay/MoMo…) | % trên doanh thu | vài giây | Cao | ❌ Quá nặng, xem Mục 3 |

> ⭐ **Con số quyết định:** 400 lượt/năm ≈ **1,1 lượt/ngày** ≈ **~33 lượt/tháng**. Ngay cả mùa cao điểm thi cũng chỉ dồn vài chục lượt trong 1–2 tuần. **Ở mật độ này, tự động hoá đối soát gần như không tạo ra giá trị kinh tế** — một người trực nhìn thông báo app ngân hàng là đủ. `[SL]` Đây là kết luận quan trọng nhất của Mục 2.

## 2.2. Cơ chế kỹ thuật — 3 nhóm, khác nhau rất lớn về pháp lý và độ tin cậy

Đây là điều **bắt buộc phải hỏi nhà cung cấp**, vì nó quyết định dịch vụ có bị "chết" đột ngột không: `[KT-C]` về mặt phân loại kỹ thuật

| Nhóm | Cách hoạt động | Rủi ro |
|---|---|---|
| **A. Tích hợp chính thức với ngân hàng** | Nhà cung cấp có **hợp đồng đối tác** với ngân hàng; ngân hàng cấp **tài khoản chuyên thu / virtual account** và API chính thức | 🟢 Thấp. Ổn định. Thường **yêu cầu tài khoản doanh nghiệp** |
| **B. Đọc email/SMS thông báo biến động số dư** | Người dùng chuyển tiếp email báo có tiền từ ngân hàng sang hệ thống nhà cung cấp; nhà cung cấp **parse nội dung email** | 🟡 Trung bình. Vỡ khi ngân hàng đổi mẫu email. Trễ hơn. Phụ thuộc dịch vụ email |
| **C. Đăng nhập hộ vào Internet Banking (scraping)** | Người dùng **giao tên đăng nhập + mật khẩu** ngân hàng cho bên thứ ba để họ đăng nhập đọc sao kê | 🔴 **NGUY HIỂM CAO** |

> 🔴🔴 **CẢNH BÁO NGHIÊM TRỌNG VỀ NHÓM C:**
> **Giao thông tin đăng nhập Internet Banking cho bên thứ ba gần như chắc chắn VI PHẠM Điều khoản & Điều kiện sử dụng dịch vụ ngân hàng điện tử của mọi ngân hàng Việt Nam.** Hậu quả: (1) ngân hàng có quyền **khoá tài khoản**; (2) nếu mất tiền, ngân hàng có căn cứ **từ chối bồi thường** vì khách đã tự làm lộ thông tin bảo mật; (3) rủi ro hình sự nếu bên thứ ba lạm dụng. `[KT-C]` về nguyên tắc pháp lý chung; `[CHƯA CÓ]` về điều khoản cụ thể của từng ngân hàng.
>
> **→ Quy tắc cứng cho ExamLap: TUYỆT ĐỐI KHÔNG đưa mật khẩu ngân hàng cho bất kỳ dịch vụ nào.** Nếu một nhà cung cấp yêu cầu điều này → **loại ngay**, bất kể giá rẻ đến đâu.

## 2.3. Bảng so sánh nhà cung cấp — TRẠNG THÁI DỮ LIỆU

🔴 **Đây là bảng RỖNG có chủ đích. Tài liệu này KHÔNG có dữ liệu để điền, và KHÔNG được phép đoán.**

| Nhà cung cấp | Giá (đ/tháng) | Giới hạn số GD | Ngân hàng hỗ trợ | Cá nhân đăng ký được? | Hộ KD được? | Tài liệu API | Ký webhook |
|---|---|---|---|---|---|---|---|
| **SePay** | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` |
| **Casso** | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` |
| **PayOS** | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` |
| **Bizfly** | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` |
| **WeOne** | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` |

**Điều duy nhất tài liệu này dám khẳng định về nhóm dịch vụ trên:**
- Chúng **tồn tại** và phục vụ đúng bài toán "webhook biến động số dư" tại thị trường Việt Nam `[KT-TB]`
- Mặt bằng chung ngành có **tầng miễn phí hoặc giá rất thấp** (đơn vị chục–trăm nghìn đồng/tháng) cho khối lượng nhỏ `[KT-T]` — **con số cụ thể phải tra, không được trích dẫn từ đây**
- `PayOS` được nhắc tới trong các file nghiên cứu anh em nhưng **không kèm bảng giá** — xem `./02-nen-tang-cho-thue-quoc-te.md` và `./12-ux-tham-chieu.md`

## 2.4. ⭐ BẢNG CÂU HỎI CHUẨN — gửi cho từng nhà cung cấp

Đây là **sản phẩm dùng được ngay** của mục này. Copy nguyên văn, gửi qua form liên hệ/Zalo OA/email của từng bên, rồi tự điền vào bảng 2.3. `[SL]`

> **Kính gửi bộ phận kinh doanh,**
>
> Chúng tôi là nhóm sinh viên đang xây dựng dịch vụ cho thuê laptop quy mô nhỏ tại Đà Nẵng. Khối lượng dự kiến: **khoảng 400–800 giao dịch/năm (~35–70 giao dịch/tháng)**, giá trị mỗi giao dịch 150.000–3.000.000 đ. Xin được hỏi:
>
> **Về điều kiện đăng ký**
> 1. Chúng tôi có thể đăng ký với tư cách **cá nhân** (chỉ có CCCD, tài khoản ngân hàng cá nhân) không, hay **bắt buộc phải có Giấy chứng nhận đăng ký doanh nghiệp**?
> 2. **Hộ kinh doanh cá thể** (có Giấy chứng nhận ĐKKD hộ kinh doanh + Mã số thuế, không phải công ty) có đăng ký được không? Cần nộp những giấy tờ gì?
> 3. Có yêu cầu **tài khoản ngân hàng đứng tên tổ chức** không, hay dùng **tài khoản cá nhân** được?
>
> **Về giá**
> 4. Bảng giá đầy đủ các gói (**VNĐ/tháng** và **VNĐ/năm**)? Có **tầng miễn phí** không, giới hạn bao nhiêu giao dịch/tháng?
> 5. Có phí **khởi tạo / phí kích hoạt / phí tối thiểu hằng tháng** không?
> 6. Vượt hạn mức giao dịch thì tính phí thế nào (đ/giao dịch vượt)?
> 7. Có **ràng buộc hợp đồng tối thiểu** (6 tháng/12 tháng) không? Huỷ giữa chừng có hoàn tiền không?
>
> **Về kỹ thuật — quan trọng nhất**
> 8. Dịch vụ lấy dữ liệu biến động số dư bằng **cơ chế nào**: (a) tích hợp API chính thức có hợp đồng với ngân hàng, (b) đọc email/SMS thông báo, hay (c) đăng nhập hộ vào Internet Banking?
> 9. **Chúng tôi có phải cung cấp tên đăng nhập/mật khẩu Internet Banking không?** *(Nếu câu trả lời là CÓ → loại nhà cung cấp này)*
> 10. **Danh sách đầy đủ ngân hàng đang hỗ trợ?** Cụ thể có hỗ trợ: Vietcombank, MB Bank, Techcombank, ACB, BIDV?
> 11. **Độ trễ trung bình** từ lúc tiền vào tài khoản đến lúc webhook được gửi (giây)?
> 12. Webhook được **ký (sign)** bằng cơ chế nào — HMAC-SHA256 với secret key, chữ ký số, hay chỉ có API key trong header? **Cho xin tài liệu mô tả cách verify chữ ký.**
> 13. Cơ chế **retry** khi endpoint của chúng tôi lỗi: thử lại mấy lần, giãn cách bao lâu?
> 14. Webhook có đảm bảo **idempotency** không (mỗi giao dịch có ID duy nhất để chống xử lý trùng)?
> 15. Có **API truy vấn lịch sử giao dịch** để đối soát bù khi webhook thất lạc không?
> 16. Nội dung chuyển khoản trả về có bị **cắt ngắn** hoặc **thêm tiền tố** của ngân hàng không? Cho xin **ví dụ chuỗi thật**.
> 17. **Link tài liệu API công khai**?
> 18. Có **môi trường sandbox** để thử miễn phí không?
>
> **Về dữ liệu & pháp lý**
> 19. Dữ liệu giao dịch được lưu ở đâu, lưu bao lâu? Có hợp đồng xử lý dữ liệu cá nhân theo **Nghị định 13/2023/NĐ-CP** không?
> 20. Có cam kết SLA về thời gian hoạt động (uptime) không?

## 2.5. ⚠️ Nguyên tắc kỹ thuật khi nhận webhook (áp dụng cho MỌI nhà cung cấp)

Dù chọn bên nào, phía ExamLap **bắt buộc** làm đủ 5 việc sau. Đây là kiến thức kỹ thuật chuẩn, độc lập với nhà cung cấp. `[KT-C]`

| # | Việc | Vì sao | Cách làm |
|---|---|---|---|
| 1 | **Xác thực chữ ký** | Endpoint webhook là **URL công khai** — bất kỳ ai biết URL đều POST giả được "đã nhận 3 triệu" | Tính HMAC-SHA256 trên **raw body** với secret key, so sánh bằng hàm **so sánh hằng thời gian** (`hmac.compare_digest`), **không** dùng `==` |
| 2 | **Chống trùng (idempotency)** | Nhà cung cấp sẽ **retry** khi bạn trả lỗi hoặc timeout → cùng 1 giao dịch đến 2–3 lần | Bảng `payment_events` với **UNIQUE constraint** trên `(provider, provider_txn_id)`. Đến lần 2 → bỏ qua, vẫn trả `200` |
| 3 | **Đối chiếu SỐ TIỀN, không chỉ mã đơn** | Khách gõ đúng mã `EXL7K2M9` nhưng chuyển 15.000 đ thay vì 150.000 đ | So khớp **cả 3**: mã đơn ∧ số tiền ≥ số tiền phải trả ∧ đơn đang ở trạng thái `chờ thanh toán` |
| 4 | **Trả `200` NGAY, xử lý sau** | Xử lý chậm → nhà cung cấp timeout → retry bão | Ghi event vào DB → trả `200` → xử lý nghiệp vụ bằng job nền |
| 5 | **Job đối soát định kỳ** | Webhook **sẽ** thất lạc | Mỗi 15 phút gọi API lịch sử giao dịch, so với DB, vá chênh lệch. **Webhook là đường nhanh, đối soát định kỳ mới là nguồn sự thật** |

> 📎 Các file nghiên cứu anh em đã bàn sâu về idempotency cho API thanh toán, có nguồn kiểm chứng được: [Designing Idempotent Payment APIs](https://arpit.substack.com/p/designing-idempotent-payment-apis) `[XM]` và [Idempotency in Payment APIs](https://simplico.net/2026/04/04/idempotency-in-payment-apis-prevent-double-charges-with-stripe-omise-and-2c2p/) `[XM]`. Xem thêm `./09-kien-truc-phan-mem-rental.md` mục webhook (dòng ~761) đã có sẵn thiết kế bảng `payment_events`.

---

<a name="3"></a>
# 3. CỔNG THANH TOÁN

## 3.1. Bảng so sánh — TRẠNG THÁI DỮ LIỆU

🔴 **Không có số liệu xác minh. Bảng để trống có chủ đích.**

| Cổng | Phí GD (%) | Yêu cầu pháp nhân | Chu kỳ đối soát & về tiền | Refund qua API? | Thời gian hoàn tiền |
|---|---|---|---|---|---|
| **VNPay** | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[KT-TB]` có API hoàn tiền | `[CHƯA CÓ]` |
| **MoMo** | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[KT-TB]` có API hoàn tiền | `[CHƯA CÓ]` |
| **ZaloPay** | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[KT-TB]` có API hoàn tiền | `[CHƯA CÓ]` |
| **OnePay** | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` |
| **Payoo** | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` |
| **Baokim** | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` |

## 3.2. Những điều có thể khẳng định ở mức nguyên tắc

| # | Khẳng định | Độ tin cậy |
|---|---|---|
| 1 | **Cả 6 cổng trên đều là tổ chức cung ứng dịch vụ trung gian thanh toán có giấy phép của NHNN.** Đây chính là lý do họ được phép giữ và luân chuyển tiền của người khác — còn ExamLap thì không (Mục 5) | `[KT-C]` |
| 2 | **Mọi cổng thanh toán đều yêu cầu người bán có tư cách pháp lý và hợp đồng ký kết** — tối thiểu là Giấy chứng nhận ĐKKD (doanh nghiệp hoặc hộ kinh doanh) + Mã số thuế + tài khoản ngân hàng khớp tên. **Không cổng nào cho cá nhân trần đăng ký làm merchant** | `[KT-C]` |
| 3 | **Tiền KHÔNG về tài khoản ngay.** Cổng giữ tiền rồi chuyển về theo chu kỳ đối soát (mặt bằng ngành là **T+1 đến T+3 ngày làm việc**) | `[KT-C]` nguyên tắc; `[KT-T]` con số ngày cụ thể |
| 4 | **Hoàn tiền (refund) qua API là tính năng chuẩn** của VNPay/MoMo/ZaloPay | `[KT-TB]` |
| 5 | **Tốc độ tiền về tay khách khi hoàn phụ thuộc PHƯƠNG THỨC gốc**, không phụ thuộc cổng: hoàn về **ví điện tử** rất nhanh (phút–giờ); hoàn về **thẻ nội địa/tài khoản ngân hàng** vài ngày làm việc; hoàn về **thẻ quốc tế** lâu nhất (có thể **hàng tuần**, do phải qua chu kỳ của tổ chức thẻ) | `[KT-C]` nguyên tắc; `[CHƯA CÓ]` số ngày cụ thể |
| 6 | Nhiều cổng **thu phí hoặc không hoàn lại phí giao dịch gốc** khi merchant refund | `[KT-TB]` |

> 🔴 **Về con số % phí:** mặt bằng ngành thanh toán VN nằm ở **bậc độ lớn đơn vị phần trăm** — `[KT-T]`, **chỉ để hình dung quy mô khi lập kịch bản, TUYỆT ĐỐI KHÔNG đưa vào bảng tài chính của proposal.** Phải lấy báo giá thật.

## 3.3. ⭐ Phân tích: cổng thanh toán CÓ ĐÁNG KHÔNG với ExamLap?

Đây là phân tích **không cần dữ liệu ngoài** — chỉ cần số liệu nội bộ của dự án. `[SL]`

**Giả định:** doanh thu năm đầu 82.000.000 đ, toàn bộ chảy qua cổng.

| Mức phí giả định | Chi phí cổng/năm | % lợi nhuận bị ăn mất |
|---|---|---|
| 1,0% | 820.000 đ | — |
| 1,5% | 1.230.000 đ | — |
| 2,0% | 1.640.000 đ | — |
| 2,5% | 2.050.000 đ | — |
| 3,0% | 2.460.000 đ | — |

> ⚠️ Cột "% lợi nhuận bị ăn mất" để trống vì **phải lấy từ file `./11-unit-economics.md`** — không bịa biên lợi nhuận ở đây.

**Nhưng vấn đề lớn hơn tiền phí là DÒNG TIỀN CỌC:** `[SL]`

Nếu thu cọc 2.000.000 đ/lượt qua cổng thanh toán, với 400 lượt/năm:
- Cổng giữ tiền **T+1…T+3** rồi mới trả về → tiền cọc **kẹt** ở cổng
- Khi trả máy, phải **hoàn 2.000.000 đ** → mất thêm phí (nếu cổng không hoàn phí gốc), và khách **chờ vài ngày mới thấy tiền về**
- Mỗi vòng "thu cọc → hoàn cọc" qua cổng có thể tiêu tốn **2 lần phí** trên một khoản tiền mà bản chất **chỉ là vật bảo đảm, không phải doanh thu**

> 🔴 **KẾT LUẬN MỤC 3:** Với ExamLap, **cổng thanh toán là lựa chọn SAI cho khoản CỌC** — nó biến một khoản bảo đảm không sinh lời thành một khoản chịu phí hai lần và làm khách bực vì chờ hoàn tiền lâu. **Chuyển khoản trực tiếp qua VietQR (Mục 1) tốt hơn về mọi mặt: phí 0 đ, tiền về ngay, hoàn cọc bằng chuyển khoản ngược lại cũng 0 đ và tức thì.** `[SL]`
>
> Cổng thanh toán chỉ nên cân nhắc ở **giai đoạn 2**, khi (a) đã có pháp nhân, (b) quy mô đủ lớn để phí % rẻ hơn chi phí nhân công đối soát thủ công, (c) cần nhận thẻ quốc tế cho khách nước ngoài. Nhận định này **trùng khớp** với kết luận độc lập trong `./09-kien-truc-phan-mem-rental.md` (dòng 1446): *"Thanh toán: QR chuyển khoản (VietQR) cho MVP → VNPay/MoMo ở giai đoạn 2"* `[XM]` (nguồn nội bộ workflow).

## 3.4. Câu hỏi gửi cổng thanh toán (nếu vẫn muốn theo đuổi)

1. **Hộ kinh doanh cá thể** có ký hợp đồng merchant được không, hay bắt buộc **công ty (doanh nghiệp)**? Danh mục hồ sơ đầy đủ?
2. Biểu phí chi tiết **theo từng phương thức**: QR · thẻ ATM nội địa · thẻ quốc tế (Visa/MC) · ví điện tử · Internet Banking?
3. Có **phí cố định/tháng**, **phí khởi tạo**, **doanh số tối thiểu cam kết** không?
4. **Chu kỳ đối soát và chuyển tiền về tài khoản merchant**: T+? ngày làm việc? Có phí chuyển tiền về không?
5. Có yêu cầu **ký quỹ / giữ lại một phần doanh thu (rolling reserve)** không? Bao nhiêu %, giữ bao lâu?
6. **API hoàn tiền**: có hỗ trợ **hoàn một phần** (partial refund) không? Hoàn được trong bao lâu kể từ giao dịch gốc (30/90/180 ngày)? **Phí giao dịch gốc có được hoàn lại không?**
7. **Thời gian thực tế tiền về tay khách** sau khi gọi API refund, theo từng phương thức gốc?
8. ⭐ **Có hỗ trợ `pre-authorization` / `authorize` rồi `capture` sau (tạm giữ hạn mức) không?** Nếu có: áp dụng cho phương thức nào, giữ được tối đa bao nhiêu ngày, có hỗ trợ **capture một phần** không? *(xem Mục 4)*
9. Có môi trường **sandbox** không? Link tài liệu API công khai?
10. Cơ chế **ký và xác thực IPN/webhook**? (thuật toán hash, secret key, danh sách IP cần whitelist)

---

<a name="4"></a>
# 4. GIỮ CỌC — VIỆT NAM CÓ PRE-AUTHORIZATION HOLD KHÔNG?

## 4.1. Pre-authorization hold là gì và tại sao nó lý tưởng

**Cơ chế:** thay vì trừ tiền, đơn vị bán **đặt một lệnh giữ hạn mức** trên thẻ tín dụng của khách. Tiền **vẫn nằm ở tài khoản khách nhưng bị khoá, không tiêu được**. Đến khi trả máy:
- Máy nguyên vẹn → **huỷ lệnh giữ** (void) → hạn mức nhả ra, **khách chưa từng mất đồng nào**
- Máy hỏng → **capture** đúng số tiền thiệt hại

**Đây là cách các nền tảng cho thuê quốc tế xử lý cọc.** Tham chiếu đã được kiểm chứng trong file anh em:

| Nội dung | Nguồn `[XM]` |
|---|---|
| Stripe dùng `PaymentIntent` với `capture_method: manual` để đặt pre-auth hold | [Stripe Docs — Extended authorization](https://docs.stripe.com/payments/extended-authorization) |
| Thời hạn giữ mặc định **7 ngày**, mở rộng tới **~28–30 ngày** tuỳ mạng thẻ (**Visa tối đa 28 ngày; Amex/Mastercard/Discover 30 ngày**) | [Stripe Docs — Extended authorization](https://docs.stripe.com/payments/extended-authorization), [Stripe Terminal — extended authorizations](https://docs.stripe.com/terminal/features/extended-authorizations) |
| Giải thích phổ thông về preauthorization | [Stripe — Preauthorization charges](https://stripe.com/resources/more/preauthorization-charges-on-credit-cards-what-they-are-and-how-long-they-last) |
| Turo giữ cọc **0–750 USD** bằng pre-auth | `./02-nen-tang-cho-thue-quoc-te.md` dòng 41 |

## 4.2. 🔴 Vấn đề cốt lõi: pre-auth là TÍNH NĂNG CỦA MẠNG THẺ TÍN DỤNG

| Phương thức thanh toán | Có cơ chế "giữ rồi nhả"? | Độ tin cậy |
|---|---|---|
| **Chuyển khoản ngân hàng (NAPAS 24/7)** | ❌ **KHÔNG.** Chuyển khoản là hành vi **chuyển quyền sở hữu tiền dứt điểm**. Không có trạng thái trung gian "đang giữ" | `[KT-C]` |
| **Quét mã QR (VietQR)** | ❌ **KHÔNG** — bản chất vẫn là chuyển khoản | `[KT-C]` |
| **Ví điện tử (MoMo, ZaloPay)** | ❌ **KHÔNG** ở luồng thanh toán thông thường | `[KT-TB]` |
| **Thẻ tín dụng quốc tế** (Visa/Mastercard) phát hành tại VN | 🟡 **Về mặt mạng thẻ thì CÓ** — đây là thứ khách sạn/hãng xe dùng khi giữ cọc. Nhưng **có cổng VN nào mở API này cho merchant nhỏ hay không thì CHƯA XÁC MINH** | `[KT-TB]` |
| **Thẻ nội địa NAPAS** | ❓ `[CHƯA CÓ]` | — |

### ⭐ Nhưng đây mới là lý do quyết định — và nó không cần tra cứu:

> **Sinh viên Đại học FPT Đà Nẵng gần như không dùng thẻ tín dụng quốc tế.**
>
> Phân khúc khách hàng của ExamLap là **sinh viên 18–22 tuổi**, phần lớn **chưa có thu nhập ổn định** → **không đủ điều kiện được ngân hàng cấp thẻ tín dụng**. Họ thanh toán bằng **chuyển khoản, QR, MoMo**. `[SL]`
>
> **→ Ngay cả khi tìm được một cổng thanh toán Việt Nam hỗ trợ pre-auth, ExamLap vẫn KHÔNG DÙNG ĐƯỢC, vì khách hàng không có công cụ (thẻ tín dụng) để thực hiện.**
>
> **Đây là kết luận cuối cùng và nó KHÔNG phụ thuộc vào việc tra cứu thêm.** Câu hỏi "cổng VN nào hỗ trợ pre-auth" là câu hỏi **thú vị nhưng không còn quan trọng** với dự án này. Kết luận này khớp với đánh giá độc lập tại `./02-nen-tang-cho-thue-quoc-te.md` dòng 668 và `./12-ux-tham-chieu.md` dòng 333–335 `[XM]`.

## 4.3. ⭐⭐ CÔNG CỤ PHÁP LÝ ĐÚNG: "KÝ CƯỢC" — Điều 329 Bộ luật Dân sự 2015

Đây là phát hiện quan trọng nhất của Mục 4. **Nhóm đang dùng sai từ.**

| Khái niệm | Điều luật | Định nghĩa | Có đúng cho ExamLap? |
|---|---|---|---|
| **Đặt cọc** | **Điều 328 BLDS 2015** | Một bên giao tiền/vật quý cho bên kia để **bảo đảm giao kết hoặc thực hiện hợp đồng** | 🟡 Đúng một phần — chỉ hợp cho khoản **giữ chỗ khi đặt trước** |
| **⭐ Ký cược** | **Điều 329 BLDS 2015** | **"Bên thuê tài sản là ĐỘNG SẢN giao cho bên cho thuê một khoản tiền hoặc kim khí quý, đá quý hoặc vật có giá trị khác trong một thời hạn để BẢO ĐẢM VIỆC TRẢ LẠI TÀI SẢN THUÊ"** | ✅✅ **CHÍNH XÁC.** Laptop = động sản. Thuê. Bảo đảm trả lại. Đây **đúng nguyên văn** tình huống ExamLap |
| **Ký quỹ** | **Điều 330 BLDS 2015** | Gửi tiền vào **tài khoản phong toả tại một tổ chức tín dụng** để bảo đảm nghĩa vụ | ❌ Quá nặng, cần ngân hàng tham gia |
| **Bảo lãnh** | **Điều 335 BLDS 2015** | Bên thứ ba cam kết thực hiện nghĩa vụ thay nếu bên có nghĩa vụ không thực hiện | 🟢 Dùng **bổ sung** được (người bảo lãnh) |

`[KT-C]` về nội dung các chế định; `[KT-TB]` về số hiệu điều luật chính xác — **phải đối chiếu Bộ luật Dân sự 2015 (Luật số 91/2015/QH13)**.

### Hệ quả pháp lý của ký cược — rất có lợi cho ExamLap `[KT-C]`

Theo Điều 329, khi hợp đồng thuê chấm dứt:
- **Trả lại tài sản thuê đúng hạn, nguyên vẹn** → bên cho thuê **phải trả lại tiền ký cược** (sau khi trừ tiền thuê nếu chưa trả)
- **Không trả lại tài sản thuê** → **tài sản thuê thuộc về bên cho thuê** *(ở đây là ngược lại: tiền ký cược thuộc về bên cho thuê)*

> ✅ **Đây chính là cơ sở pháp lý để ExamLap giữ tiền của khách một cách HỢP PHÁP, và nó KHÔNG liên quan gì tới giấy phép trung gian thanh toán** → chi tiết ở **Mục 5**.

> 📝 **Hành động cụ thể:** trong hợp đồng thuê và trên giao diện app, **đổi chữ "đặt cọc" thành "tiền ký cược"** (hoặc ghi song song *"tiền ký cược (đặt cọc)"*). Việc này **miễn phí** và làm hợp đồng vững hơn đáng kể khi có tranh chấp. `[SL]`

## 4.4. Các phương án thay thế pre-auth — xếp hạng

| # | Phương án | Cách làm | Chi phí | Ưu | Nhược | Đánh giá |
|---|---|---|---|---|---|---|
| **1** ⭐ | **Thu ký cược thật qua VietQR rồi hoàn bằng chuyển khoản** | Khách quét QR chuyển tiền ký cược → trả máy → ExamLap chuyển khoản ngược lại | **0 đ** (NAPAS 24/7 miễn phí) | Tiền về **tức thì** cả 2 chiều; không phí; không bên thứ ba; khách thấy tiền hoàn ngay nên tin tưởng | Khách phải có sẵn tiền mặt trong tài khoản; rủi ro **thao tác thủ công gõ sai số tài khoản khi hoàn** | ✅ **CHỌN** |
| **2** | **Ký cược giảm + người bảo lãnh** | Giảm tiền ký cược, bù bằng chữ ký người bảo lãnh (bạn cùng phòng/anh chị khoá trên) | 0 đ | Rào cản tài chính thấp → nhiều khách hơn | Thực thi khó; ràng buộc yếu | 🟢 Dùng **kết hợp** với #1 |
| **3** | **Ký cược theo bậc rủi ro** | Khách lần đầu ký cược cao; khách đã thuê ≥3 lần không lỗi → giảm dần | 0 đ | Thưởng khách tốt, tạo vòng lặp giữ chân | Cần dữ liệu lịch sử | 🟢 Dùng ở giai đoạn 2 |
| **4** | **Giữ tài sản có giá trị (xe máy, laptop cũ)** | — | 0 đ | — | Rủi ro bảo quản, trách nhiệm dân sự nếu mất | ❌ Không |
| **5** | **Ký quỹ ngân hàng (Điều 330)** | Phong toả tài khoản tại NH | Phí NH `[CHƯA CÓ]` | Chặt chẽ nhất | Quá nặng cho giao dịch 2 triệu/3 ngày | ❌ Không |
| **6** | **Ví trả trước nội bộ ExamLap** | Khách nạp tiền vào "ví ExamLap" | — | — | 🔴 **CÓ DẤU HIỆU VI PHẠM PHÁP LUẬT** | 🔴 **CẤM** → Mục 5 |
| **7** | **Giữ CCCD/CMND của khách** | — | 0 đ | — | 🔴 **VI PHẠM PHÁP LUẬT** | 🔴 **CẤM TUYỆT ĐỐI** |
| **8** | **Bên thứ ba giữ hộ tiền (escrow)** | — | — | — | 🔴 **Đây chính là hoạt động cần GIẤY PHÉP NHNN** | 🔴 **CẤM** → Mục 5 |

### 🔴🔴 CẢNH BÁO ĐẶC BIỆT — KHÔNG ĐƯỢC GIỮ CCCD/CMND CỦA KHÁCH

> **Giữ, cầm cố, nhận cầm cố, thế chấp giấy tờ tuỳ thân (CCCD/CMND/hộ chiếu) là HÀNH VI BỊ PHÁP LUẬT VIỆT NAM CẤM và bị xử phạt hành chính.** `[KT-C]` về nguyên tắc.
>
> Căn cứ cần đối chiếu: **Luật Căn cước 2023** (các hành vi bị nghiêm cấm liên quan đến chiếm giữ, sử dụng trái phép thẻ căn cước) và **Nghị định 144/2021/NĐ-CP** về xử phạt VPHC trong lĩnh vực an ninh trật tự (hành vi *"thế chấp, cầm cố, nhận cầm cố"* giấy tờ tuỳ thân). `[KT-TB]` về số hiệu văn bản và **`[CHƯA CÓ]` về mức phạt cụ thể** — **phải tra chính xác trước khi đưa vào proposal**.
>
> **Quy tắc vận hành:** ExamLap được phép **XEM và CHỤP ẢNH** CCCD/thẻ sinh viên để định danh (có sự đồng ý của khách, tuân thủ **Nghị định 13/2023/NĐ-CP** về bảo vệ dữ liệu cá nhân), nhưng **TUYỆT ĐỐI KHÔNG GIỮ BẢN GỐC**. Đây là điểm mà rất nhiều tiệm cho thuê nhỏ ở VN làm sai. Xem thêm `./04-ekyc-viet-nam.md`.
>
> 💡 Thẻ sinh viên thì **không phải giấy tờ tuỳ thân do Nhà nước cấp** nên rủi ro pháp lý thấp hơn — nhưng **giá trị bảo đảm gần như bằng 0** (cấp lại dễ), nên cũng không giải quyết được vấn đề. `[SL]`

## 4.5. Quy trình thu — hoàn ký cược khuyến nghị

```
ĐẶT TRƯỚC
  └─ Thu "phí giữ chỗ" nhỏ (Điều 328 - đặt cọc), KHÔNG hoàn nếu khách bỏ hẹn
     → Chống no-show

NHẬN MÁY (tại quầy, có mặt đối mặt)
  ├─ Ký hợp đồng thuê giấy/điện tử, ghi rõ "TIỀN KÝ CƯỢC" + tình trạng máy + ảnh chụp máy
  ├─ Sinh QR ĐỘNG: [tiền thuê + tiền ký cược], nội dung = mã đơn EXL7K2M9
  ├─ Khách quét, chuyển 1 lần
  ├─ Nhân sự XÁC NHẬN tiền về (nhìn app ngân hàng) → bấm nút trong hệ thống
  └─ Giao máy

TRẢ MÁY
  ├─ Kiểm tra máy, chụp ảnh đối chứng
  ├─ Máy OK      → hoàn 100% tiền ký cược NGAY tại quầy bằng chuyển khoản
  ├─ Máy hư nhẹ  → hoàn (ký cược − chi phí sửa theo biểu giá CÔNG KHAI TRƯỚC)
  └─ CẢ HAI BÊN cùng xem màn hình xác nhận số tiền hoàn → chụp màn hình biên lai
```

> ⭐ **Nguyên tắc vàng: HOÀN NGAY TẠI QUẦY, TRƯỚC MẶT KHÁCH.** `[SL]`
> Lý do: (1) NAPAS 24/7 cho phép hoàn trong **vài giây** — không có lý do gì để hẹn hôm sau; (2) loại bỏ hoàn toàn nhóm tranh chấp "sao chưa thấy tiền"; (3) tạo **bằng chứng xã hội** mạnh nhất cho marketing truyền miệng trong ký túc xá — thứ quyết định sống còn của một dịch vụ 400 lượt/năm.
>
> ⚠️ **Rủi ro thao tác cần chặn:** khi hoàn tiền thủ công, **gõ nhầm số tài khoản = mất tiền thật, gần như không lấy lại được**. Biện pháp: (a) hệ thống **lưu sẵn số tài khoản khách** từ giao dịch đến, hiển thị để copy, **không gõ tay**; (b) bắt buộc **2 người xác nhận** với khoản hoàn > 1 triệu đ; (c) đọc to số tài khoản cho khách xác nhận trước khi bấm gửi.

---

<a name="5"></a>
# 5. ⭐⭐⭐ PHÁP LÝ: GIỮ TIỀN CỦA KHÁCH CÓ PHẢI LÀ TRUNG GIAN THANH TOÁN KHÔNG?

> **ĐÂY LÀ CÂU HỎI QUAN TRỌNG NHẤT CỦA TOÀN BỘ TÀI LIỆU.** Trả lời sai không chỉ mất tiền — mà là rủi ro **bị xử phạt hành chính, đình chỉ hoạt động**, và trong trường hợp nghiêm trọng là **trách nhiệm hình sự**.

## 5.1. TRẢ LỜI NGẮN

| Câu hỏi | Trả lời | Độ tin cậy |
|---|---|---|
| ExamLap thu **tiền thuê + tiền ký cược của chính khách thuê, cho chính hợp đồng thuê của mình**, có phải là hoạt động trung gian thanh toán không? | 🟢 **KHÔNG.** Đây là **quan hệ dân sự song phương** giữa bên cho thuê và bên thuê, được điều chỉnh bởi **Bộ luật Dân sự** (hợp đồng thuê tài sản + ký cược Điều 329), **không phải dịch vụ thanh toán** | `[KT-C]` |
| Nếu ExamLap **giữ tiền hộ người khác**, cho khách **nạp tiền vào ví ExamLap**, hoặc **thu hộ/chi hộ cho bên thứ ba**? | 🔴 **CÓ.** Đây là **hoạt động trung gian thanh toán, BẮT BUỘC phải có giấy phép của Ngân hàng Nhà nước.** Làm mà không có phép là **hoạt động không phép** | `[KT-C]` |

## 5.2. ⭐ PHÉP THỬ QUYẾT ĐỊNH — "TIỀN NÀY CỦA AI?"

Đây là cách tự kiểm tra **nhanh và chính xác** cho bất kỳ tính năng nào nhóm định làm: `[SL]` dựa trên `[KT-C]` về bản chất pháp lý của dịch vụ thanh toán

```
Khách đưa tiền cho ExamLap. Hỏi: KHOẢN TIỀN NÀY CUỐI CÙNG SẼ CHẢY VỀ ĐÂU?

├─ Về chính ExamLap, để trả cho DỊCH VỤ CỦA CHÍNH EXAMLAP
│   (tiền thuê máy, tiền ký cược cho máy của ExamLap, tiền phạt trễ hạn)
│   → 🟢 QUAN HỆ DÂN SỰ SONG PHƯƠNG. Không cần giấy phép.
│     ExamLap là NGƯỜI BÁN, không phải người trung gian.
│
├─ Về một BÊN THỨ BA nào đó (chủ máy khác, người bán khác, khách khác)
│   → 🔴 ExamLap đang ĐỨNG GIỮA hai người khác và cầm tiền của họ
│     = DỊCH VỤ TRUNG GIAN THANH TOÁN → CẦN GIẤY PHÉP NHNN
│
└─ Nằm lại trong "số dư ví" của khách để khách TIÊU DẦN về sau
    → 🔴 Đây là ĐỒNG TIỀN ĐIỆN TỬ / VÍ ĐIỆN TỬ (stored value)
      = DỊCH VỤ TRUNG GIAN THANH TOÁN → CẦN GIẤY PHÉP NHNN
```

**Diễn giải bản chất:** trung gian thanh toán là hoạt động **đứng giữa người trả tiền và người nhận tiền** để làm cho khoản tiền đó chạy từ A sang B. ExamLap **chính là B** — không đứng giữa ai cả. Người ta không cần giấy phép ngân hàng để bán một cốc cà phê hay cho thuê một cái laptop. `[KT-C]`

## 5.3. Khung pháp lý cần đối chiếu

| Văn bản | Nội dung liên quan | Độ tin cậy |
|---|---|---|
| **Nghị định 52/2024/NĐ-CP** về **thanh toán không dùng tiền mặt** | Văn bản trụ cột. Định nghĩa **dịch vụ trung gian thanh toán**, liệt kê các loại hình, quy định **điều kiện cấp Giấy phép hoạt động cung ứng dịch vụ trung gian thanh toán**. Được hiểu là **thay thế Nghị định 101/2012/NĐ-CP**, ban hành 2024 và có hiệu lực từ **01/7/2024** | `[KT-TB]` về ngày ban hành/hiệu lực — **phải xác minh** |
| **Luật Các tổ chức tín dụng 2024** | Quy định về hoạt động ngân hàng và nhận tiền gửi. Liên quan tới ranh giới "nhận tiền gửi" — điều ExamLap tuyệt đối không được chạm vào | `[KT-TB]` |
| **Bộ luật Dân sự 2015** (Luật 91/2015/QH13) | Điều 328 (đặt cọc), **Điều 329 (ký cược)** ⭐, Điều 330 (ký quỹ), Điều 335 (bảo lãnh), chương hợp đồng thuê tài sản | `[KT-C]` nội dung; `[KT-TB]` số điều |
| **Nghị định 13/2023/NĐ-CP** | Bảo vệ dữ liệu cá nhân — áp dụng khi ExamLap chụp/lưu CCCD, thẻ SV, số tài khoản khách | `[KT-TB]` |
| Nghị định xử phạt VPHC lĩnh vực **tiền tệ và ngân hàng** | Chế tài với hành vi cung ứng dịch vụ TGTT **không có giấy phép** | `[CHƯA CÓ]` số hiệu và mức phạt |

### Các loại hình dịch vụ trung gian thanh toán (cần đối chiếu danh mục chính thức)

Theo hiểu biết chung về khung pháp lý VN, danh mục dịch vụ TGTT bao gồm: `[KT-TB]`
1. Dịch vụ **chuyển mạch tài chính** *(NAPAS)*
2. Dịch vụ **bù trừ điện tử**
3. Dịch vụ **cổng thanh toán điện tử** *(VNPay, OnePay…)*
4. Dịch vụ **hỗ trợ thu hộ, chi hộ** 🔴 ← **loại hình ExamLap dễ vô tình phạm phải nhất**
5. Dịch vụ **ví điện tử** 🔴 ← **loại hình thứ hai dễ phạm phải**
6. Dịch vụ **hỗ trợ chuyển tiền điện tử**

> ⚠️ **Điều kiện cấp phép TGTT bao gồm yêu cầu vốn điều lệ tối thiểu rất lớn (mức thường được nhắc tới là 50 tỷ đồng)** `[KT-T]` — **phải xác minh**. Dù con số chính xác là bao nhiêu, thông điệp không đổi: **một nhóm sinh viên hoặc một hộ kinh doanh KHÔNG BAO GIỜ xin được giấy phép này.** Vì vậy chiến lược duy nhất khả thi là **thiết kế mô hình sao cho KHÔNG CẦN giấy phép** — chứ không phải tìm cách xin phép.

## 5.4. 🔴 DANH SÁCH ĐỎ — NHỮNG VIỆC EXAMLAP TUYỆT ĐỐI KHÔNG ĐƯỢC LÀM

| # | Hành vi bị cấm | Vì sao | Mức nguy hiểm |
|---|---|---|---|
| **1** | **Cho khách "nạp tiền" vào tài khoản/ví ExamLap để dùng dần** | Tạo ra **số dư trả trước (stored value)** = dấu hiệu điển hình của **dịch vụ ví điện tử** | 🔴🔴🔴 |
| **2** | **Thu hộ / chi hộ tiền cho bên thứ ba** — ví dụ thu tiền hộ một shop khác, hoặc chuyển tiền hộ giữa hai sinh viên | Đúng định nghĩa **dịch vụ hỗ trợ thu hộ, chi hộ** | 🔴🔴🔴 |
| **3** | **Làm trung gian giữ tiền (escrow) cho giao dịch của người khác** — ví dụ mở rộng sang "sàn cho thuê C2C", sinh viên A cho sinh viên B thuê máy, ExamLap giữ tiền ở giữa | ExamLap trở thành **bên trung gian cầm tiền của hai người khác** | 🔴🔴🔴 **Đây là cái bẫy lớn nhất khi mở rộng mô hình** |
| **4** | **Phát hành thẻ/mã trả trước, voucher nạp tiền quy đổi ra tiền mặt** | Tương tự #1 | 🔴🔴 |
| **5** | **Trả lãi / hứa sinh lời trên tiền ký cược của khách** | Chạm vào **hoạt động nhận tiền gửi** — đặc quyền riêng của tổ chức tín dụng | 🔴🔴🔴 |
| **6** | **Dùng tiền ký cược của khách để chi tiêu vận hành** (mua máy mới, trả lương) | Tiền ký cược là **tiền phải hoàn lại**. Tiêu vào đó = tạo lỗ hổng thanh khoản; khi nhiều khách đòi hoàn cùng lúc mà không có tiền → **có thể bị quy kết chiếm dụng/lạm dụng tín nhiệm chiếm đoạt tài sản** | 🔴🔴🔴 |
| **7** | **Quảng cáo bằng các từ "ví", "tài khoản thanh toán", "số dư", "nạp tiền", "chuyển tiền"** | Ngôn ngữ marketing có thể tự tạo bằng chứng chống lại mình khi bị kiểm tra | 🔴🔴 |
| **8** | **Giữ bản gốc CCCD/CMND/hộ chiếu của khách** | Hành vi bị cấm, xem Mục 4.4 | 🔴🔴🔴 |
| **9** | **Đưa mật khẩu Internet Banking cho dịch vụ bên thứ ba** | Vi phạm điều khoản ngân hàng, mất quyền được bồi thường, xem Mục 2.2 | 🔴🔴🔴 |

## 5.5. 🟢 DANH SÁCH XANH — LÀM THẾ NÀY THÌ AN TOÀN

| # | Việc | Cơ sở |
|---|---|---|
| 1 | Thu **tiền thuê** trực tiếp từ khách vào tài khoản ngân hàng của ExamLap | Bán dịch vụ cho chính mình `[KT-C]` |
| 2 | Thu **tiền ký cược** để bảo đảm việc trả lại laptop | **Điều 329 BLDS 2015** `[KT-C]` |
| 3 | Thu **tiền đặt cọc giữ chỗ** khi khách đặt trước | **Điều 328 BLDS 2015** `[KT-C]` |
| 4 | **Trừ chi phí sửa chữa** vào tiền ký cược theo biểu giá đã công bố trước và có trong hợp đồng | Thoả thuận dân sự hợp pháp `[KT-C]` |
| 5 | **Hoàn tiền ký cược** bằng chuyển khoản về đúng tài khoản khách | Nghĩa vụ theo Điều 329 `[KT-C]` |
| 6 | Dùng dịch vụ đối soát để **nhận thông báo** tiền vào tài khoản **của chính mình** | Chỉ là công cụ đọc thông tin, không luân chuyển tiền của ai `[SL]` |
| 7 | Dùng **cổng thanh toán có giấy phép** làm kênh thu tiền | Giấy phép nằm ở phía cổng; ExamLap chỉ là merchant `[KT-C]` |

## 5.6. Ba nguyên tắc thiết kế để không bao giờ chạm vạch đỏ `[SL]`

> **1. MỘT CHIỀU, MỘT LẦN, DỨT ĐIỂM.**
> Mỗi lượt thuê = **một** giao dịch tiền vào, **một** giao dịch tiền ra khi trả máy. **Không có số dư tồn đọng.** Không có "tài khoản khách". Không có "ví".
>
> **2. TIỀN KÝ CƯỢC LÀ TIỀN THIÊNG — KHÔNG ĐỤNG VÀO.**
> Mở **tài khoản ngân hàng riêng** chỉ để giữ tiền ký cược, tách khỏi tài khoản vận hành. Số dư tài khoản này phải **luôn ≥ tổng tiền ký cược đang giữ**. Đây không phải yêu cầu luật định với hộ kinh doanh, mà là **kỷ luật tự đặt ra** để không bao giờ rơi vào tình trạng mất khả năng hoàn trả. Chi phí: **0 đ** (mở thêm tài khoản thanh toán cá nhân thường miễn phí).
>
> **3. NGÔN NGỮ SẠCH.**
> Trong app, hợp đồng, fanpage — dùng: *"tiền ký cược"*, *"tiền thuê"*, *"hoàn ký cược"*. **Không bao giờ dùng**: *"ví ExamLap"*, *"số dư"*, *"nạp tiền"*, *"tài khoản thanh toán"*.

## 5.7. 🔴 Giới hạn của phân tích này

> Người viết tài liệu này **không phải luật sư**, và **không tra cứu được văn bản pháp luật gốc trong phiên làm việc** (WebSearch hết hạn mức, egress bị chặn).
>
> Phân tích trên dựa trên **nguyên lý pháp lý chung** — loại kiến thức tương đối ổn định — nhưng **số hiệu điều luật, ngày hiệu lực, mức phạt đều ở mức `[KT-TB]` hoặc `[CHƯA CÓ]`**.
>
> **Hành động bắt buộc trước khi nộp proposal:**
> 1. Tra nguyên văn **Nghị định 52/2024/NĐ-CP** trên [thuvienphapluat.vn](https://thuvienphapluat.vn) `[XM]` hoặc Cổng thông tin điện tử Chính phủ, đọc **điều định nghĩa dịch vụ TGTT** và **điều về điều kiện cấp phép**
> 2. Tra nguyên văn **Điều 328, 329, 330 Bộ luật Dân sự 2015**
> 3. ⭐ **Rẻ nhất và hiệu quả nhất: mang câu hỏi này đến giảng viên môn Luật Kinh doanh / Pháp luật đại cương của trường.** Với một dự án khởi nghiệp sinh viên, đây là kênh tư vấn **miễn phí, đáng tin, và còn tạo được người bảo trợ học thuật cho proposal.** Câu hỏi cần hỏi đúng nguyên văn:
>    > *"Một hộ kinh doanh cho thuê laptop, thu tiền ký cược của khách thuê rồi hoàn lại khi khách trả máy — việc giữ tiền ký cược đó có bị coi là hoạt động cung ứng dịch vụ trung gian thanh toán theo Nghị định 52/2024/NĐ-CP không? Nếu không, cơ sở pháp lý là điều nào của Bộ luật Dân sự?"*

---

<a name="6"></a>
# 6. HOÁ ĐƠN ĐIỆN TỬ CHO HỘ KINH DOANH

## 6.1. Vị trí của ExamLap trên bản đồ ngưỡng doanh thu

**Doanh thu năm đầu dự kiến: 82.000.000 đ/năm.** Con số này nằm ở **đáy** mọi ngưỡng quy định → đây là **tin rất tốt**.

| Ngưỡng doanh thu/năm | Hệ quả | Độ tin cậy | ExamLap (82 tr) |
|---|---|---|---|
| **≤ 100.000.000 đ** | Ngưỡng **cũ** miễn thuế GTGT và thuế TNCN cho hộ/cá nhân kinh doanh | `[KT-C]` | Dưới ngưỡng ✅ |
| **≤ 200.000.000 đ** | Ngưỡng **MỚI** — nâng từ 100 triệu lên **200 triệu đ/năm**, theo **Luật Thuế Giá trị gia tăng 2024 (Luật số 48/2024/QH15)**, áp dụng từ **01/01/2026** | `[KT-TB]` — **phải xác minh** | ✅ **Dưới ngưỡng → KHÔNG PHẢI NỘP thuế GTGT và thuế TNCN** |
| **≥ 1.000.000.000 đ** | Phải dùng **hoá đơn điện tử khởi tạo từ MÁY TÍNH TIỀN** có kết nối dữ liệu với cơ quan thuế (áp dụng cho hộ/cá nhân kinh doanh trong một số ngành: bán lẻ, ăn uống, nhà hàng, khách sạn, vận tải hành khách, giải trí…) | `[KT-TB]` | ✅ **Cách ngưỡng hơn 12 lần → KHÔNG thuộc diện bắt buộc** |

> 🟢 **KẾT LUẬN MỤC 6 (điều kiện quy mô năm đầu):**
> Với doanh thu ~82 triệu đ/năm, ExamLap **không thuộc diện bắt buộc dùng hoá đơn điện tử khởi tạo từ máy tính tiền**, và **dưới ngưỡng doanh thu chịu thuế GTGT/TNCN của hộ kinh doanh**. `[SL]` dựa trên `[KT-TB]`
>
> ⚠️ **Nhưng phải theo dõi mốc 200 triệu đ/năm** — nếu ExamLap tăng trưởng (mở rộng lên 25–30 máy) thì sẽ vượt và toàn bộ nghĩa vụ thuế thay đổi. **Đưa mốc này vào kế hoạch tài chính 3 năm.**

## 6.2. Khung pháp lý về hoá đơn điện tử — cần đối chiếu

| Văn bản | Nội dung | Độ tin cậy |
|---|---|---|
| **Nghị định 123/2020/NĐ-CP** | Văn bản gốc quy định về **hoá đơn, chứng từ** | `[KT-C]` |
| **Nghị định 70/2025/NĐ-CP** | **Sửa đổi, bổ sung Nghị định 123/2020/NĐ-CP**, hiệu lực từ **01/6/2025**. Đây là văn bản mở rộng diện bắt buộc **hoá đơn điện tử khởi tạo từ máy tính tiền** | `[KT-TB]` — **phải xác minh số hiệu và ngày hiệu lực** |
| **Nghị quyết 68-NQ/TW (2025)** về phát triển kinh tế tư nhân | Định hướng **bỏ hình thức thuế khoán đối với hộ kinh doanh**, chuyển sang **tự kê khai**, mốc thường được nhắc là **từ 01/01/2026** | `[KT-TB]` |
| **Luật Thuế GTGT 2024 (số 48/2024/QH15)** | Nâng ngưỡng doanh thu không chịu thuế GTGT của hộ/cá nhân kinh doanh lên **200 triệu đ/năm** | `[KT-TB]` |
| **Luật Quản lý thuế** và các văn bản hướng dẫn | Nghĩa vụ đăng ký, kê khai | `[KT-C]` nguyên tắc |

## 6.3. Thay đổi lớn 2025–2026 mà nhóm PHẢI nắm

> 🔔 **Bối cảnh chính sách đang chuyển động rất mạnh.** Hai thay đổi lớn nhất: `[KT-TB]`
>
> **(1) Bỏ thuế khoán với hộ kinh doanh (dự kiến từ 01/01/2026).** Trước đây hộ kinh doanh nộp một khoản thuế khoán cố định do cơ quan thuế ấn định, không phải ghi sổ chi tiết. Sau khi bỏ khoán, hộ kinh doanh phải **tự kê khai theo doanh thu thực tế** → **phải có sổ sách, chứng từ**.
>
> **(2) Mở rộng hoá đơn điện tử từ máy tính tiền (từ 01/6/2025).** Áp dụng cho hộ kinh doanh có doanh thu từ 1 tỷ đ/năm trong một số ngành.
>
> **Hệ quả thực tế cho ExamLap:** dù **chưa** thuộc diện bắt buộc, nhóm nên **tập thói quen ghi chép từ ngày đầu** — mỗi lượt thuê có mã đơn, ngày, số tiền thuê, số tiền ký cược, ngày hoàn. Hệ thống phần mềm ExamLap **vốn đã phải lưu những dữ liệu này** để vận hành → **chi phí tuân thủ thêm gần như bằng 0**, mà lại sẵn sàng khi vượt ngưỡng. `[SL]`

## 6.4. Khuyến nghị thực hành

| # | Việc | Chi phí |
|---|---|---|
| 1 | **Đăng ký hộ kinh doanh** tại UBND cấp xã/phường nơi đặt địa điểm. Lệ phí đăng ký ở mức rất thấp (đơn vị chục nghìn đồng) `[KT-T]` — **phải tra mức phí cụ thể tại Đà Nẵng** | `[CHƯA CÓ]` |
| 2 | Xuất **phiếu thu / biên nhận có đánh số** cho mỗi lượt thuê (không phải hoá đơn GTGT). Đủ để minh bạch với khách và làm bằng chứng khi tranh chấp | 0 đ (in từ app) |
| 3 | ⭐ **Biên nhận ký cược phải ghi rõ**: số tiền ký cược · ngày nhận · điều kiện hoàn · biểu giá trừ khi hư hỏng · chữ ký/xác nhận hai bên | 0 đ |
| 4 | **Chưa mua phần mềm hoá đơn điện tử** ở năm đầu — chưa cần | 0 đ |
| 5 | **Hỏi trực tiếp Chi cục Thuế khu vực tại Đà Nẵng** để xác nhận nghĩa vụ với mức doanh thu 82 triệu/năm. Cán bộ thuế tư vấn miễn phí | 0 đ |

---

<a name="7"></a>
# 7. MUA TRƯỚC TRẢ SAU (BNPL) — FUNDIIN, KREDIVO, HOME PAYLATER

## 7.1. Trạng thái dữ liệu

| Nhà cung cấp | Còn hoạt động tại VN? | Phí merchant | Nhận dịch vụ cho thuê? | Nhận hộ KD nhỏ? |
|---|---|---|---|---|
| **Fundiin** | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` |
| **Kredivo Vietnam** | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` |
| **Home PayLater** (Home Credit) | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` | `[CHƯA CÓ]` |

🔴 Không có dữ liệu xác minh. Lưu ý thêm: thị trường BNPL Việt Nam **biến động mạnh** giai đoạn 2024–2026, một số đơn vị đã thu hẹp hoặc rút khỏi thị trường — **trạng thái hoạt động của từng bên phải kiểm tra lại tại thời điểm hiện tại (09/2026)**, không được dựa vào ký ức. `[KT-T]`

## 7.2. Phân tích logic — BNPL có phù hợp với ExamLap không?

Phân tích này **không cần dữ liệu ngoài**: `[SL]`

| Vấn đề | Phân tích | Kết luận |
|---|---|---|
| **BNPL được thiết kế cho MUA HÀNG HOÁ** | Mô hình BNPL: bên BNPL trả tiền cho người bán ngay, khách trả góp cho bên BNPL. Nó giả định một **giao dịch mua đứt bán đoạn**, giá trị xác định trước | Cho thuê là **hợp đồng có thời hạn, có hoàn trả tài sản, có ký cược hoàn lại** → **không khớp mô hình** |
| **Không xử lý được ký cược** | Tiền ký cược **phải hoàn lại** cho khách. BNPL không có nghiệp vụ "ứng một khoản rồi hoàn ngược" | 🔴 **Điểm chặn cứng.** BNPL không giải được bài toán cọc |
| **Giá trị giao dịch quá nhỏ** | Một lượt thuê 150.000–300.000 đ. BNPL thường có **giá trị đơn hàng tối thiểu** | Nhiều khả năng **dưới ngưỡng tối thiểu** |
| **Yêu cầu pháp nhân** | BNPL là công ty tài chính/fintech — quy trình onboard merchant **chặt hơn cả cổng thanh toán** | Hộ kinh doanh 82 triệu doanh thu **gần như chắc chắn không được duyệt** |
| **Phí merchant cao** | Mặt bằng phí BNPL **cao hơn cổng thanh toán** (vì gánh rủi ro tín dụng) | Ăn mòn biên lợi nhuận |
| **Rủi ro đạo đức với sinh viên** | Khuyến khích sinh viên **vay tiêu dùng** để thuê laptop đi thi | ⚠️ Rủi ro hình ảnh nghiêm trọng cho một dự án khởi nghiệp sinh viên. **Ban giám khảo có thể chất vấn điểm này** |

> 🔴 **KẾT LUẬN MỤC 7: KHÔNG dùng BNPL.** Không phù hợp về mô hình nghiệp vụ, không khả thi về onboarding, và tạo rủi ro hình ảnh. `[SL]`
>
> 💡 **Nếu vấn đề thật sự là "sinh viên không đủ tiền ký cược" thì lời giải nằm ở chỗ khác, và đều miễn phí:** (a) **giảm mức ký cược** kết hợp **người bảo lãnh**; (b) **ký cược theo bậc** — khách quen ký cược thấp hơn; (c) **bảo lãnh của tổ chức** — CLB, khoa, hoặc phòng CTSV đứng ra bảo lãnh cho sinh viên khó khăn; (d) **quỹ hỗ trợ** từ chính ExamLap cho một số suất/kỳ như hoạt động cộng đồng — vừa giải quyết vấn đề, vừa là **chất liệu marketing tốt hơn nhiều so với BNPL**. `[SL]` Xem thêm `./14-marketing-sinh-vien.md`.

---

<a name="8"></a>
# 8. ⭐ KHUYẾN NGHỊ CỤ THỂ VÀ RẺ NHẤT CHO NHÓM SINH VIÊN

## 8.1. Kiến trúc thanh toán khuyến nghị — "VietQR thuần, không trung gian"

```
┌──────────────────────────────────────────────────────────────────┐
│  GIAI ĐOẠN 1 (NĂM ĐẦU — 400 lượt/năm)                            │
│                                                                  │
│  Tài khoản NH cá nhân/hộ KD (VẬN HÀNH)  ← tiền thuê              │
│  Tài khoản NH riêng (KÝ CƯỢC)           ← tiền ký cược ⭐         │
│            ▲                                                     │
│            │ chuyển khoản NAPAS 24/7 (miễn phí, tức thì)         │
│            │                                                     │
│      [ QR ĐỘNG VietQR tự sinh — 40 dòng code, 0 đ ]              │
│            ▲                                                     │
│            │ quét                                                │
│      [ Điện thoại sinh viên ]                                    │
│                                                                  │
│  ĐỐI SOÁT: người trực nhìn thông báo app NH → bấm xác nhận       │
│            (KHÔNG cần dịch vụ webhook ở giai đoạn này)           │
│                                                                  │
│  HOÀN KÝ CƯỢC: chuyển khoản ngược tại quầy, trước mặt khách      │
└──────────────────────────────────────────────────────────────────┘
```

## 8.2. Bảng chi phí — con số cụ thể

| Hạng mục | Chi phí năm 1 | Căn cứ |
|---|---|---|
| Sinh mã VietQR động | **0 đ** | Tự code, thư viện `qrcode` nguồn mở `[SL]` |
| Nhận tiền (NAPAS 24/7) | **0 đ** | Người **chuyển** trả phí, mà hầu hết NH bán lẻ đã miễn phí `[KT-C]` |
| Hoàn ký cược (chuyển khoản đi) | **0 đ** | Cần **xác nhận với ngân hàng cụ thể** rằng chuyển khoản đi cũng miễn phí `[CHƯA CÓ]` |
| Dịch vụ webhook biến động số dư | **0 đ** | **Không dùng ở giai đoạn 1** — đối soát thủ công `[SL]` |
| Cổng thanh toán | **0 đ** | **Không dùng** — xem Mục 3.3 `[SL]` |
| Hoá đơn điện tử | **0 đ** | Dưới ngưỡng bắt buộc — xem Mục 6 `[KT-TB]` |
| Thuế GTGT + TNCN | **0 đ** | 82 tr < ngưỡng 200 tr/năm `[KT-TB]` |
| Lệ phí đăng ký hộ kinh doanh | `[CHƯA CÓ]` | Mức rất thấp, một lần. Tra tại UBND phường ở Đà Nẵng |
| Mở thêm 1 tài khoản NH cho tiền ký cược | **0 đ** | Mở tài khoản thanh toán cá nhân thường miễn phí `[KT-TB]` |
| **TỔNG CHI PHÍ THANH TOÁN NĂM 1** | **≈ 0 đ** (+ lệ phí ĐKKD một lần) | |

> ⭐ **Đây là con số mạnh nhất của toàn bộ nghiên cứu và nó DÙNG ĐƯỢC NGAY trong proposal:**
> **Toàn bộ hạ tầng thu — giữ — hoàn tiền của ExamLap năm đầu có thể vận hành với chi phí gần bằng 0 đồng.**
> Không phải vì cắt xén, mà vì **ở quy mô 400 lượt/năm, mọi giải pháp trung gian đều đắt hơn giá trị chúng tạo ra.** `[SL]`
>
> So sánh để thấy ý nghĩa: nếu dùng cổng thanh toán ở mức phí 2%, chi phí sẽ là **~1.640.000 đ/năm** trên 82 triệu doanh thu — và đổi lại **tiền về chậm T+1…T+3**, khách **chờ lâu mới được hoàn cọc**. Tức là **trả tiền để nhận dịch vụ tệ hơn.**

## 8.3. Lộ trình theo giai đoạn

| Giai đoạn | Điều kiện chuyển | Việc cần làm | Chi phí tăng thêm |
|---|---|---|---|
| **GĐ 1** — hiện tại<br>~400 lượt/năm | — | VietQR tự sinh + đối soát thủ công + hoàn tại quầy | 0 đ |
| **GĐ 2** — khi đối soát thủ công bắt đầu đau<br>*(dấu hiệu: >5 lượt/ngày, hoặc >2 lần/tháng sai sót khớp tiền, hoặc phải trực ngoài giờ)* | Vượt ngưỡng đau | Thêm **dịch vụ webhook biến động số dư** (SePay/Casso/PayOS). Vẫn giữ VietQR | `[CHƯA CÓ]` — dự kiến ở bậc **trăm nghìn đồng/tháng** `[KT-T]` |
| **GĐ 3** — khi có pháp nhân + cần thẻ quốc tế / khách ngoài trường | Doanh thu > 200 tr/năm | Thêm **cổng thanh toán**, đăng ký thuế đầy đủ, cân nhắc hoá đơn điện tử | % doanh thu + phần mềm HĐĐT |

> ⚠️ **Đừng nhảy cóc.** Mỗi bước chỉ làm khi **nỗi đau thật đã xuất hiện**, không làm vì "cho chuyên nghiệp". Ở một proposal khởi nghiệp sinh viên, **khả năng nhận ra mình chưa cần gì là một điểm mạnh, không phải điểm yếu** — nên nói thẳng điều này trước ban giám khảo. `[SL]`

## 8.4. Checklist triển khai — theo thứ tự

| # | Việc | Ai làm | Xong khi nào |
|---|---|---|---|
| 1 | ✅ Xác minh **danh sách BIN ngân hàng** từ nguồn NAPAS chính thức | Kỹ thuật | Trước khi code |
| 2 | ✅ Viết hàm sinh VietQR (Mục 1.5), **test với 4 app ngân hàng**, chuyển thử 2.000 đ | Kỹ thuật | Tuần 1 |
| 3 | ✅ Kiểm tra **nội dung CK có bị cắt/thêm tiền tố** ở sao kê không → viết parser bằng **regex** | Kỹ thuật | Tuần 1 |
| 4 | ✅ **Mở tài khoản ngân hàng riêng cho tiền ký cược** | Vận hành | Tuần 1 |
| 5 | ✅ Soạn **hợp đồng thuê + biên nhận ký cược**, dùng đúng từ **"ký cược"** (Điều 329 BLDS) | Pháp lý/nội dung | Tuần 2 |
| 6 | ✅ Công bố **biểu giá bồi thường hư hỏng** rõ ràng, đưa vào hợp đồng | Vận hành | Tuần 2 |
| 7 | ✅ **Hỏi giảng viên Luật** về câu hỏi ở Mục 5.7 | Cả nhóm | Tuần 2 |
| 8 | ✅ **Hỏi Chi cục Thuế Đà Nẵng** về nghĩa vụ ở mức 82 tr/năm | Vận hành | Tuần 2 |
| 9 | ✅ **Đăng ký hộ kinh doanh** | Vận hành | Tuần 3 |
| 10 | ✅ Gửi **bảng câu hỏi Mục 2.4** cho 5 nhà cung cấp, điền vào bảng 2.3 — **để dành cho GĐ 2, không mua ngay** | Kỹ thuật | Tuần 3–4 |
| 11 | ✅ Quy trình chống sai sót khi **hoàn tiền thủ công** (Mục 4.5): lưu sẵn STK, 2 người duyệt >1 triệu | Vận hành | Trước khi chạy thật |

---

<a name="9"></a>
# 9. RỦI RO VÀ ĐIỂM CHẾT

| # | Rủi ro | Mức | Biểu hiện | Cách chặn |
|---|---|---|---|---|
| R1 | **Hiểu sai ranh giới trung gian thanh toán** khi mở rộng sang mô hình C2C (sinh viên cho sinh viên thuê, ExamLap giữ tiền giữa) | 🔴🔴🔴 | Bị cơ quan quản lý tuýt còi | Áp dụng **phép thử Mục 5.2** cho **mọi** tính năng mới trước khi làm |
| R2 | **Tiêu vào tiền ký cược** rồi không hoàn được khi nhiều khách trả máy cùng lúc | 🔴🔴🔴 | Mất uy tín tức thì trong cộng đồng SV, rủi ro pháp lý | **Tài khoản ký cược riêng, bất khả xâm phạm** (Mục 5.6) |
| R3 | **Gõ sai số tài khoản khi hoàn tiền thủ công** | 🔴🔴 | Mất tiền thật, khó lấy lại | Lưu sẵn STK từ giao dịch đến, không gõ tay; 2 người duyệt |
| R4 | **Sai mã BIN ngân hàng** trong QR | 🔴🔴 | Tiền vào tài khoản người lạ | Xác minh BIN + test quét thật trước khi chạy |
| R5 | **Khách chuyển sai nội dung / sai số tiền** | 🟡 | Không khớp được đơn | QR động nhúng sẵn cả 2; vẫn cần quy trình xử lý ngoại lệ thủ công |
| R6 | **Ngân hàng cắt/sửa nội dung chuyển khoản** | 🟡 | Parser không khớp | Dùng **regex tìm trong chuỗi**, không so sánh bằng `==`; mã đơn ngắn, chỉ A-Z0-9 |
| R7 | **Độ trễ ghi có lúc cao điểm** | 🟡 | Hàng chờ ở quầy mùa thi | Nút xác nhận thủ công; không chặn cứng quy trình bàn giao |
| R8 | **Giữ CCCD bản gốc của khách** | 🔴🔴🔴 | Vi phạm pháp luật | Quy tắc cứng: **chỉ chụp ảnh, không giữ bản gốc** |
| R9 | **Đưa mật khẩu Internet Banking cho dịch vụ bên thứ ba** | 🔴🔴🔴 | Khoá tài khoản, mất quyền bồi thường | Loại ngay nhà cung cấp yêu cầu điều này |
| R10 | **Vượt ngưỡng 200 triệu đ/năm mà không biết** | 🟡 | Truy thu thuế | Theo dõi doanh thu luỹ kế hằng tháng trong hệ thống |
| R11 | **Tranh chấp mức trừ tiền ký cược khi máy hư** | 🔴🔴 | Mất khách + lan truyền tiêu cực trong KTX | **Biểu giá bồi thường công khai TRƯỚC**, ảnh chụp máy 2 chiều, cùng xem màn hình khi hoàn |
| R12 | **Toàn bộ số liệu giá trong tài liệu này là `[CHƯA CÓ]`** | 🔴🔴🔴 | Proposal chứa số bịa → mất uy tín trước ban giám khảo | **Không trích số nào từ tài liệu này. Chạy Mục 10 trước.** |

---

<a name="10"></a>
# 10. ⭐ KẾ HOẠCH KIỂM CHỨNG — TRUY VẤN CHÍNH XÁC CẦN CHẠY

> **Đây là phần thay thế cho nghiên cứu không thực hiện được.** Mỗi dòng là một truy vấn sẵn sàng copy-paste vào công cụ tìm kiếm, xếp theo **mức độ ưu tiên**. Ước tính: **~2 giờ** làm việc là điền được phần lớn khoảng trống.

## Ưu tiên 1 🔴 — PHÁP LÝ (không có cái này thì proposal không đứng được)

| # | Truy vấn | Cần lấy về |
|---|---|---|
| 1 | `Nghị định 52/2024/NĐ-CP thanh toán không dùng tiền mặt toàn văn` | Điều định nghĩa dịch vụ TGTT + danh mục loại hình |
| 2 | `Nghị định 52/2024 điều kiện cấp giấy phép trung gian thanh toán vốn điều lệ` | Mức vốn điều lệ tối thiểu — xác nhận/bác bỏ con số 50 tỷ |
| 3 | `dịch vụ hỗ trợ thu hộ chi hộ là gì có cần giấy phép NHNN không` | Ranh giới thu hộ/chi hộ |
| 4 | `Điều 329 Bộ luật Dân sự 2015 ký cược thuê tài sản động sản` | Nguyên văn điều luật ⭐ |
| 5 | `Điều 328 Bộ luật Dân sự 2015 đặt cọc` | Nguyên văn |
| 6 | `doanh nghiệp thu tiền đặt cọc của khách có phải trung gian thanh toán không` | Ý kiến chuyên gia/luật sư |
| 7 | `xử phạt hoạt động cung ứng dịch vụ trung gian thanh toán không có giấy phép` | Chế tài |
| 8 | `Nghị định 144/2021 xử phạt cầm cố nhận cầm cố giấy tờ tùy thân CCCD` | Xác minh cảnh báo Mục 4.4 |
| 9 | `Luật Căn cước 2023 hành vi bị nghiêm cấm chiếm giữ thẻ căn cước` | Xác minh |
| 10 | `Vietnam payment intermediary service license requirements Decree 52/2024` | Đối chiếu nguồn tiếng Anh |

## Ưu tiên 2 🔴 — GIÁ DỊCH VỤ ĐỐI SOÁT (bảng 2.3 đang rỗng)

| # | Truy vấn |
|---|---|
| 11 | `SePay bảng giá gói dịch vụ` · `SePay pricing` |
| 12 | `SePay đăng ký cá nhân hay doanh nghiệp điều kiện` |
| 13 | `SePay webhook chữ ký xác thực tài liệu API` |
| 14 | `Casso bảng giá` · `Casso pricing plan` |
| 15 | `Casso hộ kinh doanh đăng ký được không` |
| 16 | `PayOS bảng giá phí giao dịch` · `PayOS pricing` |
| 17 | `PayOS điều kiện đăng ký cá nhân hộ kinh doanh` |
| 18 | `Bizfly biến động số dư bảng giá` |
| 19 | `WeOne biến động số dư giá` |
| 20 | `so sánh SePay Casso PayOS đối soát biến động số dư` |
| 21 | `dịch vụ webhook biến động số dư ngân hàng miễn phí Việt Nam` |
| 22 | `SePay Casso có cần cung cấp mật khẩu internet banking không` ⭐ *(câu hỏi an toàn quan trọng)* |

## Ưu tiên 3 🟡 — CỔNG THANH TOÁN (bảng 3.1 đang rỗng)

| # | Truy vấn |
|---|---|
| 23 | `VNPAY biểu phí giao dịch merchant 2026` |
| 24 | `VNPAY hộ kinh doanh đăng ký merchant hồ sơ` |
| 25 | `VNPAY API hoàn tiền refund thời gian` |
| 26 | `MoMo Business phí giao dịch hộ kinh doanh` |
| 27 | `MoMo API refund hoàn tiền merchant` |
| 28 | `ZaloPay merchant phí giao dịch đăng ký` |
| 29 | `OnePay phí giao dịch pre-authorization hold` ⭐ |
| 30 | `Payoo biểu phí merchant` · `Baokim phí giao dịch` |
| 31 | `cổng thanh toán Việt Nam T+1 T+2 chu kỳ đối soát chuyển tiền merchant` |
| 32 | `VNPAY MoMo pre-authorization tạm giữ hạn mức thẻ` ⭐ |
| 33 | `Vietnam payment gateway pre-authorization hold support` |
| 34 | `khách sạn Việt Nam giữ tiền cọc thẻ tín dụng pre-auth cổng nào` |

## Ưu tiên 4 🟡 — VIETQR / NAPAS (xác minh Mục 1)

| # | Truy vấn |
|---|---|
| 35 | `TCCS 03:2018/NHNNVN tiêu chuẩn QR code thanh toán` |
| 36 | `VietQR cấu trúc TLV tag 38 GUID A000000727 QRIBFTTA` ⭐ |
| 37 | `danh sách mã BIN ngân hàng VietQR NAPAS đầy đủ` ⭐ **(quan trọng — sai là mất tiền)** |
| 38 | `VietQR nội dung chuyển khoản giới hạn ký tự tag 62 08` |
| 39 | `CRC16 CCITT FALSE VietQR tính checksum` |
| 40 | `Quyết định 2345/QĐ-NHNN xác thực sinh trắc học chuyển tiền 10 triệu` |
| 41 | `VietQR.io API miễn phí giới hạn` |
| 42 | `EMVCo QR merchant presented mode specification Vietnam` |

## Ưu tiên 5 🟢 — THUẾ & HOÁ ĐƠN (xác minh Mục 6)

| # | Truy vấn |
|---|---|
| 43 | `Nghị định 70/2025/NĐ-CP hóa đơn điện tử máy tính tiền hộ kinh doanh` |
| 44 | `hộ kinh doanh doanh thu 1 tỷ hóa đơn điện tử khởi tạo từ máy tính tiền` |
| 45 | `ngưỡng doanh thu 200 triệu miễn thuế GTGT hộ kinh doanh 2026` ⭐ |
| 46 | `bỏ thuế khoán hộ kinh doanh 2026 kê khai` |
| 47 | `lệ phí đăng ký hộ kinh doanh Đà Nẵng 2026` |
| 48 | `hộ kinh doanh cho thuê tài sản thuế suất` |

## Ưu tiên 6 🟢 — BNPL (xác minh Mục 7)

| # | Truy vấn |
|---|---|
| 49 | `Fundiin phí merchant điều kiện đăng ký 2026` |
| 50 | `Kredivo Việt Nam còn hoạt động 2026` |
| 51 | `Home PayLater merchant đăng ký dịch vụ` |
| 52 | `BNPL Việt Nam dùng cho dịch vụ cho thuê được không` |
| 53 | `Vietnam BNPL market 2026 Fundiin Kredivo status` |

---

<a name="11"></a>
# 11. DANH SÁCH ĐIỀU CHƯA BIẾT

## 11.1. 🔴 Chưa biết — MỨC NGHIÊM TRỌNG (chặn quyết định)

| # | Chưa biết | Ảnh hưởng |
|---|---|---|
| 1 | **Toàn bộ bảng giá** SePay/Casso/PayOS/Bizfly/WeOne (đ/tháng, hạn mức GD) | Không lập được dự toán GĐ 2 |
| 2 | **Toàn bộ biểu phí %** của VNPay/MoMo/ZaloPay/OnePay/Payoo/Baokim | Không so sánh được phương án |
| 3 | **Điều kiện đăng ký**: các dịch vụ trên có nhận **cá nhân** / **hộ kinh doanh** không | Nếu tất cả đều đòi pháp nhân doanh nghiệp thì GĐ 2 phải lùi lại |
| 4 | **Số hiệu, ngày hiệu lực chính xác** của Nghị định 52/2024/NĐ-CP và các điều khoản định nghĩa TGTT | Nền tảng của Mục 5 |
| 5 | **Mức vốn điều lệ tối thiểu** để được cấp phép TGTT | Chỉ để minh hoạ, không đổi kết luận |
| 6 | **Số điều chính xác** của "ký cược" trong BLDS 2015 (ghi Điều 329, `[KT-TB]`) | Ảnh hưởng tính chính xác hợp đồng |
| 7 | **Cơ chế kỹ thuật** của từng dịch vụ đối soát (API chính thức / đọc email / scraping) | Quyết định an toàn — xem Mục 2.2 |
| 8 | **Danh sách BIN ngân hàng chính thức** | Sai = mất tiền |

## 11.2. 🟡 Chưa biết — MỨC TRUNG BÌNH

| # | Chưa biết |
|---|---|
| 9 | Cổng thanh toán VN nào hỗ trợ **pre-authorization hold** — *(đã trở thành câu hỏi thứ yếu, vì khách sinh viên không có thẻ tín dụng, xem Mục 4.2)* |
| 10 | Thời gian thực tế **tiền về tay khách** sau refund theo từng phương thức |
| 11 | Phí giao dịch gốc **có được hoàn** khi merchant refund không |
| 12 | Ngân hàng cụ thể nào **miễn phí chuyển khoản ĐI** (quan trọng vì ExamLap hoàn cọc 400 lần/năm) |
| 13 | Giới hạn ký tự thật của **nội dung chuyển khoản** ở từng ngân hàng |
| 14 | Ngân hàng có **thêm tiền tố** vào nội dung CK không, dạng chuỗi cụ thể |
| 15 | Ngưỡng **200 triệu đ/năm** và mốc **01/01/2026** — cần xác nhận |
| 16 | **Ngưỡng 1 tỷ đ/năm** cho hoá đơn từ máy tính tiền — cần xác nhận, và **ngành cho thuê thiết bị có nằm trong danh mục ngành bị áp dụng không** |
| 17 | Số hiệu **Nghị định 70/2025/NĐ-CP** |
| 18 | Số hiệu và mức phạt của quy định cấm **cầm cố giấy tờ tuỳ thân** |
| 19 | **Lệ phí đăng ký hộ kinh doanh** tại Đà Nẵng |
| 20 | Trạng thái hoạt động hiện tại (09/2026) của **Fundiin, Kredivo VN, Home PayLater** |
| 21 | Chuỗi **GUID `A000000727`** của VietQR |
| 22 | Số hiệu **TCCS 03:2018/NHNNVN** |
| 23 | Số hiệu và ngưỡng của **Quyết định 2345/QĐ-NHNN** |

## 11.3. 🟢 Điều KHÔNG cần tra thêm — kết luận đã vững

| # | Kết luận | Vì sao vững |
|---|---|---|
| 1 | **Chuyển khoản/QR/ví KHÔNG có cơ chế pre-auth hold** | Bản chất kỹ thuật của chuyển khoản, không phải vấn đề chính sách `[KT-C]` |
| 2 | **Khách sinh viên không có thẻ tín dụng → pre-auth vô nghĩa với ExamLap** | Suy luận từ đặc điểm nhân khẩu học, không phụ thuộc dữ liệu ngoài `[SL]` |
| 3 | **ExamLap thu tiền cho dịch vụ của chính mình → không phải TGTT** | Nguyên lý pháp lý cơ bản `[KT-C]` |
| 4 | **Không được cho khách nạp tiền vào "ví ExamLap"** | Nguyên lý pháp lý cơ bản `[KT-C]` |
| 5 | **BNPL không phù hợp** | Phân tích mô hình nghiệp vụ, không cần dữ liệu giá `[SL]` |
| 6 | **Cổng thanh toán không đáng ở quy mô 400 lượt/năm** | Số học: phí % > giá trị tạo ra, và làm chậm hoàn cọc `[SL]` |
| 7 | **Đối soát thủ công là đủ ở ~1,1 lượt/ngày** | Số học `[SL]` |
| 8 | **Kiến trúc khuyến nghị tốn ~0 đ** | Từ các kết luận trên `[SL]` |

---

# PHỤ LỤC A — DANH SÁCH NGUỒN

## A.1. Nguồn ĐÃ XÁC MINH `[XM]` (URL thật, kế thừa từ các file nghiên cứu cùng workflow)

| Nguồn | URL |
|---|---|
| Stripe Docs — Extended authorization (pre-auth hold, thời hạn 7→28/30 ngày) | https://docs.stripe.com/payments/extended-authorization |
| Stripe Docs — Terminal extended authorizations | https://docs.stripe.com/terminal/features/extended-authorizations |
| Stripe — Preauthorization charges on credit cards | https://stripe.com/resources/more/preauthorization-charges-on-credit-cards-what-they-are-and-how-long-they-last |
| Designing Idempotent Payment APIs | https://arpit.substack.com/p/designing-idempotent-payment-apis |
| Idempotency in Payment APIs (Stripe/Omise/2C2P) | https://simplico.net/2026/04/04/idempotency-in-payment-apis-prevent-double-charges-with-stripe-omise-and-2c2p/ |
| Thư viện pháp luật (cổng tra cứu văn bản) | https://thuvienphapluat.vn |

## A.2. Nguồn nội bộ workflow (file anh em trong cùng thư mục)

| File | Nội dung liên quan |
|---|---|
| `/home/user/doxuta/proposal-thue-laptop/research/02-nen-tang-cho-thue-quoc-te.md` | Mục 14.1 pre-auth Stripe; Turo giữ cọc 0–750 USD; R10 "không thể hold cọc trên thẻ ở VN" |
| `/home/user/doxuta/proposal-thue-laptop/research/09-kien-truc-phan-mem-rental.md` | Thiết kế bảng `payment_events`, idempotency webhook (dòng ~761); kết luận "VietQR cho MVP" (dòng 1446) |
| `/home/user/doxuta/proposal-thue-laptop/research/12-ux-tham-chieu.md` | Màn hình S14 đặt cọc; câu hỏi mở về pre-auth VN (dòng 333–335, 614) |
| `/home/user/doxuta/proposal-thue-laptop/research/04-ekyc-viet-nam.md` | Định danh khách hàng, xử lý CCCD |
| `/home/user/doxuta/proposal-thue-laptop/research/11-unit-economics.md` | Biên lợi nhuận để tính tác động phí cổng |
| `/home/user/doxuta/proposal-thue-laptop/research/14-marketing-sinh-vien.md` | Kênh tiếp cận sinh viên |

## A.3. ❌ Nguồn KHÔNG có

**Không có URL nào cho:** SePay · Casso · PayOS · Bizfly · WeOne · VNPay · MoMo · ZaloPay · OnePay · Payoo · Baokim · NAPAS · VietQR.io · Fundiin · Kredivo · Home PayLater · Nghị định 52/2024/NĐ-CP · Nghị định 70/2025/NĐ-CP · Bộ luật Dân sự 2015.

**Tài liệu này cố ý KHÔNG tạo link cho các nguồn trên**, vì mọi URL không do công cụ tìm kiếm trả về đều là URL bịa. Xem **Mục 10** để lấy truy vấn tìm kiếm chính xác.

---

# TÓM TẮT MỘT TRANG

| Câu hỏi | Trả lời |
|---|---|
| **Sinh QR động thế nào?** | Tự sinh chuỗi TLV theo chuẩn EMV MPM: tag `01`=`12`, tag `54`=số tiền, tag `62`→`08`=mã đơn, tag `63`=CRC16-CCITT-FALSE. ~40 dòng code, **0 đ**. Code mẫu ở Mục 1.5 |
| **Nhận webhook báo tiền về?** | **Chưa cần.** Ở 1,1 lượt/ngày, người trực nhìn app ngân hàng là đủ. Để dành cho GĐ 2 |
| **Giá SePay/Casso/PayOS?** | 🔴 **KHÔNG CÓ DỮ LIỆU.** Dùng bảng câu hỏi Mục 2.4 để tự lấy báo giá |
| **Phí cổng thanh toán?** | 🔴 **KHÔNG CÓ DỮ LIỆU.** Nhưng phân tích Mục 3.3 cho thấy **không nên dùng** ở quy mô này |
| **VN có pre-auth hold không?** | Trên **chuyển khoản/QR/ví: KHÔNG** — bản chất kỹ thuật `[KT-C]`. Trên thẻ tín dụng quốc tế thì mạng thẻ có, nhưng **khách sinh viên không có thẻ tín dụng → không dùng được** |
| **Vậy giữ cọc bằng gì?** | **Thu tiền ký cược thật qua VietQR, hoàn bằng chuyển khoản ngay tại quầy trước mặt khách.** Chi phí 0 đ, tức thì cả hai chiều |
| ⭐ **Giữ tiền cọc có phải trung gian thanh toán không?** | 🟢 **KHÔNG** — thu tiền cho dịch vụ của chính mình là quan hệ dân sự song phương (**ký cược, Điều 329 BLDS 2015**), không phải dịch vụ thanh toán |
| ⭐ **Vậy KHÔNG được làm gì?** | 🔴 Không cho khách **nạp tiền vào ví ExamLap** · Không **thu hộ/chi hộ** cho bên thứ ba · Không làm **escrow** giữ tiền giữa hai người khác · Không **trả lãi** trên tiền cọc · Không **tiêu vào tiền ký cược** · Không **giữ CCCD bản gốc** · Không **đưa mật khẩu Internet Banking** cho bên thứ ba |
| **Có phải xuất hoá đơn điện tử không?** | Ở 82 tr/năm: **không thuộc diện bắt buộc** (ngưỡng máy tính tiền là 1 tỷ đ/năm) và **dưới ngưỡng chịu thuế 200 tr/năm** `[KT-TB]` — **phải xác nhận với Chi cục Thuế** |
| **Dùng BNPL được không?** | ❌ **Không.** Sai mô hình nghiệp vụ (không xử lý được cọc hoàn lại), không onboard được, rủi ro hình ảnh |
| ⭐ **Tổng chi phí thanh toán năm 1?** | **≈ 0 đồng** (+ lệ phí đăng ký hộ kinh doanh một lần) |

> 🔴 **NHẮC LẠI LẦN CUỐI:** không một con số giá nào trong tài liệu này được xác minh. **Chạy Mục 10 trước khi đưa bất cứ thứ gì vào proposal.**
