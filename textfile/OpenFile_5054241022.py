file1 = open("5054241022.txt","w")
L = ["Nama saya Royan Harits Yustanto \n", "Asal saya dari Sidoarjo \n", "Saya suka makan joder\n"]

file1.write("hello \n")
file1.writelines(L)
file1.close()

file1 = open("5054241022.txt", "r+")

print("Output of Read function is ")
print(file1.read())
print()

file1.seek(0)

print("Output of Readline function is ")
print(file1.readline())
print()

file1.seek(0)

print("Output of Read(17) function is ")
print(file1.read(17))
print()

file1.seek(0)

print("Output of Readline(100) function is ")
print(file1.readline(100))

file1.seek(0)

print("Output of Readlines function is ")
print(file1.readlines())
print()
file1.close() 