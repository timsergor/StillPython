#513. Find Bottom Left Tree Value. Medium.
#Given a binary tree, find the leftmost value in the last row of the tree.

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        def height(node):
            if node == None:
                return -1
            else:
                return max(height(node.left), height(node.right)) + 1
        
        def find(node):
            if not (node.left or node.right):
                return node.val
            elif height(node.left) >= height(node.right):
                return find(node.left)
            else:
                return find(node.right)
        
        return find(root)
        
# < 10min.
