# find the all pairs that sum to k 
# this is a tweaked question of two sum link -> https://leetcode.com/problems/two-sum/
from collections import defaultdict

nums = [2,6,3,9,11,0]
k = 9
def target_sum(nums, k):
    h = defaultdict(int)
    res = []
    for i in range(len(nums)):
        if nums[i] in h:
            res.append({nums[h[nums[i]]], nums[i]})
        else:
            h[k-nums[i]] = i 

    return res

print(target_sum(nums, k))
