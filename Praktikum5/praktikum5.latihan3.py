# ==========================================================
# Latihan 3: Mencari Nilai Maksimum (Rekursi)
# ==========================================================

def cari_maks(data, index=0):
    # Base case: jika sudah di elemen terakhir
    if index == len(data) - 1: #Jika index sama dengan panjang data - 1, maka akan mencetak data[index] 
        return data[index]
    
    # Recursive case: cari maksimum dari sisa elemen
    maks_sisa = cari_maks(data, index + 1) #Ini recursive callnya untuk menambahkan indexnya berkali kali hingga index == len(data) - 1
    
    # Bandingkan elemen sekarang dengan maksimum sisa
    if data[index] > maks_sisa: #Kode ini utk cek jika data pada index tertentu lebih dari maks sisa maka akan mencetak data[index tersebut]. 
        return data[index]      #Jika digambarkan dia akan mencetak angka maksnya 3 dahulu (3 sebagai maks_sisa skrg), kemudian masuk index selanjutnya yaitu angka 7. angka 7 itu > 3 maka angka 7 akan menggantikan angka 3 utk menjadi maks_sisa. Lalu dilanjutkan terus hingga index == len(data) - 1. 
    else:
        return maks_sisa #Jika data pada index tersebut masih lebih kecil dari maks_sisa maka dia akan mencari angka di index selanjutnya (rekursif).


angka = [3, 7, 2, 9, 5] #Ini sebagai data
print("Nilai maksimum:", cari_maks(angka))