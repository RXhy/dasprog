def mergeSort(angka):
    if len(angka) > 1:
        r = len(angka)//2
        L = angka[:r]
        M = angka[r:]

        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                angka[k] = L[i]
                i += 1
            else:
                angka[k] = M[j]
                j += 1
            k += 1
        
        while i < len(L):
            angka[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            angka[k] = M[j]
            j += 1
            k += 1
    return angka

print(mergeSort(angka=[10,23,4,5,46,243,12]))