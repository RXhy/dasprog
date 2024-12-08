def Usia(mat,rindex,counter):
    for i in range (n):
        if mat[i] < rindex:
            counter += 1
    return counter

m,n = map(int,input().split())
mat = []

for i in range (n):
    temp = list(map(int,input().split()))
    mat.extend(temp)

q = input()
r = list(map(int,input().split()))

def display():
    result = []
    for rindex in r:
        result.append(Usia(mat,rindex,counter=0))
    print(*result)
    
display()
