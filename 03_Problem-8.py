#Tower Level Elevation
n,energy,case = map(int,input().split()) #lantai, energi, kasus
a = list(map(int,input().split()))  #jumlah monster 
energyNeed = 0                      #energi yang dibutuhkan

for i in range (case):              #mengecek tiap kasus
    x,y = map(int,input().split())  #lantai awal dan lantai tujuan
    energyNeed += sum(a[x-1:y-1])   #total energi yang dibutuhkan

sisaEnergi = energy - energyNeed    #sisa energi
if sisaEnergi >= 0:                 
    print(f"EZ banget,energiku sisa {sisaEnergi}!") #energi cukup
else:
    print(f"NT, kurang {abs(sisaEnergi)} energi sih.") #energi tidak cukup