#In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well. 
#At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See the following example.
#What is the maximum total sum that the height of the buildings can be increased?

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]):
        rightSL = [max(grid[i]) for i in range(len(grid))]
        bottomSL = []
        for i in range(len(grid)):
            bottomSL.append(max(grid[j][i] for j in range(len(grid))))
        total = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                total += min(rightSL[i],bottomSL[j]) - grid[i][j]
        return(total)    
