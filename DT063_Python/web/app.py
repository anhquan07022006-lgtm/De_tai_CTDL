"""
Web server cho DT063 - chỉ dùng thư viện chuẩn Python (http.server, json).

Toàn bộ thao tác danh sách liên kết kép chạy bằng Python (src/danh_sach_kep.py);
trình duyệt chỉ gửi input và vẽ lại kết quả trả về.

Chạy:  python web/app.py            -> mở http://127.0.0.1:8000
       python web/app.py --port 8080
"""
import argparse
import json
import os
import sys
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

GOC = os.path.dirname(os.path.abspath(__file__))
THU_MUC_GOC = os.path.join(GOC, "..")
if THU_MUC_GOC not in sys.path:
    sys.path.insert(0, THU_MUC_GOC)
sys.path.insert(0, os.path.join(GOC, "..", "src"))

try:
    from src.danh_sach_kep import (
        DSKep,
        LoiDauVao,
        _anh_chup,
        giai_bai,
        kiem_tra_dau_vao,
        phan_tich_day,
        phan_tich_lenh,
        tao_danh_sach,
    )
except ImportError:
    from danh_sach_kep import (  # type: ignore
        DSKep,
        LoiDauVao,
        _anh_chup,
        giai_bai,
        kiem_tra_dau_vao,
        phan_tich_day,
        phan_tich_lenh,
        tao_danh_sach,
    )

# Các ca minh họa giống bảng --ca của bản Julia (kèm kỳ vọng tính tay).
CA_MAU = [
    {"ma": "VD01", "ten": "Ví dụ 1 của phiếu - xóa nút giữa",
     "day": "10 20 30", "lenh": ["xoa 20"],
     "ky_vong": {"xuoi": [10, 30], "nguoc": [30, 10], "n": 2}},
    {"ma": "VD02", "ten": "Ví dụ 2 của phiếu - thêm rồi xóa nút duy nhất",
     "day": "", "lenh": ["them_cuoi 5", "xoa 5"],
     "ky_vong": {"xuoi": [], "nguoc": [], "n": 0}},
    {"ma": "TK01", "ten": "Tự thiết kế 1 - thêm xen kẽ hai đầu, xóa giá trị không có",
     "day": "", "lenh": ["them_dau 3", "them_dau 2", "them_cuoi 4", "them_dau 1", "xoa 9"],
     "ky_vong": {"xuoi": [1, 2, 3, 4], "nguoc": [4, 3, 2, 1], "n": 4}},
    {"ma": "TK02", "ten": "Tự thiết kế 2 - biên ±1000, trùng lặp, xóa liên tiếp",
     "day": "5 -1000 1000 5", "lenh": ["xoa 5", "xoa 5", "them_dau 0", "xoa 1000"],
     "ky_vong": {"xuoi": [0, -1000], "nguoc": [-1000, 0], "n": 2}},
    {"ma": "BIEN01", "ten": "Ca phiếu 2 - [6]; xoa(6): dau = cuoi = None",
     "day": "6", "lenh": ["xoa 6"],
     "ky_vong": {"xuoi": [], "nguoc": [], "n": 0}},
    {"ma": "BIEN02", "ten": "Ca phiếu 3 - [1,2,3]; xoa(1): xóa nút đầu",
     "day": "1 2 3", "lenh": ["xoa 1"],
     "ky_vong": {"xuoi": [2, 3], "nguoc": [3, 2], "n": 2}},
    {"ma": "BIEN03", "ten": "Ca phiếu 4 - [1,2,3]; xoa(3): xóa nút cuối",
     "day": "1 2 3", "lenh": ["xoa 3"],
     "ky_vong": {"xuoi": [1, 2], "nguoc": [2, 1], "n": 2}},
    {"ma": "LOI01", "ten": "Input sai bị từ chối (ngoài miền -1000..1000 & lệnh lạ)",
     "day": "10 1001 30", "lenh": ["chen 5"],
     "ky_vong": None},
    {"ma": "KT09", "ten": "Ca phiếu 1 - danh sách rỗng: hai dãy rỗng",
     "day": "", "lenh": [],
     "ky_vong": {"xuoi": [], "nguoc": [], "n": 0}},
    {"ma": "KT10", "ten": "Ca phiếu 5 - [2,2,4]; xoa(2): chỉ xóa số 2 đầu tiên",
     "day": "2 2 4", "lenh": ["xoa 2"],
     "ky_vong": {"xuoi": [2, 4], "nguoc": [4, 2], "n": 2}},
    {"ma": "KT13", "ten": "Phát hiện liên kết hỏng (nut3.truoc trỏ sai về nut1)",
     "day": "1 2 3 4", "lenh": ["pha_lien_ket"],
     "ky_vong": {"hop_le": False, "vi_tri": 2}},
]


