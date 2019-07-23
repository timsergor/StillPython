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
