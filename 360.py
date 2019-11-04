# 64. Minimum Path Sum. Medium. 49.3%.

# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid) + len(grid[0]) - 1):
            for j in range(len(grid)):
                if i - j < len(grid[0]) and i - j >= 0:
                    if i - j > 0 and j > 0:
                        grid[j][i - j] += min(grid[j][i - j - 1], grid[j - 1][i - j])
                    elif i - j > 0:
                        grid[j][i - j] += grid[j][i - j - 1]
                    elif j > 0:
                        grid[j][i - j] += grid[j - 1][i - j]
        return grid[-1][-1]
