# ==========================================================
# Latihan 1: Rekursi Pangkat
# ==========================================================

def pangkat(a, n):
    # Base case: Jika n sama dengan 0
    if n == 0: #Jika n = 0 maka akan cetak 1 (atau lebih mudahnya jika pangkat 0 maka hasilnya 1)
        return 1
    
    # Recursive case: Angka akan dikalikan dengan angka itu sendiri yang dikalikan dengan n -1. Contoh: n - 1 (a * (a * n-1))
    return a * pangkat(a, n - 1) #a itu akan dikalikan dengan a yang sudah dikalikan dengan pangkat n-1. Jika digambarkan mungkin akan menjadi 2 * (2*2) * (2*1) = jadi hasilnya 16


print(pangkat(2, 3))  # Output: 16