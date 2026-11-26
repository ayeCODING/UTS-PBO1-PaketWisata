# ==============================================================================
# File        : main.py
# Deskripsi   : Program utama berbasis CLI untuk Aplikasi Paket Wisata.
#               Menyediakan menu Tambah, Tampilkan, Cari, Ubah, Cek Status, Keluar.
# ==============================================================================

from paket_wisata import PaketWisata
from wisata_alam import WisataAlam
from wisata_budaya import WisataBudaya
from pelanggan import Pelanggan

# Penyimpanan data sementara di memori selama program berjalan
daftar_paket: list[PaketWisata] = []
daftar_pelanggan: list[Pelanggan] = []


def garis(karakter: str = "=", panjang: int = 60) -> None:
    """Mencetak garis pemisah agar tampilan CLI lebih rapi."""
    print(karakter * panjang)


def input_tidak_kosong(pesan: str) -> str:
    """Memastikan input teks dari pengguna tidak kosong."""
    while True:
        nilai = input(pesan).strip()
        if nilai:
            return nilai
        print("  [!] Input tidak boleh kosong. Silakan coba lagi.")


def input_angka(pesan: str, minimal: int = 0) -> int:
    """Memastikan input angka valid dan memenuhi batas minimal."""
    while True:
        try:
            nilai = int(input(pesan).strip())
            if nilai >= minimal:
                return nilai
            print(f"  [!] Nilai minimal adalah {minimal}.")
        except ValueError:
            print("  [!] Masukkan angka yang valid.")


def cari_paket_by_kode(kode: str) -> PaketWisata | None:
    """Mencari objek PaketWisata berdasarkan kode paket (case-insensitive)."""
    for paket in daftar_paket:
        if paket.get_kode_paket().lower() == kode.lower():
            return paket
    return None


def cari_pelanggan_by_id(id_pelanggan: str) -> Pelanggan | None:
    """Mencari objek Pelanggan berdasarkan ID pelanggan (case-insensitive)."""
    for plg in daftar_pelanggan:
        if plg.get_id_pelanggan().lower() == id_pelanggan.lower():
            return plg
    return None


# ==================== DATA AWAL (SAMPLE DATA) ====================
def inisialisasi_data_awal() -> None:
    """Membuat beberapa objek awal agar menu tampil/cari/ubah/status bisa langsung diuji."""
    # Membuat objek dari subclass WisataAlam dan WisataBudaya
    p1 = WisataAlam(
        "ALM01",
        "Jelajah Kawah Papandayan",
        450000,
        10,
        "Garut, Jawa Barat",
        "Sedang",
        "Jaket tebal, sepatu trekking",
    )
    p2 = WisataAlam(
        "ALM02",
        "Eksplorasi Green Canyon",
        600000,
        4,
        "Pangandaran, Jawa Barat",
        "Mudah",
        "Pakaian ganti, sandal gunung",
    )
    p3 = WisataBudaya(
        "BDY01",
        "Wisata Saung Angklung Udjo",
        250000,
        15,
        "Bandung, Jawa Barat",
        "Pertunjukan Angklung & Tari Tradisional",
        "Kang Dedi",
    )
    p4 = WisataBudaya(
        "BDY02",
        "Tur Sejarah Keraton Yogyakarta",
        550000,
        2,
        "DI Yogyakarta",
        "Tur Keraton & Sendratari Ramayana",
        "Pak Hendra",
    )
    daftar_paket.extend([p1, p2, p3, p4])

    # Membuat objek Pelanggan dan contoh relasi Association (memesan > 1 paket)
    c1 = Pelanggan("PLG01", "Andi Pratama", "081234567890")
    c1.pesan_paket(p1)
    c1.pesan_paket(p3)

    c2 = Pelanggan("PLG02", "Siti Rahmawati", "082345678901")
    daftar_pelanggan.extend([c1, c2])


