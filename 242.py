# 1080. Insufficient Nodes in Root to Leaf Paths. Medium. 44.4%.

# Given the root of a binary tree, consider all root to leaf paths: paths from the root to any leaf.  (A leaf is a node with no children.)

# A node is insufficient if every such root to leaf path intersecting this node has sum strictly less than limit.

# Delete all insufficient nodes simultaneously, and return the root of the resulting binary tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sufficientSubset(self, root, limit):
        """
        :type root: TreeNode
        :type limit: int
        :rtype: TreeNode
        """
        delete = {}
        def toDel(Node, s, limit):
            if Node in delete or not Node:
                pass
            else:
                if not Node.left and not Node.right:
                    if s + Node.val < limit:
                        delete[Node] = True
                elif (not Node.left or Node.left in delete) and (not Node.right or Node.right in delete):
                    delete[Node] = True
                else:
                    toDel(Node.left, s + Node.val, limit)
                    toDel(Node.right, s + Node.val, limit)
        
        while True:
            l = len(delete)
            toDel(root,0,limit)
            if l == len(delete):
                break
        
        if root in delete:
            return None
        
        def Del(Node):
            if not Node:
                pass
            else:
                if Node.left in delete:
                    Node.left = None
                else:
                    Del(Node.left)
                if Node.right in delete:
                    Node.right = None
                else:
                    Del(Node.right)
        
        Del(root)
        return root
