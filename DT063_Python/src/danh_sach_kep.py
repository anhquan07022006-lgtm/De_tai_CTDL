"""
DT063 - Danh sách liên kết kép và duyệt theo hai chiều (bản Python).
Sinh viên: Bùi Anh Quân - N24DCDT075 - D24CQDT01-N.
Giáo trình INT1306, Chương 5, mục 5.2.6; trang in 122-124; trang PDF 134-136.

Mọi thao tác trên liên kết (thêm hai đầu, tìm, tách nút, duyệt xuôi/ngược,
kiểm tra nhất quán) đều tự cài bằng con trỏ `truoc`/`ke`; KHÔNG dùng list
của Python để giả lập danh sách. list chỉ dùng để trả kết quả duyệt ra ngoài.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Optional

SO_NUT_TOI_DA = 1000   # phiếu: 0..1000 nút
GIA_TRI_MIN = -1000    # phiếu: giá trị -1000..1000, cho phép trùng
GIA_TRI_MAX = 1000
LENH_HOP_LE = ("them_dau", "them_cuoi", "xoa")


class LoiDauVao(ValueError):
    """Lỗi input vi phạm hợp đồng của phiếu (tương đương ArgumentError)."""


# ---------------------------------------------------------------------------
# Cấu trúc dữ liệu
# ---------------------------------------------------------------------------
class NutKep:
    """Một nút của danh sách kép.

    - gia_tri: số nguyên lưu trong nút.
    - truoc  : nút đứng trước (None nếu là nút đầu).
    - ke     : nút đứng sau (None nếu là nút cuối).
    """

    __slots__ = ("gia_tri", "truoc", "ke")

    def __init__(self, gia_tri: int):
        self.gia_tri: int = gia_tri
        self.truoc: Optional[NutKep] = None
        self.ke: Optional[NutKep] = None

    def __repr__(self) -> str:  # pragma: no cover - chỉ để debug
        return f"NutKep({self.gia_tri})"


class DSKep:
    """Danh sách liên kết kép.

    - dau, cuoi       : nút đầu và nút cuối (None khi rỗng).
    - n               : số nút hiện có.
    - so_nut_xet      : bộ đếm số nút đã so sánh khi tìm theo giá trị.
    - so_lien_ket_sua : bộ đếm số lần gán vào dau/cuoi/truoc/ke để nối hoặc
                        tách cấu trúc (không đếm việc xóa liên kết của nút đã tách).

    Bất biến: dau is None <=> cuoi is None <=> n == 0;
              dau.truoc is None; cuoi.ke is None;
              với mọi nút u có u.ke = v thì v.truoc is u.
    """

    def __init__(self) -> None:
        self.dau: Optional[NutKep] = None
        self.cuoi: Optional[NutKep] = None
        self.n: int = 0
        self.so_nut_xet: int = 0
        self.so_lien_ket_sua: int = 0

    def dat_lai_bo_dem(self) -> "DSKep":
        """Đặt lại hai bộ đếm chi phí về 0."""
        self.so_nut_xet = 0
        self.so_lien_ket_sua = 0
        return self

    # ------------------------------------------------------------------ thêm
    def them(self, x, dau_hay_cuoi: str) -> NutKep:
        """Thêm nút giá trị x vào 'dau' hoặc 'cuoi'. Thời gian O(1)."""
        vt = dau_hay_cuoi.lstrip(":") if isinstance(dau_hay_cuoi, str) else ""
        if vt not in ("dau", "cuoi"):
            raise LoiDauVao(f"vi tri them phai la 'dau' hoac 'cuoi', nhan {dau_hay_cuoi!r}")
        v = kiem_tra_gia_tri(x)
        if self.n >= SO_NUT_TOI_DA:
            raise LoiDauVao(f"danh sach da du {SO_NUT_TOI_DA} nut, khong the them {v}")
        m = NutKep(v)
        if self.dau is None:
            # Danh sách rỗng: nút mới vừa là đầu vừa là cuối.
            self.dau = m
            self.cuoi = m
            self.so_lien_ket_sua += 2
        elif vt == "dau":
            m.ke = self.dau            # (1) nút mới trỏ tới đầu cũ
            self.dau.truoc = m         # (2) đầu cũ trỏ ngược về nút mới
            self.dau = m               # (3) cập nhật con trỏ đầu
            self.so_lien_ket_sua += 3
        else:
            m.truoc = self.cuoi        # (1) nút mới trỏ ngược về cuối cũ
            self.cuoi.ke = m           # (2) cuối cũ trỏ tới nút mới
            self.cuoi = m              # (3) cập nhật con trỏ cuối
            self.so_lien_ket_sua += 3
        self.n += 1
        return m

    # ------------------------------------------------------------------- tìm
    def tim_nut(self, x) -> Optional[NutKep]:
        """Duyệt từ đầu, trả nút ĐẦU TIÊN có giá trị x hoặc None. O(n).

        Mỗi nút được so sánh làm tăng so_nut_xet thêm 1.
        """
        v = kiem_tra_gia_tri(x)
        p = self.dau
        while p is not None:
            self.so_nut_xet += 1
            if p.gia_tri == v:
                return p
            p = p.ke
        return None

    # ------------------------------------------------------------------- xóa
    def xoa_nut(self, p: NutKep) -> int:
        """Tách nút p đã biết khỏi danh sách trong O(1) và trả giá trị của nó.

        Xử lý riêng p là đầu (cập nhật dau) hoặc cuối (cập nhật cuoi).
        Sau khi tách, p.truoc và p.ke được đặt None để không giữ con trỏ cũ.
        """
        # Kiểm tra O(1): p phải đang được hai hàng xóm (hoặc dau/cuoi) trỏ tới.
        thuoc_ds = (self.dau is p if p.truoc is None else p.truoc.ke is p) and \
                   (self.cuoi is p if p.ke is None else p.ke.truoc is p)
        if not thuoc_ds:
            raise LoiDauVao("nut khong thuoc danh sach hoac lien ket da hong")

        if p.truoc is None:
            self.dau = p.ke            # p là đầu: đầu mới là nút sau p
        else:
            p.truoc.ke = p.ke          # nút trước bỏ qua p
        if p.ke is None:
            self.cuoi = p.truoc        # p là cuối: cuối mới là nút trước p
        else:
            p.ke.truoc = p.truoc       # nút sau trỏ ngược bỏ qua p
        self.so_lien_ket_sua += 2
        p.truoc = None
        p.ke = None
        self.n -= 1
        return p.gia_tri

    def xoa_theo_gia_tri(self, x) -> dict:
        """Tìm lần xuất hiện đầu tiên của x rồi tách.

        Trả {da_xoa, nut_xet, lien_ket_sua} của riêng thao tác này.
        """
        xet0, sua0 = self.so_nut_xet, self.so_lien_ket_sua
        p = self.tim_nut(x)
        da_xoa = p is not None
        if da_xoa:
            self.xoa_nut(p)
        return {"da_xoa": da_xoa,
                "nut_xet": self.so_nut_xet - xet0,
                "lien_ket_sua": self.so_lien_ket_sua - sua0}

    # ----------------------------------------------------------------- duyệt
    def duyet_hai_chieu(self) -> tuple[list[int], list[int]]:
        """Duyệt xuôi theo ke từ dau và duyệt ngược theo truoc từ cuoi. O(n).

        Ném RuntimeError nếu số bước vượt n (dấu hiệu vòng hoặc n sai).
        """
        xuoi: list[int] = []
        p = self.dau
        while p is not None:
            if len(xuoi) >= self.n:
                raise RuntimeError(f"duyet xuoi vuot n={self.n}: lien ket hong hoac co vong")
            xuoi.append(p.gia_tri)
            p = p.ke
        nguoc: list[int] = []
        p = self.cuoi
        while p is not None:
            if len(nguoc) >= self.n:
                raise RuntimeError(f"duyet nguoc vuot n={self.n}: lien ket hong hoac co vong")
            nguoc.append(p.gia_tri)
            p = p.truoc
        return xuoi, nguoc

    # ----------------------------------------------------------- kiểm liên kết
    def kiem_tra_lien_ket(self) -> dict:
        """Kiểm sự nhất quán của danh sách.

        dau/cuoi/n đồng bộ, dau.truoc rỗng, mỗi cặp p.ke.truoc is p, nút cuối
        của chuỗi xuôi là cuoi, số nút đúng bằng n.
        vi_tri là vị trí (từ 1) của nút đầu tiên có liên kết không khớp;
        0 nếu hợp lệ hoặc lỗi nằm ở mức danh sách.
        """
        if self.dau is None or self.cuoi is None:
            ok = self.dau is None and self.cuoi is None and self.n == 0
            return _kt(True, 0, "danh sach rong hop le") if ok else \
                _kt(False, 0, "dau/cuoi khong dong thoi rong hoac n != 0")
        if self.dau.truoc is not None:
            return _kt(False, 1, "dau.truoc phai la None")
        p, i = self.dau, 1
        while True:
            if i > self.n:
                return _kt(False, i, f"so nut vuot n={self.n} (co the co vong)")
            q = p.ke
            if q is None:
                if p is not self.cuoi:
                    return _kt(False, i, "nut cuoi chuoi xuoi khong phai cuoi")
                if i != self.n:
                    return _kt(False, i, f"dem duoc {i} nut nhung n={self.n}")
                return _kt(True, 0, "moi cap ke/truoc khop")
            if q.truoc is not p:
                return _kt(False, i, f"nut {i}: ke.truoc khong tro lai nut {i}")
            p = q
            i += 1

    # ------------------------------------------------------------- hiển thị
    def so_do(self) -> str:
        """Sơ đồ một dòng: dau -> [10] <-> [30] <- cuoi."""
        if self.dau is None:
            return "dau = None, cuoi = None (rong)"
        phan, p = [], self.dau
        while p is not None and len(phan) <= self.n:
            phan.append(f"[{p.gia_tri}]")
            p = p.ke
        return "dau -> " + " <-> ".join(phan) + " <- cuoi"

    def bang_lien_ket(self) -> list[dict]:
        """Bảng liên kết: vị trí, giá trị nút trước, giá trị, giá trị nút sau."""
        def ten(q):
            return None if q is None else q.gia_tri
        dong, p, i = [], self.dau, 1
        while p is not None and i <= self.n:
            dong.append({"vi_tri": i, "truoc": ten(p.truoc),
                         "gia_tri": p.gia_tri, "ke": ten(p.ke)})
            p = p.ke
            i += 1
        return dong

    def bang_lien_ket_text(self) -> str:
        def s(v):
            return "None" if v is None else str(v)
        dong = ["vi tri | truoc   | gia tri | ke"]
        for d in self.bang_lien_ket():
            dong.append(f"{d['vi_tri']:<6} | {s(d['truoc']):<7} | {d['gia_tri']:<7} | {s(d['ke'])}")
        return "\n".join(dong)


def _kt(hop_le: bool, vi_tri: int, ly_do: str) -> dict:
    return {"hop_le": hop_le, "vi_tri": vi_tri, "ly_do": ly_do}


# ---------------------------------------------------------------------------
# Các hàm mức module theo đúng tên gợi ý trên phiếu giao đề tài DT063
# ---------------------------------------------------------------------------
def them_kep(L: DSKep, x, dau_hay_cuoi: str) -> NutKep:
    """Thêm nút giá trị x vào đầu ('dau') hoặc cuối ('cuoi') của danh sách L. O(1)."""
    return L.them(x, dau_hay_cuoi)


def tim_nut(L: DSKep, x) -> Optional[NutKep]:
    """Tìm và trả về nút đầu tiên có giá trị x trong L, hoặc None nếu không có. O(n)."""
    return L.tim_nut(x)


def xoa_nut(L: DSKep, p: NutKep) -> int:
    """Tách nút p đã biết khỏi danh sách L trong O(1), cập nhật đầu/cuối."""
    return L.xoa_nut(p)


def xoa_theo_gia_tri(L: DSKep, x) -> dict:
    """Tìm nút đầu tiên có giá trị x rồi tách khỏi L. O(n)."""
    return L.xoa_theo_gia_tri(x)


def duyet_hai_chieu(L: DSKep) -> tuple[list[int], list[int]]:
    """Xuất hai dãy (xuoi, nguoc) bằng cách duyệt từ dau theo ke và từ cuoi theo truoc. O(n)."""
    return L.duyet_hai_chieu()


def kiem_tra_lien_ket(L: DSKep) -> dict:
    """Kiểm tra tính nhất quán của các liên kết truoc/ke, dau/cuoi và số nút n. O(n)."""
    return L.kiem_tra_lien_ket()


def so_do(L: DSKep) -> str:
    """Biểu diễn sơ đồ danh sách dạng chuỗi một dòng."""
    return L.so_do()


def bang_lien_ket(L: DSKep) -> str:
    """Bảng liên kết từng nút (vị trí | truoc | gia tri | ke)."""
    return L.bang_lien_ket_text()


def dat_lai_bo_dem(L: DSKep) -> DSKep:
    """Đặt lại bộ đếm so_nut_xet và so_lien_ket_sua về 0."""
    return L.dat_lai_bo_dem()


# ---------------------------------------------------------------------------
# Kiểm tra input và giải bài
# ---------------------------------------------------------------------------
def kiem_tra_gia_tri(x) -> int:
    """Chấp nhận số nguyên trong -1000..1000; ngược lại ném LoiDauVao."""
    if isinstance(x, bool) or not isinstance(x, int):
        raise LoiDauVao(f"gia tri phai la so nguyen, nhan {x!r}")
    if not (GIA_TRI_MIN <= x <= GIA_TRI_MAX):
        raise LoiDauVao(f"gia tri {x} nam ngoai mien {GIA_TRI_MIN}..{GIA_TRI_MAX}")
    return int(x)


def tao_danh_sach(day) -> DSKep:
    """Tạo danh sách từ dãy ban đầu bằng cách thêm cuối lần lượt, rồi đặt lại bộ đếm."""
    if len(day) > SO_NUT_TOI_DA:
        raise LoiDauVao(f"day ban dau co {len(day)} phan tu, vuot {SO_NUT_TOI_DA}")
    L = DSKep()
    for x in day:
        L.them(x, "cuoi")
    return L.dat_lai_bo_dem()


_MAU_LENH = re.compile(r"^\s*(them_dau|them_cuoi|xoa)\s*\(?\s*([+-]?\d+)\s*\)?\s*;?\s*$")


def phan_tich_lenh(s: str) -> tuple[str, int]:
    """Đọc một lệnh dạng 'them_dau 5', 'them_cuoi(5)', 'xoa -3'."""
    m = _MAU_LENH.match(s)
    if m is None:
        raise LoiDauVao(f'lenh khong hop le: "{s}" (dung them_dau x | them_cuoi x | xoa x)')
    return m.group(1), kiem_tra_gia_tri(int(m.group(2)))


def phan_tich_day(s: str) -> list[int]:
    """Đọc dãy ban đầu: '10 20 30', '[10, 20, 30]' hoặc rỗng."""
    s = s.strip().strip("[]").replace(",", " ")
    kq = []
    for i, t in enumerate(s.split(), start=1):
        if not re.fullmatch(r"[+-]?\d+", t):
            raise LoiDauVao(f"day[{i}]: '{t}' khong phai so nguyen")
        kq.append(int(t))
    return kq


def kiem_tra_dau_vao(day, lenh) -> bool:
    """Hợp đồng input của phiếu.

    day : list số nguyên dài 0..1000, giá trị -1000..1000.
    lenh: list cặp (ten, x) với ten thuộc LENH_HOP_LE, x trong miền.
    Vi phạm -> LoiDauVao có lý do.
    """
    if not isinstance(day, (list, tuple)):
        raise LoiDauVao("day ban dau phai la mang")
    if len(day) > SO_NUT_TOI_DA:
        raise LoiDauVao(f"day ban dau co {len(day)} phan tu, vuot {SO_NUT_TOI_DA}")
    for i, x in enumerate(day, start=1):
        try:
            kiem_tra_gia_tri(x)
        except LoiDauVao as e:
            raise LoiDauVao(f"day[{i}]: {e}") from None
    if not isinstance(lenh, (list, tuple)):
        raise LoiDauVao("danh sach lenh phai la mang")
    for k, c in enumerate(lenh, start=1):
        if not (isinstance(c, (list, tuple)) and len(c) == 2 and isinstance(c[0], str)):
            raise LoiDauVao(f"lenh {k} phai co dang (ten, x), nhan {c!r}")
        if c[0] not in LENH_HOP_LE:
            raise LoiDauVao(f"lenh {k}: ten '{c[0]}' khong thuoc them_dau/them_cuoi/xoa")
        try:
            kiem_tra_gia_tri(c[1])
        except LoiDauVao as e:
            raise LoiDauVao(f"lenh {k}: {e}") from None
    return True


@dataclass
class KetQua:
    L: DSKep
    buoc: list = field(default_factory=list)
    xuoi: list = field(default_factory=list)
    nguoc: list = field(default_factory=list)
    n: int = 0
    ban_dau: dict = field(default_factory=dict)


def _anh_chup(L: DSKep) -> dict:
    """Ảnh chụp trạng thái danh sách để in / gửi cho web."""
    xuoi, nguoc = L.duyet_hai_chieu()
    return {"xuoi": xuoi, "nguoc": nguoc, "n": L.n,
            "so_do": L.so_do(), "bang": L.bang_lien_ket(),
            "dau": None if L.dau is None else L.dau.gia_tri,
            "cuoi": None if L.cuoi is None else L.cuoi.gia_tri,
            "kiem_tra": L.kiem_tra_lien_ket()}


def giai_bai(day, lenh) -> KetQua:
    """Kiểm input, tạo danh sách, chạy lần lượt các lệnh, ghi trạng thái sau mỗi lệnh."""
    kiem_tra_dau_vao(day, lenh)
    L = tao_danh_sach(list(day))
    kq = KetQua(L=L, ban_dau=_anh_chup(L))
    for ten, x in lenh:
        xet0, sua0 = L.so_nut_xet, L.so_lien_ket_sua
        vi_tri_xoa = 0
        if ten in ("them_dau", "them_cuoi"):
            L.them(x, "dau" if ten == "them_dau" else "cuoi")
            trang_thai = f"DA THEM {x} VAO {'DAU' if ten == 'them_dau' else 'CUOI'}"
        else:
            r = L.xoa_theo_gia_tri(x)
            trang_thai = f"DA XOA {x}" if r["da_xoa"] else f"KHONG TIM THAY {x}"
            vi_tri_xoa = r["nut_xet"] if r["da_xoa"] else 0
        anh = _anh_chup(L)
        anh.update({"lenh": f"{ten}({x})", "ten": ten, "x": x,
                    "trang_thai": trang_thai,
                    "nut_xet": L.so_nut_xet - xet0,
                    "lien_ket_sua": L.so_lien_ket_sua - sua0,
                    "vi_tri_xoa": vi_tri_xoa,
                    "hop_le": anh["kiem_tra"]["hop_le"]})
        kq.buoc.append(anh)
    kq.xuoi, kq.nguoc = L.duyet_hai_chieu()
    kq.n = L.n
    return kq
