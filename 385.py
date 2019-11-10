# 1252. Cells with Odd Values in a Matrix. Easy. Contest.

# Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices where indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.

# Return the number of cells with odd values in the matrix after applying the increment to all indices.

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        x = {}
        y = {}
        for i in range(len(indices)):
            if indices[i][0] in x:
                x.pop(indices[i][0])
            else:
                x[indices[i][0]] = True
            if indices[i][1] in y:
                y.pop(indices[i][1])
            else:
                y[indices[i][1]] = True
        print(x,y)
        return (m * len(x)) + (n * len(y)) - 2 * len(x) * len(y)
