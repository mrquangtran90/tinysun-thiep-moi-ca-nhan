# Kiểm kê toàn bộ skill của Sếp và bản đồ "nhân viên AI ↔ skill" — 20/10/2026

**Nguồn đã đọc:** (1) 11 skill đang bật trên claude.ai; (2) repo private `tinysun-codex-skills` (commit 01/10/2026, 40 skill); (3) repo private `tinysun-portable-backup` (commit 04/10/2026, 47 skill Codex + 12 skill HyperFrames + quy tắc toàn cục `AGENTS-global.md` + Đầu não Subagent); (4) repo `tinysun-thiep-moi-ca-nhan` (1 skill, cùng bản trong marketplace nội bộ).

Bản `tinysun-portable-backup/skills/codex-user/` là **bản đầy đủ và mới nhất** (chính file bàn giao của Sếp cũng ghi vậy): chứa toàn bộ 40 skill của repo codex-skills + 7 skill chỉ có ở đây (`dau-nao-subagent`, `subagent-cham-soc-khach-hang`, `subagent-tao-video`, `tinysun-kiem-toan`, `edit-captioned-vertical-video`, `hyperframes-studio`, `motion-graphics`).

---

## 1. Kết luận

- **Sếp đang có 2 công ty AI chạy song song, không biết nhau.** Hệ **Claude.ai** (Amee + 4 agent + 6 công cụ, 11 skill) lo chiến lược, kế hoạch, báo cáo, content chữ. Hệ **Codex** (Amee + Alex/Maya/Len/Mina/Aimee/Kim + Đầu não Subagent, 47 skill) lo sản xuất media, web, kế toán, văn bản, CSKH. Dispatcher của mỗi bên không có đường chuyển việc sang bên kia.
- **2 vị trí bị trùng ở cả hai hệ với nội dung khác nhau:** Nghiên cứu thị trường (Alex) và Content (Maya). Bản Codex sâu hơn hẳn (cổng duyệt claim, bộ nhận diện trên pCloud, 8 chế độ nghiên cứu, hệ nhãn xác nhận/giả định/cần kiểm). Bản Claude.ai (kể cả v2 em vừa soạn) nên kế thừa từ bản Codex, không viết lại từ đầu.
- **4 vị trí chưa có nhân viên AI nào ở cả hai hệ:** Kinh doanh/NPP/trade marketing (báo giá shop, chính sách NPP, KPI phòng KD đang làm tay), Livestream/PG (kênh bán chính nhưng không có skill kịch bản live), Vận hành đơn/kho/COD (có web /donhang nhưng không có agent), Nhân sự/đào tạo.
- **Quy tắc toàn cục của Codex (`AGENTS-global.md`) là nguồn dữ kiện tốt nhất em tìm được** và nó sửa 4 chỗ trong bộ v2.1: bỉm trẻ em (mọi dòng Tiny) thiết kế nội bộ, sản xuất tại Trung Quốc, không phải Nam Định; văn phòng Ninh Bình quản lý NPP miền Trung; TinySun 25 người, tập đoàn 300+; đối thủ trực tiếp ngành bỉm là Motaro, Gooby, Bemom, Yingcool, còn Bobby/Huggies chỉ để tham chiếu chính sách. Em đã cập nhật vào Context v2.2.
- **1 cảnh báo bảo mật:** file `rules/codex-rules/default.rules` trong repo portable-backup chứa 1 token Bearer của dịch vụ git ChatGPT nằm trong lệnh push đã lưu. Repo private nhưng vẫn nên thu hồi token và xoá dòng đó.

---

## 2. Kiểm kê theo nguồn

### 2.1 Claude.ai (11 skill, đã nghiệm thu 20/10)

| Skill | Vai trò | Ghi chú |
|---|---|---|
| amee-dispatcher | Điều phối | v2 đã viết lại |
| ceo-agent | CEO / Chiến lược | v2 |
| content-agent | Content (Maya bản Claude) | v2 |
| ke-hoach-agent, ke-hoach | Kế hoạch / Marketing | Gộp làm 1 trong v2 |
| bao-cao-agent | Báo cáo / Phân tích | v2 |
| nghien-cuu-thi-truong | Nghiên cứu (Alex bản Claude) | v2 |
| tiktok-script-writer, viral-post-writer, lead-magnet-builder, content-pillar-atomizer | Công cụ content | Gốc là bộ của Maya/Alex bên Codex; v2 đã gắn dưới content-agent |

### 2.2 Codex — 47 skill trong `tinysun-portable-backup/skills/codex-user/` (nhóm theo vị trí)

