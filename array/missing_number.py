# link: https://leetcode.com/problems/missing-number/submissions/ 

# idea
# example = [3,0,1] -> ans = 2
# example = [1,2,3] -> ans = 4

# in perfect array, nor operation on both index and values
# the bit will be 0, which we should return the border value
# in imperfect array, 
# the bit will be the value we miss

def missingNumber(self, nums):
    # bit manipulation
    # nor operation
    bit = len(nums)
    for i in range(len(nums)):
        bit ^= nums[i]
        bit ^= i
    
    return bit
