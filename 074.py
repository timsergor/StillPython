#112. Path Sum. Easy. 38.4%
#Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def isit(Node, S, answers):
            if Node == None:
                pass
            elif not (Node.left or Node.right):
                answers.append(S + Node.val)
            else:
                isit(Node.left, S + Node.val, answers)
                isit(Node.right, S + Node.val, answers)
        
        M = []
        isit(root,0,M)
        if sum in M:
            return(True)
        else:
            return(False)
