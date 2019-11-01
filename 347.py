# 865. Smallest Subtree with all the Deepest Nodes. Medium. 58.2%.

# Given a binary tree rooted at root, the depth of each node is the shortest distance to the root.

# A node is deepest if it has the largest depth possible among any node in the entire tree.

# The subtree of a node is that node, plus the set of all descendants of that node.

# Return the node with the largest depth such that it contains all the deepest nodes in its subtree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        depths = {}
        
        def depth(node):
            if node:
                if node in depths:
                    return depths[node]
                else:
                    depths[node] = max(depth(node.left), depth(node.right)) + 1
                    return depths[node]
            else:
                return 0
            
        def solution(node):
            if depth(node.left) > depth(node.right):
                return solution(node.left)
            elif depth(node.right) > depth(node.left):
                return solution(node.right)
            else:
                return node
        
        return solution(root) 
