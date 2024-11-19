def insertion(angka):
    for i in range(1, len(angka)):
        key = angka[i]
        j = i - 1
        while j >= 0 and key < angka[j]:
            angka[j + 1] = angka[j]
            j -= 1
        angka[j + 1] = key
    return angka

print(insertion(angka=[20,1,23,6,14]))