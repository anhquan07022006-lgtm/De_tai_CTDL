include(joinpath(@__DIR__, "src", "DanhSachKep.jl"))
using .DanhSachKep

const DE = "DT063 - DANH SACH LIEN KET KEP VA DUYET THEO HAI CHIEU"

fmt(v) = "[" * join(v, ",") * "]"
ten_lenh(c) = "$(c[1])($(c[2]))"

"""In trạng thái đầy đủ của danh sách: sơ đồ, bảng liên kết, hai dãy, n, kiểm liên kết."""
function in_trang_thai(L)
    d = duyet_hai_chieu(L)
    kt = kiem_tra_lien_ket(L)
    println("  So do : ", so_do(L))
    for dong in split(bang_lien_ket(L), '\n')
        println("    ", dong)
    end
    println("  xuoi=", fmt(d.xuoi), "; nguoc=", fmt(d.nguoc), "; n=", L.n)
    println("  dau=", L.dau === nothing ? "nothing" : L.dau.gia_tri,
            "; cuoi=", L.cuoi === nothing ? "nothing" : L.cuoi.gia_tri)
    println("  nguoc == dao(xuoi): ", d.nguoc == reverse(d.xuoi) ? "DUNG" : "SAI",
            "; kiem_tra_lien_ket: ", kt.hop_le ? "HOP LE" : "LOI tai vi tri $(kt.vi_tri)", " (", kt.ly_do, ")")
end

"""
Chạy một ca: in input, expected tính tay trước, trạng thái sau từng lệnh và kết luận.
`ky_vong` = (xuoi, nguoc, n).
"""
function chay_ca(ma, mo_ta, day, lenh, ky_vong)
    println(DE)
    println("Ca ", ma, ": ", mo_ta)
    println("Input  : day=", fmt(day), "; lenh=", isempty(lenh) ? "(khong co)" : join(ten_lenh.(lenh), "; "))
    println("Expected (tinh tay): xuoi=", fmt(ky_vong[1]), "; nguoc=", fmt(ky_vong[2]), "; n=", ky_vong[3])
    kiem_tra_dau_vao(day, lenh)
    L = tao_danh_sach(day)
    println("\nBuoc 0 - khoi tao tu day ban dau")
    in_trang_thai(L)
    for (k, c) in enumerate(lenh)
        xet0, sua0 = L.so_nut_xet, L.so_lien_ket_sua
        if c[1] === :xoa
            kq = xoa_theo_gia_tri!(L, c[2])
            tt = kq.da_xoa ? "DA XOA $(c[2]) (lan xuat hien dau tien)" : "KHONG TIM THAY $(c[2]), danh sach giu nguyen"
        else
            them_kep!(L, c[2], c[1] === :them_dau ? :dau : :cuoi)
            tt = "DA THEM $(c[2]) VAO $(c[1] === :them_dau ? "DAU" : "CUOI")"
        end
        println("\nBuoc ", k, " - ", ten_lenh(c), " -> ", tt)
        println("  So nut xet khi tim: ", L.so_nut_xet - xet0,
                "; so lien ket sua: ", L.so_lien_ket_sua - sua0)
        in_trang_thai(L)
    end
    d = duyet_hai_chieu(L)
    actual = (d.xuoi, d.nguoc, L.n)
    println("\nActual : xuoi=", fmt(actual[1]), "; nguoc=", fmt(actual[2]), "; n=", actual[3])
    ok = actual == (ky_vong[1], ky_vong[2], ky_vong[3]) && kiem_tra_lien_ket(L).hop_le
    println("KET LUAN: ", ok ? "KHOP KY VONG" : "KHONG KHOP KY VONG")
    ok || exit(1)
    return L
end

