# ==============================================================================
# File        : paket_wisata.py
# Deskripsi   : Superclass PaketWisata yang menyimpan data dasar paket wisata.
# Konsep OOP  : Class, Constructor, Encapsulation (Private Attribute & Getter/Setter)
# ==============================================================================


class PaketWisata:
    """Superclass untuk merepresentasikan paket wisata secara umum."""

    # Constructor berparameter untuk menginisialisasi atribut private
    def __init__(
        self,
        kode_paket: str,
        nama_paket: str,
        harga: int,
        kuota: int,
        aktif: bool = True,
    ):
        # Atribut private (diawali double underscore '__') untuk Encapsulation
        self.__kode_paket = kode_paket
        self.__nama_paket = nama_paket
        self.__harga = harga
        self.__kuota = kuota
        self.__aktif = aktif

    # ==================== GETTER & SETTER (ENCAPSULATION) ====================
    def get_kode_paket(self) -> str:
        """Mengambil nilai atribut private __kode_paket."""
        return self.__kode_paket

    def get_nama_paket(self) -> str:
        """Mengambil nilai atribut private __nama_paket."""
        return self.__nama_paket

    def set_nama_paket(self, nama_baru: str) -> None:
        """Mengubah nama paket dengan validasi tidak boleh kosong."""
        if nama_baru.strip():
            self.__nama_paket = nama_baru.strip()

    def get_harga(self) -> int:
        """Mengambil nilai atribut private __harga."""
        return self.__harga

    def set_harga(self, harga_baru: int) -> bool:
        """Mengubah harga paket jika bernilai lebih dari 0."""
        if harga_baru > 0:
            self.__harga = harga_baru
            return True
        return False

    def get_kuota(self) -> int:
        """Mengambil sisa kuota paket wisata."""
        return self.__kuota

    def set_kuota(self, kuota_baru: int) -> bool:
        """Mengubah kuota paket jika bernilai tidak negatif."""
        if kuota_baru >= 0:
            self.__kuota = kuota_baru
            return True
        return False

    def is_aktif(self) -> bool:
        """Mengambil status aktif/nonaktif paket."""
        return self.__aktif

    def set_aktif(self, status_baru: bool) -> None:
        """Mengubah status aktif/nonaktif paket."""
        self.__aktif = status_baru

    # ==================== METHOD TAMBAHAN ====================
    def get_kategori(self) -> str:
        """Mengembalikan kategori paket (akan di-override oleh subclass)."""
        return "Paket Umum"

    def kurangi_kuota(self, jumlah: int = 1) -> bool:
        """Mengurangi kuota paket saat terjadi pemesanan oleh pelanggan."""
        if self.__aktif and jumlah > 0 and self.__kuota >= jumlah:
            self.__kuota -= jumlah
            return True
        return False

    def cek_status(self) -> str:
        """Mengecek status ketersediaan paket wisata berdasarkan status aktif dan kuota."""
        if not self.__aktif:
            return "Nonaktif (Tidak Tersedia)"
        if self.__kuota == 0:
            return "Penuh (Kuota Habis)"
        if self.__kuota <= 5:
            return f"Kuota Terbatas (Sisa {self.__kuota} kursi)"
        return f"Tersedia (Sisa {self.__kuota} kursi)"

    def hitung_biaya_total(self, jumlah_orang: int = 1) -> int:
        """Menghitung total biaya dasar paket wisata."""
        return self.__harga * jumlah_orang

    def tampilkan_info(self) -> str:
        """Menampilkan informasi lengkap paket wisata dalam bentuk teks terformat."""
        return (
            f"Kode Paket  : {self.__kode_paket}\n"
            f"Kategori    : {self.get_kategori()}\n"
            f"Nama Paket  : {self.__nama_paket}\n"
            f"Harga Dasar : Rp {self.__harga:,}\n"
            f"Sisa Kuota  : {self.__kuota} orang\n"
            f"Status      : {self.cek_status()}"
        )