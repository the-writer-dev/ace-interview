# link: https://leetcode.com/problems/odd-even-linked-list/


def oddEvenList(head):
    odd = even = head
    eHead = head.next

    while even and even.next:
        # jump to next odd index nodes
        odd.next = odd.next.next

        # jump to next even index nodes
        even.next = even.next.next
        odd = odd.next
        even = even.next

    odd.next = eHead
    return head
