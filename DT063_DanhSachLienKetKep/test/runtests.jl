using Test
using Random
include(joinpath(@__DIR__, "..", "src", "DanhSachKep.jl"))
using .DanhSachKep

# Mỗi @testset là MỘT ca độc lập có ID; một ca có thể chứa nhiều phép @test (assert).
# Expected được tính tay trước khi chạy; KT14 dùng Vector làm bộ giải độc lập (oracle).

"""Chạy giai_bai và trả (xuoi, nguoc, n) cùng kết quả kiểm liên kết."""
function chay(day, lenh)
    kq = giai_bai(day, lenh)
    return kq, kiem_tra_lien_ket(kq.L)
end

@testset verbose = true "DT063 - Danh sach lien ket kep" begin

    @testset "VD01 - vi du 1: [10,20,30]; xoa(20)" begin
        kq, kt = chay([10, 20, 30], [(:xoa, 20)])
        @test kq.xuoi == [10, 30]
        @test kq.nguoc == [30, 10]
        @test kq.n == 2
        @test kq.L.dau.ke === kq.L.cuoi          # 10.ke -> 30
        @test kq.L.cuoi.truoc === kq.L.dau       # 30.truoc -> 10
        @test kt.hop_le
    end

    @testset "VD02 - vi du 2: []; them_cuoi(5); xoa(5)" begin
        kq, kt = chay(Int[], [(:them_cuoi, 5), (:xoa, 5)])
        @test kq.xuoi == Int[] && kq.nguoc == Int[] && kq.n == 0
        @test kq.L.dau === nothing && kq.L.cuoi === nothing
        @test kt.hop_le
    end

    @testset "TK01 - them xen ke hai dau, xoa gia tri khong co" begin
        kq, kt = chay(Int[], [(:them_dau, 3), (:them_dau, 2), (:them_cuoi, 4), (:them_dau, 1), (:xoa, 9)])
        @test kq.xuoi == [1, 2, 3, 4]
        @test kq.nguoc == [4, 3, 2, 1]
        @test kq.n == 4
        @test kq.buoc[end].trang_thai == "KHONG TIM THAY 9"
        @test kq.buoc[end].nut_xet == 4            # đã xét hết 4 nút
        @test kq.buoc[end].lien_ket_sua == 0       # không tách gì
        @test kt.hop_le
    end

    @testset "TK02 - bien -1000/1000, trung lap, xoa lien tiep" begin
        kq, kt = chay([5, -1000, 1000, 5], [(:xoa, 5), (:xoa, 5), (:them_dau, 0), (:xoa, 1000)])
        @test [b.xuoi for b in kq.buoc] == [[-1000, 1000, 5], [-1000, 1000], [0, -1000, 1000], [0, -1000]]
        @test kq.nguoc == [-1000, 0]
        @test kq.n == 2
        @test all(b.hop_le for b in kq.buoc)
        @test kt.hop_le
    end

    @testset "BIEN01 - ca phieu 2: [6]; xoa(6) -> dau = cuoi = nothing" begin
        L = tao_danh_sach([6])
        p = tim_nut(L, 6)
        @test xoa_nut!(L, p) == 6
        @test L.dau === nothing && L.cuoi === nothing && L.n == 0
        @test p.truoc === nothing && p.ke === nothing   # không giữ con trỏ cũ
        @test duyet_hai_chieu(L) == (xuoi = Int[], nguoc = Int[])
    end

    @testset "BIEN02 - ca phieu 3: [1,2,3]; xoa(1) -> [2,3]" begin
        L = tao_danh_sach([1, 2, 3])
        nut2 = L.dau.ke
        @test xoa_theo_gia_tri!(L, 1).da_xoa
        @test L.dau === nut2 && nut2.truoc === nothing  # đầu mới, truoc rỗng
        @test duyet_hai_chieu(L) == (xuoi = [2, 3], nguoc = [3, 2])
        @test kiem_tra_lien_ket(L).hop_le
    end

    @testset "BIEN03 - ca phieu 4: [1,2,3]; xoa(3) -> [1,2]" begin
        L = tao_danh_sach([1, 2, 3])
        nut2 = L.dau.ke
        @test xoa_theo_gia_tri!(L, 3).da_xoa
        @test L.cuoi === nut2 && nut2.ke === nothing     # cuối mới, ke rỗng
        @test duyet_hai_chieu(L) == (xuoi = [1, 2], nguoc = [2, 1])
        @test kiem_tra_lien_ket(L).hop_le
    end

    @testset "LOI01 - validator tu choi gia tri ngoai mien, lenh la, du lieu sai kieu" begin
        @test_throws ArgumentError giai_bai([10, 1001, 30], [(:xoa, 10)])
        @test_throws ArgumentError giai_bai([-1001], Tuple{Symbol,Int}[])
        @test_throws ArgumentError giai_bai([1, 2], [(:chen, 5)])
        @test_throws ArgumentError giai_bai([1.5], Tuple{Symbol,Int}[])
        @test_throws ArgumentError phan_tich_lenh("chen 5")
        @test_throws ArgumentError phan_tich_lenh("xoa abc")
        @test_throws ArgumentError them_kep!(DSKep(), 1, :giua)
        msg = try giai_bai([10, 1001], Tuple{Symbol,Int}[]); "" catch e; e.msg end
        @test occursin("day[2]", msg) && occursin("1001", msg)
    end

    @testset "KT09 - ca phieu 1: danh sach rong -> hai day rong" begin
        kq, kt = chay(Int[], Tuple{Symbol,Int}[])
        @test kq.xuoi == Int[] && kq.nguoc == Int[] && kq.n == 0
        @test kt.hop_le
        @test !xoa_theo_gia_tri!(kq.L, 7).da_xoa         # xóa trên rỗng không lỗi
        @test tim_nut(kq.L, 7) === nothing
    end

    @testset "KT10 - ca phieu 5: [2,2,4]; xoa(2) chi xoa so 2 dau tien" begin
        L = tao_danh_sach([2, 2, 4])
        nut2_thu_hai = L.dau.ke
        @test xoa_theo_gia_tri!(L, 2).da_xoa
        @test L.dau === nut2_thu_hai                     # nút còn lại là số 2 thứ hai
        @test duyet_hai_chieu(L) == (xuoi = [2, 4], nguoc = [4, 2])
        @test L.n == 2
    end

    @testset "KT11 - gioi han 1000 nut va phan tich lenh hop le" begin
        L = tao_danh_sach(fill(0, 1000))
        @test L.n == 1000
        @test_throws ArgumentError them_kep!(L, 1, :cuoi)
        @test L.n == 1000 && kiem_tra_lien_ket(L).hop_le  # lỗi không làm hỏng danh sách
        @test_throws ArgumentError tao_danh_sach(fill(0, 1001))
        @test phan_tich_lenh("them_dau 5") == (:them_dau, 5)
        @test phan_tich_lenh("them_cuoi(-1000)") == (:them_cuoi, -1000)
        @test phan_tich_lenh("  xoa ( 7 ) ") == (:xoa, 7)
    end

    @testset "KT12 - bo dem: tim ton O(vi tri), tach luon ton 2 lien ket" begin
        for (x, ky_vong_xet) in ((1, 1), (3, 3), (5, 5), (0, 5))
            L = tao_danh_sach([1, 2, 3, 4, 5])
            kq = xoa_theo_gia_tri!(L, x)
            @test kq.nut_xet == ky_vong_xet
            @test kq.lien_ket_sua == (kq.da_xoa ? 2 : 0)
        end
        L = DSKep()
        them_kep!(L, 1, :cuoi)                            # rỗng: 2 (dau, cuoi)
        @test L.so_lien_ket_sua == 2
        them_kep!(L, 0, :dau)                             # không rỗng: 3
        @test L.so_lien_ket_sua == 5
    end

    @testset "KT13 - kiem_tra_lien_ket bao vi tri dau tien khong khop" begin
        L = tao_danh_sach([1, 2, 3, 4])
        @test kiem_tra_lien_ket(L) == (hop_le = true, vi_tri = 0, ly_do = "moi cap ke/truoc khop")
        L.dau.ke.ke.truoc = L.dau                         # phá: nut3.truoc -> nut1
        kt = kiem_tra_lien_ket(L)
        @test !kt.hop_le && kt.vi_tri == 2
        L2 = tao_danh_sach([1, 2])
        L2.n = 3                                          # n sai
        @test !kiem_tra_lien_ket(L2).hop_le
        L3 = tao_danh_sach([1, 2, 3])
        @test_throws ArgumentError xoa_nut!(L3, NutKep(2)) # nút lạ không thuộc danh sách
    end

    @testset "KT14 - 300 day lenh ngau nhien so voi Vector (oracle doc lap)" begin
        rng = MersenneTwister(2026)
        for lan in 1:300
            day = rand(rng, -5:5, rand(rng, 0:8))
            lenh = Tuple{Symbol,Int}[]
            for _ in 1:rand(rng, 0:15)
                push!(lenh, (rand(rng, (:them_dau, :them_cuoi, :xoa)), rand(rng, -5:5)))
            end
            # Oracle: Vector với pushfirst!/push!/findfirst/deleteat!
            ref = copy(day)
            for (ten, x) in lenh
                if ten === :them_dau
                    pushfirst!(ref, x)
                elseif ten === :them_cuoi
                    push!(ref, x)
                else
                    i = findfirst(==(x), ref)
                    i === nothing || deleteat!(ref, i)
                end
            end
            kq, kt = chay(day, lenh)
            @test kq.xuoi == ref
            @test kq.nguoc == reverse(ref)
            @test kq.n == length(ref)
            @test kt.hop_le
        end
    end
end
