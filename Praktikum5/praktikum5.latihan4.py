# ==========================================================
# Latihan 4: Kombinasi Huruf
# ==========================================================

def kombinasi(n, hasil=""):
    # Base case: jika panjang hasil sudah n
    if len(hasil) == n: #Jika panjang hasil sudah sama dengan n maka akan mencetak hasil. 
        print(hasil)
        return
    
    # Tambah huruf A
    kombinasi(n, hasil + "A") #Pada kode ini dia akan mencetak A dahulu menjadi "AA". Kemudian akan lanjut menggunakan B menjadi "AB" dan "BA"
    

    # Tambah huruf B
    kombinasi(n, hasil + "B") #Kemudian akan lanjut menggunakan B menjadi "AB", "BA", "BB".

    #Mengapa kombinasi tersebut dapat terjadi? Karena program akan menjelajahi dari kiri ke kanan. Oleh karena itu AA, AB, BA, dan BB. Setelah A selesai Baru ia lanjut ke B. Jadi tetap yang diutamakan adalah kode yang diatasnya.

kombinasi(2) #Ini untuk menentukan seberapa banyak kombinasinya.