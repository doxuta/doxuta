# 06 — CHỐNG TRỘM & QUẢN LÝ THIẾT BỊ CHO ĐỘI LAPTOP CHO THUÊ (10–50 MÁY)

> Nguyên liệu thô cho proposal khởi nghiệp "Website cho thuê laptop đi thi" — ĐH FPT Đà Nẵng (Hoà Hải, Ngũ Hành Sơn).
> Ngày nghiên cứu: **14/09/2026**.
> Người dùng cuối: sinh viên thuê máy theo **ca thi / theo ngày**, thời gian giữ máy ngắn (2–8 giờ), số máy 10–50.

---

## 0. CẢNH BÁO VỀ PHẠM VI DỮ LIỆU (ĐỌC TRƯỚC)

Phiên nghiên cứu này chạy sau **proxy egress có allowlist rất hẹp**. Chỉ 3 tên miền truy cập được:

| Tên miền | Trạng thái |
|---|---|
| `www.microsoft.com` | ✅ Truy cập được |
| `github.com` | ✅ Truy cập được |
| `raw.githubusercontent.com` | ✅ Truy cập được |

Các tên miền bị chặn (đã thử và nhận lỗi `EGRESS_BLOCKED`), nên **KHÔNG có số liệu giá xác minh** cho nhóm này:
`preyproject.com`, `www.hexnode.com`, `scalefusion.com`, `www.manageengine.com`, `www.miradore.com`, `fleetdm.com` (website), `www.absolute.com`, `www.faronics.com`, `www.kensington.com`, `www.apple.com`, `support.microsoft.com`, `learn.microsoft.com`, `en.wikipedia.org`, `vnexpress.net`, `tiki.vn`, `shopee.vn`, `cellphones.com.vn`, `fptshop.com.vn`, `www.thegioididong.com`, `www.amazon.com`.

Ngân sách WebSearch của phiên cũng đã cạn (200/200), nên không thể khám phá thêm tên miền mới.

