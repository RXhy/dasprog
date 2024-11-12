n,m = map(int,input().split())

price = list(map(int,input().split()))
total = 0 
cece =  list(map(int,input().split()))
utang = 0 

for i in price:
    if i > 0:
        total += i 
        
if total == 0:
   total = max(price) 

for j in cece:
    if j < 0: 
        utang += j
        
if utang == 0:
    utang = min(cece)

if total > utang:
    result = total - utang  
else: result = utang - total         
print(result)
print(total,utang)