def selectionSort(data):
    for i in range(len(data)-1,0,-1):
        max = 0
        for lokasi in range(1, i+1):
            if data[lokasi] < data[max]:
                max = lokasi
        
        # Swap
        temp = data[i]
        data[i] = data[max]
        data[max] = temp

data = [54,26,93,17,77,31,44,55,20]
selectionSort(data)
print(data)