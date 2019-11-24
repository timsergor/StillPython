# 1091. Shortest Path in Binary Matrix. Medium. 36.5%.

# In an N by N square grid, each cell is either empty (0) or blocked (1).

# A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

# Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
# C_1 is at location (0, 0) (ie. has value grid[0][0])
# C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
# If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
# Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def neir(p):
            for i in range(-1,2):
                for j in range(-1,2):
                    if (i != 0 or j != 0) and p[0] + i >= 0 and p[0] + i < len(grid) and p[1] + j >= 0 and p[1] + j < len(grid[0]):
                        yield (p[0] + i, p[1] + j)
        
        if grid[0][0]:
            return -1
        
        space = {(0,0) : 1}
        last = [(0,0)]
        t = 1
        while last and (len(grid) - 1, len(grid[0]) - 1) not in space:
            t += 1
            new = []
            for p in last:
                for q in neir(p):
                    if grid[q[0]][q[1]] == 0 and q not in space:
                        space[q] = t
                        new.append(q)
            last = new
        if (len(grid) - 1, len(grid[0]) - 1) in space:
            return space[(len(grid) - 1, len(grid[0]) - 1)]
        else:
            return -1
