from node import Node
from traverse import traverse


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

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
