# 652. Find Duplicate Subtrees. 47.8%.

# Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

# Two trees are duplicate if they have the same structure with same node values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        char = {}
        get = {}
        answer = set()
        
        def code(node):
            if not node:
                return ()
            if node in char:
                return char[node]
            char[node] = (node.val, code(node.left), code(node.right))
            return char[node]
        
        def absorb(node):
            if node:
                absorb(node.left)
                absorb(node.right)
                if code(node) in get:
                    get[code(node)] += 1
                    if get[code(node)] == 2:
                        answer.add(node)
                else:
                    get[code(node)] = 1
        
        absorb(root)
        return list(answer)
