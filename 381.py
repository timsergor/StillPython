# 116. Populating Next Right Pointers in Each Node. Medium. 40.1%.

# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def solve(node):
            if node:
                l = node.left
                r = node.right
                L = []
                R = []
                while l:
                    L.append(l)
                    l = l.right
                while r:
                    R.append(r)
                    r = r.left
                for i in range(min(len(L),len(R))):
                    L[i].next = R[i]
                solve(node.left)
                solve(node.right)
        
        solve(root)
        return root
