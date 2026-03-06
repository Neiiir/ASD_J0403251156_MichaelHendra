def insertionSort(data):
    for i in range (1, len(data)):
        currentvalue = data[i]
        posisi = i

        while posisi > 0 and data[posisi-1] < currentvalue:
            data[posisi] = data[posisi-1]
            posisi = posisi-1
        data[posisi] = currentvalue

data = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]
insertionSort(data)
print(data)
print("Top 5 Kandidat:")
for i in range(len(data)):
    if i < 5:
        print([i + 1], data[i])
#Soal:
#1. Jika Pak Budi akan meloloskan lima kandidat dengan nilai tertinggi, tuliskanlah skor lima kandidat tersebut dari yang paling tinggi hingga terendah.
#= [98, 89, 76, 68, 57]
#2. Kandidat berapa saja yang lolos