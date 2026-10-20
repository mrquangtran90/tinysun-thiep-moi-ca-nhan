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

## 4 dữ kiện cần Sếp chốt trước khi upload (đang đánh dấu "(cần Sếp xác nhận)" trong context)

1. Doanh thu thực thu kênh online: **80% giá lẻ** (3 skill cũ) hay **20–30%** (skill ke-hoach cũ)? Bản v2 dùng 80%.
2. Dòng nào là "NPP độc quyền tại VN": BB Jollity Natural hay BB Jollity?
3. BB Jollity / Natural: nhập khẩu Nhật hay sản xuất Nam Định theo công nghệ Nhật? (ảnh hưởng claim xuất xứ trong content)
4. Văn phòng Ninh Bình thuộc vùng nào (skill cũ ghi "miền Trung")?
5. Thực thu kênh Facebook inbox/COD (tạm dùng 80% như sàn) và quỹ MKT có ngưỡng riêng cho nhãn giai đoạn test (AMEBE) không?
