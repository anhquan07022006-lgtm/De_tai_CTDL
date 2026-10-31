"""
Demo console DT063 (Python).

  python demo.py              # hai ví dụ trên phiếu
  python demo.py --ca 3       # 1..10 (xem README)
  python demo.py --nhap       # nhập từ bàn phím
  python demo.py --khao-sat   # đo nút xét / liên kết sửa với n = 5, 20, 100
"""
import argparse
import os
import sys

# Đảm bảo in tiếng Việt trên console Windows không bị UnicodeEncodeError
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Thêm thư mục gốc vào sys.path để chạy từ bất kỳ đâu
GOC = os.path.dirname(os.path.abspath(__file__))
if GOC not in sys.path:
    sys.path.insert(0, GOC)
sys.path.insert(0, os.path.join(GOC, "src"))
sys.path.insert(0, os.path.join(GOC, "web"))

try:
    from src.danh_sach_kep import (
        DSKep,
        LoiDauVao,
        giai_bai,
        phan_tich_day,
        phan_tich_lenh,
        tao_danh_sach,
    )
    from web.app import CA_MAU
except ImportError:
    from danh_sach_kep import (  # type: ignore
        DSKep,
        LoiDauVao,
        giai_bai,
        phan_tich_day,
        phan_tich_lenh,
        tao_danh_sach,
    )
    from app import CA_MAU  # type: ignore


DE = "DT063 - DANH SACH LIEN KET KEP VA DUYET THEO HAI CHIEU"


def _fmt(v: list[int]) -> str:
    return "[" + ",".join(str(x) for x in v) + "]"


def _in_trang_thai(anh: dict) -> None:
    kt = anh["kiem_tra"]
    print(f"  So do : {anh['so_do']}")
    print("    vi tri | truoc   | gia tri | ke")
    for d in anh["bang"]:
        tr = "None" if d["truoc"] is None else str(d["truoc"])
        ke = "None" if d["ke"] is None else str(d["ke"])
        print(f"    {d['vi_tri']:<6} | {tr:<7} | {d['gia_tri']:<7} | {ke}")
    print(f"  xuoi={_fmt(anh['xuoi'])}; nguoc={_fmt(anh['nguoc'])}; n={anh['n']}")
    dau_s = "None" if anh["dau"] is None else str(anh["dau"])
    cuoi_s = "None" if anh["cuoi"] is None else str(anh["cuoi"])
    print(f"  dau={dau_s}; cuoi={cuoi_s}")
    dao_ok = "DUNG" if anh["nguoc"] == list(reversed(anh["xuoi"])) else "SAI"
    kt_s = "HOP LE" if kt["hop_le"] else f"LOI tai vi tri {kt['vi_tri']}"
    print(f"  nguoc == dao(xuoi): {dao_ok}; kiem_tra_lien_ket: {kt_s} ({kt['ly_do']})")


def minh_hoa_lien_ket_hong():
    print(DE)
    print("Ca KT13: kiem_tra_lien_ket phat hien vi tri lien ket khong khop (yeu cau tuy chon)")
    L = tao_danh_sach([1, 2, 3, 4])
    print("Truoc khi pha:", L.kiem_tra_lien_ket())
    nut3 = L.dau.ke.ke
    nut3.truoc = L.dau  # co y lam sai: truoc cua nut 3 tro ve nut 1 thay vi nut 2
    print("Co y gan nut3.truoc = nut1 (dung phai la nut2).")
    print("Expected: hop_le=False, vi_tri=2 (nut 2 co ke.truoc khong tro lai chinh no).")
    kt = L.kiem_tra_lien_ket()
    print("Actual  :", kt)
    ok = not kt["hop_le"] and kt["vi_tri"] == 2
    print("KET LUAN:", "KHOP KY VONG" if ok else "KHONG KHOP KY VONG")
    if not ok:
        sys.exit(1)


