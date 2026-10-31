# -*- coding: utf-8 -*-
"""
ĐỀ TÀI DT063 - DANH SÁCH LIÊN KẾT KÉP VÀ DUYỆT THEO HAI CHIỀU
Sinh viên: Bùi Anh Quân | MSSV: N24DCDT075 | Lớp: D24CQDT01-N

BÀI 08 (Ca thử mẫu 8 - LOI01): Kiểm tra bộ lọc dữ liệu đầu vào (Validator)
- Từ chối giá trị ngoài miền -1000..1000 (1001, -1001), sai kiểu dữ liệu (1.5, True), và lệnh lạ ("chen 5")
"""

from pathlib import Path
import sys

if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.danh_sach_kep import LoiDauVao, giai_bai, phan_tich_day, phan_tich_lenh


def main() -> None:
    print("=" * 70)
    print("BAI 08 (LOI01): KIEM TRA BO LOC DU LIEU DAU VAO (VALIDATOR)")
    print("Sinh vien: Bui Anh Quan - N24DCDT075 - DT063")
    print("=" * 70)

    cac_truong_hop_loi = [
        ("Gia tri 1001 vuot mien tren", lambda: giai_bai([10, 1001, 30], [("xoa", 10)])),
        ("Gia tri -1001 vuot mien duoi", lambda: giai_bai([-1001], [])),
        ("Lenh co gia tri 2000 vuot mien", lambda: giai_bai([1], [("them_dau", 2000)])),
        ("Ten lenh khong hop le ('chen')", lambda: giai_bai([1], [("chen", 5)])),
        ("Phan tu khong phai so nguyen (1.5)", lambda: giai_bai([1.5], [])),  # type: ignore[list-item]
        ("Phan tu kieu bool (True)", lambda: giai_bai([True], [])),  # type: ignore[list-item]
        ("Chuoi nhap chua chu cai ('10 abc 20')", lambda: phan_tich_day("10 abc 20")),
        ("Lenh go tu ban phim sai ('chen 5')", lambda: phan_tich_lenh("chen 5")),
    ]

    so_ca_bat_duoc = 0
    for stt, (mo_ta, ham_chay) in enumerate(cac_truong_hop_loi, start=1):
        try:
            ham_chay()
            raise AssertionError(f"Khong bat duoc loi cho truong hop: {mo_ta}")
        except LoiDauVao as e:
            so_ca_bat_duoc += 1
            print(f"  [{stt}] {mo_ta:<38} -> DA TU CHOI DUNG: {e}")

    assert so_ca_bat_duoc == len(cac_truong_hop_loi)
    print("-" * 70)
    print(f"KET LUAN: KHOP KY VONG (Da chan thanh cong {so_ca_bat_duoc}/{len(cac_truong_hop_loi)} input sai)")
    print(">>> [BAI 08 - LOI01] KIEM TRA ASSERT: DAT 100% (PASS)")


if __name__ == "__main__":
    main()
