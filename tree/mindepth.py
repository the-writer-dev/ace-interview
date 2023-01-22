from tree_node import TreeNode

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(1)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(6)


def min_depth(root):
    if not root:
        return 0
    if None in [root.left, root.right]:
        return max(min_depth(root.left), min_depth(root.right)) + 1
    else:
        return min(min_depth(root.left), min_depth(root.right)) + 1


d = min_depth(root)
