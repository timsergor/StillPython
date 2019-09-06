# 107. Binary Tree Level Order Traversal II. Easy. 48.1%.
# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def solution(node):
            if node == None:
                return []
            if not (node.left or node.right):
                return [[node.val]]
            else:
                L = solution(node.left)
                R = solution(node.right)
                M = []
                if len(L) > len(R):
                    L.reverse()
                    while len(L) > len(R):
                        M.append(L.pop())
                    L.reverse()
                if len(R) > len(L):
                    R.reverse()
                    while len(R) > len(L):
                        M.append(R.pop())
                    R.reverse()
                for i in range(len(L)):
                    L[i].extend(R[i])
                    M.append(L[i])
                M.append([node.val])
            return M
        return solution(root)
        
# 30 min
