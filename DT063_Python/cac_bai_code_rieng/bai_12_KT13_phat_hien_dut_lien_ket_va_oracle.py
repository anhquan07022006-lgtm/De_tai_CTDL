# -*- coding: utf-8 -*-
"""
ĐỀ TÀI DT063 - DANH SÁCH LIÊN KẾT KÉP VÀ DUYỆT THEO HAI CHIỀU
Sinh viên: Bùi Anh Quân | MSSV: N24DCDT075 | Lớp: D24CQDT01-N

BÀI 12 (Ca thử mẫu 12 - KT13 & KT14): Phát hiện đứt liên kết hai chiều & Đối chiếu 300 dãy ngẫu nhiên (Oracle)
- Yêu cầu tùy chọn: kiem_tra_lien_ket báo chính xác vị trí đầu tiên có liên kết ke/truoc không khớp
- Kiểm thử đối chiếu (Differential Testing): 300 dãy lệnh ngẫu nhiên đối chiếu với list chuẩn của Python
"""

from pathlib import Path
import random
import sys

if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.danh_sach_kep import giai_bai, kiem_tra_lien_ket, tao_danh_sach


def main() -> None:
    print("=" * 74)
    print("BAI 12 (KT13 & KT14): PHAT HIEN DUT LIEN KET & DOI CHIEU 300 DAY NGAU NHIEN")
    print("Sinh vien: Bui Anh Quan - N24DCDT075 - DT063")
    print("=" * 74)

    # 1. KT13: Phát hiện đứt liên kết
    L = tao_danh_sach([10, 20, 30])
    truoc_pha = kiem_tra_lien_ket(L)
    print(f"[KT13] Truoc khi pha: {truoc_pha}")
    assert truoc_pha["hop_le"] is True

    # Cố ý gán sai nut3.truoc = nut1 (đúng phải là nut2)
    assert L.cuoi is not None and L.dau is not None
    L.cuoi.truoc = L.dau
    sau_pha = kiem_tra_lien_ket(L)
    print(f"[KT13] Sau khi gan sai nut3.truoc = nut1: {sau_pha}")
    assert sau_pha["hop_le"] is False and sau_pha["vi_tri"] == 2

    # 2. KT14: Đối chiếu 300 dãy lệnh ngẫu nhiên với Python list (seed=2026)
    rng = random.Random(2026)
    ten_lenh = ["them_dau", "them_cuoi", "xoa"]
    so_phep_kiem = 0
    for _ in range(300):
        m = rng.randint(0, 15)
        day = [rng.randint(-5, 5) for _ in range(m)]
        k = rng.randint(1, 25)
        lenh = [(rng.choice(ten_lenh), rng.randint(-5, 5)) for _ in range(k)]

        mau = list(day)
        for t, x in lenh:
            if t == "them_dau":
                mau.insert(0, x)
            elif t == "them_cuoi":
                mau.append(x)
            else:
                if x in mau:
                    mau.remove(x)

        kq = giai_bai(day, lenh)
        assert kq.xuoi == mau
        assert kq.nguoc == list(reversed(mau))
        assert kq.n == len(mau)
        assert kq.L.kiem_tra_lien_ket()["hop_le"] is True
        so_phep_kiem += 4

    print(f"[KT14] Doi chieu 300 day ngau nhien voi Python list: {so_phep_kiem}/{so_phep_kiem} phep kiem KHOP 100%")
    print("-" * 74)
    print(">>> [BAI 12 - KT13 & KT14] KIEM TRA ASSERT: DAT 100% (PASS)")


if __name__ == "__main__":
    main()
