# 861. Score After Flipping Matrix. Medium. 70.4%

# We have a two dimensional matrix A where each value is 0 or 1.
# A move consists of choosing any row or column, and toggling each value in that row or column: changing all 0s to 1s, and all 1s to 0s.
# After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.
# Return the highest possible score.

class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        def row(A,i):
            for j in range(len(A[i])):
                A[i][j] = 1 - A[i][j]
            return(A)

        def col(A,i):
            for j in range(len(A)):
                A[j][i] = 1 - A[j][i]
            return(A)
        
        def colsum(A,i):
            s = 0
            for j in range(len(A)):
                s += A[j][i]
            return(s)
        
        T = 2**(len(A[0]) - 1)
        S = T*len(A)
        for i in range(len(A)):
            if A[i][0] == 0:
                A = row(A,i)
                
        for j in range(1,len(A[0])):
            T //= 2
            s = colsum(A,j)
            if s < len(A)/2:
                S += T * (len(A) - s)
            else:
                S += T * s
        return(S)
