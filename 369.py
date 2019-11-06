# 623. Add One Row to Tree. Medium. 48%.

# Given the root of a binary tree, then value v and depth d, you need to add a row of nodes with value v at the given depth d. The root node is at depth 1.

# The adding rule is: given a positive integer depth d, for each NOT null tree nodes N in depth d-1, create two tree nodes with value v as N's left subtree root and right subtree root. And N's original left subtree should be the left subtree of the new left subtree root, its original right subtree should be the right subtree of the new right subtree root. If depth d is 1 that means there is no depth d-1 at all, then create a tree node with value v as the new root of the whole original tree, and the original tree is the new root's left subtree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        def solution(node,v,d):
            if node:
                if d == 1:
                    newroot = TreeNode(v)
                    newroot.left = node
                    node = newroot
                elif d == 2:
                    l = TreeNode(v)
                    r = TreeNode(v)
                    l.left = node.left
                    r.right = node.right
                    node.left = l
                    node.right = r
                else:
                    solution(node.left, v, d - 1)
                    solution(node.right, v, d - 1)
            return node
        
        return solution(root, v, d)
