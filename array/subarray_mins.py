# link: https://leetcode.com/problems/sum-of-subarray-minimums/

def subarray_mins(arr):
    left = [x+1 for x in range(len(arr))]
    right = [len(arr) - x for x in range(len(arr))]

    p = []
    n = []
    for i in range(len(arr)):
        # previous less 
        while p and p[-1][0] > arr[i]: 
            p.pop()
        left[i] = i+1 if not p else i - p[-1][1]
        p.append([arr[i], i])

        # next less
        while n and n[-1][0] > arr[i]:
            x = n[-1]
            n.pop()
            right[x[1]] = i - x[1]
        n.append([arr[i], i])

    ans = 0
    mod = 10 ** 9 + 7
    for i in range(len(arr)):
        ans = (ans + arr[i]*left[i]*right[i]) % mod
    return ans

arr = [3,7,8,4]
print(subarray_mins(arr))
arr = [2,9,7,3,4,6,1]
print(subarray_mins(arr))