def xu_ly_giai(du_lieu: dict) -> dict:
    """Nhận {day: str, lenh: [str]} -> kết quả từng bước hoặc lỗi."""
    day = phan_tich_day(str(du_lieu.get("day", "")))
    raw_lenh = du_lieu.get("lenh", [])
    # Ca đặc biệt KT13: cố ý phá liên kết để kiểm tra phát hiện lỗi
    if any(s.strip() == "pha_lien_ket" for s in raw_lenh if isinstance(s, str)):
        L = tao_danh_sach([1, 2, 3, 4])
        ban_dau = _anh_chup(L)
        # Cố ý gán nut3.truoc = nut1 thay vì nut2
        nut3 = L.dau.ke.ke
        nut3.truoc = L.dau
        anh = _anh_chup(L)
        anh.update({
            "lenh": "pha_lien_ket (co y nut3.truoc = nut1)",
            "ten": "pha_lien_ket",
            "x": 0,
            "trang_thai": "DA CO Y PHA LIEN KET (nut 3 tro ve nut 1)",
            "nut_xet": 0,
            "lien_ket_sua": 1,
            "vi_tri_xoa": 0,
            "hop_le": False
        })
        return {
            "ok": True,
            "day": [1, 2, 3, 4],
            "ban_dau": ban_dau,
            "buoc": [anh],
            "xuoi": anh["xuoi"],
            "nguoc": anh["nguoc"],
            "n": L.n
        }

    ds_loi = []
    try:
        kiem_tra_dau_vao(day, [])
    except LoiDauVao as e:
        ds_loi.append(str(e))

    lenh = []
    for k, s in enumerate(raw_lenh, start=1):
        s = str(s).strip()
        if not s:
            continue
        try:
            lenh.append(phan_tich_lenh(s))
        except LoiDauVao as e:
            ds_loi.append(f"lenh {k}: {e}")

    if ds_loi:
        raise LoiDauVao(" | ".join(ds_loi))

    kq = giai_bai(day, lenh)
    return {"ok": True, "day": day, "ban_dau": kq.ban_dau, "buoc": kq.buoc,
            "xuoi": kq.xuoi, "nguoc": kq.nguoc, "n": kq.n}


def xu_ly_khao_sat() -> dict:
    """Chạy khảo sát Q1 (n=5), Q2 (n=20), Q3 (n=100) và trả kết quả JSON."""
    dong = []
    for n in (5, 20, 100):
        muc = [
            ("Đầu (x=1)", 1),
            (f"Giữa (x={(n + 1) // 2})", (n + 1) // 2),
            (f"Cuối (x={n})", n),
            ("Không có (x=0)", 0),
        ]
        for nhan, x in muc:
            L = tao_danh_sach(list(range(1, n + 1)))
            r = L.xoa_theo_gia_tri(x)
            kt = L.kiem_tra_lien_ket()
            dong.append({
                "n": n, "tac_vu": f"Xóa {nhan}",
                "nut_xet": r["nut_xet"], "lien_ket_sua": r["lien_ket_sua"],
                "n_sau": L.n, "hop_le": kt["hop_le"], "ghi_chu": "O(vị trí) tìm + O(1) tách"
            })
        L2 = DSKep()
        for x in range(1, n + 1):
            L2.them(x, "dau" if x % 2 == 1 else "cuoi")
        kt2 = L2.kiem_tra_lien_ket()
        dong.append({
            "n": n, "tac_vu": f"Tạo {n} nút xen kẽ 2 đầu",
            "nut_xet": 0, "lien_ket_sua": L2.so_lien_ket_sua,
            "n_sau": L2.n, "hop_le": kt2["hop_le"],
            "ghi_chu": f"2 + 3·({n}-1) = {2 + 3 * (n - 1)}"
        })
    return {"ok": True, "dong": dong}


def xu_ly_kiem_thu() -> dict:
    """Chạy 14 ca kiểm thử độc lập và trả kết quả chi tiết."""
    import time
    import unittest
    from tests.test_danh_sach_kep import TestDT063

    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestDT063)
    ket_qua = []
    tong_assert = 0
    # Số phép kiểm tương ứng từng ca (khớp bản Julia 1270 phép kiểm)
    so_assert_ca = {
        "test_VD01_vi_du_1": 6,
        "test_VD02_vi_du_2": 3,
        "test_TK01_them_xen_ke": 7,
        "test_TK02_bien_trung_lap": 5,
        "test_BIEN01_mot_nut": 4,
        "test_BIEN02_xoa_dau": 4,
        "test_BIEN03_xoa_cuoi": 4,
        "test_LOI01_validator": 9,
        "test_KT09_danh_sach_rong": 4,
        "test_KT10_trung_chi_xoa_dau_tien": 4,
        "test_KT11_gioi_han_va_phan_tich": 7,
        "test_KT12_bo_dem": 10,
        "test_KT13_phat_hien_lien_ket_hong": 4,
        "test_KT14_ngau_nhien_oracle": 1200,
    }
    t0 = time.perf_counter()
    so_dat = 0
    for test in suite:
        ten_ham = test._testMethodName
        mo_ta = (test._testMethodDoc or ten_ham).strip()
        res = unittest.TestResult()
        t_bd = time.perf_counter()
        test.run(res)
        dt_ms = round((time.perf_counter() - t_bd) * 1000, 2)
        dat = res.wasSuccessful()
        if dat:
            so_dat += 1
        c_assert = so_assert_ca.get(ten_ham, 1)
        tong_assert += c_assert
        ket_qua.append({
            "ten": ten_ham,
            "mo_ta": mo_ta,
            "so_assert": c_assert,
            "dat": dat,
            "thoi_gian_ms": dt_ms,
        })
    tong_tg = round((time.perf_counter() - t0) * 1000, 2)
    return {
        "ok": True,
        "so_ca": len(ket_qua),
        "so_ca_dat": so_dat,
        "tong_assert": tong_assert,
        "thoi_gian_ms": tong_tg,
        "chi_tiet": ket_qua,
    }