def in_ket_qua(ma, ten, day_str, lenh_str, ky_vong=None):
    print("=" * 70)
    if ma == "KT13":
        return minh_hoa_lien_ket_hong()
    if ma == "LOI01":
        print(DE)
        print(f"Ca {ma}: {ten}")
        print("Input  : day=[10,1001,30]; lenh=xoa(10)")
        print("Expected: validator tu choi, bao day[2] = 1001 ngoai mien; khong tao danh sach.")
        da_bat = False
        try:
            giai_bai([10, 1001, 30], [("xoa", 10)])
        except LoiDauVao as e:
            print(f"DA TU CHOI: {e}")
            da_bat = "day[2]" in str(e) and "1001" in str(e)
        print('\nInput bo sung: lenh go tu ban phim "chen 5" (ten lenh khong co trong phieu)')
        try:
            phan_tich_lenh("chen 5")
            da_bat = False
        except LoiDauVao as e:
            print(f"DA TU CHOI: {e}")
            da_bat = da_bat and ("khong hop le" in str(e))
        print("KET LUAN:", "KHOP KY VONG (loi du kien da duoc bat, chuong trinh khong dung bat thuong)"
              if da_bat else "KHONG KHOP KY VONG")
        if not da_bat:
            sys.exit(1)
        return

    print(DE)
    print(f"Ca {ma}: {ten}")
    try:
        day = phan_tich_day(day_str)
        lenh = [phan_tich_lenh(s) for s in lenh_str]
        lenh_hien_thi = "; ".join(f"{c[0]}({c[1]})" for c in lenh) if lenh else "(khong co)"
        print(f"Input  : day={_fmt(day)}; lenh={lenh_hien_thi}")
        if ky_vong is not None:
            print(f"Expected (tinh tay): xuoi={_fmt(ky_vong['xuoi'])}; "
                  f"nguoc={_fmt(ky_vong['nguoc'])}; n={ky_vong['n']}")
        kq = giai_bai(day, lenh)
    except LoiDauVao as e:
        print(f"  -> DA TU CHOI (LoiDauVao): {e}")
        return

    print("\nBuoc 0 - khoi tao tu day ban dau")
    _in_trang_thai(kq.ban_dau)
    for k, b in enumerate(kq.buoc, start=1):
        print(f"\nBuoc {k} - {b['lenh']} -> {b['trang_thai']}")
        print(f"  So nut xet khi tim: {b['nut_xet']}; so lien ket sua: {b['lien_ket_sua']}")
        _in_trang_thai(b)

    print(f"\nActual : xuoi={_fmt(kq.xuoi)}; nguoc={_fmt(kq.nguoc)}; n={kq.n}")
    if ky_vong is not None:
        ok = (kq.xuoi == ky_vong["xuoi"] and kq.nguoc == ky_vong["nguoc"]
              and kq.n == ky_vong["n"] and kq.L.kiem_tra_lien_ket()["hop_le"])
        print("KET LUAN:", "KHOP KY VONG" if ok else "KHONG KHOP KY VONG")
        if not ok:
            sys.exit(1)


def nhap():
    print(DE, "- NHAP TU BAN PHIM")
    day = input("Nhap day ban dau (cac so nguyen cach nhau boi dau cach, Enter neu rong): ")
    k_str = input("Nhap so lenh k: ").strip()
    if not k_str.isdigit():
        raise LoiDauVao(f"so lenh k phai la so nguyen khong am, nhan {k_str!r}")
    k = int(k_str)
    lenh = [input(f"Lenh {i + 1} (them_dau x | them_cuoi x | xoa x): ") for i in range(k)]
    in_ket_qua("NHAP", "Du lieu nhap tu ban phim", day, lenh)


def khao_sat():
    print("=" * 78)
    print("KHAO SAT CHI PHI: day = [1,2,...,n]; dem so nut xet (tim) va so lien ket sua (tach)")
    print(f"{'n':<5} | {'x can xoa':<22} | {'nut xet':>7} | {'lien ket sua':>12} | {'n sau':>5} | hop le")
    for n in (5, 20, 100):
        muc = [("dau (x=1)", 1),
               (f"giua (x={(n + 1) // 2})", (n + 1) // 2),
               (f"cuoi (x={n})", n),
               ("khong co (x=0)", 0)]
        for nhan, x in muc:
            L = tao_danh_sach(list(range(1, n + 1)))
            r = L.xoa_theo_gia_tri(x)
            hl = "co" if L.kiem_tra_lien_ket()["hop_le"] else "KHONG"
            print(f"{n:<5} | {nhan:<22} | {r['nut_xet']:>7} | {r['lien_ket_sua']:>12} | {L.n:>5} | {hl}")
        L = DSKep()
        for x in range(1, n + 1):
            L.them(x, "dau" if x % 2 == 1 else "cuoi")
        hl = "co" if L.kiem_tra_lien_ket()["hop_le"] else "KHONG"
        print(f"{n:<5} | {'tao n nut xen ke 2 dau':<22} | {0:>7} | {L.so_lien_ket_sua:>12} | {L.n:>5} | {hl}"
              f"   (= 2 + 3(n-1) = {2 + 3 * (n - 1)})")
        print("-" * 78)
    print("Bo nho: moi nut giu 1 gia tri + 2 lien ket (truoc, ke); DSLK don chi giu 1 lien ket.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ca", type=int, help="chọn ca từ 1 đến 11")
    ap.add_argument("--nhap", action="store_true", help="nhập từ bàn phím")
    ap.add_argument("--khao-sat", action="store_true", help="khảo sát n=5, 20, 100")
    ap.add_argument("--tat-ca", action="store_true", help="chạy toàn bộ 11 ca")
    a = ap.parse_args()
    if a.nhap:
        return nhap()
    if a.khao_sat:
        return khao_sat()
    if a.ca is not None:
        if not (1 <= a.ca <= len(CA_MAU)):
            print(f"Loi: chi co the chon --ca tu 1 den {len(CA_MAU)}")
            sys.exit(1)
        ds = [CA_MAU[a.ca - 1]]
    elif a.tat_ca:
        ds = CA_MAU
    else:
        ds = CA_MAU[:2]
    for c in ds:
        in_ket_qua(c["ma"], c["ten"], c["day"], c["lenh"], c.get("ky_vong"))


if __name__ == "__main__":
    main()
