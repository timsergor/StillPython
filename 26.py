#Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

#The root is the maximum number in the array.
#The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
#The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
#Construct the maximum tree by the given array and output the root node of this tree.

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def getMBT(list):
            m = max(list)
            i = list.index(m)
            left = list[0:i]
            right = list[i+1:len(list)]
            T = TreeNode(m)
            if len(left) > 0:
                T.left = getMBT(left)
            if len(right) > 0:
                T.right = getMBT(right)
            return(T)
        return(getMBT(nums))
