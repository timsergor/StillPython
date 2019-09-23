# 94. Binary Tree Inorder Traversal. Medium. 58.5%.

# Given a binary tree, return the inorder traversal of its nodes' values.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# RECURSIVELY

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def solution(root):
            if not root:
                return []
            L = solution(root.left)
            R = solution(root.right)
            return L + [root.val] + R
        return solution(root)
        
# 4-5min.
