# link: https://leetcode.com/problems/find-the-duplicate-number/

# the idea is discussed in /graph/cycle_detection.py


def findDuplicate(nums):
    if len(nums) < 2:
        return -1

    slow = nums[0]
    fast = nums[nums[0]]

    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]

    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow


nums = [1, 3, 4, 2, 2]
print(findDuplicate(nums))
