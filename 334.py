# 62. Unique Paths. Medium. 49.8%.

# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m, n = min(n,m), max(n,m)
        dyn = [1] * m
        for i in range(n - 1):
            new = [1]
            for j in range(m - 1):
                new.append(new[j] + dyn[j + 1])
            dyn = new
        return dyn[-1]
