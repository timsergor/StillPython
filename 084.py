#101. Symmetric Tree. Easy. 44.1%.
#Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(Node1,Node2):
            if (Node1 == None and Node2 == None):
                return(True)
            elif Node1 == None or Node2 == None:
                return(False)
            if Node1.val == Node2.val and isMirror(Node1.left, Node2.right) and isMirror(Node1.right, Node2.left):
                return(True)
            return(False)
        
        return(isMirror(root,root))

# 8min
