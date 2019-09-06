# 54. Spiral Matrix. 31.3%.

# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        answer = []
        point = [0,0]
        trace = -1
        while len(answer) < len(matrix) * len(matrix[0]) - 1:
            if trace < 1:
                if point[1] + 1 < len(matrix[0]) and matrix[point[0]][point[1] + 1] != "*":
                    answer.append(matrix[point[0]][point[1]])
                    matrix[point[0]][point[1]] = "*"
                    point[1] += 1
                else:
                    trace = (trace + 1) % 4
            elif trace == 1:
                if point[0] + 1 < len(matrix) and matrix[point[0] + 1][point[1]] != "*":
                    answer.append(matrix[point[0]][point[1]])
                    matrix[point[0]][point[1]] = "*"
                    point[0] += 1
                else:
                    trace = (trace + 1) % 4
            elif trace == 2:
                if point[1] - 1 >= 0 and matrix[point[0]][point[1] - 1] != "*":
                    answer.append(matrix[point[0]][point[1]])
                    matrix[point[0]][point[1]] = "*"
                    point[1] -= 1
                else:
                    trace = (trace + 1) % 4
            elif trace == 3:
                if point[0] - 1 >= 0 and matrix[point[0] - 1][point[1]] != "*":
                    answer.append(matrix[point[0]][point[1]])
                    matrix[point[0]][point[1]] = "*"
                    point[0] -= 1
                else:
                    trace = (trace + 1) % 4
        answer.append(matrix[point[0]][point[1]])
        return answer
        
# 20-25min.
