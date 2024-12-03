def binarySearch(array, x, low, high):
    if high >= low:
        mid = low + (high - low)//2
        if x == array[mid]:
            return mid
        
        elif x > array[mid]:
            return binarySearch(array, x, mid + 1, high)
        else:
            return binarySearch(array, x, low, mid - 1)
    else:
        return -1

array = [23, 24, 55, 76, 87, 90, 120]
x = 24

print(binarySearch(array, x, 0, len(array)-1))