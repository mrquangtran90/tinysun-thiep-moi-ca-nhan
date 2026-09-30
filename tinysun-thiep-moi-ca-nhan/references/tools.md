# Dùng script với SVG nhiều lớp

Các script không sinh nhân vật. Bước thay người/trang phục/dáng luôn dùng `image_gen`, rồi mới lắp ảnh đã kiểm vào mẫu.

## Runtime

Python 3 chỉ dùng thư viện chuẩn cho `template_layers.py`. Node + Sharp dùng để render SVG. Nếu chưa có runtime trên PATH, gọi công cụ workspace dependencies để tìm bản được cấp sẵn. Truyền thư mục `node_modules` đó qua `--modules`; không đoán đường dẫn người dùng khác. Không tự mua/cài dịch vụ.

## Lệnh

Ví dụ dùng đường dẫn tuyệt đối thật và thư mục output mới đã qua cổng pCloud:

```text
python template_layers.py inspect --template "template.svg"
python template_layers.py extract --template "template.svg" --layer portrait-background --out "portrait-to-edit.png"
# Xem portrait-to-edit.png và ảnh khách, gọi image_gen, xem ảnh trả về.
python template_layers.py replace --template "template.svg" --layer portrait-background --portrait "portrait-reviewed.png" --out "Khach-A-v1.svg" --field guest-name --value "NGUYỄN MINH ANH"
node render_svg.cjs --svg "Khach-A-v1.svg" --out "Khach-A-v1" --modules "runtime/node_modules"
```

`inspect` trả kích thước, lớp ảnh và trường chữ nhưng không in base64 ảnh. `extract` chỉ trích ảnh nhúng nguyên gốc, không chỉnh hình.

`replace` giữ tọa độ, nền vector, logo và chữ khác; thay href của đúng layer. Chỉ `--field` được đổi text. Nếu cần thu gọn tên sau khi kiểm ảnh, thêm `--font-size 34 --letter-spacing 1.5`; không tự đổi nội dung tên. Font/spacing chỉ được phép đổi trên field đã chỉ định. Field nhiều dòng/tspan cần workflow chỉnh lớp khác, script từ chối.

Kết quả JSON của `replace` có SHA-256 nguồn/kết quả và `protected_structure_unchanged`. Digest chứng minh các node ngoài vùng sửa không đổi; **không** chứng minh AI giữ nguyên khuôn mặt/nền trong ảnh portrait. Kiểm thị giác riêng.

`render_svg.cjs` tạo `.png`, `.jpg`, `-preview.png`, `-render.json`. SVG nguồn giữ nguyên; output phải chưa tồn tại. Không mở liên kết mạng, không thực thi script từ SVG. Chỉ hỗ trợ SVG tĩnh tự chứa đã kiểm bằng `template_layers.py`; ảnh remote, script, foreignObject, DOCTYPE/entity và CSS external bị từ chối. Renderer cũng chặn tài nguyên ngoài. Một SVG hợp lệ không đảm bảo font máy khác giống; kiểm ảnh sau render.

## Kiểm thử

```text
python -m unittest discover -s tests -v
```

Chạy từ thư mục skill. Test kiểm scope thay lớp/text, giữ nguyên nguồn, chống ghi đè, lỗi ID/mẫu, XML escaping tên. Test không đo chất lượng khuôn mặt hoặc tư thế AI. Không gọi tạo ảnh để chạy unit test.
