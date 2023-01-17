## Tree Terminology
- tree is data structure defined as a collection of nodes.
- subtrees are descendants of a node
- nodes have value and they are connected with edges
- root has no parent node
- parent node is immediate predecessor of a node
- children nodes are all immediate successors of a node
- leaf node has no children nodes
- edge is a connection between one node to another
- path is a number of successive edges from one node to another
- depth of a node is the number of edges from the node to the tree's root node.
- root node will have a depth of 0.
- height of a node is the number of edges on the longest path from the node to a leaf.
- leaf nodes will have a height of 0.

## Types of tree
- binary tree: every node can have at most 2 children, left and right
- complete tree: binary tree, which every level is completely filled, possibly except for the lowest level. 
- balanced tree: binary tree, which the height of the left and right subtree at any node differs at most by 1.
- perfect tree: binary tree, which every internal node has exactly two child nodes and all the leaf nodes are at the same level.
- binary search tree: left subtree of a node contains only nodes with keys lesser than the node’s key. right subtree of a node contains only nodes with keys greater than the node’s key.

## Traverse
Traversing nodes in tree is essential to solve any tree related problems. 
Make sure you know how to traverse in
- In Order 
- Pre Order 
- Post Order
- Level Order
- [Link](./traverse.py)
