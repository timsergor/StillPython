# 1260. Shift 2D Grid. Easy. Contest.

# Given a 2D grid of size n * m and an integer k. You need to shift the grid k times.

# In one shift operation:

# Element at grid[i][j] becomes at grid[i][j + 1].
# Element at grid[i][m - 1] becomes at grid[i + 1][0].
# Element at grid[n - 1][m - 1] becomes at grid[0][0].
# Return the 2D grid after applying shift operation k times.

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def shift(grid):
            new = []
            for i in range(len(grid)):
                new.append([grid[(i - 1) % len(grid)][-1]] + grid[i][:len(grid[0]) - 1])
            return new
        
        for i in range(k):
            grid = shift(grid)
        return grid
        
        """if k == 0:
            return grid
        answer = []
        if len(grid[0]) == 1:
            for i in range(len(grid)):
                answer.append(grid[(i - k) % len(grid)])  
        else:
            for i in range(len(grid)):
                answer.append([])
                for j in range(len(grid[0])):
                    answer[-1].append(grid[(i - len(grid[0]) // k - int(j < k % len(grid[0]))) % len(grid)][(j - k) % len(grid[0])])
        return answer"""
