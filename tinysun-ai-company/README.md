# Tinysun AI Company — bộ skill v2 (nguồn sự thật duy nhất)

Thư mục này là **mã nguồn** của 10 skill "nhân viên AI" dùng trên claude.ai (Amee). Bản đang cài trên tài khoản (v1) được nghiệm thu ngày 20/10/2026 — xem `BAO-CAO-NGHIEM-THU-2026-10-20.md`.

## Cấu trúc

```
tinysun-ai-company/
├── context/
│   ├── tinysun-context.md       ← dữ kiện doanh nghiệp DÙNG CHUNG (sửa ở đây, không sửa trong skill)
│   ├── product-fact-sheet.md    ← bảng thông số sản phẩm (Sếp/đội sản phẩm điền)
│   └── file-rules.md            ← quy tắc lưu file thống nhất
├── templates/<skill>.md         ← nội dung riêng từng skill, có chỗ trống {{CONTEXT}} {{FILE_RULES}}
├── build.py                     ← ghép context vào template → dist/
├── dist/<skill>/SKILL.md        ← BẢN ĐỂ UPLOAD lên claude.ai
└── tests/test-cases.md          ← 7 ca nghiệm thu dùng lại
```

## Quy trình cập nhật

1. Sửa dữ kiện trong `context/*.md` (hoặc nội dung riêng trong `templates/`).
2. Chạy `python3 build.py` (không cần thư viện ngoài).
3. Trên claude.ai → Settings → Skills: thay nội dung từng skill bằng `dist/<skill>/SKILL.md`.
4. **Xoá skill `ke-hoach`** (đã gộp vào `ke-hoach-agent`).
5. Chạy lại 7 ca trong `tests/test-cases.md`.

## Đã chốt với Sếp ngày 20/10/2026 (Context v2.1)

- Kênh online đang bán: TikTok Shop + web tinysun.vn/gianhang; Facebook kéo đơn về web; Shopee không còn trong danh sách.
- BB Jollity và BB Jollity Natural: thương hiệu Nhật, mã vạch Nhật, sản xuất tại Trung Quốc, TinySun phân phối độc quyền tại VN.
- AMEBE tạm dừng, chưa có sản phẩm; không lập plan/nghiên cứu/content cho đến khi Sếp báo.

## Context v2.2 (20/10/2026) — đối chiếu với `AGENTS-global.md` trong repo `tinysun-portable-backup`

Đã sửa: bỉm trẻ em sản xuất tại Trung Quốc (thiết kế nội bộ); văn phòng Ninh Bình quản lý NPP miền Trung; nhân sự TinySun ~25 / tập đoàn 300+; đối thủ trực tiếp Motaro, Gooby, Bemom, Yingcool; thêm TinyCare Pro, Khăn khô BB Jollity Natural; hệ nhãn xác nhận / giả định / cần kiểm; quy tắc thông tin nội bộ; cổng xác nhận; bảng chuyển việc sang 47 skill Codex trong dispatcher. Kiểm kê đầy đủ: `KIEM-KE-SKILL-2026-10-20.md`.

## Còn chờ Sếp

1. Tỷ lệ thực thu web tinysun.vn/gianhang (mặc định 85–90%, giả định).
2. Bảng thông số sản phẩm: bộ nhận diện 10 nhãn đã có trên pCloud `Output Admin/outputs/Bộ nhận diện/` — đưa vào Project/Drive để Claude đọc, thay vì điền tay `product-fact-sheet.md`.
3. Chọn 1 chuẩn lưu file cho cả Codex và Claude (pCloud `Tên công việc D.M.YY` hay `YYYY-MM-DD Tên công việc`).
