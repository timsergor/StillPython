# 1034. Coloring A Border. Medium. 43.4%.

# Given a 2-dimensional grid of integers, each value in the grid represents the color of the grid square at that location.

# Two squares belong to the same connected component if and only if they have the same color and are next to each other in any of the 4 directions.

# The border of a connected component is all the squares in the connected component that are either 4-directionally adjacent to a square not in the component, or on the boundary of the grid (the first or last row or column).

# Given a square at location (r0, c0) in the grid and a color, color the border of the connected component of that square with the given color, and return the final grid.

class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        def neir(p):
            for i in range(-1,2):
                for j in range(-1,2):
                    if abs(i + j) == 1 and p[0] + i >= 0 and p[0] + i < len(grid) and p[1] + j >= 0 and p[1] + j < len(grid[0]):
                        yield (p[0] + i, p[1] + j)
        
        now = [(r0, c0)]
        border = {}
        get = {}
        while now:
            new = []
            for p in now:
                n = list(neir(p))
                if len(n) < 4:
                    border[p] = True
                for q in n:
                    if grid[p[0]][p[1]] != grid[q[0]][q[1]]:
                        border[p] = True
                    elif q not in get:
                        new.append(q)
                get[p] = True
            now = new
        for c in border:
            grid[c[0]][c[1]] = color
        return grid
