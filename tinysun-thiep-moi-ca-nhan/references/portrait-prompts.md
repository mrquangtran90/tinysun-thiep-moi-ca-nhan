# Prompt tạo nhân vật theo mẫu thiệp

Điền các biến từ ảnh đã xem, không gửi nguyên placeholder. Dùng `image_gen` có sẵn. Luôn xác định rõ thứ tự/vai trò ảnh trong lời gọi. Không lấy khuôn mặt trong mẫu làm nguồn cho khách.

Đọc `portrait-quality-gates.md` trước; khi chọn/đổi đồ đọc thêm `wardrobe-and-skill-routing.md`. Chỉ dùng prompt tạo ảnh khi ảnh gốc đủ rõ để phân biệt các nét mặt. Nếu nguồn mờ/thiếu nhận diện, không sinh prompt “tái tạo mặt từ ảnh mờ” và không gọi công cụ để thử đoán; xin ảnh khác. Chọn riêng khối outfit, tóc và retouch đúng phạm vi, bỏ những lệnh mặc định trái với chỉ dẫn cụ thể của người dùng.

## Chỉnh lớp chân dung hoặc thiệp phẳng

> Edit reference image 1, the invitation [portrait/background layer OR complete invitation]. Reference image 2 is the NEW GUEST whose source photograph has already been checked for sufficiently clear facial detail. It is the sole facial identity reference. Completely replace the old person from reference 1; never blend their identities or reuse the old person's physique. Preserve the new guest's distinctive eye/brow, nose, lip and chin characteristics, their relationships, apparent age and natural hairline. Identity preservation does not require copying poor source lighting, temporary blemishes, selfie distortion or an awkward expression. Apply only the selected hair and retouch instructions below. Keep the same recognizable person, not a generic beautified substitute.
>
> Wardrobe mode: [AUTO_DIVERSE / SPECIFIED / KEEP_CURRENT, CHOOSE ONE]. [For a new outfit: dress the guest in ONE exact coordinated look: SILHOUETTE/CUT, COLOR, FABRIC, COLLAR/LAPEL, INNER LAYER and RESTRAINED ACCESSORIES, selected for the actual EVENT DRESS CODE. Do not substitute the generic black suit or copy the template guest's clothes.] [For keep_current: preserve the existing outfit and accessories exactly.] Hair mode: [ONE MODE + FILLED HAIR INSTRUCTION]. Retouch mode: [ONE MODE + FILLED STUDIO/RETOUCH INSTRUCTION]. Use [SPECIFIC STANDING POSE] with [WAIST-UP / FULL-LENGTH] crop. Fit a harmonious head-to-shoulder ratio and the available portrait slot; do not use face warping to fix an oversized head in the layout. Keep body proportions consistent with the guest source, reconstructing unseen areas conservatively. Use [SPECIFIC RELAXED EXPRESSION] without imposing the old guest's smile or copying a frozen speaking frame. Clothing, hands and fingers must be physically credible.
>
> Keep the template's background and composition. Harmonize the newly directed portrait lighting with the template, NOT with the source selfie/room illumination. [For full-length: feet are planted on the actual ground surface, with contact shadows, no floating.] Keep arms and head fully within the designated portrait space; leave [TEXT/NAMEPLATE REGIONS] clear. Keep the original canvas/aspect ratio. Do not introduce new graphics, podiums, decorations or text.
>
> [LAYER MODE: Do not render invitation text, logos, badges or names; those are protected separate layers.] [FLAT MODE: Preserve every existing word, accent, logo, QR code, date, title, company detail and graphic outside the authorized portrait/name region. Do not redesign the invitation. Change only the expressly authorized text: ...]
>
> Final result: realistic, restrained luxury portrait seamlessly integrated into the existing invitation, not a new standalone poster, not a collage comparison.

## Khối studio và retouch — chọn đúng phạm vi

**`studio_luxury`**, thiệp mới hoặc yêu cầu sửa chất lượng chân dung:

> Re-create the guest as a professionally photographed luxury studio portrait, not a pasted selfie face. Lighting: [SPECIFIC KEY DIRECTION] large softbox slightly above eye level, gentle opposite fill retaining soft facial modeling, subtle hair/rim separation on the dark background. Natural eye catchlights, no glare hiding eyes behind glasses. Correct the source color cast and flat overhead illumination. Match skin, neck, ears and hands under one coherent light setup.
>
> Beauty retouch: clean and gently brighten the complexion, even skin tone, reduce temporary blemishes, redness, oily hotspots and tired under-eye shadows while retaining real fine skin texture, apparent age and the person's natural undertone. Makeup: [SPECIFIC GROOMING OR REFINED EVENT MAKEUP]. No plastic skin, chalk-white face, heavy generic filter or identity-changing makeup.
>
> Face balance: first correct the close-selfie perspective and head/body composition toward a natural studio-portrait perspective. [If mild contour refinement is warranted and permitted: subtly refine cheek/jaw fullness for a more harmonious face; preserve distinctive eyes, nose, lips, recognizable chin and their relationships. Keep realistic anatomy; no generic V-shaped chin, globally squeezed skull or elongated neck.] [If face shaping is forbidden: do not geometrically slim or reshape the face.] Use a relaxed, confident expression with natural eyes and mouth, not a forced grin or invented perfect teeth. Do not change the guest into another person.

Điền một lựa chọn, không gửi hai nhánh bóp mặt/cấm bóp mặt cùng nhau. Ví dụ ánh sáng cho nền tối/gold: key mềm từ trước-trái cao nhẹ, fill phải nhẹ và rim mảnh. Phong cách nam có thể dùng `discreet complexion grooming, tidy brows and healthy natural lips, no visible glam makeup`; nữ có thể dùng `refined thin-base evening makeup, softly defined brows/eyes, balanced blush and natural rose lips` nếu hợp ảnh và trang phục.

**`keep_original`**, khi người dùng yêu cầu giữ mặt nguyên hoặc phạm vi chỉ sửa tóc/tên:

> Preserve the current approved facial appearance and expression. Do not brighten skin, remove skin details, add makeup, slim cheeks or reshape the face. Change only the explicitly requested elements. Lighting changes, if any, are limited to the user's stated scope.

## Chốt một outfit, không lặp công thức mặc định

Dùng `wardrobe-and-skill-routing.md` để chọn một bộ theo sự kiện và phần thân nhìn thấy. Lấy các thuộc tính cụ thể đưa vào prompt; không gửi toàn bộ bảng phong cách cho công cụ tự chọn/trộn. Khác biệt nằm ở phom và ít nhất một chi tiết khác nhìn thấy được, khi brief cho phép; không chỉ đổi màu một bộ suit.

Ví dụ nam hội chợ ban ngày: `a tailored taupe textured blazer with notch lapels, ivory open-collar shirt and dark espresso trousers; restrained styling, one hand lightly adjusting the jacket button, other arm relaxed`. Chỉ mô tả giày/quần chi tiết nếu crop nhìn thấy hoặc cần giữ cùng bộ.

Ví dụ nữ gặp đối tác: `an ivory structured pantsuit with a single-breasted jacket and refined silk blouse, small pearl studs, hands resting lightly in front of the waist`. Không tự gắn phụ kiện nổi bật, đầm dạ hội hoặc makeup đậm chỉ vì là phong cách nữ.

Ví dụ nữ gala đã xác nhận: `a deep emerald crepe evening gown with a clean boat neckline and softly structured cape sleeves, discreet earrings, one hand relaxed at the waist`. Đây không phải bộ mặc định cho Vietbaby ban ngày.

Khi có ảnh đồ mẫu, gán nó là tham chiếu TRANG PHỤC duy nhất, không lấy mặt/thân người mẫu làm identity. `keep_current` chỉ dùng block giữ đồ; bỏ mọi câu đổi bộ. Yêu cầu trang phục/tóc cụ thể của người dùng thắng gợi ý; không suy giới tính từ tên.

## Khối tóc — chỉ đưa một chế độ vào prompt

Chọn kiểu cụ thể trước khi gọi công cụ, không đưa nhiều lựa chọn trái nhau. Giữ màu tóc/đường chân tóc tự nhiên trừ thay đổi được yêu cầu rõ. Tóc mới không tự cho phép đổi nhận diện hoặc tuổi; chỉnh da/đường mặt nếu có chỉ theo khối retouch đã chọn, không phát sinh thêm từ bước tóc.

**`auto_event`** — điền một kiểu đã chọn theo trang phục và độ dài tóc nhìn thấy:

> Restyle the guest's hair into [CHOSEN EVENT HAIRSTYLE], coordinated with [OUTFIT AND NECKLINE] for [EVENT FORMALITY]. Preserve the original natural hair color, hairline and plausible density. Arrange the existing length realistically; do not add extensions, dramatically cut the hair or let hair styling alter the forehead, ears, age or identity. Facial retouch is governed only by the separate selected retouch instruction. Photorealistic individual strands, natural scalp/temple attachment, no wig effect. Keep eyes, important facial features, logo and text unobstructed. No tiara, large ornaments or new headwear.

Ví dụ nữ tóc dài, đầm cổ thuyền xanh ngọc: `a soft low chignon at the nape, subtle natural side part and a few controlled soft strands, refined rather than bridal`. Ví dụ nữ tóc ngang vai: `polished soft waves at her existing shoulder length, neatly tucked on one side`. Ví dụ nam tóc ngắn, suit: `a neat natural side part with restrained volume at the existing hair length`.

**`keep_original`**:

> Keep the guest's original hairstyle, parting, hair length, color, texture and hairline unchanged. Adjust only illumination on the hair to match the selected scene lighting. This hair constraint does not override the separately selected facial retouch scope. Do not restyle, curl, tie, cut or add hair accessories.

**`specified`**:

> Change only the hairstyle to [USER'S EXACT STYLE], using [OPTIONAL HAIR REFERENCE] for hair arrangement only, never for the face. Preserve the guest's facial identity, natural hairline and age. Keep original hair color and realistic length unless the user explicitly requested a change to those. Keep all protected invitation content unobstructed.

## Chỉ sửa tóc của thiệp đã có

Giữ tóc hiện tại nếu yêu cầu chỉ sửa tên/chữ. Khi tóc là phần được sửa, chọn chế độ/kiểu như trên rồi dùng:

> Reference 1 is the existing portrait layer/invitation to edit. Reference 2 is the original guest identity photo. Change ONLY the HAIR to [SELECTED HAIR INSTRUCTION]. Keep the current face size, position, expression, eyes, nose, mouth, facial structure, age and skin tone, as well as the current clothing, hands, pose, body and all background/graphic/text/logo layers. The original identity photo is for the guest's face, not an instruction to revert the approved outfit or pose. Blend hair edges naturally at scalp, ears, neck and collar. No unrelated edits.

## Sửa lỗi cục bộ

> Keep the composition, new guest identity, clothing, approved hairstyle, event graphics and all correct details unchanged. Fix ONLY [OBSERVED DEFECT]. Success condition: [VISIBLE CHECK]. Use the original guest photo as facial identity reference again; do not revert the selected hairstyle unless hair itself is the requested correction, and do not use the template person's face. Do not change unrelated elements.

Ví dụ lỗi: ngón thừa; tay che bảng tên; vai quá rộng; chân không tiếp đất; ánh sáng/da chưa đạt. Với mặt khác người, chỉ sửa bằng ảnh gốc đủ rõ; thiếu căn cứ phải xin ảnh khác, không dùng block này để tiếp tục đoán. Phải xem ảnh xác nhận lỗi trước, không tạo vấn đề giả để sửa.

## Mẫu Vietbaby 26.9.26

Đọc preset JSON để biết lớp cần thay. Nền chân dung gốc có người, không phải nền sạch. Edit người trong lớp đó; giữ vòng kim loại/nền xanh đen, không thêm chữ, giữ vị trí đầu/thân để không chạm logo bên trên hoặc plaque bên dưới. Mọi chữ sự kiện/logo là lớp SVG riêng. Thông tin 15–18/10/2026 không áp dụng cho sự kiện khác.
