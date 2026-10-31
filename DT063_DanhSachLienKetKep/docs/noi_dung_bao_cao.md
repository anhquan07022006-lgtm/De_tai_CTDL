# NỘI DUNG BÁO CÁO DT063 – điền vào `02_Mau_bao_cao_de_tai_ca_nhan.docx`

> Bản nháp để chép vào từng ô `[...]` của mẫu Word. Phần `[TỰ ĐIỀN ...]` (URL, SHA,
> ngày, ảnh) chỉ có sau khi bạn tự push lên GitHub và tự chụp ảnh. Số liệu dưới đây là
> số liệu chạy thật trên máy (Julia 1.12.7); khi chạy lại hãy đối chiếu và sửa nếu khác.

---

## Bìa và phiếu

| Ô trong mẫu | Nội dung |
|---|---|
| KHOA | [TỰ ĐIỀN theo lớp D24CQDT01-N, ví dụ Khoa Kỹ thuật Điện tử 2] |
| Ngành | [TỰ ĐIỀN] |
| Tên đề tài | DANH SÁCH LIÊN KẾT KÉP VÀ DUYỆT THEO HAI CHIỀU |
| Mã đề | DT063 |
| Họ và tên / MSSV / Lớp | Bùi Anh Quân / N24DCDT075 / D24CQDT01-N |
| Căn cứ giáo trình | Chương 5, 5.2.6 Danh sách liên kết kép; trang in 122–124; trang PDF 134–136 |
| Phiên bản báo cáo | [Ngày] – commit C `[SHA C đầy đủ]` |

Phiếu giao: chép nguyên phiếu DT063 trong `91_Phieu_giao_de_tai_INT13185_N03.docx`
(Ctrl+F “N24DCDT075”).

## LỜI CAM ĐOAN

Tôi là Bùi Anh Quân, MSSV N24DCDT075, cam đoan đề tài DT063 do tôi thực hiện. Cấu trúc
`NutKep`, `DSKep` và các thao tác thêm hai đầu, tìm, tách nút, duyệt hai chiều, kiểm tra
liên kết do tôi tự cài đặt bằng Julia dựa trên mục 5.2.6 của giáo trình INT1306. Cách tổ
chức thư mục, script chạy và cách trình bày ca kiểm thử tham khảo mã mẫu BFS của giảng
viên; phần thuật toán, dữ liệu kiểm thử, ảnh và số liệu trong báo cáo là kết quả tôi tự
chạy tại commit được ghi trong Chương 4 và có thể chạy lại theo README.

## TÓM TẮT

Đề tài xây dựng danh sách liên kết kép số nguyên, mỗi nút giữ liên kết `truoc` và `ke`;
danh sách giữ `dau`, `cuoi` và số nút `n`. Chương trình thêm nút ở hai đầu trong O(1),
tìm nút đầu tiên theo giá trị trong O(n), tách nút đã biết trong O(1) với xử lý riêng
nút đầu/nút cuối, và xuất dãy xuôi, dãy ngược. Hàm `kiem_tra_lien_ket` kiểm bất biến
`next(u)=v ⇒ prev(v)=u`, `dau.truoc = cuoi.ke = nothing`, số nút bằng `n`, và báo vị trí
đầu tiên bị sai. Bộ kiểm thử gồm 14 ca độc lập (2 ví dụ, 5 ca phiếu, 2 ca tự thiết kế,
1 ca input sai, các ca hàm con/bất biến và 300 dãy lệnh ngẫu nhiên đối chiếu với Vector),
tổng 1270 phép kiểm, tất cả đạt. Khảo sát n = 5, 20, 100 cho thấy số nút xét khi tìm bằng
vị trí của nút cần xóa (tối đa n), còn số liên kết sửa khi tách luôn bằng 2. Giới hạn:
miền 0..1000 nút, giá trị −1000..1000, chỉ xóa lần xuất hiện đầu tiên.

---

# CHƯƠNG 1. TỔNG QUAN ĐỀ TÀI

## 1.1. Bài toán và lý do thực hiện

Danh sách liên kết đơn chỉ đi được một chiều: muốn xóa một nút phải biết nút đứng trước,
nên phải duyệt lại từ đầu. Danh sách liên kết kép (giáo trình INT1306, mục 5.2.6, trang in
122–124) bổ sung cho mỗi nút một liên kết `truoc`, nhờ đó duyệt được theo hai chiều và tách
một nút đã biết địa chỉ trong thời gian hằng. Đổi lại, mỗi thao tác phải cập nhật đồng thời
hai liên kết; chỉ cần sửa thiếu một liên kết thì dãy xuôi và dãy ngược sẽ không còn khớp.

Đề tài DT063 yêu cầu xây dựng danh sách kép số nguyên, thực hiện thêm ở hai đầu, tìm một
nút theo giá trị rồi xóa nút đó, xuất danh sách theo cả hai chiều, kiểm sự nhất quán giữa
hai liên kết và xử lý đúng khi thay đổi nút đầu, nút cuối. Kết quả cần tính sau mỗi lệnh:
dãy xuôi, dãy ngược, số nút và trạng thái xóa.

## 1.2. Mục tiêu và sản phẩm

1. `them_kep!(L, x, :dau/:cuoi)`: thêm nút; điều kiện hoàn thành – dãy xuôi có x ở đầu/cuối, n tăng 1, liên kết hợp lệ.
2. `tim_nut(L, x)`: trả nút đầu tiên có giá trị x hoặc `nothing`; kiểm bằng ca [2,2,4].
3. `xoa_nut!(L, p)`: tách nút đã biết, cập nhật `dau`/`cuoi` khi p ở biên; sau khi xóa nút duy nhất `dau = cuoi = nothing`.
4. `duyet_hai_chieu(L)`: trả (xuoi, nguoc); điều kiện: `nguoc == reverse(xuoi)`.
5. `kiem_tra_lien_ket(L)` (yêu cầu tùy chọn): báo vị trí đầu tiên có liên kết trước/sau không khớp.
6. Sản phẩm: mã nguồn Julia (`src/DanhSachKep.jl`, `demo.jl`), bộ test `test/runtests.jl` 14 ca, script `Run_all.ps1`, 11 ảnh A01–A11, báo cáo này và repo GitHub `[URL]`.

## 1.3. Phạm vi, đầu vào và đầu ra

### 1.3.1. Miền và quy ước đầu vào

