# 1277. Count Square Submatrices with All Ones. Medium. Contest.

# Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        for i in range(len(matrix)):
            matrix[i].reverse()
            matrix[i].append(0)
            matrix[i].reverse()
        matrix.reverse()
        matrix.append([0] * len(matrix[0]))
        matrix.reverse()
        answer = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i and j:
                    matrix[i][j] = matrix[i][j] + matrix[i][j - 1] + matrix[i - 1][j] - matrix[i - 1][j - 1]
                elif i:
                    matrix[i][j] = matrix[i][j] + matrix[i - 1][j]
                elif j:
                    matrix[i][j] = matrix[i][j] + matrix[i][j - 1]
                for k in range(1, min(i,j) + 1):
                    if i and j and matrix[i][j] - matrix[i - k][j] - matrix[i][j - k] + matrix[i - k][j - k] == k ** 2:
                        answer += 1
                    else:
                        break
        return answer