| Vị trí (persona) | Skill | Trạng thái theo bàn giao 04/10 |
|---|---|---|
| **Đầu não / điều phối** | dau-nao-subagent (+ `agents/tinysun-subagent-hub` CLI, registry 5 vai: research, video-edit, quality-review, customer-care-draft, flow-tvc) | CLI lưu job, không tự chạy; cần cấu hình lại path trên Mac |
| **Nghiên cứu (Alex)** | tinysun-nghien-cuu-thi-truong | 8 chế độ, hợp đồng bàn giao content-intelligence brief |
| **Content (Maya)** | tinysun-fb-content (Maya engine, profile registry, claim-approval-gate, đăng/lên lịch FB & TikTok), viral-facebook-reel-maker, tinysun-videoviral, ts-video-review-san-pham | Facebook là kênh chính; bộ nhận diện 10 nhãn trên pCloud `Bộ nhận diện/` |
| **Media – ảnh** | tinysun-poster-san-pham, tinysun-batch-creative, tinysun-thuong-hieu-ca-nhan, tinysun-thiep-moi-ca-nhan, tinysun-cameo-nhan-vat, model-quang-1, model-nha-thanh-02 | Có asset nhận diện; QA bằng mắt bắt buộc |
| **Media – video** | tinysun-video-san-pham-hero, tinysun-video-thoi-trang, tinysun-video-khoa-hoc-zoom, tinysun-xem-phan-tich-video, video-hoan-doi-nv, edit-captioned-vertical-video, general-video, motion-graphics, tinysun-kho-am-thanh (113 MP3) | |
| **Media – Google Flow / HeyGen** | flow-tvc-director, subagent-tao-video, tinysun-flow-video, tinysun-flow-cameo-channel, heygen-video, heygen-avatar, heygen-translate | Dịch vụ trả phí: phải xin duyệt trước Generate |
| **Media – HyperFrames** | hyperframes, -core, -animation, -audio, -cli, -creative, -keyframes, -registry, -studio, media-use | Cài từ `heygen-com/hyperframes`, bản sao ở `agents-user/` trùng |
| **Web / Dev / Automation** | tinysun-web, tinysun-zalo-miniapp, tinysun-n8n, tinysun-kiem-duyet-code | /ketoan chưa deploy; Zalo Mini App chưa tìm thấy project gốc |
| **Văn phòng / Pháp lý (Mina)** | tinysun-van-phong (báo giá, hợp đồng, chính sách, công văn, P&L) | 8 năng lực Mina |
| **Kế toán / Kiểm toán** | tinysun-kiem-toan (Excel–KiotViet, công nợ, thu hộ) | Rà soát nội bộ, không thay kế toán |
| **CSKH** | subagent-cham-soc-khach-hang | Mới là bản nháp; chưa nối Facebook/Zalo |
| **AMEBE (Aimee + Kim)** | amebe-thiet-ke-thoi-trang | Tạm dừng theo Sếp 20/10 |
| **Review chất lượng (Len)** | quality-gates trong dau-nao-subagent; tinysun-kiem-duyet-code | Không có skill riêng |

### 2.3 Trùng lặp cần dọn

| Trùng | Ở đâu | Đề xuất |
|---|---|---|
| 12 skill HyperFrames | `skills/agents-user/` và `skills/codex-user/` trong portable-backup | Giữ `codex-user`, xoá `agents-user` (bàn giao đã ghi "không chép 2 bản") |
| 40 skill | repo `tinysun-codex-skills` (01/10) và `portable-backup/skills/codex-user` (04/10) | Chọn 1 repo làm nguồn: đề xuất giữ `tinysun-codex-skills` làm repo skill, đồng bộ 7 skill mới từ portable sang, rồi portable chỉ giữ web/agents/rules |
| tinysun-thiep-moi-ca-nhan | 4 bản (repo riêng, codex-skills, portable, 3 phiên bản marketplace) | Repo riêng là nguồn; các bản còn lại trỏ về |
| Nghiên cứu thị trường | Claude `nghien-cuu-thi-truong` vs Codex `tinysun-nghien-cuu-thi-truong` | Claude kế thừa cấu trúc Codex (xem mục 4) |
| Content | Claude `content-agent` vs Codex `tinysun-fb-content` | Claude kế thừa claim-approval-gate và shared-content-core (mục 4) |

---

## 3. Bản đồ vị trí nhân viên AI ↔ skill (cả hai hệ)