Dữ liệu vào gồm dãy ban đầu `day` và dãy lệnh `lenh`. `day` là mảng số nguyên dài 0..1000,
mỗi giá trị trong −1000..1000, cho phép trùng; danh sách được tạo bằng cách thêm cuối lần
lượt nên phần tử `day[1]` là nút đầu. Mỗi lệnh là một cặp `(ten, x)` với `ten` là
`:them_dau`, `:them_cuoi` hoặc `:xoa` và x trong −1000..1000. Trong mọi thời điểm danh sách
có không quá 1000 nút. Dữ liệu được khai báo trực tiếp trong `demo.jl`/`test/runtests.jl`
hoặc nhập bàn phím bằng `julia demo.jl --nhap` (dòng 1: dãy ban đầu, dòng 2: số lệnh k,
k dòng sau: `them_dau x`, `them_cuoi x`, `xoa x`; chấp nhận cả dạng `xoa(20)`).

### 1.3.2. Kết quả và trường hợp đặc biệt

Sau mỗi lệnh chương trình in trạng thái (`DA THEM x VAO DAU/CUOI`, `DA XOA x`,
`KHONG TIM THAY x`), sơ đồ `dau -> [..] <-> [..] <- cuoi`, bảng `truoc | gia tri | ke` của
từng nút, dãy xuôi, dãy ngược, n, số nút đã xét và số liên kết đã sửa. Khi giá trị xuất hiện
nhiều lần chỉ xóa lần xuất hiện đầu tiên tính từ `dau`. Xóa giá trị không có là trường hợp
hợp lệ: danh sách giữ nguyên, trạng thái `KHONG TIM THAY`. Danh sách rỗng in hai dãy rỗng,
`dau = cuoi = nothing`. Input sai (giá trị ngoài miền, không phải số nguyên, tên lệnh lạ,
vượt 1000 nút) bị từ chối bằng `ArgumentError` có lý do, không làm hỏng danh sách.

**Bảng 1.1 Đặc tả dữ liệu vào**

| Tên dữ liệu | Kiểu và kích thước | Miền và điều kiện | Cách nhập hoặc khai báo |
|---|---|---|---|
| `day` | `Vector{Int}`, 0..1000 phần tử | mỗi giá trị −1000..1000, cho phép trùng | khai báo trong mã hoặc dòng 1 bàn phím |
| `lenh` | `Vector{Tuple{Symbol,Int}}` | ten ∈ {them_dau, them_cuoi, xoa}; x ∈ −1000..1000 | khai báo hoặc k dòng bàn phím |
| `n` (trong quá trình chạy) | `Int` | 0 ≤ n ≤ 1000 | do `them_kep!` kiểm |

**Bảng 1.2 Đặc tả kết quả đầu ra**

| Kết quả | Kiểu hoặc cách in | Ý nghĩa và điều kiện đúng | Hòa / vô nghiệm / lỗi |
|---|---|---|---|
| `xuoi` | `Vector{Int}` `[a1,...,an]` | duyệt theo `ke` từ `dau` | rỗng → `[]` |
| `nguoc` | `Vector{Int}` | duyệt theo `truoc` từ `cuoi`; phải bằng `reverse(xuoi)` | rỗng → `[]` |
| `n` | `Int` | số nút hiện có | – |
| trạng thái xóa | chuỗi | `DA XOA x` / `KHONG TIM THAY x` | trùng: xóa lần đầu |
| lỗi input | `ArgumentError` | thông báo vị trí/lý do | không tạo danh sách |

## 1.4. Cách thực hiện và cấu trúc báo cáo

Quy trình theo năm bước của phiếu: (1) đọc mục 5.2.6, vẽ hai mũi tên cho mỗi cặp nút và
tính tay kết quả Ví dụ 1; (2) cài `DSKep` với `dau`, `cuoi`, `n` và hàm thêm đầu/cuối, chạy
riêng; (3) cài tìm và tách nút, xử lý riêng đầu/cuối, in trạng thái từng bước; (4) cài duyệt
xuôi/ngược và kiểm từng cặp `p.ke.truoc === p`; (5) chạy hai ví dụ, năm ca, bổ sung ca tự
thiết kế và so sánh chi phí tìm với chi phí tách. Chương 2 trình bày cơ sở lý thuyết, Chương 3
thiết kế–cài đặt–lần vết–độ phức tạp, Chương 4 kết quả kiểm thử, khảo sát và GitHub,
Chương 5 kết luận.

**Bảng 1.3 Đối chiếu yêu cầu và sản phẩm**

| Yêu cầu trên phiếu | Sản phẩm / điều kiện kiểm | Mục |
|---|---|---|
| Nút có liên kết trước và sau | `NutKep(gia_tri, truoc, ke)` | 2.2, 3.2 |
| Thêm ở hai đầu | `them_kep!`; TK01, VD02 | 3.3, 4.4 |
| Tìm nút theo giá trị rồi xóa | `tim_nut`, `xoa_nut!`, `xoa_theo_gia_tri!`; VD01, KT10 | 3.3, 4.3 |
| Xuất theo hai chiều | `duyet_hai_chieu`; `nguoc == reverse(xuoi)` mọi ca | 3.3, 4.2 |
| Xử lý nút đầu, nút cuối | BIEN01–BIEN03 | 4.5 |
| Kiểm nhất quán hai liên kết (tùy chọn) | `kiem_tra_lien_ket`; KT13 | 3.5, 4.2 |
| Phân tích O(n) tìm, O(1) tách, n=5,20,100 | bộ đếm `so_nut_xet`, `so_lien_ket_sua` | 3.6, 4.8 |

---

# CHƯƠNG 2. CƠ SỞ LÝ THUYẾT

## 2.1. Khái niệm và mô hình dữ liệu

Danh sách tuyến tính là dãy hữu hạn phần tử a1, a2, …, an có thứ tự. Trong cài đặt liên kết,
mỗi phần tử nằm trong một nút cấp phát riêng và thứ tự được biểu diễn bằng liên kết giữa các
nút, không phụ thuộc vị trí trong bộ nhớ. Danh sách liên kết kép (giáo trình mục 5.2.6) là
danh sách liên kết mà mỗi nút có hai liên kết: `ke` trỏ tới nút sau và `truoc` trỏ tới nút
trước. Ký hiệu: n là số nút; `nothing` biểu thị liên kết rỗng (tương đương NULL trong C++).

## 2.2. Cấu trúc dữ liệu sử dụng

### 2.2.1. Dữ liệu và thao tác chính

- `NutKep`: lưu `gia_tri::Int`, `truoc`, `ke` (kiểu `Union{NutKep,Nothing}`).
- `DSKep`: lưu `dau`, `cuoi`, `n` và hai bộ đếm `so_nut_xet`, `so_lien_ket_sua` dùng để phân tích chi phí.

Giữ cả `dau` và `cuoi` giúp thêm ở hai đầu trong O(1); liên kết `truoc` giúp tách một nút
đã biết mà không cần tìm nút đứng trước, đúng nội dung so sánh DSLK đơn/kép của giáo trình.

