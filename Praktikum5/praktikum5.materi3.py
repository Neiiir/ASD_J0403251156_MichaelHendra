# ==========================================================
# Contoh Rekursi 3: Menjumlahkan Elemen List
# ==========================================================

def jumlah_list(data, index=0):
    # Base case: jika index sudah mencapai panjang list
    if index == len(data): #Jika index sama dengan panjang data (atau artinya datanya kosong) maka akan return 0 
        return 0
    
    # Recursive case: elemen sekarang + jumlah elemen setelahnya
    return data[index] + jumlah_list(data, index + 1) # Lalu kode ini akan mengambil angka pertama pada data(angka pada index ke 0) kemudian akan ditambahkan dengan angka dengan index 0 + 1 (atau angka kedua) dan akan terus ditambahkan hingga angka index terakhir di data.


print(jumlah_list([2, 4, 6, 8]))  # Output: 20 #Jika digambarkan akan seperti ini (data[0] + data[1] + data[2] + data[3]) maka hasilnya jadi 20