# ==================== MENU 1: TAMBAH DATA ====================
def menu_tambah_data() -> None:
    """Menangani penambahan Paket Wisata Alam, Wisata Budaya, Pelanggan, dan Pemesanan."""
    garis()
    print("MENU TAMBAH DATA")
    garis("-")
    print("1. Tambah Paket Wisata Alam")
    print("2. Tambah Paket Wisata Budaya")
    print("3. Tambah Data Pelanggan")
    print("4. Buat Pemesanan Paket oleh Pelanggan (Relasi Association)")
    print("0. Kembali ke Menu Utama")

    pilihan = input("Pilih submenu (0-4): ").strip()

    if pilihan == "1":
        print("\n--- Tambah Paket Wisata Alam ---")
        kode = input_tidak_kosong("Kode Paket (misal ALM03) : ").upper()
        if cari_paket_by_kode(kode):
            print(f"  [!] Kode paket '{kode}' sudah terdaftar.")
            return
        nama = input_tidak_kosong("Nama Paket               : ")
        harga = input_angka("Harga Dasar (Rp)         : ", minimal=1)
        kuota = input_angka("Kuota Peserta            : ", minimal=0)
        lokasi = input_tidak_kosong("Lokasi Alam              : ")
        kesulitan = input_tidak_kosong("Tingkat Kesulitan (Mudah/Sedang/Sulit): ")
        peralatan = input_tidak_kosong("Peralatan Wajib          : ")

        paket_baru = WisataAlam(kode, nama, harga, kuota, lokasi, kesulitan, peralatan)
        daftar_paket.append(paket_baru)
        print(f"  [OK] Paket Wisata Alam '{nama}' berhasil ditambahkan!")

    elif pilihan == "2":
        print("\n--- Tambah Paket Wisata Budaya ---")
        kode = input_tidak_kosong("Kode Paket (misal BDY03) : ").upper()
        if cari_paket_by_kode(kode):
            print(f"  [!] Kode paket '{kode}' sudah terdaftar.")
            return
        nama = input_tidak_kosong("Nama Paket               : ")
        harga = input_angka("Harga Dasar (Rp)         : ", minimal=1)
        kuota = input_angka("Kuota Peserta            : ", minimal=0)
        daerah = input_tidak_kosong("Daerah Budaya            : ")
        atraksi = input_tidak_kosong("Jenis Atraksi            : ")
        pemandu = input_tidak_kosong("Nama Pemandu Lokal       : ")

        paket_baru = WisataBudaya(kode, nama, harga, kuota, daerah, atraksi, pemandu)
        daftar_paket.append(paket_baru)
        print(f"  [OK] Paket Wisata Budaya '{nama}' berhasil ditambahkan!")

    elif pilihan == "3":
        print("\n--- Tambah Data Pelanggan ---")
        id_plg = input_tidak_kosong("ID Pelanggan (misal PLG03): ").upper()
        if cari_pelanggan_by_id(id_plg):
            print(f"  [!] ID Pelanggan '{id_plg}' sudah terdaftar.")
            return
        nama = input_tidak_kosong("Nama Pelanggan            : ")
        telepon = input_tidak_kosong("No. Telepon               : ")

        pelanggan_baru = Pelanggan(id_plg, nama, telepon)
        daftar_pelanggan.append(pelanggan_baru)
        print(f"  [OK] Pelanggan '{nama}' berhasil ditambahkan!")

    elif pilihan == "4":
        print("\n--- Pemesanan Paket Wisata oleh Pelanggan ---")
        if not daftar_pelanggan or not daftar_paket:
            print("  [!] Pastikan data pelanggan dan paket wisata sudah tersedia.")
            return

        id_plg = input_tidak_kosong("Masukkan ID Pelanggan  : ")
        pelanggan = cari_pelanggan_by_id(id_plg)
        if not pelanggan:
            print(f"  [!] Pelanggan dengan ID '{id_plg}' tidak ditemukan.")
            return

        print("\nDaftar Paket Wisata Tersedia:")
        for p in daftar_paket:
            print(
                f"  - [{p.get_kode_paket()}] {p.get_nama_paket()} "
                f"({p.get_kategori()}) | Rp {p.hitung_biaya_total(1):,} | {p.cek_status()}"
            )

        kode_pkt = input_tidak_kosong("\nMasukkan Kode Paket    : ")
        paket = cari_paket_by_kode(kode_pkt)
        if not paket:
            print(f"  [!] Paket dengan kode '{kode_pkt}' tidak ditemukan.")
            return

        berhasil, pesan = pelanggan.pesan_paket(paket)
        simbol = "[OK]" if berhasil else "[!]"
        print(f"  {simbol} {pesan}")

    elif pilihan == "0":
        return
    else:
        print("  [!] Pilihan tidak valid.")


# ==================== MENU 2: TAMPILKAN DATA ====================
def menu_tampilkan_data() -> None:
    """Menampilkan seluruh data Paket Wisata atau data Pelanggan beserta pesanannya."""
    garis()
    print("MENU TAMPILKAN DATA")
    garis("-")
    print("1. Tampilkan Semua Paket Wisata")
    print("2. Tampilkan Semua Pelanggan & Pesanannya")
    print("0. Kembali ke Menu Utama")

    pilihan = input("Pilih submenu (0-2): ").strip()

    if pilihan == "1":
        print("\n=== DAFTAR SEMUA PAKET WISATA ===")
        if not daftar_paket:
            print("  Belum ada data paket wisata.")
            return
        for idx, paket in enumerate(daftar_paket, start=1):
            garis("-")
            print(f"Data Paket #{idx}")
            print(paket.tampilkan_info())

    elif pilihan == "2":
        print("\n=== DAFTAR PELANGGAN & PESANAN PAKET ===")
        if not daftar_pelanggan:
            print("  Belum ada data pelanggan.")
            return
        for idx, plg in enumerate(daftar_pelanggan, start=1):
            garis("-")
            print(f"Data Pelanggan #{idx}")
            print(plg.tampilkan_info())

    elif pilihan == "0":
        return
    else:
        print("  [!] Pilihan tidak valid.")


