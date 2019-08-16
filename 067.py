#951. Flip Equivalent Binary Trees. Medium. 64.9%.

#For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.
#A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.
#Write a function that determines whether two binary trees are flip equivalent.  The trees are given by root nodes root1 and root2.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        def isLeaf(Node):
            if not(Node.left or Node.right):
                return(True)
            else:
                return(False)
        
        def isFlipped(node1, node2):
            if node1 == None and node2 == None:
                return(True)
            elif (node1 == None) or (node2 == None) or (node1.val != node2.val):
                return(False)
            else:
                if isFlipped(node1.left, node2.left) and isFlipped(node1.right, node2.right):
                    return(True)
                elif isFlipped(node1.left, node2.right) and isFlipped(node1.right, node2.left):
                    return(True)
                return(False)
            
        return(isFlipped(root1, root2))
