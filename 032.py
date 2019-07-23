# 1022. Sum of Root To Leaf Binary Numbers. Easy, 57.4%

# Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
#For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.
#Return the sum of these numbers.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def somewhat(node):
            if not(node.left or node.right):
                return([1], node.val)
            elif not(node.right):
                M, S = somewhat(node.left)
                M.append(0)
                if node.val:
                    d = 1
                    for i in range(len(M)):
                        S += (d * M[len(M)-1-i])
                        d *= 2
                return(M,S)
            elif not(node.left):
                M, S = somewhat(node.right)
                M.append(0)
                if node.val:
                    d = 1
                    for i in range(len(M)):
                        S += (d * M[len(M)-1-i])
                        d *= 2
                return(M,S)
            else:
                Ml, Sl = somewhat(node.left)
                Mr, Sr = somewhat(node.right)
                S = Sl + Sr
                if len(Ml) > len(Mr):
                    M = Ml
                    for i in range(len(Mr)):
                        M[len(M)-1-i] += Mr[len(Mr)-1-i]
                else:
                    M = Mr
                    for i in range(len(Ml)):
                        M[len(M)-1-i] += Ml[len(Ml)-1-i]
                M.append(0)
                if node.val:
                    d = 1
                    for i in range(len(M)):
                        S += d * M[len(M)-1-i]
                        d *= 2
            return(M,S)
        M,S = somewhat(root)
        return(S)

# 30-140 min
