# 958. Check Completeness of a Binary Tree. Medium. 50.3%.

# Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        def solution(node):
            if node:
                L = node
                R = node
                l = r = 0
                while L.left:
                    l += 1
                    L = L.left
                while R.right:
                    r += 1
                    R = R.right
                if l == r:
                    a = solution(node.left) 
                    b = solution(node.right)
                    if a[0] and b[0] and a[1] == 0 and b[1] == 0:
                        return (True, 0)
                    else:
                        return (False, 0)
                elif l == r + 1:
                    a = solution(node.left) 
                    b = solution(node.right)
                    print (node.val, a,b)
                    if a[0] and b[0] and (a[1] + b[1] < 2):
                        return (True, 1)
                    else:
                        return (False, 1)
                else:
                    return (False, l - r)
            return (True, 0)
        
        return solution(root)[0]
