# 1139. Largest 1-Bordered Square. Medium. 44.8%.

# Given a 2D grid of 0s and 1s, return the number of elements in the largest square subgrid that has all 1s on its border, or 0 if such a subgrid doesn't exist in the grid.

class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        def check(i,j,a):
            for k in range(1,a):
                if not(grid[i + a - 1][j + k] == 1 and grid[i + k][j + a - 1] == 1):
                    return False
            return True
        
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                Flag = True
                for k in range(min(answer,len(grid) - i, len(grid[0]) - j)):
                    if not(grid[i + k][j] == 1 and grid[i][j + k] == 1):
                        Flag = False
                        break
                if Flag:
                    for k in range(answer, min(len(grid) - i, len(grid[0]) - j)):
                        if grid[i + k][j] == 1 and grid[i][j + k] == 1:
                            if check(i,j,k + 1):
                                answer = k + 1
                        else:
                            break
        return answer ** 2
