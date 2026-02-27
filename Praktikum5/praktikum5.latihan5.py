# ==========================================================
# Studi Kasus: Generator PIN
# ==========================================================

def buat_pin(panjang, hasil=""):
    # Base case: jika panjang PIN sudah sesuai
    if len(hasil) == panjang: # Jika panjang hasil sama dengan panjang maka akan memberhentikan rekursif dan mencentak angka tersebut.
        print("PIN:", hasil)
        return
    
    # Pilihan angka yang boleh dipakai
    for angka in ["0", "1", "2"]: 
        # if angka not in hasil: #Kode disamping digunakan agar angka tidak berulang.
            buat_pin(panjang, hasil + angka) #Kode ini untuk meng isikan hasil dengan angka pada list. Karena alur program itu menjelajahi dari kiri ke kanan. Maka ia akan mencetak 000 dahulu kemudian 001, dan 002. Dan seterusnya.


buat_pin(3)