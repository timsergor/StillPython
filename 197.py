# 103. Binary Tree Zigzag Level Order Traversal. Medium. 43.3%.

# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def floors(node):
            if node == None:
                return []
            L = floors(node.left)
            R = floors(node.right)
            answer = [[node.val]]
            for i in range(len(L)):
                if i < len(R):
                    answer.append(L[i] + R[i])
                else:
                    answer.append(L[i])
            if len(R) > len(L):
                for i in range(len(L),len(R)):
                    answer.append(R[i])
            return answer
        
        M = floors(root)
        for i in range(len(M)):
            if i % 2:
                M[i].reverse()
        return M
