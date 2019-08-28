118. Pascal's Triangle. Easy. 47.6%.

#Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return([])
        Pascal = [[1]]
        for i in range(1, numRows):
            next = list(Pascal[-1])
            for j in range(i):
                if j + 1 < i:
                    next[j + 1] += Pascal[-1][j]
                else:
                    next.append(1)
            Pascal.append(next)
        return Pascal
        
# 8min.