### 2.2.2. Quy ước và điều kiện hợp lệ

Vị trí nút đánh số từ 1 tính từ `dau`. Danh sách rỗng khi `dau = cuoi = nothing` và n = 0.
Cho phép khóa trùng; xóa theo giá trị chỉ xóa nút đầu tiên tìm thấy khi duyệt từ `dau`.

**Bảng 2.1 Biến cấu trúc và điều kiện phải duy trì**

| Ký hiệu / cấu trúc | Ý nghĩa | Miền / bất biến |
|---|---|---|
| `L.dau` | nút đầu | `dau === nothing ⇔ n == 0`; nếu khác rỗng `dau.truoc === nothing` |
| `L.cuoi` | nút cuối | `cuoi === nothing ⇔ n == 0`; nếu khác rỗng `cuoi.ke === nothing` |
| `L.n` | số nút | 0 ≤ n ≤ 1000; bằng số bước duyệt xuôi từ `dau` tới `nothing` |
| `p.ke`, `p.truoc` | liên kết sau/trước | `p.ke = q ≠ nothing ⇒ q.truoc === p` |
| `xuoi`, `nguoc` | hai dãy duyệt | `nguoc == reverse(xuoi)`, độ dài n |

Hình 2.1 (tự vẽ): `dau → [nothing|10|•] ⇄ [•|20|•] ⇄ [•|30|nothing] ← cuoi`, minh họa
Ví dụ 1 trước khi xóa 20; sau khi xóa, mũi tên `ke` của 10 và `truoc` của 30 nối thẳng nhau.

## 2.3. Nguyên lý thuật toán

### 2.3.1. Ý tưởng xử lý

- Thêm đầu: tạo nút m; nếu rỗng thì `dau = cuoi = m`; ngược lại `m.ke = dau; dau.truoc = m; dau = m`.
  Thêm cuối đối xứng với `cuoi`.
- Tìm: duyệt `p = dau, p = p.ke` cho tới khi gặp giá trị x hoặc `nothing`.
- Tách nút p: nếu p có nút trước thì `p.truoc.ke = p.ke`, ngược lại `dau = p.ke`; nếu p có nút sau
  thì `p.ke.truoc = p.truoc`, ngược lại `cuoi = p.truoc`; sau đó đặt `p.truoc = p.ke = nothing`, n giảm 1.
- Duyệt xuôi theo `ke` từ `dau`, duyệt ngược theo `truoc` từ `cuoi`.

### 2.3.2. Điều kiện bắt đầu và kết thúc

Khởi đầu danh sách rỗng thỏa mọi bất biến Bảng 2.1. Mỗi thao tác thêm/tách giữ các bất biến
(chứng minh ở 3.5). Vòng tìm và vòng duyệt dừng vì mỗi bước tiến sang nút kế, danh sách có hữu
hạn n nút và nút cuối có `ke = nothing`; bản cài còn chặn số bước ≤ n để phát hiện vòng.

## 2.4. Cơ sở đánh giá thời gian và bộ nhớ

Quy mô là n – số nút hiện có. Phép toán chính: (a) một lần so sánh giá trị nút khi tìm
(`so_nut_xet`); (b) một lần gán vào trường `dau`, `cuoi`, `truoc`, `ke` để nối/tách
(`so_lien_ket_sua`). Theo giáo trình: thêm đầu/cuối O(1); tìm theo giá trị O(n) trong trường
hợp xấu nhất; xóa nút đã có tham chiếu O(1); duyệt O(n). Bộ nhớ dữ liệu Θ(n) với mỗi nút giữ
một giá trị và hai liên kết (gấp đôi số liên kết so với DSLK đơn); bộ nhớ phụ của các thao tác
là O(1), riêng hai mảng kết quả duyệt là O(n) và thuộc phần xuất kết quả.

Giả mã nền tảng (theo mục 5.2.6, điều chỉnh tên biến theo mã):

```text
THEM_DAU(L, x):  m ← nut(x); nếu L.dau = rỗng: L.dau ← m; L.cuoi ← m
                 ngược lại: m.ke ← L.dau; L.dau.truoc ← m; L.dau ← m
                 L.n ← L.n + 1
XOA_NUT(L, p):   nếu p.truoc = rỗng: L.dau ← p.ke   ngược lại: p.truoc.ke ← p.ke
                 nếu p.ke = rỗng:    L.cuoi ← p.truoc ngược lại: p.ke.truoc ← p.truoc
                 p.truoc ← rỗng; p.ke ← rỗng; L.n ← L.n − 1
```

---

# CHƯƠNG 3. PHÂN TÍCH, THIẾT KẾ VÀ CÀI ĐẶT

## 3.1. Phân tích yêu cầu chương trình

### 3.1.1. Hợp đồng input/output

`giai_bai(day, lenh)` nhận `day::AbstractVector` số nguyên và `lenh` là mảng cặp
`(Symbol, Int)`; trả NamedTuple `(L, buoc, xuoi, nguoc, n)`, trong đó mỗi phần tử `buoc` ghi
`lenh, trang_thai, xuoi, nguoc, n, nut_xet, lien_ket_sua, hop_le` sau từng lệnh. Lỗi input
ném `ArgumentError`.

### 3.1.2. Kiểm tra đầu vào

`kiem_tra_dau_vao` kiểm: `day` là mảng, dài ≤ 1000, mỗi phần tử là số nguyên (không nhận
`Bool`, số thực) trong −1000..1000; mỗi lệnh là cặp `(Symbol, x)` với tên hợp lệ và x trong
miền. Giới hạn 1000 nút trong quá trình chạy do `them_kep!` kiểm trước khi sửa liên kết, nên
lệnh bị từ chối không làm thay đổi danh sách (KT11). `phan_tich_lenh` từ chối chuỗi bàn phím
sai cú pháp. Xóa giá trị không có là input hợp lệ không có nghiệm, không phải input sai.

## 3.2. Thiết kế các hàm và dữ liệu

Toàn bộ thao tác liên kết tự cài; `Vector` chỉ dùng để trả dãy duyệt và làm oracle trong test.

**Bảng 3.1 Tổ chức các hàm và tệp**

