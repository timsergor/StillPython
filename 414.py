# 988. Smallest String Starting From Leaf. Medium. 44.9%.

# Given the root of a binary tree, each node has a value from 0 to 25 representing the letters 'a' to 'z': a value of 0 represents 'a', a value of 1 represents 'b', and so on.

# Find the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

# (As a reminder, any shorter prefix of a string is lexicographically smaller: for example, "ab" is lexicographically smaller than "aba".  A leaf of a node is a node that has no children.)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        answer = None
        
        def solution(node, pre):
            if not(node.left) and not(node.right):
                now = pre + [chr(node.val + ord("a"))]
                now.reverse()
                x = "".join(now)
                nonlocal answer
                if answer == None or x < answer:
                    answer = x
            else:
                if node.left:
                    solution(node.left, pre + [chr(node.val + ord("a"))])
                if node.right:
                    solution(node.right, pre + [chr(node.val + ord("a"))])
        
        solution(root, [])
        return answer
