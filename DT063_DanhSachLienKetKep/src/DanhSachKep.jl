"""
DT063 - Danh sách liên kết kép và duyệt theo hai chiều.
Giáo trình INT1306, Chương 5, mục 5.2.6; trang in 122–124; trang PDF 134–136.

Mọi thao tác trên liên kết (thêm hai đầu, tìm, tách nút, duyệt xuôi/ngược,
kiểm tra nhất quán) đều tự cài; không dùng Vector để giả lập danh sách.
Vector chỉ dùng để trả kết quả duyệt ra ngoài.
"""
module DanhSachKep

export NutKep, DSKep, them_kep!, tim_nut, xoa_nut!, xoa_theo_gia_tri!,
       duyet_hai_chieu, kiem_tra_lien_ket, tao_danh_sach, kiem_tra_gia_tri,
       kiem_tra_dau_vao, phan_tich_lenh, giai_bai, so_do, bang_lien_ket,
       dat_lai_bo_dem!, SO_NUT_TOI_DA, GIA_TRI_MIN, GIA_TRI_MAX

const SO_NUT_TOI_DA = 1000   # phiếu: 0..1000 nút
const GIA_TRI_MIN = -1000    # phiếu: giá trị -1000..1000, cho phép trùng
const GIA_TRI_MAX = 1000
const LENH_HOP_LE = (:them_dau, :them_cuoi, :xoa)

"""
    NutKep

Một nút của danh sách kép.
- `gia_tri`: số nguyên lưu trong nút.
- `truoc` : nút đứng trước (`nothing` nếu là nút đầu).
- `ke`    : nút đứng sau (`nothing` nếu là nút cuối).
"""
mutable struct NutKep
    gia_tri::Int
    truoc::Union{NutKep,Nothing}
    ke::Union{NutKep,Nothing}
end
NutKep(x::Int) = NutKep(x, nothing, nothing)

"""
    DSKep

Danh sách liên kết kép.
- `dau`, `cuoi`: nút đầu và nút cuối (`nothing` khi rỗng).
- `n`          : số nút hiện có.
- `so_nut_xet` : bộ đếm số nút đã so sánh khi tìm theo giá trị.
- `so_lien_ket_sua`: bộ đếm số lần gán vào trường dau/cuoi/truoc/ke
  để nối hoặc tách cấu trúc (không đếm phép xóa liên kết của nút đã tách).

Bất biến: dau === nothing ⇔ cuoi === nothing ⇔ n == 0;
dau.truoc === nothing; cuoi.ke === nothing;
với mọi nút u có u.ke = v thì v.truoc === u.
"""
mutable struct DSKep
    dau::Union{NutKep,Nothing}
    cuoi::Union{NutKep,Nothing}
    n::Int
    so_nut_xet::Int
    so_lien_ket_sua::Int
end
DSKep() = DSKep(nothing, nothing, 0, 0, 0)

"""Đặt lại hai bộ đếm chi phí về 0."""
function dat_lai_bo_dem!(L::DSKep)
    L.so_nut_xet = 0
    L.so_lien_ket_sua = 0
    return L
end

"""
    kiem_tra_gia_tri(x) -> Int

Chấp nhận số nguyên trong -1000..1000; ngược lại ném `ArgumentError`.
"""
function kiem_tra_gia_tri(x)
    (x isa Integer && !(x isa Bool)) ||
        throw(ArgumentError("gia tri phai la so nguyen, nhan $(repr(x))"))
    GIA_TRI_MIN <= x <= GIA_TRI_MAX ||
        throw(ArgumentError("gia tri $x nam ngoai mien $GIA_TRI_MIN..$GIA_TRI_MAX"))
    return Int(x)
end