| Hàm / tệp | Input | Output | Vai trò và phần tự cài |
|---|---|---|---|
| `them_kep!` (src) | L, x, `:dau`/`:cuoi` | nút mới | Bước 2 phiếu – nối 2 hoặc 3 liên kết |
| `tim_nut` (src) | L, x | nút hoặc `nothing` | Bước 3 – duyệt tuyến tính |
| `xoa_nut!` (src) | L, p | giá trị nút | Bước 3 – tách O(1), xử lý đầu/cuối |
| `xoa_theo_gia_tri!` (src) | L, x | `(da_xoa, nut_xet, lien_ket_sua)` | ghép tìm + tách |
| `duyet_hai_chieu` (src) | L | `(xuoi, nguoc)` | Bước 4 |
| `kiem_tra_lien_ket` (src) | L | `(hop_le, vi_tri, ly_do)` | Bước 4 + yêu cầu tùy chọn |
| `kiem_tra_dau_vao`, `phan_tich_lenh` (src) | day, lenh / chuỗi | true / lệnh | validator |
| `giai_bai` (src) | day, lenh | NamedTuple | chạy toàn bộ, ghi vết |
| `so_do`, `bang_lien_ket` (src) | L | chuỗi | in sơ đồ và bảng prev/next |
| `demo.jl` | `--ca=k`, `--nhap`, `--khao-sat` | màn hình | minh họa A01–A08, khảo sát |
| `test/runtests.jl` | – | Test Summary | 14 ca độc lập |

Sơ đồ xử lý (Hình 3.1): Nhập/khai báo → `kiem_tra_dau_vao` (sai → `ArgumentError`) →
`tao_danh_sach` → với mỗi lệnh: `them_kep!` hoặc `xoa_theo_gia_tri!` → `duyet_hai_chieu`
+ `kiem_tra_lien_ket` → in trạng thái.

**Bảng 3.2 Tiền điều kiện và hậu điều kiện của các hàm**

| Hàm và chữ ký | Tiền điều kiện | Hậu điều kiện | Lỗi / đặc biệt |
|---|---|---|---|
| `them_kep!(L, x, vt)` | L thỏa bất biến; x ∈ −1000..1000; n < 1000 | x ở đầu/cuối; n tăng 1; bất biến giữ | vt lạ, x ngoài miền, đủ 1000 nút → `ArgumentError`, L không đổi |
| `tim_nut(L, x)` | L thỏa bất biến | trả nút đầu tiên có giá trị x hoặc `nothing`; L không đổi | rỗng → `nothing` |
| `xoa_nut!(L, p)` | p đang thuộc L | p bị tách; `dau`/`cuoi` cập nhật nếu p ở biên; `p.truoc = p.ke = nothing`; n giảm 1 | p không thuộc L → `ArgumentError` |
| `duyet_hai_chieu(L)` | L thỏa bất biến | `nguoc == reverse(xuoi)`, độ dài n | vượt n bước → lỗi (vòng) |
| `kiem_tra_lien_ket(L)` | bất kỳ | `hop_le = true` ⇔ mọi bất biến Bảng 2.1 đúng | trả vị trí đầu tiên sai |

## 3.3. Thuật toán và mã nguồn chính

### 3.3.1. Giả mã theo cài đặt

```text
giai_bai(day, lenh):
    kiem_tra_dau_vao(day, lenh)
    L ← DSKep();  với x trong day: them_kep!(L, x, :cuoi);  dat_lai_bo_dem!(L)
    với (ten, x) trong lenh:
        nếu ten = them_dau/them_cuoi: them_kep!(L, x, :dau/:cuoi)
        ngược lại:  p ← tim_nut(L, x)
                    nếu p ≠ nothing: xoa_nut!(L, p)  → "DA XOA x"
                    ngược lại → "KHONG TIM THAY x"
        ghi (xuoi, nguoc) ← duyet_hai_chieu(L), n, bộ đếm, kiem_tra_lien_ket(L)
    trả (L, buoc, xuoi, nguoc, n)
```

### 3.3.2. Đoạn mã và giải thích

Trích `xoa_nut!` từ `src/DanhSachKep.jl` (permalink: `[URL]/blob/[SHA C]/src/DanhSachKep.jl`):

```julia
function xoa_nut!(L::DSKep, p::NutKep)
    thuoc_ds = (p.truoc === nothing ? L.dau === p : p.truoc.ke === p) &&
               (p.ke === nothing ? L.cuoi === p : p.ke.truoc === p)
    thuoc_ds || throw(ArgumentError("nut khong thuoc danh sach hoac lien ket da hong"))
    if p.truoc === nothing
        L.dau = p.ke              # p là đầu: đầu mới là nút sau p
    else
        p.truoc.ke = p.ke         # nút trước bỏ qua p
    end
    if p.ke === nothing
        L.cuoi = p.truoc          # p là cuối: cuối mới là nút trước p
    else
        p.ke.truoc = p.truoc      # nút sau trỏ ngược bỏ qua p
    end
    L.so_lien_ket_sua += 2
    p.truoc = nothing
    p.ke = nothing
    L.n -= 1
    return p.gia_tri
end
```

Hai khối `if` độc lập bao trọn bốn trường hợp: nút giữa (sửa 2 liên kết của hàng xóm), nút đầu
(sửa `dau` và `truoc` của nút sau), nút cuối (sửa `ke` của nút trước và `cuoi`), nút duy nhất
(sửa `dau` và `cuoi` thành `nothing`). Thứ tự quan trọng: phải đọc `p.ke`, `p.truoc` trước khi
xóa liên kết của p; nếu đặt `p.ke = nothing` trước thì nút trước sẽ bị nối với `nothing` và mất
đuôi. Phép kiểm `thuoc_ds` O(1) ngăn tách một nút không thuộc danh sách (KT13).

Trích `them_kep!` nhánh thêm đầu:

```julia
m.ke = L.dau          # (1) nút mới trỏ tới đầu cũ
L.dau.truoc = m       # (2) đầu cũ trỏ ngược về nút mới
L.dau = m             # (3) cập nhật con trỏ đầu
```

Nếu đổi (3) lên trước (2), `L.dau.truoc = m` sẽ gán vào chính m và đầu cũ vẫn có `truoc = nothing`
– dãy xuôi đúng nhưng dãy ngược mất nút mới; `kiem_tra_lien_ket` phát hiện lỗi tại vị trí 1.

### 3.3.3. Xử lý tình huống đặc biệt

Danh sách rỗng (KT09, VD02), một nút (BIEN01), xóa đầu (BIEN02), xóa cuối (BIEN03), giá trị
trùng (KT10, TK02), giá trị không có (TK01), giá trị biên ±1000 (TK02), đủ 1000 nút (KT11),
input sai (LOI01), liên kết hỏng (KT13).

## 3.4. Lần vết ví dụ nhỏ

Ca truy vết **VD01** – Input `day = [10,20,30]; lenh = xoa(20)` – Expected tính tay:
`xuoi = [10,30]; nguoc = [30,10]; n = 2`.

**Bảng 3.3 Truy vết ca VD01** (A = nút 10, B = nút 20, C = nút 30)

