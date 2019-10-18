# 1161. Maximum Level Sum of a Binary Tree. Medium. 71%.

# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

# Return the smallest level X such that the sum of all the values of nodes at level X is maximal.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        def floars(node):
            if not node:
                return []
            else:
                L = floars(node.left)
                R = floars(node.right)
                L.reverse()
                R.reverse()
                answer = [[node.val]]
                while len(L) and len(R):
                    L[-1].extend(R.pop())
                    answer.append(L.pop())
                while len(L):
                    answer.append(L.pop())
                while len(R):
                    answer.append(R.pop())
                return answer
            
        levels = floars(root)
        m = root.val
        answer = 1
        for i in range(1,len(levels)):
            x = sum(levels[i])
            if x > m:
                m = x
                answer = i + 1
        return answer
