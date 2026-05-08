# ==============================================================================
# UJIAN TENGAH PRAKTIKUM - ALGORITMA & STRUKTUR DATA (TPL2106)
# Nama    : Michael Hendra
# NIM     : J0403251156
# Kelas   : TPL 1B
# ==============================================================================

import os  # Digunakan untuk membentuk path absolut file buku.txt

# ==============================================================================
# BAGIAN 1: FILE HANDLING & DICTIONARY (Bobot 20%)
# ==============================================================================

def muat_data_buku(nama_file):
    """
    Fungsi untuk membaca file 'buku.txt' dan menyimpannya ke dalam Dictionary.

    Format setiap baris dalam file:
        kode_buku,judul,harga

    Struktur Dictionary yang dihasilkan:
        Key   : kode_buku (string)
        Value : dictionary berisi 'judul' (string) dan 'harga' (integer)

    Menggunakan encoding 'utf-8-sig' untuk menangani file yang disimpan
    dengan Notepad Windows (yang menambahkan BOM di awal file).

    Parameter:
        nama_file (str): Path absolut file teks yang akan dibaca.

    Return:
        database_buku (dict): Dictionary berisi seluruh data buku dari file.
    """
    database_buku = {}  # Inisialisasi dictionary kosong

    try:
        with open(nama_file, "r", encoding="utf-8-sig") as file:
            # utf-8-sig otomatis menghapus BOM (Byte Order Mark)
            # yang muncul saat file disimpan via Notepad Windows
            for nomor_baris, baris in enumerate(file, start=1):
                baris = baris.strip()  # Hapus spasi/newline di awal dan akhir baris

                # Lewati baris kosong
                if not baris:
                    continue

                # Lewati baris header jika ada (misal: "kode_buku,judul,harga")
                if baris.lower().startswith("kode"):
                    continue

                # Pisahkan nilai berdasarkan koma, strip spasi tiap nilai
                bagian = [b.strip() for b in baris.split(",")]

                # Pastikan baris memiliki tepat 3 kolom
                if len(bagian) != 3:
                    print(f"  [PERINGATAN] Baris {nomor_baris} dilewati (format salah): '{baris}'")
                    continue

                kode, judul, harga = bagian

                # Validasi: harga harus berupa angka bulat positif
                if not harga.isdigit():
                    print(f"  [PERINGATAN] Baris {nomor_baris} dilewati (harga bukan angka): '{baris}'")
                    continue

                # Simpan ke dictionary dengan kode_buku sebagai key
                database_buku[kode] = {
                    "judul": judul,
                    "harga": int(harga)
                }

    except FileNotFoundError:
        print(f"  [ERROR] File tidak ditemukan: {nama_file}")
        print("  Pastikan file 'buku.txt' ada di folder yang sama dengan program ini.")
    except Exception as e:
        print(f"  [ERROR] Gagal membaca file: {e}")

    return database_buku


# ==============================================================================
# BAGIAN 2: LINKED LIST - MANAJEMEN PROMOSI (Bobot 30%)
# ==============================================================================

class Node:
    """
    Kelas Node untuk Single Linked List.

    Setiap Node menyimpan:
        - kode  : kode buku yang sedang dipromosikan
        - judul : judul buku yang sedang dipromosikan
        - next  : pointer/referensi ke Node berikutnya dalam list
    """
    def __init__(self, kode, judul):
        self.kode  = kode   # Kode buku (key dari katalog)
        self.judul = judul  # Judul buku
        self.next  = None   # Pointer ke node berikutnya (default: None)


