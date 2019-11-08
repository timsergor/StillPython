# 1162. As Far from Land as Possible. Medium. 40.1%.

# Given an N x N grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized and return the distance.

# The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

# If no land or water exists in the grid, return -1.

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        def neir(p):
            for i in range(-1,2):
                for j in range(-1,2):
                    if abs(i + j) == 1 and p[0] + i >= 0 and p[0] + i < len(grid) and p[1] + j >= 0 and p[1] + j < len(grid[0]):
                        yield (p[0] + i, p[1] + j)
                       
        S = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                S += grid[i][j]
        if S == 0 or S == len(grid) * len(grid[0]):
            return -1
        
        def border(p):
            for q in neir(p):
                if grid[q[0]][q[1]] == 0:
                    return True
            return False  
        
        layer = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and border((i,j)):
                    layer.append((i,j))
        
        answer = 0
        while layer:
            answer += 1
            new = []
            for p in layer:
                for q in neir(p):
                    if grid[q[0]][q[1]] == 0:
                        new.append(q)
                        grid[q[0]][q[1]] = answer
            layer = new
        print(grid)
        return answer - 1
