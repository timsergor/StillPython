# 590. N-ary Tree Postorder Traversal

# Given an n-ary tree, return the postorder traversal of its nodes' values.

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        answer = []
        
        def solution(node):
            if node:
                for c in node.children:
                    solution(c)
                answer.append(node.val)
        
        solution(root)
        return answer
