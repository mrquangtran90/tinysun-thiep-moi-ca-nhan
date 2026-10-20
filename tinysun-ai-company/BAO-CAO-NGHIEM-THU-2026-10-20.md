# Báo cáo nghiệm thu Tinysun AI Company — 20/10/2026

**Đối tượng nghiệm thu:** 11 skill đang bật trên tài khoản claude.ai của Sếp (bản v1): `amee-dispatcher`, `ceo-agent`, `content-agent`, `ke-hoach-agent`, `ke-hoach`, `bao-cao-agent`, `nghien-cuu-thi-truong`, `tiktok-script-writer`, `viral-post-writer`, `lead-magnet-builder`, `content-pillar-atomizer`.

**Phương pháp:** (1) đọc toàn bộ 11 file SKILL.md và đối chiếu chéo dữ kiện; (2) chạy thật 7 ca nghiệm thu, mỗi ca là một hội thoại mới với câu lệnh thực tế của Sếp, quan sát skill được kích hoạt, câu hỏi đặt ra, đường dẫn lưu, số liệu bịa, điểm mâu thuẫn; (3) soạn bộ v2 và chạy lại 2 ca nặng nhất để xác nhận.

---

## 1. Kết luận điều hành

- **Quy trình chạy được.** 7/7 ca kích hoạt đúng agent chủ qua dispatcher; 0/7 ca bịa số liệu; 7/7 tuân thủ xưng hô, không dùng từ cấm. Chất lượng đầu ra (kế hoạch Q4 AMEBE, phân tích bỉm người già) ở mức dùng được ngay sau khi Sếp điền số nội bộ.
- **Nhưng hệ thống đang "chạy nhờ" agent tự vá lỗi.** 5/7 ca agent phải tự suy luận ngoài hướng dẫn: tự gọi skill mà dispatcher không biết (T4, T7), tự chọn giữa 2 skill trùng nhau (T3), tự bỏ qua con số sai (T3), tự dung hoà 2 quy trình mâu thuẫn (T2, T7).
- **Skill chưa gắn đúng cho nhân viên:** dispatcher chỉ biết 4/10 agent; `nghien-cuu-thi-truong` và `ke-hoach` mồ côi; 4 skill công cụ content còn gắn với persona "Maya/Alex" của bộ plugin khác và tham chiếu 2 skill không tồn tại.
- **1 lỗi dữ kiện nghiêm trọng:** doanh thu thực thu kênh online ghi **80%** ở 3 skill nhưng **20–30%** ở skill `ke-hoach` — lệch gần 3 lần, đủ làm sai toàn bộ P&L nếu agent chọn nhầm skill.
- **Đã soạn bộ v2** (10 skill, gộp `ke-hoach` vào `ke-hoach-agent`, 1 nguồn ngữ cảnh duy nhất, quy tắc lưu file thống nhất). Chờ Sếp chốt 4 dữ kiện rồi upload.

---

## 2. Kết quả 7 ca nghiệm thu (bản v1 đang cài)

| Ca | Yêu cầu của Sếp | Skill kích hoạt | Bịa số? | Kết quả | Vấn đề chính phát hiện |
|---|---|---|---|---|---|
| T1 | TinyCare bán chậm, "muốn làm gì đó" (mơ hồ) | dispatcher | Không | **Đạt** | Thiếu quy tắc mặc định khi câu không có động từ; context TinyCare quá mỏng |
| T2 | Bài Facebook ra mắt BB Jollity Natural, mục tiêu bán | dispatcher → content-agent | Không (placeholder) | **Đạt** | Thiếu bảng thông số SP; mâu thuẫn "hỏi trước" vs "làm ngay"; thiếu quy tắc claim; không phân biệt fanpage tập đoàn/nhãn |
| T3 | Kế hoạch marketing Q4 AMEBE 150tr / 600tr | dispatcher → ke-hoach-agent (mượn thêm ke-hoach) | Không (giả định ghi rõ) | **Đạt** | 2 skill kế hoạch trùng; **thực thu online 80% vs 20–30%**; 3 quy tắc lưu file khác nhau; thiếu AOV/COGS |
| T4 | Phân tích Moony/Merries để quyết định tăng giá | dispatcher → ceo-agent → tự gọi nghien-cuu | Không ("chưa xác minh") | **Đạt một phần** | Dispatcher không có route nghiên cứu; 2 format output và 2 quy tắc lưu file xung đột; WebSearch không tìm được thị phần/giá 2026 |
| T5 | Báo cáo doanh thu bỉm T9 vs T8, không có file | dispatcher → bao-cao-agent | **Không** (mọi ô "chưa có dữ liệu") | **Đạt** | Đường dẫn macOS không tồn tại trên cloud; thiếu fallback khi không có dữ liệu; tên file quá dài |
| T6 | Bỉm người già: thương hiệu riêng hay OEM? | dispatcher → ceo-agent | Không (giả định đánh dấu) | **Đạt** | ceo-agent tự mâu thuẫn ("không tư vấn từ giả định" vs "hỏi thay vì giả định"); context thiếu mảng bỉm người già; context AMEBE cũ 4 tháng |
| T7 | Script TikTok 30s Tiny Hachi, mẹ ở tỉnh | dispatcher → content-agent → tự gọi tiktok-script-writer | Không (placeholder) | **Đạt** | Skill tham chiếu Maya/Alex, 2 skill không tồn tại; hook "gây sốc" trái quy tắc Sếp; ví dụ 100% niche "kiếm tiền online"; thiếu CTA giỏ hàng |

