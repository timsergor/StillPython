# 766. Toeplitz Matrix. Easy. 62.8%.

# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

# Now given an M x N matrix, return True if and only if the matrix is Toeplitz.

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(- len(matrix) + 1, len(matrix[0])):
            for j in range(len(matrix)):
                if i + j == 0 or (i > 0 and j == 0):
                    x = matrix[j][i + j]
                elif i + j > 0 and i + j < len(matrix[0]) and j and matrix[j][i + j] != x:
                    return False
        return True    
