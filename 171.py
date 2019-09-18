# 508. Most Frequent Subtree Sum. Medium. 55.4%.

# Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        char = {}
        def treeSum(node):
            if node == None:
                return 0
            else:
                return treeSum(node.left) + node.val + treeSum(node.right)
        
        def addSum(node):
            S = treeSum(node)
            if S not in char:
                char[S] = 1
            else:
                char[S] += 1
            if node.left:
                addSum(node.left)
            if node.right:
                addSum(node.right)
        
        addSum(root)
        max = 0
        answer = []
        for c in char:
            if char[c] > max:
                max = char[c]
        for c in char:
            if char[c] == max:
                answer.append(c)
        return answer