| # | Vị trí | Claude.ai | Codex | Đánh giá |
|---|---|---|---|---|
| 1 | Điều phối (Amee) | amee-dispatcher | dau-nao-subagent | **Thiếu cầu nối**: Claude không biết chuyển việc media/web/kế toán sang Codex; Codex registry chỉ có 5 vai |
| 2 | CEO / Chiến lược | ceo-agent | — | Đủ (chỉ cần ở Claude) |
| 3 | Kế hoạch / Marketing | ke-hoach-agent | — | Đủ ở Claude; thiếu benchmark nội bộ |
| 4 | Báo cáo / Phân tích số liệu | bao-cao-agent | tinysun-kiem-toan, tinysun-van-phong (P&L) | **Tách đôi**: Claude làm KPI/marketing, Codex làm đối soát kế toán. Thiếu 1 nguồn dữ liệu chung (KiotViet export, báo cáo NPP) |
| 5 | Nghiên cứu (Alex) | nghien-cuu-thi-truong | tinysun-nghien-cuu-thi-truong | **Trùng, khác nội dung** |
| 6 | Content (Maya) | content-agent + 4 công cụ | tinysun-fb-content + 3 skill video viral | **Trùng, Codex mạnh hơn**; Claude thiếu cổng duyệt claim và bộ nhận diện |
| 7 | Sản xuất media | — | 25 skill | Đủ ở Codex; Claude đúng là không nên có (không chạy được tool) |
| 8 | Web / Dev / Automation | — | 4 skill | Đủ ở Codex |
| 9 | Văn phòng / Pháp lý (Mina) | — | tinysun-van-phong | **Claude thiếu**, dù preference của Sếp ghi Amee là "chuyên gia luật" |
| 10 | Kế toán / Kiểm toán | — | tinysun-kiem-toan | Đủ ở Codex; chỉ 1 skill cho cả kế toán |
| 11 | CSKH | — | subagent-cham-soc-khach-hang (nháp) | **Thiếu nội dung**: chưa có FAQ sản phẩm, kịch bản xử lý khiếu nại, chưa nối kênh |
| 12 | AMEBE thiết kế (Aimee/Kim) | — | amebe-thiet-ke-thoi-trang | Tạm dừng |
| 13 | Review chất lượng (Len) | — | quality-gates, kiem-duyet-code | **Claude thiếu** bước review chéo trước khi giao |
| 14 | **Kinh doanh / NPP / Trade marketing** | — | — | **THIẾU HẲN.** Bằng chứng việc đang làm tay: "Bảng tổng hợp báo giá shop 28.8.26", "Bảng KPI phòng MKT và KD 29.8.26" trong lịch sử lệnh Codex |
| 15 | **Livestream / PG** | — | — | **THIẾU HẲN** dù là kênh bán chính (TikTok Shop, live tại shop, PG điểm bán) |
| 16 | **Vận hành đơn / kho / COD / GHTK** | — | — (chỉ có web /donhang) | **THIẾU**: không có agent đối soát COD, theo dõi đơn, cảnh báo tồn kho |
| 17 | **Nhân sự / đào tạo / chấm công** | — | — (có app /chamcong, video khoá học) | **THIẾU** agent HR: JD, onboarding, đào tạo PG/sales |

---

## 4. Việc cần làm, theo ưu tiên

### Ưu tiên 1 — Sửa dữ kiện và nối hai hệ (tuần này)

1. **Context v2.2 đã sửa theo `AGENTS-global.md`** (xem mục 5). Sếp kiểm 1 lần rồi upload 10 skill v2.
2. **Thêm bảng chuyển việc Claude → Codex vào dispatcher** (đã thêm trong v2.2): media/video/ảnh → Codex skill tương ứng; web/Zalo/n8n → Codex; văn bản pháp lý, báo giá, hợp đồng → `tinysun-van-phong`; đối soát kế toán → `tinysun-kiem-toan`; CSKH → `subagent-cham-soc-khach-hang`. Amee trên Claude trả lời: "Việc này thuộc Codex skill X, Sếp mở Codex và gọi `$X`", kèm brief đã soạn sẵn.
3. **Thống nhất hệ nhãn số liệu** thành đúng 3 nhãn của Sếp: **xác nhận / giả định / cần kiểm** (v2.2 đã đổi; trước đó Claude dùng "(ước tính)", "(chưa xác minh)").
4. **Thu hồi token** trong `rules/codex-rules/default.rules` và xoá dòng chứa nó.

### Ưu tiên 2 — Hợp nhất 2 vị trí trùng (2 tuần)

5. **Alex:** Claude `nghien-cuu-thi-truong` lấy lại 8 chế độ, hợp đồng "content-intelligence brief" và nguyên tắc nguồn từ bản Codex; giữ phần "giới hạn công cụ" của Claude.
6. **Maya:** Claude `content-agent` lấy `shared-content-core.md`, `claim-approval-gate.md` và đường dẫn bộ nhận diện 10 nhãn (`Bộ nhận diện/<nhãn>/03-dac-diem-noi-bat.md`, `04-chinh-sach-gia.md`) từ `tinysun-fb-content`. Đây chính là "bảng thông số sản phẩm" em đang xin Sếp điền: **nó đã có trên pCloud**, chỉ cần Claude đọc được (upload vào Project hoặc Google Drive).

