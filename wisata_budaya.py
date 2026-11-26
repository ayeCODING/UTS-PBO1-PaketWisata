# ==============================================================================
# File        : wisata_budaya.py
# Deskripsi   : Subclass WisataBudaya yang mewarisi sifat dari PaketWisata.
# Konsep OOP  : Inheritance, super(), Encapsulation, Method Overriding
# ==============================================================================

from paket_wisata import PaketWisata


class WisataBudaya(PaketWisata):
    """Subclass untuk paket wisata bertema budaya, sejarah, dan tradisi lokal."""

    # Constructor berparameter
    def __init__(
        self,
        kode_paket: str,
        nama_paket: str,
        harga: int,
        kuota: int,
        daerah_budaya: str,
        jenis_atraksi: str,
        pemandu_lokal: str,
        aktif: bool = True,
    ):
        # Memanggil constructor milik superclass PaketWisata
        super().__init__(kode_paket, nama_paket, harga, kuota, aktif)

        # 3 Atribut private khusus milik WisataBudaya
        self.__daerah_budaya = daerah_budaya
        self.__jenis_atraksi = jenis_atraksi
        self.__pemandu_lokal = pemandu_lokal

    # ==================== GETTER & SETTER ====================
    def get_daerah_budaya(self) -> str:
        return self.__daerah_budaya

    def set_daerah_budaya(self, daerah_baru: str) -> None:
        if daerah_baru.strip():
            self.__daerah_budaya = daerah_baru.strip()

    def get_jenis_atraksi(self) -> str:
        return self.__jenis_atraksi

    def set_jenis_atraksi(self, atraksi_baru: str) -> None:
        if atraksi_baru.strip():
            self.__jenis_atraksi = atraksi_baru.strip()

    def get_pemandu_lokal(self) -> str:
        return self.__pemandu_lokal

    def set_pemandu_lokal(self, pemandu_baru: str) -> None:
        if pemandu_baru.strip():
            self.__pemandu_lokal = pemandu_baru.strip()

    # ==================== METHOD TAMBAHAN & OVERRIDING ====================
    def get_kategori(self) -> str:
        """Override method kategori dari superclass."""
        return "Wisata Budaya"

    def info_etika_kunjungan(self) -> str:
        """Memberikan panduan etika kunjungan di lokasi budaya."""
        return f"Gunakan pakaian sopan dan ikuti arahan pemandu lokal ({self.__pemandu_lokal})."

    def hitung_biaya_total(self, jumlah_orang: int = 1) -> int:
        """
        Override perhitungan biaya:
        Wisata budaya menambahkan donasi pelestarian budaya Rp 15.000 per orang.
        """
        donasi_budaya = 15000
        return (self.get_harga() + donasi_budaya) * jumlah_orang

    def tampilkan_info(self) -> str:
        """Override method tampilkan_info untuk menampilkan detail khusus WisataBudaya."""
        info_dasar = super().tampilkan_info()
        return (
            f"{info_dasar}\n"
            f"Daerah      : {self.__daerah_budaya}\n"
            f"Atraksi     : {self.__jenis_atraksi}\n"
            f"Pemandu     : {self.__pemandu_lokal}\n"
            f"Etika       : {self.info_etika_kunjungan()}\n"
            f"Total/Orang : Rp {self.hitung_biaya_total(1):,} (termasuk donasi budaya Rp 15,000)"
        )