import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)


def in_order(root):
    if root:
        in_order(root.left)
        print(root.val)
        in_order(root.right)


def pre_order(root):
    if root:
        print(root.val)
        print(root.left)
        print(root.right)


def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.val)


def level_order(root):
    if root == None:
        return

    q = collections.deque([root])
    while q:
        c = q.popleft()
        print(c.val)
        if c.left:
            q.append(c.left)
        if c.right:
            q.append(c.right)
