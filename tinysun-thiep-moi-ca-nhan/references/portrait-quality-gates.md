# Cổng ảnh nguồn và chất lượng chân dung studio

Đọc trước mỗi lần tạo/chỉnh chân dung. Đích: khách nhận ra đúng mình nhưng được chuẩn bị trang phục, tóc, trang điểm và ánh sáng như một buổi chụp studio sang trọng. Giữ danh tính không đồng nghĩa giữ khuyết điểm và điều kiện chụp xấu; làm đẹp không cho phép đoán một khuôn mặt mới.

## 1. Đầu vào — đủ rõ mới được tạo

Xem ảnh gốc, không chỉ thumbnail. Kiểm khả năng phân biệt mắt/mí, chân mày, sống và cánh mũi, viền môi, cằm, đường mặt và đặc điểm riêng; cả ánh mắt sau kính nếu đeo kính. Tóc, màu áo, kính hay tên khách không thay thế được chi tiết khuôn mặt.

- Đủ rõ: các nét này nhìn được để đối chiếu. Ảnh có da chưa đẹp, ánh sáng phẳng hoặc ám màu vẫn có thể dùng nếu nét mặt rõ; những điểm đó xử lý ở bước studio.
- Không đủ rõ: mặt nhỏ, rung/mờ/nén nặng, che khuất/cháy sáng làm mất nét, filter bóp mặt mạnh, hoặc không chắc người được chọn. Dừng khách đó trước mọi lệnh tạo chân dung/thiệp. Không thử “khôi phục” rồi coi chi tiết AI sinh thêm là bằng chứng thật.
- Screenshot không tự động bị loại; chất lượng phần mặt mới quyết định. Không dựa vào độ phân giải toàn ảnh hoặc đặt một ngưỡng pixel như bảo đảm nhận diện. Phóng to/crop để quan sát không khôi phục dữ liệu đã mất.
- Nếu chưa chắc đủ rõ, ghi **cần kiểm** và xin ảnh khác; không tạo bản “tạm” có một khuôn mặt phỏng đoán. Một khách thiếu ảnh không chặn các khách khác đủ ảnh.

Xin đúng đầu vào cần thiết: “Sếp gửi giúp ảnh gốc chụp gần từ ngực trở lên, rõ mắt–mũi–miệng, đủ sáng, không filter làm đẹp mạnh; nhìn thẳng hoặc hơi nghiêng, không cắt mặt. Tránh ảnh chụp màn hình video bị mờ.” Không yêu cầu ảnh giấy tờ. Một ảnh rõ thường đủ; chỉ xin góc bổ sung khi góc đầu ra thực sự không có căn cứ.

## 2. Khóa nhận diện khác với khóa toàn bộ diện mạo

Ghi vài đặc điểm phân biệt nhìn được trong ảnh, không suy tính cách/tuổi chính xác/danh tính ngoài tên người dùng cung cấp. Ảnh người trong mẫu chỉ định khung và phong cách, không quyết định mặt, vóc dáng hoặc biểu cảm của khách.

Giữ tương quan và đặc điểm riêng của mắt, mũi, môi, đường chân tóc, tuổi biểu kiến, sắc độ tự nhiên và các dấu nhận diện nổi bật. Cho phép điều chỉnh chuẩn bị chụp ảnh trong phạm vi dưới đây; không biến mọi khuôn mặt thành V-line, mắt to/mũi cao giống nhau. Kính và phụ kiện nhận diện được giữ nếu không được yêu cầu đổi.

Ảnh AI trước đó không thay thế ảnh gốc. Khi người dùng báo sai nhân vật, kết quả đó không đạt và không được dùng tiếp làm identity. Với ảnh nguồn thiếu chi tiết, phải xin nguồn tốt hơn, không tiếp tục “sửa cho giống” từ chính bản sai.

## 3. `studio_luxury` — mặc định thiệp mới đủ nguồn

### Da và trang điểm

- Tái tạo màu da dưới ánh sáng sạch; nâng sáng vừa phải, đều màu, giảm ám xanh/vàng, bóng dầu, đỏ da, quầng mệt và khuyết điểm tạm thời. Giữ chuyển sắc, chi tiết da thật và tuổi, không làm mặt sáp hoặc trắng bệt; màu cổ/tai/tay phải hòa với mặt.
- Phong cách nam: retouch grooming tự nhiên, làm da sạch/sáng, môi khỏe, giảm bóng dầu; không mặc định son/mắt đậm.
- Phong cách nữ: lớp nền mỏng, mắt/mày/má/môi hài hòa với outfit và sự kiện; có thể contour nhẹ để gọn mặt. Không mặc định makeup nặng, môi quá căng, lông mi hoặc kính bị méo.
- Chỉ tăng makeup mạnh khi người dùng yêu cầu. Không tự trẻ hóa hoặc xóa đặc điểm nhận diện nổi bật chỉ vì gọi là “khuyết điểm”.

