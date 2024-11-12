'''n, r, c = map(int, input().split())
position ={}

for _ in range(n):
    a, b, c = map(int,input().split())
    position[(b,c)] = a 

print(position)
for _ in range(1,n+1):
    print("_",_)
    exist = False
    for (a,b), siswa in position.items():
        print(siswa, "a,b ", a,b)
        if siswa == _:
            if (a,b-1) in position:
                print(a,b-1,position[(a,b-1)])
                exist = True
            elif(a,b+1) in position:
                print(a,b+1,position[(a,b+1)])
                exist = True
            break
    if not exist:
        print(0)'''
        
n, r, c = map(int, input().split())
positionCol = []
positionRow = [positionCol]

for _ in range(n):
    m, x, y = map(int,input().split())
    positionRow.append(x)
    positionCol.append(y)

sebelah = False
sebaris = False

for siswa in range (1,n+1):
    print("siswa",siswa)
    for baris in range (0,len(positionRow)):
        if positionRow[siswa-1] == siswa:
            print(sebaris)
