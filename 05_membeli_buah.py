n, k = map(int,input().split())
a = list(map(int,input().split()))
counter = 0
daftar = []

for i in range (len(a)):
    if k >= a[i]: 
        counter += 1
        daftar.append(i)
        
print(counter)
print(f"Dengan uang {k} ia bisa membeli dengan kemungkinan {counter} jenis buah", end="")
if counter > 1:
    print(" yaitu buah ", end="")
    for _ in range (counter):
        if _ == counter-1:
            print(f"dan jenis ke-{daftar[_]+1}.",end="")
        else:    
            print(f"jenis ke-{daftar[_]+1},",end="")
elif counter == 1:
    print(f" yaitu buah jenis ke-{daftar[0]}", end="")
elif counter == 0:
    print("mana duitnya wak")