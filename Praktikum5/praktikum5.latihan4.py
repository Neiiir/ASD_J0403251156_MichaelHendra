# ==========================================================
# Latihan 4: Kombinasi Huruf
# ==========================================================

def kombinasi(n, hasil=""):
    # Base case: jika panjang hasil sudah n
    if len(hasil) == n: #Jika panjang hasil sudah sama dengan n maka akan mencetak hasil 
        print(hasil)
        return
    
    # Tambah huruf A
    kombinasi(n, hasil + "A") 
    

    # Tambah huruf B
    kombinasi(n, hasil + "B")


kombinasi(2) #Ini untuk menentukan seberapa banyak kombinasinya.