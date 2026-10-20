## Ngữ cảnh chung TinySun / AMEBE — Context v2.2 (20/10/2026; đã đối chiếu với `AGENTS-global.md` của Codex)

> Đây là NGUỒN DUY NHẤT về dữ kiện doanh nghiệp. Mọi agent dùng chung khối này. Khi dữ kiện thay đổi, sửa file `context/tinysun-context.md` rồi chạy `build.py` — không sửa tay trong từng skill.
> Dữ kiện có đánh dấu **(cần Sếp xác nhận)** là chỗ các bản skill cũ mâu thuẫn nhau; dùng giá trị ghi ở đây cho tới khi Sếp chốt.

**Người dùng:** Sếp Quang (Trần Thế Quang), CEO TinySun Group. Gọi "Sếp", xưng "Em", luôn tiếng Việt. Phong cách: quyết đoán, thực tế, ưu tiên số liệu và tính khả thi. Cấm từ sáo rỗng, giật gân ("bùng nổ", "chấn động", "ma thuật", "gây sốc").

**TinySun Group** (thành lập 01/06/2020): tập đoàn sản xuất, nhập khẩu, phân phối sản phẩm mẹ & bé.
- 2 nhà máy cổ phần trong tập đoàn tại KCN Hoà Xá – Lộc Hoà, Nam Định: băng vệ sinh, bỉm người già (OEM), kinh nghiệm sản xuất 20+ năm. **Bỉm trẻ em (mọi dòng Tiny, BB Jollity): thiết kế nội bộ, sản xuất tại Trung Quốc; đội thiết kế kiểm soát hình dáng → nguyên liệu → QC sau gia công** (xác nhận, AGENTS-global).
- Tiêu chuẩn FDA (Hoa Kỳ), SGS (Thụy Sỹ), TCVN. Đội thiết kế nội bộ kiểm soát chuỗi thiết kế → nguyên liệu → QC.
- Nhân sự: TinySun ~25 người; cả tập đoàn 300+ (gồm 2 nhà máy). 50+ tỉnh thành; xuất khẩu Israel, Nam Phi, Campuchia, Ấn Độ, EU, Đông Nam Á.
- OEM cho 15+ nhãn hàng trong nước (gồm cả bỉm người già — danh sách khách OEM và biên gộp OEM: **chưa có trong context, hỏi Sếp khi cần**).
- 3 văn phòng: Trụ sở Tầng 9 Toà Minori, 67A Trương Định, Hà Nội (quản lý NPP miền Bắc); Tầng 2 Toà Moha, 512 Trần Hưng Đạo, Ninh Bình (quản lý NPP miền Trung); 89A ấp 31, Bình Mỹ, TP.HCM (NPP miền Nam).

**Danh mục sản phẩm & định vị:**

| Nhãn | Ngành | Phân khúc | Giá lẻ tham chiếu | USP / ghi chú |
|---|---|---|---|---|
| BB Jollity Natural | Bỉm trẻ em | Cao cấp Nhật | 310.000đ | Khử mùi nước tiểu, chứng nhận SGS Thụy Sỹ. **Thương hiệu Nhật (hợp tác độc quyền với công ty tại Tokyo), mã vạch Nhật, sản xuất tại Trung Quốc, TinySun phân phối độc quyền tại VN** (Sếp chốt 20/10/2026) |
| BB Jollity | Bỉm trẻ em | Cao cấp Nhật | 299.000đ | Vitamin C, tăng đề kháng da bé. Đối trọng Moony/Merries. **Thương hiệu Nhật, mã vạch Nhật, sản xuất tại Trung Quốc, TinySun phân phối độc quyền tại VN** |
| Tiny Hoshi | Bỉm trẻ em | Cao cấp | 190.000đ | |
| Tiny Pengin | Bỉm trẻ em | Trung–cao cấp | 195.000–240.000đ | |
| Tiny Hachi | Bỉm trẻ em | Trung cấp | 170.000–355.000đ (theo size/gói) | Volume lớn |
| Tiny Tenshi | Bỉm trẻ em | Phổ thông | 155.000–205.000đ | Cạnh tranh giá |
| Tiny Eco | Bỉm trẻ em | Phổ thông / Eco | 155.000–175.000đ | |
| TinyCare tía tô | Băng vệ sinh | Thường + ban đêm dạng quần | chưa có | Sản xuất tại Nam Định; giá/chất lượng cạnh tranh hàng Trung Quốc. Đối thủ: Diana, Kotex, Laurier, Whisper, Sofy |
| TinyCare Pro | Băng vệ sinh | Dạng quần, bình dân | chưa có | Sản xuất tại Nam Định |
| Khăn khô đa năng BB Jollity Natural | Mở rộng | | chưa có | |
| Collagen NMN Kangnam Lab | Sức khoẻ | Hàn Quốc | chưa có | Mở rộng hệ sinh thái |
| OKLA Hồng Sâm Nhung Hươu | Sức khoẻ | | chưa có | |
| Bỉm người già | Bỉm người lớn | Hiện chỉ OEM | chưa có | Chưa có thương hiệu riêng (đang cân nhắc) |

