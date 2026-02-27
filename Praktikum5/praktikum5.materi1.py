# ========================================================== 
# Contoh Rekursi 1: Faktorial 
# ========================================================== 
def faktorial(n): #Fungsi utk faktorial
# Base case: berhenti ketika n = 0 
    if n == 0: #Jika 0! maka hasilnya akan 1
        return 1 
    # Recursive case: masalah diperkecil menjadi faktorial(n-1) 
    return n * faktorial(n - 1) #Jika angka bukan 0! maka akan mengalikan angka tersebut dengan angka-1 hingga angka tersebut 0 (namun jika angka tsb 0 maka akan menjadi 1)
print(faktorial(3))  #Gambaran jika di run akan seperti ini (3*2*1). Saat dia mencapai angka 0 maka angka tsb menjadi 1 maka hasilnya tidak akan 0.