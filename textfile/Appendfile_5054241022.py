file1 = open("myfile.txt","w")
L = ["This is Keputih \n", "This is Sukolilo \n", "This is Surabaya\n"]
file1.writelines(L)
file1.close()

file1 = open("myfile.txt", "a")
file1.write("This is ITS \n")
file1.close

file1 = open("myfile.txt", "r")
print("Output of Readlines after appending")
print(file1.readlines())
print()
file1.close()

# Write-Overwrites
file1 = open("myfile.txt", "w")  # write mode
file1.write("Teknik Informatika \n")
file1.close()

file1 = open("myfile.txt", "r")
print("Output of Readlines after writing")
print(file1.readlines())
print()
file1.close()