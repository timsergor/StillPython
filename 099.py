572. Subtree of Another Tree. Easy. 42.1%.

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def isIt(node1, node2):
            if not (node1 or node2):
                return(True)
            elif not node1 or not node2:
                return(False)
            else:
                if node1.val != node2.val:
                    return(False)
                else:
                    return(isIt(node1.left, node2.left) and isIt(node1.right, node2.right))
        
        def solution(node1, node2):
            if isIt(node1, node2):
                return(True)
            if not (node1 or node2):
                return(True)
            elif not node1 or not node2:
                return(False)
            else:
                return(solution(node1.left, node2) or solution(node1.right, node2))
        
        if solution(s,t):
            return(True)
        return(False)
        
# 9min.
