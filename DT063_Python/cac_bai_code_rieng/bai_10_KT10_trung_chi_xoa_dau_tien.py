# -*- coding: utf-8 -*-
"""
ĐỀ TÀI DT063 - DANH SÁCH LIÊN KẾT KÉP VÀ DUYỆT THEO HAI CHIỀU
Sinh viên: Bùi Anh Quân | MSSV: N24DCDT075 | Lớp: D24CQDT01-N

BÀI 10 (Ca thử mẫu 10 - KT10): Ca bắt buộc số 5 trong phiếu — Giá trị trùng chỉ xóa lần xuất hiện đầu tiên
- Đầu vào: dãy ban đầu = [2, 2, 4], lệnh = xoa(2)
- Kỳ vọng (Expected): xuoi = [2, 4], nguoc = [4, 2], n = 2, nut_xet = 1, lien_ket_sua = 2
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
        ma="KT10",
        ten="Ca phiếu 5 - [2,2,4]; xoa(2): chỉ xóa số 2 đầu tiên",
        day_str="2 2 4",
        lenh_str=["xoa 2"],
        ky_vong={"xuoi": [2, 4], "nguoc": [4, 2], "n": 2},
    )

    kq = giai_bai([2, 2, 4], [("xoa", 2)])
    assert kq.xuoi == [2, 4]
    assert kq.nguoc == [4, 2]
    assert kq.n == 2
    assert kq.buoc[-1]["nut_xet"] == 1
    assert kq.buoc[-1]["lien_ket_sua"] == 2
    assert kq.L.kiem_tra_lien_ket()["hop_le"] is True
    print(">>> [BAI 10 - KT10] KIEM TRA ASSERT: DAT 100% (PASS)")


if __name__ == "__main__":
    main()
