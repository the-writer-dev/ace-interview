
# link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
def deleteDuplicate(head):
    curr = head
    while curr:
        while curr.next and curr.val == curr.next.val:
            curr.next = curr.next.next
        curr = curr.next
    return head
