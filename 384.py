# 100. Same Tree. Easy. 51.1%.

# Given two binary trees, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def eq(node1, node2):
            if node1 and node2:
                if node1.val == node2.val:
                    return eq(node1.left, node2.left) and eq(node1.right, node2.right)
                else:
                    return False
            elif node1 or node2:
                return False
            else:
                return True
        
        return eq(p, q)
