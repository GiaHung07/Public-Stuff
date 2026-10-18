# Kiểm tra URL trong Public-Stuff

Dùng Python 3 standard library, không cần pip.

    python3 tools/check_links.py --output link-report.json
    python3 tools/check_links.py README.md CATALOG.md --output curated.json
    python3 tools/check_links.py --include-drive --output drive-attempt.json

- Mặc định quét toàn bộ *.md / *.txt (trừ .git/.github); ghi JSON và không sửa nội dung.
- Google Drive/Docs/Google Groups và playlist YouTube được phân loại MANUAL_CHECK_REQUIRED nếu chưa bật include-drive.
- 401, 403, 429, timeout không được xem là link chết. Riêng M3U cần thử từng kênh.
- Thêm --fail-on-broken nếu muốn thoát mã 1 khi gặp HTTP 404/410 đã đối chiếu.
- GitHub Actions quét hàng tuần, upload artifact link-report.json; không tự commit/xóa link.

### Kiểm tra Drive thủ công

Mở bằng trình duyệt ẩn danh, xem có danh sách file thực tế hay lỗi 'does not exist', phân biệt 'request access' và 'not found'. Giữ URL có quyền truy cập hợp lệ, loại link xác nhận đã xóa.