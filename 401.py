# 96. Unique Binary Search Trees. Medium. 48.5%.

# Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dyn = [1,1,2]
        for i in range(3, n + 1):
            new = 0
            for j in range(len(dyn)):
                new += dyn[j] * dyn[-1 - j]
            dyn.append(new)
        return dyn[n]
