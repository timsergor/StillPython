# 979. Distribute Coins in Binary Tree. Medium. 67.9%.

# Given the root of a binary tree with N nodes, each node in the tree has node.val coins, and there are N coins total.

# In one move, we may choose two adjacent nodes and move one coin from one node to another.  (The move may be from parent to child, or from child to parent.)

# Return the number of moves required to make every node have exactly one coin.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def mass(node):
            if not node:
                return 0
            else:
                return node.val + mass(node.left) + mass(node.right)
        
        def space(node):
            if not node:
                return 0
            else:
                return 1 + space(node.left) + space(node.right)

        def solution(node):
            if not node:
                return 0
            else:
                return abs(mass(node.left) - space(node.left)) + abs(mass(node.right) - space(node.right)) + solution(node.left) + solution(node.right)
        
        return solution(root)
