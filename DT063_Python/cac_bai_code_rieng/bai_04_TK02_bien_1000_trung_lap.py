# -*- coding: utf-8 -*-
"""
ĐỀ TÀI DT063 - DANH SÁCH LIÊN KẾT KÉP VÀ DUYỆT THEO HAI CHIỀU
Sinh viên: Bùi Anh Quân | MSSV: N24DCDT075 | Lớp: D24CQDT01-N

BÀI 04 (Ca thử mẫu 4 - TK02): Tự thiết kế 2 — Giá trị biên -1000/1000, trùng lặp, xóa liên tiếp
- Đầu vào: dãy ban đầu = [5, -1000, 1000, 5], lệnh = xoa(5); xoa(5); them_dau(0); xoa(1000)
- Kỳ vọng (Expected): xuoi = [0, -1000], nguoc = [-1000, 0], n = 2
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
        ma="TK02",
        ten="Tự thiết kế 2 - biên ±1000, trùng lặp, xóa liên tiếp",
        day_str="5 -1000 1000 5",
        lenh_str=["xoa 5", "xoa 5", "them_dau 0", "xoa 1000"],
        ky_vong={"xuoi": [0, -1000], "nguoc": [-1000, 0], "n": 2},
    )

    kq = giai_bai([5, -1000, 1000, 5], [("xoa", 5), ("xoa", 5), ("them_dau", 0), ("xoa", 1000)])
    assert kq.xuoi == [0, -1000]
    assert kq.nguoc == [-1000, 0]
    assert kq.n == 2
    assert kq.L.kiem_tra_lien_ket()["hop_le"] is True
    print(">>> [BAI 04 - TK02] KIEM TRA ASSERT: DAT 100% (PASS)")


if __name__ == "__main__":
    main()
