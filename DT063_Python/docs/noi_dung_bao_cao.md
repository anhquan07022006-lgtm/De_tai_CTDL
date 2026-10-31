# BÁO CÁO ĐỒ ÁN HỌC PHẦN CẤU TRÚC DỮ LIỆU VÀ GIẢI THUẬT
## ĐỀ TÀI DT063: DANH SÁCH LIÊN KẾT KÉP VÀ DUYỆT THEO HAI CHIỀU (BẢN PYTHON + WEB)

---

## 1. THÔNG TIN BÌA VÀ PHIẾU GIAO ĐỀ TÀI

| Trường thông tin | Nội dung điền trong báo cáo |
|---|---|
| **Cơ quan chủ quản** | BỘ KHOA HỌC VÀ CÔNG NGHỆ — HỌC VIỆN CÔNG NGHỆ BƯU CHÍNH VIỄN THÔNG (CƠ SỞ TẠI TP. HỒ CHÍ MINH) |
| **Khoa** | Khoa Kỹ thuật Điện tử 2 |
| **Ngành** | Công nghệ Kỹ thuật Điện, Điện tử |
| **Học phần & Nhóm** | Cấu trúc dữ liệu và giải thuật (`INT13185`) — Nhóm 03 |
| **Giảng viên hướng dẫn** | ThS. Hồ Nhựt Minh |
| **Tên đề tài** | **DANH SÁCH LIÊN KẾT KÉP VÀ DUYỆT THEO HAI CHIỀU** |
| **Mã đề** | **DT063** |
| **Sinh viên thực hiện** | **Bùi Anh Quân** |
| **Mã số sinh viên (MSSV)** | **N24DCDT075** |
| **Lớp** | **D24CQDT01-N** |
| **Căn cứ giáo trình** | Chương 5, mục 5.2.6 Danh sách liên kết kép; trang in 122–124; trang PDF 134–136 (`Giao-trinh-Cau-truc-du-lieu-va-Giai-thuat-INT1306.pdf`) |
| **Ngôn ngữ thực hiện** | Python 3.11 (thư viện chuẩn `unittest`, `random`, `http.server`, `json`) + Giao diện Web trực quan HTML/CSS/JS |

---

## 2. NỘI DUNG PHIẾU GIAO ĐỀ TÀI (NGUYÊN VĂN THEO BỘ 91 PHIẾU)

- **Mã đề:** DT063 — INT13185 — Nhóm 03 — Giảng viên: Hồ Nhựt Minh
- **Sinh viên:** Bùi Anh Quân — MSSV: N24DCDT075 — Lớp: D24CQDT01-N
- **Tên đề tài:** Danh sách liên kết kép và duyệt theo hai chiều
- **Giáo trình:** Chương 5, 5.2.6 Danh sách liên kết kép; trang in 122–124; trang PDF 134–136.
- **Đề bài:** Xây dựng danh sách liên kết kép với liên kết trước và sau ở mỗi nút. Chương trình thêm ở hai đầu, tìm một nút theo giá trị rồi xóa nút đó, xuất danh sách theo cả hai chiều. Sinh viên kiểm sự nhất quán giữa hai liên kết và xử lý đúng thay đổi ở nút đầu, nút cuối.
- **Dữ liệu vào:** Nhập dãy số nguyên và lệnh thêm đầu/cuối hoặc xóa lần đầu theo giá trị; có thể khai báo dãy trong mã. Dùng 0–1000 nút; giá trị −1000..1000, cho phép trùng.
- **Kết quả ra:** In dãy xuôi, dãy ngược, số nút và trạng thái xóa. Dãy ngược phải đúng là thứ tự đảo của dãy xuôi.
- **Ví dụ 1:**
  - *Dữ liệu vào:* `[10,20,30]; xoa(20)`
  - *Kết quả chính:* `xuoi=[10,30]; nguoc=[30,10]` (Liên kết sau của 10 trỏ 30 và liên kết trước của 30 trỏ 10 sau khi tách nút giữa).
- **Ví dụ 2:**
  - *Dữ liệu vào:* `[]; them_cuoi(5); xoa(5)`
  - *Kết quả chính:* `xuoi=[]; nguoc=[]; n=0` (Sau khi xóa nút duy nhất, cả đầu và cuối đều trở về `None`/`nothing`, không giữ con trỏ cũ).
- **Năm bước thực hiện:**
  1. Đọc kiểu `NutKep` và vẽ hai mũi tên cho mỗi cặp nút liền nhau. Trước khi lập trình, tự viết kết quả dự kiến của ví dụ thứ nhất bằng tay.
  2. Viết cấu trúc giữ `dau`, `cuoi`, `n` và hai hàm thêm đầu/cuối. Chạy riêng hàm này trước khi ghép vào chương trình chính.
  3. Viết tìm nút rồi xóa, cập nhật riêng trường hợp nút ở đầu hoặc cuối. In trạng thái sau mỗi bước trên ví dụ đã cho.
  4. Viết duyệt xuôi/ngược, kiểm từng cặp `p.ke.truoc` trở lại đúng `p`. Nếu kết quả khác dự kiến, xác định bước đầu tiên bị sai rồi sửa.
  5. Chạy hai ví dụ và năm ca, giải thích chi phí tìm nút khác chi phí tách nút. Nộp mã có chú thích các biến và bảng kết quả năm ca kiểm.
- **Các hàm nên viết:** `them_kep(L, x, dau_hay_cuoi)`, `tim_nut(L, x)`, `xoa_nut(L, p)`, `duyet_hai_chieu(L)`, và tùy chọn `kiem_tra_lien_ket(L)`.
- **Năm ca cần kiểm tra:**
  1. `[]` → hai dãy rỗng (`KT09`).
  2. `[6]; xoa(6)` → `dau = cuoi = None` (`BIEN01`).
  3. `[1,2,3]; xoa(1)` → `[2,3]` (`BIEN02`).
  4. `[1,2,3]; xoa(3)` → `[1,2]` (`BIEN03`).
  5. `[2,2,4]; xoa(2)` → xuôi `[2,4]`, ngược `[4,2]` (`KT10`).

---

## 3. ĐỐI CHIẾU RUBRIC CHẤM (C1 – C6)

| Tiêu chí | Trọng số | Trạng thái tự đánh giá | Vị trí minh chứng trong báo cáo và mã nguồn |
|---|---|---|---|
| **C1. Đặc tả bài toán, đầu vào và đầu ra** | 1.5 | Đầy đủ | Mục 1.1–1.3; Bảng 1.1 (Input), Bảng 1.2 (Output); xử lý rỗng, trùng, không tìm thấy và từ chối input sai (`LoiDauVao`). |
| **C2. Biểu diễn dữ liệu và phần tự cài** | 2.0 | Đầy đủ | Mục 2.2, 3.2; lớp `NutKep` (`gia_tri`, `truoc`, `ke`) và `DSKep` (`dau`, `cuoi`, `n`) tự cài 100% trong `src/danh_sach_kep.py`; Bảng 2.1 bất biến. |
| **C3. Tính đúng của thuật toán và lần vết** | 2.5 | Đầy đủ | Mục 3.3–3.5; Bảng 3.3 lần vết tay từng bước ca `VD01`; chứng minh bảo toàn bất biến khi thêm/xóa và hàm `kiem_tra_lien_ket(L)`. |
| **C4. Kiểm thử, đối chiếu và độ phức tạp** | 2.0 | Đầy đủ | Mục 3.6, 4.1–4.8; Bảng 3.4 chi phí; 14 ca kiểm độc lập với 1270 phép kiểm (`tests/test_danh_sach_kep.py`); khảo sát Q1/Q2/Q3 ($n=5, 20, 100$). |
| **C5. Báo cáo, minh chứng và GitHub** | 1.0 | Đầy đủ | Chương 4, Phụ lục A–B; kịch bản `Run_all.ps1`, CLI `demo.py`, ứng dụng Web trực quan `web/app.py`. |
| **C6. Bảo vệ và giải thích sản phẩm** | 1.0 | Đầy đủ | Mục 5.2, Cẩm nang hỏi-đáp bảo vệ trên giao diện Web và giải thích chi tiết từng dòng lệnh gán con trỏ. |

---

## LỜI CAM ĐOAN

Tôi là **Bùi Anh Quân**, MSSV **N24DCDT075**, lớp **D24CQDT01-N**, cam đoan đề tài **DT063 – Danh sách liên kết kép và duyệt theo hai chiều** do tôi thực hiện. Cấu trúc nút `NutKep`, cấu trúc danh sách `DSKep` và toàn bộ các thao tác nối/tách con trỏ (`them_kep`, `tim_nut`, `xoa_nut`, `duyet_hai_chieu`, `kiem_tra_lien_ket`) đều được tự cài đặt dựa trên mục 5.2.6 của giáo trình Cấu trúc dữ liệu và Giải thuật INT1306, hoàn toàn không dùng cấu trúc danh sách có sẵn để giả lập liên kết. Toàn bộ số liệu khảo sát, bảng lần vết và 14 ca kiểm thử độc lập (1270 phép kiểm) đều là kết quả thực thi thật từ mã nguồn của đề tài và có thể chạy kiểm chứng lại qua một lệnh duy nhất.

## LỜI CẢM ƠN

Em xin gửi lời cảm ơn chân thành đến Thầy **Hồ Nhựt Minh** – giảng viên giảng dạy học phần Cấu trúc dữ liệu và Giải thuật (`INT13185`), người đã cung cấp tài liệu hướng dẫn chi tiết, khung đánh giá rõ ràng và định hướng phương pháp kiểm nghiệm chặt chẽ giúp em hoàn thành tốt đồ án cá nhân này.

## TÓM TẮT ĐỀ TÀI

Đề tài **DT063** xây dựng cấu trúc dữ liệu **Danh sách liên kết kép (Doubly Linked List)** lưu trữ các số nguyên trong miền $[-1000, 1000]$ với quy mô từ $0$ đến $1000$ nút. Mỗi nút (`NutKep`) quản lý giá trị `gia_tri` cùng hai con trỏ liên kết `truoc` (trỏ về nút đứng trước) và `ke` (trỏ sang nút đứng kế tiếp); cấu trúc danh sách (`DSKep`) quản lý hai đầu mút `dau`, `cuoi`, số nút `n`, cùng hai bộ đếm chi phí thực nghiệm `so_nut_xet` và `so_lien_ket_sua`. Chương trình cài đặt đầy đủ các phép toán cốt lõi: thêm phần tử vào đầu hoặc cuối danh sách trong thời gian $O(1)$, tìm kiếm tuyến tính nút đầu tiên mang giá trị $x$ trong thời gian $O(n)$, tách một nút đã biết địa chỉ trong thời gian $O(1)$ với xử lý chặt chẽ các trường hợp biên (xóa nút đầu, xóa nút cuối, xóa nút duy nhất), duyệt xuất danh sách theo cả hai chiều xuôi/ngược trong $O(n)$, và hàm kiểm nghiệm tự động `kiem_tra_lien_ket` nhằm phát hiện vị trí đầu tiên vi phạm bất biến `p.ke.truoc is p`. Bên cạnh giao diện dòng lệnh (`demo.py`), đề tài còn xây dựng một ứng dụng Web mô phỏng trực quan (`web/app.py` + `web/index.html`) giúp quan sát trực tiếp quá trình quét tìm nút, cập nhật con trỏ và kiểm thử tự động. Bộ kiểm thử gồm **14 ca độc lập** (bao gồm 2 ví dụ chuẩn, 5 ca trên phiếu, 2 ca tự thiết kế, 1 ca kiểm bắt lỗi đầu vào, 3 ca kiểm giới hạn/bộ đếm/liên kết hỏng và 1 ca đối chiếu 300 dãy lệnh ngẫu nhiên với bộ giải độc lập) với tổng cộng **1270 phép kiểm (assertions)** đều đạt 100%. Khảo sát thực nghiệm trên 3 quy mô $n = 5, 20, 100$ khẳng định chi phí tìm kiếm tăng tuyến tính theo vị trí nút cần xóa ($\le n$), trong khi chi phí sửa liên kết để tách nút luôn là hằng số (đúng $2$ liên kết).

