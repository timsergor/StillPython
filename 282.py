# 129. Sum Root to Leaf Numbers. Medium. 44.1%.

# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

# An example is the root-to-leaf path 1->2->3 which represents the number 123.

# Find the total sum of all root-to-leaf numbers.

# Note: A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def height(node):
            if not node:
                return 0
            else:
                return max(height(node.left), height(node.right)) + 1
            
        def leafs(node):
            if not node:
                return 0
            if not (node.left or node.right):
                return 1
            else:
                return leafs(node.left) + leafs(node.right)
        
        def upgrate(node):
            if not node:
                pass
            elif not (node.left or node.right):
                node.val = (node.val, [0])
            else:
                if node.left and type(node.left.val) is int:
                    upgrate(node.left)
                if node.right and type(node.right.val) is int:
                    upgrate(node.right)
                if node.left and node.right:
                    theLeafs = node.left.val[1] + node.right.val[1]
                    for i in range(len(theLeafs)):
                        theLeafs[i] += 1
                    node.val = (node.val, theLeafs)
                elif node.left:
                    theLeafs = list(node.left.val[1])
                    for i in range(len(theLeafs)):
                        theLeafs[i] += 1
                    node.val = (node.val, theLeafs)
                elif node.right:
                    theLeafs = list(node.right.val[1])
                    for i in range(len(theLeafs)):
                        theLeafs[i] += 1
                    node.val = (node.val, theLeafs)
         
        upgrate(root)
        def solution(node):
            if not node:
                return 0
            s = 0
            for i in range(len(node.val[1])):
                s += node.val[0] * 10 ** node.val[1][i]
            return s + solution(node.left) + solution(node.right)
        

        return solution(root)