Nguồn dữ liệu WebSearch thực tế có được trong T4/T6: Metric (doanh số tã bỉm 4 sàn 9T/2025), IMARC (thị trường tã VN 2024), số liệu dân số 60+ năm 2025 (Nhân Dân/VnExpress), Euromonitor 2023 qua ITPC. Thị phần và giá 2026 của Moony/Merries không tìm được.

---

## 3. Phát hiện theo mức độ ưu tiên

### Ưu tiên 1 — Sai dữ kiện, phải sửa trước khi dùng cho tài chính

| # | Vấn đề | Ở đâu | Hệ quả | Xử lý trong v2 |
|---|---|---|---|---|
| 1.1 | Thực thu online: "thu về 80%" vs "~80% chi phí → 20–30% giá lẻ" | dispatcher, ke-hoach-agent, bao-cao (80%) vs ke-hoach (20–30%) | P&L lệch ~3 lần | Dùng 80% + đánh dấu "(cần Sếp xác nhận)" |
| 1.2 | "NPP độc quyền" gắn cho BB Jollity (dispatcher) nhưng gắn cho BB Jollity Natural (ceo-agent) | 2 skill | Content/claim sai dòng | Đánh dấu cần xác nhận |
| 1.3 | "Cao cấp Nhật" không rõ nhập khẩu hay sản xuất Nam Định | content-agent | Nguy cơ claim xuất xứ sai trong bài đăng | Đánh dấu cần xác nhận; thêm cột "xuất xứ" vào fact-sheet |
| 1.4 | Ninh Bình ghi "miền Trung" | ke-hoach-agent | Sai địa lý | Đánh dấu cần xác nhận |

### Ưu tiên 2 — Skill gắn sai / thiếu cho nhân viên

| # | Vấn đề | Xử lý trong v2 |
|---|---|---|
| 2.1 | Dispatcher chỉ biết 4 agent; `nghien-cuu-thi-truong` không có route | Bản đồ 5 agent chủ + 4 skill công cụ + bảng chuỗi kết hợp |
| 2.2 | `ke-hoach` và `ke-hoach-agent` trùng trigger; ke-hoach có framework tốt hơn nhưng mồ côi | Gộp framework vào `ke-hoach-agent`; **xoá `ke-hoach`** |
| 2.3 | 4 skill công cụ: `agent: maya`, tham chiếu Alex/Ace và 2 skill không tồn tại (`trending-content-scout`, `audience-profiling`, `email-automation-builder`) | Gỡ hết; ghi rõ "chạy dưới content-agent"; trend → nghien-cuu-thi-truong |
| 2.4 | content-agent không biết 4 skill công cụ; không có quy tắc ai thắng khi mâu thuẫn | Bảng skill công cụ + quy tắc "agent chủ thắng" |
| 2.5 | Hook "gây sốc", tone "Shock", ví dụ "mất 50 triệu", "kiếm 100 triệu/tháng" trái quy tắc cấm giật gân; ví dụ toàn niche kiếm tiền online | Thay bằng 6 loại hook hợp lệ, ví dụ mẹ & bé; thêm CTA "giỏ hàng vàng" |

### Ưu tiên 3 — Quy trình mâu thuẫn hoặc thiếu

| # | Vấn đề | Xử lý trong v2 |
|---|---|---|
| 3.1 | "Yêu cầu rõ → làm ngay" (dispatcher) vs "brainstorm 2–3 góc, Sếp chọn" (content-agent) | Quy tắc chung Bước 4: mục tiêu rõ → tự chọn, giao bản chính + angle thay thế |
| 3.2 | ceo-agent: "không tư vấn từ giả định" vs "hỏi thay vì giả định" → one-shot bế tắc | Hỏi tối đa 2 câu **và** trả lời luôn với giả định đánh dấu; mục "Số liệu em cần Sếp" |
| 3.3 | bao-cao không có fallback khi không có dữ liệu | Trả khung + 3 câu hỏi chuẩn |
| 3.4 | Không nhắc kiểm tra ngày hiện tại vs kỳ kế hoạch; không xử lý ngân sách vượt quỹ MKT 10% | Thêm vào dispatcher Bước 4 và checklist ke-hoach-agent |
| 3.5 | nghien-cuu kỳ vọng dữ liệu không khả thi (Statista/Euromonitor trả phí, Shopee không index, WebSearch thiên US) | Mục "Giới hạn công cụ và cách xử lý"; mục "Không tìm được" bắt buộc |
| 3.6 | Thiếu quy tắc claim y tế / nêu tên đối thủ / tone fanpage tập đoàn | Thêm vào context chung + content-agent |

### Ưu tiên 4 — Lưu file và bảo trì

