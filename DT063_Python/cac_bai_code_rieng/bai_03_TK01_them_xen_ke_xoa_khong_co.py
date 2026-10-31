# -*- coding: utf-8 -*-
"""
ĐỀ TÀI DT063 - DANH SÁCH LIÊN KẾT KÉP VÀ DUYỆT THEO HAI CHIỀU
Sinh viên: Bùi Anh Quân | MSSV: N24DCDT075 | Lớp: D24CQDT01-N

BÀI 03 (Ca thử mẫu 3 - TK01): Tự thiết kế 1 — Thêm xen kẽ hai đầu, xóa giá trị không có
- Đầu vào: dãy ban đầu = [], lệnh = them_dau(3); them_dau(2); them_cuoi(4); them_dau(1); xoa(9)
- Kỳ vọng (Expected): xuoi = [1, 2, 3, 4], nguoc = [4, 3, 2, 1], n = 4
"""

from pathlib import Path
import sys

if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from demo import in_ket_qua
from src.danh_sach_kep import giai_bai


def main() -> None:
    in_ket_qua(
        ma="TK01",
        ten="Tự thiết kế 1 - thêm xen kẽ hai đầu, xóa giá trị không có",
        day_str="",
        lenh_str=["them_dau 3", "them_dau 2", "them_cuoi 4", "them_dau 1", "xoa 9"],
        ky_vong={"xuoi": [1, 2, 3, 4], "nguoc": [4, 3, 2, 1], "n": 4},
    )

    kq = giai_bai([], [("them_dau", 3), ("them_dau", 2), ("them_cuoi", 4), ("them_dau", 1), ("xoa", 9)])
    assert kq.xuoi == [1, 2, 3, 4]
    assert kq.nguoc == [4, 3, 2, 1]
    assert kq.n == 4
    assert kq.buoc[-1]["trang_thai"] == "KHONG TIM THAY 9"
    assert kq.buoc[-1]["nut_xet"] == 4
    assert kq.buoc[-1]["lien_ket_sua"] == 0
    assert kq.L.kiem_tra_lien_ket()["hop_le"] is True
    print(">>> [BAI 03 - TK01] KIEM TRA ASSERT: DAT 100% (PASS)")


if __name__ == "__main__":
    main()
