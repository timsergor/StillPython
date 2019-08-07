#235. Lowest Common Ancestor of a Binary Search Tree. Easy. 45.6%

#Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
#According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def solution(root, p, q):
            if p.val > q.val:
                a, b = q.val, p.val
            else:
                a, b = p.val, q.val
            if root.val >= a and root.val <= b:
                return(root)
            elif root.val > b:
                root = root.left
                return(solution(root,p,q))
            else:
                root = root.right
                return(solution(root,p,q))
        return(solution(root,p,q))
