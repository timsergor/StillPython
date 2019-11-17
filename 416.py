# 1261. Find Elements in a Contaminated Binary Tree. Medium. Contest.

# Given a binary tree with the following rules:

# root.val == 0
# If treeNode.val == x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
# If treeNode.val == x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
# Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.

# You need to first recover the binary tree and then implement the FindElements class:

# FindElements(TreeNode* root) Initializes the object with a contamined binary tree, you need to recover it first.
# bool find(int target) Return if the target value exists in the recovered binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements:

    def __init__(self, root: TreeNode):
        self.values = set()
        
        def recover(node, x):
            if node:
                node.val = x
                self.values.add(x)
                recover(node.left, 2 * x + 1)
                recover(node.right, 2 * x + 2)
        
        recover(root, 0)
        

    def find(self, target: int) -> bool:
        return target in self.values
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
