file1 = open("Myfamily.txt","w")

for i in range(3):
    name = input("Enter your name:")
    file1.write(name)
    file1.write("\n")
file1.close()