| Bước | Thao tác | Trạng thái trước | Trạng thái sau | Giải thích |
|---|---|---|---|---|
| 0 | Khởi tạo | `day=[10,20,30]` | `dau=A, cuoi=C, n=3`; A(truoc=–, ke=B), B(A, C), C(B, –) | thêm cuối 3 lần |
| 1 | `tim_nut(L,20)`: p = A | p = A | 10 ≠ 20 → p = B; nut_xet = 1 | chưa gặp |
| 2 | p = B | p = B | 20 = 20 → trả B; nut_xet = 2 | gặp lần đầu |
| 3 | kiểm `thuoc_ds` | B.truoc = A, A.ke = B; B.ke = C, C.truoc = B | đúng | B thuộc L |
| 4 | B.truoc ≠ nothing → `A.ke = B.ke` | A.ke = B | A.ke = C | liên kết sửa 1 |
| 5 | B.ke ≠ nothing → `C.truoc = B.truoc` | C.truoc = B | C.truoc = A | liên kết sửa 2 |
| 6 | `B.truoc = B.ke = nothing`, n−1 | n = 3 | n = 2, B tách rời | không giữ con trỏ cũ |
| Cuối | Duyệt hai chiều | – | xuoi = [10,30], nguoc = [30,10] | khớp expected; A.ke.truoc = C.truoc = A ✓ |

Bảng khớp output thật của `julia demo.jl --ca=1` (Hình 4.1): “So nut xet khi tim: 2; so lien
ket sua: 2”, bảng liên kết sau xóa `1 | nothing | 10 | 30` và `2 | 10 | 30 | nothing`. `dau` và
`cuoi` không đổi vì nút bị xóa là nút giữa.

## 3.5. Giải thích tính đúng và điều kiện dừng

### 3.5.1. Điều kiện khởi đầu và duy trì

Bất biến I: (i) `dau === nothing ⇔ cuoi === nothing ⇔ n = 0`; (ii) `dau.truoc` và `cuoi.ke`
rỗng; (iii) với mọi u, `u.ke = v ≠ nothing ⇒ v.truoc = u`; (iv) đi theo `ke` từ `dau` gặp đúng
n nút và dừng tại `cuoi`. Danh sách rỗng thỏa I.

- Thêm đầu khi rỗng: `dau = cuoi = m`, m không có liên kết → I đúng với n = 1.
- Thêm đầu khi không rỗng: sau (1)(2), cặp (m, dau cũ) thỏa (iii); m.truoc rỗng và trở thành
  `dau` → (ii); các cặp cũ không đổi; dãy xuôi dài thêm 1 → (iv). Thêm cuối đối xứng.
- Tách p với hàng xóm a = p.truoc, b = p.ke: sau thao tác a.ke = b và b.truoc = a nên cặp mới
  (a, b) thỏa (iii); nếu a rỗng thì `dau = b` và b.truoc = a = rỗng → (ii); tương tự với b rỗng.
  Nếu cả hai rỗng thì `dau = cuoi = nothing`, n = 0 → (i). Các cặp khác không bị chạm.

Từ (iii) và (iv), duyệt ngược theo `truoc` từ `cuoi` đi qua đúng các nút của dãy xuôi theo thứ
tự ngược lại, nên `nguoc = reverse(xuoi)`. `tim_nut` duyệt theo thứ tự xuôi và trả nút đầu tiên
khớp nên chỉ xóa lần xuất hiện đầu tiên ([2,2,4] → [2,4]).

### 3.5.2. Kết thúc và output

Mỗi vòng `tim_nut`/`duyet_hai_chieu` chuyển sang nút kế; theo (iv) sau tối đa n bước gặp
`nothing`, nên vòng dừng. Bản cài còn dừng có lỗi nếu số bước vượt n (phát hiện vòng do liên
kết hỏng). Số lệnh hữu hạn nên `giai_bai` dừng. Kiểm thử (đặc biệt KT14 với 300 dãy lệnh ngẫu
nhiên) là bằng chứng bổ sung, không thay lập luận trên.

## 3.6. Phân tích độ phức tạp

Với vị trí k của nút đầu tiên có giá trị x (k = n+1 nếu không có): `tim_nut` xét đúng
min(k, n) nút; `xoa_nut!` luôn sửa đúng 2 liên kết; thêm vào danh sách rỗng sửa 2, thêm vào
danh sách khác rỗng sửa 3. Do đó tạo n nút sửa 2 + 3(n−1) liên kết. Dự đoán cho khảo sát
n = 5, 20, 100: nút xét khi xóa nút cuối hoặc giá trị không có bằng 5, 20, 100; liên kết sửa
khi tách luôn bằng 2.

**Bảng 3.4 Chi phí của từng pha trong bản cài**

| Pha thực hiện | Tham số | Phép toán đếm | Thời gian | Bộ nhớ phụ |
|---|---|---|---|---|
| Kiểm tra và chuẩn bị | \|day\|, \|lenh\| | 1 kiểm/phần tử; tạo n nút: 2+3(n−1) liên kết | O(\|day\|+\|lenh\|) | O(n) cho các nút (dữ liệu chính) |
| Thêm đầu/cuối | – | 2 hoặc 3 liên kết | O(1) | O(1) |
| Tìm theo giá trị | n, vị trí k | min(k, n) so sánh | O(n) xấu nhất, O(1) tốt nhất | O(1) |
| Tách nút đã biết | – | 2 liên kết | O(1) | O(1) |
| Kiểm nghiệm `kiem_tra_lien_ket` | n | ≤ n bước | O(n) | O(1) |
| In và định dạng (`duyet_hai_chieu`) | n | 2n bước | O(n) | O(n) cho hai mảng kết quả |
| Toàn chương trình | n ≤ 1000, m = \|lenh\| | – | O(\|day\| + m·n) (do duyệt in sau mỗi lệnh) | O(n) |

---

# CHƯƠNG 4. KẾT QUẢ THỬ NGHIỆM VÀ NHẬN XÉT

## 4.1. Môi trường và kế hoạch kiểm thử

### 4.1.1. Môi trường và phiên bản

Windows [phiên bản], PowerShell 5.1, Julia 1.12.7 (chỉ thư viện chuẩn `Test`, `Random`).
Chương trình `demo.jl`, thuật toán `src/DanhSachKep.jl`, test `test/runtests.jl`.
Repo `[URL]`, SHA chạy C `[SHA C]`. SHA nộp S ghi trong ThongTinNop.txt.

### 4.1.2. Phương pháp xác định kỳ vọng

