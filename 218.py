# 814. Binary Tree Pruning. Medium. 71.9%.

# We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.

# Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

# (Recall that the subtree of a node X is X, plus every node that is a descendant of X.)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def check(node):
            if not node:
                return False
            if node.val:
                return True
            else:
                return check(node.left) or check(node.right)
        
        def solution(node):
            F = check(node)
            if not F:
                return None
            else:
                if check(node.left):
                    node.left = solution(node.left)
                else:
                    node.left = None
                if check(node.right):
                    node.right = solution(node.right)
                else:
                    node.right = None
                return node
        
        return solution(root)
