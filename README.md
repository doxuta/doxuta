<div align="center">

### Xuan Tai Doan · 도안 쑤언 타이

**Software engineer in Da Nang, Viet Nam.** I build products end to end and the infrastructure underneath them.

Vietnamese (native) · English (C1) · 한국어 (advanced) · 日本語 (upper-intermediate)

</div>

---

**Right now:** building [*Nexus*](https://github.com/doxuta/nexus), an open-source, agent-native platform for business apps in **Go + MySQL**. Agents never write application code: they propose changes to a typed, versioned, permissioned model, and a person reviews, publishes and can roll back every change. Most of it is written by AI agents behind that same review gate; each slice is checked by an independent verifier before it merges. The story of how it is built: [Turning the lights back on](https://github.com/doxuta/nexus/blob/main/docs/writeup/turning-the-lights-back-on.md).

**Before that:** BSc Software Engineering, FPT University (Dec 2025), Bridge Software Engineer track with a Korean focus, and a bridge-engineer internship at FPT Software liaising with Korean clients.

### What I've built

| | |
|---|---|
| **[Nexus](https://github.com/doxuta/nexus)** · [write-up](https://github.com/doxuta/nexus/blob/main/docs/writeup/turning-the-lights-back-on.md) | An **agent-native platform for business apps**: agents propose typed changes (tables, fields, layouts, workflows, access), people review the diff, publish, and roll back. Per-tenant, per-row access proven as a non-admin user; an MCP server so Claude Code can design apps under "agents propose, humans dispose". CI replays an 18-step demo in Chrome on every change from a recorded model run, so it needs no key. Measured, not claimed: builder-bench pass@1 0.85 (`claude-haiku-5-5`, 60 attempts), MCP tool-use eval 5/5, and a harness eval that honestly shows no effect yet. |
| **[TEdu](https://github.com/doxuta/tedu)** · [live](https://tedu-app.netlify.app) | A teaching ledger for solo tutors — attendance, self-calculating tuition, VietQR receipts, an offline-first AI assistant driven by natural Vietnamese. The whole web app is **one HTML file**. In production with its first tutor. VI/EN/KO. |
| **[TAIELTS](https://github.com/doxuta/TAIELTS)** | A source-first IELTS platform: every lesson cites an approved source, and the Gemini scorer may only cite those. Next.js 14 + Prisma, dressed as a Vietnamese school notebook. |
| **[amlich](https://github.com/doxuta/amlich)** | Vietnamese & Korean lunisolar calendars computed from **new-moon astronomy**, not lookup tables — zero deps, golden-validated against 59,810 production conversions, fuzzed 38.9M runs. Ships an MCP server so agents stop guessing when Tết is. |
| **[ai-factory-kit](https://github.com/doxuta/ai-factory-kit)** | The **operating system for AI-driven development** distilled from building Nexus: spec-first flow, executable gates, adversarial verification, a constitution template, and a retro-fit playbook for brownfield repos. Every rule in it was paid for on a production codebase. |
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

**Hiện tại:** xây [*Nexus*](https://github.com/doxuta/nexus), nền tảng mã nguồn mở cho ứng dụng nghiệp vụ, thiết kế cho AI agent, viết bằng **Go + MySQL**. Agent không viết code ứng dụng: agent đề xuất thay đổi trên một mô hình có kiểu, có phiên bản, có phân quyền; người duyệt, xuất bản và có thể quay lại từng thay đổi. Phần lớn code do AI agent viết, đi qua cùng cổng review đó; mỗi phần đều được một verifier độc lập kiểm trước khi merge.

**Học vấn:** Cử nhân Kỹ thuật phần mềm, Đại học FPT (12/2025), chuyên ngành Bridge Software Engineer hướng Hàn Quốc; từng thực tập BrSE tại FPT Software, làm cầu nối với khách hàng Hàn.

**Sản phẩm:** [Nexus](https://github.com/doxuta/nexus) — nền tảng ứng dụng nghiệp vụ cho AI agent: agent đề xuất, người quyết. [TEdu](https://tedu-app.netlify.app) — sổ tay quản lý dạy học cho gia sư, toàn bộ web app nằm trong **một file HTML**, đang chạy thật với người dùng đầu tiên. [TAIELTS](https://github.com/doxuta/TAIELTS) — nền tảng luyện IELTS "nguồn trước, bài sau". [amlich](https://github.com/doxuta/amlich) — thư viện Go tính âm lịch Việt–Hàn bằng thiên văn. [ai-factory-kit](https://github.com/doxuta/ai-factory-kit) — bộ khung vận hành phát triển bằng AI (spec-first, cổng kiểm chạy được). [caudao](https://github.com/doxuta/caudao) — cầu dao ngắt chi phí cho AI agent. [mcpvet](https://github.com/doxuta/mcpvet) — kiểm thử hợp đồng cho MCP server.

**Cách làm việc:** tôi dùng AI agent và nói thẳng điều đó. Phần tôi giữ lại cho mình là phần quan trọng: chọn hướng đi, review từng thay đổi, và viết test để chứng minh kết quả đúng chứ không chỉ trông có vẻ đúng.

</details>

<details>
<summary><b>한국어</b></summary>

<br>

베트남 다낭의 소프트웨어 엔지니어입니다. 제품을 처음부터 끝까지 만들고, 그 아래의 인프라까지 직접 다룹니다.

**현재:** 오픈소스 업무 애플리케이션 플랫폼 [*Nexus*](https://github.com/doxuta/nexus) 를 만들고 있습니다. **Go + MySQL** 기반이며 AI 에이전트를 위해 설계되었습니다. 에이전트는 애플리케이션 코드를 쓰지 않고, 타입·버전·권한이 있는 모델에 대한 변경을 제안합니다. 사람이 그 변경을 검토하고 게시하며, 언제든 되돌릴 수 있습니다. 대부분의 코드는 AI 에이전트가 작성하지만, 모든 변경은 독립 검증을 거친 뒤에만 병합됩니다.

**학력:** FPT 대학교 소프트웨어공학 학사(2025년 12월), 한국 방향 브리지 SE 트랙. FPT Software에서 브리지 엔지니어 인턴으로 한국 고객사와의 커뮤니케이션을 담당했습니다.

**만든 것:** [Nexus](https://github.com/doxuta/nexus) — AI 에이전트를 위한 업무 앱 플랫폼(에이전트는 제안하고, 사람이 결정합니다). [TEdu](https://tedu-app.netlify.app) — 개인 교습 강사를 위한 관리 장부, 웹 앱 전체가 **HTML 파일 하나**이며 실제 사용자와 함께 운영 중입니다. [TAIELTS](https://github.com/doxuta/TAIELTS) — 출처 우선 IELTS 학습 플랫폼. [amlich](https://github.com/doxuta/amlich) — 천문 계산 기반 베트남·한국 음력 Go 라이브러리(설날과 Tết이 어긋나는 해를 계산합니다). [caudao](https://github.com/doxuta/caudao) — AI 에이전트용 비용 차단기. [mcpvet](https://github.com/doxuta/mcpvet) — MCP 서버 계약 테스트 도구.

**작업 방식:** AI 에이전트를 사용하며, 이를 숨기지 않습니다. 제가 직접 맡는 것은 방향을 정하고, 모든 변경을 리뷰하고, 결과가 그럴듯한 것이 아니라 실제로 옳다는 것을 증명하는 테스트를 쓰는 일입니다.

</details>
