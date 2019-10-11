# 1026. Maximum Difference Between Node and Ancestor

# Given the root of a binary tree, find the maximum value V for which there exists different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

# (A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def isLeaf(node):
            return not (node.left and node.right)
        
        def solution(node,mn,mx):
            if not node:
                return mx - mn
            else:
                mn = min(mn, node.val)
                mx = max(mx, node.val)
                return max(solution(node.left, mn, mx), solution(node.right, mn, mx))
        
        return solution(root, root.val, root.val)
