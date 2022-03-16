# link: https://leetcode.com/problems/jump-game-vi/

# idea
# similar to max sliding window problem
# note that the first element and the last element should be always included in the calculation

# analysis: O(n)/ O(n)
from collections import deque
def max_result(nums, k):
    q = deque()
    for i in range(len(nums)):
        nums[i] += nums[q[0]] if len(q) else 0
        while q and nums[i] >= nums[q[-1]]: q.pop() # remove elements which are smaller than the current input
        if q and i - q[0] == k: q.popleft()  # remove expired elements which are earlier than the (i-k)th element
        q.append(i)
    return nums[-1]

nums = [1,-1,-2,4,-7,3] 
k = 2

print(max_result(nums,k))
