# kiwa the spy 
t = int(input())        #jumlah perulangan 
mode = int(input())     #enkripsi=0 dekprpsi=1
message = input().upper()   #message in only uppercase 

kodeEnkripsi = [19, 17, 20, 4, 18, 10, 8, 11, 11] #pola enkripsi
kodeDekripsi = [7, 9, 6, 22, 8, 16, 18, 15, 15]     #pola dekripsi

def Memecahkan(t,mode,message):
    encrypted = ""     #hasil enkripsi yang masih kosong
    for x in range(t):  #perulangan
        index = 0       
        for huruf in message:   #mengecek tiap huruf
            if huruf.isalpha(): #mengecek apakah karakter adlaah alfabet
                if huruf.isupper(): #mengecek apakah huruf kapital
                    if mode == 0: #enkripsi
                        kode = kodeEnkripsi[index % 9] 
                        encrypted += chr(((ord(huruf) - ord("A") + kode) % 26) + ord("A"))
                    elif mode == 1: #dekripsi
                        kode = kodeDekripsi[index % 9]
                        encrypted += chr(((ord(huruf) - ord("A") + kode) % 26) + ord("A")) #ASCII
                index += 1 
            elif huruf.isspace(): #spasi / whitespace           
                encrypted += huruf
    return encrypted

hasil = Memecahkan(t,mode,message)                                
print(hasil)