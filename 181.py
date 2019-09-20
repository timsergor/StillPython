# 120. Triangle

# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

# For example, given the following triangle

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 0:
            return 0
        for i in range(1,len(triangle)):
            for j in range(i + 1):
                if j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                elif j == i:
                    triangle[i][j] += triangle[i - 1][j - 1]
                else:
                    triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j]) 
        return min(triangle[-1])