| # | Vấn đề | Xử lý trong v2 |
|---|---|---|
| 4.1 | 4 quy tắc lưu file khác nhau: `~/claude/outputs/[Agent]/[Project]/DD-MM-YYYY` (ceo) · `/Users/quangtran/Claude/Projects/Agent .../` phẳng, không sub-folder (content, bao-cao, ke-hoach-agent) · `~/.claude/outputs/` + "Bản 1.0" (ke-hoach) · `Market Research/` + ngày hậu tố (nghien-cuu). Đường dẫn macOS không tồn tại trên cloud. | 1 quy tắc duy nhất theo đúng preference của Sếp + fallback cloud |
| 4.2 | Mục "Quy tắc lưu file" trong 3 agent bị mất định dạng (bảng dính 1 dòng, mất tiêu đề) | Viết lại sạch |
| 4.3 | Context doanh nghiệp bị dán lặp ở 6 skill với sai khác nhỏ; sửa 1 dữ kiện phải sửa 6 chỗ | 1 file `context/tinysun-context.md` + `build.py` ghép tự động |
| 4.4 | Context thiếu: thông số SKU, TinyCare/Collagen/OKLA, bỉm người già OEM, AOV/COGS/nhân sự AMEBE, kết quả GĐ1 AMEBE (plan 2.1 từ 12/06/2026, đã 4 tháng) | `product-fact-sheet.md` để Sếp điền; các ô "chưa có — hỏi Sếp" ghi rõ |
| 4.5 | Tên gọi `/ceo-agent` trong dispatcher khác tên thật `anthropic-skills:ceo-agent` | Dùng tên thật |

---

## 4. Bộ v2 đã soạn (thư mục `tinysun-ai-company/`)

| Skill | Thay đổi chính | Kích thước |
|---|---|---|
| amee-dispatcher | Bản đồ 5 agent + 4 công cụ; chuỗi kết hợp; quy tắc làm ngay/hỏi; kiểm tra ngày; vượt quỹ MKT | 14,7 KB |
| ceo-agent | Gọi nghien-cuu khi cần; fallback giả định; quy tắc chọn framework khi chồng lấn; mục "số liệu cần Sếp" | 12,4 KB |
| content-agent | Agent chủ của 4 skill công cụ; quy tắc claim; fanpage tập đoàn vs nhãn; fact-sheet | 13,4 KB |
| ke-hoach-agent | Gộp 6 framework từ `ke-hoach`; 3 kịch bản bắt buộc; checklist; xử lý vượt quỹ | 15,4 KB |
| bao-cao-agent | Fallback không dữ liệu; quy ước tìm Gmail/Drive; ngưỡng đèn | 12,9 KB |
| nghien-cuu-thi-truong | Có route từ dispatcher; giới hạn công cụ; mục "không tìm được"; chuyển ceo-agent sau nghiên cứu | 14,2 KB |
| tiktok-script-writer | Gỡ Maya/Alex; 6 hook hợp lệ; CTA giỏ hàng vàng; khung 30s đầy đủ | 5,0 KB |
| viral-post-writer | Gỡ Maya; ví dụ mẹ & bé; checklist claim | 3,6 KB |
| lead-magnet-builder | Gỡ Ace; Zalo/SĐT là kênh chính; ví dụ đúng ngành | 3,8 KB |
| content-pillar-atomizer | Gỡ Maya/Alex; pillar mẫu bỉm & AMEBE; xưng Sếp/Em | 3,8 KB |
| ~~ke-hoach~~ | **Xoá** (đã gộp) | — |

Các agent chủ dài 12–15 KB vì mang khối context chung (~6 KB) + quy tắc lưu file (~1,5 KB). Đổi lại, sửa dữ kiện chỉ ở 1 chỗ.

## 5. Kết quả chạy lại trên v2

{{V2_RESULTS}}

---

## 6. Việc Sếp cần làm (theo thứ tự)

1. **Chốt 4 dữ kiện** (mục 3, ưu tiên 1): thực thu online; dòng NPP độc quyền; xuất xứ BB Jollity; vùng của văn phòng Ninh Bình.
2. **Điền `context/product-fact-sheet.md`** (giá, số miếng, giờ thấm hút, chứng nhận từng SKU; AOV/COGS/nhân sự AMEBE; kết quả GĐ1). Không có bảng này, content vẫn phải để trống số.
3. Chạy `python3 build.py`, upload 10 file `dist/*/SKILL.md` lên claude.ai, **xoá skill `ke-hoach`**.
4. Chạy lại 7 ca trong `tests/test-cases.md`.

## 7. Giới hạn của lần nghiệm thu này

- Chạy trong môi trường cloud: không kiểm được việc ghi file thật vào `~/claude/outputs` trên máy Sếp (dry run, chỉ kiểm đường dẫn dự kiến).
- Không kiểm tích hợp Gmail/Drive (T5 cấm đọc).
- WebSearch trong môi trường này thiên kết quả US; chất lượng nghiên cứu tiếng Việt trên máy Sếp có thể khác.
- Mỗi ca chạy 1 lần; chưa đo độ ổn định khi lặp nhiều lần.
