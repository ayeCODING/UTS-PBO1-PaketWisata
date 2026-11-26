# ==============================================================================
# File        : wisata_alam.py
# Deskripsi   : Subclass WisataAlam yang mewarisi sifat dari PaketWisata.
# Konsep OOP  : Inheritance, super(), Encapsulation, Method Overriding
# ==============================================================================

from paket_wisata import PaketWisata


class WisataAlam(PaketWisata):
    """Subclass untuk paket wisata bertema alam (gunung, pantai, air terjun, dll)."""

    # Constructor berparameter yang memanggil constructor superclass dengan super()
    def __init__(
        self,
        kode_paket: str,
        nama_paket: str,
        harga: int,
        kuota: int,
        lokasi_alam: str,
        tingkat_kesulitan: str,
        peralatan_wajib: str,
        aktif: bool = True,
    ):
        # Memanggil constructor milik superclass PaketWisata
        super().__init__(kode_paket, nama_paket, harga, kuota, aktif)

        # 3 Atribut private khusus milik WisataAlam
        self.__lokasi_alam = lokasi_alam
        self.__tingkat_kesulitan = tingkat_kesulitan
        self.__peralatan_wajib = peralatan_wajib

    # ==================== GETTER & SETTER ====================
    def get_lokasi_alam(self) -> str:
        return self.__lokasi_alam

    def set_lokasi_alam(self, lokasi_baru: str) -> None:
        if lokasi_baru.strip():
            self.__lokasi_alam = lokasi_baru.strip()

    def get_tingkat_kesulitan(self) -> str:
        return self.__tingkat_kesulitan

    def set_tingkat_kesulitan(self, tingkat_baru: str) -> None:
        if tingkat_baru.strip():
            self.__tingkat_kesulitan = tingkat_baru.strip()

    def get_peralatan_wajib(self) -> str:
        return self.__peralatan_wajib

    def set_peralatan_wajib(self, peralatan_baru: str) -> None:
        if peralatan_baru.strip():
            self.__peralatan_wajib = peralatan_baru.strip()

    # ==================== METHOD TAMBAHAN & OVERRIDING ====================
    def get_kategori(self) -> str:
        """Override method kategori dari superclass."""
        return "Wisata Alam"

    def cek_rekomendasi_fisik(self) -> str:
        """Memberikan rekomendasi persiapan fisik berdasarkan tingkat kesulitan."""
        level = self.__tingkat_kesulitan.lower()
        if level == "sulit":
            return "Wajib fisik prima & berpengalaman trekking."
        elif level == "sedang":
            return "Disarankan pemanasan ringan & stamina cukup."
        return "Ramah pemula & cocok untuk keluarga."

    def hitung_biaya_total(self, jumlah_orang: int = 1) -> int:
        """
        Override perhitungan biaya:
        Wisata alam menambahkan biaya asuransi keselamatan Rp 25.000 per orang.
        """
        biaya_asuransi = 25000
        return (self.get_harga() + biaya_asuransi) * jumlah_orang

    def tampilkan_info(self) -> str:
        """Override method tampilkan_info untuk menampilkan detail khusus WisataAlam."""
        info_dasar = super().tampilkan_info()
        return (
            f"{info_dasar}\n"
            f"Lokasi Alam : {self.__lokasi_alam}\n"
            f"Kesulitan   : {self.__tingkat_kesulitan} ({self.cek_rekomendasi_fisik()})\n"
            f"Peralatan   : {self.__peralatan_wajib}\n"
            f"Total/Orang : Rp {self.hitung_biaya_total(1):,} (termasuk asuransi alam Rp 25,000)"
        )