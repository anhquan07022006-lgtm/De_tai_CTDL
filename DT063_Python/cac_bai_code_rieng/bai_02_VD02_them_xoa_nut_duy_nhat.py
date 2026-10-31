# -*- coding: utf-8 -*-
"""
ĐỀ TÀI DT063 - DANH SÁCH LIÊN KẾT KÉP VÀ DUYỆT THEO HAI CHIỀU
Sinh viên: Bùi Anh Quân | MSSV: N24DCDT075 | Lớp: D24CQDT01-N

BÀI 02 (Ca thử mẫu 2 - VD02): Ví dụ 2 của phiếu giao đề — Thêm vào rỗng rồi xóa nút duy nhất
- Đầu vào: dãy ban đầu = [], lệnh = them_cuoi(5); xoa(5)
- Kỳ vọng (Expected): xuoi = [], nguoc = [], n = 0, dau = None, cuoi = None
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
        ma="VD02",
        ten="Ví dụ 2 của phiếu - thêm rồi xóa nút duy nhất",
        day_str="",
        lenh_str=["them_cuoi 5", "xoa 5"],
        ky_vong={"xuoi": [], "nguoc": [], "n": 0},
    )

    kq = giai_bai([], [("them_cuoi", 5), ("xoa", 5)])
    assert kq.xuoi == []
    assert kq.nguoc == []
    assert kq.n == 0
    assert kq.L.dau is None and kq.L.cuoi is None
    assert kq.L.kiem_tra_lien_ket()["hop_le"] is True
    print(">>> [BAI 02 - VD02] KIEM TRA ASSERT: DAT 100% (PASS)")


if __name__ == "__main__":
    main()
