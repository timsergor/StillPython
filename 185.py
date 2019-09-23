# 73. Set Matrix Zeroes. Medium. 40.9%.

# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][j] = "*"
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "*":
                    for k in range(len(matrix)):
                        if matrix[k][j] != "*":
                            matrix[k][j] = 0
                    for k in range(len(matrix[0])):
                        if matrix[i][k] != "*":
                            matrix[i][k] = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "*":
                    matrix[i][j] = 0
        return matrix
        
# 5min.
