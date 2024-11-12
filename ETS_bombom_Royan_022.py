n,m = map(int,input().split())

maps = []
count = 0 

for i in range(n):
    temp = list(map(int,input().split()))
    maps.append(temp)
    
for i in range(n):
    for j in range(m):
        if maps[i][j] == 1:
            if i+1 < n and maps[i+1][j] == 0:
                count += 1
            if i-1 >=0 and maps[i-1][j] == 0:
                count += 1
            if j+1 < m and maps[i][j+1] == 0:
                count += 1
            if j-1 >=0 and maps[i][j-1] == 0:
                count += 1
            if i+1 <n and j+1 < m and maps[i+1][j+1] == 0:
                count += 1
            if i-1 >=0 and j-1 >=0 and maps[i-1][j-1] == 0 :
                count += 1
            if i+1 <n and j-1 >=0 and maps[i+1][j-1] == 0:
                count += 1
            if i-1 >=0 and j+1 < m and maps[i-1][j+1] == 0:
                count += 1
print(count)