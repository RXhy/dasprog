#function
def Perkalian(a,b):
    print(f"{a}*{b} = {a*b}")

Perkalian(10,5)

def Destinasi(asal,tujuan):
    rute = f"bis a akan memulai rutenya dengan berangkat dari halte {asal} dan berakhir di {tujuan}"
    return rute

print(Destinasi("ITS","UNAIR C"))
print(Destinasi(tujuan="Wonokromo",asal="Keputih"))

def Belanjaan(*keranjang):
    print(f"belanjaan ibu yang paling mahal adalah {keranjang[1]}")
    
Belanjaan("alphard","helikopter","kapal tanker","tank")

def Hari_bulan(**tanggalnya):
    print('Hari ini adalah hari '+ tanggalnya['hari']+ ' dan bulan adalah bulan '+ tanggalnya['bulan'])
    
Hari_bulan(hari='rabu',bulan='Oktober')

def Hobi(nama="royan", hobi="hapean"):
    print(f"namaku {nama} dan hobiku {hobi}")

Hobi()
Hobi(nama="udin")
Hobi(hobi="lesehan")
Hobi(nama="amba",hobi="halusinasi")

def Absen(anak):
  for x in anak:
    print(x)

kehadiran = ["budi", "bukan budi", "budi lagi"]

Absen(kehadiran)

def my_function(x,y, /):
    print('x is '+str(x)+' and y is '+str(y))

my_function(3,4)
my_function(4,5)
#[ERROR tidak boleh key-argument karena positional] my_function(x = 3, y = 4)

def my_function(*, x):
    print(x)
    
my_function(x = 5)
#[ERROR hanya bisa key-argument] my_function(5)

def my_function(a,b, /, *, c, d):
    print(a + b + c + d)
    
my_function(5, 6, c=7,d=8)