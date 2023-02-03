# link: https://leetcode.com/problems/palindrome-linked-list/description/

# idea: move the first pointer to the mid
# while moving the first pointer to last node, reverse the second pointer to the first node


def isPalindrome(head):
    slow, fast, prev = head, head, None
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    prev, prev.next, slow = slow, None, slow.next

    # reverse the last half of linked list
    while slow:
        slow.next, prev, slow = prev, slow, slow.next

    fast, slow = head, prev

    # check the first half of linked list and last half of linked list
    while slow:
        if fast.val != slow.val:
            return False
        fast, slow = fast.next, slow.next
    return True
