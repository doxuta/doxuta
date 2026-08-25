<div align="center">

### Xuan Tai Doan · 도안 쑤언 타이

**Software engineer in Da Nang, Viet Nam.** I build products end to end and the infrastructure underneath them.

Vietnamese (native) · English (C1) · 한국어 (advanced) · 日本語 (upper-intermediate)

</div>

---

**Right now:** sole contract engineer on *Nexus*, a multi-tenant, metadata-driven core platform in **Go + MySQL** that generates business applications — CRM, LMS, ticketing, ERP — from metadata, for an EdTech company. Most of it is written by AI agents behind a human review gate on infrastructure I run myself; none of it is merged unreviewed.

**Before that:** BSc Software Engineering, FPT University (Dec 2025), Bridge Software Engineer track with a Korean focus, and a bridge-engineer internship at FPT Software liaising with Korean clients.

### What I've built

| | |
|---|---|
| **[TEdu](https://github.com/doxuta/tedu)** · [live](https://tedu-app.netlify.app) | A teaching ledger for solo tutors — attendance, self-calculating tuition, VietQR receipts, an offline-first AI assistant driven by natural Vietnamese. The whole web app is **one HTML file**. In production with its first tutor. VI/EN/KO. |
| **[TAIELTS](https://github.com/doxuta/TAIELTS)** | A source-first IELTS platform: every lesson cites an approved source, and the Gemini scorer may only cite those. Next.js 14 + Prisma, dressed as a Vietnamese school notebook. |
| **[amlich](https://github.com/doxuta/amlich)** | Vietnamese & Korean lunisolar calendars computed from **new-moon astronomy**, not lookup tables — zero deps, golden-validated against 59,810 production conversions, fuzzed 38.9M runs. Ships an MCP server so agents stop guessing when Tết is. |
| **[caudao](https://github.com/doxuta/caudao)** | A **fail-closed spending circuit breaker** for autonomous agents: meters tokens live from the SSE stream and cuts the connection mid-response when the budget is gone. Named after the cầu dao on every Vietnamese wall. |
| **[mcpvet](https://github.com/doxuta/mcpvet)** | `go vet` for MCP servers — lockfile your agent's tool surface so CI catches silent schema and description drift, plus JSON-Schema-driven fuzzing of tool inputs. |

Every repo above has tests and green CI. The Go ones are fuzzed; `amlich`'s fuzzer found three defects in the classical reference algorithm it was ported from.

### How I work

I build with AI agents and say so. What I keep for myself is the part that matters: choosing the approach, reviewing every change, and writing the tests that prove the output is right rather than merely plausible. The fuzz corpora and golden files in my repos exist because that is how I check an agent's work.

### Reach me

[xuantai.net@gmail.com](mailto:xuantai.net@gmail.com) · [LinkedIn](https://www.linkedin.com/in/doan-matthew)

<details>
<summary><b>Tiếng Việt</b></summary>

<br>

Kỹ sư phần mềm ở Đà Nẵng. Tôi làm sản phẩm từ đầu đến cuối, và làm cả hạ tầng bên dưới nó.

**Hiện tại:** kỹ sư hợp đồng duy nhất của *Nexus* — nền tảng lõi đa tenant, vận hành bằng metadata, viết bằng **Go + MySQL**, sinh ra các ứng dụng nghiệp vụ (CRM, LMS, ticketing, ERP) từ metadata cho một công ty EdTech. Phần lớn code do AI agent viết, nhưng đi qua cổng review của người; không dòng nào được merge mà chưa đọc.

**Học vấn:** Cử nhân Kỹ thuật phần mềm, Đại học FPT (12/2025), chuyên ngành Bridge Software Engineer hướng Hàn Quốc; từng thực tập BrSE tại FPT Software, làm cầu nối với khách hàng Hàn.

**Sản phẩm:** [TEdu](https://tedu-app.netlify.app) — sổ tay quản lý dạy học cho gia sư, toàn bộ web app nằm trong **một file HTML**, đang chạy thật với người dùng đầu tiên. [TAIELTS](https://github.com/doxuta/TAIELTS) — nền tảng luyện IELTS "nguồn trước, bài sau". [amlich](https://github.com/doxuta/amlich) — thư viện Go tính âm lịch Việt–Hàn bằng thiên văn. [caudao](https://github.com/doxuta/caudao) — cầu dao ngắt chi phí cho AI agent. [mcpvet](https://github.com/doxuta/mcpvet) — kiểm thử hợp đồng cho MCP server.

**Cách làm việc:** tôi dùng AI agent và nói thẳng điều đó. Phần tôi giữ lại cho mình là phần quan trọng: chọn hướng đi, review từng thay đổi, và viết test để chứng minh kết quả đúng chứ không chỉ trông có vẻ đúng.

</details>

<details>
<summary><b>한국어</b></summary>

<br>

베트남 다낭의 소프트웨어 엔지니어입니다. 제품을 처음부터 끝까지 만들고, 그 아래의 인프라까지 직접 다룹니다.

**현재:** EdTech 기업을 위한 멀티테넌트 메타데이터 기반 코어 플랫폼 *Nexus* 의 단독 계약 엔지니어입니다. **Go + MySQL** 로 작성되었으며, 메타데이터로부터 CRM·LMS·티케팅·ERP 같은 업무 애플리케이션을 생성합니다. 대부분의 코드는 AI 에이전트가 작성하지만, 사람의 리뷰 게이트를 반드시 거칩니다.

**학력:** FPT 대학교 소프트웨어공학 학사(2025년 12월), 한국 방향 브리지 SE 트랙. FPT Software에서 브리지 엔지니어 인턴으로 한국 고객사와의 커뮤니케이션을 담당했습니다.

**만든 것:** [TEdu](https://tedu-app.netlify.app) — 개인 교습 강사를 위한 관리 장부, 웹 앱 전체가 **HTML 파일 하나**이며 실제 사용자와 함께 운영 중입니다. [TAIELTS](https://github.com/doxuta/TAIELTS) — 출처 우선 IELTS 학습 플랫폼. [amlich](https://github.com/doxuta/amlich) — 천문 계산 기반 베트남·한국 음력 Go 라이브러리(설날과 Tết이 어긋나는 해를 계산합니다). [caudao](https://github.com/doxuta/caudao) — AI 에이전트용 비용 차단기. [mcpvet](https://github.com/doxuta/mcpvet) — MCP 서버 계약 테스트 도구.

**작업 방식:** AI 에이전트를 사용하며, 이를 숨기지 않습니다. 제가 직접 맡는 것은 방향을 정하고, 모든 변경을 리뷰하고, 결과가 그럴듯한 것이 아니라 실제로 옳다는 것을 증명하는 테스트를 쓰는 일입니다.

</details>
