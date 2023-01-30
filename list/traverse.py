from node import ListNode


def traverse(head):
    curr = head
    while curr:
        print(curr.data)
        curr = curr.next


def insert(head, data, pos):
    new = ListNode(data)
    if pos == 0:
        new.next = head
        head = new
        return

    prev = head
    for _ in range(pos-1):
        prev = prev.next
    new.next = prev.next
    prev.next = new


def delete(head, pos):
    if pos == 0:
        head = head.next
        return
    prev = head
    for _ in range(pos-1):
        prev = prev.next
    prev.next = prev.next.next
