# 1145. Binary Tree Coloring Game. Medium. 49.2%.

# Two players play a turn based game on a binary tree.  We are given the root of this binary tree, and the number of nodes n in the tree.  n is odd, and each node has a distinct value from 1 to n.

# Initially, the first player names a value x with 1 <= x <= n, and the second player names a value y with 1 <= y <= n and y != x.  The first player colors the node with value x red, and the second player colors the node with value y blue.

# Then, the players take turns starting with the first player.  In each turn, that player chooses a node of their color (red if player 1, blue if player 2) and colors an uncolored neighbor of the chosen node (either the left child, right child, or parent of the chosen node.)

# If (and only if) a player cannot choose such a node in this way, they must pass their turn.  If both players pass their turn, the game ends, and the winner is the player that colored more nodes.

# You are the second player.  If it is possible to choose such a y to ensure you win the game, return true.  If it is not possible, return false.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        def size(node):
            if not node:
                return 0
            return size(node.left) + size(node.right) + 1
        
        def whereTheNode(node):
            if node:
                if node.val == x:
                    return node
                a = whereTheNode(node.left)
                if a != None:
                    return a
                else:
                    return whereTheNode(node.right)
        
        node = whereTheNode(root)
        l = size(node.left)
        r = size(node.right)
        return l > n // 2 or r > n // 2 or r + l + 1 <= n // 2
