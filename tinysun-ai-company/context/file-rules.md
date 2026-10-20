## Quy tắc lưu file (thống nhất toàn hệ thống — File rules v2.0)

**Thư mục gốc:** `~/claude/outputs/` (riêng tư). KHÔNG lưu vào folder "Tinysun Project" (chia sẻ với người khác).

```
~/claude/outputs/
├── TinySun/YYYY-MM-DD Tên công việc/     ← mọi việc TinySun Group
├── AMEBE/YYYY-MM-DD Tên công việc/       ← mọi việc AMEBE / Aimee Bebe
└── Chung/YYYY-MM-DD Tên công việc/       ← không thuộc dự án cụ thể
```

- Mỗi công việc = 1 folder con `YYYY-MM-DD Tên công việc`. Mọi file của cùng công việc (docx, xlsx, pptx, md) và mọi phiên bản sửa đều nằm trong folder đó.
- Tên file: `YYYY-MM-DD Tên mô tả.đuôi` (ví dụ `2026-10-20 Kế hoạch marketing Q4 AMEBE.docx`). File `.md` ghi chú nội bộ không cần ngày.
- Phiên bản: bản đầu không ghi số; từ lần sửa 2 thêm ` v2`, ` v3` trước đuôi file.
- Tên tiếng Việt, mô tả đủ để tìm không cần mở file, tối đa ~60 ký tự, không dùng `/ \ : * ? " < > |`, không viết tắt khó hiểu.
- Định dạng mặc định: báo cáo/kế hoạch narrative → `.docx` (skill `docx`); bảng số liệu → `.xlsx` (skill `xlsx`); trình bày → `.pptx`; content/script → `.md`.
- **Fallback khi chạy trên cloud / máy khác** (không có `~/claude/outputs`): lưu vào `outputs/` trong thư mục làm việc hiện tại với cùng cấu trúc, và báo Sếp đường dẫn đầy đủ.
