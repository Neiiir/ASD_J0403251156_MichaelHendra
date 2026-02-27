# ==========================================================
# Contoh Backtracking 2:
# Kombinasi Biner dengan Batas '1' (Pruning)
# ==========================================================

def biner_batas(n, batas, hasil="", jumlah_1=0):
    # Pruning: jika jumlah_1 sudah melewati batas, berhenti
    if jumlah_1 > batas: #Jika jumlah1 sudah lebih dari batas maka dia akan berhenti mencetak 1 dan akan lanjut ke angka 0.
        return
    
    # Base case: jika panjang string sudah n
    if len(hasil) == n:  #Jika panjang hasil sudah mencapai n (angkanya sudah ada 4 maka hasil akan dicetak dan rekursif akan berhenti)
        print(hasil)
        return
    
    # Pilih '0'
    biner_batas(n, batas, hasil + "0", jumlah_1) #Pertama kode ini akan menggunakan angka 0 dulu karna kodenya yang berada di atas dari 1. jadi jika digambarkan akan jadi 0 + 0 + 0 + 0 jadi "0000"
    
    # Pilih '1'
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1) #Kedua jika semua 0 akan dipakai maka akan menggunakan angka 1. Jadi 0001, 0010, 0011, 0100, 0101, 1000. 
    #dia tidak mencetak angka 0111 karna batas penggunaan 1 hanya bisa 2x karna batasnya 2.


biner_batas(4, 2) #Kode ini utk menentukan seberapa banyak kombinasi angka dan juga batas.
#Batas ini utk membatasi penggunaan 1, jika penggunaan angka 1 > batas maka akan berhenti dan lanjut menggunakan angka 0.