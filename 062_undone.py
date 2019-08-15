# 980. Unique Paths III. Hard. 71.3%

#On a 2-dimensional grid, there are 4 types of squares:

#1 represents the starting square.  There is exactly one starting square.
#2 represents the ending square.  There is exactly one ending square.
#0 represents empty squares we can walk over.
#-1 represents obstacles that we cannot walk over.
#Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

from multiprocessing import Queue

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        H = len(grid)
        L = len(grid[0])
        
        def next(coord):
            i = coord[0]
            j = coord[1]
            N = []
            if i > 0:
                N.append((i - 1, j))
            if j > 0:
                N.append((i, j - 1))
            if j < L - 1:
                N.append((i, j + 1))
            if i < H - 1:
                N.append((i + 1, j))
            return(N)
        
        space = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    space += 1
                elif grid[i][j] == 1:
                    start = (i,j)
                elif grid[i][j] == 2:
                    finish = (i,j)
        
        paths = Queue()
        paths.put([start])
        TheWay = []
        while paths:
            Now = paths.get()
            if len(Now) <= space:
                for way in next(Now[len(Now) - 1]):
                    if grid[way[0]][way[1]] == 0 and way not in Now:
                        New = list(Now)
                        New.append(way)
                        paths.put(New)
            else:
                for way in next(Now[len(Now) - 1]):
                    if way == finish:
                        TheWay.append(Now.append(way))
        return(len(TheWay))