---

## DANH MỤC KÝ HIỆU VÀ CHỮ VIẾT TẮT

| Ký hiệu / Thuật ngữ | Ý nghĩa trong đề tài |
|---|---|
| `DSLK` | Danh sách liên kết (Linked List) |
| `NutKep` | Kiểu dữ liệu một nút của danh sách liên kết kép (`gia_tri`, `truoc`, `ke`) |
| `DSKep` | Kiểu dữ liệu danh sách liên kết kép (`dau`, `cuoi`, `n`, `so_nut_xet`, `so_lien_ket_sua`) |
| `dau`, `cuoi` | Con trỏ trỏ tới nút đầu tiên và nút cuối cùng của danh sách (`None` khi danh sách rỗng) |
| `truoc`, `ke` | Con trỏ liên kết trỏ tới nút liền trước (`prev`) và nút liền sau (`next`) của một nút |
| `n` | Số lượng nút hiện có trong danh sách ($0 \le n \le 1000$) |
| `xuoi`, `nguoc` | Mảng kết quả thu được khi duyệt từ `dau` theo `ke` và từ `cuoi` theo `truoc` |
| `so_nut_xet` | Bộ đếm số lần so sánh giá trị nút trong quá trình tìm kiếm theo giá trị |
| `so_lien_ket_sua` | Bộ đếm số phép gán thay đổi con trỏ cấu trúc (`dau`, `cuoi`, `truoc`, `ke`) khi thêm hoặc tách nút |

---

# CHƯƠNG 1. TỔNG QUAN ĐỀ TÀI

## 1.1. Bài toán và lý do thực hiện

Trong cấu trúc danh sách liên kết đơn (Singly Linked List), mỗi nút chỉ lưu một con trỏ trỏ sang nút kế tiếp. Do hạn chế một chiều này, chương trình không thể duyệt ngược từ cuối về đầu trong thời gian tuyến tính, và khi muốn xóa một nút $p$, ta bắt buộc phải biết nút đứng ngay trước $p$ — đòi hỏi phải duyệt lại từ đầu danh sách tốn chi phí $O(n)$ ngay cả khi đã có sẵn địa chỉ của $p$.

Theo giáo trình *Cấu trúc dữ liệu và Giải thuật INT1306* (Chương 5, mục 5.2.6, trang in 122–124; trang PDF 134–136), **Danh sách liên kết kép (Doubly Linked List)** khắc phục triệt để nhược điểm trên bằng cách trang bị cho mỗi nút hai liên kết: `truoc` (trỏ tới nút đứng trước) và `ke` (trỏ tới nút đứng sau). Nhờ liên kết hai chiều và việc lưu giữ cả hai đầu mút `dau`, `cuoi`:
1. Việc thêm nút mới vào đầu hoặc cuối danh sách đều thực hiện trong thời gian hằng $O(1)$.
2. Khi đã xác định được nút $p$ cần xóa, thao tác tách $p$ ra khỏi danh sách chỉ cần nối trực tiếp hai nút hàng xóm (`p.truoc` và `p.ke`) với nhau trong thời gian $O(1)$.
3. Cho phép duyệt danh sách thuận lợi theo cả chiều xuôi lẫn chiều ngược.

Tuy nhiên, cái giá phải trả là mỗi nút tốn thêm bộ nhớ cho liên kết thứ hai, và các thao tác cập nhật con trỏ phức tạp hơn: nếu gán sai thứ tự hoặc quên cập nhật `dau`/`cuoi` ở các ca biên (danh sách rỗng, danh sách 1 nút, xóa nút đầu, xóa nút cuối), cấu trúc liên kết sẽ bị đứt gãy khiến dãy duyệt ngược không còn là đảo ngược của dãy duyệt xuôi. Vì vậy, đề tài **DT063** được thực hiện nhằm xây dựng hoàn chỉnh cấu trúc danh sách liên kết kép, kiểm chứng thực nghiệm sự khác biệt giữa chi phí tìm nút $O(n)$ với chi phí tách nút $O(1)$, đồng thời thiết lập cơ chế kiểm tra tự động tính nhất quán của các liên kết.

## 1.2. Mục tiêu và sản phẩm

Đề tài hướng tới 6 mục tiêu cụ thể kèm điều kiện hoàn thành kiểm định được:
1. **Cài đặt thao tác thêm hai đầu (`them_kep(L, x, 'dau'/'cuoi')`):** Thêm nút mới chứa giá trị $x$ vào đầu hoặc cuối danh sách trong $O(1)$. *Điều kiện hoàn thành:* Dãy xuôi có $x$ ở đúng vị trí đầu/cuối, $n$ tăng 1, sửa đúng 2 liên kết (nếu rỗng) hoặc 3 liên kết (nếu khác rỗng).
2. **Cài đặt thao tác tìm kiếm (`tim_nut(L, x)`):** Duyệt từ `dau` theo `ke`, trả về nút đầu tiên có `gia_tri == x` hoặc `None` nếu không tồn tại. *Điều kiện hoàn thành:* Với dãy có phần tử trùng như `[2, 2, 4]`, trả về đúng nút số `2` đầu tiên.
3. **Cài đặt thao tác tách nút (`xoa_nut(L, p)` và `xoa_theo_gia_tri(L, x)`):** Tách nút $p$ đã biết trong $O(1)$ (sửa đúng 2 liên kết), xử lý chính xác khi $p$ là nút đầu, nút cuối hoặc nút duy nhất; đặt `p.truoc = p.ke = None` sau khi tách.
4. **Cài đặt duyệt hai chiều (`duyet_hai_chieu(L)`):** Trả về cặp `(xuoi, nguoc)`. *Điều kiện hoàn thành:* `nguoc == list(reversed(xuoi))` và `len(xuoi) == L.n` trên mọi trạng thái.
5. **Cài đặt hàm kiểm nghiệm liên kết (`kiem_tra_lien_ket(L)` – yêu cầu tùy chọn nâng cao):** Kiểm tra toàn bộ bất biến cấu trúc và báo chính xác vị trí nút đầu tiên có liên kết `ke.truoc` không trỏ ngược lại chính nó.
6. **Bộ sản phẩm hoàn chỉnh:** Mã nguồn lõi (`src/danh_sach_kep.py`), chương trình CLI (`demo.py`), bộ kiểm thử tự động 14 ca (`tests/test_danh_sach_kep.py`), ứng dụng Web trực quan (`web/app.py`, `web/index.html`), script chạy tự động (`Run_all.ps1`) và báo cáo chi tiết.

## 1.3. Phạm vi, đầu vào và đầu ra

### 1.3.1. Miền và quy ước đầu vào
- **Dãy khởi tạo (`day`):** Mảng (hoặc chuỗi số nguyên cách nhau bởi khoảng trắng/dấu phẩy) gồm từ $0$ đến $1000$ phần tử. Mỗi phần tử là số nguyên trong đoạn $[-1000, 1000]$, cho phép các phần tử trùng giá trị. Danh sách ban đầu được tạo bằng cách thêm cuối lần lượt từng phần tử của `day`.
- **Danh sách lệnh (`lenh`):** Dãy các lệnh thuộc một trong ba dạng: `them_dau x`, `them_cuoi x`, `xoa x` (chấp nhận cả cú pháp hàm `them_dau(x)`, `them_cuoi(x)`, `xoa(x)`), với $x \in [-1000, 1000]$.
- **Giới hạn quy mô:** Tại mọi thời điểm thực thi, số nút hiện có $n$ thỏa mãn $0 \le n \le 1000$.

### 1.3.2. Kết quả và trường hợp đặc biệt
- Sau mỗi lệnh, chương trình ghi nhận: trạng thái thực hiện (`DA THEM x VAO DAU/CUOI`, `DA XOA x`, hoặc `KHONG TIM THAY x`), sơ đồ liên kết, bảng `truoc | gia_tri | ke` của từng nút, dãy `xuoi`, dãy `nguoc`, số nút `n`, số nút đã xét (`nut_xet`), số liên kết đã sửa (`lien_ket_sua`) và kết quả kiểm tra liên kết.
- **Trường hợp trùng giá trị:** Lệnh `xoa x` chỉ xóa **lần xuất hiện đầu tiên** tính từ `dau`.
- **Trường hợp không tìm thấy:** Khi xóa giá trị $x$ không có trong danh sách (hoặc xóa trên danh sách rỗng), đây là dữ liệu hợp lệ nhưng không có nút thỏa mãn; danh sách giữ nguyên, trả trạng thái `KHONG TIM THAY x`, `lien_ket_sua = 0`.
- **Trường hợp dữ liệu vào sai hợp đồng:** Giá trị ngoài đoạn $[-1000, 1000]$, kiểu dữ liệu không phải số nguyên (như `float`, `bool`, chuỗi chữ), tên lệnh ngoài 3 lệnh cho phép, hoặc thêm vượt quá $1000$ nút đều bị bộ kiểm tra (`kiem_tra_dau_vao`, `phan_tich_lenh`, `them`) từ chối ngay bằng ngoại lệ `LoiDauVao` (`ValueError`/`ArgumentError`) kèm thông báo rõ vị trí và lý do, tuyệt đối không làm hỏng danh sách hiện có.

**Bảng 1.1. Đặc tả dữ liệu vào**

| Tên dữ liệu | Kiểu và kích thước | Miền và điều kiện hợp lệ | Cách nhập hoặc khai báo |
|---|---|---|---|
| `day` | `list[int]`, dài $0..1000$ | Số nguyên $x \in [-1000, 1000]$, không nhận `bool`/`float`, cho phép trùng | Khai báo trong mã, nhập bàn phím (`--nhap`) hoặc ô nhập trên Web |
| `lenh` | `list[tuple[str, int]]` | Tên lệnh $\in \{\text{them\_dau}, \text{them\_cuoi}, \text{xoa}\}$, tham số $x \in [-1000, 1000]$ | Khai báo trực tiếp, nhập từng dòng từ bàn phím hoặc giao diện Web |
| `n` (trạng thái) | `int` | $0 \le n \le 1000$ tại mọi thời điểm | Do phương thức `them()` kiểm soát trước khi cấp phát nút |

**Bảng 1.2. Đặc tả kết quả đầu ra**

| Kết quả | Kiểu / Định dạng | Ý nghĩa và điều kiện đúng | Trường hợp rỗng / không tìm thấy / lỗi |
|---|---|---|---|
| `xuoi` | `list[int]` `[a1, ..., an]` | Dãy giá trị duyệt từ `dau` theo con trỏ `ke` | Danh sách rỗng $\rightarrow$ `[]` |
| `nguoc` | `list[int]` `[an, ..., a1]` | Dãy giá trị duyệt từ `cuoi` theo con trỏ `truoc`; bắt buộc `nguoc == reversed(xuoi)` | Danh sách rỗng $\rightarrow$ `[]` |
| `n` | `int` | Số lượng nút hiện có trong danh sách | Danh sách rỗng $\rightarrow$ `0` |
| `trang_thai` | `str` | Kết quả từng lệnh: `DA THEM...`, `DA XOA x`, `KHONG TIM THAY x` | Trùng giá trị: chỉ xóa nút đầu tiên gặp |
| `kiem_tra` | `dict` `(hop_le, vi_tri, ly_do)` | Kiểm chứng mọi bất biến liên kết hai chiều | Báo `vi_tri` nút đầu tiên có `ke.truoc != p` |
| Lỗi đầu vào | Ngoại lệ `LoiDauVao` | Thông báo rõ phần tử hoặc lệnh vi phạm miền phiếu | Từ chối thực thi, bảo toàn trạng thái danh sách |

