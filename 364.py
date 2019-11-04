# 113. Path Sum II. 42.9%.

# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        answer = []
        
        def solution(node, s, path):
            if not node.left and not node.right:
                if node.val + s == sum:
                    answer.append(path + [node.val])
            if node.left:
                solution(node.left, s + node.val, path + [node.val])
            if node.right:
                solution(node.right, s + node.val, path + [node.val])
        
        if root:
            solution(root, 0, [])
        return answer