function minh_hoa_du_lieu_sai()
    println(DE)
    println("Ca LOI01: input vi pham mien gia tri cua phieu (-1000..1000)")
    day = [10, 1001, 30]
    lenh = [(:xoa, 10)]
    println("Input  : day=", fmt(day), "; lenh=xoa(10)")
    println("Expected: validator tu choi, bao day[2] = 1001 ngoai mien; khong tao danh sach.")
    da_bat = false
    try
        giai_bai(day, lenh)
    catch e
        e isa ArgumentError || rethrow()
        println("DA TU CHOI: ", e.msg)
        da_bat = occursin("day[2]", e.msg) && occursin("1001", e.msg)
    end
    println("\nInput bo sung: lenh go tu ban phim \"chen 5\" (ten lenh khong co trong phieu)")
    try
        phan_tich_lenh("chen 5")
    catch e
        e isa ArgumentError || rethrow()
        println("DA TU CHOI: ", e.msg)
        da_bat &= occursin("khong hop le", e.msg)
    end
    println("KET LUAN: ", da_bat ? "KHOP KY VONG (loi du kien da duoc bat, chuong trinh khong dung bat thuong)" :
                                    "KHONG KHOP KY VONG")
    da_bat || exit(1)
end

function minh_hoa_lien_ket_hong()
    println(DE)
    println("Ca KT13: kiem_tra_lien_ket phat hien vi tri lien ket khong khop (yeu cau tuy chon)")
    L = tao_danh_sach([1, 2, 3, 4])
    println("Truoc khi pha: ", kiem_tra_lien_ket(L))
    nut3 = L.dau.ke.ke
    nut3.truoc = L.dau          # co y lam sai: truoc cua nut 3 tro ve nut 1 thay vi nut 2
    println("Co y gan nut3.truoc = nut1 (dung phai la nut2).")
    println("Expected: hop_le=false, vi_tri=2 (nut 2 co ke.truoc khong tro lai chinh no).")
    kt = kiem_tra_lien_ket(L)
    println("Actual  : ", kt)
    ok = !kt.hop_le && kt.vi_tri == 2
    println("KET LUAN: ", ok ? "KHOP KY VONG" : "KHONG KHOP KY VONG")
    ok || exit(1)
end

"""Khảo sát ba quy mô n=5,20,100: đếm nút xét khi tìm và liên kết sửa khi tách."""
function khao_sat()
    println(DE)
    println("KHAO SAT CHI PHI: day = [1,2,...,n]; dem so nut xet (tim) va so lien ket sua (tach)")
    println(rpad("n", 5), "| ", rpad("x can xoa", 22), "| nut xet | lien ket sua | n sau | hop le")
    for n in (5, 20, 100)
        for (nhan, x) in (("dau (x=1)", 1), ("giua (x=$(cld(n, 2)))", cld(n, 2)),
                          ("cuoi (x=$n)", n), ("khong co (x=0)", 0))
            L = tao_danh_sach(collect(1:n))
            kq = xoa_theo_gia_tri!(L, x)
            println(rpad(string(n), 5), "| ", rpad(nhan, 22), "| ", lpad(kq.nut_xet, 7), " | ",
                    lpad(kq.lien_ket_sua, 12), " | ", lpad(L.n, 5), " | ",
                    kiem_tra_lien_ket(L).hop_le ? "co" : "KHONG")
        end
        L = tao_danh_sach(Int[])
        for x in 1:n
            them_kep!(L, x, isodd(x) ? :dau : :cuoi)
        end
        println(rpad(string(n), 5), "| ", rpad("tao n nut xen ke 2 dau", 22), "| ", lpad(0, 7), " | ",
                lpad(L.so_lien_ket_sua, 12), " | ", lpad(L.n, 5), " | ",
                kiem_tra_lien_ket(L).hop_le ? "co" : "KHONG", "   (= 2 + 3(n-1) = $(2 + 3 * (n - 1)))")
        println("-"^78)
    end
    println("Bo nho: moi nut giu 1 gia tri + 2 lien ket (truoc, ke); DSLK don chi giu 1 lien ket.")
end

