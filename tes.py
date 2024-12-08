# def faktor(n):
#     if n == 1:
#         return 1
#     else:
#         return (n * faktor(n-1))
        
# n = int(input())
# print(faktor(n))

# isstrong = True
# password, key = map(str,input().split())

# if password.isdigit() == False:
#     print("Password needs number")
#     isstrong = False
# if password.isupper() == False:
#     print("Password requires at least one uppercase letter")
#     isstrong = False
# if len(password) != key:
#     isstrong = False
#     print("Digits in password not equal to key")

# if isstrong:
#     print("strong")
# else: print("weak")

# n = int(input())

# dictf = {0:0, 1:1, 2:1}

# def fibo(n):
#     if n in dictf:
#         return dictf[n]
#     else:
#         dictf[n] = fibo(n-1) + fibo(n-2) 
#         return dictf[n]

# tabel = []    
# def ans(n,x):
#     if fibo(x) <= n:
#         tabel.insert(0,fibo(x))
#         ans(n,x+1)

# def total(n):
#     if n == 0:
#         return tabel[n]
#     else:
#         return tabel[n] + total(n-1)
             
# ans(n,0)
# print(tabel,'\n',total(len(tabel)-1))

# dict_pass = {1:[1]}
# def len_string(n):
#     if n in dict_pass:
#         return dict_pass[n]
#     else:
#         for i in range(2,n+1):
#             dict_pass[i] = dict_pass[i-1] + [i] + dict_pass[i-1]
#         return dict_pass[i]

# def password(n):
#     for i in len_string(n):
#         if i == n:
#             print("z"*i)
#         elif i % 2 == 1:
#             print("d"*i)
#         else:
#             print("e"*i)

# N = int(input())
# print(dict_pass)
# password(N)

# 5 6 
# 00020
# 10101
# 12001
# 10100
# 00021
# 11100

# 5 5 
# 02000
# 00010
# 21010
# 00000
# 11110

# dic = { "ajan":3, "budi":1, "kwon":2}

# # sot = sorted(dic,key=lambda index: dic.values())
# sep = sorted(dic.items(),key=lambda item:item[1])
# print(sep)

# n = [3,2,4,22,333,11]
# def ko(x):
#     return -len(str(x)),x

# n.sort(key=ko)
# print(n)

m,n = map(int,input().split())
mat = []
for i in range (n):
    temp = list(map(int,input().split()))
    mat.append(temp)

target = input() 
x = 0 
y = 0 
def linearSearch(x,y,m,n,mat):
    for i in range (m):
        for j in range(n):
            if mat[i][j] == target:
                x = i+1
                y = i+1
                print(x,y)
                return x,y 

linearSearch(x,y,m,n,mat)
        
print(f"Element {target} found at position: ({x},{y})")