def mergeSort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = mergeSort(arr[0:mid])
    right = mergeSort(arr[mid:])
    
    return merge(left, right)

# unlike JS, list has no popleft thus we need indicies to iterate through
def merge(l, r):
    res = [] 
    i = 0
    j = 0 
    while i < len(l)and j < len(r):
        if l[i] < r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1

    while i < len(l) :
        res.append(l[i])
        i += 1
    while j < len(r):
        res.append(r[j])
        j += 1

    return res 

arr = [4,8,7,2,11,1,3]
print(mergeSort(arr))
