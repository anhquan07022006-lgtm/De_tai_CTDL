# -*- coding: utf-8 -*-
"""
ĐỀ TÀI DT063 - DANH SÁCH LIÊN KẾT KÉP VÀ DUYỆT THEO HAI CHIỀU
Sinh viên: Bùi Anh Quân | MSSV: N24DCDT075 | Lớp: D24CQDT01-N

BÀI 07 (Ca thử mẫu 7 - BIEN03): Ca bắt buộc số 4 trong phiếu — Xóa nút cuối danh sách
- Đầu vào: dãy ban đầu = [1, 2, 3], lệnh = xoa(3)
- Kỳ vọng (Expected): xuoi = [1, 2], nguoc = [2, 1], n = 2, cuoi = 2, cuoi.ke = None
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
        ma="BIEN03",
        ten="Ca phiếu 4 - [1,2,3]; xoa(3): xóa nút cuối",
        day_str="1 2 3",
        lenh_str=["xoa 3"],
        ky_vong={"xuoi": [1, 2], "nguoc": [2, 1], "n": 2},
    )

    kq = giai_bai([1, 2, 3], [("xoa", 3)])
    assert kq.xuoi == [1, 2]
    assert kq.nguoc == [2, 1]
    assert kq.n == 2
    assert kq.L.cuoi is not None and kq.L.cuoi.gia_tri == 2 and kq.L.cuoi.ke is None
    assert kq.L.kiem_tra_lien_ket()["hop_le"] is True
    print(">>> [BAI 07 - BIEN03] KIEM TRA ASSERT: DAT 100% (PASS)")


if __name__ == "__main__":
    main()
