from tree_node import TreeNode

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)


def max_depth(root):
    def dfs(root):
        if root == None:
            return 0
        else:
            l = dfs(root.left)
            r = dfs(root.right)
            return max(l, r) + 1
    return dfs(root)


d = max_depth(root)
