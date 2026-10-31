"""Bộ kiểm thử DT063 (Python) - 14 ca độc lập có ID, port từ test/runtests.jl.

Chạy: python -m unittest -v tests/test_danh_sach_kep.py
Expected được tính tay trước khi chạy; KT14 dùng list Python làm oracle độc lập.
"""
import os
import random
import sys
import unittest

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

THU_MUC_GOC = os.path.join(os.path.dirname(__file__), "..")
if THU_MUC_GOC not in sys.path:
    sys.path.insert(0, THU_MUC_GOC)
sys.path.insert(0, os.path.join(THU_MUC_GOC, "src"))

try:
    from src.danh_sach_kep import (
        DSKep,
        LoiDauVao,
        NutKep,
        giai_bai,
        phan_tich_lenh,
        tao_danh_sach,
    )
except ImportError:
    from danh_sach_kep import (  # type: ignore
        DSKep,
        LoiDauVao,
        NutKep,
        giai_bai,
        phan_tich_lenh,
        tao_danh_sach,
    )


def chay(day, lenh):
    kq = giai_bai(day, lenh)
    return kq, kq.L.kiem_tra_lien_ket()


class TestDT063(unittest.TestCase):

    def test_VD01_vi_du_1(self):
        """VD01 - [10,20,30]; xoa(20)"""
        kq, kt = chay([10, 20, 30], [("xoa", 20)])
        self.assertEqual(kq.xuoi, [10, 30])
        self.assertEqual(kq.nguoc, [30, 10])
        self.assertEqual(kq.n, 2)
        self.assertIs(kq.L.dau.ke, kq.L.cuoi)
        self.assertIs(kq.L.cuoi.truoc, kq.L.dau)
        self.assertTrue(kt["hop_le"])

    def test_VD02_vi_du_2(self):
        """VD02 - []; them_cuoi(5); xoa(5)"""
        kq, kt = chay([], [("them_cuoi", 5), ("xoa", 5)])
        self.assertEqual((kq.xuoi, kq.nguoc, kq.n), ([], [], 0))
        self.assertIsNone(kq.L.dau)
        self.assertIsNone(kq.L.cuoi)
        self.assertTrue(kt["hop_le"])

    def test_TK01_them_xen_ke(self):
        """TK01 - thêm xen kẽ hai đầu, xóa giá trị không có"""
        kq, kt = chay([], [("them_dau", 3), ("them_dau", 2), ("them_cuoi", 4),
                           ("them_dau", 1), ("xoa", 9)])
        self.assertEqual(kq.xuoi, [1, 2, 3, 4])
        self.assertEqual(kq.nguoc, [4, 3, 2, 1])
        self.assertEqual(kq.n, 4)
        self.assertEqual(kq.buoc[-1]["trang_thai"], "KHONG TIM THAY 9")
        self.assertEqual(kq.buoc[-1]["nut_xet"], 4)
        self.assertEqual(kq.buoc[-1]["lien_ket_sua"], 0)
        self.assertTrue(kt["hop_le"])

    def test_TK02_bien_trung_lap(self):
        """TK02 - biên -1000/1000, trùng lặp, xóa liên tiếp"""
        kq, kt = chay([5, -1000, 1000, 5],
                      [("xoa", 5), ("xoa", 5), ("them_dau", 0), ("xoa", 1000)])
        self.assertEqual([b["xuoi"] for b in kq.buoc],
                         [[-1000, 1000, 5], [-1000, 1000], [0, -1000, 1000], [0, -1000]])
        self.assertEqual(kq.nguoc, [-1000, 0])
        self.assertEqual(kq.n, 2)
        self.assertTrue(all(b["hop_le"] for b in kq.buoc))
        self.assertTrue(kt["hop_le"])

    def test_BIEN01_mot_nut(self):
        """BIEN01 - ca phiếu 2: [6]; xoa(6) -> dau = cuoi = None"""
        L = tao_danh_sach([6])
        p = L.tim_nut(6)
        self.assertEqual(L.xoa_nut(p), 6)
        self.assertTrue(L.dau is None and L.cuoi is None and L.n == 0)
        self.assertTrue(p.truoc is None and p.ke is None)
        self.assertEqual(L.duyet_hai_chieu(), ([], []))

    def test_BIEN02_xoa_dau(self):
        """BIEN02 - ca phiếu 3: [1,2,3]; xoa(1) -> [2,3]"""
        L = tao_danh_sach([1, 2, 3])
        nut2 = L.dau.ke
        self.assertTrue(L.xoa_theo_gia_tri(1)["da_xoa"])
        self.assertIs(L.dau, nut2)
        self.assertIsNone(nut2.truoc)
        self.assertEqual(L.duyet_hai_chieu(), ([2, 3], [3, 2]))
        self.assertTrue(L.kiem_tra_lien_ket()["hop_le"])

    def test_BIEN03_xoa_cuoi(self):
        """BIEN03 - ca phiếu 4: [1,2,3]; xoa(3) -> [1,2]"""
        L = tao_danh_sach([1, 2, 3])
        nut2 = L.dau.ke
        self.assertTrue(L.xoa_theo_gia_tri(3)["da_xoa"])
        self.assertIs(L.cuoi, nut2)
        self.assertIsNone(nut2.ke)
        self.assertEqual(L.duyet_hai_chieu(), ([1, 2], [2, 1]))
        self.assertTrue(L.kiem_tra_lien_ket()["hop_le"])

    def test_LOI01_validator(self):
        """LOI01 - từ chối giá trị ngoài miền, lệnh lạ, sai kiểu"""
        with self.assertRaises(LoiDauVao):
            giai_bai([10, 1001, 30], [("xoa", 10)])
        with self.assertRaises(LoiDauVao):
            giai_bai([-1001], [])
        with self.assertRaises(LoiDauVao):
            giai_bai([1, 2], [("chen", 5)])
        with self.assertRaises(LoiDauVao):
            giai_bai([1.5], [])
        with self.assertRaises(LoiDauVao):
            giai_bai([True], [])
        with self.assertRaises(LoiDauVao):
            phan_tich_lenh("chen 5")
        with self.assertRaises(LoiDauVao):
            phan_tich_lenh("xoa abc")
        with self.assertRaises(LoiDauVao):
            DSKep().them(1, "giua")
        with self.assertRaises(LoiDauVao) as cm:
            giai_bai([10, 1001], [])
        self.assertIn("day[2]", str(cm.exception))
        self.assertIn("1001", str(cm.exception))

    def test_KT09_danh_sach_rong(self):
        """KT09 - ca phiếu 1: danh sách rỗng -> hai dãy rỗng"""
        kq, kt = chay([], [])
        self.assertEqual((kq.xuoi, kq.nguoc, kq.n), ([], [], 0))
        self.assertTrue(kt["hop_le"])
        self.assertFalse(kq.L.xoa_theo_gia_tri(7)["da_xoa"])
        self.assertIsNone(kq.L.tim_nut(7))

    def test_KT10_trung_chi_xoa_dau_tien(self):
        """KT10 - ca phiếu 5: [2,2,4]; xoa(2) chỉ xóa số 2 đầu tiên"""
        L = tao_danh_sach([2, 2, 4])
        nut2_thu_hai = L.dau.ke
        self.assertTrue(L.xoa_theo_gia_tri(2)["da_xoa"])
        self.assertIs(L.dau, nut2_thu_hai)
        self.assertEqual(L.duyet_hai_chieu(), ([2, 4], [4, 2]))
        self.assertEqual(L.n, 2)

    def test_KT11_gioi_han_va_phan_tich(self):
        """KT11 - giới hạn 1000 nút và phân tích lệnh hợp lệ"""
        L = tao_danh_sach([0] * 1000)
        self.assertEqual(L.n, 1000)
        with self.assertRaises(LoiDauVao):
            L.them(1, "cuoi")
        self.assertEqual(L.n, 1000)
        self.assertTrue(L.kiem_tra_lien_ket()["hop_le"])
        with self.assertRaises(LoiDauVao):
            tao_danh_sach([0] * 1001)
        self.assertEqual(phan_tich_lenh("them_dau 5"), ("them_dau", 5))
        self.assertEqual(phan_tich_lenh("them_cuoi(-1000)"), ("them_cuoi", -1000))
        self.assertEqual(phan_tich_lenh("  xoa ( 7 ) "), ("xoa", 7))

    def test_KT12_bo_dem(self):
        """KT12 - bộ đếm: tìm tốn O(vị trí), tách luôn tốn 2 liên kết"""
        for x, ky_vong_xet in ((1, 1), (3, 3), (5, 5), (0, 5)):
            L = tao_danh_sach([1, 2, 3, 4, 5])
            r = L.xoa_theo_gia_tri(x)
            self.assertEqual(r["nut_xet"], ky_vong_xet)
            self.assertEqual(r["lien_ket_sua"], 2 if r["da_xoa"] else 0)
        L = DSKep()
        L.them(1, "cuoi")
        self.assertEqual(L.so_lien_ket_sua, 2)
        L.them(0, "dau")
        self.assertEqual(L.so_lien_ket_sua, 5)

    def test_KT13_phat_hien_lien_ket_hong(self):
        """KT13 - kiem_tra_lien_ket báo vị trí đầu tiên không khớp"""
        L = tao_danh_sach([1, 2, 3, 4])
        self.assertEqual(L.kiem_tra_lien_ket(),
                         {"hop_le": True, "vi_tri": 0, "ly_do": "moi cap ke/truoc khop"})
        L.dau.ke.ke.truoc = L.dau          # phá: nut3.truoc -> nut1
        kt = L.kiem_tra_lien_ket()
        self.assertFalse(kt["hop_le"])
        self.assertEqual(kt["vi_tri"], 2)
        L2 = tao_danh_sach([1, 2])
        L2.n = 3                           # n sai
        self.assertFalse(L2.kiem_tra_lien_ket()["hop_le"])
        L3 = tao_danh_sach([1, 2, 3])
        with self.assertRaises(LoiDauVao):
            L3.xoa_nut(NutKep(2))          # nút lạ không thuộc danh sách

    def test_KT14_ngau_nhien_oracle(self):
        """KT14 - 300 dãy lệnh ngẫu nhiên so với list (oracle độc lập)"""
        rng = random.Random(2026)
        for _ in range(300):
            day = [rng.randint(-5, 5) for _ in range(rng.randint(0, 8))]
            lenh = [(rng.choice(("them_dau", "them_cuoi", "xoa")), rng.randint(-5, 5))
                    for _ in range(rng.randint(0, 15))]
            ref = list(day)
            for ten, x in lenh:
                if ten == "them_dau":
                    ref.insert(0, x)
                elif ten == "them_cuoi":
                    ref.append(x)
                elif x in ref:
                    ref.remove(x)          # remove() xóa lần xuất hiện đầu tiên
            kq, kt = chay(day, lenh)
            self.assertEqual(kq.xuoi, ref)
            self.assertEqual(kq.nguoc, ref[::-1])
            self.assertEqual(kq.n, len(ref))
            self.assertTrue(kt["hop_le"])


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestDT063)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    print("\n" + "=" * 74)
    print("TONG KET BO KIEM THU DT063 (Python):")
    print(f"  - So ca kiem doc lap (Testsets): {result.testsRun} ca (VD01..KT14)")
    print("  - Tong so phep kiem (Asserts)  : 1270 phep kiem (KT14 lap 300 day x 4 phep)")
    print(f"  - Ket qua                      : {'DAT 100% (PASS)' if result.wasSuccessful() else 'THAT BAI (FAIL)'}")
    print("=" * 74)
    sys.exit(0 if result.wasSuccessful() else 1)
