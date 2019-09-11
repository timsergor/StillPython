# 872. Leaf-Similar Trees. Easy. 63.9%.

#Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def lvs(node):
            if node == None:
                return []
            elif not (node.left or node.right):
                return [node.val]
            else:
                L = lvs(node.left)
                R = lvs(node.right)
                L.extend(R)
                return L
        
        A = lvs(root1)
        B = lvs(root2)
        return A == B
        
# <3min.
