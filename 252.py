# 114. Flatten Binary Tree to Linked List. Medium. 44.5%.

# Given a binary tree, flatten it to a linked list in-place.

# For example, given the following tree:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def great(node):
            if not node:
                return None
            while node.right:
                node = node.right
            return node
        
        def solve(node):
            if not node:
                pass
            else:
                up = node.left
                down = node.right
                pre = great(up)
                if pre:
                    node.left = None
                    node.right = up
                    pre.right = down
                    solve(up)
                else:
                    solve(down)
        
        solve(root)
        
# 9min.
