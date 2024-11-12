n = int(input())
hasil = []

for _ in range(n):
    m = int(input())
    angka = list(map(int,input().split()))
    cek = [0]*10
    
    for i in angka:
        cek[i] += 1
    
    a = max(cek)
    b = cek.index(a)
    
    if len(angka) == 1 or m == 1:
        hasil.append(-1)
        
    elif cek.count(a) == 1:
        temp = f"{a} * {b} = {a*b}"
        hasil.append(temp)
        
    elif cek.count(a) > 1:
        sementara = []
        tempstr =""
        perkalian = 1
        for m in range (len(cek)): 
            if cek[m] == a:
                sementara.append(m)
        for i in sementara:
            perkalian *= i  
            if sementara.index(i) == (len(sementara)-1):
                tempstr += f"{i} = {perkalian}"
                break
            else:
                tempstr += f"{i}*"
        hasil.append(tempstr)
        
for i in hasil:
    print(i)