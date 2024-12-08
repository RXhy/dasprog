n = list(map(int,input().split()))
def spesial(x):
    return len(str(x)),x

n.sort(key=spesial)
print(*n)