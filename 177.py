# 59. Spiral Matrix II. Medium. 48.3%.

# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ma = [0] * n
        map = []
        for i in range(n):
            map.append(list(ma))
        head = [0,0]
        score = 1
        d = 0
        Flag = 0
        while Flag < 2:
            if d == 0:
                if head[1] + 1 < n and map[head[0]][head[1] + 1] == 0:
                    map[head[0]][head[1]] = score
                    score += 1
                    head[1] += 1
                    Flag = 0
                else:
                    d = (d + 1) % 4
                    Flag += 1
            elif d == 1:
                if head[0] + 1 < n and map[head[0] + 1][head[1]] == 0:
                    map[head[0]][head[1]] = score
                    score += 1
                    head[0] += 1
                    Flag = 0
                else:
                    d = (d + 1) % 4
                    Flag += 1
            elif d == 2:
                if head[1] - 1 >= 0 and map[head[0]][head[1] - 1] == 0:
                    map[head[0]][head[1]] = score
                    score += 1
                    head[1] -= 1
                    Flag = 0
                else:
                    d = (d + 1) % 4
                    Flag += 1
            elif d == 3:
                if head[0] - 1 >= 0 and map[head[0] - 1][head[1]] == 0:
                    map[head[0]][head[1]] = score
                    score += 1
                    head[0] -= 1
                    Flag = 0
                else:
                    d = (d + 1) % 4
                    Flag += 1
        map[head[0]][head[1]] = score
        
# 17-18min
