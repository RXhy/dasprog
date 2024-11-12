import sys
mode,key = map(int,input().split()) #mode 1 = enkripsi / 2 = deskripsi . key merupakan jumlah pergeseran caesar cipher code
pesan = list(sys.stdin.read().lower())  

alphabet ="abcdefghijklmnopqrstuvwxyz" #alfabet untuk digeser

def Enkripsi(pesan,key,alphabet): #fungsi enkripsi
    shifted = alphabet[key%26:] + alphabet[:key%26]
    encrypted = ""                  #pesan yang telah dienkripsi
    for huruf in pesan:             #melakukan loop untuk tiap huruf        
        if huruf in alphabet:     #jika huruf berada pada aplhabet
            encrypted += shifted[alphabet.index(huruf)]             
        else:                       #jika huruf merupakan simbol atau angka atau yang tidak berada variabel alphabet.
            encrypted += huruf
    return encrypted                #mengembalikan nilai berupa pesan yang telah dienkripsi

def Dekripsi(pesan,key,alphabet):  #model dekripsi
    shifted = alphabet[-key%26:] + alphabet[:-key%26]     
    encrypted = ""                  #pesan yang telah didekripsi
    for huruf in pesan:
        if huruf in alphabet:
            encrypted += shifted[alphabet.index(huruf)]
        else:
            encrypted += huruf 
    return encrypted                #mengembalikan nilai berupa pesan yang telah didekripsi

if mode == 1:
    result = Enkripsi(pesan,key,alphabet) #enkripsi
    print(result)
elif mode == 2:
    result = Dekripsi(pesan,key,alphabet) #dekripsi
    print(result)