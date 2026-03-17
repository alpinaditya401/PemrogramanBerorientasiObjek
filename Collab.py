class Pasien:
    def __init__(self, nama, layanan, biaya):
        self.nama = nama
        self.layanan = layanan
        self.biaya = biaya

    def __str__(self):
        return f"Pasien: {self.nama:15} | Layanan: {self.layanan:15} | Biaya: Rp{self.biaya:,}"

class Klinik:
    def __init__(self, nama_klinik):
        self.nama_klinik = nama_klinik
        self.daftar_antrean = []

    def tambah_pasien(self, objek_pasien):
        self.daftar_antrean.append(objek_pasien)
        print(f"✅ {objek_pasien.nama} berhasil ditambahkan ke antrean.")

    def tampilkan_laporan(self):
        print(f"\n=== LAPORAN HARIAN {self.nama_klinik.upper()} ===")
        total_pendapatan = 0

        for p in self.daftar_antrean:
            print(p)
            total_pendapatan += p.biaya

        print("-" * 50)
        print(f"TOTAL PENDAPATAN HARI INI: Rp{total_pendapatan:,}")

    # ===== METHOD BARU DITAMBAHKAN DI SINI =====
    def cari_pasien(self, nama):
        print(f"\n🔍 Mencari pasien dengan nama: '{nama}'...")
        for p in self.daftar_antrean:
            if p.nama.lower() == nama.lower(): 
                print("✅ Pasien Ditemukan!")
                print(p)
                return 
        print("❌ Pasien TIDAK ditemukan dalam antrean.")


# --- KODE UTAMA (TIDAK ADA YANG DIUBAH) ---
klinik_kita = Klinik("Informatika Sehat")

p1 = Pasien("Alpin", "Cek Kesehatan Mental", 150000)
p2 = Pasien("Nehan", "Konsultasi Kejiwaan", 75000)
p3 = Pasien("Feri", "Cek Narkoba", 350000)


klinik_kita.tambah_pasien(p1)
klinik_kita.tambah_pasien(p2)
klinik_kita.tambah_pasien(p3)

klinik_kita.tampilkan_laporan() 

# --- CONTOH PEMANGGILAN METHOD BARU ---
klinik_kita.cari_pasien("Nehan")
klinik_kita.cari_pasien("Budi")