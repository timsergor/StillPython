#1123. Lowest Common Ancestor of Deepest Leaves. Medium. 64.4%.

#Given a rooted binary tree, return the lowest common ancestor of its deepest leaves.
#Recall that:
#The node of a binary tree is a leaf if and only if it has no children
#The depth of the root of the tree is 0, and if the depth of a node is d, the depth of each of its children is d+1.
#The lowest common ancestor of a set S of nodes is the node A with the largest depth such that every node in S is in the subtree with root A.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def hieght(Node):
            if Node == None:
                return(-1)
            if not (Node.right or Node.left):
                return(0)
            else:
                return(1 + max(hieght(Node.left), hieght(Node.right)))
            
        def solution(Node):
            L = hieght(Node.left) 
            R = hieght(Node.right)
            if L == R:
                return(Node)
            elif L > R:
                return(solution(Node.left))
            else:
                return(solution(Node.right))
        
        return(solution(root))
        
 # 15 min
