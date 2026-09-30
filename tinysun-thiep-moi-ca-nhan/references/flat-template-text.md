# Thay tên chính xác trên mẫu JPG/PNG phẳng

Đọc khi mẫu raster phẳng có trường tên, chức danh hoặc placeholder cần cá nhân hóa. Mục tiêu là thay đúng chữ mà không làm model ảnh vẽ lại logo, ngày, địa điểm hoặc phần thiết kế đã đạt.

## 1. Lập bản đồ cá nhân hóa

Ghi trước khi sửa:

- tên khách và nguồn tên `chat`, `filename` hoặc `confirmed`;
- chuỗi nguồn đang nhìn thấy trong vùng tên;
- chuỗi đích chính xác, gồm viết hoa và dấu tiếng Việt;
- hộp giới hạn `x, y, width, height` và vùng an toàn;
- vùng nền/viền phải giữ;
- font, weight, cỡ, màu, căn dòng và letter spacing nếu xác định được;
- bản ảnh đầu vào dùng làm nguồn cho lần sửa chữ.

Khi brief đã có tên khách và ô dành cho khách còn một nhãn chung như “NHÀ PHÂN PHỐI - SHOP MẸ & BÉ”, thay toàn bộ nhãn chung bằng tên khách. Không coi việc thay ảnh là đã hoàn tất cá nhân hóa. Chỉ giữ nhãn chung khi người dùng yêu cầu rõ giữ nguyên chữ.

Nếu chat chưa nói tên nhưng file ảnh có stem giống tên người, dùng stem đó sau khi bỏ phần mở rộng và đổi `_`/`-` thành khoảng trắng. Không tự thêm dấu tiếng Việt hoặc danh xưng không có trong tên file. Tên số/hash/timestamp, mã camera/tải xuống và các stem chung như `IMG_1234`, `DSC_0001`, `Screenshot` không hợp lệ; phải hỏi người dùng. Nếu tên chat và tên file mâu thuẫn, hỏi mapping trước khi sửa.

Ví dụ:

| Chat | File ảnh | Kết quả |
|---|---|---|
| Chưa nêu tên | `Mrs_Tran_Chung.jpg` | Dùng `Mrs Tran Chung`, `name_source=filename` |
| `Mrs Trần Chung` | `1790610125430.jpg` | Dùng `Mrs Trần Chung`, `name_source=chat` |
| Chưa nêu tên | `IMG_2039.jpg` | Hỏi tên khách |
| `Nguyễn Minh An` | `Tran_Thu_Ha.jpg` | Hỏi xác nhận mapping |

## 2. Chọn font có bằng chứng

Ưu tiên theo thứ tự:

1. font và thông số từ SVG/PSD/Canva hoặc metadata của template;
2. font được cấu hình trong preset/brand kit của đúng mẫu;
3. font Việt hóa hợp lệ đã có trong asset dự án;
4. một font thay thế có đủ glyph tiếng Việt, được so trực quan cạnh mẫu ở kích thước thật.

Không tự rơi về Arial, Arial Black hoặc font hệ thống chỉ vì chúng có sẵn. Không khẳng định biết chính xác font từ ảnh raster nếu không có metadata. Nếu chênh lệch hình dáng chữ còn rõ và không có nguồn font, ghi **cần kiểm** và tạo tối đa hai mẫu font cục bộ để người dùng chọn; không bàn giao một font ngẫu nhiên như bản hoàn tất.

Font phải hiển thị đúng toàn bộ dấu tiếng Việt. Dấu bị tách, lệch, thiếu glyph hoặc đổi sang font fallback là lỗi chặn bàn giao.

## 3. Sửa đúng lớp

- Ưu tiên sửa field trong file nhiều lớp.
- Với ảnh phẳng, khôi phục riêng nền của hộp tên bằng clean plate/asset gốc hoặc chỉnh cục bộ có kiểm soát. Sau đó chèn chữ bằng công cụ dàn trang xác định; không yêu cầu model ảnh sinh chữ chính xác.
- Không tô một hình chữ nhật phẳng che mất texture, viền, ánh sáng hoặc nếp gấp của bảng tên. Mép vá, sọc màu và thay đổi gradient nhìn thấy ở 100% là lỗi.
- Chỉ thay hộp tên đã map. Xuất bản mới `v2`, `v3` thay vì ghi đè bản cũ.

## 4. QA bắt buộc

1. Đọc lại chuỗi đích ký tự theo ký tự, gồm dấu và khoảng trắng.
2. Xem ở kích thước thật và bản thu nhỏ 720 px: tên phải vừa khung, cân giữa và có độ tương phản đúng.
3. So hình dáng font với chữ cùng cấp trên mẫu; không chỉ kiểm “đọc được”.
4. So sánh pixel hoặc checksum vùng ngoài hộp tên khi quy trình deterministic cho phép; sai khác ngoài vùng được phép phải bằng 0.
5. Kiểm nền bảng tên không còn bóng chữ cũ, vệt vá, sọc hoặc đường nối.
6. Manifest ghi chuỗi nguồn, chuỗi đích, hộp tên, font/thông số, nguồn font và kết quả QA.

Font đúng và hash ngoài vùng đúng không chứng minh thẩm mỹ. Vẫn cần kiểm thị giác; nếu người dùng báo font sai, bản đó không đạt và không dùng làm chuẩn cho lần sau.
