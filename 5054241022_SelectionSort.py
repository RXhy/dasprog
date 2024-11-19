def Selection(angka,length):
    for i in range(length):
        min = i 
        for j in range(i + 1,length):
            if angka[j] < angka[min]:
                min = j
        angka[i],angka[min] = angka[min],angka[i]    
    return angka
angka =[5,2,1,7,8]
length = len(angka)    
print(Selection(angka,length))