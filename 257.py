# 230. Kth Smallest Element in a BST. Easy. 53.7%.

# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

# Note:
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def amount(node):
            if not node:
                return 0
            else:
                return amount(node.left) + 1 + amount(node.right)
        
        def solution(node, k):
            l = amount(node.left)
            if l >= k:
                return solution(node.left, k)
            elif l == k - 1:
                return node.val
            else:
                return solution(node.right, k - l - 1)
        
        return solution(root,k)
