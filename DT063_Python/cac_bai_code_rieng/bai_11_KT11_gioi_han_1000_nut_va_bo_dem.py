# -*- coding: utf-8 -*-
"""
ĐỀ TÀI DT063 - DANH SÁCH LIÊN KẾT KÉP VÀ DUYỆT THEO HAI CHIỀU
Sinh viên: Bùi Anh Quân | MSSV: N24DCDT075 | Lớp: D24CQDT01-N

BÀI 11 (Ca thử mẫu 11 - KT11 & KT12): Giới hạn tối đa 1000 nút & Khảo sát bộ đếm chi phí n = 5, 20, 100
- Kiểm tra danh sách chứa đúng 1000 nút hợp lệ và từ chối khi thêm nút thứ 1001
- Kiểm tra số nút xét khi tìm O(n) và số liên kết sửa khi tách nút luôn bằng 2 O(1)
"""

from pathlib import Path
import sys

if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.danh_sach_kep import LoiDauVao, dat_lai_bo_dem, kiem_tra_lien_ket, tao_danh_sach, them_kep, xoa_theo_gia_tri


def main() -> None:
    print("=" * 74)
    print("BAI 11 (KT11 & KT12): GIOI HAN 1000 NUT VA KHAO SAT BO DEM CHI PHI")
    print("Sinh vien: Bui Anh Quan - N24DCDT075 - DT063")
    print("=" * 74)

    # 1. Kiểm tra giới hạn 1000 nút
    L1000 = tao_danh_sach(list(range(1, 1001)))
    assert L1000.n == 1000
    assert kiem_tra_lien_ket(L1000)["hop_le"] is True
    print(f"[1] Khoi tao danh sach 1000 nut: THANH CONG (n = {L1000.n}, hop_le = True)")

    bi_chan = False
    try:
        them_kep(L1000, 1, "cuoi")
    except LoiDauVao as e:
        bi_chan = True
        print(f"[2] Thu them nut thu 1001: DA TU CHOI DUNG -> {e}")
    assert bi_chan is True

    # 2. Khảo sát bộ đếm chi phí trên n = 5, 20, 100
    print("-" * 74)
    print(f"{'n':<5} | {'Vi tri xoa':<18} | {'Nut xet':>8} | {'Lien ket sua':>13} | {'Hop le'}")
    print("-" * 74)
    for n in (5, 20, 100):
        for ten, x, ky_vong_xet, ky_vong_sua in [
            (f"dau (x=1)", 1, 1, 2),
            (f"giua (x={n // 2})", n // 2, n // 2, 2),
            (f"cuoi (x={n})", n, n, 2),
            ("khong co (x=0)", 0, n, 0),
        ]:
            L = tao_danh_sach(list(range(1, n + 1)))
            dat_lai_bo_dem(L)
            xoa_theo_gia_tri(L, x)
            kt = kiem_tra_lien_ket(L)
            assert L.so_nut_xet == ky_vong_xet
            assert L.so_lien_ket_sua == ky_vong_sua
            assert kt["hop_le"] is True
            print(f"{n:<5} | {ten:<18} | {L.so_nut_xet:>8} | {L.so_lien_ket_sua:>13} | {kt['hop_le']}")

    print("-" * 74)
    print(">>> [BAI 11 - KT11 & KT12] KIEM TRA ASSERT: DAT 100% (PASS)")


if __name__ == "__main__":
    main()