Expected của các ca VD/TK/BIEN/KT09–KT10 được tính tay bằng cách vẽ sơ đồ nút trước khi
chạy và được khai báo cứng trong `demo.jl`/`runtests.jl`. Ngoài so sánh dãy xuôi/ngược và n,
mọi ca còn kiểm bất biến `kiem_tra_lien_ket` và `nguoc == reverse(xuoi)`; các ca biên kiểm
trực tiếp danh tính nút (`L.dau === nut2`) để phân biệt xóa đúng nút. KT14 dùng bộ giải độc
lập là `Vector` với `pushfirst!`, `push!`, `findfirst`, `deleteat!`. Không dùng số thực nên
không có sai số.

## 4.2. Bảng kết quả ít nhất 12 ca

Bộ kiểm thử có 14 ca độc lập (mỗi ca là một `@testset` có ID), tổng 1270 phép `@test`.
Miền chính hẹp nên KT11–KT14 là ca hàm con/validator/bất biến có mục tiêu riêng.

**Bảng 4.1 Ánh xạ năm ca kiểm trên phiếu**

| Ca trên phiếu | Input và kỳ vọng theo phiếu | Mã ca | Ảnh / log |
|---|---|---|---|
| Ca phiếu 1 | `[]` → hai dãy rỗng | KT09 | `demo.jl --ca=9`, test KT09 |
| Ca phiếu 2 | `[6]; xoa(6)` → đầu = cuối = nothing | BIEN01 | A05 |
| Ca phiếu 3 | `[1,2,3]; xoa(1)` → `[2,3]` | BIEN02 | A06 |
| Ca phiếu 4 | `[1,2,3]; xoa(3)` → `[1,2]` | BIEN03 | A07 |
| Ca phiếu 5 | `[2,2,4]; xoa(2)` → xuôi `[2,4]`, ngược `[4,2]` | KT10 | `demo.jl --ca=10`, test KT10 |

**Bảng 4.2 Thiết kế ít nhất 12 ca kiểm độc lập**

| Ca | Nguồn / đối tượng | Input | Expected và cách kiểm |
|---|---|---|---|
| VD01 | Ví dụ 1 / chính | `[10,20,30]; xoa(20)` | `[10,30]`, `[30,10]`, n=2; 10.ke = 30, 30.truoc = 10 |
| VD02 | Ví dụ 2 / chính | `[]; them_cuoi(5); xoa(5)` | `[]`, `[]`, n=0; dau = cuoi = nothing |
| TK01 | Tự thiết kế / chính | `[]; them_dau 3, them_dau 2, them_cuoi 4, them_dau 1, xoa 9` | `[1,2,3,4]`, `[4,3,2,1]`; xóa 9 KHONG TIM THAY, xét 4 nút, sửa 0 |
| TK02 | Tự thiết kế / chính | `[5,-1000,1000,5]; xoa 5, xoa 5, them_dau 0, xoa 1000` | từng bước `[-1000,1000,5]`, `[-1000,1000]`, `[0,-1000,1000]`, `[0,-1000]` |
| BIEN01 | Ca phiếu 2 / `xoa_nut!` | `[6]; xoa(6)` | dau = cuoi = nothing, n=0, nút bị tách không giữ liên kết |
| BIEN02 | Ca phiếu 3 / chính | `[1,2,3]; xoa(1)` | `[2,3]`/`[3,2]`; dau là nút 2 cũ, dau.truoc = nothing |
| BIEN03 | Ca phiếu 4 / chính | `[1,2,3]; xoa(3)` | `[1,2]`/`[2,1]`; cuoi là nút 2 cũ, cuoi.ke = nothing |
| LOI01 | Input sai / validator | `[10,1001,30]`; `[-1001]`; lệnh `:chen`; `[1.5]`; `"chen 5"`; `"xoa abc"`; vị trí `:giua` | `ArgumentError`; thông báo chứa `day[2]` và `1001` |
| KT09 | Ca phiếu 1 / chính | `[]`, không lệnh; xóa 7 trên rỗng | `[]`, `[]`, n=0; xóa trên rỗng trả `da_xoa=false` |
| KT10 | Ca phiếu 5 / chính | `[2,2,4]; xoa(2)` | `[2,4]`/`[4,2]`; nút đầu còn lại là số 2 thứ hai |
| KT11 | Bổ sung / giới hạn + parser | 1000 nút rồi thêm 1; 1001 phần tử; 3 chuỗi lệnh | thêm bị từ chối, n giữ 1000, liên kết hợp lệ; parser đọc đúng |
| KT12 | Bổ sung / bộ đếm | `[1..5]` xóa 1, 3, 5, 0; thêm vào rỗng rồi thêm đầu | nút xét 1, 3, 5, 5; liên kết sửa 2, 2, 2, 0; thêm 2 rồi 3 |
| KT13 | Bổ sung / `kiem_tra_lien_ket` | `[1,2,3,4]` gán nut3.truoc = nut1; n sai; tách nút lạ | hop_le=false, vi_tri=2; n sai bị phát hiện; nút lạ bị từ chối |
| KT14 | Bổ sung / oracle | 300 dãy ngẫu nhiên (seed 2026), giá trị −5..5 | xuoi = Vector oracle, nguoc = reverse, n, liên kết hợp lệ |

**Bảng 4.3 Actual, kết luận và vị trí minh chứng**

| Ca | Actual | Kết luận | Ảnh / log, SHA |
|---|---|---|---|
| VD01 | xuoi=[10,30]; nguoc=[30,10]; n=2 | Đạt | A01 / [SHA C] |
| VD02 | xuoi=[]; nguoc=[]; n=0; dau=cuoi=nothing | Đạt | A02 / [SHA C] |
| TK01 | [1,2,3,4] / [4,3,2,1]; KHONG TIM THAY 9, xét 4 | Đạt | A03 / [SHA C] |
| TK02 | [0,-1000] / [-1000,0]; n=2 | Đạt | A04 / [SHA C] |
| BIEN01 | dau=nothing; cuoi=nothing; n=0 | Đạt | A05 / [SHA C] |
| BIEN02 | [2,3] / [3,2]; dau=2 | Đạt | A06 / [SHA C] |
| BIEN03 | [1,2] / [2,1]; cuoi=2 | Đạt | A07 / [SHA C] |
| LOI01 | “day[2]: gia tri 1001 nam ngoai mien -1000..1000”; “lenh khong hop le: "chen 5"” | Đạt | A08 / [SHA C] |
| KT09 | [] / []; n=0 | Đạt | log test / [SHA C] |
| KT10 | [2,4] / [4,2] | Đạt | log test / [SHA C] |
| KT11 | thêm thứ 1001 bị từ chối, n=1000 | Đạt | log test / [SHA C] |
| KT12 | 1, 3, 5, 5 nút; 2, 2, 2, 0 liên kết | Đạt | log test / [SHA C] |
| KT13 | hop_le=false, vi_tri=2 | Đạt | log test, `--ca=11` / [SHA C] |
| KT14 | 300/300 dãy khớp oracle | Đạt | log test / [SHA C] |

