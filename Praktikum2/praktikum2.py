#============================================================
#Praktikum 2: Konsep file ADT dan file handling (Studi Kasus)
#Latihan Dasar 1: Membuat Fungsi Load Data
#============================================================

nama_file = "data_mahasiswa.txt"

def baca_data(nama_file):
    data_dict = {} #inisialisasi data dictionary
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip() #ambil data per baris dan hilangkan new line
            nim, nama, nilai = baris.split(",") #ambil data per item data
            data_dict[nim] = {"nama": nama, "nim": nim, "nilai":int(nilai)} #masukkan dalam 
    return data_dict

# buka_data = baca_data(nama_file)
# print("Jumlah data terbaca", len(buka_data))

#============================================================
#Praktikum 2: Konsep file ADT dan file handling (Studi Kasus)
#Latihan Dasar 2: Membuat Fungsi Menampilkan Data
#============================================================
def tampilkan_data(data_dict):
    #Membuat header tabel
    print("\n========= Daftar Mahasiswa ========")
    print(f"{'NIM':<10} | {"Nama":<12} | {"Nilai":>5}")
    print("-"*35) #Membuat garis

    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim:<10} | {nama:<12} | {int(nilai): >5}")

# tampilkan_data(buka_data) #Memanggil fungsi utk menampilkan data

#============================================================
#Praktikum 2: Konsep file ADT dan file handling (Studi Kasus)
#Latihan Dasar 3: Membuat fungsi mencari data
#============================================================

#Membuat fungsi pencarian data
def cari_data(data_dict):
    #Pencarian data berdasarkan nim sebagai key dictionary
    #Membuat input nim mahasiswa yang akan dicari
    nim_cari = input("Masukkan NIM mahasiswa yang ingin dicari: ").strip()

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("====== Data Mahasiswa Ditemukan ======")
        print(f"NIM: {nim_cari}")
        print(f"Nama: {nama}")
        print(f"Nilai: {nilai}")
    
    else:
        print("Data tidak ditemukan. Pastikan NIM yang dimasukkan benar!")

# cari_data(buka_data)

#============================================================
#Praktikum 2: Konsep file ADT dan file handling (Studi Kasus)
#Latihan Dasar 4: Membuat fungsi mengubah data
#============================================================

#Membuat fungsi update data
def ubah_data(data_dict):
    #Awali dulu dengan mencari nim/data mahasiswa yang ingin diupdate
    nim = input("Masukkan NIM mahasiswa yang ingin diubah datanya: ").strip()

    if nim not in data_dict:
        print("NIM tidak ditemukan. Update dibatalkan")
        return
    
    try:
        nilai_baru = int(input("Masukkan nilai yang baru 0-100: "))
    except ValueError:
        print("Nilai harus berupa angka. Update dibatalkan")
    
    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara 0 sampai 100. Update dibatalkan")


    nilai_lama =  data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru

    print(f"Update berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")

# ubah_data(buka_data)

#============================================================
#Praktikum 2: Konsep file ADT dan file handling (Studi Kasus)
#Latihan Dasar 5: Membuat fungsi menyimpan data pada file
#============================================================

#Membuat fungsi menyimpan data ke file
def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}")

#Memanggil fungsi simpan data
# simpan_data(nama_file, buka_data)
# print("\n Data berhasil Disimpan ke file: ", nama_file)

#============================================================
#Praktikum 2: Konsep file ADT dan file handling (Studi Kasus)
#Latihan Dasar 6: Membuat Menu
#============================================================

def main():
    #Load data otomatis saat program dimulai
    buka_data = baca_data(nama_file)

    while True:
        print("\n==== MENU ====")
        print("1. Tampilkan data mahasiswa")
        print("2. Cari data mahasiswa berdasarkan NIM")
        print("3. Ubah nilai mahasiswa")
        print("4. Simpan data ke file")
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

        elif pilihan == "0":
            print("Program selesai")
            break

        else:
            print("Pilihan tidak valid. Silahkan coba lagi!")
    
main()
# if __name__
