# -*- coding: utf-8 -*-
"""
ĐỀ TÀI DT063 - DANH SÁCH LIÊN KẾT KÉP VÀ DUYỆT THEO HAI CHIỀU
Sinh viên: Bùi Anh Quân | MSSV: N24DCDT075 | Lớp: D24CQDT01-N

BÀI 01 (Ca thử mẫu 1 - VD01): Ví dụ 1 của phiếu giao đề — Xóa nút ở giữa danh sách
- Đầu vào: dãy ban đầu = [10, 20, 30], lệnh = xoa(20)
- Kỳ vọng (Expected): xuoi = [10, 30], nguoc = [30, 10], n = 2
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
        ma="VD01",
        ten="Ví dụ 1 của phiếu - xóa nút giữa",
        day_str="10 20 30",
        lenh_str=["xoa 20"],
        ky_vong={"xuoi": [10, 30], "nguoc": [30, 10], "n": 2},
    )

    kq = giai_bai([10, 20, 30], [("xoa", 20)])
    assert kq.xuoi == [10, 30]
    assert kq.nguoc == [30, 10]
    assert kq.n == 2
    assert kq.L.kiem_tra_lien_ket()["hop_le"] is True
    print(">>> [BAI 01 - VD01] KIEM TRA ASSERT: DAT 100% (PASS)")


if __name__ == "__main__":
    main()
