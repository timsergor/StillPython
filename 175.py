# 200. Number of Islands. Medium. 42.9%

# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def virus(point):
            if grid[point[0]][point[1]] == "1":
                grid[point[0]][point[1]] = "2"
                for i in range(-1,2):
                    for j in range(-1,2):
                        if abs(i + j) == 1 and point[0] + i >= 0 and point[0] + i < len(grid) and point[1] + j >= 0 and point[1] + j < len(grid[0]):
                            virus((point[0] + i, point[1] + j))
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    answer += 1
                virus((i,j))
        return answer