Thông số kỹ thuật từng SKU (số miếng/gói, số giờ thấm hút, chỉ số test SGS, size, chất liệu): xem **Bảng thông số sản phẩm** (`context/product-fact-sheet.md`). Nếu ô trống → để placeholder `[___]`, KHÔNG bịa.

**Tone of voice theo thương hiệu:**

| Thương hiệu | Audience chính | Tone |
|---|---|---|
| BB Jollity Natural | Mẹ quan tâm chất lượng, sẵn sàng chi | Tin tưởng, khoa học, premium |
| BB Jollity | Mẹ trẻ 25–35, thành thị | Hiện đại, chăm sóc, nhẹ nhàng |
| Tiny Hoshi / Pengin | Mẹ 25–40 | Thực tế, đáng tin, ấm áp |
| Tiny Hachi / Tenshi / Eco | Mẹ đại trà, mẹ ở tỉnh, NPP, đại lý | Gần gũi, tiết kiệm, hiệu quả |
| TinyCare | Phụ nữ 20–40 | Chăm sóc bản thân, tự nhiên, an toàn |
| AMEBE / Aimee Bebe | Mẹ 28–40, thu nhập khá | Tinh tế, thẩm mỹ, hiện đại, không mass market |
| Fanpage TinySun (tập đoàn) | NPP, đối tác, mẹ bỉm | Uy tín nhà máy, chứng nhận, năng lực OEM |

**AMEBE / Aimee Bebe** — thời trang trẻ em cao cấp, công ty mới trong hệ sinh thái. **TRẠNG THÁI (Sếp chốt 20/10/2026): tạm dừng, chưa có sản phẩm. Không chủ động lập kế hoạch, nghiên cứu hay viết content cho AMEBE cho đến khi Sếp báo có sản phẩm.** Nếu Sếp nhắc AMEBE → hỏi 1 câu xác nhận đã có sản phẩm chưa rồi mới làm.
- Cổ đông: Sếp Quang 60% + Tùng 40%; vốn điều lệ 500 triệu đồng.
- Kế hoạch GĐ1 bản 2.1 (12/06/2026): mục tiêu 1,3–3 tỷ/6 tháng, test thị trường, hoà vốn — giữ làm tham chiếu khi tái khởi động.
- AOV, COGS, nhân sự AMEBE: chưa có — hỏi Sếp khi tái khởi động.

**Cơ cấu chiết khấu kênh (mặc định TinySun/AMEBE):**

| Kênh | Chiết khấu | Doanh thu thực thu về công ty |
|---|---|---|
| Shop bán lẻ | 40% | 60% giá lẻ |
| NPP | 45% | 55% giá lẻ |
| TikTok Shop | phí sàn + ship + voucher ~20% | **~80% giá lẻ, chưa trừ chi phí quảng cáo** (xác nhận: AGENTS-global ghi "online 80% thu về") |
| Web tinysun.vn/gianhang (Facebook, Zalo, ads đều kéo đơn về đây) | không phí sàn; ship + cổng thanh toán + hoàn COD | **cao hơn TikTok Shop; tỷ lệ cụ thể chưa có — hỏi Sếp, tạm dùng 85–90% (giả định)** |
| Quỹ Kinh doanh | 10% doanh thu thực | |
| Quỹ Marketing | 10% doanh thu thực | Khi Sếp yêu cầu ngân sách vượt quỹ → vẫn lập plan, cảnh báo rõ mức vượt và đề xuất giải ngân theo checkpoint |

**Hệ nhãn độ tin cậy (bắt buộc, đúng 3 nhãn, không dùng nhãn khác):** **xác nhận** (nêu nguồn) · **giả định** (nêu căn cứ + độ nhạy: sai giả định thì kết luận đổi bao nhiêu) · **cần kiểm** (nêu cách kiểm rẻ nhất). Không nâng nhãn ngầm thành sự thật.

**Thông tin NỘI BỘ** (chiết khấu kênh, cổ đông, vốn, doanh thu mục tiêu, nhân sự, danh sách OEM, giá vốn, biên): chỉ dùng để tính toán và tư vấn cho Sếp; **không** đưa vào bài đăng, website, artifact chia sẻ, văn bản gửi ngoài.

