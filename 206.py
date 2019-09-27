# 542. 01 Matrix. Medium. 36.9%.

# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

# The distance between two adjacent cells is 1.

class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    matrix[i][j] = -1
        
        def dist(point):
            if matrix[point[0]][point[1]] != 0:
                for i in range(-1,2):
                    for j in range(-1,2):
                        if abs(i + j) == 1 and point[0] + i >=0 and point[0] + i < len(matrix) and point[1] + j >= 0 and point[1] + j < len(matrix[0]) and matrix[point[0] + i][point[1] + j] >= 0:
                            if matrix[point[0]][point[1]] > 0:
                                matrix[point[0]][point[1]] = min(matrix[point[0]][point[1]],matrix[point[0] + i][point[1] + j] + 1)
                            else:
                                matrix[point[0]][point[1]] = matrix[point[0] + i][point[1] + j] + 1
                if point[0] > 0 and (matrix[point[0] - 1][point[1]] == -1 or matrix[point[0] - 1][point[1]] > matrix[point[0]][point[1]] + 1):
                    dist([point[0] - 1,point[1]])
                if point[1] > 0 and (matrix[point[0]][point[1] - 1] == -1 or matrix[point[0]][point[1] - 1] > matrix[point[0]][point[1]] + 1):
                    dist([point[0],point[1] - 1])
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dist([i,j])
        
        return matrix