"""
    them_kep!(L, x, dau_hay_cuoi) -> NutKep

Thêm nút giá trị `x` vào đầu (`:dau`) hoặc cuối (`:cuoi`). Thời gian O(1).
"""
function them_kep!(L::DSKep, x, dau_hay_cuoi::Symbol)
    dau_hay_cuoi in (:dau, :cuoi) ||
        throw(ArgumentError("vi tri them phai la :dau hoac :cuoi, nhan :$dau_hay_cuoi"))
    v = kiem_tra_gia_tri(x)
    L.n < SO_NUT_TOI_DA ||
        throw(ArgumentError("danh sach da du $SO_NUT_TOI_DA nut, khong the them $v"))
    m = NutKep(v)
    if L.dau === nothing
        # Danh sách rỗng: nút mới vừa là đầu vừa là cuối.
        L.dau = m
        L.cuoi = m
        L.so_lien_ket_sua += 2
    elseif dau_hay_cuoi === :dau
        m.ke = L.dau          # (1) nút mới trỏ tới đầu cũ
        L.dau.truoc = m       # (2) đầu cũ trỏ ngược về nút mới
        L.dau = m             # (3) cập nhật con trỏ đầu
        L.so_lien_ket_sua += 3
    else
        m.truoc = L.cuoi      # (1) nút mới trỏ ngược về cuối cũ
        L.cuoi.ke = m         # (2) cuối cũ trỏ tới nút mới
        L.cuoi = m            # (3) cập nhật con trỏ cuối
        L.so_lien_ket_sua += 3
    end
    L.n += 1
    return m
end

"""
    tim_nut(L, x) -> Union{NutKep,Nothing}

Duyệt từ đầu, trả nút ĐẦU TIÊN có giá trị `x`, hoặc `nothing`. Thời gian O(n).
Mỗi nút được so sánh làm tăng `L.so_nut_xet` thêm 1.
"""
function tim_nut(L::DSKep, x)
    v = kiem_tra_gia_tri(x)
    p = L.dau
    while p !== nothing
        L.so_nut_xet += 1
        p.gia_tri == v && return p
        p = p.ke
    end
    return nothing
end

"""
    xoa_nut!(L, p) -> Int

Tách nút `p` đã biết khỏi `L` trong O(1) và trả giá trị của nó.
Xử lý riêng `p` là đầu (cập nhật `L.dau`) hoặc cuối (cập nhật `L.cuoi`).
Sau khi tách, `p.truoc` và `p.ke` được đặt `nothing` để không giữ con trỏ cũ.
"""
function xoa_nut!(L::DSKep, p::NutKep)
    # Kiểm tra O(1): p phải đang được hai hàng xóm (hoặc dau/cuoi) trỏ tới.
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

"""
    xoa_theo_gia_tri!(L, x) -> NamedTuple

Tìm lần xuất hiện đầu tiên của `x` rồi tách. Trả
`(da_xoa, nut_xet, lien_ket_sua)` của riêng thao tác này.
"""
function xoa_theo_gia_tri!(L::DSKep, x)
    xet0, sua0 = L.so_nut_xet, L.so_lien_ket_sua
    p = tim_nut(L, x)
    da_xoa = p !== nothing
    da_xoa && xoa_nut!(L, p)
    return (da_xoa = da_xoa, nut_xet = L.so_nut_xet - xet0,
            lien_ket_sua = L.so_lien_ket_sua - sua0)
end

"""
    duyet_hai_chieu(L) -> (xuoi, nguoc)

Duyệt xuôi theo `ke` từ `dau` và duyệt ngược theo `truoc` từ `cuoi`.
Ném lỗi nếu số bước vượt `L.n` (dấu hiệu vòng hoặc `n` sai). Thời gian O(n).
"""
function duyet_hai_chieu(L::DSKep)
    xuoi = Int[]
    p = L.dau
    while p !== nothing
        length(xuoi) < L.n || error("duyet xuoi vuot n=$(L.n): lien ket hong hoac co vong")
        push!(xuoi, p.gia_tri)
        p = p.ke
    end
    nguoc = Int[]
    p = L.cuoi
    while p !== nothing
        length(nguoc) < L.n || error("duyet nguoc vuot n=$(L.n): lien ket hong hoac co vong")
        push!(nguoc, p.gia_tri)
        p = p.truoc
    end
    return (xuoi = xuoi, nguoc = nguoc)
