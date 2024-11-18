t = int(input())
ans = []

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    q = int(input())

    sumarr = sum(a[:k])
    maxSum = sumarr
    minSum = sumarr
    print(sumarr,maxSum,minSum)
    for i in range(1, k + 1):
        #sumarr = sum(a[:i])
        maxSum = max(maxSum, sumarr)
        minSum = min(minSum, sumarr)
        print(i,sumarr,maxSum,minSum)
        for j in range(1, n - i + 1):
            '''sumarr = sumarr - a[j - 1] + a[j + i - 1]'''
            maxSum = max(maxSum, sumarr)
            minSum = min(minSum, sumarr)
            print(j,sumarr,maxSum,minSum)

    if q == 1:
        ans.append(maxSum)
    elif q == 2:
        ans.append(minSum)
for i in ans:
    print(i)