class LinkedListPromosi:
    """
    Kelas Single Linked List untuk mengelola daftar buku promosi.

    Linked List adalah struktur data linier di mana setiap elemen (node)
    terhubung ke elemen berikutnya melalui pointer. Operasi dilakukan
    dari head (kepala) list.

    Hanya buku yang terdaftar di katalog (data_buku) yang dapat dipromosikan.
    Input dilakukan melalui kode buku.

    Atribut:
        head (Node): Node pertama dalam linked list.
    """
    def __init__(self):
        self.head = None  # List dimulai kosong

    def sudah_ada(self, kode):
        """
        Mengecek apakah buku dengan kode tertentu sudah ada di daftar promosi.

        Parameter:
            kode (str): Kode buku yang akan dicek.

        Return:
            bool: True jika sudah ada, False jika belum.
        """
        current = self.head
        while current:
            if current.kode == kode:
                return True
            current = current.next
        return False

    def tambah_buku_promosi(self, kode, data_buku):
        """
        Menambahkan buku ke bagian AKHIR linked list berdasarkan kode buku.

        Validasi:
            - Kode harus terdaftar di katalog (data_buku).
            - Buku yang sama tidak bisa ditambahkan dua kali.

        Langkah:
            1. Cek apakah kode ada di katalog.
            2. Cek apakah buku belum ada di daftar promosi.
            3. Buat node baru dan sambungkan ke akhir list.

        Parameter:
            kode      (str) : Kode buku yang akan dipromosikan.
            data_buku (dict): Dictionary katalog buku sebagai referensi validasi.
        """
        if kode not in data_buku:
            print(f"  [ERROR] Kode '{kode}' tidak ditemukan dalam katalog.")
            return

        if self.sudah_ada(kode):
            print(f"  [INFO] Buku '{data_buku[kode]['judul']}' sudah ada di daftar promosi.")
            return

        judul     = data_buku[kode]["judul"]
        node_baru = Node(kode, judul)

        if self.head is None:
            self.head = node_baru
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node_baru

        print(f"  Buku '[{kode}] {judul}' berhasil ditambahkan ke daftar promosi.")

    def tampilkan_promosi(self):
        """
        Menampilkan seluruh daftar buku yang sedang dipromosikan.

        Melakukan traversal dari head hingga akhir list,
        mencetak kode dan judul buku pada setiap node.
        """
        current = self.head

        if current is None:
            print("  Belum ada buku dalam daftar promosi.")
            return

        print("\n  === Daftar Buku Promosi ===")
        print(f"  {'No.':<5} {'Kode':<8} {'Judul'}")
        print("  " + "-" * 40)
        nomor = 1
        while current:
            print(f"  {nomor:<5} {current.kode:<8} {current.judul}")
            current = current.next
            nomor += 1

# ==============================================================================
# BAGIAN 3: QUEUE - ANTREAN KASIR (Bobot 20%)
# ==============================================================================

class AntreanKasir:
    """
    Kelas Queue (Antrean) untuk mensimulasikan antrean pelanggan di kasir.

    Queue menggunakan prinsip FIFO (First In, First Out):
        - Pelanggan yang pertama masuk akan dilayani pertama kali.
        - Penambahan dilakukan di bagian belakang (enqueue).
        - Pengambilan dilakukan dari bagian depan (dequeue).

    Setiap entri antrean menyimpan:
        - nama pelanggan
        - kode buku yang dibeli
        - jumlah buku yang dibeli
        - total harga transaksi

    Implementasi menggunakan List Python sebagai wadah antrean.
    """
    def __init__(self):
        self.antrean = []  # List kosong sebagai wadah antrean pelanggan

    def tambah_antrean(self, nama_pelanggan, kode_buku, jumlah, harga_satuan):
        """
        Menambahkan pelanggan baru ke BELAKANG antrean (Enqueue).

        Setiap pelanggan menyimpan informasi transaksi:
            nama, kode buku, jumlah, dan total harga.

        Parameter:
            nama_pelanggan (str): Nama pelanggan.
            kode_buku      (str): Kode buku yang dibeli.
            jumlah         (int): Jumlah buku yang dibeli.
            harga_satuan   (int): Harga per buku dari katalog.
        """
        total_harga = harga_satuan * jumlah  # Hitung total harga transaksi

        data_pelanggan = {
            "nama"        : nama_pelanggan,
            "kode_buku"   : kode_buku,
            "jumlah"      : jumlah,
            "total_harga" : total_harga
        }

        self.antrean.append(data_pelanggan)
        posisi = len(self.antrean)
        print(f"  {nama_pelanggan} masuk ke antrean (Posisi #{posisi}).")
        print(f"  Buku : {kode_buku} x{jumlah} = Rp {total_harga:,}")

    def layani_pelanggan(self, riwayat_transaksi):
        """
        Melayani dan mengeluarkan pelanggan pertama dari antrean (Dequeue).

        Setelah dilayani, total harga transaksi pelanggan tersebut
        ditambahkan ke riwayat_transaksi untuk keperluan laporan penjualan.

        Menggunakan method .pop(0) sesuai prinsip FIFO.

        Parameter:
            riwayat_transaksi (list): List tempat menyimpan total harga
                                      transaksi yang sudah selesai dilayani.
        """
        if len(self.antrean) == 0:
            print("  [INFO] Antrean sedang kosong. Tidak ada pelanggan.")
        else:
            pelanggan = self.antrean.pop(0)  # Ambil pelanggan pertama (FIFO)

            print(f"  Melayani pelanggan : {pelanggan['nama']}")
            print(f"  Buku dibeli        : {pelanggan['kode_buku']} x{pelanggan['jumlah']}")
            print(f"  Total Pembayaran   : Rp {pelanggan['total_harga']:,}")

            # Catat total harga ke riwayat transaksi untuk laporan penjualan
            riwayat_transaksi.append(pelanggan["total_harga"])
            print(f"  [INFO] Transaksi Rp {pelanggan['total_harga']:,} dicatat ke laporan penjualan.")

            if self.antrean:
                nama_sisa = [p["nama"] for p in self.antrean]
                print(f"  Sisa antrean: {', '.join(nama_sisa)}")
            else:
                print("  Antrean kini kosong.")

