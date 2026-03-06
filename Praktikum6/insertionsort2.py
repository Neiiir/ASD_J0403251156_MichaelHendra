def insertionSort(data):
    for i in range (1, len(data)):
        currentvalue = data[i]
        posisi = i

        while posisi > 0 and data[posisi-1] < currentvalue:
            data[posisi] = data[posisi-1]
            posisi = posisi-1
        data[posisi] = currentvalue

data = [54,26,93,17,77,31,44,55,20]
insertionSort(data)
print(data)