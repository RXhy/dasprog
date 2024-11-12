n = int(input())

def fungsi(n):
    if n == 1:
        return 1
    else:
        if n % 2 == 0:
            return 1 + fungsi(n/2)
        else:
            return 1 + fungsi(n-1)

print(fungsi(n)) 