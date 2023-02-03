# link: https://leetcode.com/problems/swap-nodes-in-pairs/

# idea: messing around the multiple pointers...


def swapPairs(head):
    dummy = ListNode(None, head)
    prev, cur = dummy, head
    while cur and cur.next:
        prev.next = cur.next
        cur.next = cur.next.next
        prev.next.next = cur
        prev, cur = cur, cur.next
    return dummy.next
