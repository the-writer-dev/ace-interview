# find the middle node of the given linked list


def middle(head):
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow
