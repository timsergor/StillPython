# 498. Diagonal Traverse. Medium. 46.2%.

# Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        head = [0,0]
        state = 1
        answer = []
        if matrix:
            while not (head[0] == len(matrix) - 1 and head[1] == len(matrix[0]) - 1):
                answer.append(matrix[head[0]][head[1]])
                if state:
                    if head[0] > 0 and head[1] < len(matrix[0]) - 1:
                        head = [head[0] - 1, head[1] + 1]
                    elif head[1] == len(matrix[0]) - 1:
                        head = [head[0] + 1, head[1]]
                        state = 0
                    else:
                        head = [0, head[1] + 1]
                        state = 0
                else:
                    if head[0] < len(matrix) - 1 and head[1] > 0:
                        head = [head[0] + 1, head[1] - 1]
                    elif head[0] == len(matrix) - 1:
                        head = [head[0], head[1] + 1]
                        state = 1
                    else:
                        head = [head[0] + 1, 0]
                        state = 1
            answer.append(matrix[head[0]][head[1]])
        return answer