end

"""
    kiem_tra_lien_ket(L) -> (hop_le, vi_tri, ly_do)

Kiểm sự nhất quán: dau/cuoi/n đồng bộ, dau.truoc rỗng, mỗi cặp p.ke.truoc === p,
nút cuối của chuỗi xuôi là `L.cuoi`, số nút đúng bằng `n`.
`vi_tri` là vị trí (từ 1) của nút đầu tiên có liên kết không khớp; 0 nếu hợp lệ
hoặc lỗi nằm ở mức danh sách.
"""
function kiem_tra_lien_ket(L::DSKep)
    if L.dau === nothing || L.cuoi === nothing
        ok = L.dau === nothing && L.cuoi === nothing && L.n == 0
        return ok ? (hop_le = true, vi_tri = 0, ly_do = "danh sach rong hop le") :
                    (hop_le = false, vi_tri = 0, ly_do = "dau/cuoi khong dong thoi rong hoac n != 0")
    end
    L.dau.truoc === nothing ||
        return (hop_le = false, vi_tri = 1, ly_do = "dau.truoc phai la nothing")
    p = L.dau
    i = 1
    while true
        i <= L.n || return (hop_le = false, vi_tri = i, ly_do = "so nut vuot n=$(L.n) (co the co vong)")
        q = p.ke
        if q === nothing
            p === L.cuoi ||
                return (hop_le = false, vi_tri = i, ly_do = "nut cuoi chuoi xuoi khong phai L.cuoi")
            i == L.n ||
                return (hop_le = false, vi_tri = i, ly_do = "dem duoc $i nut nhung n=$(L.n)")
            return (hop_le = true, vi_tri = 0, ly_do = "moi cap ke/truoc khop")
        end
        q.truoc === p ||
            return (hop_le = false, vi_tri = i, ly_do = "nut $i: ke.truoc khong tro lai nut $i")
        p = q
        i += 1
    end
end

"""
    tao_danh_sach(day) -> DSKep

Tạo danh sách từ dãy ban đầu bằng cách thêm cuối lần lượt, sau đó đặt lại bộ đếm.
"""
function tao_danh_sach(day::AbstractVector)
    length(day) <= SO_NUT_TOI_DA ||
        throw(ArgumentError("day ban dau co $(length(day)) phan tu, vuot $SO_NUT_TOI_DA"))
    L = DSKep()
    for x in day
        them_kep!(L, x, :cuoi)
    end
    return dat_lai_bo_dem!(L)
end

"""
    phan_tich_lenh(s) -> Tuple{Symbol,Int}

Đọc một lệnh dạng `them_dau 5`, `them_cuoi(5)`, `xoa -3`.
"""
function phan_tich_lenh(s::AbstractString)
    m = match(r"^\s*(them_dau|them_cuoi|xoa)\s*\(?\s*([+-]?\d+)\s*\)?\s*;?\s*$", s)
    m === nothing && throw(ArgumentError("lenh khong hop le: \"$s\" (dung them_dau x | them_cuoi x | xoa x)"))
    x = tryparse(Int, m.captures[2])
    x === nothing && throw(ArgumentError("so khong doc duoc trong lenh \"$s\""))
    return (Symbol(m.captures[1]), kiem_tra_gia_tri(x))
end

