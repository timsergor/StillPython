#655. Print Binary Tree. Medium. 52.4%.

#Print a binary tree in an m*n 2D string array following these rules:

#The row number m should be equal to the height of the given binary tree.
#The column number n should always be an odd number.
#The root node's value (in string format) should be put in the exactly middle of the first row it can be put. The column and the row where the root node belongs will separate the rest space into two parts (left-bottom part and right-bottom part). You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part. The left-bottom part and the right-bottom part should have the same size. Even if one subtree is none while the other is not, you don't need to print anything for the none subtree but still need to leave the space as large as that for the other subtree. However, if two subtrees are none, then you don't need to leave space for both of them.
#Each unused space should contain an empty string "".
#Print the subtrees following the same rules.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        def height(node):
            if node == None:
                return -1
            else:
                return max(height(node.left), height(node.right)) + 1
        
        H = height(root)
        def solution(node, h):
            if node == None:
                if h >= 0:
                    M = [[""] * (2 ** (h + 1) - 1)]
                    for i in range(h):
                        M.append([""] * (2 ** (h + 1) - 1))
                    return(M)
            if not (node.left or node.right):
                M = [[""] * (2 ** (h + 1) - 1)]
                M[0][len(M[0])//2] = str(node.val)  
                for i in range(h):
                    M.append([""] * (2 ** (h + 1) - 1))
                return M
            else:
                L = solution(node.left,h - 1)
                R = solution(node.right,h - 1)
                M = [[""] * (2**h - 1) + [str(node.val)] + [""] * (2**h - 1)]
                for i in range(len(L)):
                    L[i].append("")
                    L[i].extend(R[i])
                    M.append(L[i])
                return(M)
        
        return solution(root,H)  
