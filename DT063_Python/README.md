# DT063 – Danh sách liên kết kép và duyệt theo hai chiều (Python + Web)

- Sinh viên: **Bùi Anh Quân – N24DCDT075 – D24CQDT01-N** (INT13185, Nhóm 03).
- Giáo trình INT1306, Chương 5, mục 5.2.6; trang in 122–124; trang PDF 134–136.
- Ngôn ngữ: Python ≥ 3.9, **chỉ dùng thư viện chuẩn** (không cần `pip install`).

## Cấu trúc

```text
DT063_Python/
├── src/danh_sach_kep.py        # NutKep, DSKep và mọi thao tác tự cài (truoc/ke)
├── tests/test_danh_sach_kep.py # 14 ca kiểm độc lập (VD01..KT14)
├── demo.py                     # demo console, nhập bàn phím, khảo sát
├── web/app.py                  # máy chủ http.server, API /api/giai, /api/ca
├── web/index.html              # giao diện mô phỏng trực quan
└── Run_all.ps1                 # chạy demo + khảo sát + test
```

| Hàm / phương thức | Vai trò | Chi phí |
|---|---|---|
| `DSKep.them(x, 'dau'/'cuoi')` | thêm nút ở đầu/cuối | O(1) |
| `DSKep.tim_nut(x)` | nút đầu tiên có giá trị x hoặc `None` | O(n) |
| `DSKep.xoa_nut(p)` | tách nút đã biết, cập nhật đầu/cuối | O(1) |
| `DSKep.xoa_theo_gia_tri(x)` | `tim_nut` + `xoa_nut` | O(n) |
| `DSKep.duyet_hai_chieu()` | `(xuoi, nguoc)` | O(n) |
| `DSKep.kiem_tra_lien_ket()` | vị trí đầu tiên `p.ke.truoc is not p` | O(n) |
| `kiem_tra_dau_vao(day, lenh)` | validator theo phiếu → `LoiDauVao` | O(\|day\|+\|lenh\|) |
| `giai_bai(day, lenh)` | kiểm input, chạy lệnh, ghi trạng thái | O(n·\|lenh\|) |

## Chạy

```powershell
python web/app.py                  # mở trang web http://127.0.0.1:8000
python demo.py                     # hai ví dụ trên phiếu
python demo.py --ca 5              # 1..11: VD01 VD02 TK01 TK02 BIEN01-03 LOI01 KT09 KT10 KT13
python demo.py --nhap              # nhập từ bàn phím
python demo.py --khao-sat          # n = 5, 20, 100
python -m unittest -v tests/test_danh_sach_kep.py
.\Run_all.ps1                      # tất cả
```

Trang web: nhập dãy ban đầu + danh sách lệnh (`them_dau x`, `them_cuoi x`, `xoa x`), bấm
**▶ Chạy** để xem hoạt ảnh từng bước (quét tìm nút, tách nút, nối lại `truoc/ke`), bảng
liên kết, dãy xuôi/ngược, bộ đếm nút xét/liên kết sửa và kết quả kiểm tra liên kết.
Phím tắt: ← / → chuyển bước, Space phát/dừng.
