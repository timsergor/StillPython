# 98. Validate Binary Search Tree. Medium. 26.5%.

# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def isIt(node, down = "#", up = "#"):
            if not node:
                return True
            Flag = (down == "#" or down < node.val) and (up == "#" or up > node.val)
            return Flag and isIt(node.left, down, node.val) and isIt(node.right, node.val, up)
        
        return isIt(root)
