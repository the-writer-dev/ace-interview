# link: https://leetcode.com/problems/linked-list-cycle/description/

# idea: assume they are on the circular track.
# if one is twice as fast as the other one, it will catch the other one at some point
def hasCycle(head):
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
