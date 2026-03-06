# =========================================================
# Contoh Rekursi 2: Tracing Masuk/Keluar
# =========================================================

def hitung(n):
    # Base case
    if n == 0:
        print("Selesai")
        return

    print("Masuk:", n)     # fase stacking (disini program akan memanggil angka yang diinput dari hitung())
    hitung(n - 1)          # pemanggilan rekursif (setelah itu angka akan dikurangi 1 hingga mencapai 0 dan jika sudah sampai 0 maka akan print "Selesai")
    print("Keluar:", n)    # fase unwinding (setelah kode diatas dieksekusi, baru kode ini yang dieksekusi, 
                            # dan yang dipanggil adalah angka 1 (karena ini angka terakhir sebelum print("Selesai").))

hitung(3)