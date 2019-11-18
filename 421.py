# 501. Find Mode in Binary Search Tree. 40.5%.

# Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        def shear(node):
            if node:
                a = shear(node.left)
                b = shear(node.right)
                char = {node.val : 1}
                for c in a:
                    if c in char:
                        char[c] += a[c]
                    else:
                        char[c] = a[c]
                for c in b:
                    if c in char:
                        char[c] += b[c]
                    else:
                        char[c] = b[c]
                return char
            else:
                return {}
        
        char = shear(root)
        answer = []
        m = 1
        for c in char:
            if char[c] > m:
                answer = [c]
                m = char[c]
            elif char[c] == m:
                answer.append(c)
        return answer
