def bubblesort(data):
    for nomor in range(len(data)-1,0,-1):
        for i in range(nomor):
            if data[i] > data[i+1]:
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp

data = [54,26,93,17,77,31,44,55,20]
bubblesort(data)
print(data)