# 589. N-ary Tree Preorder Traversal. Easy. 69.3%.

# Given an n-ary tree, return the preorder traversal of its nodes' values.

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        answer = []
        
        def solve(node):
            if node:
                answer.append(node.val)
                for c in node.children:
                    solve(c)
        
        solve(root)
        return answer
