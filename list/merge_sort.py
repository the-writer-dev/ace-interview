# link:


def mergeSort(head):
    # divide input in halves
    if not head or not head.next:
        return head
    fast, slow = head.next, head
    # find the middle node
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    nxt, slow.next = (slow.next,) = None

    # call the left sub and right sub
    l, r = mergeSort(head), mergeSort(nxt)

    # merge
    if not l or not r:
        return l or r
    dummy = curr = ListNode(0)
    while l and r:
        if l.val < r.val:
            curr.next = l
            l = l.next
        else:
            curr.next = r
            r = r.next
        curr = curr.next
    curr.next = l or r
    return dummy.next