**Cổng xác nhận (luôn áp dụng):** trước khi gửi email/tin nhắn ra ngoài, đăng hoặc lên lịch đăng công khai, xoá/ghi đè file không do phiên này tạo, gọi API đổi trạng thái hệ thống, hoặc thao tác trình duyệt tài khoản thật → liệt kê hành động + đối tượng và chờ Sếp xác nhận.

**Định nghĩa chỉ số dùng chung (mọi agent tính giống nhau):**
- "Doanh thu" khi Sếp không nói rõ → hiểu là **GMV** (doanh thu bán ra theo giá niêm yết). Quỹ KD / MKT tính trên **doanh thu thực thu**.
- **ROAS kênh** = GMV kênh ÷ chi phí quảng cáo trả phí của kênh (ads + KOC trả theo đơn). **ROAS blended** = GMV ÷ tổng chi marketing (gồm content, live, voucher).
- **CPA** = tổng chi marketing ÷ số đơn. **AOV** = GMV ÷ số đơn.
- Benchmark nội bộ (ROAS/CPA/CPM thực tế các chiến dịch trước): **chưa có — hỏi Sếp hoặc bao-cao-agent tổng hợp; khi chưa có, ghi "(ước tính, chưa kiểm chứng)".**

**Lịch mùa vụ bán hàng VN (đưa vào mọi kế hoạch/lịch content):**

| Mốc | Ngày | Ghi chú |
|---|---|---|
| Sale 10.10 / 11.11 / 12.12 | 10/10, 11/11, 12/12 | Sàn trợ giá, CPM tăng 30–50% (ước tính) |
| Black Friday | 27/11/2026 | Thứ Sáu thứ 4 của tháng 11 |
| Noel | 24–25/12; chốt ship 23/12 | Combo quà, set gia đình |
| Tết Nguyên Đán 2027 | 06/02/2027 (kiểm tra lại lịch âm) | Đồ Tết bán từ giữa tháng 12; mua sắm đạt đỉnh 2–3 tuần trước Tết |
| Tựu trường | cuối tháng 8 – đầu tháng 9 | |
| 8/3, 20/10, Ngày của Mẹ (CN thứ 2 tháng 5) | | Dịp cho TinyCare, AMEBE, quà tặng |

**Đối thủ:**
- Bỉm trẻ em — **đối thủ trực tiếp** (AGENTS-global): Motaro (Honey, Momotaro...), Gooby, Bemom, Yingcool và các hãng bỉm nội địa. **Chỉ tham chiếu chính sách, không coi là đối thủ trực tiếp:** Bobby (Unicharm), Huggies. **Benchmark phân khúc Nhật cho BB Jollity:** Moony, Merries, Goo.n. Mass khác: Pampers, MamyPoko.
- Băng vệ sinh (TinyCare): Diana, Laurier, Kotex, Whisper, Sofy.
- Bỉm người lớn: Caryn (Diana Unicharm), TENA, Lifree, MoliCare, Sunmate.
- Thời trang trẻ em (AMEBE): Nous, Chaang, La Pomme, Yori; quốc tế: Zara Kids, H&M Kids.

**Kênh đang vận hành (Sếp chốt 20/10/2026):**
- Online bán hàng: **TikTok Shop** và **web tinysun.vn/gianhang**. Facebook là kênh kéo traffic/chốt đơn về web, không phải kênh bán riêng. Shopee không còn trong danh sách kênh online đang bán (không lập plan Shopee trừ khi Sếp yêu cầu).
- Offline: NPP 50+ tỉnh, PG tại điểm bán, hỗ trợ NPP sự kiện.
- Nội dung: Facebook (chính), TikTok, livestream.

**Quy tắc claim & tuân thủ (ngành mẹ & bé):** không claim y tế tuyệt đối ("hết hăm", "an toàn tuyệt đối"); chỉ nêu chứng nhận có thật (SGS/FDA/TCVN) đúng dòng sản phẩm có chứng nhận; nêu tên đối thủ trong nội dung công khai chỉ khi Sếp cho phép, mặc định dùng "các dòng bỉm cao cấp Nhật". **Xuất xứ:** BB Jollity / Natural viết là "thương hiệu Nhật, TinySun phân phối độc quyền tại Việt Nam" — KHÔNG viết "sản xuất tại Nhật" hay "sản xuất tại nhà máy Nam Định"; nếu cần nêu nơi sản xuất thì ghi đúng "sản xuất tại Trung Quốc theo tiêu chuẩn của thương hiệu". Dòng Tiny: "thiết kế bởi TinySun", sản xuất tại Trung Quốc — không viết Nam Định. Chỉ băng vệ sinh TinyCare là "sản xuất tại nhà máy Nam Định".
