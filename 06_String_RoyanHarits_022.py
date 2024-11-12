string0 = "Royan Harits Yustanto"
string1 = "5054241022"
string2 = "Sidoarjo"

print("Nama saya adalah "+string0)
print("NRP "+ string1)      
print("Asal daerah "+string2) 
print("Inisial saya "+string0[0]+string0[6]+string0[13])

#Slicing
print("Nama belakang saya "+string0[13:])
print("Nama panggilan saya "+string0[0:5])
print("PRN "+string1[::-1])

#ubah menjadi saya bukan mahasiswa RPL
rka = "Saya mahasiswa RKA"
temp = list(rka)
temp.insert(5,"bukan ")
temp[16:] = 'RPL'
rpl = "".join(temp)
print(rpl)

#Delete 'a' dari "Sidoarjo"
delString2 = string2[0:4] + string2[5:] 
print(delString2)

#Escape sequencing
m = 'you\'re in!'
print(m)
m = "you're trying to access \\home\\user\\Documents\\\"Folder\""
print(m)

#Python string formatting
print(f"Nama saya adalah {string0}\nNRP {string1}\nAsal daerah {string2}") 

day = "9"
month = "October"
year = "2024"
print(f"today: {day},{month},{year}")

buah1 = ["apel",1000]
buah2 = ["mangga",4000]
buah3 = ["stroberi",2500]
print(f"Pak Dengklek membeli buah {buah1[0]},{buah2[0]},dan {buah3[0]},dengan total biaya {buah1[1]+buah2[1]+buah3[1]}")