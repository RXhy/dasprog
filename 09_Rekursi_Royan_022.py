#PRIME CHECKER
def IsPrime(angka):
    for i in range(2,angka+1):
        if  i != angka and angka % i == 0:
            return "bukan prima"
        elif angka / i == 1:
            return "prima"
print(IsPrime(1))
        
def CountPrime():
    for i in range(1,101):
        for j in range(2,i+1):
            if j != i and i % j == 0:
                break
            elif i / j == 1:
                print(f"{i} ",end="")
                break
CountPrime()

#Apple
def Remainder(apple,people):
    remainder = apple % people
    print(f"\n{remainder}")

Remainder(2310,24)

#Fibonaci 
def Fibonaci(n):
    if n == 0: 
        print(0)
    elif n == 1:
        print("0 1")
    else:
        f = [0] * n
        f[0] = 0
        f[1] = 1
        for i in range (2,n):
            f[i] = f[i-1] + f[i-2]  
        print(*f)

Fibonaci(20)

#odd number counter
def countOdd(odd):
    counter = 0
    for i in odd:
        if i % 2 == 1:
            counter += 1
    print(counter)

countOdd([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])