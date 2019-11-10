# 980. Unique Paths III. Hard. 71.5%.

# On a 2-dimensional grid, there are 4 types of squares:

# 1 represents the starting square.  There is exactly one starting square.
# 2 represents the ending square.  There is exactly one ending square.
# 0 represents empty squares we can walk over.
# -1 represents obstacles that we cannot walk over.
# Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

from queue import Queue

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        space = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    p = (i, j)
                elif grid[i][j] == 0:
                    space += 1
        
        def neir(p):
            for i in range(-1,2):
                for j in range(-1,2):
                    if abs(i + j) == 1 and p[0] + i >= 0 and p[0] + i < len(grid) and p[1] + j >= 0 and p[1] + j < len(grid[0]):
                        yield((p[0] + i, p[1] + j))
        
        answer = 0
        flow = Queue()
        flow.put((set(),p))
        while not flow.empty():
            now = flow.get()
            path = now[0].union(set([now[1]]))
            if len(path) > space:
                for q in neir(now[1]):
                    if grid[q[0]][q[1]] == 2:
                        answer += 1
            else:
                for q in neir(now[1]):
                    if q not in path and grid[q[0]][q[1]] == 0:
                        flow.put((path, q))
        return answer
