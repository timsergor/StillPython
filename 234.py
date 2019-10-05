# 1214. Two Sum BSTs. Medium. Contest.

# Given two binary search trees, return True if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer target.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def twoSumBSTs(self, root1, root2, target):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :type target: int
        :rtype: bool
        """
        char = {}
        def solution(node1,node2):
            if not (node1 and node2):
                return False
            if node1.val + node2.val == target:
                return True
            if node1.val + node2.val < target:
                if (node1, node2.right) not in char:
                    char[(node1, node2.right)] = solution(node1, node2.right)
                if (node1.right, node2) not in char:
                    char[(node1.right, node2)] = solution(node1.right, node2)
                return char[(node1, node2.right)] or char[(node1.right, node2)]
            else:
                if (node1, node2.left) not in char:
                    char[(node1, node2.left)] = solution(node1, node2.left)
                if (node1.left, node2) not in char:
                    char[(node1.left, node2)] = solution(node1.left, node2)
                return solution(node1, node2.left) or solution(node1.left, node2)
        
        return solution(root1,root2)
        
# <20min.
