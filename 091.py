#671. Second Minimum Node In a Binary Tree. Easy. 43.1%.

#Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.
#Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.
#If no such second minimum value exists, output -1 instead.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        def solution(node, n):
            if not (node.left or node.right):
                return(node.val)
            else:
                if node.val > n:
                    return(node.val)
                else:
                    a = solution(node.left, node.val)
                    b = solution(node.right, node.val)
                    if max(a,b) == node.val:
                        return(node.val)
                    elif min(a,b) != node.val:
                        return(min(a,b))
                    else:
                        return(max(a,b))
        
        x =solution(root, root.val)
        if root.val == x:
            return(-1)
        else:
            return(x)