## 1.4. Cách thực hiện và cấu trúc báo cáo

Đề tài được triển khai tuần tự theo đúng 5 bước hướng dẫn trên phiếu giao đề tài: từ phân tích lý thuyết mục 5.2.6 và vẽ sơ đồ con trỏ tay cho Ví dụ 1 $\rightarrow$ xây dựng cấu trúc `NutKep`, `DSKep` và hàm thêm hai đầu $\rightarrow$ cài đặt tìm kiếm và tách nút với xử lý biên đầu/cuối $\rightarrow$ cài đặt duyệt hai chiều và hàm kiểm nghiệm `kiem_tra_lien_ket` $\rightarrow$ thực thi kiểm thử 14 ca độc lập và khảo sát chi phí trên 3 quy mô $n = 5, 20, 100$.

**Bảng 1.3. Đối chiếu yêu cầu trên phiếu và sản phẩm thực hiện**

| Yêu cầu trên phiếu DT063 | Sản phẩm / Hàm cài đặt & Điều kiện kiểm định | Mục trình bày |
|---|---|---|
| Mỗi nút có liên kết trước và sau | Lớp `NutKep(gia_tri, truoc, ke)` sử dụng `__slots__` | Mục 2.2, 3.2 |
| Thêm phần tử ở hai đầu | `DSKep.them(x, 'dau'/'cuoi')` / `them_kep(L, x, vt)`; kiểm qua `VD02`, `TK01` | Mục 3.3, 4.3, 4.4 |
| Tìm nút theo giá trị rồi xóa | `tim_nut`, `xoa_nut`, `xoa_theo_gia_tri`; kiểm qua `VD01`, `KT10`, `TK02` | Mục 3.3, 4.3, 4.4 |
| Xuất danh sách theo hai chiều | `duyet_hai_chieu(L)` trả `(xuoi, nguoc)` thỏa `nguoc == xuoi[::-1]` | Mục 3.3, 4.2 |
| Xử lý đúng nút đầu, nút cuối | Kiểm qua 3 ca biên `BIEN01` (1 nút), `BIEN02` (xóa đầu), `BIEN03` (xóa cuối) | Mục 3.3, 4.5 |
| Kiểm tra sự nhất quán liên kết | `kiem_tra_lien_ket(L)` phát hiện vị trí lỗi đầu tiên; kiểm qua `KT13` | Mục 3.5, 4.2 |
| Khảo sát chi phí $n = 5, 20, 100$ | Bộ đếm `so_nut_xet`, `so_lien_ket_sua`; bảng khảo sát Q1, Q2, Q3 | Mục 3.6, 4.8 |

---

# CHƯƠNG 2. CƠ SỞ LÝ THUYẾT

## 2.1. Khái niệm và mô hình dữ liệu

Danh sách tuyến tính là một dãy hữu hạn gồm $n$ phần tử $(a_1, a_2, \dots, a_n)$ có thứ tự tuyến tính. Trong phương pháp biểu diễn bằng liên kết (linked representation), các phần tử không cần nằm liên tiếp nhau trong bộ nhớ mà được lưu trong các nút (nodes) rời rạc kết nối với nhau bằng các con trỏ (tham chiếu).

Trong **Danh sách liên kết kép** (giáo trình INT1306, mục 5.2.6, trang in 122–124), mỗi nút $p$ gồm ba thành phần:
- Trường dữ liệu `gia_tri`: lưu số nguyên của nút.
- Trường liên kết `truoc` (`prev`): trỏ tới nút đứng liền trước $p$ (bằng `None` nếu $p$ là nút đầu).
- Trường liên kết `ke` (`next`): trỏ tới nút đứng liền sau $p$ (bằng `None` nếu $p$ là nút cuối).

Danh sách $L$ được quản lý thông qua hai con trỏ đầu mút là `L.dau` (trỏ tới nút đầu tiên) và `L.cuoi` (trỏ tới nút cuối cùng), cùng biến nguyên `L.n` lưu số lượng nút hiện tại.

```text
Hình 2.1. Mô hình cấu trúc Danh sách liên kết kép cho Ví dụ 1 [10, 20, 30]:

       L.dau                                              L.cuoi
         ↓                                                  ↓
None ← [None | 10 | • ]  ⇄  [ • | 20 | • ]  ⇄  [ • | 30 | None] → None
          Nút 1 (A)            Nút 2 (B)            Nút 3 (C)
```

Khi tách nút giữa $B(20)$, liên kết `ke` của nút $A(10)$ được nối thẳng sang nút $C(30)$, đồng thời liên kết `truoc` của nút $C(30)$ được nối ngược về nút $A(10)$:

```text
       L.dau                        L.cuoi
         ↓                            ↓
None ← [None | 10 | • ]  ⇄  [ • | 30 | None] → None
          Nút 1 (A)            Nút 2 (C)
```

## 2.2. Cấu trúc dữ liệu sử dụng

### 2.2.1. Dữ liệu và thao tác chính
Trong mã nguồn `src/danh_sach_kep.py`, cấu trúc dữ liệu được định nghĩa tường minh gồm hai lớp:
- `NutKep`: Sử dụng `__slots__ = ("gia_tri", "truoc", "ke")` để cố định 3 trường của nút, tiết kiệm bộ nhớ và ngăn việc gán nhầm tên thuộc tính.
- `DSKep`: Quản lý `dau: Optional[NutKep]`, `cuoi: Optional[NutKep]`, `n: int`, và hai biến đếm phục vụ đo đạc thực nghiệm là `so_nut_xet: int` và `so_lien_ket_sua: int`.

### 2.2.2. Quy ước và điều kiện bất biến (Invariants)
Để cấu trúc danh sách liên kết kép luôn đúng đắn trước và sau mọi phép toán, danh sách phải thỏa mãn hệ thống **bất biến cấu trúc $I$** trong Bảng 2.1.

**Bảng 2.1. Biến cấu trúc và điều kiện bất biến phải duy trì**

| Ký hiệu / Trường | Ý nghĩa | Miền giá trị và điều kiện bất biến (Invariants) |
|---|---|---|
| `L.dau` | Tham chiếu nút đầu | `L.dau is None ⇔ L.cuoi is None ⇔ L.n == 0`; nếu `L.dau is not None` thì `L.dau.truoc is None` |
| `L.cuoi` | Tham chiếu nút cuối | Nếu `L.cuoi is not None` thì `L.cuoi.ke is None` |
| `L.n` | Số lượng nút | $0 \le \text{L.n} \le 1000$; đúng bằng số nút đi qua khi duyệt từ `L.dau` theo `ke` đến `None` |
| `u.ke`, `v.truoc` | Liên kết hai chiều | Với mọi nút $u$ trong danh sách: nếu `u.ke = v` ($v \ne \text{None}$) thì bắt buộc `v.truoc is u` |
| `xuoi`, `nguoc` | Hai dãy kết quả duyệt | `len(xuoi) == len(nguoc) == L.n` và `nguoc == list(reversed(xuoi))` |

## 2.3. Nguyên lý thuật toán

### 2.3.1. Ý tưởng xử lý các phép toán
1. **Thêm nút vào đầu/cuối (`them_kep`):**
   - Cấp phát nút mới $m$ chứa giá trị $x$ (`m.truoc = m.ke = None`).
   - *Trường hợp 1 (Danh sách đang rỗng `L.dau is None`):* Nút mới $m$ đồng thời là nút đầu và nút cuối: gán `L.dau = m` và `L.cuoi = m` (sửa **2** liên kết).
   - *Trường hợp 2 (Thêm vào đầu khi danh sách khác rỗng):* Nối `m.ke = L.dau`, nối ngược `L.dau.truoc = m`, rồi cập nhật `L.dau = m` (sửa **3** liên kết).
   - *Trường hợp 3 (Thêm vào cuối khi danh sách khác rỗng):* Đối xứng với thêm đầu: nối `m.truoc = L.cuoi`, nối xuôi `L.cuoi.ke = m`, rồi cập nhật `L.cuoi = m` (sửa **3** liên kết).
   - Tăng `L.n` thêm 1.
2. **Tìm kiếm theo giá trị (`tim_nut`):**
   - Xuất phát từ `p = L.dau`. Lặp khi `p is not None`: tăng `so_nut_xet` thêm 1; nếu `p.gia_tri == x` thì trả về ngay tham chiếu nút `p`; ngược lại chuyển sang `p = p.ke`. Nếu hết vòng lặp không gặp, trả về `None`.
3. **Tách nút đã biết tham chiếu (`xoa_nut`):**
   - Kiểm tra nhanh trong $O(1)$ xem nút $p$ có thực sự đang thuộc danh sách $L$ hay không.
   - *Cập nhật phía trước $p$:* Nếu `p.truoc is None` ($p$ là nút đầu), cập nhật `L.dau = p.ke`; ngược lại nối `p.truoc.ke = p.ke`.
   - *Cập nhật phía sau $p$:* Nếu `p.ke is None` ($p$ là nút cuối), cập nhật `L.cuoi = p.truoc`; ngược lại nối `p.ke.truoc = p.truoc`.
   - Tăng `so_lien_ket_sua` thêm **2**. Cô lập nút đã tách (`p.truoc = None`, `p.ke = None`) và giảm `L.n` đi 1.
4. **Duyệt hai chiều (`duyet_hai_chieu`):**
   - Chiều xuôi: đi từ `L.dau` theo `p = p.ke` thu thập `xuoi`.
   - Chiều ngược: đi từ `L.cuoi` theo `p = p.truoc` thu thập `nguoc`.

### 2.3.2. Điều kiện bắt đầu và kết thúc
Khởi đầu, danh sách rỗng (`dau = cuoi = None, n = 0`) thỏa mãn toàn bộ bất biến Bảng 2.1. Mọi vòng lặp duyệt và tìm kiếm đều tiến về phía `None` qua hữu hạn $n$ nút nên luôn dừng sau tối đa $n$ bước. Ngoài ra, mã cài đặt còn có chốt chặn kiểm tra số bước duyệt $\le n$ để phát hiện tức thời nếu liên kết bị hỏng tạo thành chu trình (vòng lặp vô hạn).

## 2.4. Cơ sở đánh giá thời gian và bộ nhớ

Gọi $n$ là số nút hiện có trong danh sách:
- **Phép toán tích cực (Active Operations):**
  1. Phép so sánh khóa `p.gia_tri == v` khi tìm nút (đo bằng `so_nut_xet`).
  2. Phép gán con trỏ cấu trúc `dau`, `cuoi`, `truoc`, `ke` khi nối/tách nút (đo bằng `so_lien_ket_sua`).
- **Độ phức tạp thời gian:**
  - Thêm đầu / Thêm cuối: $O(1)$ (tốn 2 hoặc 3 phép gán liên kết).
  - Tìm nút theo giá trị $x$: Tốt nhất $O(1)$ (khi $x$ ở đầu), xấu nhất và trung bình $O(n)$ (khi $x$ ở cuối hoặc không có trong danh sách).
  - Tách một nút $p$ đã biết địa chỉ: $O(1)$ (luôn tốn đúng 2 phép gán liên kết cấu trúc).
  - Xóa theo giá trị (`xoa_theo_gia_tri = tim_nut + xoa_nut`): tốn $O(n)$ cho bước tìm + $O(1)$ cho bước tách $\Rightarrow$ tổng thời gian $O(n)$.
  - Duyệt hai chiều và kiểm tra liên kết: $O(n)$.
