def shortBubbleSort(data):
    acc = True
    batas = len(data) - 1
    while batas > 0 and acc:
        acc = False
        for i in range(batas):
            if data[i] < data[i+1]:
                acc = True
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp
        batas = batas - 1

data = [20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(data)
print(data)