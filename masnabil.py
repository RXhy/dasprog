bil = int(input())
angka = list(map(int,input().split()))

hasil = 1  
for i in range(bil-1):
    for j in range(i+1,bil):
            a = angka[i] ^ angka[j]
            print(angka[i],angka[j])
            if hasil == 0:
                break
            hasil *= a
print(hasil)    
