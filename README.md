<div align="center">

# 🧰 Public-Stuff

**Kho công cụ và tài liệu công nghệ — danh mục làm mới năm 2026**

Windows · Linux · Android · iOS · AI · Developer · PDF · Media · Network · Self-host

[📚 Danh mục 68 công cụ](CATALOG.md) · [🔎 Báo cáo Drive](LINK-REVIEW.md) · [✅ Quy trình kiểm tra](docs/LINK-CHECKING.md)

</div>

---

## 🚀 Dùng ngay

| Nhu cầu | Công cụ | Điểm mạnh |
|---|---|---|
| Chuyển file Android ↔ Linux/Windows | [LocalSend](https://github.com/localsend/localsend) | Wi-Fi nội bộ, không tài khoản |
| Ghép điện thoại với KDE | [KDE Connect](https://github.com/KDE/kdeconnect-kde) | Clipboard, thông báo, gửi file |
| Điều khiển Android trên PC | [scrcpy](https://github.com/Genymobile/scrcpy) | Nhanh và nhẹ |
| Tải app Android đúng upstream | [Obtainium](https://github.com/ImranR98/Obtainium) | Theo dõi bản phát hành |
| Xử lý PDF | [Stirling PDF](https://github.com/Stirling-Tools/Stirling-PDF) | Nhiều công cụ trên web/local |
| Test REST API | [Bruno](https://github.com/usebruno/bruno) | File lưu trong Git |
| Chạy AI local | [Ollama](https://github.com/ollama/ollama) | Model chạy ngay trên máy |
| Chặn quảng cáo mạng | [AdGuard Home](https://github.com/AdguardTeam/AdGuardHome) | DNS tự host |
| Backup ảnh/video | [Immich](https://github.com/immich-app/immich) | Google Photos tự host |

## 📂 Khám phá theo nhóm

| Nhóm | Số mục |
|---|---:|
| Windows & Linux | 13 |
| Android & iOS | 11 |
| PDF & học tập | 11 |
| AI, lập trình & API | 13 |
| DNS & network | 9 |
| Video, media & IPTV | 6 |
| Backup & self-host | 5 |

👉 **[Mở CATALOG.md để xem link, mô tả, nền tảng và chi phí cho từng công cụ](CATALOG.md)**

## 🔒 Chính sách lọc link

1. Ưu tiên URL chính thức/upstream, không quảng cáo bản mod hay installer không rõ nguồn.
2. Drive/Docs cũ bị đưa ra khỏi danh mục hiện hành nếu chưa xác minh được; **không nói sai rằng bị 404**. Ghi tên ở [LINK-REVIEW.md](LINK-REVIEW.md).
3. File nhị phân cũ vẫn còn trong GitHub để không làm mất dữ liệu, nhưng được đánh dấu legacy/rủi ro.
4. Website hoạt động không có nghĩa dịch vụ dùng được; riêng M3U phải kiểm tra từng luồng.
5. [Link checker](docs/LINK-CHECKING.md) có thể chạy định kỳ bằng GitHub Actions và không tự xóa file.

## ⌨️ Tự kiểm tra

Chạy từ thư mục repo:

    python3 tools/check_links.py --output link-report.json

Báo cáo JSON phân biệt OK, redirect, 404/410, giới hạn 401/403/429 và các nguồn phải kiểm tra thủ công.

> Tài liệu cập nhật: 19/10/2026. Giữ bản gốc trong lịch sử Git tại commit 4c1f034.