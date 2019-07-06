#Given the root of a binary search tree with distinct values, modify it so that every node has a new value equal to the sum of the values of the original tree that are greater than or equal to node.val.

#As a reminder, a binary search tree is a tree that satisfies these constraints:
#The left subtree of a node contains only nodes with keys less than the node's key.
#The right subtree of a node contains only nodes with keys greater than the node's key.
#Both the left and right subtrees must also be binary search trees.

#не на всех примерах сработал

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode):
        sum = 0
        trace = 0
        arrow = [root]
        current = root
        while arrow and len(arrow) < 7:
            if trace == 0:
                if current.right:
                    arrow.append(current.right)
                    current = current.right
                    trace = 1
                elif current.left:
                    sum += current.val
                    arrow.append(current.left)
                    current = current.left
                    trace = 2
                else:
                    return(root)
            elif trace == 1:
                if current.right:
                    arrow.append(current.right)
                    current = current.right
                elif current.left:
                    current.val += sum
                    sum = current.val
                    arrow.append(current.left)
                    current = current.left
                    trace = 2
                else:                    
                    current = arrow.pop()
                    current.val += sum
                    sum = current.val
                    current = arrow[len(arrow)-1]
                    trace = 4
            elif trace == 2:
                if current.right:
                    arrow.append(current.right)
                    current = current.right
                    trace = 1
                elif current.left:
                    current.val += sum
                    sum = current.val
                    arrow.append(current.left)
                    current = current.left
                else:                    
                    current = arrow.pop()
                    current.val += sum
                    sum = current.val
                    current = arrow[len(arrow)-1]
                    trace = 3
            elif trace == 4:
                if current.left:
                    current.val += sum
                    sum = current.val
                    arrow.append(current.left)
                    current = arrow[len(arrow)-1]
                    trace = 2
                else:                    
                    current.val += sum
                    sum = current.val
                    if len(arrow) == 1:
                        return(root)
                    else:
                        last = current
                        arrow.pop()
                        current = arrow[len(arrow)-1]
                        if current.left == last:
                            trace = 3
            elif trace == 3:
                    last = arrow.pop()
                    if len(arrow) == 0:
                        return(root)
                    current = arrow[len(arrow)-1]    
                    if current.left != last:
                        trace = 4       
        return(root) 