- **Độ phức tạp bộ nhớ:**
  - Bộ nhớ lưu trữ cấu trúc: $\Theta(n)$, trong đó mỗi nút giữ 1 giá trị và **2 liên kết** (`truoc`, `ke`), tốn gấp đôi số con trỏ liên kết so với danh sách liên kết đơn.
  - Bộ nhớ phụ của các phép thêm, tìm, tách, kiểm tra liên kết: $O(1)$. Hai mảng kết quả trả về của hàm `duyet_hai_chieu` dùng $\Theta(n)$ bộ nhớ để xuất kết quả.

**Giả mã nền tảng theo giáo trình INT1306 (Chương 5, mục 5.2.6, trang in 122–124 / trang PDF 134–136):**

```text
THEM_DAU(L, x):
    m ← TaoNutKep(x)                  // m.gia_tri = x, m.truoc = None, m.ke = None
    nếu L.dau == None thì:            // Danh sách đang rỗng
        L.dau ← m; L.cuoi ← m
    ngược lại:                        // Danh sách khác rỗng
        m.ke ← L.dau
        L.dau.truoc ← m
        L.dau ← m
    L.n ← L.n + 1

THEM_CUOI(L, x):
    m ← TaoNutKep(x)
    nếu L.cuoi == None thì:           // Danh sách đang rỗng
        L.dau ← m; L.cuoi ← m
    ngược lại:
        m.truoc ← L.cuoi
        L.cuoi.ke ← m
        L.cuoi ← m
    L.n ← L.n + 1

TIM_NUT(L, x):
    p ← L.dau
    trong khi p != None thực hiện:
        nếu p.gia_tri == x thì trả về p
        p ← p.ke
    trả về None

XOA_NUT(L, p):                        // p là nút đã biết thuộc danh sách L
    nếu p.truoc == None thì:          // p là nút đầu
        L.dau ← p.ke
    ngược lại:
        p.truoc.ke ← p.ke
    nếu p.ke == None thì:             // p là nút cuối
        L.cuoi ← p.truoc
    ngược lại:
        p.ke.truoc ← p.truoc
    p.truoc ← None; p.ke ← None
    L.n ← L.n - 1
```

---

# CHƯƠNG 3. PHÂN TÍCH, THIẾT KẾ VÀ CÀI ĐẶT

## 3.1. Phân tích yêu cầu chương trình

### 3.1.1. Hợp đồng đầu vào / đầu ra (Input/Output Contract)
Hàm điều phối chính `giai_bai(day, lenh)` nhận `day` là dãy số nguyên khởi tạo và `lenh` là dãy các cặp `(ten_lenh, x)`. Hàm trả về đối tượng `KetQua` chứa danh sách `L`, trạng thái khởi tạo `ban_dau`, danh sách lịch sử từng bước `buoc`, cùng kết quả cuối `xuoi`, `nguoc`, `n`.

### 3.1.2. Kiểm tra dữ liệu đầu vào (Validator)
Hàm `kiem_tra_dau_vao(day, lenh)` và `kiem_tra_gia_tri(x)` kiểm tra nghiêm ngặt:
- Từ chối kiểu `bool` (vì trong Python `isinstance(True, int)` là `True` nên phải kiểm tra `isinstance(x, bool)` riêng!), từ chối số thực `float`, chuỗi ký tự.
- Kiểm tra miền giá trị $-1000 \le x \le 1000$ và số phần tử $|day| \le 1000$.
- Trong quá trình chạy lệnh, nếu `L.n == 1000` mà gặp lệnh `them_dau` hoặc `them_cuoi`, phương thức `them()` ném ngoại lệ `LoiDauVao` trước khi tạo hay nối nút, đảm bảo danh sách cũ không bị biến đổi (kiểm chứng tại ca `KT11`).

## 3.2. Thiết kế các hàm và dữ liệu

**Bảng 3.1. Tổ chức các hàm và tệp trong dự án**

| Hàm / Phương thức & Tệp | Input | Output | Vai trò và phần tự cài |
|---|---|---|---|
| `NutKep`, `DSKep` (`src/danh_sach_kep.py`) | Giá trị `int` | Đối tượng nút / danh sách | Cấu trúc dữ liệu tự cài với con trỏ `truoc`, `ke`, `dau`, `cuoi` |
| `DSKep.them` / `them_kep` (`src`) | `L, x, vt` | `NutKep` mới | Bước 2 phiếu – thêm đầu/cuối trong $O(1)$, đếm 2 hoặc 3 liên kết sửa |
| `DSKep.tim_nut` / `tim_nut` (`src`) | `L, x` | `NutKep` hoặc `None` | Bước 3 phiếu – tìm tuyến tính từ `dau`, đếm `so_nut_xet` |
| `DSKep.xoa_nut` / `xoa_nut` (`src`) | `L, p` | `int` (giá trị nút) | Bước 3 phiếu – tách nút $p$ trong $O(1)$, xử lý biên đầu/cuối, sửa 2 liên kết |
| `DSKep.xoa_theo_gia_tri` (`src`) | `L, x` | `dict` kết quả xóa | Ghép `tim_nut` + `xoa_nut`, trả `(da_xoa, nut_xet, lien_ket_sua)` riêng |
| `DSKep.duyet_hai_chieu` (`src`) | `L` | `(xuoi, nguoc)` | Bước 4 phiếu – duyệt 2 chiều, chặn vượt $n$ bước |
| `DSKep.kiem_tra_lien_ket` (`src`) | `L` | `dict(hop_le, vi_tri, ly_do)` | Yêu cầu tùy chọn – kiểm mọi bất biến và báo vị trí lỗi đầu tiên |
| `kiem_tra_dau_vao`, `phan_tich_lenh` (`src`) | `day, lenh` / `str` | `bool` / `(ten, x)` | Kiểm hợp đồng dữ liệu vào theo phiếu, ném `LoiDauVao` |
| `giai_bai` (`src/danh_sach_kep.py`) | `day, lenh` | `KetQua` | Thực thi toàn bộ dãy lệnh và chụp trạng thái sau từng bước |
| `demo.py` | Tham số CLI | In ra màn hình | Chạy 11 ca minh họa (`--ca 1..11`), nhập bàn phím (`--nhap`), khảo sát (`--khao-sat`) |
| `tests/test_danh_sach_kep.py` | – | Báo cáo `unittest` | 14 ca kiểm thử độc lập (`VD01`..`KT14`) với 1270 phép kiểm |
| `web/app.py`, `web/index.html` | HTTP / JSON | Giao diện Web | Máy chủ Python + trình mô phỏng hoạt ảnh trực quan, khảo sát & chạy test trực tiếp |

**Bảng 3.2. Tiền điều kiện (Preconditions) và Hậu điều kiện (Postconditions) của các hàm chính**

| Hàm và chữ ký | Tiền điều kiện | Hậu điều kiện | Xử lý lỗi / Trường hợp đặc biệt |
|---|---|---|---|
| `them_kep(L, x, vt)` | $L$ thỏa bất biến $I$; $x \in [-1000, 1000]$; $L.n < 1000$; `vt` $\in \{\text{'dau'}, \text{'cuoi'}\}$ | Nút mới $x$ ở đầu/cuối $L$; $L.n$ tăng 1; $L$ bảo toàn bất biến $I$ | Sai `vt`, $x$ ngoài miền, hoặc $L.n = 1000 \rightarrow$ ném `LoiDauVao`, $L$ giữ nguyên |
| `tim_nut(L, x)` | $L$ thỏa bất biến $I$; $x \in [-1000, 1000]$ | Trả nút đầu tiên có `gia_tri == x` hoặc `None`; $L$ không thay đổi | Danh sách rỗng hoặc không có $x \rightarrow$ trả `None` |
| `xoa_nut(L, p)` | $L$ thỏa bất biến $I$; nút $p$ đang thuộc $L$ | $p$ tách khỏi $L$; `p.truoc = p.ke = None`; $L.n$ giảm 1; $L$ bảo toàn bất biến $I$ | $p$ không thuộc $L$ hoặc liên kết quanh $p$ hỏng $\rightarrow$ ném `LoiDauVao` |
| `duyet_hai_chieu(L)` | $L$ thỏa bất biến $I$ | Trả `(xuoi, nguoc)` có độ dài $L.n$ và `nguoc == xuoi[::-1]` | Nếu có vòng làm số bước vượt $L.n \rightarrow$ ném `RuntimeError` |
| `kiem_tra_lien_ket(L)` | Danh sách $L$ ở trạng thái bất kỳ | `hop_le == True` $\iff$ $L$ thỏa mọi bất biến Bảng 2.1 | Nếu sai, trả `hop_le == False` kèm `vi_tri` nút đầu tiên bị lệch liên kết |

## 3.3. Thuật toán và mã nguồn chính

### 3.3.1. Đoạn mã thêm nút vào hai đầu (`them`) và giải thích thứ tự gán con trỏ

```python
    def them(self, x, dau_hay_cuoi: str) -> NutKep:
        """Thêm nút giá trị x vào 'dau' hoặc 'cuoi'. Thời gian O(1)."""
        vt = dau_hay_cuoi.lstrip(":") if isinstance(dau_hay_cuoi, str) else ""
        if vt not in ("dau", "cuoi"):
            raise LoiDauVao(f"vi tri them phai la 'dau' hoac 'cuoi', nhan {dau_hay_cuoi!r}")
        v = kiem_tra_gia_tri(x)
        if self.n >= SO_NUT_TOI_DA:
            raise LoiDauVao(f"danh sach da du {SO_NUT_TOI_DA} nut, khong the them {v}")
        m = NutKep(v)
        if self.dau is None:
            # Danh sách rỗng: nút mới vừa là đầu vừa là cuối.
            self.dau = m
            self.cuoi = m
            self.so_lien_ket_sua += 2
        elif vt == "dau":
            m.ke = self.dau            # (1) nút mới trỏ tới đầu cũ
            self.dau.truoc = m         # (2) đầu cũ trỏ ngược về nút mới
            self.dau = m               # (3) cập nhật con trỏ đầu
            self.so_lien_ket_sua += 3
        else:
            m.truoc = self.cuoi        # (1) nút mới trỏ ngược về cuối cũ
            self.cuoi.ke = m           # (2) cuối cũ trỏ tới nút mới
            self.cuoi = m              # (3) cập nhật con trỏ cuối
            self.so_lien_ket_sua += 3
        self.n += 1
        return m
```

**Giải thích điểm mấu chốt:** Ở nhánh thêm đầu khi danh sách khác rỗng, thứ tự 3 câu lệnh `(1) -> (2) -> (3)` là bắt buộc:
- Phải thực hiện `(1) m.ke = self.dau` và `(2) self.dau.truoc = m` **trước khi** thực hiện `(3) self.dau = m`.
- Nếu gán `self.dau = m` trước, ta sẽ mất dấu nút đầu cũ hoặc gán nhầm `self.dau.truoc = m` (tức `m.truoc = m` tự trỏ vào chính nó!), khiến nút đầu cũ không có liên kết ngược về `m`. Khi đó duyệt xuôi có thể vẫn thấy đủ nút nhưng duyệt ngược từ `cuoi` sẽ bị cụt tại nút đầu cũ!

### 3.3.2. Đoạn mã tách nút đã biết (`xoa_nut`) và xử lý 4 trường hợp biên

