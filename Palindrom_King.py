string = str(input())
palindrom = False

flip = string[::-1]

if flip == string:
    palindrom = True

if palindrom == True:
    print("Palindrome King!")
else: print("Bukan King!")