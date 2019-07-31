#994. Rotting Oranges. 46.5%

#In a given grid, each cell can have one of three values:
#the value 0 representing an empty cell;
#the value 1 representing a fresh orange;
#the value 2 representing a rotten orange.
#Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
#Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

from copy import deepcopy

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def MinuteLater(grid):
            newgrid = deepcopy(grid)
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == 1 and (((i > 0) and (grid[i-1][j] == 2)) or ((i < len(grid)-1) and (grid[i+1][j] == 2)) or ((j > 0) and (grid[i][j-1] == 2)) or ((j < len(grid[i]) - 1) and (grid[i][j+1] == 2))):
                        newgrid[i][j] = 2
            return(newgrid)
        
        def AnyFresh(grid):
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == 1:
                        return(True)
            return(False)
                                                                                        
        t = 0
        while (AnyFresh(grid)) and (t <= len(grid) * len(grid[0]) + 1):
            grid = MinuteLater(grid)
            t += 1
        if t > len(grid) * len(grid[0]):
            return(-1)
        else:
            return(t)
