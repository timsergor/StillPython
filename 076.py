#110. Balanced Binary Tree. Easy. 41.5%

#Given a binary tree, determine if it is height-balanced.
#For this problem, a height-balanced binary tree is defined as:
#a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def hieght(Node):
            if Node == None:
                return(-1)
            else:
                return(max(hieght(Node.left), hieght(Node.right)) + 1)
        
        def check(Node):
            if Node == None:
                return(True)
            else:
                if abs(hieght(Node.left) - hieght(Node.right)) <= 1:
                    return(check(Node.left) and check(Node.right))
                else:
                    return(False)
        
        return(check(root))
        
# < 10min
