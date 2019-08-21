#437. Path Sum III. Easy. 43.5%.

#You are given a binary tree in which each node contains an integer value.
#Find the number of paths that sum to a given value.
#The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
#The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        counter = 0
        char = {}
        def solution(root, s):
            if root == None:
                pass
            else:
                s += root.val
                if s == sum:
                    nonlocal counter
                    counter += 1
                solution(root.left, s)
                if root.left not in char:
                    solution(root.left, 0)
                    char[root.left] = True
                solution(root.right, s)
                if root.right not in char:
                    solution(root.right, 0)
                    char[root.right] = True
        
        solution(root, 0)
        return(counter)