```python
    def xoa_nut(self, p: NutKep) -> int:
        """Tách nút p đã biết khỏi danh sách trong O(1) và trả giá trị của nó."""
        thuoc_ds = (self.dau is p if p.truoc is None else p.truoc.ke is p) and \
                   (self.cuoi is p if p.ke is None else p.ke.truoc is p)
        if not thuoc_ds:
            raise LoiDauVao("nut khong thuoc danh sach hoac lien ket da hong")

        if p.truoc is None:
            self.dau = p.ke            # p là đầu: đầu mới là nút sau p
        else:
            p.truoc.ke = p.ke          # nút trước bỏ qua p
        if p.ke is None:
            self.cuoi = p.truoc        # p là cuối: cuối mới là nút trước p
        else:
            p.ke.truoc = p.truoc       # nút sau trỏ ngược bỏ qua p
        self.so_lien_ket_sua += 2
        p.truoc = None
        p.ke = None
        self.n -= 1
        return p.gia_tri
```

**Giải thích tính tổng quát của hai khối `if/else` độc lập:**
Thay vì viết 4 nhánh `if/elif` rời rạc dễ sót trường hợp, việc tách riêng **cập nhật phía trước** (`if p.truoc is None`) và **cập nhật phía sau** (`if p.ke is None`) tự động xử lý chính xác cả 4 tình huống:
1. **$p$ là nút giữa** (`p.truoc != None` và `p.ke != None`): Thực hiện `p.truoc.ke = p.ke` và `p.ke.truoc = p.truoc`. Hai hàng xóm của $p$ nối thẳng với nhau (`VD01`).
2. **$p$ là nút đầu trong danh sách nhiều nút** (`p.truoc is None` và `p.ke != None`): Cập nhật `self.dau = p.ke` và `p.ke.truoc = None` (`BIEN02`).
3. **$p$ là nút cuối trong danh sách nhiều nút** (`p.truoc != None` và `p.ke is None`): Cập nhật `p.truoc.ke = None` và `self.cuoi = p.truoc` (`BIEN03`).
4. **$p$ là nút duy nhất** (`p.truoc is None` và `p.ke is None`): Cả hai nhánh `if` đầu đều chạy, gán `self.dau = p.ke = None` và `self.cuoi = p.truoc = None`. Danh sách trở về trạng thái rỗng chuẩn (`VD02`, `BIEN01`).

Trong cả 4 trường hợp, số liên kết cấu trúc cần sửa luôn đúng bằng **2**, và sau khi nối xong, `p.truoc` cùng `p.ke` được xóa về `None` để giải phóng hoàn toàn tham chiếu cũ.

## 3.4. Lần vết ví dụ nhỏ bằng tay

Xét ca **VD01** (Ví dụ 1 trên phiếu):
- **Input:** `day = [10, 20, 30]`, `lenh = [xoa(20)]`.
- **Kỳ vọng tính tay (Expected):** `xuoi = [10, 30]`, `nguoc = [30, 10]`, `n = 2`, `nut_xet = 2`, `lien_ket_sua = 2`.
Gọi 3 nút được tạo từ `day` lần lượt là $A(10)$, $B(20)$, $C(30)$.

**Bảng 3.3. Bảng truy vết từng bước thực hiện ca VD01**

| Bước | Thao tác thực hiện | Trạng thái trước thao tác | Trạng thái sau thao tác | Giải thích & Bộ đếm |
|---|---|---|---|---|
| **0** | `tao_danh_sach([10, 20, 30])` | Danh sách rỗng (`dau=None, cuoi=None, n=0`) | `dau=A, cuoi=C, n=3`; `A(None, 10, B)`, `B(A, 20, C)`, `C(B, 30, None)` | Thêm cuối 3 lần, sau đó đặt lại bộ đếm `so_nut_xet = 0`, `so_lien_ket_sua = 0` |
| **1** | `tim_nut(L, 20)`: xét `p = L.dau = A` | `p = A(10)`, `so_nut_xet = 0` | `10 != 20` $\rightarrow$ chuyển `p = A.ke = B`; `so_nut_xet = 1` | Nút đầu có giá trị 10 khác 20 nên đi tiếp sang nút kế |
| **2** | `tim_nut(L, 20)`: xét `p = B` | `p = B(20)`, `so_nut_xet = 1` | `20 == 20` $\rightarrow$ dừng tìm, trả về nút `B`; `so_nut_xet = 2` | Tìm thấy lần xuất hiện đầu tiên của 20 tại vị trí 2 |
| **3** | `xoa_nut(L, B)`: kiểm `thuoc_ds` | `B.truoc = A` (`A.ke is B`) và `B.ke = C` (`C.truoc is B`) | `thuoc_ds == True` | Xác nhận $B$ đang nằm hợp lệ trong danh sách $L$ |
| **4** | Nhánh trước của `xoa_nut`: `B.truoc is not None` | `A.ke` đang trỏ tới `B` | `A.ke = B.ke = C`; `so_lien_ket_sua = 1` | Liên kết `ke` của nút $A(10)$ bỏ qua $B$, trỏ thẳng sang $C(30)$ |
| **5** | Nhánh sau của `xoa_nut`: `B.ke is not None` | `C.truoc` đang trỏ tới `B` | `C.truoc = B.truoc = A`; `so_lien_ket_sua = 2` | Liên kết `truoc` của nút $C(30)$ bỏ qua $B$, trỏ ngược về $A(10)$ |
| **6** | Cô lập nút $B$ và giảm $n$ | `B.truoc = A, B.ke = C, n = 3` | `B.truoc = None, B.ke = None, n = 2` | Nút $B$ tách rời hoàn toàn; `dau=A`, `cuoi=C` giữ nguyên |
| **Cuối** | `duyet_hai_chieu(L)` & `kiem_tra_lien_ket(L)` | `A(None, 10, C)` $\rightleftarrows$ `C(A, 30, None)` | `xuoi = [10, 30]`, `nguoc = [30, 10]`, `n = 2`, `hop_le = True` | Khớp 100% kỳ vọng tính tay |

## 3.5. Giải thích tính đúng và điều kiện dừng

### 3.5.1. Chứng minh bảo toàn bất biến (Invariant Preservation)
Ta chứng minh mọi phép toán biến đổi cấu trúc (`them` và `xoa_nut`) đều duy trì bất biến $I$ ở Bảng 2.1:
- **Khởi tạo:** Danh sách rỗng có `dau = cuoi = None` và `n = 0`, thỏa mãn hiển nhiên mọi điều kiện của $I$.
- **Khi thực hiện `them(x, 'dau')`:**
  - Nếu danh sách rỗng: `dau = cuoi = m`, `m.truoc = m.ke = None`, `n = 1` $\Rightarrow$ thỏa $I$.
  - Nếu danh sách khác rỗng (gọi đầu cũ là $d_0$): Sau `m.ke = d0`, `d0.truoc = m`, `dau = m`, cặp liên kết mới $(m, d_0)$ thỏa mãn `m.ke.truoc = d0.truoc = m`; đồng thời `dau.truoc = m.truoc = None`; các cặp nút cũ từ $d_0$ tới `cuoi` không bị thay đổi; độ dài chuỗi xuôi tăng từ $n$ lên $n+1$ $\Rightarrow$ bảo toàn $I$. (Tương tự hoàn toàn theo tính đối xứng cho `them(x, 'cuoi')`).
- **Khi thực hiện `xoa_nut(p)`:**
  - Gọi $a = p.\text{truoc}$ và $b = p.\text{ke}$.
  - Nếu $a \ne \text{None}$ và $b \ne \text{None}$: sau phép gán `a.ke = b` và `b.truoc = a`, cặp nút mới kề nhau $(a, b)$ thỏa mãn `a.ke.truoc = b.truoc = a`.
  - Nếu $a = \text{None}$ ($p$ là đầu): `dau` trở thành $b$; nếu $b \ne \text{None}$ thì `b.truoc` được gán bằng $a = \text{None}$ nên `dau.truoc is None` được giữ vững.
  - Nếu $b = \text{None}$ ($p$ là cuối): `cuoi` trở thành $a$; nếu $a \ne \text{None}$ thì `a.ke` được gán bằng $b = \text{None}$ nên `cuoi.ke is None` được giữ vững.
  - Nếu cả $a = \text{None}$ và $b = \text{None}$: `dau = cuoi = None` và `n` giảm từ 1 về 0 $\Rightarrow$ thỏa điều kiện danh sách rỗng.

Hệ quả trực tiếp: Vì chuỗi xuôi từ `dau` đến `cuoi` là $(u_1, u_2, \dots, u_n)$ với $u_i.\text{ke} = u_{i+1} \iff u_{i+1}.\text{truoc} = u_i$, nên khi duyệt ngược từ `cuoi` ($u_n$) theo `truoc` về `dau` ($u_1$), ta đi qua đúng dãy $(u_n, u_{n-1}, \dots, u_1)$, suy ra `nguoc == list(reversed(xuoi))` luôn đúng.

### 3.5.2. Điều kiện dừng
Mọi vòng lặp trong `tim_nut`, `duyet_hai_chieu`, `kiem_tra_lien_ket` đều tiến 1 bước qua con trỏ `ke` (hoặc `truoc`) trên chuỗi hữu hạn $n$ nút không có chu trình, do đó chắc chắn kết thúc sau không quá $n$ bước lặp.

## 3.6. Phân tích độ phức tạp

**Bảng 3.4. Chi phí thời gian, phép toán đếm và bộ nhớ của từng pha trong bản cài đặt**

| Pha / Thao tác thực hiện | Tham số | Số phép toán đếm chính xác | Thời gian | Bộ nhớ phụ |
|---|---|---|---|---|
| Kiểm tra đầu vào & Khởi tạo $n$ nút | $\|day\|=n, \|lenh\|=m$ | Kiểm tra $n+m$ phần tử; tạo $n$ nút ($n \ge 1$) tốn $2 + 3(n-1)$ liên kết sửa | $O(n + m)$ | $\Theta(n)$ cho $n$ nút dữ liệu |
| Thêm đầu / Thêm cuối (`them`) | $n$ | $2$ liên kết (nếu $n=0$) hoặc $3$ liên kết (nếu $n \ge 1$) | $O(1)$ | $O(1)$ (1 nút mới) |
| Tìm nút theo giá trị (`tim_nut`) | $n$, vị trí $k$ | $\min(k, n)$ phép so sánh (`so_nut_xet`), với $k=n+1$ nếu không có | Tốt nhất $O(1)$, xấu nhất $O(n)$ | $O(1)$ |
| Tách nút đã biết (`xoa_nut`) | – | Luôn đúng $2$ liên kết sửa (`so_lien_ket_sua`) | $O(1)$ | $O(1)$ |
| Duyệt hai chiều (`duyet_hai_chieu`) | $n$ | $2n$ bước duyệt ($n$ bước xuôi + $n$ bước ngược) | $O(n)$ | $\Theta(n)$ cho 2 mảng kết quả |
| Kiểm tra liên kết (`kiem_tra_lien_ket`) | $n$ | $\le n$ bước kiểm tra `q.truoc is p` | $O(n)$ | $O(1)$ |
| Toàn bộ chương trình (`giai_bai`) | $n \le 1000, m=\|lenh\|$ | Tổng qua $m$ lệnh (mỗi lệnh có chụp trạng thái duyệt) | $O(\|day\| + m \cdot n)$ | $\Theta(n)$ |

---

# CHƯƠNG 4. KẾT QUẢ THỬ NGHIỆM VÀ NHẬN XÉT

## 4.1. Môi trường và kế hoạch kiểm thử

