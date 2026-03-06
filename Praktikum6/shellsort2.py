def shellShort(data):
    hitung = len(data)//2
    while hitung > 0:
        for mulai in range(hitung):
            batas(data, mulai, hitung)
        
        print("After increments of size", hitung, "The list is", data)
        hitung = hitung//2

def batas(data, start, gap):
    for i in range(start+gap, len(data), gap):
        currentValue = data[i]
        posisi = i

        while posisi>=gap and data[posisi-gap]<currentValue:
            data[posisi] = data[posisi-gap]
            posisi = posisi - gap
        
        data[posisi] = currentValue

data = [54,26,93,17,77,31,44,55,20]
shellShort(data)
print(data)