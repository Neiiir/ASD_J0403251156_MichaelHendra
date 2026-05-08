def insertionsort(data):
    for i in range(1, len(data)):
        currentValue = data[i]
        posisi = i

        while posisi > 0 and data[posisi-1] > currentValue:
            data[posisi] = data[posisi-1]
            posisi = posisi-1
        data[posisi] = currentValue

data = [9,8,7,4,5,2,1]
insertionsort(data)
print(data)