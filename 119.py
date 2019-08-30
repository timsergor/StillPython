#94. Binary Tree Inorder Traversal. Medium. 58.1%.
#Given a binary tree, return the inorder traversal of its nodes' values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def solution(node):
            if node == None:
                return []
            else:
                L = solution(node.left)
                R = solution(node.right)
                L.append(node.val)
                L.extend(R)
                return L
        
        return solution(root)
        
# 5min

