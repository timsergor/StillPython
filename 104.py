#1020. Number of Enclaves. Medium. 54.5%.

#Given a 2D array A, each cell is 0 (representing sea) or 1 (representing land)
#A move consists of walking from one land square 4-directionally to another land square, or off the boundary of the grid.
#Return the number of land squares in the grid for which we cannot walk off the boundary of the grid in any number of moves.

from queue import Queue

class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        if len(A) < 3 or len(A[0]) < 3:
            return(0)
        
        def neir(p, A):
            for i in range(-1,2):
                for j in range(-1,2):
                    if abs(i + j) == 1 and p[0] + i >= 0 and p[0] + i < len(A) and p[1] + j >= 0 and p[1] + j < len(A[0]):
                        yeild([p[0] + i, p[1] + j])
            
        outro = Queue()
        for i in range(len(A[0])):
            if A[0][i] == 1:
                A[0][i] = 2
                outro.put([0,i])
            if A[-1][i] == 1:
                A[-1][i] = 2
                outro.put([len(A) - 1, i])
        for i in range(1,len(A) - 1):
            if A[i][0] == 1:
                A[i][0] = 2
                outro.put([i,0])
            if A[i][-1] == 1:
                A[i][-1] = 2
                outro.put([i,len(A[0]) - 1])
        
        while not outro.empty():
            p = outro.get()
            for x in neir(p,A):
                if A[x[0]][x[1]] == 1:
                    A[x[0]][x[1]] = 2
                    outro.put(x)
        x = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    x += 1
        return(x)

# 55min
