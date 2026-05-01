# ── CLASS DENGAN ENKAPSULASI ────────────────────────────────
class AkunUser:
    def __init__(self, nama, email, password):
        self.nama           = nama    # public  — boleh diakses bebas
        self._email         = email   # protected — disarankan internal
        self.__password     = password  # private — TIDAK bisa diakses luar
        self.__login_gagal  = 0         # private — hitungan gagal login
    # Getter email — satu-satunya cara baca email
    def get_email(self):
        return self._email
    # Setter email — validasi dulu sebelum disimpan
    def set_email(self, email_baru):
        if "@" in email_baru:
            self._email = email_baru
            print("Email berhasil diubah!")
        else:
            print("Email tidak valid!")
    # Verifikasi password — tidak mengembalikan password asli
    def cek_password(self, input_password):
        if input_password == self.__password:
            self.__login_gagal = 0
            return True
        else:
            self.__login_gagal += 1
            print(f"Password salah! Percobaan ke-{self.__login_gagal}")
            if self.__login_gagal >= 3:
                print("Akun dikunci! Terlalu banyak percobaan.")
            return False
    def tampilkan_info(self):
        print(f"Nama  : {self.nama}")
        print(f"Email : {self.get_email()}")
        # __password TIDAK ditampilkan di sini!

# ── CLASS KOMODITAS DENGAN HARGA POKOK RAHASIA ──────────────
class KomoditasRahasia:
    def __init__(self, nama, harga_jual, harga_pokok, pin_admin):
        self.nama          = nama
        self.harga_jual    = harga_jual
        self.__harga_pokok = harga_pokok  # PRIVATE — rahasia bisnis
        self.__pin_admin   = pin_admin    # PRIVATE — PIN verifikasi
    # Getter harga pokok — hanya tampilkan, tidak bisa diubah langsung
    def get_harga_pokok(self):
        return self.__harga_pokok
    # Update harga pokok — harus verifikasi PIN dulu
    def update_harga_pokok(self, harga_baru, pin_input):
        if pin_input == self.__pin_admin:
            if harga_baru > 0:
                self.__harga_pokok = harga_baru
                print(f"Harga pokok {self.nama} berhasil diperbarui.")
            else:
                print("Harga tidak boleh nol atau negatif!")
        else:
            print("PIN salah! Anda tidak memiliki akses.")
    def info(self):
        margin = self.harga_jual - self.__harga_pokok
        print(f"Produk: {self.nama} | Jual: Rp {self.harga_jual:,} | Margin: Rp {margin:,}")

# ── PENGGUNAAN ─────────────────────────────────────────────
user1 = AkunUser("Budi", "budi@mail.com", "rahasia123")
user1.tampilkan_info()
user1.cek_password("salah")      # Output: Password salah! Percobaan ke-1
user1.cek_password("rahasia123")  # Output: login berhasil (return True)
# print(user1.__password)  # AttributeError! — atribut private tidak bisa diakses
	
beras = KomoditasRahasia("Beras Medium", 15000, 12000, "1234")
beras.info()  # Output: Produk: Beras Medium | Jual: Rp 15,000 | Margin: Rp 3,000
beras.update_harga_pokok(13000, "5678")  # Gagal: PIN salah
beras.update_harga_pokok(13000, "1234")  # Berhasil
