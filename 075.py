#104. Maximum Depth of Binary Tree. Easy. 61.6%
#Given a binary tree, find its maximum depth.
#The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def hieght(Node):
            if Node == None:
                return(0)
            else:
                return(max(hieght(Node.left), hieght(Node.right)) + 1)
        
        return(hieght(root))

  # 1min
