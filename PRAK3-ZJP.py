import sys
sys.setrecursionlimit(10 ** 9)

memo = dict()
MOD = 10**9 + 7
def f(n):
    if(memo.get(n) != None):
        return memo[n]
    else:
        if(n <= 0):
            return 0
        elif(n == 1):
            return 0
        elif(n == 2):
            return 1
        elif(n == 3):
            return 1
        elif(n == 4):
            return 2
        else:
            memo[n] = ((f(n - 2)%MOD) + (f(n - 3)%MOD) + (f(n - 4)%MOD))%MOD
            return memo[n]
n = int(input())
print(f(n))


# 1 x 2 / 1 x 3 / 1 x 4 / 1x2+1x3/ 1x2+1x4 / 1x3+1x4 / 1x2+1x3+1x4/
#   2 : 1 + 0 + 0
#   3 : 0 + 1 + 0
#   4 : 1 + 0 + 1  