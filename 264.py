# 827. Making A Large Island. Hard. 44%.

# In a 2D grid of 0s and 1s, we change at most one 0 to a 1.

# After, what is the size of the largest island? (An island is a 4-directionally connected group of 1s).

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        t = 2
        size = {0:0}
        def neir(p):
            for i in range(-1,2):
                for j in range(-1,2):
                    if abs(i + j) == 1 and p[0] + i >= 0 and p[0] + i < len(grid) and p[1] + j >= 0 and p[1] + j < len(grid[0]):
                        yield (p[0] + i, p[1] + j)
        
        def conquer(p, t):
            grid[p[0]][p[1]] = t
            size[t] += 1
            for q in neir(p):
                if grid[q[0]][q[1]] == 1:
                    conquer(q, t)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    size[t] = 0
                    conquer((i,j),t)
                    t += 1
        
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    can = []
                    for p in neir((i,j)):
                        can.append(grid[p[0]][p[1]])
                    can = set(can)
                    land = 1
                    for isl in can:
                        land += size[isl]
                    answer = max(answer,land)
                else:
                    answer = max(answer,size[grid[i][j]])
        return answer
        
# 25min
