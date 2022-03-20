# link: https://leetcode.com/problems/linked-list-cycle-ii/

# the idea is discussed in /graph/cycle_detection.py
def detectCycle(self, head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
