# 783. Minimum Distance Between BST Nodes. Easy. 51%.

# Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def values(node):
            if node:
                return values(node.left) + values(node.right) + [node.val]
            else:
                return []
        
        L = values(root)
        L.sort()
        answer = L[-1] - L[0]
        for i in range(1,len(L)):
            answer = min(answer, L[i] - L[i - 1])
        return answer
