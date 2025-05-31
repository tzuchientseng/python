def Quicksort(arr, start, end):
    if end <= start: return #Base case
    pivot = Partition(arr, start, end)
    Quicksort(arr, start, pivot- 1)
    Quicksort(arr, pivot + 1, end)

def Partition(arr, start, end):
    i = start - 1 
    for j in range(start, end):
        if arr[j] < arr[end]:
            i+=1
            arr[i], arr[j] = arr[j], arr[i] 
    i+=1
    arr[i], arr[end] = arr[end], arr[i]
    return i  #New pivot

array = [4,-3454,545,343,4563,-43,3,45,2463,38,78,66,8,67,3,841]
Quicksort(array, 0, len(array)-1)
print(array)