# ==================== MENU 3: CARI DATA ====================
def menu_cari_data() -> None:
    """Mencari Paket Wisata berdasarkan kode/nama atau Pelanggan berdasarkan ID/nama."""
    garis()
    print("MENU CARI DATA")
    garis("-")
    print("1. Cari Paket Wisata (Kode / Nama)")
    print("2. Cari Pelanggan (ID / Nama)")
    print("0. Kembali ke Menu Utama")

    pilihan = input("Pilih submenu (0-2): ").strip()

    if pilihan == "1":
        kata_kunci = input_tidak_kosong("Masukkan Kode atau Nama Paket: ").lower()
        hasil = [
            p
            for p in daftar_paket
            if kata_kunci in p.get_kode_paket().lower()
            or kata_kunci in p.get_nama_paket().lower()
        ]
        if not hasil:
            print("  [!] Paket wisata tidak ditemukan.")
        else:
            print(f"\nDitemukan {len(hasil)} paket wisata:")
            for p in hasil:
                garis("-")
                print(p.tampilkan_info())

    elif pilihan == "2":
        kata_kunci = input_tidak_kosong("Masukkan ID atau Nama Pelanggan: ").lower()
        hasil = [
            c
            for c in daftar_pelanggan
            if kata_kunci in c.get_id_pelanggan().lower()
            or kata_kunci in c.get_nama_pelanggan().lower()
        ]
        if not hasil:
            print("  [!] Pelanggan tidak ditemukan.")
        else:
            print(f"\nDitemukan {len(hasil)} pelanggan:")
            for c in hasil:
                garis("-")
                print(c.tampilkan_info())

    elif pilihan == "0":
        return
    else:
        print("  [!] Pilihan tidak valid.")


# ==================== MENU 4: UBAH DATA ====================
def menu_ubah_data() -> None:
    """Mengubah data Paket Wisata atau data Pelanggan menggunakan method Setter."""
    garis()
    print("MENU UBAH DATA")
    garis("-")
    print("1. Ubah Data Paket Wisata")
    print("2. Ubah Data Pelanggan")
    print("0. Kembali ke Menu Utama")

    pilihan = input("Pilih submenu (0-2): ").strip()

    if pilihan == "1":
        kode = input_tidak_kosong("Masukkan Kode Paket yang akan diubah: ")
        paket = cari_paket_by_kode(kode)
        if not paket:
            print(f"  [!] Paket dengan kode '{kode}' tidak ditemukan.")
            return

        print("\nData Paket Saat Ini:")
        print(paket.tampilkan_info())
        print("\n(Kosongkan input jika tidak ingin mengubah field tertentu)")

        nama_baru = input(f"Nama Baru [{paket.get_nama_paket()}]: ").strip()
        if nama_baru:
            paket.set_nama_paket(nama_baru)

        harga_input = input(f"Harga Baru [{paket.get_harga()}]: ").strip()
        if harga_input:
            try:
                if not paket.set_harga(int(harga_input)):
                    print("  [!] Harga harus lebih dari 0, perubahan harga dilewati.")
            except ValueError:
                print("  [!] Input harga bukan angka, perubahan harga dilewati.")

        kuota_input = input(f"Kuota Baru [{paket.get_kuota()}]: ").strip()
        if kuota_input:
            try:
                if not paket.set_kuota(int(kuota_input)):
                    print("  [!] Kuota tidak boleh negatif, perubahan kuota dilewati.")
            except ValueError:
                print("  [!] Input kuota bukan angka, perubahan kuota dilewati.")

        status_input = input("Status Aktif (y/n, kosongkan jika tetap): ").strip().lower()
        if status_input == "y":
            paket.set_aktif(True)
        elif status_input == "n":
            paket.set_aktif(False)

        # Ubah atribut khusus sesuai subclass-nya
        if isinstance(paket, WisataAlam):
            lokasi_baru = input(f"Lokasi Alam Baru [{paket.get_lokasi_alam()}]: ").strip()
            if lokasi_baru:
                paket.set_lokasi_alam(lokasi_baru)
            kesulitan_baru = input(
                f"Tingkat Kesulitan Baru [{paket.get_tingkat_kesulitan()}]: "
            ).strip()
            if kesulitan_baru:
                paket.set_tingkat_kesulitan(kesulitan_baru)
        elif isinstance(paket, WisataBudaya):
            daerah_baru = input(f"Daerah Budaya Baru [{paket.get_daerah_budaya()}]: ").strip()
            if daerah_baru:
                paket.set_daerah_budaya(daerah_baru)
            pemandu_baru = input(f"Pemandu Lokal Baru [{paket.get_pemandu_lokal()}]: ").strip()
            if pemandu_baru:
                paket.set_pemandu_lokal(pemandu_baru)

        print("  [OK] Data paket wisata berhasil diperbarui!")

    elif pilihan == "2":
        id_plg = input_tidak_kosong("Masukkan ID Pelanggan yang akan diubah: ")
        pelanggan = cari_pelanggan_by_id(id_plg)
        if not pelanggan:
            print(f"  [!] Pelanggan dengan ID '{id_plg}' tidak ditemukan.")
            return

        print("\nData Pelanggan Saat Ini:")
        print(pelanggan.tampilkan_info())
        print("\n(Kosongkan input jika tidak ingin mengubah field tertentu)")

        nama_baru = input(f"Nama Baru [{pelanggan.get_nama_pelanggan()}]: ").strip()
        if nama_baru:
            pelanggan.set_nama_pelanggan(nama_baru)

        telp_baru = input(f"No. Telepon Baru [{pelanggan.get_no_telepon()}]: ").strip()
        if telp_baru:
            pelanggan.set_no_telepon(telp_baru)

        print("  [OK] Data pelanggan berhasil diperbarui!")

    elif pilihan == "0":
        return
    else:
        print("  [!] Pilihan tidak valid.")


