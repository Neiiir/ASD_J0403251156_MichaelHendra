#==============================================
#Praktikum 1: Konsep file ADT dan file handling
#Latihan Dasar 1: Membaca seluruh isi file data
#==============================================

print("=== Membuka file dalam satu string ===")
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = print(file.read())
print(isi_file)
print("=== Hasil Read ===")
print("Tipe data: ", type(isi_file))

print("=== Membuka file per baris ===")
jumlah_baris = 0 #untuk inisialisasi variabel utk menghitung jumlah baris
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip() #menghilangkan karakter baris baru
        print("Baris ke- ", jumlah_baris)
        print("Isinya: ", baris)

data_list = [] #inisialisasi list utk menampung data
#Parsing baris menjadi data satuan dan menampilkannya dalam bentuk kolom-kolom data
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter baris baru
        nim, nama, nilai = baris.split(",") #pecah menjadi data satuan
        print("NIM: ", nim, "| Nama: ", nama, "| Nilai: ", nilai)
        data_list.append([nim,nama,int(nilai)])

print("=== Menampilkan list ===")
print(data_list)
print("Contoh record ke 1:", data_list[0])
print("Contoh record ke 2:", data_list[1])
print("Jumlah record", len(data_list))

#==========================================================================
#Praktikum 1: Konsep file ADT dan file handling
#Latihan Dasar 4: Membaca data dan menyimpannya ke Struktur Data Dictionary
#==========================================================================
data_dict = {}

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter baris baru
        nim, nama, nilai = baris.split(",") #pecah menjadi data satuan
        data_dict[nim] = {
            "nama": nama,
            "nilai": int(nilai)
        }
print("=== Menampilkan data dictionary ===")
print(data_dict)