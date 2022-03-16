# link: https://leetcode.com/problems/sliding-window-maximum/ 

# idea
# use the monotonic deque 

# analysis: O(n)/ O(n)
from collections import deque
def max_sliding_window(nums, k):
    q = deque()
    res = []
    for i in range(len(nums)):
        while q and nums[q[-1]] <= nums[i]:
            q.pop()
        q.append(i)
        
        if i-q[0] == k:
            q.popleft()
       
        if i >= k-1:
            res.append(nums[q[0]])
    return res

nums = [1,3,-1,-3,5,3,6,7]
k = 3

print(max_sliding_window(nums,k))