## 4.3. Hai ví dụ trên phiếu

### 4.3.1. Ví dụ 1 — VD01

Input `[10,20,30]; xoa(20)`. Expected `xuoi=[10,30]; nguoc=[30,10]` xác định bằng lần vết tay
Bảng 3.3. Lệnh `julia --startup-file=no demo.jl --ca=1`. Actual khớp. [CHÈN A01]
Nhận xét: chương trình xét 2 nút để tìm 20 và sửa đúng 2 liên kết (`10.ke`, `30.truoc`), đúng
với lập luận tách nút giữa. `dau`, `cuoi` không đổi vì nút bị xóa không nằm ở biên.

### 4.3.2. Ví dụ 2 — VD02

Input `[]; them_cuoi(5); xoa(5)`. Lệnh `demo.jl --ca=2`. [CHÈN A02]
Khác VD01, thao tác thêm đi vào nhánh danh sách rỗng (sửa 2 liên kết `dau`, `cuoi`) và thao tác
xóa đi vào cả hai nhánh biên nên `dau` và `cuoi` cùng trở về `nothing`. Kết quả hai dãy rỗng,
n = 0, không còn con trỏ cũ.

## 4.4. Hai ca sinh viên tự thiết kế

### 4.4.1. Ca TK01

Mục đích: kiểm thêm xen kẽ hai đầu và xóa giá trị không có. Expected tính tay: thêm đầu 3 →
[3]; thêm đầu 2 → [2,3]; thêm cuối 4 → [2,3,4]; thêm đầu 1 → [1,2,3,4]; xóa 9 không thấy.
Lệnh `demo.jl --ca=3`. [CHÈN A03] Thao tác `xoa(9)` xét đủ 4 nút rồi dừng tại `nothing`, sửa 0
liên kết và giữ nguyên danh sách – đây là trường hợp hợp lệ không có nghiệm, khác input sai.

### 4.4.2. Ca TK02

Input `[5,-1000,1000,5]` với các lệnh `xoa 5, xoa 5, them_dau 0, xoa 1000`. Ca này có diễn tiến
khác TK01: lần xóa 5 đầu tiên trúng nút đầu (xét 1), lần thứ hai phải đi tới nút cuối (xét 3),
và dùng hai giá trị biên của miền. Lệnh `demo.jl --ca=4`. [CHÈN A04] Actual `[0,-1000]` /
`[-1000,0]`. Ca này phát hiện được lỗi xóa sai bản sao của giá trị trùng hoặc không cập nhật
`cuoi` khi xóa nút cuối.

## 4.5. Ba ca biên phù hợp với đề tài

### 4.5.1. Ca BIEN01 — ca phiếu 2

`[6]; xoa(6)`, lệnh `demo.jl --ca=5`. [CHÈN A05] Nút duy nhất vừa là đầu vừa là cuối, nên cả hai
nhánh biên của `xoa_nut!` cùng chạy; sau xóa `dau = cuoi = nothing`, n = 0.

### 4.5.2. Ca BIEN02 — ca phiếu 3

`[1,2,3]; xoa(1)`, lệnh `demo.jl --ca=6`. [CHÈN A06] Nút bị xóa là đầu, nên `dau` chuyển sang nút
2 và `truoc` của nút 2 được đặt `nothing`; kết quả `[2,3]` / `[3,2]`.

### 4.5.3. Ca BIEN03 — ca phiếu 4

`[1,2,3]; xoa(3)`, lệnh `demo.jl --ca=7`. [CHÈN A07] Nút bị xóa là cuối, nên `cuoi` lùi về nút 2,
`2.ke = nothing`; dãy ngược bắt đầu từ 2, chứng tỏ `cuoi` đã được cập nhật.

## 4.6. Kiểm tra input không hợp lệ — LOI01

Phiếu quy định giá trị −1000..1000. Input `day=[10,1001,30]` vi phạm tại phần tử thứ hai; lệnh
bàn phím `chen 5` không thuộc ba lệnh của phiếu. Lệnh `demo.jl --ca=8`. Expected: từ chối có lý
do, không tạo danh sách. Actual: “DA TU CHOI: day[2]: gia tri 1001 nam ngoai mien -1000..1000” và
“lenh khong hop le: "chen 5"”. [CHÈN A08]

## 4.7. Kết quả toàn bộ kiểm thử

Lệnh `julia --startup-file=no test/runtests.jl`: 14 ca, 1270 phép kiểm, Pass 1270, Fail 0
[CẬP NHẬT THEO ẢNH A09 BẠN TỰ CHỤP]. Số assert lớn hơn số ca vì KT14 chứa 300 lần lặp × 4 phép
kiểm. Kết quả khớp Bảng 4.3. [CHÈN A09]

## 4.8. Khảo sát ba quy mô hoặc ba cấu hình hợp lệ

### 4.8.1. Dữ liệu và điều kiện khảo sát

Ba quy mô theo phiếu Q1: n = 5, Q2: n = 20, Q3: n = 100, dữ liệu `[1,2,…,n]`. Với mỗi n, xóa
giá trị ở đầu, giữa (⌈n/2⌉), cuối và giá trị không có (0); đếm số nút xét và số liên kết sửa
bằng bộ đếm trong mã (không đo thời gian). Thêm: tạo n nút bằng thêm xen kẽ hai đầu.
Lệnh `julia --startup-file=no demo.jl --khao-sat`.

### 4.8.2. Kết quả và giới hạn nhận xét

**Bảng 4.4 Khảo sát Q1 Q2 Q3**

| Bộ | Input | Yếu tố thay đổi | Nút xét (đầu/giữa/cuối/không có) – liên kết sửa | Nhận xét |
|---|---|---|---|---|
| Q1 | `[1..5]` | n = 5 | 1 / 3 / 5 / 5 – 2 / 2 / 2 / 0; tạo 5 nút: 14 | bộ nhớ 5 nút × 2 liên kết |
| Q2 | `[1..20]` | n = 20 | 1 / 10 / 20 / 20 – 2 / 2 / 2 / 0; tạo 20 nút: 59 | tìm tăng theo vị trí |
| Q3 | `[1..100]` | n = 100 | 1 / 50 / 100 / 100 – 2 / 2 / 2 / 0; tạo 100 nút: 299 | tách vẫn 2 liên kết |

