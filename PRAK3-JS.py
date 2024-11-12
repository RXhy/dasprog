m, n = map(int,input().split())

mall = []
for _ in range(n):
    temp = list(map(int,input()))
    mall.append(temp)
    
icurrent = 0
jcurrent = 0
ifinish = n-1
jfinish = m-1

def move(icurrent, jcurrent, ifinish, jfinish,mall):
    if (icurrent == ifinish) and (jcurrent ==jfinish):
        return mall
    else:
        if (icurrent + 1 <=n-1) and (mall[icurrent+1][jcurrent] != 1):
            mall[icurrent][jcurrent] = '*'
            return move(icurrent+1,jcurrent,ifinish,jfinish,mall)
        
        elif (jcurrent + 1 <=m-1) and (mall[icurrent][jcurrent+1] != 1):
            mall[icurrent][jcurrent] = '*'
            return move(icurrent,jcurrent+1,ifinish,jfinish,mall)
        
        elif (jcurrent - 1 >=0) and (mall[icurrent][jcurrent-1] != 1):
            mall[icurrent][jcurrent] = '*'
            return move(icurrent,jcurrent-1,ifinish,jfinish,mall)
        
        elif (icurrent - 1 >=0) and (mall[icurrent-1][jcurrent] != 1):
            mall[icurrent][jcurrent] = '*'
            return move(icurrent-1,jcurrent,ifinish,jfinish,mall)

move(icurrent,jcurrent,ifinish,jfinish,mall)

for i in range(n):
    for j in range(m):
        print(mall[i][j],end='')
    print("")