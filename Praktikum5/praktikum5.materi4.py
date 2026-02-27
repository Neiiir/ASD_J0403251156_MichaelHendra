# ==========================================================
# Contoh Backtracking 1: Kombinasi Biner (n)
# ==========================================================

def biner(n, hasil=""):
    # Base case: jika panjang string sudah n, cetak hasil
    if len(hasil) == n: #Jika panjang hasil sama dengan n (artinya jika kombinasi sudah mencapai 3 angka maka akan diprint hasilnya dan rekursif selesai.)
        print(hasil)
        return
    
    # Choose + Explore: tambah '0'
    biner(n, hasil + "0") #Kode ini akan mencetak angka 0 sebanyak 3x atau 0+0+0 sehingga jadi "000". Lalu setelah selesai dia akan lanjut ke 1
    
    # Choose + Explore: tambah '1'
    biner(n, hasil + "1") #Setelah dari 000 dia akan mencoba 1 dan menjadi 001, kemudian ke 011. Nah setelah kombinasi dengan 0 habis ia akan memulai dengan 1.
                        # Dari 100 lanjut ke 101, 110 kemudian 111. 


biner(3) #Kode ini utk menentukan seberapa banyak kombinasi angkanya biner(3 ) berarti ada 3 angka yang bisa dikombinasikan