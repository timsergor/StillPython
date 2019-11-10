# 222. Count Complete Tree Nodes. Medium. 38.5%.

# Given a complete binary tree, count the number of nodes.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def bonders(node):
            if node:
                dl = dr = 1
                l = r = node
                while l.left:
                    l = l.left
                    dl += 1
                while r.right:
                    r = r.right
                    dr += 1
                return (dl,dr)
            return (0,0)
        
        def solution(node):
            if not node:
                return 0
            else:
                B = bonders(node)
                if B[0] == B[1]:
                    return 2 ** B[0] - 1
                return 1 + solution(node.left) + solution(node.right)
        
        return solution(root)
