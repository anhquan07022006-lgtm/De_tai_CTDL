# -*- coding: utf-8 -*-
"""
ĐỀ TÀI DT063 - DANH SÁCH LIÊN KẾT KÉP VÀ DUYỆT THEO HAI CHIỀU
Sinh viên: Bùi Anh Quân | MSSV: N24DCDT075 | Lớp: D24CQDT01-N

BÀI 06 (Ca thử mẫu 6 - BIEN02): Ca bắt buộc số 3 trong phiếu — Xóa nút đầu danh sách
- Đầu vào: dãy ban đầu = [1, 2, 3], lệnh = xoa(1)
- Kỳ vọng (Expected): xuoi = [2, 3], nguoc = [3, 2], n = 2, dau = 2, dau.truoc = None
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
        ma="BIEN02",
        ten="Ca phiếu 3 - [1,2,3]; xoa(1): xóa nút đầu",
        day_str="1 2 3",
        lenh_str=["xoa 1"],
        ky_vong={"xuoi": [2, 3], "nguoc": [3, 2], "n": 2},
    )

    kq = giai_bai([1, 2, 3], [("xoa", 1)])
    assert kq.xuoi == [2, 3]
    assert kq.nguoc == [3, 2]
    assert kq.n == 2
    assert kq.L.dau is not None and kq.L.dau.gia_tri == 2 and kq.L.dau.truoc is None
    assert kq.L.kiem_tra_lien_ket()["hop_le"] is True
    print(">>> [BAI 06 - BIEN02] KIEM TRA ASSERT: DAT 100% (PASS)")


if __name__ == "__main__":
    main()
