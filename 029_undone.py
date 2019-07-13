# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        root = TreeNode(preorder[0])
        route = [root]
        node = root
        greatest = root.val
        i = 1
        while i < len(preorder):
            if preorder[i] < node.val:
                node.left = TreeNode(preorder[i])
                node = node.left
                route.append(node)
                i += 1
#            elif len(route) == 1 or route[len(route) - 2].val > preorder[i]:
            elif node.val == greatest:
                node.right = TreeNode(preorder[i])
                node = node.right
                route.append(node)
                i += 1
            else:
                route.pop()
                node = route[len(route)-1]
        return(root)  
