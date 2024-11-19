angka = [2,10,31,4]

def BubbleSort(angka):
    for i in range (len(angka)):
        for j in range(0,len(angka)-i-1):
            if angka[j] > angka[j+1]:
                angka[j],angka[j+1] = angka[j+1],angka[j]
    return angka
print(BubbleSort(angka))