Số nút xét khi tìm tăng tuyến tính theo vị trí, đạt n khi nút ở cuối hoặc không có – khớp O(n).
Số liên kết sửa khi tách luôn là 2 ở cả ba quy mô – khớp O(1); số liên kết khi tạo n nút đúng
bằng 2 + 3(n−1). Mỗi nút cần 2 liên kết thay vì 1 như DSLK đơn. Số liệu là phép đếm trên dữ
liệu tăng dần nên không phản ánh thời gian thực hay ảnh hưởng của bộ nhớ đệm.

## 4.9. GitHub và chạy lại từ bản clone sạch

**Bảng 4.5 Kho mã và phiên bản**

| Thông tin | Giá trị |
|---|---|
| URL repo | [TỰ ĐIỀN] |
| Full SHA chạy ảnh C | [TỰ ĐIỀN – `git rev-parse HEAD`] |
| SHA S | Xem ThongTinNop.txt nộp kèm |
| Permalink hàm chính | [URL]/blob/[SHA C]/src/DanhSachKep.jl |
| Mã/kiểm thử giữa C và S | [Giống nhau / nêu phần chạy lại] |
| Lệnh chạy lại | `julia --startup-file=no demo.jl` ; `julia --startup-file=no test/runtests.jl` |

[CHÈN A10: clone vào thư mục mới, `git rev-parse HEAD`, `julia --version`, chạy demo + test]
[CHÈN A11: trang GitHub repo/commit C]

---

# CHƯƠNG 5. KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN

## 5.1. Mức hoàn thành so với phiếu

Đã cài đủ bốn hàm phiếu gợi ý (`them_kep!`, `tim_nut`, `xoa_nut!`, `duyet_hai_chieu`) và yêu
cầu tùy chọn `kiem_tra_lien_ket`. Hai ví dụ và năm ca phiếu chạy đúng (Bảng 4.1, Hình 4.1–4.7);
14 ca độc lập với 1270 phép kiểm đều đạt (Hình 4.9). Khảo sát Bảng 4.4 xác nhận tìm O(n), tách
O(1). Mã chạy lại được từ bản clone sạch (Hình 4.10).

**Bảng 5.1 Mức hoàn thành và bằng chứng**

| Mục tiêu | Mức | Bằng chứng | Giới hạn |
|---|---|---|---|
| Thêm hai đầu | Đạt | `them_kep!`; TK01, VD02 | ≤ 1000 nút |
| Tìm và xóa theo giá trị | Đạt | `tim_nut`, `xoa_nut!`; VD01, KT10 | chỉ xóa lần đầu |
| Xuất hai chiều | Đạt | `duyet_hai_chieu`; mọi ca | – |
| Đầu/cuối | Đạt | BIEN01–03 | – |
| Kiểm liên kết (tùy chọn) | Đạt | `kiem_tra_lien_ket`; KT13 | báo lỗi đầu tiên |
| Phân tích chi phí | Đạt | Bảng 3.4, 4.4 | phép đếm, không đo thời gian |

## 5.2. Giới hạn và bài học

Chương trình chỉ hỗ trợ miền phiếu (≤ 1000 nút, giá trị −1000..1000) và xóa lần xuất hiện đầu
tiên. Khi cài đặt, lỗi dễ gặp nhất là cập nhật `dau` trước khi gán `dau.truoc = m` trong thêm
đầu: dãy xuôi vẫn đúng nhưng dãy ngược thiếu nút mới. Lỗi này chỉ lộ ra khi so dãy ngược với
đảo của dãy xuôi, vì vậy mọi ca kiểm đều so cả hai chiều và chạy `kiem_tra_lien_ket`.

## 5.3. Hướng phát triển phù hợp

(1) Thêm thao tác chèn trước/sau một nút đã biết trong O(1); (2) xóa tất cả lần xuất hiện của
một giá trị trong một lượt duyệt; (3) dùng nút cầm canh (sentinel) để bỏ các nhánh đặc biệt của
đầu/cuối. Các mục này là đề xuất, chưa cài đặt.

# TÀI LIỆU THAM KHẢO

[1] Giáo trình Cấu trúc dữ liệu và Giải thuật INT1306, tệp
Giao-trinh-Cau-truc-du-lieu-va-Giai-thuat-INT1306.pdf; mục 5.2.6 Danh sách liên kết kép, trang in
122–124, trang PDF 134–136.
[2] Mã mẫu BFS của giảng viên (Ma_BFS_mau.zip) – tham khảo cách tổ chức thư mục, `Run_all.ps1`
và cách trình bày ca kiểm thử; không dùng thuật toán BFS.
[3] Julia documentation – Unit Testing (`Test`), https://docs.julialang.org/en/v1/stdlib/Test/, [ngày truy cập].

# PHỤ LỤC A. Tổ chức mã và hướng dẫn chạy

```text
DT063_DanhSachLienKetKep/
├── README.md, .gitignore, Run_all.ps1, demo.jl
├── src/DanhSachKep.jl
├── test/runtests.jl
└── docs/anh_ket_qua/ (A01–A11)
```

- Ví dụ 1: `julia --startup-file=no demo.jl --ca=1`
- Ví dụ 2: `julia --startup-file=no demo.jl --ca=2`
- Nhập mới: `julia --startup-file=no demo.jl --nhap`
- Bộ kiểm thử: `julia --startup-file=no test/runtests.jl`
- Tất cả: `powershell -ExecutionPolicy Bypass -File .\Run_all.ps1`

# PHỤ LỤC B. Danh mục bằng chứng (lệnh chụp từng ảnh)

| Mã ảnh | Ca | Lệnh chụp | Tệp |
|---|---|---|---|
| A01 | VD01 | `julia --startup-file=no demo.jl --ca=1` | 01_vi_du_1.png |
| A02 | VD02 | `... demo.jl --ca=2` | 02_vi_du_2.png |
| A03 | TK01 | `... demo.jl --ca=3` | 03_tu_thiet_ke_1.png |
| A04 | TK02 | `... demo.jl --ca=4` | 04_tu_thiet_ke_2.png |
| A05 | BIEN01 | `... demo.jl --ca=5` | 05_bien_1.png |
| A06 | BIEN02 | `... demo.jl --ca=6` | 06_bien_2.png |
| A07 | BIEN03 | `... demo.jl --ca=7` | 07_bien_3.png |
| A08 | LOI01 | `... demo.jl --ca=8` | 08_input_khong_hop_le.png |
| A09 | TEST_ALL | `julia --startup-file=no test/runtests.jl` | 09_tong_ket_kiem_thu.png |
| A10 | CLONE | `git clone ... ; git rev-parse HEAD ; julia ...` | 10_clone_sach_chay_lai.png |
| A11 | GITHUB | trang repo/commit trên trình duyệt | 11_github_repo_commit.png |