# ==============================================================================
# BAGIAN 4: SORTING - LAPORAN PENJUALAN (Bobot 30%)
# ==============================================================================

def urutkan_transaksi(list_harga):
    """
    Mengurutkan list harga transaksi dari TERKECIL ke TERBESAR
    menggunakan algoritma INSERTION SORT secara manual.

    Cara Kerja Insertion Sort:
        - Dimulai dari elemen indeks ke-1.
        - Setiap elemen dibandingkan dengan elemen-elemen di sebelah kirinya.
        - Elemen digeser ke kanan selama lebih besar dari elemen saat ini (key).
        - Proses ini membentuk bagian kiri list yang selalu sudah terurut.
        - Tidak menggunakan fungsi bawaan .sort() atau sorted().

    Kompleksitas Waktu:
        - Best Case  : O(n)   — data sudah terurut
        - Worst Case : O(n^2) — data terurut terbalik

    Parameter:
        list_harga (list): List berisi nilai harga transaksi (integer).

    Return:
        list_harga (list): List yang sudah diurutkan secara ascending.
    """
    for i in range(1, len(list_harga)):
        key = list_harga[i]  # elemen yang sedang akan disisipkan
        j   = i - 1          # Indeks elemen terakhir pada bagian yang sudah terurut

        # Geser elemen yang lebih besar dari key ke posisi satu langkah ke kanan
        while j >= 0 and list_harga[j] > key:
            list_harga[j + 1] = list_harga[j]
            j -= 1

        # Sisipkan key ke posisi yang tepat
        list_harga[j + 1] = key

    return list_harga

# ==============================================================================
# MAIN PROGRAM - MENU ANTARMUKA UTAMA
# ==============================================================================

