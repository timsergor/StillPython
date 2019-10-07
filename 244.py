# 463. Island Perimeter. Easy. 61.9%.

# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def per(cell):
            if grid[cell[0]][cell[1]] == 0:
                return 0
            p = 0
            for i in range(-1,2):
                for j in range(-1,2):
                    if abs(i + j) == 1 and (cell[0] + i < 0 or cell[0] + i >= len(grid) or cell[1] + j < 0 or cell[1] + j >= len(grid[0]) or grid[cell[0] + i][cell[1] + j] == 0):
                        p += 1
            return p
        
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                answer += per((i,j))
        
        return answer