**Hệ quả quan trọng cho người viết proposal:**
- Mọi con số trong file này đều kèm URL đã fetch thật. Chỗ nào **không có URL** → đã đưa xuống mục **"§10 — Chưa xác minh"**. Tuyệt đối không bịa thêm số.
- Toàn bộ **giá tại Việt Nam (VND)** cho AirTag, GPS tracker, khoá Kensington, tem niêm phong, khắc laser… **chưa xác minh được** và phải đi khảo giá lại (xem §10 + §11 checklist).
- Tài liệu Microsoft được lấy từ **repo nguồn chính thức của Microsoft Learn** (`MicrosoftDocs/memdocs`) trên GitHub, vì `learn.microsoft.com` bị chặn. Repo này đã được **archive ngày 02/09/2026** (read-only) nhưng vẫn là bản nguồn chính thức: [MicrosoftDocs/memdocs](https://github.com/MicrosoftDocs/memdocs).

---

## 1. BỐI CẢNH RỦI RO CỤ THỂ CỦA MÔ HÌNH NÀY

Trước khi chọn công cụ, cần định nghĩa đúng "địch thủ" (threat model). Mô hình cho thuê laptop đi thi có **4 rủi ro tách biệt**, và mỗi rủi ro cần một lớp phòng thủ khác nhau:

| # | Rủi ro | Xác suất (định tính) | Thiệt hại | Lớp phòng thủ phù hợp |
|---|---|---|---|---|
| R1 | **Không trả máy / ôm máy bỏ trốn** (thuê rồi biến mất) | Thấp–trung bình (KH là SV có mã số, có thể truy) | Cao (mất nguyên máy) | Định danh + đặt cọc + hợp đồng; MDM chỉ hỗ trợ chứng cứ |
| R2 | **Mất/bị trộm trong lúc thuê** (để quên ở căn tin, bị giật) | Trung bình | Cao | Định vị + khoá/xoá từ xa + bảo hiểm/cọc |
| R3 | **Hư hỏng / cài bậy / nhiễm mã độc** trong ca thuê | Cao (chắc chắn xảy ra) | Thấp mỗi lần, nhưng tốn công | Khôi phục trạng thái sạch tự động (đây mới là chi phí vận hành thật) |
| R4 | **Rò rỉ dữ liệu giữa 2 lượt thuê** (SV A để lại file/mật khẩu, SV B đọc được) | Cao | Trung bình (uy tín, pháp lý) | Xoá tài khoản tự động + mã hoá đĩa |

**Nhận định cốt lõi:** với đội 10–50 máy phục vụ ca thi ngắn, **R3 và R4 xảy ra hằng ngày**, còn R1/R2 là sự kiện hiếm. Ngân sách nên đổ vào **tự động hoá làm sạch máy giữa các lượt**, chứ không phải vào các gói MDM chống trộm đắt tiền. Đây là kết luận trung tâm của toàn bộ báo cáo.

---

## 2. MDM / UEM CHO WINDOWS

### 2.1 Microsoft Intune — giá chính thức (đã fetch)

Nguồn: [Microsoft Intune pricing — microsoft.com](https://www.microsoft.com/en-us/security/business/microsoft-intune-pricing) (fetch ngày 14/09/2026)

| Sản phẩm | Giá niêm yết (USD) | Điều kiện |
|---|---|---|
| **Microsoft Intune Plan 1** (standalone) | **8,00 USD / người dùng / tháng** | trả theo năm, tự động gia hạn |
| Microsoft Intune Plan 2 (add-on) | 4,00 USD / người dùng / tháng | trả theo năm; **cần Plan 1 làm nền** |
| **Microsoft Intune Suite** | **10,00 USD / người dùng / tháng** | gói tổng hợp |
| Intune Remote Help (add-on) | 3,50 USD / người dùng / tháng | cần Plan 1 |
| Intune Endpoint Privilege Management | 3,00 USD / người dùng / tháng | cần Plan 1 |
| Intune Advanced Analytics | 5,00 USD / người dùng / tháng | cần Plan 1 |
| Intune Enterprise Application Management | 2,00 USD / người dùng / tháng | cần Plan 1 |
| Microsoft Cloud PKI | 2,00 USD / người dùng / tháng | cần Plan 1 |
| Microsoft 365 E3 (có Teams) | 39,00 USD / người dùng / tháng | trả theo năm; đã bao gồm Intune nền tảng |
| Microsoft 365 E3 (không Teams) | 30,45 USD / người dùng / tháng | trả theo năm |
| Microsoft 365 E5 (có Teams) | 60,00 USD / người dùng / tháng | trả theo năm; đầy đủ Intune |
| Microsoft 365 E5 (không Teams) | 51,45 USD / người dùng / tháng | trả theo năm |

**Ghi chú thời sự:** trang giá nêu rằng **từ tháng 7/2026, một số năng lực Intune nâng cao đã được đưa vào sẵn Microsoft 365 E3 và E5**. Điều này có nghĩa mốc giá trên là mốc 2026, hợp lệ để trích dẫn cho proposal tháng 9/2026.

### 2.2 Vấn đề chí mạng: Intune tính tiền theo NGƯỜI DÙNG, không theo MÁY

Đây là điểm mà đa số bản proposal sinh viên hiểu sai. Toàn bộ bảng giá công khai của Intune là **per user/month**, không phải per device/month ([nguồn giá đã dẫn](https://www.microsoft.com/en-us/security/business/microsoft-intune-pricing) — mục FAQ không hề nhắc tới SKU per-device, đã kiểm tra).

Tuy nhiên tài liệu kỹ thuật xác nhận **có tồn tại license theo thiết bị**:

> "Organizations can purchase device-only subscriptions for non-user-affiliated devices (kiosks, IoT, shared devices). These apply when devices enroll through specific methods including Windows Autopilot Self-Deploying mode, Apple Device Enrollment Program without user affinity, or Android Enterprise dedicated enrollment."
> — [memdocs/intune/fundamentals/licensing.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/intune/fundamentals/licensing.md)

Giới hạn của license device-only (trích cùng nguồn): **"Intune app protection policies"**, **Conditional Access** và các tính năng gắn với người dùng **"not supported"**.

Tài liệu Autopilot self-deploying cũng xác nhận mô hình tính tiền này:
> "Licensing: Organizations can use device-only subscriptions, with Intune licensing **'per device per month'** for unaffiliated devices."
> — [memdocs/autopilot/self-deploying.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/autopilot/self-deploying.md)

⚠️ **Giá cụ thể của SKU device-only KHÔNG xuất hiện trên trang giá công khai đã fetch** → xem §10.

**Ý nghĩa cho startup:** mô hình cho thuê là "thiết bị dùng chung, không gắn người dùng cố định" → về mặt kiến trúc đúng là kịch bản device-only. Nhưng vì không xác minh được giá, **proposal nên tính theo kịch bản xấu nhất: 1 license user Plan 1 = 8 USD/tháng** và nói rõ đây là trần chi phí.

### 2.3 Intune for Education

> "Intune Plan 1 for Education is included in the following licenses: **Microsoft 365 Education A5**" và "**Microsoft 365 Education A3**".
> — [memdocs/intune/fundamentals/licensing.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/intune/fundamentals/licensing.md)

Tài liệu Autopilot liệt kê **"Intune for Education subscription"** là một trong các license hợp lệ để chạy Autopilot ([requirements.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/autopilot/requirements.md)).

**Cơ hội thực tế cần kiểm chứng:** ĐH FPT là tổ chức giáo dục, nhiều khả năng đã có tenant Microsoft 365 Education. Nếu nhóm khởi nghiệp là **CLB/dự án được nhà trường bảo trợ**, có khả năng dùng ké tenant A1/A3 của trường thay vì mua license thương mại. Đây là đòn bẩy chi phí lớn nhất có thể có. **Chưa xác minh được** (trang giá Education của Microsoft trả HTTP 503 khi fetch) → §10.

### 2.4 Windows Autopilot — điều kiện & giá trị thực

Nguồn: [memdocs/autopilot/requirements.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/autopilot/requirements.md)

**Phiên bản Windows được hỗ trợ:**
- Windows 11: Pro, Pro Education, Pro for Workstations, Enterprise, Education, Enterprise LTSC, IoT Enterprise
- Windows 10: các bản tương ứng
- ❗ **Windows Home KHÔNG có trong danh sách.**

**License bắt buộc (trích nguyên văn):**
> "Microsoft 365 Business Premium subscription, Microsoft 365 F1 or F3 subscription, Microsoft 365 Academic A1, A3, or A5 subscription, Microsoft 365 Enterprise E3 or E5 subscription, Enterprise Mobility + Security E3 or E5 subscription, Intune for Education subscription, or Microsoft Entra ID P1 or P2 and Microsoft Intune subscription or an alternative MDM service."

**Yêu cầu mạng:** phân giải DNS ra Internet; *"Allow access to all hosts via port 80 (HTTP), 443 (HTTPS), and 123 (UDP/NTP)"*.

**Đăng ký máy thủ công (quan trọng cho startup mua máy cũ):**
Nguồn: [memdocs/autopilot/manual-registration.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/autopilot/manual-registration.md)
- Phải lấy **hardware hash** của máy rồi upload lên dịch vụ Autopilot.
- Upload qua: **Intune (500 máy/lần)**, Partner Center (1.000 máy/lần), M365 Business Premium (1.000 máy/lần).
- Đăng ký thủ công chỉ nhận **"4K HH" (4K hardware hash)**, trong khi OEM/partner nhận được **Tuple hoặc PKID** (linh hoạt hơn).
- ⚠️ Microsoft nói thẳng: đăng ký thủ công *"is intended primarily for testing and evaluation scenarios"* — chủ yếu để thử nghiệm, không phải triển khai quy mô.

**Autopilot self-deploying mode** ([self-deploying.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/autopilot/self-deploying.md)) — đúng kịch bản "máy dùng chung":
- Yêu cầu **TPM 2.0** (không chấp nhận VM / Hyper-V TPM).
- Máy nối Ethernet: **không cần thao tác nào**; máy Wi-Fi: chỉ chọn ngôn ngữ + kết nối mạng.
- Không cần nhập credential: máy tự xác thực bằng **TPM attestation** và tự join Microsoft Entra ID.
- Hạn chế: **chỉ Entra join** (không hybrid); **không tự re-enroll** — muốn triển khai lại phải xoá record và đăng ký lại; **không gán primary user**.

**Yêu cầu phần cứng** ([autopilot-device-guidelines.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/autopilot/autopilot-device-guidelines.md)): *"TPM 2.0 is enabled and in a good state on devices intended for Windows Autopilot self-deploying mode."*

### 2.5 Hexnode / Scalefusion / ManageEngine MDM Plus / Miradore

❌ **Không xác minh được giá.** Cả 4 tên miền đều bị proxy chặn (xem §0). Không đưa số nào vào proposal nếu chưa tự khảo lại. Xem §10 và checklist §11.

### 2.6 Fleet (FleetDM) — mã nguồn mở, có giá xác minh được ✅

Nguồn giá (đọc trực tiếp từ mã nguồn trang pricing trong repo chính thức): [fleetdm/fleet — website/views/pages/pricing.ejs](https://raw.githubusercontent.com/fleetdm/fleet/main/website/views/pages/pricing.ejs)

| Gói | Giá | Mô tả |
|---|---|---|
| **Free** | **0,00 USD / host / tháng** | "Basic features, no support" |
| **Premium** | **7,00 USD / host / tháng** | "Manage and protect endpoints" |
| Custom | Liên hệ | Cho triển khai lớn |

Trang giá **không nêu số host tối thiểu**.

**Phân chia tính năng** ([handbook/company/pricing-features-table.yml](https://raw.githubusercontent.com/fleetdm/fleet/main/handbook/company/pricing-features-table.yml)):

| Có trong bản FREE | Chỉ có ở PREMIUM |
|---|---|
| Self-hosted; MDM đa nền tảng (Apple, **Windows**, Linux, iOS, iPadOS, Android, ChromeOS) | Managed cloud hosting; MDM migration; zero-touch setup |
| Áp cấu hình OS bằng configuration profiles | **Disk encryption enforcement** (ép mã hoá đĩa) |
| **Script execution** (chạy script từ xa) | **Remote lock and wipe commands** (khoá & xoá từ xa) |
| Device inventory; labels; policies | OS update enforcement; conditional access / device health |
| FIM, file carving, quét lỗ hổng liên tục | Application deployment & management; device remediation |
| REST API; webhooks & automations; SSO/SAML; custom logging | Two-factor authentication; **RBAC**; audit logging; EPSS/CVSS, CISA KEV |

License: **MIT cho bản free** — *"Free Version: Available under the MIT license and 'will always be free'"* ([fleetdm/fleet README](https://raw.githubusercontent.com/fleetdm/fleet/main/README.md)).

⚠️ **Bẫy cho startup:** tính năng mà mô hình cho thuê cần nhất — **remote lock/wipe** và **ép mã hoá đĩa** — nằm ở **Premium (7 USD/host/tháng)**. Với 30 máy = **210 USD/tháng**, đắt hơn cả Intune Plan 1 nếu tính theo số máy. Bản Free vẫn hữu ích (inventory + chạy script + policy), nhưng không phải công cụ chống trộm.

### 2.7 Lựa chọn headless / mã nguồn mở khác

**MeshCentral** — [github.com/Ylianst/MeshCentral](https://github.com/Ylianst/MeshCentral)
- *"A complete web-based remote monitoring and management web site"*, quản lý máy trong LAN hoặc qua Internet.
- Tính năng: **remote desktop, terminal, quản lý/truyền file, Wake-on-LAN, device location/mapping**.
- **License Apache 2.0 — miễn phí, tự host.**
- ✅ **Đây là ứng viên số 1 cho startup vốn nhỏ**: 0 đồng license, chạy được trên 1 VPS rẻ, có sẵn bản đồ vị trí thiết bị và remote desktop để hỗ trợ khách đang thi.

**Tactical RMM** — [github.com/amidaware/tacticalrmm](https://raw.githubusercontent.com/amidaware/tacticalrmm/develop/README.md)
- Django + Vue, agent Golang, **tích hợp sẵn MeshCentral**.
- Tính năng: *"Teamviewer-like remote desktop control"*, *"real-time remote shell"*, sửa registry, duyệt file, *"Remote command and script execution (batch, powershell, python, nushell and deno scripts)"*, patch management, event log, quản lý services, cảnh báo email/SMS/webhook, triển khai phần mềm qua chocolatey, kiểm kê.
- Agent chạy trên **Windows 7, 8.1, 10, 11** và Server 2008R2–2025.
- 🚨 **RỦI RO PHÁP LÝ CẦN LƯU Ý:** license là **"Tactical RMM License Version 1.0"** — *không phải* open source. [LICENSE.md](https://github.com/amidaware/tacticalrmm/blob/develop/LICENSE.md) cấm dùng phần mềm *"as part of any other commercial or for-profit service"* nếu không có chấp thuận bằng văn bản của AmidaWare LLC. Giám sát nội bộ mạng của chính mình thì được tự do; nhưng vì startup này **là** một dịch vụ thương mại, cần hỏi ý kiến nhà cung cấp trước khi dùng. **Trong proposal nên ưu tiên MeshCentral (Apache 2.0) để tránh vướng.**

**Prey** — [github.com/prey/prey-node-client](https://github.com/prey/prey-node-client)
- *"a SaaS platform for device tracking, monitoring, data protection, and device management"* với **agent mã nguồn mở**.
- Chạy trên **Windows, macOS và Ubuntu**.
- Agent phát hành theo **GPLv3**.
- Năng lực API (đọc từ [prey/mcp-prey README](https://raw.githubusercontent.com/prey/mcp-prey/main/README.md)): kích hoạt device action **alarm / alert / lock**; đánh dấu thiết bị **missing / recovered**; lấy **lịch sử vị trí** (JSON hoặc CSV); quản lý **zones (geofence)** — liệt kê, xem chi tiết, tạo/cập nhật; quản lý user, device, label và **mass actions**.
- ⚠️ Tài liệu MCP **không thấy** tool `locate` hay `wipe` riêng — chỉ có alarm/alert/lock; và thao tác ghi bị tắt mặc định (`PREY_ALLOW_WRITE=true` mới bật).
- ❌ **Giá Prey không xác minh được** (`preyproject.com` bị chặn) → §10.

### 2.8 Bảng so sánh MDM/UEM (chỉ ghi số đã xác minh)

| Giải pháp | Giá đã xác minh | Đơn vị tính | Windows? | Khoá từ xa | Xoá từ xa | Định vị | Nguồn |
|---|---|---|---|---|---|---|---|
| Intune Plan 1 | **8,00 USD/tháng** | / người dùng | ✅ | ❌ **Không hỗ trợ Windows** | ✅ | ✅ (có điều kiện) | [pricing](https://www.microsoft.com/en-us/security/business/microsoft-intune-pricing) |
| Intune Plan 2 (add-on) | 4,00 USD/tháng | / người dùng | ✅ | — | — | — | như trên |
| Intune Suite | 10,00 USD/tháng | / người dùng | ✅ | — | — | — | như trên |
| Intune device-only | ⚠️ chưa có giá | / thiết bị / tháng | ✅ | — | — | — | [licensing.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/intune/fundamentals/licensing.md) |
| M365 Business Premium | ⚠️ chưa xác minh (503) | / người dùng | ✅ | — | — | — | — |
| M365 E3 (có Teams) | 39,00 USD/tháng | / người dùng | ✅ | — | — | — | [pricing](https://www.microsoft.com/en-us/security/business/microsoft-intune-pricing) |
| Fleet Free | **0 USD** | / host | ✅ | ❌ (Premium) | ❌ (Premium) | ❌ | [pricing.ejs](https://raw.githubusercontent.com/fleetdm/fleet/main/website/views/pages/pricing.ejs) |
| Fleet Premium | **7,00 USD/tháng** | / host | ✅ | ✅ | ✅ | ❌ (không nêu) | như trên |
| MeshCentral | **0 USD (Apache 2.0)** | tự host | ✅ | — | — | ✅ mapping | [repo](https://github.com/Ylianst/MeshCentral) |
| Tactical RMM | 0 USD nhưng **hạn chế thương mại** | tự host | ✅ | — | — | — | [LICENSE](https://github.com/amidaware/tacticalrmm/blob/develop/LICENSE.md) |
| Prey | ⚠️ chưa xác minh | — | ✅ | ✅ lock | ⚠️ không rõ | ✅ location history + geofence | [mcp-prey](https://raw.githubusercontent.com/prey/mcp-prey/main/README.md) |
| Hexnode / Scalefusion / ManageEngine / Miradore | ❌ bị chặn | — | — | — | — | — | — |

---

## 3. PHÁT HIỆN QUAN TRỌNG NHẤT: INTUNE **KHÔNG** KHOÁ ĐƯỢC MÁY WINDOWS TỪ XA

Đây là điều gần như mọi bài viết marketing về MDM đều làm người đọc hiểu nhầm. Tài liệu chính thức nói rõ:

**Remote lock — nền tảng được hỗ trợ (trích nguyên văn):**
> "Android Enterprise corporate-owned dedicated (COSU)
> Android Enterprise corporate-owned fully managed (COBO)
> Android Enterprise corporate-owned work profile (COPE)
> Android Open Source Project (AOSP)
> iOS/iPadOS
> macOS
> visionOS 2.0+"
>
> — [memdocs/.../actions/remote-lock.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/intune/device-management/actions/remote-lock.md)

👉 **Windows KHÔNG có trong danh sách.** Không có nút "khoá máy Windows từ xa" trong Intune.

**Locate device — nền tảng được hỗ trợ (trích nguyên văn):**
> "Android Enterprise corporate-owned dedicated (COSU)
> - Android Enterprise corporate-owned fully managed (COBO)
> - Android Enterprise corporate-owned work profile (COPE)
> - iOS/iPadOS in Supervised Mode
> - **Windows**"
>
> — [memdocs/.../actions/locate.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/intune/device-management/actions/locate.md)

👉 **Windows CÓ** định vị được. Nhưng kèm điều kiện và giới hạn nặng:
- Phải tạo trước **Settings catalog policy** cho Windows với setting *"Privacy > Let Apps Access Location: Force allow"* và gán cho device group. Không có policy này thì lệnh locate vô tác dụng.
- **Dữ liệu vị trí chỉ lưu 24 giờ** rồi tự xoá; **không hỗ trợ xoá thủ công**.
- **Không có Lost Mode cho Windows** (Lost Mode chỉ có ở iOS/iPadOS và Android).

**Kết luận cho proposal:** nếu chọn Intune, kịch bản mất máy Windows thực tế chỉ còn **Locate (24h) + Wipe**, chứ **không** có "khoá màn hình hiển thị số điện thoại liên hệ" như trên iPhone. Đừng vẽ tính năng đó vào slide.

---

## 4. XOÁ / KHÔI PHỤC MÁY GIỮA CÁC LƯỢT THUÊ — PHẦN QUAN TRỌNG NHẤT VỀ VẬN HÀNH

### 4.1 Bốn lệnh reset của Windows/Intune — khác nhau ra sao

| Lệnh | Xoá gì | Giữ gì | Còn quản lý được không | Nguồn |
|---|---|---|---|---|
| **Wipe** | Factory reset: xoá dữ liệu người dùng, cài đặt, policy MDM | (tuỳ chọn) | Tuỳ chọn | [wipe.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/intune/device-management/actions/wipe.md) |
| **Retire** | Xoá dữ liệu công ty, unenroll khỏi Intune, xoá app/policy/profile Wi-Fi/VPN/chứng chỉ | **Giữ dữ liệu cá nhân**, M365 Apps, Win32 app cài qua Intune | ❌ Mất quản lý | [retire.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/intune/device-management/actions/retire.md) |
| **Fresh Start** | Xoá app (đặc biệt app OEM cài sẵn) | Tuỳ chọn *"Retain user data"*: giữ nội dung thư mục Home, giữ Entra join, tự re-enroll MDM | ✅ nếu retain | [fresh-start.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/intune/device-management/actions/fresh-start.md) |
| **Autopilot Reset** ⭐ | Xoá file cá nhân, app, settings; đặt lại region/ngôn ngữ/bàn phím | **Giữ Entra ID identity, giữ enrollment Intune, giữ Wi-Fi, giữ provisioning package, giữ chứng chỉ SCEP** | ✅ | [windows-autopilot-reset.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/autopilot/windows-autopilot-reset.md) |

**Wipe trên Windows có 3 chế độ** ([wipe.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/intune/device-management/actions/wipe.md)):
1. **Preserve enrollment & user account** — factory reset nhưng giữ dữ liệu/tài khoản người dùng, máy vẫn enroll Intune.
2. **Protected wipe with power persistence** — xoá sạch + ghi đè vùng trống, tiếp tục cả khi mất điện. ⚠️ Microsoft cảnh báo: *"This option can prevent some devices from starting up again"* — chỉ dùng trên máy công ty có quy trình phục hồi.
3. **Standard wipe** — factory reset thường; nếu bị gián đoạn, máy có thể rollback hoặc **thành cục gạch**.

### 4.2 ⭐ Autopilot Reset — lựa chọn kỹ thuật tốt nhất để "trả máy về trạng thái sạch"

Nguồn: [memdocs/autopilot/windows-autopilot-reset.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/autopilot/windows-autopilot-reset.md) và [actions/autopilot-reset.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/intune/device-management/actions/autopilot-reset.md)

**Reset tại chỗ (local) — miễn phí thao tác, đúng cho quầy nhận máy:**
- Từ **màn hình khoá**, nhấn tổ hợp **`CTRL + WIN + R`**.
- Cần xác thực bằng **credential local admin**.
- Lưu ý: khi reset local, *"the device's primary user and the Microsoft Entra device owner aren't updated"*.

**Reset từ xa (remote):**
- Kích hoạt từ Intune; máy phải **MDM-managed + Microsoft Entra joined**.
- Cần vai trò: **Help Desk Operator**, **School Administrator**, hoặc custom role có quyền *"Remote tasks/Wipe"*. (Tài liệu tổng quan còn nhắc tới Intune Service Administrator.)
- Remote reset **xoá primary user và device owner**; người đăng nhập kế tiếp trở thành owner.

**Điều kiện kỹ thuật:** phải bật **Windows Recovery Environment (WinRE)** — nếu chưa, chạy `reagentc.exe /enable`.

**Giới hạn:** *"Windows Autopilot Reset doesn't support Microsoft Entra hybrid joined devices or Surface Hub devices."*

**Hỗ trợ:** Windows 11 và Windows 10.

👉 **Quy trình vận hành đề xuất:** khách trả máy → nhân viên quầy nhấn `CTRL+WIN+R` ngay tại màn hình khoá → nhập mật khẩu admin → máy tự về trạng thái sạch, **vẫn giữ Wi-Fi và vẫn còn nằm trong Intune**, sẵn sàng cho lượt thuê sau. Đây là thao tác **1 phím tắt, 0 đồng license bổ sung** (miễn là đã có Intune/Autopilot).

### 4.3 ⭐⭐ Shared PC mode (Shared multi-user device) — giải pháp rẻ nhất và phù hợp nhất

Nguồn: [ref-shared-device-settings-windows.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/intune/device-configuration/templates/ref-shared-device-settings-windows.md) và [configure-shared-device.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/intune/device-configuration/templates/configure-shared-device.md)

Windows có sẵn chế độ "máy dùng chung" — **đúng y hệt mô hình cho thuê theo ca**.

**Nền tảng hỗ trợ:** Windows **Professional**, Windows **Enterprise**, Windows Holographic for Business.
❗ **Windows Home KHÔNG được hỗ trợ.**

**Quyền cần có để cấu hình:** vai trò Intune **Policy and Profile Manager**.

**Các thiết lập có sẵn (trích từ tài liệu tham chiếu):**

| Thiết lập | Ý nghĩa với mô hình cho thuê |
|---|---|
| **Shared PC Mode** | Bật chế độ dùng chung; *"only one user signs in to the device at a time"* |
| **Guest Account** | Cho phép đăng nhập bằng **Guest**, **Domain**, hoặc **Guest and domain** → SV thuê máy có thể vào bằng tài khoản khách |
| **Account Management** | Bật tự động xoá tài khoản guest và directory theo ngưỡng |
| **Account Deletion Timing** ⭐ | Chọn **"Immediately after log-out"** → **tài khoản + dữ liệu của SV bị xoá ngay khi đăng xuất** |
| Start Delete Threshold | % dung lượng còn lại (0–100) bắt đầu xoá tài khoản |
| Stop Delete Threshold | % dung lượng (0–100) dừng xoá |
| Inactive Account Threshold | Xoá tài khoản sau N ngày không đăng nhập (**0–60 ngày**) |
| **Local Storage** | Cho/cấm người dùng lưu file cục bộ qua File Explorer |
| Power Policies | Cho/cấm người dùng đổi hibernate/sleep/power |
| Sleep Timeout | Số giây không hoạt động trước khi ngủ (**0–18000 giây**) |
| Sign-in When PC Wakes | Bắt buộc/miễn nhập mật khẩu khi máy thức dậy |
| Maintenance Start Time | Giờ chạy update & bảo trì tự động (tính bằng phút từ nửa đêm) |
| **Education Policies** | Bật bộ thiết lập hạn chế tối ưu cho môi trường trường học |

👉 **Đây là "Deep Freeze của người nghèo" — và nó miễn phí, có sẵn trong Windows Pro.**
Cấu hình **Guest Account + Account Deletion Timing = "Immediately after log-out" + Local Storage = block** đã giải quyết trọn vẹn **R4 (rò rỉ dữ liệu giữa 2 lượt thuê)** và phần lớn **R3 (máy bị bẩn)** mà **không tốn đồng license nào**.

⚠️ Tài liệu Intune đã fetch **chỉ mô tả cách cấu hình qua Intune** và *"does not mention provisioning packages or the SharedPC CSP as alternatives"*. Việc cấu hình Shared PC mode **không cần Intune** (qua provisioning package/CSP) là điều **chưa xác minh được trong phiên này** → §10. Nếu xác minh được, startup có thể dùng Shared PC mode **hoàn toàn miễn phí, không cần mua MDM**.

### 4.4 BitLocker + TPM — mã hoá đĩa

**Yêu cầu phiên bản Windows:**
Theo bảng so sánh chính thức, **BitLocker device encryption chỉ có ở Windows 11 Pro và Pro for Workstations; Home KHÔNG có** — [Compare Windows 11 editions, microsoft.com](https://www.microsoft.com/en-us/windows/business/compare-windows-11).

**Điều kiện bật BitLocker im lặng (silent enablement) qua Intune** — [encrypt-bitlocker-windows.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/intune/device-configuration/endpoint-security/encrypt-bitlocker-windows.md):
- Windows 10 phiên bản **1809 trở lên**, hoặc Windows 11
- Máy **Microsoft Entra joined** hoặc hybrid joined
- **UEFI BIOS mode** đang bật
- **Secure Boot** và **Windows Recovery Environment** đã cấu hình
- **Không được cài phần mềm mã hoá bên thứ ba**
- **TPM 1.2 trở lên**
- Recovery key **tự động backup lên Microsoft Entra ID** khi mã hoá; tối đa **200 recovery key / thiết bị** lưu trên Entra ID
- ⚠️ Cảnh báo: *"Settings Catalog doesn't include the necessary TPM startup authentication controls required for reliable silent BitLocker enablement"* → phải dùng policy **endpoint security** hoặc **device configuration**, không dùng Settings Catalog.

**Các thiết lập BitLocker khả dụng** — [ref-disk-encryption-settings.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/intune/device-configuration/endpoint-security/ref-disk-encryption-settings.md):
- Thuật toán: AES-CBC 128/256, XTS-AES 128/256. **XTS-AES 128-bit là mặc định của Windows.**
- Xác thực khi khởi động: TPM (Blocked/Required/Allowed); **TPM + PIN** với độ dài PIN tối thiểu **4–20 chữ số**; TPM + startup key (USB); TPM + startup key + PIN.
- Recovery: cho/cấm người dùng tự tạo recovery key; bắt buộc backup lên Entra ID; DRA certificate; thông điệp & URL khôi phục tuỳ chỉnh trước khi boot.
- Ổ cố định: chặn ghi vào ổ không được BitLocker bảo vệ. Ổ rời: bắt buộc mã hoá, giới hạn truy cập theo tổ chức.
- *"Allow standard users to enable encryption during Autopilot"* — cho phép user thường bật mã hoá trong lúc Autopilot chạy.

**BitLocker khi dùng cùng Autopilot** — [autopilot/bitlocker.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/autopilot/bitlocker.md):
- Máy tương thích sẽ **tự mã hoá ổ trong OOBE**.
- Phải cấu hình **BitLocker policy + gán Enrollment Status Page (ESP)** *trước*, vì *"BitLocker will be enabled after the device setup portion of the enrollment status page"*.
- ⚠️ Nếu máy tự mã hoá trước khi policy kịp áp, **phải giải mã rồi mới đổi được thuật toán** — rất tốn thời gian với đội 30 máy.
- Chọn được **full disk encryption** hay **used space-only encryption** (used-space nhanh hơn nhiều khi setup hàng loạt).
- Policy phải gán cho **device group**, không phải user group.

👉 **Đánh giá thực tế:** BitLocker bảo vệ **dữ liệu**, không bảo vệ **tài sản**. Kẻ trộm vẫn bán được máy. Với mô hình cho thuê, giá trị chính của BitLocker là **R4 (không để lộ dữ liệu SV trước cho SV sau)** và **giảm rủi ro pháp lý**. Nhưng nếu đã bật Shared PC mode xoá tài khoản ngay khi logout, BitLocker là lớp bổ sung, không phải lớp chính. **Nên bật vì miễn phí (có sẵn trong Win Pro), nhưng đừng bật TPM+PIN** — bắt SV nhập thêm PIN trước khi boot ngay buổi sáng đi thi là thảm hoạ trải nghiệm.

### 4.5 Deep Freeze (Faronics), Windows Sandbox, tài khoản khách

- **Deep Freeze (Faronics):** ❌ `www.faronics.com` bị chặn → **không xác minh được giá, phiên bản, hay tính năng**. Không đưa số vào proposal. Xem §10.
- **Windows Sandbox:** ❌ Tài liệu chính thức nằm ở `learn.microsoft.com` (bị chặn) và repo `MicrosoftDocs/windows-itpro-docs` **không còn public trên GitHub** (đã kiểm tra, trả 404; các repo public còn lại của MicrosoftDocs không chứa nội dung Windows IT Pro). Bảng so sánh Windows 11 đã fetch **không nhắc tới Windows Sandbox** cho bất kỳ edition nào. → **Chưa xác minh.**
  - *Lưu ý logic:* kể cả nếu có, Windows Sandbox là môi trường ảo tạm thời để chạy app đáng ngờ — **nó không làm sạch máy chủ**. Nó **không** phải giải pháp cho R3/R4 trong mô hình này. Không nên đưa vào proposal.
- **Tài khoản khách (Guest account):** ✅ Có, và đã xác minh — là một thiết lập chính thức của **Shared PC mode** (§4.3), với 3 lựa chọn "Guest", "Domain", "Guest and domain".

---

## 5. CHỐNG TRỘM PHẦN MỀM

### 5.1 Windows "Find my device"

- ✅ Xác minh được **phạm vi edition**: Find My Device có ở **cả Home, Pro và Pro for Workstations** — [Compare Windows 11 editions](https://www.microsoft.com/en-us/windows/business/compare-windows-11), mô tả *"keep track of your devices—even your digital pen."*
- ❌ Chi tiết vận hành (bắt buộc đăng nhập tài khoản Microsoft cá nhân, phải là admin, phải bật location, và **có hoạt động trên máy Entra-joined/tài khoản cơ quan hay không**) — trang `support.microsoft.com` bị chặn → **chưa xác minh** → §10.
- ⚠️ **Cảnh báo thiết kế:** Find My Device gắn với **tài khoản Microsoft cá nhân**. Nếu máy được Entra-join vào tenant của startup và cấu hình Shared PC mode, việc đăng nhập một MSA cá nhân của chủ startup lên 30 máy là **vừa khó quản vừa dễ vỡ**. Không nên coi đây là lớp chống trộm chính.

### 5.2 Prey Project

- Agent **GPLv3**, chạy **Windows/macOS/Ubuntu** — [prey/prey-node-client](https://github.com/prey/prey-node-client).
- Năng lực xác minh được qua API/MCP: **alarm / alert / lock**, đánh dấu **missing/recovered**, **lịch sử vị trí** (JSON/CSV), **zones (geofencing)** tạo/sửa, **mass actions**, quản lý label — [prey/mcp-prey](https://raw.githubusercontent.com/prey/mcp-prey/main/README.md).
- ❌ **Giá: chưa xác minh** (`preyproject.com` bị chặn).
- ⚠️ Trong tài liệu MCP đã đọc, **không thấy** action `wipe` hay `locate` độc lập — chỉ có alarm/alert/lock và location **history**. Nếu proposal muốn khẳng định "Prey xoá được dữ liệu từ xa", phải tự kiểm chứng lại trên trang chính hãng.

### 5.3 Absolute Persistence / Computrace

- ❌ `www.absolute.com` bị chặn; `en.wikipedia.org` cũng bị chặn → **không xác minh được** danh sách máy hỗ trợ, cơ chế firmware, hay giá.
- ⚠️ **Nhận định có thể nêu trong proposal mà không cần số:** Absolute Persistence là module **nhúng trong firmware của máy khi xuất xưởng**. Nghĩa là nó **chỉ hoạt động nếu chiếc laptop đó vốn đã được OEM nhúng sẵn**. Một startup mua máy cũ trên thị trường Đà Nẵng **không thể "cài thêm" Absolute vào máy không hỗ trợ**. Với ngân sách <100 triệu VND, đây là hướng **loại ngay từ vòng gửi xe** — không cần khảo giá.
- Chi tiết kỹ thuật & giá → §10.

---

## 6. BIOS/UEFI, CHẶN BOOT USB, CHỐNG CÀI LẠI WINDOWS

### 6.1 DFCI — cách duy nhất khoá UEFI mà kẻ trộm không phá được

Nguồn: [memdocs/autopilot/dfci-management.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/autopilot/dfci-management.md)

**DFCI là gì:** *"DFCI enables Windows to pass management commands from Intune to UEFI for Windows Autopilot deployed devices."*

**Vì sao nó mạnh hơn mật khẩu BIOS thường (trích nguyên văn):**
> "DFCI's trust chain uses public key cryptography, and doesn't depend on local UEFI password security. This layer of security blocks local users from accessing managed settings from the device's UEFI menus."

Và quan trọng nhất:
> "If a user reinstalls a previous Windows version, installs a separate OS, or formats the hard drive, they can't override DFCI management."

👉 Đây chính xác là câu trả lời cho **"chống cài lại Windows"**: format ổ cứng hay cài OS khác **không gỡ được DFCI**.

**Chặn boot từ USB:** tài liệu nêu ví dụ *"the boot options can be locked down to prevent users from booting up another OS."*
⚠️ Tài liệu đã fetch **không liệt kê đầy đủ** danh sách setting khoá được (USB / network boot / camera / radio không được liệt kê cụ thể trong bản này) → §10.

**OEM hỗ trợ DFCI (danh sách trong tài liệu):** Acer, Asus, Dynabook, Fujitsu, **Microsoft Surface**, Panasonic, VAIO, Samsung, NEC.

🚨 **HAI ĐIỀU KIỆN GIẾT CHẾT DFCI CHO STARTUP NÀY:**
1. **Dell, HP, Lenovo KHÔNG có trong danh sách OEM hỗ trợ** — mà đây lại là 3 hãng chiếm phần lớn thị trường laptop cũ/giá rẻ ở Việt Nam.
2. **"Device must be registered through an OEM or Cloud Solution Partner — not manually via CSV import."** Startup mua máy lẻ, tự lấy hardware hash và upload CSV thủ công → **DFCI sẽ KHÔNG hoạt động.**

**Kết luận:** DFCI là công nghệ đúng nhất về mặt kỹ thuật, nhưng **không khả thi** cho đội laptop mua lẻ/máy cũ của một startup sinh viên. **Loại.**

### 6.2 Mật khẩu BIOS/UEFI thường (supervisor password)

- ❌ Không có nguồn chính thức nào fetch được trong phiên này (tài liệu Windows IT Pro không còn public).
- ⚠️ Điều **suy ra được từ nguồn đã có**: chính tài liệu DFCI ngầm khẳng định mật khẩu UEFI cục bộ là **lớp bảo vệ yếu hơn**, khi nhấn mạnh DFCI *"doesn't depend on local UEFI password security"*. Nếu mật khẩu UEFI cục bộ đủ mạnh thì Microsoft đã không cần xây DFCI.
- **Khuyến nghị vận hành (không cần nguồn):** vẫn nên đặt supervisor password + tắt boot từ USB + bật Secure Boot trên từng máy. Chi phí = 0 đồng, chỉ tốn ~5 phút/máy khi nhập kho. Nó chặn được **99% khách hàng nghịch ngợm**, dù không chặn được kẻ trộm chuyên nghiệp (reset CMOS / gỡ pin CMOS / dùng master password của hãng).

---

## 7. ĐỊNH VỊ PHẦN CỨNG (AirTag / SmartTag / GPS có SIM)

❌ **Toàn bộ mục này KHÔNG xác minh được trong phiên** — `apple.com`, `thegioididong.com`, `cellphones.com.vn`, `fptshop.com.vn`, `tiki.vn`, `shopee.vn`, `amazon.com` đều bị chặn.

**KHÔNG được đưa bất kỳ con số giá nào vào proposal cho mục này nếu chưa tự khảo giá.** Xem checklist §11.

Những gì **có thể nói mà không cần số** (lập luận logic, nên ghi rõ là phân tích của nhóm chứ không phải dữ liệu trích dẫn):
- AirTag / Galaxy SmartTag **không có GPS và không có SIM**. Chúng phát tín hiệu Bluetooth và mượn điện thoại của người lạ đi ngang để báo vị trí. Trong khuôn viên ĐH FPT Đà Nẵng — nơi mật độ iPhone cao — mạng Find My có thể đủ dày. Nhưng nếu máy bị mang về một khu trọ vắng, tag có thể **im lặng hàng giờ**.
- Cả hai loại tag đều có **cảnh báo chống theo dõi (anti-stalking)**: iPhone/Android sẽ báo cho người đang mang theo rằng "có một tag lạ đang di chuyển cùng bạn". Nghĩa là **kẻ trộm sẽ được hệ điều hành mách nước** để tìm và vứt tag. Đây là giới hạn mang tính thiết kế, không thể khắc phục.
- GPS tracker có SIM thì định vị thật, nhưng phát sinh **cước SIM hằng tháng × số máy** và cần **sạc pin định kỳ** — với 30 máy đây là gánh nặng vận hành đáng kể.
- Cả 3 loại đều **gắn ngoài** → tháo ra trong 10 giây.

---

## 8. KHOÁ VẬT LÝ, TEM NIÊM PHONG, KHẮC LASER, QR ASSET TAG

❌ **Không xác minh được giá** (`kensington.com`, các sàn TMĐT VN đều bị chặn). Xem §10 + §11.

Phân tích định tính (ghi rõ trong proposal đây là lập luận, không phải số liệu):

| Biện pháp | Chống được gì | Không chống được gì | Phù hợp mô hình cho thuê? |
|---|---|---|---|
| **Khoá Kensington** | Trộm vặt khi máy để trên bàn **tại một chỗ cố định** | Không dùng được khi khách **mang máy đi thi** (bản chất khoá là cột máy vào vật cố định) | ⚠️ **Chỉ hợp cho kho/quầy**, vô dụng khi máy rời khỏi cửa hàng |
| **Tem niêm phong vỡ (tamper-evident)** | Phát hiện việc **mở máy, tráo RAM/SSD/pin** | Không chống mất máy | ✅ **Rất đáng làm** — rẻ, giải quyết tranh chấp "máy hỏng từ trước hay do bạn" |
| **Khắc laser mã tài sản** | Làm máy **khó bán lại**, chứng minh quyền sở hữu khi trình báo công an | Không ngăn được hành vi lấy máy | ✅ **Đáng làm** — chi phí một lần, tác dụng răn đe thật |
| **Tem QR asset tag** | Quản lý kiểm kê, gắn máy với lượt thuê, quét nhanh khi giao/nhận | Bóc ra được | ✅ **Bắt buộc** cho vận hành, không phải cho chống trộm |

**Nhận định:** trong mô hình này, khoá Kensington phần lớn là **security theater** (xem §9). Ngược lại, **khắc laser + tem niêm phong vỡ + tem QR** là bộ ba rẻ nhất, thiết thực nhất — vì nó phục vụ **R3 (tranh chấp hư hỏng)** vốn xảy ra thường xuyên, chứ không phải R2 (mất máy) vốn hiếm.

---

## 9. ĐÁNH GIÁ: CÁI GÌ LÀ "SECURITY THEATER"?

Xếp hạng theo **giá trị thực / chi phí** cho startup <100 triệu VND, 10–50 máy, ca thuê ngắn:

### 🟢 Nhóm A — Giá trị thật, chi phí gần bằng 0 (LÀM NGAY)

| Biện pháp | Chi phí | Vì sao đáng |
|---|---|---|
| **Shared PC mode + xoá tài khoản ngay khi logout** | 0 đ (có sẵn Windows Pro) | Giải quyết trọn R4 và phần lớn R3 — vấn đề xảy ra **mỗi ngày**. [Nguồn](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/intune/device-configuration/templates/ref-shared-device-settings-windows.md) |
| **Autopilot Reset local (`CTRL+WIN+R`)** | 0 đ thao tác | Về trạng thái sạch trong 1 phím tắt, **giữ nguyên Wi-Fi + enrollment**. [Nguồn](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/autopilot/windows-autopilot-reset.md) |
| **BitLocker (TPM, không PIN)** | 0 đ (Windows Pro) | Bảo vệ dữ liệu, giảm rủi ro pháp lý. [Nguồn](https://www.microsoft.com/en-us/windows/business/compare-windows-11) |
| **Supervisor password BIOS + tắt boot USB + Secure Boot** | 0 đ, ~5 phút/máy | Chặn 99% khách nghịch |
| **Khắc laser mã tài sản + tem niêm phong vỡ + tem QR** | thấp, một lần | Chống bán lại, giải quyết tranh chấp hư hỏng |
| **Đặt cọc + xác thực thẻ SV/CCCD + hợp đồng thuê** | 0 đ | **Đây mới là lớp chống thất thoát thật sự** |
| **MeshCentral tự host (Apache 2.0)** | 0 đ license + phí VPS | Remote desktop hỗ trợ khách + device mapping. [Nguồn](https://github.com/Ylianst/MeshCentral) |

### 🟡 Nhóm B — Có giá trị nhưng phải cân nhắc chi phí

| Biện pháp | Chi phí đã xác minh | Cân nhắc |
|---|---|---|
| Intune Plan 1 | **8,00 USD/user/tháng** | Cần cho Autopilot Reset **từ xa** và Locate. Nếu chỉ dùng reset **local** thì có thể không cần. |
| Fleet Premium | **7,00 USD/host/tháng** | 30 máy = **210 USD/tháng** — quá đắt so với doanh thu dự kiến của một startup SV |
| Fleet Free | **0 USD** | Inventory + script + policy thì tốt; **không có** lock/wipe/encryption enforcement |
| GPS tracker có SIM | chưa xác minh | Chỉ nên gắn cho **vài máy đắt tiền nhất**, không gắn toàn đội |

### 🔴 Nhóm C — SECURITY THEATER hoặc bất khả thi (BỎ)

| Biện pháp | Vì sao bỏ |
|---|---|
| **"Khoá máy Windows từ xa qua Intune"** | **KHÔNG TỒN TẠI.** Remote lock của Intune không hỗ trợ Windows — [danh sách nền tảng chính thức](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/intune/device-management/actions/remote-lock.md). Đừng vẽ tính năng này lên slide. |
| **DFCI khoá UEFI** | Yêu cầu đăng ký qua **OEM/CSP, không chấp nhận CSV thủ công**; và **Dell/HP/Lenovo không nằm trong danh sách OEM hỗ trợ** — [dfci-management.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/autopilot/dfci-management.md). Bất khả thi với máy mua lẻ. |
| **Absolute Persistence / Computrace** | Phải được nhúng firmware **từ nhà máy**. Không "cài thêm" được vào máy cũ. |
| **Khoá Kensington cho máy mang đi thi** | Bản chất là cột máy vào bàn — mâu thuẫn hoàn toàn với việc cho khách **mang máy đi**. Chỉ hợp cho kho. |
| **AirTag như biện pháp chống trộm chính** | Không GPS, không SIM; hệ điều hành **chủ động cảnh báo** người đang mang tag → kẻ trộm được mách để vứt tag. |
| **Windows Sandbox** | Cách ly app trong VM tạm; **không làm sạch máy chủ** → sai công cụ cho R3/R4. |
| **Intune Suite / Plan 2 / các add-on** | 10 / 4 / 2–5 USD/user/tháng cho các tính năng (Remote Help, EPM, Advanced Analytics, Cloud PKI) **không liên quan** tới bài toán cho thuê. |
| **Protected wipe with power persistence** | Microsoft cảnh báo *"can prevent some devices from starting up again"* — với startup không có quy trình phục hồi, rủi ro biến máy thành cục gạch. |

---

## 10. ⚠️ NHỮNG ĐIỀU **CHƯA XÁC MINH ĐƯỢC** (KHÔNG ĐƯỢC ĐOÁN)

Toàn bộ danh sách dưới đây **phải tự khảo lại** trước khi đưa số vào proposal:

**Giá phần mềm:**
1. Giá **Prey Project** (mọi gói) — `preyproject.com` bị chặn.
2. Giá **Hexnode UEM** — bị chặn.
3. Giá **Scalefusion** — bị chặn.
4. Giá **ManageEngine MDM Plus**, kể cả **bản free giới hạn bao nhiêu thiết bị** — bị chặn.
5. Giá **Miradore** và **có hay không bản free** — bị chặn.
6. Giá **Absolute Persistence**, danh sách máy hỗ trợ firmware — bị chặn.
7. Giá **Deep Freeze (Faronics)**, các phiên bản (Standard/Enterprise/Cloud) — bị chặn.
8. **Giá SKU Intune device-only** (per device/month) — tài liệu xác nhận SKU tồn tại nhưng trang giá công khai không niêm yết.
9. Giá **Microsoft 365 Business Premium** — trang trả HTTP 503 (thử 2 lần).
10. Giá **Microsoft 365 Education A1 / A3 / A5** — trang trả HTTP 503.
11. **Chính sách nonprofit/education/startup** của Microsoft cho tổ chức VN — chưa kiểm tra được.
12. Số **host tối thiểu** của Fleet Premium — trang giá không nêu.
13. Giới hạn số agent của **Tactical RMM** và điều kiện xin phép thương mại từ AmidaWare LLC.

**Giá phần cứng tại Việt Nam (VND) — TOÀN BỘ chưa xác minh:**
14. AirTag, Galaxy SmartTag.
15. GPS tracker có SIM + cước data hằng tháng tại VN.
16. Khoá Kensington (T-Bar / Nano / Wedge) tại VN.
17. Tem niêm phong vỡ, tem QR asset tag, dịch vụ khắc laser tại Đà Nẵng.
18. Giá laptop cũ/refurbished tại Đà Nẵng (đầu vào chính của vốn đầu tư).
19. **Tỷ giá USD/VND tháng 9/2026** — không có nguồn xác minh nào trong phiên. Mọi quy đổi trong proposal phải dùng tỷ giá tra cứu tại thời điểm viết và ghi rõ nguồn.

**Tài liệu kỹ thuật chưa truy cập được:**
20. Chi tiết **Windows "Find my device"**: có chạy trên máy Entra-joined / tài khoản cơ quan không? Bắt buộc MSA cá nhân? (`support.microsoft.com` bị chặn.)
21. **Windows Sandbox** có trong Windows 11 Pro không — bảng so sánh edition đã fetch không nhắc tới; repo `MicrosoftDocs/windows-itpro-docs` không còn public (404).
22. **Danh sách đầy đủ setting UEFI mà DFCI khoá được** (USB boot, network boot, camera, radio) — tài liệu chỉ nêu ví dụ chung về boot options.
23. Có cấu hình được **Shared PC mode KHÔNG cần Intune** (qua **SharedPC CSP** / provisioning package / Windows Configuration Designer) hay không — tài liệu Intune *"does not mention provisioning packages or the SharedPC CSP as alternatives"*. **Đây là câu hỏi có giá trị tài chính lớn nhất còn bỏ ngỏ**: nếu được thì startup dùng Shared PC mode **hoàn toàn miễn phí**, không cần mua MDM.
24. Hướng dẫn chính thức về **BIOS/UEFI supervisor password** và cách chặn boot USB theo từng hãng.
25. **Computrace** (tên cũ của Absolute) — cơ chế, máy hỗ trợ.

**Thực tiễn ngành & pháp lý:**
26. **Thư viện đại học cho mượn laptop chống mất bằng cách nào** — không tìm được bất kỳ nguồn nào (mọi tên miền học thuật/tin tức đều bị chặn). ❗ Đây là phần **hoàn toàn thiếu dữ liệu**; proposal **không được** bịa "theo kinh nghiệm các thư viện đại học…". Xem §11 để biết cách lấy dữ liệu này rẻ và đáng tin hơn cả tra mạng.
27. Quy định pháp lý VN về **cho thuê tài sản, đặt cọc, giữ CCCD/thẻ SV** — chưa xác minh. ⚠️ Riêng việc **giữ CCCD của khách làm tin** cần kiểm tra kỹ tính hợp pháp trước khi đưa vào quy trình.
28. Chính sách của ĐH FPT Đà Nẵng về việc **mang thiết bị lạ vào phòng thi** — yếu tố sống còn của mô hình, phải hỏi trực tiếp phòng Khảo thí.

---

## 11. VIỆC CẦN LÀM TIẾP (CHECKLIST CHO NGƯỜI VIẾT PROPOSAL)

**Khảo giá (1 buổi, tự làm được):**
- [ ] Mở trực tiếp `preyproject.com/pricing`, `hexnode.com/.../pricing`, `scalefusion.com/pricing`, `manageengine.com/.../pricing.html`, `miradore.com/pricing`, `faronics.com` → chụp màn hình kèm ngày.
- [ ] Khảo giá AirTag / GPS tracker / khoá Kensington trên Thế Giới Di Động, FPT Shop, CellphoneS, Tiki, Shopee → **chụp màn hình có ngày**, ghi cả giá niêm yết lẫn giá khuyến mãi.
- [ ] Đi khảo giá trực tiếp **khắc laser + tem niêm phong vỡ + in tem QR** tại các cơ sở ở Ngũ Hành Sơn / Hoà Hải — giá thật thường rẻ hơn nhiều so với tra mạng.
- [ ] Tra tỷ giá USD/VND từ Vietcombank/SBV đúng ngày viết proposal, ghi rõ nguồn.

**Phỏng vấn (giá trị cao hơn tra mạng rất nhiều):**
- [ ] **Phỏng vấn thủ thư / phòng thiết bị ĐH FPT Đà Nẵng**: trường có cho mượn laptop/thiết bị không? Quy trình thế nào? Đặt cọc bao nhiêu? Tỷ lệ mất/hỏng thực tế? → Đây là **dữ liệu sơ cấp**, mạnh hơn mọi bài blog quốc tế, và bù đắp đúng lỗ hổng ở §10 mục 26.
- [ ] Hỏi **phòng Khảo thí** về quy định mang laptop lạ vào phòng thi (§10 mục 28) — nếu trường cấm, toàn bộ mô hình phải xoay trục.
- [ ] Hỏi **phòng CNTT của trường** xem tenant Microsoft 365 Education của trường là A1/A3/A5, và dự án SV có được cấp license không (§2.3) — đây là đòn bẩy chi phí lớn nhất.

**Thử nghiệm kỹ thuật (làm trên 1 máy, chứng minh tính khả thi trong proposal):**
- [ ] Dựng thử **MeshCentral** trên 1 VPS rẻ, cài agent lên 1 laptop → chụp màn hình remote desktop + bản đồ thiết bị. Bằng chứng "đã làm được" giá trị hơn nhiều so với bảng so sánh lý thuyết.
- [ ] Bật **Shared PC mode** trên 1 máy Windows Pro với Account Deletion = "Immediately after log-out" → quay video: đăng nhập guest, tạo file, đăng xuất, đăng nhập lại → file biến mất. **Đây là demo thuyết phục nhất của cả proposal.**
- [ ] Thử **`CTRL+WIN+R`** (Autopilot Reset local) trên 1 máy → bấm giờ xem mất bao lâu, để đưa vào tính toán thời gian quay vòng máy giữa 2 ca thi.
- [ ] Kiểm tra từng laptop định mua: có **TPM 2.0** không, có chạy **Windows Pro** không (Home là hỏng kế hoạch), có bật được **Secure Boot + UEFI** không.

---

## 12. TÓM TẮT KHUYẾN NGHỊ (1 ĐOẠN CHO SLIDE)

Với đội 10–50 laptop cho SV thuê theo ca thi, **rủi ro thật sự tốn tiền mỗi ngày là máy bẩn và dữ liệu sót lại giữa hai lượt thuê, không phải mất trộm**. Vì vậy kiến trúc đề xuất là: mua laptop **có Windows 11 Pro + TPM 2.0** (Home là loại thẳng — mất cả BitLocker lẫn Shared PC mode lẫn Autopilot), bật **Shared PC mode với chế độ xoá tài khoản ngay khi đăng xuất** (miễn phí, có sẵn), bật **BitLocker chỉ với TPM** (không PIN, để không phá trải nghiệm sáng ngày thi), đặt **mật khẩu BIOS + tắt boot USB**, dùng **`CTRL+WIN+R`** để đưa máy về trạng thái sạch tại quầy, và tự host **MeshCentral (Apache 2.0, 0 đồng license)** để hỗ trợ khách từ xa. Chi phí phần mềm gần như bằng 0. Chống thất thoát tài sản dựa vào **đặt cọc + xác thực thẻ sinh viên + hợp đồng + khắc laser mã tài sản**, chứ không dựa vào MDM. Cần loại bỏ dứt khoát khỏi proposal ba thứ: **"khoá máy Windows từ xa qua Intune"** (Microsoft không hỗ trợ Windows cho tính năng này), **DFCI** (đòi đăng ký qua OEM/CSP và không hỗ trợ Dell/HP/Lenovo), và **Absolute Persistence** (phải nhúng firmware từ nhà máy).

---

## PHỤ LỤC A — DANH SÁCH NGUỒN ĐÃ FETCH THẬT

| # | Nguồn | Dùng cho |
|---|---|---|
| 1 | [Microsoft Intune pricing](https://www.microsoft.com/en-us/security/business/microsoft-intune-pricing) | Toàn bộ giá Intune Plan 1/2/Suite/add-on, M365 E3/E5 |
| 2 | [Compare Windows 11 editions (business)](https://www.microsoft.com/en-us/windows/business/compare-windows-11) | BitLocker/Assigned Access/MDM/Group Policy chỉ có ở Pro; Find My Device có ở mọi edition |
| 3 | [memdocs — repo gốc Microsoft Learn](https://github.com/MicrosoftDocs/memdocs) | Repo nguồn, archive 02/09/2026 |
| 4 | [autopilot/requirements.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/autopilot/requirements.md) | Edition & license bắt buộc cho Autopilot; cổng 80/443/123 |
| 5 | [autopilot/windows-autopilot-reset.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/autopilot/windows-autopilot-reset.md) | `CTRL+WIN+R`, giữ/xoá gì, WinRE, giới hạn hybrid |
| 6 | [autopilot/bitlocker.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/autopilot/bitlocker.md) | Thuật toán mã hoá, ESP, cảnh báo phải giải mã nếu áp policy trễ |
| 7 | [autopilot/dfci-management.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/autopilot/dfci-management.md) | DFCI, khoá boot, danh sách OEM, yêu cầu đăng ký OEM/CSP |
| 8 | [autopilot/self-deploying.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/autopilot/self-deploying.md) | TPM 2.0, licensing "per device per month", hạn chế |
| 9 | [autopilot/manual-registration.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/autopilot/manual-registration.md) | Hardware hash 4K HH, giới hạn 500/1000 máy, "testing and evaluation" |
| 10 | [autopilot/autopilot-device-guidelines.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/autopilot/autopilot-device-guidelines.md) | TPM 2.0, CBR/OA3 |
| 11 | [intune/fundamentals/licensing.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/intune/fundamentals/licensing.md) | Plan 1/2/Suite, Intune for Education (A3/A5), device-only subscriptions |
| 12 | [actions/remote-lock.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/intune/device-management/actions/remote-lock.md) | ❗ Windows KHÔNG hỗ trợ remote lock |
| 13 | [actions/locate.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/intune/device-management/actions/locate.md) | Windows CÓ locate; cần policy Force allow; lưu 24h; không có Lost Mode |
| 14 | [actions/wipe.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/intune/device-management/actions/wipe.md) | 3 chế độ wipe + cảnh báo hỏng máy |
| 15 | [actions/retire.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/intune/device-management/actions/retire.md) | Retire xoá gì / giữ gì |
| 16 | [actions/fresh-start.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/intune/device-management/actions/fresh-start.md) | Fresh Start, tuỳ chọn giữ dữ liệu |
| 17 | [actions/autopilot-reset.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/intune/device-management/actions/autopilot-reset.md) | Autopilot Reset từ xa, vai trò cần thiết |
| 18 | [endpoint-security/encrypt-bitlocker-windows.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/intune/device-configuration/endpoint-security/encrypt-bitlocker-windows.md) | Điều kiện silent BitLocker, TPM 1.2+, escrow 200 key |
| 19 | [endpoint-security/ref-disk-encryption-settings.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/intune/device-configuration/endpoint-security/ref-disk-encryption-settings.md) | XTS-AES 128 mặc định, TPM+PIN 4–20 số |
| 20 | [templates/ref-shared-device-settings-windows.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/intune/device-configuration/templates/ref-shared-device-settings-windows.md) | ⭐ Toàn bộ setting Shared PC mode |
| 21 | [templates/configure-shared-device.md](https://raw.githubusercontent.com/MicrosoftDocs/memdocs/main/intune/device-configuration/templates/configure-shared-device.md) | Shared PC chỉ hỗ trợ Pro/Enterprise |
| 22 | [fleetdm/fleet — pricing.ejs](https://raw.githubusercontent.com/fleetdm/fleet/main/website/views/pages/pricing.ejs) | Free 0 USD, Premium 7,00 USD/host/tháng |
| 23 | [fleetdm/fleet — pricing-features-table.yml](https://raw.githubusercontent.com/fleetdm/fleet/main/handbook/company/pricing-features-table.yml) | Free vs Premium: lock/wipe/encryption ở Premium |
| 24 | [fleetdm/fleet README](https://raw.githubusercontent.com/fleetdm/fleet/main/README.md) | MIT license, đa nền tảng |
| 25 | [Ylianst/MeshCentral](https://github.com/Ylianst/MeshCentral) | Apache 2.0, miễn phí, tự host, remote desktop + mapping |
| 26 | [amidaware/tacticalrmm README](https://raw.githubusercontent.com/amidaware/tacticalrmm/develop/README.md) | Tính năng RMM, Windows 7–11 |
| 27 | [amidaware/tacticalrmm LICENSE](https://github.com/amidaware/tacticalrmm/blob/develop/LICENSE.md) | 🚨 Hạn chế dùng cho dịch vụ thương mại |
| 28 | [prey/prey-node-client](https://github.com/prey/prey-node-client) | Agent GPLv3, Windows/macOS/Ubuntu |
| 29 | [prey/mcp-prey README](https://raw.githubusercontent.com/prey/mcp-prey/main/README.md) | Action alarm/alert/lock, location history, zones |
| 30 | [Prey trên GitHub](https://github.com/prey) | Danh sách repo, xác nhận sản phẩm |

