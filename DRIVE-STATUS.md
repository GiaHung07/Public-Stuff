# Link Google Drive / Docs — kiểm tra thực tế 19/10/2026

> Lấy từ README và các file gốc tại commit `4c1f034`; kiểm tra HTTP và tiếp tục bằng **Chromium/Playwright đăng xuất** trong [GitHub Actions](https://github.com/GiaHung07/Public-Stuff/actions/runs/39156006823). Không dùng mỗi HTTP 200 để đánh giá link còn sống.

## Tổng quan

| Nhóm | Link | Ý nghĩa |
|---|---:|---|
| Danh sách file/thư mục hiển thị trong trình duyệt | **25** | Có bằng chứng nội dung xuất hiện; chưa bảo đảm tải thành công toàn bộ file |
| Trang Google Docs có dấu hiệu hiển thị tài liệu | **1** | Chưa xác minh đọc được nội dung thực tế |
| HTTP 404/410, trình duyệt chưa xác minh được | **13** | Không truy cập công khai qua môi trường quét; có thể bị xóa **hoặc** hạn chế quyền |
| HTTP 200 nhưng không hiển thị được nội dung rõ ràng | **7** | Chưa đủ bằng chứng |

## A. Danh sách có bằng chứng hiển thị (25 mục)

**Có thể giữ trong kho tham khảo.** Giá trị DOM rows là số hàng giao diện tìm thấy, **không phải số file chính xác**. Quyền tải về và bản quyền nội dung từng mục vẫn cần tự đối chiếu.

| # | Link gốc | Bằng chứng | Vị trí file cũ |
|---:|---|---|---|
| 1 | [Mấy thứ linh tinh cho Photoshop](https://drive.google.com/drive/u/0/folders/1mcBf9uiGv0G951emv1lTx0yw50N7GLRF) | 11 DOM rows | README.md:18 |
| 2 | [Luts Evanto Free GFXVIET.NET](https://drive.google.com/drive/u/0/folders/1L1-XCpM9SrT27JTga6-jdZM4843cpM1i) | 17 DOM rows | README.md:19 |
| 3 | [Khoá học Premiere Pro 2](https://drive.google.com/drive/u/0/folders/1j3qgMozhMI8-_xBzmMtwUiuZ3U4yTYQB) | 8 DOM rows | README.md:66 |
| 4 | [Thiết kế - Dựng phim](https://drive.google.com/drive/u/0/folders/1RAvb8TXETN1xQAC7HJhTSIbkBwD6CpkG) | 7 DOM rows | README.md:68 |
| 5 | [Album sách](https://drive.google.com/drive/u/0/folders/1nwdctr4BcRYEw-iROjaFjPjLCTOCwJKS) | 6 DOM rows | README.md:72 |
| 6 | [Kịch](https://drive.google.com/drive/mobile/folders/1BvdLoy4zYCugSQl7ToGF97i1RwAbEf09/1iYRwsdkb-P6ZHeFiyj6UWR1vfNUr1YQU?sort=13&direction=a) | 17 DOM rows | README.md:126 |
| 7 | [Book 3](https://drive.google.com/drive/mobile/folders/0B1ySOrPxOWJmZGlNTkEtQnlEM3M) | 18 DOM rows | README.md:129 |
| 8 | [Book for Developer](https://drive.google.com/drive/mobile/folders/0B7T1_yL7RJIabmFBdkdCci1aTzA?resourcekey=0-NRT40ihLkhp2sM6uLiVwLA) | 44 DOM rows | README.md:131 |
| 9 | [CSS](https://drive.google.com/drive/mobile/folders/0Bwq1uYZkxJQeYm54X080WHQwZGc) | 50 DOM rows | README.md:133 |
| 10 | [Book 4](https://drive.google.com/drive/mobile/folders/1iQMdq5yK0EBqa1fgkmQTfW7EWSeJWYvT) | 7 DOM rows | README.md:134 |
| 11 | [Ninja Go](https://drive.google.com/drive/mobile/folders/1-OOdzY2lANvqfYs_MNTLdBYHfuDGlroI) | 33 DOM rows | README.md:136 |
| 12 | [Combat Footage](https://drive.google.com/drive/mobile/folders/1cs6Inepeh7cryX1abtNaCqq5Bwi-5NBT?usp=sharing) | 50 DOM rows | README.md:137 |
| 13 | [Pooh](https://drive.google.com/drive/mobile/folders/1now-ZYgev0jqF9zYajiridnCuB4jK-Li) | 43 DOM rows | README.md:138 |
| 14 | [Forbidden](https://drive.google.com/drive/mobile/folders/1RIhxwUu7KkSF2jMDJJ1E45l-pgr_HZKo) | 43 DOM rows | README.md:139 |
| 15 | [IDKI](https://drive.google.com/drive/mobile/folders/1ZXEhzbLRLU1giKKRJkjm8N04cO_JoYE2?usp=sharing) | 12 DOM rows | README.md:142 |
| 16 | [Football](https://drive.google.com/drive/mobile/folders/1k6xE2DtXBKAriL8ZywzOhnN7iZqq_zvl?usp=drive_open) | 21 DOM rows | README.md:143 |
| 17 | [Comic](https://drive.google.com/drive/mobile/folders/0BzQJzw2V271wYTJna0VoMVZVaXc?tid=0BzQJzw2V271wYTJna0VoMVZVaXc&resourcekey=0-g413K9OOzU5fTTeH7Y78XA) | 24 DOM rows | README.md:144 |
| 18 | [Civil War](https://drive.google.com/drive/folders/0B8Ywk6I3mYFHVE5rQkVSU2JwSTQ) | 50 DOM rows | README.md:145 |
| 19 | [Runaways](https://drive.google.com/drive/folders/0B3-Dw8F7GF9mVTNwWGJOTFJPZkU) | 6 DOM rows | README.md:146 |
| 20 | [Tintin](https://drive.google.com/drive/folders/1YaYbVAvWT6nYtnBz0bKuTE1OekufW-K9) | 24 DOM rows | README.md:147 |
| 21 | [Xmas Show](https://drive.google.com/drive/mobile/folders/0B1j88lrqI04bUzQ5MUlpanhDMlk) | 34 DOM rows | README.md:148 |
| 22 | [Music Learn](https://drive.google.com/drive/mobile/folders/0B_7ouZw-H499TGdvNUdvRWJBRW8) | 50 DOM rows | README.md:149 |
| 23 | [Book 6](https://drive.google.com/drive/mobile/folders/1n0fBJiHtmB8F-rDFwi4TsSS-k7ZMmc8k) | 50 DOM rows | README.md:150 |
| 24 | [Anesthesia](https://drive.google.com/drive/mobile/folders/0B0eS5jOms_k3TEtFNHNMdi14TlU) | 22 DOM rows | README.md:151 |
| 25 | [Cursor Windows](https://drive.google.com/drive/folders/1WbFEMDwppXfVeUBDVCqfSgJRKFgF2QxL) | 3 DOM rows | Cursor for Windows/README.md:3 |

## B. Google Docs cần xác minh thêm (1 mục)

| # | Link gốc | Tình trạng | Vị trí cũ |
|---:|---|---|---|
| 1 | [Phần mềm backup bản quyền](https://docs.google.com/document/d/e/2PACX-1vS6qiila2Ty-AjMYyw3k7GJY-T2qiKqkL-NsUwQHU85Ckqy5iTRDVHNgy3Rbm4f_ORzNBorELALEPIk/pub) | Có giao diện tài liệu, chưa xác nhận văn bản | README.md:38 |

## C. Không truy cập công khai qua HTTP (13 mục)

**Không gọi là đã bị xóa 100%.** Google có thể ẩn file không được chia sẻ bằng 404. Chỉ xóa khỏi danh mục chính, vẫn lưu lịch sử.

| # | Mục | HTTP | URL |
|---:|---|---:|---|
| 1 | Adobe 2022 | 410 | [Kiểm tra thủ công](https://docs.google.com/spreadsheets/d/1niE7GXhFp4phCIuXojIY4mTriyRcOb05xQheH2SkNRk/htmlview) |
| 2 | Trọn bộ Photoshop | 404 | [Kiểm tra thủ công](https://drive.google.com/drive/u/0/folders/1I-Wvp_x4nBA294mDzjyb8PS6SnH8DrV_) |
| 3 | Tài liệu học ngoại ngữ | 404 | [Kiểm tra thủ công](https://drive.google.com/drive/u/0/folders/1Qd1OotqV3sJsgoI5T5tTz0_Qs8-b2DzU) |
| 4 | Movie Theme | 404 | [Kiểm tra thủ công](https://drive.google.com/drive/mobile/folders/1P15Ets-NwYxW1n2wu59Knm9uYn27cPey?usp=sharing) |
| 5 | Orienting Child | 404 | [Kiểm tra thủ công](https://drive.google.com/drive/mobile/folders/1ZI1Ta8ZTY_an7vEKa5oSrNBpaPFob1FB?usp=sharing) |
| 6 | Powerpoint | 404 | [Kiểm tra thủ công](https://drive.google.com/drive/mobile/folders/0BwRuZt4Aidm1LXd3dGNldHcyZm8?resourcekey=0-Z_bVUcrH1Jk6Kfm4Sodbiw) |
| 7 | Book 2 | 404 | [Kiểm tra thủ công](https://drive.google.com/drive/mobile/folders/1Z30-9EO6B0oEuFHYMKUzzzEO6p82-dYU/1mXAydnwLE_Bq3yr2OXZD28lgM6MdX43y?usp=sharing&sort=13&direction=a) |
| 8 | Various | 404 | [Kiểm tra thủ công](https://drive.google.com/drive/mobile/folders/1S-zjW17dRGK3XEi8l1T5bEUHJqMxto5X) |
| 9 | Movie Good | 404 | [Kiểm tra thủ công](https://drive.google.com/drive/mobile/folders/1uXCWl9rGsndFg_jpQ6VHq59OcQYb-Et1?usp=sharing) |
| 10 | Book 5 | 404 | [Kiểm tra thủ công](https://drive.google.com/drive/mobile/folders/1vlY512iwG0yrTFE3Hha_lhBZq9zavQE) |
| 11 | Various 2 | 404 | [Kiểm tra thủ công](https://drive.google.com/drive/mobile/folders/1OuJJg_zr4pG3EW2SYFyV4CaBxlyypZAQl) |
| 12 | Freepik | 404 | [Kiểm tra thủ công](https://drive.google.com/drive/mobile/folders/1OuAHMxZ5cBFrewoOKaWrYwQJWUaXwdx) |
| 13 | Tổng hợp Android TV apps | 404 | [Kiểm tra thủ công](https://drive.google.com/drive/u/0/folders/1PFdV02DrH0AjbszXD8Klo_23cC8Q3F2_) |

## D. HTTP 200 nhưng trình duyệt chưa xác minh được (7 mục)

| # | Mục | HTTP | URL |
|---:|---|---:|---|
| 1 | Tất cả App 😵‍💫 | 200 | [Mở để xác minh](https://docs.google.com/spreadsheets/d/e/2PACX-1vRlK-vRwPJHDaANT81EjyG4m5ZnLXdKRYfS0eKXyCzGymEfUDmKHRhxvUbtWYTfVn7MJ3E2jk7v3cGi/pubhtml#) |
| 2 | Của da.tuu.1810 | 200 | [Mở để xác minh](https://docs.google.com/document/d/1eGe5MAWn-_YypoJSgopnyJGaCdzjKlqlirRCtySGsak/edit) |
| 3 | Voz TRUYỆN Doraemon | 200 | [Mở để xác minh](https://docs.google.com/spreadsheets/d/1qV9RD_DOCLrlqcoaPm2sENnL9DEXHt2i_t87v0OBfGg/edit#gid=0) |
| 4 | Khoá học tổng hợp | 200 | [Mở để xác minh](https://docs.google.com/spreadsheets/d/14tOY5Nrm9wUDywpW3l0Q4ihAHGZcUL0xwUDt8JnDE4w/htmlview) |
| 5 | Tài liệu tổng hợp | 200 | [Mở để xác minh](https://docs.google.com/document/d/1ET3IkLGa0mXl_o96ZgxxevBNfs96hVmh/edit?usp=drivesdk&ouid=100653803810411128617&rtpof=true&sd=true) |
| 6 | Book | 200 | [Mở để xác minh](https://drive.google.com/drive/folders/1nitHECSorEadPtGwK5F_9-TdAcHHJGZG) |
| 7 | - Link cũ dự phòng: https://drive.google.com/file/d/10iyxB_1WBw_u | 200 | [Mở để xác minh](https://drive.google.com/file/d/10iyxB_1WBw_uCwwhfyHMWahpt30ZplvQ/view?usp=sharing) |

## Hạn chế

- Chromium chạy ẩn danh trên GitHub-hosted runner; nếu cần tài khoản Google cụ thể, không thể xác minh quyền của tài khoản đó.
- HTML/Google Drive có thể thay đổi giao diện, dẫn đến đếm hàng không chính xác; kiểm tra browser chỉ là bằng chứng nội dung đã render.
- Danh mục này là snapshot ngày 19/10/2026, không phải kiểm tra liên tục. Dùng workflow `Audit original links` để chạy lại.
- Bản sao nguyên văn các danh sách năm 2023 nằm trong `legacy/2023/`; không xóa dữ liệu vì 1 lần thất bại.

[⬅ Trang chủ](README.md) · [Danh mục công cụ](CATALOG.md) · [Báo cáo HTTP](LINK-REVIEW.md)