# ==================== MENU 5: CEK STATUS DATA ====================
def menu_cek_status_data() -> None:
    """Mengecek status ketersediaan seluruh Paket Wisata dan status pesanan Pelanggan."""
    garis()
    print("MENU CEK STATUS DATA")
    garis("-")
    print("1. Cek Status Ketersediaan Semua Paket Wisata")
    print("2. Cek Status Pesanan Semua Pelanggan")
    print("0. Kembali ke Menu Utama")

    pilihan = input("Pilih submenu (0-2): ").strip()

    if pilihan == "1":
        print("\n=== STATUS KETERSEDIAAN PAKET WISATA ===")
        if not daftar_paket:
            print("  Belum ada data paket wisata.")
            return
        for p in daftar_paket:
            print(
                f"  [{p.get_kode_paket()}] {p.get_nama_paket():<32} | "
                f"{p.get_kategori():<13} | Status: {p.cek_status()}"
            )

    elif pilihan == "2":
        print("\n=== STATUS PESANAN PELANGGAN ===")
        if not daftar_pelanggan:
            print("  Belum ada data pelanggan.")
            return
        for c in daftar_pelanggan:
            print(
                f"  [{c.get_id_pelanggan()}] {c.get_nama_pelanggan():<20} | "
                f"Status: {c.cek_status_pesanan()} | "
                f"Total Tagihan: Rp {c.hitung_total_pembayaran():,}"
            )

    elif pilihan == "0":
        return
    else:
        print("  [!] Pilihan tidak valid.")


# ==================== PROGRAM UTAMA (LOOP MENU) ====================
def main() -> None:
    """Fungsi utama untuk menjalankan siklus menu berbasis teks (CLI)."""
    inisialisasi_data_awal()

    while True:
        garis()
        print("      APLIKASI MANAJEMEN PAKET WISATA - BIRO PERJALANAN     ")
        garis()
        print("1. Tambah Data (Paket / Pelanggan / Pemesanan)")
        print("2. Tampilkan Data")
        print("3. Cari Data")
        print("4. Ubah Data")
        print("5. Cek Status Data")
        print("6. Keluar dari Program")
        garis("-")

        pilihan = input("Pilih menu (1-6): ").strip()

        if pilihan == "1":
            menu_tambah_data()
        elif pilihan == "2":
            menu_tampilkan_data()
        elif pilihan == "3":
            menu_cari_data()
        elif pilihan == "4":
            menu_ubah_data()
        elif pilihan == "5":
            menu_cek_status_data()
        elif pilihan == "6":
            garis()
            print("Terima kasih telah menggunakan Aplikasi Paket Wisata. Sampai jumpa!")
            garis()
            break
        else:
            print("  [!] Pilihan tidak valid. Silakan pilih angka 1 sampai 6.")


# Titik masuk utama program
if __name__ == "__main__":
    main()