# ==========================================================
# Latihan 2: Tracing Rekursi
# ==========================================================

def countdown(n):
    #Base case: Jika n sama dengan 0 maka rekursif berhenti
    if n == 0:
        print("Selesai")
        return
    
    #Recursive case
    print("Masuk:", n) #Kode ini akan mencetak n
    countdown(n - 1) #Kode ini akan mengurangi n dengan angka 1 sehingga program akan mencetak angka 3, 2 , 1. Namun saat mencapai angka 0 program akan mengeluarkan output Selesai.
    print("Keluar:", n) #Lalu setelah ada output "Selesai". Kode ini dijalankan dengan mengambil nilai n yang terakhir kali dieksekusi (Last in first out). Maka akan mencetak 1, 2, 3.


countdown(3)