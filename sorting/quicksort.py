# analysis: O(n^2)

def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    print("i {} and pivot {}".format(i, pivot))
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] =  arr[j], arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return (i+1)

def quicksort(arr, start, end):
    if start >= end:
        return arr 
    pivotIndex = partition(arr, start, end)

    quicksort(arr, start, pivotIndex - 1)
    quicksort(arr, pivotIndex + 1, end)

    return arr

arr = [4,8,7,2,11,1,3]
print(quicksort(arr, 0, len(arr)-1))
