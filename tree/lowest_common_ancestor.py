def lca(root, p, q):
    if root.left:
        l = lca(root.left, p, q)
    if root.right:
        r = lca(root.right, p, q)

    if l and r:
        return root
    return l or r
