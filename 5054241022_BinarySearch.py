import time
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

start_time = time.time()
a = binarySearch(array, x, 0, len(array)-1)
end_time = time.time()
time_taken = end_time - start_time

print(a)
print(time_taken)