### Ưu tiên 3 — Tuyển thêm 4 nhân viên AI đang thiếu (theo thứ tự giá trị)

7. **Kinh doanh / NPP:** skill `kinh-doanh-npp-agent`: chính sách chiết khấu theo kênh (đã có số), bảng báo giá shop/NPP từ giá niêm yết, KPI phòng KD theo vùng, kịch bản chốt NPP mới, đánh giá NPP (sell-in/sell-out/tồn). Đầu vào có sẵn: 2 bảng Sếp đã làm tay tháng 8.
8. **Livestream / PG:** skill `livestream-pg-agent`: kịch bản live 60–120 phút theo SKU, combo/voucher theo phút, câu trả lời comment thường gặp, checklist PG tại điểm bán, báo cáo sau live (GMV, đơn, người xem đỉnh).
9. **Vận hành đơn / COD:** skill `van-hanh-don-agent`: đọc export /donhang và GHTK, cảnh báo đơn kẹt, đối soát COD 3 lớp theo đúng nguyên tắc trong bàn giao, cảnh báo tồn kho theo size.
10. **CSKH hoàn thiện:** bổ sung FAQ 10 nhãn từ bộ nhận diện, cây xử lý khiếu nại, và quyết định có nối Zalo OA hay chưa.
11. **Nhân sự (sau cùng):** JD, onboarding PG/sales, bài kiểm tra kiến thức sản phẩm.

### Ưu tiên 4 — Dọn kho skill

12. Chọn 1 repo nguồn cho skill Codex (đề xuất `tinysun-codex-skills`), đồng bộ 7 skill mới, xoá bản `agents-user/` trùng.
13. Chuẩn hoá quy tắc lưu file giữa 2 hệ: Codex dùng pCloud `outputs/TinySun/Tên công việc D.M.YY/` (ngày cuối), Claude dùng `~/claude/outputs/TinySun/YYYY-MM-DD Tên công việc/` (ngày đầu). Sếp chọn 1 chuẩn; em đề xuất lấy chuẩn pCloud của Codex làm gốc vì đã đổi tên 40 folder cũ theo chuẩn đó.

---

## 5. Dữ kiện lấy từ `AGENTS-global.md` đã đưa vào Context v2.2

| Dữ kiện | Bản v2.1 (sai/thiếu) | v2.2 (theo AGENTS-global, nhãn xác nhận) |
|---|---|---|
| Nơi sản xuất bỉm trẻ em | Tiny sản xuất Nam Định | Mọi dòng bỉm trẻ em: thiết kế nội bộ, sản xuất tại Trung Quốc; nhà máy Nam Định sản xuất băng vệ sinh (và bỉm người già OEM) |
| Văn phòng Ninh Bình | "cần xác nhận" | Tầng 2 Toà Moha, 512 Trần Hưng Đạo, Ninh Bình — quản lý NPP miền Trung |
| Nhân sự | 300+ CBCNV | TinySun ~25 người; cả tập đoàn 300+ (gồm 2 nhà máy cổ phần) |
| Đối thủ bỉm | Bobby/Pampers/Huggies/MamyPoko mass; Moony/Merries/Goo.n cao cấp | Trực tiếp: Motaro (Honey, Momotaro), Gooby, Bemom, Yingcool, bỉm nội địa. Bobby/Huggies: chỉ tham chiếu chính sách. Moony/Merries/Goo.n: benchmark phân khúc Nhật cho BB Jollity |
| Sản phẩm thiếu | — | TinyCare Pro dạng quần (bình dân); Khăn khô đa năng BB Jollity Natural; Tiny Eco 155–175k |
| BB Jollity | thương hiệu Nhật, SX Trung Quốc | + hợp tác độc quyền với công ty Nhật tại Tokyo |
| Hệ nhãn số liệu | (giả định) / (chưa xác minh) / (ước tính) | xác nhận / giả định (căn cứ + độ nhạy) / cần kiểm (cách kiểm rẻ nhất) |
| Thông tin nội bộ | — | Chiết khấu, cổ đông, vốn, doanh thu mục tiêu, nhân sự, OEM: không đưa vào bài đăng, website, artifact chia sẻ |
| Cổng xác nhận | — | 5 thao tác khó thu hồi (gửi ngoài, đăng công khai, xoá/ghi đè file cũ, API đổi state, trình duyệt tài khoản thật) phải chờ Sếp |