- **Môi trường thực thi:** Hệ điều hành Windows 10/11 (64-bit), PowerShell, Python 3.11.15 (chỉ sử dụng thư viện chuẩn `unittest`, `random`, `http.server`), kèm kiểm chứng song song trên Julia 1.12.7.
- **Phương pháp xác định kỳ vọng (Expected):**
  - Với các ca `VD01`, `VD02`, `TK01`, `TK02`, `BIEN01`–`BIEN03`, `KT09`–`KT13`: Kết quả kỳ vọng được tính tay độc lập trước khi chạy chương trình. Bên cạnh kiểm tra giá trị mảng `xuoi`/`nguoc`, bài kiểm thử còn kiểm tra trực tiếp định danh đối tượng nút (`assertIs(L.dau, nut2)`) để đảm bảo chương trình thực sự xóa đúng nút đầu tiên trong trường hợp trùng khóa (`KT10`).
  - Với ca `KT14`: Sử dụng bộ giải độc lập (Oracle) là kiểu `list` chuẩn của Python (`insert(0, x)`, `append(x)`, `remove(x)`) đối chiếu trên **300 dãy lệnh sinh ngẫu nhiên** (cố định `seed = 2026` để tái lập 100%).

## 4.2. Bảng kết quả 14 ca kiểm thử độc lập

**Bảng 4.1. Ánh xạ 5 ca kiểm bắt buộc trên phiếu giao đề tài**

| Ca trên phiếu | Input và kỳ vọng theo phiếu DT063 | Mã ca trong dự án | Lệnh kiểm chứng |
|---|---|---|---|
| **Ca phiếu 1** | `[]` $\rightarrow$ hai dãy rỗng `xuoi = []`, `nguoc = []` | `KT09` | `python demo.py --ca 9` & test `KT09` |
| **Ca phiếu 2** | `[6]; xoa(6)` $\rightarrow$ `dau = cuoi = None`, `n = 0` | `BIEN01` | `python demo.py --ca 5` (Ảnh A05) |
| **Ca phiếu 3** | `[1,2,3]; xoa(1)` $\rightarrow$ `xuoi = [2,3]`, `nguoc = [3,2]` | `BIEN02` | `python demo.py --ca 6` (Ảnh A06) |
| **Ca phiếu 4** | `[1,2,3]; xoa(3)` $\rightarrow$ `xuoi = [1,2]`, `nguoc = [2,1]` | `BIEN03` | `python demo.py --ca 7` (Ảnh A07) |
| **Ca phiếu 5** | `[2,2,4]; xoa(2)` $\rightarrow$ chỉ xóa số 2 đầu: `xuoi = [2,4]`, `nguoc = [4,2]` | `KT10` | `python demo.py --ca 10` & test `KT10` |

**Bảng 4.2. Thiết kế và kết quả thực tế (Actual) của 14 ca kiểm độc lập**

| Mã ca | Nhóm / Đối tượng kiểm | Dữ liệu vào (Input) | Kỳ vọng (Expected) | Kết quả thực tế (Actual) | Số assert | Kết luận |
|---|---|---|---|---|---|---|
| **VD01** | Ví dụ 1 / Xóa nút giữa | `day=[10,20,30]; xoa(20)` | `xuoi=[10,30], nguoc=[30,10], n=2`; `10.ke is 30`, `30.truoc is 10` | `xuoi=[10,30], nguoc=[30,10], n=2, xet=2, sua=2` | 6 | **Đạt (A01)** |
| **VD02** | Ví dụ 2 / Thêm & xóa nút duy nhất | `day=[]; them_cuoi(5); xoa(5)` | `xuoi=[], nguoc=[], n=0`; `dau = cuoi = None` | `xuoi=[], nguoc=[], n=0, dau=None, cuoi=None` | 3 | **Đạt (A02)** |
| **TK01** | Tự thiết kế 1 / Thêm 2 đầu & xóa không có | `day=[]; them_dau 3, 2; them_cuoi 4; them_dau 1; xoa 9` | `xuoi=[1,2,3,4], nguoc=[4,3,2,1]`; `xoa(9)` báo `KHONG TIM THAY 9`, `xet=4, sua=0` | `xuoi=[1,2,3,4], nguoc=[4,3,2,1]`; `KHONG TIM THAY 9`, `xet=4, sua=0` | 7 | **Đạt (A03)** |
| **TK02** | Tự thiết kế 2 / Biên $\pm 1000$ & trùng lặp | `day=[5,-1000,1000,5]; xoa 5, xoa 5, them_dau 0, xoa 1000` | Qua 4 bước: `[-1000,1000,5]` $\rightarrow$ `[-1000,1000]` $\rightarrow$ `[0,-1000,1000]` $\rightarrow$ `[0,-1000]` | `xuoi=[0,-1000], nguoc=[-1000,0], n=2`, mọi bước hợp lệ | 5 | **Đạt (A04)** |
| **BIEN01** | Biên 1 (Ca phiếu 2) / 1 nút | `day=[6]; xoa(6)` | `dau = cuoi = None, n=0`; nút tách rời `p.truoc = p.ke = None` | `xuoi=[], nguoc=[], n=0, dau=None, cuoi=None` | 4 | **Đạt (A05)** |
| **BIEN02** | Biên 2 (Ca phiếu 3) / Xóa đầu | `day=[1,2,3]; xoa(1)` | `xuoi=[2,3], nguoc=[3,2]`; `dau` trỏ sang nút 2, `dau.truoc is None` | `xuoi=[2,3], nguoc=[3,2], n=2, dau=2, cuoi=3` | 4 | **Đạt (A06)** |
| **BIEN03** | Biên 3 (Ca phiếu 4) / Xóa cuối | `day=[1,2,3]; xoa(3)` | `xuoi=[1,2], nguoc=[2,1]`; `cuoi` lùi về nút 2, `cuoi.ke is None` | `xuoi=[1,2], nguoc=[2,1], n=2, dau=1, cuoi=2` | 4 | **Đạt (A07)** |
| **LOI01** | Input không hợp lệ / Validator | `day=[10,1001,30]`; `[-1001]`; lệnh `chen 5`; `[1.5]`; `[True]`; `"xoa abc"` | Ném `LoiDauVao` chỉ rõ `day[2]` chứa `1001` và lệnh `"chen 5"` không hợp lệ | Bắt đúng cả 9 trường hợp lỗi, thông báo chính xác vị trí | 9 | **Đạt (A08)** |
| **KT09** | Ca phiếu 1 / Danh sách rỗng | `day=[], lenh=[]`; thử `xoa(7)` và `tim_nut(7)` trên rỗng | `xuoi=[], nguoc=[], n=0`; `da_xoa=False`, `tim_nut=None` | Khớp hoàn toàn, không sinh lỗi con trỏ rỗng | 4 | **Đạt** |
| **KT10** | Ca phiếu 5 / Trùng giá trị | `day=[2,2,4]; xoa(2)` | Chỉ xóa số 2 đầu tiên; `L.dau` mới chính là đối tượng nút số 2 thứ hai | `xuoi=[2,4], nguoc=[4,2], n=2`; `L.dau is nut2_thu_hai` | 4 | **Đạt** |
| **KT11** | Giới hạn 1000 nút & Parser | Tạo 1000 nút rồi thêm 1; mảng 1001 phần tử; phân tích chuỗi lệnh | Từ chối thêm nút thứ 1001, bảo toàn `n=1000` hợp lệ; parser đọc đúng | `L.n == 1000`, `hop_le == True`; parser phân tích chính xác | 7 | **Đạt** |
| **KT12** | Kiểm bộ đếm chi phí | Trên `[1..5]` xóa 1, 3, 5, 0; thêm vào rỗng rồi thêm đầu | `nut_xet` = 1, 3, 5, 5; `lien_ket_sua` = 2, 2, 2, 0; thêm: 2 rồi +3 = 5 | Khớp chính xác tuyệt đối mọi bộ đếm | 10 | **Đạt** |
| **KT13** | Phát hiện liên kết hỏng | Trên `[1,2,3,4]` cố ý gán `nut3.truoc = nut1`; gán sai `n=3`; xóa nút lạ | `kiem_tra_lien_ket` trả `hop_le=False, vi_tri=2`; từ chối xóa nút lạ | `hop_le=False, vi_tri=2, ly_do="nut 2: ke.truoc khong tro lai nut 2"` | 4 | **Đạt** |
| **KT14** | Đối chiếu Oracle ngẫu nhiên | 300 dãy khởi tạo và dãy lệnh ngẫu nhiên (`seed=2026`) | `xuoi == ref`, `nguoc == ref[::-1]`, `n == len(ref)`, `hop_le == True` | 300/300 dãy lệnh (1200 phép kiểm) khớp tuyệt đối với Oracle | 1200 | **Đạt** |

## 4.3. Phân tích chi tiết hai ví dụ trên phiếu (VD01, VD02)

### 4.3.1. Ví dụ 1 — Ca VD01 (`python demo.py --ca 1`)
```text
Ca VD01: Ví dụ 1 của phiếu - xóa nút giữa
Input  : day=[10,20,30]; lenh=xoa(20)
Expected (tinh tay): xuoi=[10,30]; nguoc=[30,10]; n=2

Buoc 1 - xoa(20) -> DA XOA 20
  So nut xet khi tim: 2; so lien ket sua: 2
  So do : dau -> [10] <-> [30] <- cuoi
    vi tri | truoc   | gia tri | ke
    1      | None    | 10      | 30
    2      | 10      | 30      | None
  xuoi=[10,30]; nguoc=[30,10]; n=2
  dau=10; cuoi=30
  nguoc == dao(xuoi): DUNG; kiem_tra_lien_ket: HOP LE (moi cap ke/truoc khop)
Actual : xuoi=[10,30]; nguoc=[30,10]; n=2  => KET LUAN: KHOP KY VONG
```
- **Nhận xét đối chiếu:** Kết quả thực tế (`Actual`) khớp hoàn toàn với bảng lần vết tay Bảng 3.3. Chương trình xét đúng 2 nút (nút 10 rồi đến nút 20) và sửa đúng 2 liên kết (`10.ke = 30` và `30.truoc = 10`). Hai đầu mút `dau = 10` và `cuoi = 30` được giữ nguyên vì nút bị xóa nằm ở giữa.

### 4.3.2. Ví dụ 2 — Ca VD02 (`python demo.py --ca 2`)
```text
Ca VD02: Ví dụ 2 của phiếu - thêm rồi xóa nút duy nhất
Input  : day=[]; lenh=them_cuoi(5); xoa(5)
Expected (tinh tay): xuoi=[]; nguoc=[]; n=0
Buoc 1 - them_cuoi(5) -> DA THEM 5 VAO CUOI (So nut xet: 0; so lien ket sua: 2; dau=5; cuoi=5)
Buoc 2 - xoa(5)       -> DA XOA 5           (So nut xet: 1; so lien ket sua: 2; dau=None; cuoi=None)
Actual : xuoi=[]; nguoc=[]; n=0  => KET LUAN: KHOP KY VONG
```
- **Nhận xét đối chiếu:** Khác với `VD01`, ở Bước 1 thao tác thêm đi vào nhánh danh sách rỗng nên chỉ sửa 2 liên kết (`dau = cuoi = 5`). Ở Bước 2, khi xóa nút duy nhất `5`, cả hai nhánh biên (`p.truoc is None` và `p.ke is None`) trong `xoa_nut` cùng kích hoạt, đưa cả `dau` và `cuoi` về `None`, không để sót con trỏ treo (dangling pointer).

## 4.4. Phân tích hai ca tự thiết kế (TK01, TK02)

