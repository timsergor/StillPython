# 700. Search in a Binary Search Tree. 69.7%.

# Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def solution(node):
            if node:
                if node.val > val:
                    return solution(node.left)
                elif node.val < val:
                    return solution(node.right)
                else:
                    return node
            else:
                return None
        
        return solution(root)
