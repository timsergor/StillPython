# 199. Binary Tree Right Side View. Medium. 50.3%.

# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        def solution(node):
            if node:
                L = solution(node.left)
                R = [node.val] + solution(node.right)
                for i in range(len(R) - 1,len(L)):
                    R.append(L[i])
                return R
            else:
                return []
        
        return solution(root)
