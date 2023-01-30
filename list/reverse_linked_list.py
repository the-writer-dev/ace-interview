from node import ListNode
from traverse import traverse


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

# reverse the linked list
# recursion


def reverse_itr(head):
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev


def reverse_rec(node, prev=None):
    if not node:
        return prev
    n = node.next
    node.next = prev
    return reverse_rec(n, node)


traverse(reverse_rec(head))
