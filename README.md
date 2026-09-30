# TinySun - Thiệp mời cá nhân hóa

Skill Codex dùng để cá nhân hóa thiệp mời từ ảnh khách: giữ nhận diện, thay đúng trường tên, xử lý mẫu phẳng hoặc mẫu có lớp, và kiểm tra ảnh trước khi bàn giao.

## Cài bằng Codex

Gửi yêu cầu sau trong Codex:

```text
Cài skill từ https://github.com/mrquangtran90/tinysun-thiep-moi-ca-nhan với path tinysun-thiep-moi-ca-nhan
```

## Cài bằng script hệ thống

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo mrquangtran90/tinysun-thiep-moi-ca-nhan \
  --path tinysun-thiep-moi-ca-nhan
```

Trên Windows, thay `~/.codex` bằng `%USERPROFILE%\.codex` nếu shell không tự mở rộng `~`.

Sau khi cài, skill nằm tại:

```text
~/.codex/skills/tinysun-thiep-moi-ca-nhan
```

Skill sẽ khả dụng từ lượt làm việc tiếp theo của Codex.

## Yêu cầu

- Codex có công cụ tạo/chỉnh ảnh tích hợp.
- Ảnh khách đủ rõ để đối chiếu khuôn mặt.
- Mẫu thiệp hoặc preset phù hợp với yêu cầu hiện tại.

Các đường dẫn pCloud trong skill là quy ước tùy chọn dành cho quy trình TinySun; máy khác cần cấu hình `TINYSUN_PCLOUD_OUTPUT_ROOT` hoặc chọn thư mục bàn giao phù hợp.
