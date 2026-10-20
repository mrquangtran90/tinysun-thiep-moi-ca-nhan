# Bộ ca nghiệm thu Tinysun AI Company (7 ca) — dùng lại mỗi khi sửa skill

Cách chạy: mở hội thoại mới (hoặc subagent), gửi đúng câu của Sếp, yêu cầu cuối cùng thêm mục `=== META ===` (skill đã gọi, câu hỏi đã đặt, đường dẫn file, số liệu không nguồn, điểm mâu thuẫn). Dry run: không ghi file.

| # | Câu của Sếp | Kỳ vọng route | Tiêu chí đạt |
|---|---|---|---|
| T1 | "Em ơi, TinyCare dạo này bán chậm, anh muốn làm gì đó với nó." | dispatcher hỏi đúng 1 câu (3 hướng) | Không làm nửa vời; không bịa; có gợi ý mặc định |
| T2 | "Viết cho anh 1 bài Facebook ra mắt BB Jollity Natural, mục tiêu bán hàng, đăng trên fanpage TinySun." | content-agent | Bản chính + visual + angle thay thế; placeholder cho giá/số; không từ cấm; không claim y tế; tone fanpage tập đoàn; danh sách ô cần Sếp điền |
| T3 | "Lên kế hoạch marketing Q4/2026 cho AMEBE, ngân sách 150 triệu, mục tiêu doanh thu 600 triệu trong quý. Kênh chính là Facebook và TikTok Shop." | ke-hoach-agent (duy nhất) | Thực thu online 80%; bảng tài chính + 3 kịch bản; cảnh báo vượt quỹ MKT 10%; lịch tính từ hôm nay; giả định AOV/COGS ghi rõ |
| T4 | "Phân tích đối thủ Moony và Merries tại Việt Nam cho anh, để anh quyết định có tăng giá BB Jollity không." | nghien-cuu-thi-truong → ceo-agent | Có nguồn + năm; "không tìm được" liệt kê rõ; 1 format khuyến nghị (ceo-agent); 1 đường dẫn lưu |
| T5 | "Làm cho anh báo cáo doanh thu bỉm tháng 9/2026 so với tháng 8, phân theo NPP 3 miền và TikTok Shop." (không file) | bao-cao-agent | 0 con số bịa; trả khung + tối đa 3 câu hỏi |
| T6 | "Anh đang cân nhắc đưa dòng bỉm người già cao cấp ra thị trường dưới thương hiệu riêng thay vì chỉ làm OEM. Nên hay không?" | ceo-agent (+ nghien-cuu nếu cần) | Trả lời thẳng nên/không ở câu đầu; so sánh phương án; giả định nội bộ đánh dấu; mục "số liệu em cần Sếp" |
| T7 | "Viết script TikTok 30 giây cho Tiny Hachi, nhắm mẹ ở tỉnh, mục tiêu kéo đơn về TikTok Shop." | content-agent → tiktok-script-writer | Khung 30s đúng timestamp; CTA giỏ hàng vàng; không hook gây sốc; 3 hook; caption ≤150; không tham chiếu Maya/Alex |

Kết quả lần chạy 20/10/2026 (bản v1 đang cài): xem `BAO-CAO-NGHIEM-THU-2026-10-20.md`.
