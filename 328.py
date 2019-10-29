# 173. Binary Search Tree Iterator. Medium. 51.3%.

# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

# Calling next() will return the next smallest number in the BST.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.path = []

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if not self.path:
            self.path.append(self.root)
            while self.path[-1].left:
                self.path.append(self.path[-1].left)
            return self.path[-1].val
        elif self.path[-1].right:
            self.path.append(self.path[-1].right)
            while self.path[-1].left:
                self.path.append(self.path[-1].left)
            return self.path[-1].val
        else:
            node = self.path.pop()
            while self.path[-1].right == node:
                node = self.path.pop()
            return self.path[-1].val
            

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if not self.path:
            return bool(self.root)
        if self.path[-1].right:
            return True
        else:
            t = len(self.path) - 2
            while t >= 0 and self.path[t].right == self.path[t + 1]:
                t -= 1
            return t != -1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
