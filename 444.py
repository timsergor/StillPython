# 1267. Count Servers that Communicate. Medium. Contest.

# You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

# Return the number of servers that communicate with any other server.

class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        x = {}
        y = {}
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    if i in x:
                        x[i] += 1
                    else:
                        x[i] = 1
                    if j in y:
                        y[j] += 1
                    else:
                        y[j] =1
                    answer += 1
                else:
                    if i not in x:
                        x[i] = 0
                    if j not in y:
                        y[j] = 0
        print(answer, x, y)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and x[i] == 1 and y[j] == 1:
                    answer -= 1
        return answer
