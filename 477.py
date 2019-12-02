# 993. Cousins in Binary Tree. Easy. 51.9%.

# In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

# Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

# We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

# Return true if and only if the nodes corresponding to the values x and y are cousins.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def depth(k, node, d):
            if not node:
                return "*"
            if node.val == k:
                return d
            else:
                A = depth(k, node.left, d + 1)
                B = depth(k, node.right, d + 1)
                if A != "*":
                    return A
                if B != "*":
                    return B
                else:
                    return "*"
        
        def isBrothers(a, b, node):
            if not node:
                return False
            elif node.left and node.right:
                if set([node.left.val, node.right.val]) == set([a,b]):
                    return True
                A = isBrothers(a,b, node.left)
                B = isBrothers(a,b, node.right)
                return A or B
            elif node.left:
                return isBrothers(a,b, node.left)
            elif node.right:
                return isBrothers(a,b, node.right)
        
        d1 = depth(x, root, 0)
        d2 = depth(y, root, 0)
        return (d1 == d2) and (not isBrothers(x,y, root))
