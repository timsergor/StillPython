#695. Max Area of Island. Medium. 58.4%.

#Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
#Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        theArea = 0
        def neir(grid, point):
            for i in range(-1,2):
                for j in range(-1,2):
                    if abs(i + j) == 1 and point[0] + i >= 0 and point[0] + i < len(grid) and point[1] + j >= 0 and point[1] + j < len(grid[0]):
                        yield((point[0] + i,point[1] + j))
        
        def observe(grid, point):
            if grid[point[0]][point[1]] != 1:
                return(0)
            else:
                area = 1
                grid[point[0]][point[1]] = 2
                for another in neir(grid, point):
                    area += observe(grid, another)
                return(area)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                theArea = max(theArea, observe(grid,(i,j)))
        return(theArea)
        
# 15min.
