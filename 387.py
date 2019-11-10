# 1254. Number of Closed Islands. Medium. Contest.

# Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

# Return the number of closed islands.

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def neir(p):
            for i in range(-1,2):
                for j in range(-1,2):
                    if abs(i + j) == 1 and p[0] + i >= 0 and p[0] + i < len(grid) and p[1] + j >= 0 and p[1] + j < len(grid[0]):
                        yield (p[0] + i, p[1] + j)
        
        char = {}
        answer = 0
        
        def check(p):
            if grid[p[0]][p[1]] == 0 and p not in char:
                Flag = True
                char[p] = True
                now = [p]
                while now:
                    new = []
                    for q in now:
                        l = list(neir(q))
                        if len(l) < 4:
                            Flag = False
                        for r in l:
                            if grid[r[0]][r[1]] == 0 and r not in char:
                                new.append(r)
                            char[r] = True
                    now = new
                return Flag
            else:
                return False
                        

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if check((i,j)):
                    answer += 1
        return answer
