# DT063 – Danh sách liên kết kép và duyệt theo hai chiều

## Thông tin và căn cứ

- Họ tên, MSSV, lớp: **Bùi Anh Quân – N24DCDT075 – D24CQDT01-N**.
- Mã và tên đề tài: **DT063 – Danh sách liên kết kép và duyệt theo hai chiều** (INT13185, Nhóm 03, GV Hồ Nhựt Minh).
- Giáo trình: `Giao-trinh-Cau-truc-du-lieu-va-Giai-thuat-INT1306.pdf`,
  Chương 5, mục 5.2.6 Danh sách liên kết kép; trang in 122–124; trang PDF 134–136.
- URL GitHub: `[DIEN URL THAT]`; SHA chạy C và permalink ghi trong báo cáo / ThongTinNop.txt.
- Ngôn ngữ: Julia (chỉ dùng thư viện chuẩn `Test`, `Random`).

## Bài toán

Xây dựng danh sách liên kết kép, mỗi nút có liên kết `truoc` và `ke`. Chương trình
thêm ở hai đầu, tìm nút đầu tiên theo giá trị rồi tách nút đó, xuất danh sách theo cả
hai chiều, kiểm sự nhất quán giữa hai liên kết và xử lý đúng nút đầu/nút cuối.

| Input | Kiểu / miền |
|---|---|
| `day` | dãy số nguyên, 0..1000 phần tử, giá trị −1000..1000, cho phép trùng |
| `lenh` | dãy `(ten, x)` với `ten ∈ {:them_dau, :them_cuoi, :xoa}`, `x ∈ −1000..1000` |

Output: dãy xuôi, dãy ngược, số nút `n`, trạng thái từng lệnh (`DA THEM`, `DA XOA`,
`KHONG TIM THAY`), sơ đồ `dau/cuoi`, bảng `truoc/ke` từng nút, số nút xét và số liên
kết sửa. Dãy ngược luôn phải là đảo của dãy xuôi. Input sai bị `ArgumentError` từ chối.

## Cấu trúc mã

```text
DT063_DanhSachLienKetKep/
├── src/DanhSachKep.jl    # NutKep, DSKep và mọi thao tác tự cài
├── demo.jl               # các ca minh họa, nhập bàn phím, khảo sát
├── test/runtests.jl      # 14 ca kiểm độc lập có ID
├── Run_all.ps1           # chạy toàn bộ demo + khảo sát + test
└── docs/anh_ket_qua/     # 11 ảnh A01–A11
```

| Hàm (src/DanhSachKep.jl) | Vai trò | Chi phí |
|---|---|---|
| `them_kep!(L, x, :dau/:cuoi)` | thêm nút ở đầu/cuối | O(1) |
| `tim_nut(L, x)` | nút đầu tiên có giá trị x hoặc `nothing` | O(n) |
| `xoa_nut!(L, p)` | tách nút đã biết, cập nhật đầu/cuối | O(1) |
| `xoa_theo_gia_tri!(L, x)` | `tim_nut` + `xoa_nut!` | O(n) |
| `duyet_hai_chieu(L)` | `(xuoi, nguoc)` | O(n) |
| `kiem_tra_lien_ket(L)` | vị trí đầu tiên `p.ke.truoc !== p` (tùy chọn) | O(n) |
| `kiem_tra_dau_vao(day, lenh)` | validator theo phiếu | O(\|day\|+\|lenh\|) |
| `giai_bai(day, lenh)` | kiểm input, chạy lệnh, ghi trạng thái | O(n·\|lenh\|) |

## Chạy

```powershell
julia --version
julia --startup-file=no demo.jl                 # hai ví dụ trên phiếu
julia --startup-file=no demo.jl --ca=1          # 1..11, xem bảng dưới
julia --startup-file=no demo.jl --nhap          # nhập từ bàn phím
julia --startup-file=no demo.jl --khao-sat      # n = 5, 20, 100
julia --startup-file=no test/runtests.jl        # bộ kiểm thử
.\Run_all.ps1                                   # tất cả
```

| `--ca=` | Mã ca | Nội dung | Ảnh |
|---|---|---|---|
| 1 | VD01 | `[10,20,30]; xoa(20)` | A01 |
| 2 | VD02 | `[]; them_cuoi(5); xoa(5)` | A02 |
| 3 | TK01 | thêm xen kẽ hai đầu, xóa giá trị không có | A03 |
| 4 | TK02 | giá trị biên ±1000, trùng lặp, xóa liên tiếp | A04 |
| 5 | BIEN01 | ca phiếu 2: `[6]; xoa(6)` | A05 |
| 6 | BIEN02 | ca phiếu 3: `[1,2,3]; xoa(1)` | A06 |
| 7 | BIEN03 | ca phiếu 4: `[1,2,3]; xoa(3)` | A07 |
| 8 | LOI01 | giá trị 1001 và lệnh `chen 5` bị từ chối | A08 |
| 9 | KT09 | ca phiếu 1: danh sách rỗng | log |
| 10 | KT10 | ca phiếu 5: `[2,2,4]; xoa(2)` | log |
| 11 | KT13 | `kiem_tra_lien_ket` phát hiện liên kết hỏng | log |

Nhập bàn phím (`--nhap`): dòng 1 là dãy ban đầu (Enter nếu rỗng), dòng 2 là số lệnh k,
k dòng tiếp theo mỗi dòng một lệnh `them_dau x`, `them_cuoi x` hoặc `xoa x`.

## Kết quả kiểm thử

- **14 ca kiểm độc lập** (`VD01`, `VD02`, `TK01`, `TK02`, `BIEN01`–`03`, `LOI01`, `KT09`–`KT14`).
- **Tổng số phép kiểm (asserts): 1270 phép kiểm — Pass: 1270 / 1270 (Fail: 0, đạt 100%)**; số assert lớn hơn số ca vì `KT14` lặp 300 dãy ngẫu nhiên × 4 phép kiểm đối chiếu với `Vector` oracle.
