def linear(n, target):
    for i in range(len(n)):
        if n[i] == target:
            return i
    return -1

n = [1,24,46,5,6,78,83,20,4,35,7,37]
target = 4

print(linear(n,target))