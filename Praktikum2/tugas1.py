#============================================================
#Praktikum 2: Konsep file ADT dan file handling (Studi Kasus)
#Latihan Dasar 1: Membuat Fungsi Load Data
#============================================================

nama_file = "stok_barang.txt"

def baca_data(nama_file):
    data_dict = {} #inisialisasi data dictionary
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip() #ambil data per baris dan hilangkan new line
            kode, nama, jumlah = baris.split(",") #ambil data per item data
            data_dict[kode] = {"kode": kode, "nama": nama, "jumlah":int(jumlah)} #masukkan dalam 
    return data_dict

# buka_data = baca_data(nama_file)
# print("Jumlah data terbaca", len(buka_data))

#============================================================
#Praktikum 2: Konsep file ADT dan file handling (Studi Kasus)
#Latihan Dasar 2: Membuat Fungsi Menampilkan Data
#============================================================
def tampilkan_data(data_dict):
    #Membuat header tabel
    print("\n========= Daftar Barang =========")
    print(f"{"Kode":<10} | {"Nama":<12} | {"Jumlah":>5}")
    print("-"*35) #Membuat garis

    for kode in sorted(data_dict.keys()):
        nama = data_dict[kode]["nama"]
        jumlah = data_dict[kode]["jumlah"]
        print(f"{kode:<10} | {nama:<12} | {int(jumlah): >5}")

# tampilkan_data(buka_data) #Memanggil fungsi utk menampilkan data

#============================================================
#Praktikum 2: Konsep file ADT dan file handling (Studi Kasus)
#Latihan Dasar 3: Membuat fungsi mencari data
#============================================================

#Membuat fungsi pencarian data
def cari_data(data_dict):
    #Pencarian data berdasarkan kode barang sebagai key dictionary
    #Membuat input kode barang yang akan dicari
    kode_cari = input("Masukkan Kode Barang yang ingin dicari: ").strip().upper()

    if kode_cari in data_dict:
        nama = data_dict[kode_cari]["nama"]
        jumlah = data_dict[kode_cari]["jumlah"]

        print("====== Data Barang Ditemukan ======")
        print(f"NIM: {kode_cari}")
        print(f"Nama: {nama}")
        print(f"Jumlah: {jumlah}")
    
    else:
        print("Data tidak ditemukan. Pastikan Kode yang dimasukkan benar!")

# cari_data(buka_data)

#============================================================
#Praktikum 2: Konsep file ADT dan file handling (Studi Kasus)
#Latihan Dasar 4: Membuat fungsi mengubah data
#============================================================

#Membuat fungsi update data
def ubah_data(data_dict):
    #Awali dulu dengan mencari nim/data mahasiswa yang ingin diupdate
    kode = input("Masukkan Kode barang yang ingin diubah datanya: ").strip().upper()

    if kode not in data_dict:
        print("Kode barang tidak ditemukan. Update dibatalkan")
        return
    
    try:
        jumlah_baru = int(input("Masukkan Jumlah barang yang baru > 0: "))
    except ValueError:
        print("Jumlah barang harus berupa angka. Update dibatalkan")
    
    if jumlah_baru < 0:
        print("Jumlah barang harus lebih atau sama dengan 0. Update dibatalkan")

    jumlah_lama =  data_dict[kode]["jumlah"]
    data_dict[kode]["jumlah"] = jumlah_baru

    print(f"Update berhasil. Nilai {kode} berubah dari {jumlah_lama} menjadi {jumlah_baru}")

# ubah_data(buka_data)

#============================================================
#Praktikum 2: Konsep file ADT dan file handling (Studi Kasus)
#Latihan Dasar 5: Membuat fungsi menyimpan data pada file
#============================================================

#Membuat fungsi menyimpan data ke file
def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for kode in sorted(data_dict.keys()):
            nama = data_dict[kode]["nama"]
            jumlah = data_dict[kode]["jumlah"]
            file.write(f"{kode},{nama},{jumlah}\n")

#Memanggil fungsi simpan data
# simpan_data(nama_file, buka_data)
# print("\n Data berhasil Disimpan ke file: ", nama_file)

def tambah_data(data_dict):
    kode= input("Masukkan Kode barang yang ingin ditambahkan: ").strip().upper()
    if kode in data_dict:
        print("Kode barang sudah ada. Penambahan data dibatalkan")
        return
    
    try:
        nama_baru = input("Masukkan nama barang yang baru: ")
        jumlah_baru = int(input("Masukkan Jumlah barang yang baru > 0: "))
    except ValueError:
        print("Jumlah barang harus berupa angka. Penambahan data dibatalkan")
    
    if jumlah_baru < 0:
        print("Jumlah barang harus lebih atau sama dengan 0. Update dibatalkan")
    
    data_dict[kode] = {
        "kode": kode,
        "nama": nama_baru,
        "jumlah": jumlah_baru
    }

    print(f"Penambahan data berhasil.")


#============================================================
#Praktikum 2: Konsep file ADT dan file handling (Studi Kasus)
#Latihan Dasar 6: Membuat Menu
#============================================================

def main():
    #Load data otomatis saat program dimulai
    buka_data = baca_data(nama_file)

    while True:
        print("\n================ MENU =================")
        print("1. Tampilkan data stok barang")
        print("2. Cari data stok barang berdasarkan Kode")
        print("3. Ubah jumlah stok barang")
        print("4. Simpan data ke file")
        print("5. Tambah data stok barang")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()
        if pilihan == "1":
            tampilkan_data(buka_data)
        
        elif pilihan == "2":
            cari_data(buka_data)
            
        elif pilihan == "3":
            ubah_data(buka_data)

        elif pilihan == "4":
            simpan_data(nama_file, buka_data)
            print("Data berhasil disimpan")
        
        elif pilihan == "5":
            tambah_data(buka_data)

        elif pilihan == "0":
            print("Program selesai")
            break

        else:
            print("Pilihan tidak valid. Silahkan coba lagi!")
    
if __name__== "__main__":
    main()
