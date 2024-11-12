# Bisector

#input
x = int(input("insert coordinate x for A :"))
y = int(input("insert coordinate y for A :"))
p = int(input("insert coordinate x for B :"))
q = int(input("insert coordinate y for B :"))

# calculate slope / middle point
m = (y-q)/(x-p) 
mside = m / -1
midX = (x+p)/2
midY = (y+q)/2
intercept = midY - midX*m 

#output 
print("Original point A (",x,",",y,") and B (",p,",",q,")")
print("Slope :",m," with middle point : (",midX,",",midY,")")
print("perpendicular bisector y =",m,"x +",intercept)
 