function nhap_ban_phim()
    println(DE, " - NHAP TU BAN PHIM")
    println("Nhap day ban dau (cac so nguyen cach nhau boi dau cach, Enter neu rong):")
    dong = strip(readline())
    day = Int[]
    for t in split(dong)
        x = tryparse(Int, t)
        x === nothing && throw(ArgumentError("\"$t\" khong phai so nguyen"))
        push!(day, x)
    end
    println("Nhap so lenh k:")
    k = tryparse(Int, strip(readline()))
    (k === nothing || k < 0) && throw(ArgumentError("k phai la so nguyen khong am"))
    lenh = Tuple{Symbol,Int}[]
    for i in 1:k
        println("Lenh $i (them_dau x | them_cuoi x | xoa x):")
        push!(lenh, phan_tich_lenh(readline()))
    end
    kq = giai_bai(day, lenh)   # kiểm input trước khi chạy
    println("\nBuoc 0: xuoi=", fmt(day))
    for (i, b) in enumerate(kq.buoc)
        println("Buoc $i - ", b.lenh, " -> ", b.trang_thai, "; xuoi=", fmt(b.xuoi),
                "; nguoc=", fmt(b.nguoc), "; n=", b.n, "; nut xet=", b.nut_xet,
                "; lien ket sua=", b.lien_ket_sua, "; lien ket ", b.hop_le ? "hop le" : "LOI")
    end
    println("\nKET QUA: xuoi=", fmt(kq.xuoi), "; nguoc=", fmt(kq.nguoc), "; n=", kq.n)
    println(so_do(kq.L))
end

const CAC_CA = Dict(
    1  => () -> chay_ca("VD01", "Vi du 1 cua phieu - xoa nut giua",
                        [10, 20, 30], [(:xoa, 20)], ([10, 30], [30, 10], 2)),
    2  => () -> chay_ca("VD02", "Vi du 2 cua phieu - them roi xoa nut duy nhat",
                        Int[], [(:them_cuoi, 5), (:xoa, 5)], (Int[], Int[], 0)),
    3  => () -> chay_ca("TK01", "Tu thiet ke 1 - them xen ke hai dau, xoa gia tri khong co",
                        Int[], [(:them_dau, 3), (:them_dau, 2), (:them_cuoi, 4), (:them_dau, 1), (:xoa, 9)],
                        ([1, 2, 3, 4], [4, 3, 2, 1], 4)),
    4  => () -> chay_ca("TK02", "Tu thiet ke 2 - gia tri bien -1000/1000, trung lap, xoa lien tiep",
                        [5, -1000, 1000, 5], [(:xoa, 5), (:xoa, 5), (:them_dau, 0), (:xoa, 1000)],
                        ([0, -1000], [-1000, 0], 2)),
    5  => () -> chay_ca("BIEN01", "Ca phieu 2 - [6]; xoa(6): dau = cuoi = nothing",
                        [6], [(:xoa, 6)], (Int[], Int[], 0)),
    6  => () -> chay_ca("BIEN02", "Ca phieu 3 - [1,2,3]; xoa(1): xoa nut dau",
                        [1, 2, 3], [(:xoa, 1)], ([2, 3], [3, 2], 2)),
    7  => () -> chay_ca("BIEN03", "Ca phieu 4 - [1,2,3]; xoa(3): xoa nut cuoi",
                        [1, 2, 3], [(:xoa, 3)], ([1, 2], [2, 1], 2)),
    8  => minh_hoa_du_lieu_sai,
    9  => () -> chay_ca("KT09", "Ca phieu 1 - danh sach rong: hai day rong",
                        Int[], Tuple{Symbol,Int}[], (Int[], Int[], 0)),
    10 => () -> chay_ca("KT10", "Ca phieu 5 - [2,2,4]; xoa(2): chi xoa so 2 dau tien",
                        [2, 2, 4], [(:xoa, 2)], ([2, 4], [4, 2], 2)),
    11 => minh_hoa_lien_ket_hong,
)

if "--nhap" in ARGS
    nhap_ban_phim()
elseif "--khao-sat" in ARGS
    khao_sat()
elseif any(startswith("--ca="), ARGS)
    so = tryparse(Int, replace(only(filter(startswith("--ca="), ARGS)), "--ca=" => ""))
    haskey(CAC_CA, something(so, 0)) || throw(ArgumentError("chon --ca=1 den --ca=11"))
    CAC_CA[so]()
else
    # Hai ví dụ đúng như phiếu DT063. Có thể sửa trực tiếp dữ liệu trong CAC_CA.
    CAC_CA[1]()
    println("\n", "="^70, "\n")
    CAC_CA[2]()
end