### Đầu và đường mặt hài hòa

Phân biệt trước khi sửa:

1. Đầu bị đặt quá lớn trên thân/thiệp: sửa tỷ lệ và vị trí chân dung, không bóp mặt để bù lỗi bố cục.
2. Góc selfie gần gây cảm giác mặt rộng: tái tạo phối cảnh chân dung studio và góc đầu nhẹ, không thay đổi góc đến mức phải đoán bên mặt chưa thấy.
3. Sau hai bước trên, má/hàm vẫn cần thon hơn theo yêu cầu: chỉnh gọn nhẹ có kiểm soát, phối contour và bóng tạo khối; giữ đặc điểm mắt–mũi–miệng, độ tuổi và dáng cằm nhận diện. Không co ngang cả đầu, thu nhỏ sọ, đổi cằm nhọn hoặc tăng cổ dài bất thường.

Không ép phần trăm bóp mặt chung cho mọi người. Ghi phần đã chỉnh vào brief và đối chiếu lại với nguồn. Nếu muốn chỉnh mạnh đến mức làm khác người, hỏi phạm vi trước, không tự áp dụng.

### Ánh sáng và biểu cảm studio

Tái dựng ánh sáng trên người, không bê nguyên ánh sáng phòng/selfie. Chọn setup cụ thể hợp mẫu: softbox lớn đặt chếch phía trước và cao nhẹ làm key, fill mềm phía đối diện giữ bóng có chiều sâu, rim/hair light tinh tế khi nền tối. Catchlight tự nhiên trong mắt; kính không lóa che mắt; da, tóc và vải cùng hướng sáng. Ấm/lạnh hòa nền nhưng không để ánh kim nền làm da ám vàng.

Tái tạo cảm giác ống kính chân dung tự nhiên, không méo góc rộng. Điều chỉnh đầu/ánh mắt vừa phải trong phạm vi nguồn đủ rõ. Cho cơ mặt thư giãn, miệng và mắt cùng biểu cảm; chọn nụ cười nhẹ tự tin hoặc cười răng tự nhiên nếu phù hợp. Không bắt buộc chép nguyên nét cười gượng/khung hình đang nói; không tạo bộ răng hoặc nếp miệng kỳ lạ.

## 4. Giới hạn theo yêu cầu đang làm

- Chỉ sửa tóc/tên/chữ: giữ nguyên mặt, makeup và ánh sáng đã đạt; không tự mở rộng retouch.
- “Không retouch/giữ nguyên mặt”: `retouch_mode=keep_original`, không làm sáng, bóp mặt hoặc trang điểm ngoài yêu cầu. Đừng vừa ghi giữ nguyên vừa chèn block làm đẹp.
- “Không bóp mặt”: vẫn có thể làm da/đánh sáng studio nếu được yêu cầu, nhưng loại hoàn toàn chỉnh hình học mặt khỏi prompt.
- `studio_luxury` không cấp quyền thay nhân vật, thay sự kiện, sửa logo hoặc cập nhật canon.

## 5. Hai cổng đầu ra độc lập

**Nhận diện:** xem nguồn và mặt sinh ra ở kích thước tương đương; không so mặt thumbnail với ảnh cận lớn. Kiểm riêng mắt/mày, mũi, môi/cằm, tổng thể tuổi và nét riêng. Makeup, kính hoặc tóc giống không đủ để kết luận cùng người. Không chắc hoặc người dùng báo sai → chưa đạt, không ghép tiếp như thành phẩm.

**Chân dung studio:** da được xử lý có chủ đích, ánh sáng có hướng/chiều sâu, mắt và biểu cảm tự nhiên, đầu–vai cân đối, không mặt sáp, không viền cắt ghép, không mảng cổ/tay khác màu. Ảnh đúng người nhưng thô/ánh sáng selfie vẫn chưa đạt; ảnh đẹp nhưng khác người cũng chưa đạt.

Chỉ ghép/xuất thiệp sau khi cả hai cổng đạt kiểm thị giác. Kiểm lại trên thiệp hoàn chỉnh, tên đúng người, tay/mặt không bị che và mọi chữ/logo vẫn đúng. Không dùng unit test/checksum làm bằng chứng nhận diện hay thẩm mỹ. Ghi rõ đây là kiểm bằng mắt, không bảo đảm sinh trắc; người dùng vẫn duyệt thẩm mỹ cuối, nhưng lời mời duyệt không thay thế cổng dừng khi thiếu nguồn.
