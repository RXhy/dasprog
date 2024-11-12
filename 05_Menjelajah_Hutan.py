# Menjelajah hutan

row, col, n = map(int, input().split())
grid = []

for _ in range(row):
    temp = list(map(int, input().split()))
    grid.append(temp)

move = input().upper()
i = 0
j = 0
duit = grid[i][j]

for _ in move:
    if _ == "U":
        nextI,nextJ = i - 1, j 
    elif _ == "D":
        nextI,nextJ = i + 1, j 
    elif _ == "R":
        nextI,nextJ = i, j + 1
    elif _ == "L":
        nextI,nextJ = i, j - 1

    if (nextI < 0 or nextI >= row) or (nextJ < 0 or nextJ >= col):
        print("gerakanmu salah bung!")
        break
    
    grid[i][j]=0 
    i, j = nextI, nextJ
    if _ == "U":
        duit += 3
    elif _ == "D":
        duit -= 2
    elif _ == "R":
        duit += 3
    elif _ == "L":
        duit -= 2
        
    goldPos = grid[i][j]    
    
    duit += goldPos


                 
    print(_,i, j, grid[i][j], duit)

print(duit)