"""
    kiem_tra_dau_vao(day, lenh) -> true

Hợp đồng input của phiếu: `day` là dãy số nguyên dài 0..1000, giá trị -1000..1000;
`lenh` là dãy cặp `(ten, x)` với `ten ∈ (:them_dau, :them_cuoi, :xoa)`, x trong miền.
Vi phạm -> `ArgumentError` có lý do. Giới hạn 1000 nút trong quá trình chạy do
`them_kep!` kiểm.
"""
function kiem_tra_dau_vao(day, lenh)
    day isa AbstractVector || throw(ArgumentError("day ban dau phai la mang"))
    length(day) <= SO_NUT_TOI_DA ||
        throw(ArgumentError("day ban dau co $(length(day)) phan tu, vuot $SO_NUT_TOI_DA"))
    for (i, x) in enumerate(day)
        try
            kiem_tra_gia_tri(x)
        catch e
            e isa ArgumentError || rethrow()
            throw(ArgumentError("day[$i]: " * e.msg))
        end
    end
    lenh isa AbstractVector || throw(ArgumentError("danh sach lenh phai la mang"))
    for (k, c) in enumerate(lenh)
        (c isa Tuple && length(c) == 2 && c[1] isa Symbol) ||
            throw(ArgumentError("lenh $k phai co dang (ten, x), nhan $(repr(c))"))
        c[1] in LENH_HOP_LE ||
            throw(ArgumentError("lenh $k: ten :$(c[1]) khong thuoc them_dau/them_cuoi/xoa"))
        kiem_tra_gia_tri(c[2])
    end
    return true
end

"""
    giai_bai(day, lenh) -> NamedTuple

Kiểm input, tạo danh sách, chạy lần lượt các lệnh và ghi trạng thái sau mỗi lệnh.
Trả `(L, buoc, xuoi, nguoc, n)`; mỗi phần tử `buoc` gồm
`lenh, trang_thai, xuoi, nguoc, n, nut_xet, lien_ket_sua, hop_le`.
"""
function giai_bai(day, lenh)
    kiem_tra_dau_vao(day, lenh)
    L = tao_danh_sach(day)
    buoc = NamedTuple[]
    for (ten, x) in lenh
        xet0, sua0 = L.so_nut_xet, L.so_lien_ket_sua
        if ten === :them_dau || ten === :them_cuoi
            them_kep!(L, x, ten === :them_dau ? :dau : :cuoi)
            trang_thai = "DA THEM $x VAO $(ten === :them_dau ? "DAU" : "CUOI")"
        else
            kq = xoa_theo_gia_tri!(L, x)
            trang_thai = kq.da_xoa ? "DA XOA $x" : "KHONG TIM THAY $x"
        end
        d = duyet_hai_chieu(L)
        push!(buoc, (lenh = "$(ten)($x)", trang_thai = trang_thai,
                     xuoi = d.xuoi, nguoc = d.nguoc, n = L.n,
                     nut_xet = L.so_nut_xet - xet0,
                     lien_ket_sua = L.so_lien_ket_sua - sua0,
                     hop_le = kiem_tra_lien_ket(L).hop_le))
    end
    d = duyet_hai_chieu(L)
    return (L = L, buoc = buoc, xuoi = d.xuoi, nguoc = d.nguoc, n = L.n)
end

"""Sơ đồ một dòng: `dau -> [10] <-> [30] <- cuoi`."""
function so_do(L::DSKep)
    L.dau === nothing && return "dau = nothing, cuoi = nothing (rong)"
    phan = String[]
    p = L.dau
    while p !== nothing && length(phan) <= L.n
        push!(phan, "[$(p.gia_tri)]")
        p = p.ke
    end
    return "dau -> " * join(phan, " <-> ") * " <- cuoi"
end

"""Bảng liên kết từng nút: vị trí, giá trị của nút trước, giá trị, giá trị của nút sau."""
function bang_lien_ket(L::DSKep)
    ten(q) = q === nothing ? "nothing" : string(q.gia_tri)
    dong = ["vi tri | truoc   | gia tri | ke"]
    p = L.dau
    i = 1
    while p !== nothing && i <= L.n
        push!(dong, rpad(string(i), 6) * " | " * rpad(ten(p.truoc), 7) * " | " *
                    rpad(string(p.gia_tri), 7) * " | " * ten(p.ke))
        p = p.ke
        i += 1
    end
    return join(dong, "\n")
end

end # module DanhSachKep
