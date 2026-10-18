# Báo cáo liên kết cũ — 19/10/2026

[← README](README.md)

## Kiểm tra thực tế trên GitHub Actions (19/10/2026)

**Đã chạy trên GitHub-hosted runner** ở [lượt #39155780262](https://github.com/GiaHung07/Public-Stuff/actions/runs/39155780262):

- **46 link Drive/Docs khác nhau:** gồm 44 link từ README cũ và 2 link từ README con.
- **13 link trả HTTP 404/410** (12 link 404 và 1 link 410). Điều này chứng minh không truy cập công khai được trong lượt kiểm tra, **không chứng minh chắc file đã bị xóa**, vì quyền chia sẻ Google cũng có thể khiến request trả 404.
- **33 link trả HTTP 200** nhưng chưa có bằng chứng danh sách file/tài liệu được xem; **không được gắn nhãn còn sống**.
- Kết quả chi tiết từng link nằm trong artifact `legacy-drive-audit`, gồm JSON và Markdown; chưa kiểm chứng bằng browser đăng xuất trong lượt này.

Dự án đã bổ sung trình kiểm tra phiên bản cũ thay vì chỉ kiểm tra link đã được chọn lọc. Về độ tin cậy, chính trang Google Drive và quyền truy cập cuối cùng vẫn phải xác minh bằng trình duyệt khi kết quả không rõ.

## Kết quả kiểm kê

- README cũ có 631 dòng và khoảng 259 URL theo mẫu quét phổ biến (bao gồm URL trùng).
- Có **44 liên kết Drive/Docs trong README**; thêm 2 link Drive trong README con của TV và Cursor.
- Web reader không truy xuất được phần lớn Google Drive; thông báo unavailable/403 không phải bằng chứng 404.
- Hai thư mục Civil War và Tintin có metadata trong chỉ mục tìm kiếm cũ, nhưng chưa được xác thực truy cập hiện tại.
- Link cũ vẫn có thể xem lại tại commit Git **4c1f034**. Không xóa các file nhị phân gốc.

## Danh sách Drive/Docs đã rút khỏi danh mục hiện hành

| # | Tên mục trước đây | Dòng README gốc | Trạng thái |
|---:|---|---:|---|
| 1 | Tất cả App 😵‍💫 | 12 | Chưa xác minh công khai |
| 2 | Adobe 2022 | 15 | Chưa xác minh công khai |
| 3 | Của da.tuu.1810 | 16 | Chưa xác minh công khai |
| 4 | Trọn bộ Photoshop | 17 | Chưa xác minh công khai |
| 5 | Mấy thứ linh tinh cho Photoshop | 18 | Chưa xác minh công khai |
| 6 | Luts Evanto Free GFXVIET.NET | 19 | Chưa xác minh công khai |
| 7 | Phần mềm backup bản quyền | 38 | Chưa xác minh công khai |
| 8 | Voz TRUYỆN Doraemon | 53 | Chưa xác minh công khai |
| 9 | Khoá học tổng hợp | 57 | Chưa xác minh công khai |
| 10 | Tài liệu học ngoại ngữ | 60 | Chưa xác minh công khai |
| 11 | Tài liệu tổng hợp | 63 | Chưa xác minh công khai |
| 12 | Khoá học Premiere Pro 2 | 66 | Chưa xác minh công khai |
| 13 | Thiết kế - Dựng phim | 68 | Chưa xác minh công khai |
| 14 | Album sách | 72 | Chưa xác minh công khai |
| 15 | Book | 123 | Chưa xác minh công khai |
| 16 | Movie Theme | 124 | Chưa xác minh công khai |
| 17 | Orienting Child | 125 | Chưa xác minh công khai |
| 18 | Kịch | 126 | Chưa xác minh công khai |
| 19 | Powerpoint | 127 | Chưa xác minh công khai |
| 20 | Book 2 | 128 | Chưa xác minh công khai |
| 21 | Book 3 | 129 | Chưa xác minh công khai |
| 22 | Various | 130 | Chưa xác minh công khai |
| 23 | Book for Developer | 131 | Chưa xác minh công khai |
| 24 | Movie Good | 132 | Chưa xác minh công khai |
| 25 | CSS | 133 | Chưa xác minh công khai |
| 26 | Book 4 | 134 | Chưa xác minh công khai |
| 27 | Book 5 | 135 | Chưa xác minh công khai |
| 28 | Ninja Go | 136 | Chưa xác minh công khai |
| 29 | Combat Footage | 137 | Chưa xác minh công khai |
| 30 | Pooh | 138 | Chưa xác minh công khai |
| 31 | Forbidden | 139 | Chưa xác minh công khai |
| 32 | Various 2 | 140 | Chưa xác minh công khai |
| 33 | Freepik | 141 | Chưa xác minh công khai |
| 34 | IDKI | 142 | Chưa xác minh công khai |
| 35 | Football | 143 | Chưa xác minh công khai |
| 36 | Comic | 144 | Chưa xác minh công khai |
| 37 | Civil War | 145 | Chưa xác minh công khai |
| 38 | Runaways | 146 | Chưa xác minh công khai |
| 39 | Tintin | 147 | Chưa xác minh công khai |
| 40 | Xmas Show | 148 | Chưa xác minh công khai |
| 41 | Music Learn | 149 | Chưa xác minh công khai |
| 42 | Book 6 | 150 | Chưa xác minh công khai |
| 43 | Anesthesia | 151 | Chưa xác minh công khai |
| 44 | Tổng hợp Android TV apps | 426 | Chưa xác minh công khai |

Thêm 2 link Drive trong phần TV (BeeTV backup) và Cursor (Google Drive backup) cũng không được giới thiệu nữa.

## Có bằng chứng đã lỗi thời

| Mục | Trạng thái có cơ sở | Nguồn |
|---|---|---|
| Heroku free dyno 550 giờ | Dịch vụ free dyno đã dừng 28/11/2022 | [Heroku](https://devcenter.heroku.com/changelog-items/2502) |
| YouTube Vanced | Dự án ngừng phát triển từ tháng 3/2022 | [TeamVanced](https://github.com/TeamVanced/Vanced) |
| File APK TV mod / Windows crack trong repo | Tính an toàn và vận hành chưa xác minh | Không giới thiệu như bản download an toàn |

## Nguyên tắc xử lý

- **OK:** server phản hồi thành công, chưa xác nhận nội dung bên trong.
- **REDIRECT:** theo dõi URL cuối; không coi như còn nguyên tài nguyên.
- **BROKEN_404_410:** server xác nhận không thấy hoặc tài nguyên đã gone.
- **AUTH_OR_RATE_LIMIT:** 401/403/429 không kết luận link chết.
- **NETWORK_ERROR:** lỗi mạng/DNS/TLS/timeout, thử lại.
- **MANUAL_CHECK_REQUIRED:** Google Drive/Docs, playlist YouTube cần kiểm tra bằng trình duyệt và nội dung.

Chưa có bằng chứng đủ để kết luận 100% link trong README cũ là sống/chết. Các link chưa chứng thực chỉ bị loại khỏi bảng link khuyến nghị, không được ghi sai trạng thái.

[README cũ](https://github.com/GiaHung07/Public-Stuff/blob/4c1f034829f112b4b57240623e101a0d594b0ecc/README.md)