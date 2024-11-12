n = int(input())

print("+"+("-"*(2*n+1))+"+")

sawah = [[' ' for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            if j % 2 == 0:
                sawah[i][j] = 'V'
            else:
                sawah[i][j] = '.'
        else:
            if j % 2 == 0:
                sawah[i][j] = '.'
            else:
                sawah[i][j] = 'V'
    print('| ',end='')
    print(*sawah[i],end='')
    print(' |')
            
print("+"+("-"*(2*n+1))+"+")