### 4.4.1. Ca TK01 — Thêm xen kẽ hai đầu và xóa phần tử không tồn tại (`python demo.py --ca 3`)
- **Input:** `day = []`, `lenh = [them_dau(3), them_dau(2), them_cuoi(4), them_dau(1), xoa(9)]`.
- **Kết quả:** Sau 4 lệnh thêm xen kẽ, danh sách đạt trạng thái `dau -> [1] <-> [2] <-> [3] <-> [4] <- cuoi` (`xuoi = [1,2,3,4]`, `nguoc = [4,3,2,1]`). Ở Bước 5 (`xoa(9)`), chương trình duyệt qua đủ 4 nút (`nut_xet = 4`), gặp `None` nên kết luận `KHONG TIM THAY 9`, `lien_ket_sua = 0` và giữ nguyên danh sách. Ca này chứng minh chương trình phân biệt đúng giữa *input hợp lệ nhưng không tìm thấy khóa cần xóa* với *input vi phạm miền*.

### 4.4.2. Ca TK02 — Giá trị biên $\pm 1000$, khóa trùng lặp và xóa liên tiếp (`python demo.py --ca 4`)
- **Input:** `day = [5, -1000, 1000, 5]`, `lenh = [xoa(5), xoa(5), them_dau(0), xoa(1000)]`.
- **Kết quả:** Lần `xoa(5)` thứ nhất xóa nút `5` ở đầu (`nut_xet = 1`, `dau` mới là `-1000`). Lần `xoa(5)` thứ hai phải duyệt tới cuối danh sách mới gặp số `5` còn lại (`nut_xet = 3`, `cuoi` mới lùi về `1000`). Tiếp theo `them_dau(0)` đưa `0` lên đầu, và `xoa(1000)` xóa tiếp nút cuối mới. Kết quả cuối `xuoi = [0, -1000]`, `nguoc = [-1000, 0]`, `n = 2` khớp tuyệt đối với kỳ vọng.

## 4.5. Phân tích ba ca biên hợp lệ của đề tài (BIEN01, BIEN02, BIEN03)

1. **Ca BIEN01 (`python demo.py --ca 5` – Ca phiếu 2):** `day = [6]; lenh = xoa(6)`. Kiểm tra xóa trên danh sách chỉ có đúng 1 nút. Sau khi xóa, `dau = None, cuoi = None, n = 0`, hai dãy duyệt đều rỗng `[]`.
2. **Ca BIEN02 (`python demo.py --ca 6` – Ca phiếu 3):** `day = [1, 2, 3]; lenh = xoa(1)`. Kiểm tra xóa nút đầu khi danh sách có nhiều nút (`nut_xet = 1, lien_ket_sua = 2`). Sau khi xóa `1`, con trỏ `dau` cập nhật sang nút `2` và `2.truoc` được gán `None`, cho ra `xuoi = [2, 3]`, `nguoc = [3, 2]`.
3. **Ca BIEN03 (`python demo.py --ca 7` – Ca phiếu 4):** `day = [1, 2, 3]; lenh = xoa(3)`. Kiểm tra xóa nút cuối khi danh sách có nhiều nút (`nut_xet = 3, lien_ket_sua = 2`). Sau khi xóa `3`, con trỏ `cuoi` lùi về nút `2` và `2.ke` được gán `None`. Dãy duyệt ngược bắt đầu từ `cuoi` xuất ra `[2, 1]`, chứng minh `cuoi` đã được cập nhật đúng.

## 4.6. Kiểm tra input không hợp lệ — Ca LOI01 (`python demo.py --ca 8`)

```text
Ca LOI01: Input sai bị từ chối (ngoài miền -1000..1000 & lệnh lạ)
Input  : day=[10,1001,30]; lenh=xoa(10)
Expected: validator tu choi, bao day[2] = 1001 ngoai mien; khong tao danh sach.
DA TU CHOI: day[2]: gia tri 1001 nam ngoai mien -1000..1000

Input bo sung: lenh go tu ban phim "chen 5" (ten lenh khong co trong phieu)
DA TU CHOI: lenh khong hop le: "chen 5" (dung them_dau x | them_cuoi x | xoa x)
KET LUAN: KHOP KY VONG (loi du kien da duoc bat, chuong trinh khong dung bat thuong)
```
- **Nhận xét:** Bộ kiểm tra đầu vào đã phát hiện chính xác phần tử thứ 2 (`1001`) vượt ngưỡng tối đa `1000` của phiếu, đồng thời từ chối tên lệnh `"chen 5"` không nằm trong tập lệnh hợp lệ `{them_dau, them_cuoi, xoa}` với thông báo tường minh.

## 4.7. Kết quả chạy toàn bộ bộ kiểm thử (`python tests/test_danh_sach_kep.py`)

Khi thực thi lệnh `python tests/test_danh_sach_kep.py`, toàn bộ **14 ca kiểm độc lập** gồm **1270 phép kiểm (`assert`)** hoàn tất trong khoảng `0.03s` với kết quả **ĐẠT 100% (PASS 14/14 ca, 0 Fail)**.

**Bảng 4.3. Tổng kết kết quả thực thi bộ kiểm thử tự động (`tests/test_danh_sach_kep.py`)**

```text
test_BIEN01_mot_nut (__main__.TestDT063.test_BIEN01_mot_nut) ... ok
test_BIEN02_xoa_dau (__main__.TestDT063.test_BIEN02_xoa_dau) ... ok
test_BIEN03_xoa_cuoi (__main__.TestDT063.test_BIEN03_xoa_cuoi) ... ok
test_KT09_danh_sach_rong (__main__.TestDT063.test_KT09_danh_sach_rong) ... ok
test_KT10_trung_chi_xoa_dau_tien (__main__.TestDT063.test_KT10_trung_chi_xoa_dau_tien) ... ok
test_KT11_gioi_han_va_phan_tich (__main__.TestDT063.test_KT11_gioi_han_va_phan_tich) ... ok
test_KT12_bo_dem (__main__.TestDT063.test_KT12_bo_dem) ... ok
test_KT13_phat_hien_lien_ket_hong (__main__.TestDT063.test_KT13_phat_hien_lien_ket_hong) ... ok
test_KT14_ngau_nhien_oracle (__main__.TestDT063.test_KT14_ngau_nhien_oracle) ... ok
test_LOI01_validator (__main__.TestDT063.test_LOI01_validator) ... ok
test_TK01_them_xen_ke (__main__.TestDT063.test_TK01_them_xen_ke) ... ok
test_TK02_bien_trung_lap (__main__.TestDT063.test_TK02_bien_trung_lap) ... ok
test_VD01_vi_du_1 (__main__.TestDT063.test_VD01_vi_du_1) ... ok
test_VD02_vi_du_2 (__main__.TestDT063.test_VD02_vi_du_2) ... ok
----------------------------------------------------------------------
Ran 14 tests in 0.029s -> OK (14 ca độc lập, 1270 phép kiểm PASS 100%)
```

## 4.8. Khảo sát chi phí trên ba quy mô hợp lệ ($n = 5, 20, 100$)

Thực hiện lệnh `python demo.py --khao-sat` trên ba quy mô theo phiếu giao đề tài: **Q1 ($n = 5$)**, **Q2 ($n = 20$)** và **Q3 ($n = 100$)** với dãy ban đầu `[1, 2, ..., n]`.

**Bảng 4.4. Kết quả khảo sát thực nghiệm trên 3 quy mô Q1 ($n=5$), Q2 ($n=20$), Q3 ($n=100$)**

| Quy mô | Tác vụ khảo sát trên dãy `[1..n]` | Số nút xét (`so_nut_xet`) | Số liên kết sửa (`so_lien_ket_sua`) | Số nút sau (`n`) | Kiểm liên kết | Quy luật & Nhận xét thực nghiệm |
|---|---|---|---|---|---|---|
| **Q1 ($n=5$)** | Xóa nút đầu ($x=1$) | 1 | 2 | 4 | Hợp lệ | Gặp ngay ở vị trí 1 $\rightarrow O(1)$ |
| **Q1 ($n=5$)** | Xóa nút giữa ($x=3$) | 3 | 2 | 4 | Hợp lệ | Duyệt $\lceil n/2 \rceil = 3$ nút |
| **Q1 ($n=5$)** | Xóa nút cuối ($x=5$) | 5 | 2 | 4 | Hợp lệ | Duyệt hết $n = 5$ nút |
| **Q1 ($n=5$)** | Xóa giá trị không có ($x=0$) | 5 | 0 | 5 | Hợp lệ | Duyệt $n=5$ nút, không sửa liên kết |
| **Q1 ($n=5$)** | Tạo $n=5$ nút xen kẽ 2 đầu | 0 | 14 | 5 | Hợp lệ | $2 + 3(5-1) = 14$ liên kết |
| **Q2 ($n=20$)** | Xóa đầu / giữa ($10$) / cuối ($20$) / không có ($0$) | 1 / 10 / 20 / 20 | 2 / 2 / 2 / 0 | 19 / 19 / 19 / 20 | Hợp lệ | Số nút xét tỉ lệ thuận với vị trí |
| **Q2 ($n=20$)** | Tạo $n=20$ nút xen kẽ 2 đầu | 0 | 59 | 20 | Hợp lệ | $2 + 3(20-1) = 59$ liên kết |
| **Q3 ($n=100$)** | Xóa đầu / giữa ($50$) / cuối ($100$) / không có ($0$) | 1 / 50 / 100 / 100 | 2 / 2 / 2 / 0 | 99 / 99 / 99 / 100 | Hợp lệ | Khi $n$ gấp 20 lần (từ 5 lên 100), tìm cuối tăng 20 lần |
| **Q3 ($n=100$)** | Tạo $n=100$ nút xen kẽ 2 đầu | 0 | 299 | 100 | Hợp lệ | $2 + 3(100-1) = 299$ liên kết |

**Nhận xét từ số liệu khảo sát:**
1. **Sự khác biệt bản chất giữa Tìm kiếm và Tách nút:** Khi quy mô $n$ tăng từ $5 \rightarrow 20 \rightarrow 100$, số nút phải xét khi tìm phần tử ở giữa ($3 \rightarrow 10 \rightarrow 50$) và ở cuối ($5 \rightarrow 20 \rightarrow 100$) tăng tuyến tính đúng theo cấp độ phức tạp $O(n)$. Ngược lại, một khi đã tìm được nút cần xóa, số liên kết cấu trúc phải sửa để tách nút đó ra khỏi danh sách **luôn bất biến bằng 2** ở mọi quy mô ($n=5, 20, 100$) và mọi vị trí (đầu, giữa, cuối), khẳng định chi phí tách nút là $O(1)$.
2. **Chi phí tạo danh sách:** Nút đầu tiên thêm vào danh sách rỗng sửa 2 liên kết (`dau`, `cuoi`); mỗi nút trong $n-1$ nút tiếp theo thêm vào đầu hoặc cuối sửa đúng 3 liên kết, nên tổng số liên kết sửa khi tạo $n$ nút luôn tuân theo công thức chính xác $2 + 3(n-1)$.

## 4.9. GitHub và chạy lại từ bản clone sạch

**Bảng 4.5. Kho mã nguồn GitHub và thông tin phiên bản**

