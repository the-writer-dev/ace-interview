# link: https://leetcode.com/problems/copy-list-with-random-pointer/description/

import collections


class RandomNode:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


def deep_copy(head):
    dic = collections.defaultdict(lambda: RandomNode(0))

    # in case a node's random pointer refers to None
    dic[None] = None
    curr = head

    # while iterating, default dict will create a randome node with next and random set to none
    while curr:
        dic[curr].val = curr.val
        dic[curr].next = dic[curr.next]
        dic[curr].random = dic[curr.random]
        curr = curr.next

    return dic[head]
