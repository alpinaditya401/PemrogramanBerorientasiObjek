# ── CLASS INDUK ────────────────────────────────────────────
class Komoditas:
    def __init__(self, nama, harga_kemarin, harga_sekarang):
        self.nama           = nama
        self.harga_kemarin  = harga_kemarin
        self.harga_sekarang = harga_sekarang
    def hitung_selisih(self):
        return self.harga_sekarang - self.harga_kemarin
    def hitung_status(self):  # akan di-override tiap anak
        return "Status belum ditentukan"
    def tampilkan_info(self):
        selisih = self.hitung_selisih()
        status  = self.hitung_status()   # polimorfisme terjadi di sini!
        print(f"Komoditas : {self.nama}")
        print(f"Harga     : Rp {self.harga_sekarang:,}")
        print(f"Selisih   : Rp {selisih:,}")
        print(f"Status    : {status}")
        print("-" * 35)

# ── CLASS ANAK 1: KomoditasPangan ──────────────────────────
class KomoditasPangan(Komoditas):
    def hitung_status(self):   # override — batas naik 5%
        selisih = self.hitung_selisih()
        persen  = (selisih / self.harga_kemarin) * 100
        if persen > 5:
            return f"NAIK {persen:.1f}% - Perlu Perhatian"
        elif persen < -5:
            return f"TURUN {abs(persen):.1f}% - Stok Melimpah"
        else:
            return "STABIL"

# ── CLASS ANAK 2: KomoditasBBM ─────────────────────────────
class KomoditasBBM(Komoditas):
    def hitung_status(self):   # override — batas naik lebih ketat 2%
        selisih = self.hitung_selisih()
        persen  = (selisih / self.harga_kemarin) * 100
        if persen > 2:
            return f"NAIK {persen:.1f}% - Potensi Inflasi"
        elif persen < -2:
            return f"TURUN {abs(persen):.1f}% - Harga Turun"
        else:
            return "STABIL"

# ── PENGGUNAAN: satu loop untuk semua jenis ─────────────────
daftar = [
    KomoditasPangan("Beras Medium", 14000, 14700),
    KomoditasBBM("Pertalite",  10000, 10200),
    KomoditasPangan("Cabai Rawit", 40000, 58000),
]
for item in daftar:
    item.tampilkan_info()   # method sama, hasil beda (POLIMORFISME)
# Output:
# Komoditas : Beras Medium | Selisih: Rp 700   | Status: NAIK 5.0% - Perlu Perhatian
# Komoditas : Pertalite    | Selisih: Rp 200   | Status: STABIL
# Komoditas : Cabai Rawit  | Selisih: Rp 18.000| Status: NAIK 45.0% - Perlu Perhatian
