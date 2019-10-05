# 976. Largest Perimeter Triangle

# Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.

# If it is impossible to form any triangle of non-zero area, return 0.

class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        for i in range(len(A)-1,1,-1):
            if A[-1] >= A[-2] + A[-3]:
                A.pop()
            else:
                return A[-1] + A[-2] + A[-3]
        return 0