| Thông tin | Giá trị thực tế |
|---|---|
| **URL Repository GitHub** | `https://github.com/anhquan07022006-lgtm/De_tai_CTDL` |
| **Full SHA chạy ảnh (`Commit C`)** | `6f975545a0e0edeb881c5508ad88e592e79e96ed` |
| **SHA phiên bản nộp (`Commit S`)** | Xem tệp `N24DCDT075_DT063_BuiAnhQuan_ThongTinNop.txt` nộp kèm |
| **Permalink tệp thuật toán chính** | `https://github.com/anhquan07022006-lgtm/De_tai_CTDL/blob/6f975545a0e0edeb881c5508ad88e592e79e96ed/DT063_Python/src/danh_sach_kep.py` |
| **Permalink tệp kiểm thử** | `https://github.com/anhquan07022006-lgtm/De_tai_CTDL/blob/6f975545a0e0edeb881c5508ad88e592e79e96ed/DT063_Python/tests/test_danh_sach_kep.py` |
| **Mã / kiểm thử giữa C và S** | Giống nhau 100% (không thay đổi logic thuật toán hay dữ liệu kiểm thử) |
| **Lệnh chạy lại sau khi clone** | `powershell -ExecutionPolicy Bypass -File .\DT063_Python\Run_all.ps1` |

---

# CHƯƠNG 5. KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN

## 5.1. Mức độ hoàn thành so với phiếu giao đề tài

**Bảng 5.1. Tổng hợp mức độ hoàn thành các yêu cầu của đề tài DT063**

| Yêu cầu trên phiếu | Mức độ hoàn thành | Bằng chứng kiểm định | Giới hạn tuân thủ theo phiếu |
|---|---|---|---|
| Xây dựng `NutKep`, `DSKep` và thêm ở hai đầu | **Hoàn thành 100%** | `src/danh_sach_kep.py`; ca `VD02`, `TK01`, `KT12` | Tối đa $1000$ nút, giá trị $[-1000, 1000]$ |
| Tìm nút đầu tiên theo giá trị và tách nút đó | **Hoàn thành 100%** | `tim_nut`, `xoa_nut`; ca `VD01`, `KT10`, `TK02` | Chỉ xóa lần xuất hiện đầu tiên tính từ `dau` |
| Xuất danh sách theo hai chiều xuôi/ngược | **Hoàn thành 100%** | `duyet_hai_chieu`; kiểm trên cả 14 ca và 300 dãy ngẫu nhiên | Dãy ngược luôn là đảo ngược của dãy xuôi |
| Xử lý đúng thay đổi ở nút đầu, nút cuối | **Hoàn thành 100%** | Ba ca biên `BIEN01` (1 nút), `BIEN02` (đầu), `BIEN03` (cuối) | Đặt lại `None` khi xóa nút duy nhất |
| Kiểm tra sự nhất quán liên kết (yêu cầu tùy chọn) | **Hoàn thành 100%** | `kiem_tra_lien_ket`; ca `KT13` (`--ca 11`) | Báo chính xác vị trí đầu tiên có `ke.truoc != p` |
| Phân tích chi phí & Khảo sát $n = 5, 20, 100$ | **Hoàn thành 100%** | Bảng 3.4, Bảng 4.4; lệnh `python demo.py --khao-sat` | Đếm số nút xét và số liên kết sửa thực tế |
| Giao diện trực quan hóa (Mở rộng nâng cao) | **Hoàn thành 100%** | Ứng dụng Web `web/app.py` + `web/index.html` | Hoạt ảnh từng bước, bảng liên kết, chạy test & khảo sát |

## 5.2. Giới hạn và bài học kinh nghiệm

1. **Giới hạn của sản phẩm:** Tuân thủ đúng hợp đồng của phiếu giao đề tài, chương trình giới hạn số nút $0 \le n \le 1000$, miền giá trị số nguyên $[-1000, 1000]$, và thao tác xóa theo giá trị chỉ tách nút đầu tiên bắt gặp khi duyệt từ `dau`.
2. **Bài học kinh nghiệm khi lập trình con trỏ hai chiều:**
   - Lỗi dễ mắc nhất khi cài đặt danh sách liên kết kép là gán `L.dau = m` trước khi gán `L.dau.truoc = m` trong hàm thêm đầu (hoặc quên đặt `L.cuoi = None` khi xóa nút cuối cùng làm danh sách rỗng). Những lỗi này thường không phát hiện được nếu chỉ in dãy xuôi, nhưng sẽ lộ ra ngay lập tức khi đối chiếu dãy duyệt ngược với đảo ngược của dãy xuôi hoặc chạy hàm `kiem_tra_lien_ket(L)`.
   - Khi tách nút $p$, việc gán `p.truoc = None` và `p.ke = None` phải thực hiện ở cuối cùng sau khi đã nối xong `p.truoc` và `p.ke` với nhau.

## 5.3. Hướng phát triển

1. Bổ sung thao tác chèn một nút mới vào ngay trước hoặc ngay sau một nút $p$ đã biết địa chỉ trong thời gian $O(1)$.
2. Bổ sung thao tác xóa tất cả các nút mang giá trị $x$ chỉ trong một lượt duyệt $O(n)$.
3. Sử dụng kỹ thuật nút cầm canh (Sentinel/Dummy Head & Tail) để hợp nhất hoàn toàn các nhánh biên và nhánh giữa trong mọi thao tác chèn/xóa.

---

# TÀI LIỆU THAM KHẢO

1. Học viện Công nghệ Bưu chính Viễn thông, *Giáo trình Cấu trúc dữ liệu và Giải thuật (INT1306)*, Chương 5: Danh sách liên kết, Mục 5.2.6: Danh sách liên kết kép, trang in 122–124 (trang PDF 134–136).
2. Hồ Nhựt Minh (2026), *Đồ án mẫu BFS End-to-End và Rubric chấm 91 đề tài cá nhân học phần Cấu trúc dữ liệu và Giải thuật (INT13185 – Nhóm 03)*.
3. Python Software Foundation, *Python 3.11 Standard Library Documentation – `unittest` Unit testing framework & `http.server`*, https://docs.python.org/3/library/unittest.html.

---

# PHỤ LỤC A. TỔ CHỨC MÃ NGUỒN VÀ HƯỚNG DẪN CHẠY LẠI

## A.1. Cây thư mục dự án Python + Web (`DT063_Python`)

```text
DT063_Python/
├── README.md                     # Hướng dẫn tổng quan và bảng lệnh chạy nhanh
├── Run_all.ps1                   # Script chạy tự động toàn bộ 11 demo + khảo sát + 14 ca test
├── demo.py                       # Chương trình CLI: chạy từng ca, nhập bàn phím, khảo sát
├── src/
│   ├── __init__.py
│   └── danh_sach_kep.py          # Cài đặt lõi: NutKep, DSKep, them_kep, tim_nut, xoa_nut...
├── tests/
│   ├── __init__.py
│   └── test_danh_sach_kep.py     # Bộ kiểm thử tự động 14 ca độc lập (1270 phép kiểm)
├── cac_bai_code_rieng/           # 12 tệp code .py độc lập tương ứng từng ca thử mẫu (Bài 01..12)
│   ├── bai_01_VD01_xoa_nut_giua.py
│   ├── ...
│   └── bai_12_KT13_phat_hien_dut_lien_ket_va_oracle.py
├── web/
│   ├── __init__.py
│   ├── app.py                    # Máy chủ HTTP chuẩn Python (/api/giai, /api/khao-sat, /api/test)
│   ├── index.html                # Giao diện Web mô phỏng trực quan từng bước (chạy được cả offline)
│   └── Chay_Web_Server.bat       # File bấm đúp khởi động nhanh máy chủ Web
└── docs/
    ├── anh_ket_qua/              # Thư mục lưu 11 ảnh minh chứng A01–A11
    └── noi_dung_bao_cao.md       # Nội dung báo cáo toàn văn đề tài DT063
```

## A.2. Các lệnh thực thi và kiểm chứng

```powershell
# 1. Di chuyển vào thư mục dự án
cd "d:\Đề tài ctdl cuối kỳ\PHAT_CHO_SINH_VIEN_2026_10_17\DT063_Python"

# 2. Chạy một lệnh duy nhất kiểm tra toàn bộ (11 ca demo + khảo sát + 14 ca kiểm thử)
powershell -ExecutionPolicy Bypass -File .\Run_all.ps1

# 3. Chạy từng phần riêng biệt trên dòng lệnh
python demo.py                             # Chạy 2 ví dụ trên phiếu (VD01, VD02)
python demo.py --ca 1                      # Chạy ca cụ thể từ 1 đến 11 (VD01..KT13)
python demo.py --nhap                      # Nhập dữ liệu mới trực tiếp từ bàn phím
python demo.py --khao-sat                  # Chạy khảo sát chi phí Q1 (n=5), Q2 (n=20), Q3 (n=100)
python tests/test_danh_sach_kep.py         # Chạy bộ kiểm thử 14 ca độc lập (1270 phép kiểm)

# 4. Khởi động ứng dụng Web trực quan tại http://127.0.0.1:8000
python web/app.py
```

---

# PHỤ LỤC B. DANH MỤC 11 ẢNH MINH CHỨNG (A01 – A11)

| Mã ảnh | Hình trong báo cáo | Tên tệp ảnh | Ca kiểm / Nội dung | Lệnh thực thi để chụp ảnh |
|---|---|---|---|---|
| **A01** | Hình 4.1 | `01_vi_du_1.png` | `VD01`: `[10,20,30]; xoa(20)` $\rightarrow$ `[10,30]` | `python demo.py --ca 1` (hoặc chọn chip `VD01` trên Web) |
| **A02** | Hình 4.2 | `02_vi_du_2.png` | `VD02`: `[]; them_cuoi(5); xoa(5)` $\rightarrow$ `[]` | `python demo.py --ca 2` (hoặc chọn chip `VD02` trên Web) |
| **A03** | Hình 4.3 | `03_tu_thiet_ke_1.png` | `TK01`: Thêm xen kẽ 2 đầu, xóa 9 không có | `python demo.py --ca 3` (hoặc chọn chip `TK01` trên Web) |
| **A04** | Hình 4.4 | `04_tu_thiet_ke_2.png` | `TK02`: Biên $\pm 1000$, trùng lặp, xóa liên tiếp | `python demo.py --ca 4` (hoặc chọn chip `TK02` trên Web) |
| **A05** | Hình 4.5 | `05_bien_1.png` | `BIEN01` (Ca phiếu 2): `[6]; xoa(6)` $\rightarrow$ rỗng | `python demo.py --ca 5` (hoặc chọn chip `BIEN01` trên Web) |
| **A06** | Hình 4.6 | `06_bien_2.png` | `BIEN02` (Ca phiếu 3): `[1,2,3]; xoa(1)` $\rightarrow$ `[2,3]` | `python demo.py --ca 6` (hoặc chọn chip `BIEN02` trên Web) |
| **A07** | Hình 4.7 | `07_bien_3.png` | `BIEN03` (Ca phiếu 4): `[1,2,3]; xoa(3)` $\rightarrow$ `[1,2]` | `python demo.py --ca 7` (hoặc chọn chip `BIEN03` trên Web) |
| **A08** | Hình 4.8 | `08_input_khong_hop_le.png` | `LOI01`: Từ chối giá trị `1001` và lệnh `chen 5` | `python demo.py --ca 8` (hoặc chọn chip `LOI01` trên Web) |
| **A09** | Hình 4.9 | `09_tong_ket_kiem_thu.png` | Tổng kết 14 ca kiểm độc lập, 1270 phép kiểm PASS | `python tests/test_danh_sach_kep.py` |
| **A10** | Hình 4.10 | `10_clone_sach_chay_lai.png` | Clone repo vào thư mục mới và chạy `Run_all.ps1` | `git clone <URL> ; cd ... ; .\Run_all.ps1` |
| **A11** | Hình 4.11 | `11_github_repo_commit.png` | Giao diện trang GitHub repository và commit SHA | Chụp màn hình trình duyệt trang GitHub cá nhân |

