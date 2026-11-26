# ==============================================================================
# File        : pelanggan.py
# Deskripsi   : Class Pelanggan yang berelasi (Association) dengan PaketWisata.
#               Satu Pelanggan dapat memesan satu atau lebih objek PaketWisata.
# Konsep OOP  : Association (One-to-Many), Encapsulation, Constructor
# ==============================================================================

from paket_wisata import PaketWisata


class Pelanggan:
    """Class Pelanggan yang memiliki relasi Association ke satu atau lebih PaketWisata."""

    # Constructor berparameter
    def __init__(self, id_pelanggan: str, nama_pelanggan: str, no_telepon: str):
        # 4 Atribut private
        self.__id_pelanggan = id_pelanggan
        self.__nama_pelanggan = nama_pelanggan
        self.__no_telepon = no_telepon
        # Relasi Association: list berisi objek-objek PaketWisata (WisataAlam / WisataBudaya)
        self.__daftar_paket: list[PaketWisata] = []

    # ==================== GETTER & SETTER ====================
    def get_id_pelanggan(self) -> str:
        return self.__id_pelanggan

    def get_nama_pelanggan(self) -> str:
        return self.__nama_pelanggan

    def set_nama_pelanggan(self, nama_baru: str) -> None:
        if nama_baru.strip():
            self.__nama_pelanggan = nama_baru.strip()

    def get_no_telepon(self) -> str:
        return self.__no_telepon

    def set_no_telepon(self, telepon_baru: str) -> None:
        if telepon_baru.strip():
            self.__no_telepon = telepon_baru.strip()

    def get_daftar_paket(self) -> list[PaketWisata]:
        """Mengembalikan salinan list paket wisata yang dipesan agar enkapsulasi terjaga."""
        return list(self.__daftar_paket)

    # ==================== METHOD TAMBAHAN ====================
    def pesan_paket(self, paket: PaketWisata) -> tuple[bool, str]:
        """
        Memesan satu objek PaketWisata.
        Memvalidasi ketersediaan kuota sebelum menambahkannya ke daftar pesanan pelanggan.
        """
        if not isinstance(paket, PaketWisata):
            return False, "Objek yang dipesan bukan merupakan PaketWisata yang valid."

        if not paket.is_aktif():
            return False, f"Paket '{paket.get_nama_paket()}' sedang nonaktif."

        if paket.kurangi_kuota(1):
            self.__daftar_paket.append(paket)
            return True, f"Berhasil memesan paket '{paket.get_nama_paket()}'."

        return False, f"Kuota paket '{paket.get_nama_paket()}' sudah habis."

    def hitung_total_pembayaran(self) -> int:
        """Menghitung total biaya seluruh paket wisata yang telah dipesan pelanggan."""
        total = 0
        for paket in self.__daftar_paket:
            total += paket.hitung_biaya_total(1)
        return total

    def cek_status_pesanan(self) -> str:
        """Mengecek status pemesanan pelanggan berdasarkan jumlah paket yang dipesan."""
        jumlah = len(self.__daftar_paket)
        if jumlah == 0:
            return "Belum Memesan Paket"
        elif jumlah == 1:
            return "Pesanan Aktif (1 Paket Wisata)"
        return f"Pelanggan Prioritas ({jumlah} Paket Wisata Dipesan)"

    def tampilkan_info(self) -> str:
        """Menampilkan detail pelanggan beserta daftar paket wisata yang dipesannya."""
        hasil = (
            f"ID Pelanggan   : {self.__id_pelanggan}\n"
            f"Nama Pelanggan : {self.__nama_pelanggan}\n"
            f"No. Telepon    : {self.__no_telepon}\n"
            f"Status Pesanan : {self.cek_status_pesanan()}\n"
            f"Daftar Pesanan :"
        )

        if not self.__daftar_paket:
            hasil += "\n  (Belum ada paket wisata yang dipesan)"
        else:
            for idx, paket in enumerate(self.__daftar_paket, start=1):
                hasil += (
                    f"\n  {idx}. [{paket.get_kode_paket()}] {paket.get_nama_paket()} "
                    f"({paket.get_kategori()}) - Rp {paket.hitung_biaya_total(1):,}"
                )
            hasil += f"\nTotal Tagihan  : Rp {self.hitung_total_pembayaran():,}"

        return hasil