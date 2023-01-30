from node import ListNode

# merge two sorted linked list in one sorted linked list


def merge(l1, l2):
    curr = dummy = ListNode(-1)
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = ListNode(l1.val)
            curr, l1 = curr.next, l1.next
        else:
            curr.next = ListNode(l2.val)
            curr, l2 = curr.next, l2.next
    if l1 or l2:
        curr.next = l1 or l2

    return dummy.next
