---
name: tiktok-script-writer
description: Viết script TikTok / Reels / Shorts theo cấu trúc Hook–Body–CTA cho TinySun / AMEBE — có timestamp theo độ dài, 3 biến thể hook, caption, ghi chú sản xuất. Skill công cụ, chạy dưới content-agent.
version: 2.0.0
category: content
tags: [tiktok, script, video, hook, tiktok-shop, vietnam, me-va-be]
---

# TikTok Script Writer (v2.0 — 20/10/2026)

Đầu ra là script quay được ngay — từng câu, từng beat, từng CTA. **Skill này là công cụ của `content-agent`**: thương hiệu, tone, audience, dữ liệu sản phẩm, quy tắc claim và nơi lưu file lấy từ content-agent. Nếu được gọi trực tiếp, đọc ngữ cảnh ở content-agent trước.

## Input (content-agent cấp; thiếu thì hỏi tối đa 2 câu, vẫn giao bản nháp với `[___]`)

```
Thương hiệu / SKU: ___ (tone theo bảng thương hiệu)
Mục tiêu: [Awareness / Engagement / Lead / Sale TikTok Shop]
Đối tượng: ___ (mẹ thành thị 25–35 / mẹ ở tỉnh / mẹ quan tâm chất lượng / người tặng quà...)
Độ dài: [15s / 30s / 60s]
CTA cuối: [Giỏ hàng vàng / Comment size / Follow / Inbox / Link bio]
Tone: [Chia sẻ thật / Hướng dẫn / Hài nhẹ / Story]
Số liệu thật có sẵn: giá, số miếng, số giờ thấm, chứng nhận (từ fact-sheet; không có → [___])
```

## Phần 1 — HOOK (0–3s): 6 loại được dùng

1. **Nhắm thẳng audience:** "Mẹ nào ở quê mua bỉm ngoài tạp hoá thì nghe em nói câu này đã."
2. **Câu hỏi đúng nỗi đau:** "Đêm nào cũng dậy thay bỉm 2 lần, mẹ có chắc là do con?"
3. **Số liệu thật:** "Một tháng nhà em tốn [___]k tiền bỉm. Giờ còn [___]k." (số phải có thật hoặc để trống)
4. **So sánh nhìn thấy được:** "Cùng [___]k, ngoài tạp hoá được [___] miếng, trên này được [___] miếng — em để hai bịch cạnh nhau."
5. **Test tại chỗ:** "Mẹ nào sợ mua bỉm trên mạng bị hàng kém, em đổ nước thử cho xem."
6. **Câu chuyện bắt đầu từ giữa:** "Hôm qua bà nội hỏi sao dạo này cháu ngủ xuyên đêm..."

**Không dùng:** tuyên bố gây sốc, tranh cãi để câu view, hứa kết quả y tế ("hết hăm 100%"), từ "bùng nổ / chấn động / bí mật không ai nói".

## Phần 2 — BODY

- Mỗi beat ≤ 5 giây; xen điểm nhấn: con số thật, ví dụ thật, đổi cảnh.
- Pattern interrupt mỗi 10–15s: đổi góc / zoom / B-roll (mặt trong bỉm, đổ nước thử, bé mặc).
- Ngôn ngữ nói, thân mật, có "à", "thì", "nha"; giọng vùng miền thật cho mẹ ở tỉnh.
- Format: **List** (3 lý do…), **Story** (trước → vấn đề → bước ngoặt → kết quả), **Tutorial** (bước 1-2-3), **Test** (đổ nước, lật ngược, khăn giấy).

## Phần 3 — CTA (5s cuối) — theo mục tiêu

| Mục tiêu | CTA mẫu |
|---|---|
| **Sale TikTok Shop** | "Bấm vào **giỏ hàng vàng** góc dưới, đang có [mã/combo ___]. Ship tận xã, [nhận hàng mới trả tiền — nếu Sếp xác nhận COD]." |
| Comment | "Comment **size bé đang dùng**, em báo giá ngay." |
| Follow | "Follow để xem phần 2: test thấm hút 8 tiếng." |
| Inbox | "Nhắn em chữ 'SIZE', em gửi bảng size + giá." |
| Save | "Lưu video này, lúc đổi size mở ra xem." |
| Engagement | "Nhà mình đang dùng bỉm gì? Comment cho em biết." |

Luôn lặp lại CTA bằng text overlay.

## Khung theo độ dài

- **15s:** 0–2s hook · 2–10s 1 ý duy nhất + ví dụ · 10–15s CTA
- **30s:** 0–3s hook · 3–9s nỗi đau · 9–16s giải pháp (+ B-roll) · 16–22s điểm mạnh nhất (số thật) · 22–30s CTA
- **60s:** 0–3s hook · 3–10s bối cảnh · 10–45s 3–5 beats · 45–55s kết quả/takeaway · 55–60s CTA

## Template

```
=== SCRIPT: [Tiêu đề] ===
Thương hiệu: · Mục tiêu: · Độ dài: · Format: [talking head / voiceover / test]
--- HOOK (0–3s) --- [câu nói] [visual] [text overlay]
--- BEAT 1 --- ... --- BEAT n ---
--- CTA --- [câu] [text overlay lặp CTA]
=== GHI CHÚ SẢN XUẤT === người quay (mẹ thật / KOC / nhân sự), bối cảnh thật, nhạc nền nhẹ, caption chữ BẬT, ánh sáng tự nhiên, đạo cụ
=== 3 BIẾN THỂ HOOK ===
=== CAPTION (≤150 ký tự) + hashtag ===
=== CẦN SẾP ĐIỀN / XÁC NHẬN === giá, mã giảm, số miếng, chứng nhận đúng dòng, COD, vùng miền
```

Giờ đăng gợi ý (20h–22h, 11h30–13h) là giả định theo thói quen mẹ bỉm — ghi rõ "cần đối chiếu TikTok Analytics của kênh".

## Chỉ số thành công

- Hook giữ người xem trong 1 giây đầu · Không câu thừa · 1 CTA duy nhất · Đọc to nghe như nói chuyện · Không có số bịa.
