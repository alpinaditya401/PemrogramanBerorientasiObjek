# ── CLASS INDUK (Parent Class) ────────────────────────────
class User:
    def __init__(self, nama, email, password):
        self.nama     = nama
        self.email    = email
        self.password = password
        self.aktif    = True
    def tampilkan_info(self):
        print(f"Nama  : {self.nama}")
        print(f"Email : {self.email}")
        print(f"Status: {'Aktif' if self.aktif else 'Nonaktif'}")

# ── CLASS ANAK 1: Kontributor ──────────────────────────────
# Mewarisi semua dari User, tambah atribut provinsi
class Kontributor(User):
    def __init__(self, nama, email, password, provinsi):
        super().__init__(nama, email, password)  # warisi dari User
        self.provinsi = provinsi                 # atribut khusus Kontributor
    def tampilkan_info(self):  # override method induk
        super().tampilkan_info()
        print(f"Provinsi: {self.provinsi}")
        print(f"Role  : Kontributor")
    def lapor_harga(self, nama_barang, harga):
        print(f"{self.nama} melaporkan harga {nama_barang}: Rp {harga:,}")

# ── CLASS ANAK 2: Admin ────────────────────────────────────
# Mewarisi semua dari User, tambah atribut level
class Admin(User):
    def __init__(self, nama, email, password, level):
        super().__init__(nama, email, password)  # warisi dari User
        self.level = level                       # 'master' atau 'reguler'
    def tampilkan_info(self):  # override method induk
        super().tampilkan_info()
        print(f"Role  : Admin {self.level}")
    def setujui_data(self, nama_barang):
        print(f"Admin {self.nama} menyetujui data: {nama_barang}")

# ── PENGGUNAAN ─────────────────────────────────────────────
budi  = Kontributor("Budi", "budi@mail.com", "pass123", "Jawa Timur")
admin = Admin("Siti", "siti@infoharga.id", "admin123", "master")
budi.tampilkan_info()
# Output:
# Nama  : Budi
# Email : budi@mail.com
# Status: Aktif
# Provinsi: Jawa Timur
# Role  : Kontributor
budi.lapor_harga("Beras Medium", 14500)
# Output: Budi melaporkan harga Beras Medium: Rp 14,500
admin.setujui_data("Beras Medium")
# Output: Admin Siti menyetujui data: Beras Medium