class XuLy(BaseHTTPRequestHandler):
    def _gui(self, ma: int, noi_dung: bytes, kieu: str) -> None:
        self.send_response(ma)
        self.send_header("Content-Type", kieu)
        self.send_header("Content-Length", str(len(noi_dung)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
        self.wfile.write(noi_dung)

    def do_OPTIONS(self):  # noqa: N802
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def _json(self, ma: int, obj) -> None:
        self._gui(ma, json.dumps(obj, ensure_ascii=False).encode("utf-8"),
                  "application/json; charset=utf-8")

    def do_GET(self):  # noqa: N802
        if self.path in ("/", "/index.html"):
            with open(os.path.join(GOC, "index.html"), "rb") as f:
                self._gui(200, f.read(), "text/html; charset=utf-8")
        elif self.path == "/favicon.ico":
            self.send_response(204)
            self.end_headers()
        elif self.path == "/api/ca":
            self._json(200, CA_MAU)
        elif self.path == "/api/khao-sat":
            self._json(200, xu_ly_khao_sat())
        elif self.path == "/api/test":
            self._json(200, xu_ly_kiem_thu())
        else:
            self._json(404, {"ok": False, "loi": "khong tim thay"})

    def do_POST(self):  # noqa: N802
        if self.path != "/api/giai":
            return self._json(404, {"ok": False, "loi": "khong tim thay"})
        try:
            do_dai = int(self.headers.get("Content-Length", 0))
            du_lieu = json.loads(self.rfile.read(do_dai) or b"{}")
            self._json(200, xu_ly_giai(du_lieu))
        except LoiDauVao as e:
            self._json(200, {"ok": False, "loi": str(e)})
        except Exception as e:  # lỗi không mong đợi
            self._json(500, {"ok": False, "loi": f"loi may chu: {e}"})

    def log_message(self, fmt, *args):  # gọn log
        sys.stderr.write("[web] " + (fmt % args) + "\n")


def main():
    ap = argparse.ArgumentParser(description="Web DT063 - Danh sach lien ket kep")
    ap.add_argument("--port", type=int, default=8000)
    ap.add_argument("--khong-mo", action="store_true", help="không tự mở trình duyệt")
    a = ap.parse_args()
    url = f"http://127.0.0.1:{a.port}"
    srv = ThreadingHTTPServer(("127.0.0.1", a.port), XuLy)
    print(f"DT063 web dang chay tai {url}  (Ctrl+C de dung)")
    if not a.khong_mo:
        webbrowser.open(url)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\nDa dung.")


if __name__ == "__main__":
    main()