def main():
    """
    Fungsi utama yang menjalankan program Sistem Manajemen Toko Buku.

    Menginisialisasi semua struktur data dan menampilkan menu interaktif
    yang memungkinkan pengguna memilih fitur yang tersedia.
    """

    # --- Inisialisasi Semua Struktur Data ---
    # menggunakan path absolut agar buku.txt selalu dicari di folder yang sama
    file_db = os.path.join(os.path.dirname(os.path.abspath(__file__)), "buku.txt")

    data_buku         = muat_data_buku(file_db)  # Dictionary dari file
    list_promosi      = LinkedListPromosi()       # Linked List untuk promosi
    antrean_toko      = AntreanKasir()            # queue untuk antrean kasir
    riwayat_transaksi = []                        # Diisi otomatis dari layani_pelanggan

    # --- Loop Menu Utama ---
    while True:
        print("\n" + "=" * 40)
        print("   SISTEM MANAJEMEN TOKO BUKU")
        print("=" * 40)
        print("  1. Lihat Katalog Buku        (Dictionary / File Handling)")
        print("  2. Kelola Daftar Promosi     (Linked List)")
        print("  3. Kelola Antrean Kasir      (Queue)")
        print("  4. Laporan Penjualan Terurut (Sorting)")
        print("  5. Keluar")
        print("=" * 40)

        pilihan = input("  Pilih menu (1-5): ").strip()

        # ---- Menu 1: Katalog Buku ----
        if pilihan == '1':
            print("\n  === Katalog Buku ===")
            if not data_buku:
                print("  [INFO] Data buku kosong atau file tidak tersedia.")
            else:
                print(f"  {'Kode':<8} {'Judul':<30} {'Harga'}")
                print("  " + "-" * 50)
                for kode, info in data_buku.items():
                    print(f"  {kode:<8} {info['judul']:<30} Rp {info['harga']:,}")

        # ---- Menu 2: Linked List - Daftar Promosi ----
        elif pilihan == '2':
            print("\n  --- Sub-menu Daftar Promosi ---")
            print("  1. Tambah Buku ke Promosi")
            print("  2. Lihat Daftar Promosi")
            sub = input("  Pilih: ").strip()

            if sub == '1':
                if not data_buku:
                    print("  [INFO] Katalog kosong, tidak ada buku yang bisa dipromosikan.")
                else:
                    print("\n  Katalog tersedia:")
                    print(f"  {'Kode':<8} {'Judul':<30} {'Harga'}")
                    print("  " + "-" * 50)
                    for kode, info in data_buku.items():
                        print(f"  {kode:<8} {info['judul']:<30} Rp {info['harga']:,}")

                    kode_input = input("\n  Masukkan kode buku yang ingin dipromosikan: ").strip().upper()
                    list_promosi.tambah_buku_promosi(kode_input, data_buku)

            elif sub == '2':
                list_promosi.tampilkan_promosi()
            else:
                print("  [ERROR] Pilihan tidak valid.")

        # ---- Menu 3: Queue - Antrean Kasir ----
        elif pilihan == '3':
            print("\n  --- Sub-menu Antrean Kasir ---")
            print("  1. Tambah Pelanggan ke Antrean")
            print("  2. Layani Pelanggan (Dequeue)")
            sub = input("  Pilih: ").strip()

            if sub == '1':
                if not data_buku:
                    print("  [INFO] Katalog kosong, tidak dapat memproses pembelian.")
                else:
                    nama = input("  Nama Pelanggan: ").strip()
                    if not nama:
                        print("  [ERROR] Nama pelanggan tidak boleh kosong.")
                    else:
                        print("\n  Katalog Buku:")
                        print(f"  {'Kode':<8} {'Judul':<30} {'Harga'}")
                        print("  " + "-" * 50)
                        for kode, info in data_buku.items():
                            print(f"  {kode:<8} {info['judul']:<30} Rp {info['harga']:,}")

                        kode_beli = input("\n  Masukkan kode buku yang dibeli: ").strip().upper()
                        if kode_beli not in data_buku:
                            print(f"  [ERROR] Kode '{kode_beli}' tidak ditemukan dalam katalog.")
                        else:
                            jumlah_input = input("  Jumlah buku yang dibeli: ").strip()
                            if not jumlah_input.isdigit() or int(jumlah_input) < 1:
                                print("  [ERROR] Jumlah harus berupa angka positif.")
                            else:
                                jumlah       = int(jumlah_input)
                                harga_satuan = data_buku[kode_beli]["harga"]
                                antrean_toko.tambah_antrean(nama, kode_beli, jumlah, harga_satuan)

            elif sub == '2':
                antrean_toko.layani_pelanggan(riwayat_transaksi)
            else:
                print("  [ERROR] Pilihan tidak valid.")

        # ---- Menu 4: Sorting - Laporan Penjualan ----
        elif pilihan == '4':
            print("\n  === Laporan Penjualan ===")
            if not riwayat_transaksi:
                print("  [INFO] Belum ada transaksi yang selesai dilayani.")
                print("  Layani pelanggan di Menu 3 terlebih dahulu.")
            else:
                data_sort  = riwayat_transaksi[:]       # Salin agar data asli tidak berubah
                print(f"  Harga Sebelum Diurutkan : {data_sort}")

                hasil_sort = urutkan_transaksi(data_sort)  # Insertion Sort manual
                print(f"  Harga Sesudah Diurutkan : {hasil_sort}")
                print(f"  Transaksi Terendah      : Rp {hasil_sort[0]:,}")
                print(f"  Transaksi Tertinggi     : Rp {hasil_sort[-1]:,}")
                print(f"  Total Seluruh Transaksi : Rp {sum(hasil_sort):,}")
                print(f"  Jumlah Transaksi        : {len(hasil_sort)} transaksi")

        # ---- Menu 5: Keluar ----
        elif pilihan == '5':
            print("\n  Program selesai. Terima kasih!\n")
            break

        # ---- Input Tidak Valid ----
        else:
            print("  [ERROR] Pilihan tidak valid! Masukkan angka 1-5.")


# Entry point program
if __name__ == "__main__":
    main()