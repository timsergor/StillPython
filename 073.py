#1110. Delete Nodes And Return Forest. Medium. 63.2%.

#Given the root of a binary tree, each node in the tree has a distinct value.
#After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).
#Return the roots of the trees in the remaining forest.  You may return the result in any order.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]):
        def clean(Node):
            if Node == None:
                return(None)
            if Node.left and Node.left.val in to_delete:
                Node.left = None
            if Node.right and Node.right.val in to_delete:
                Node.right = None
            Node.left = clean(Node.left)
            Node.right = clean(Node.right)
            return(Node)
        
        def check(Node, Flag):
            if Node == None:
                return([])
            elif Node.val in to_delete:
                A = check(Node.left, True)
                A.extend(check(Node.right, True))
                return(A)
            else:
                print(Node.val)
                if Flag:
                    A = check(Node.left, False)
                    A.extend(check(Node.right, False))
                    A.append(clean(Node))
                    return(A)
                else:
                    A = check(Node.left, False)
                    A.extend(check(Node.right, False))
                    return(A)
            return([])
        return(check(root,True))
