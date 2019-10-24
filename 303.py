304. Range Sum Query 2D - Immutable. Medium. 34.7%.

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.summ = matrix
        for i in range(len(matrix)):
            for j in range(1,len(matrix[0])):
                matrix[i][j] += matrix[i][j - 1]
        for i in range(1,len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] += matrix[i - 1][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        S = self.summ[row2][col2]
        if row1 > 0:
            S -= self.summ[row1 - 1][col2]
        if col1 > 0:
            S -= self.summ[row2][col1 - 1]
        if row1 > 0 and col1 > 0:
            S += self.summ[row1 - 1][col1 - 1]
        return S


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# 12min.
