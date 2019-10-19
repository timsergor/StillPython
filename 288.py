# 773. Sliding Puzzle. Hard. 55%.

# On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.

# A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

# The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

# Given a puzzle board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

from itertools import permutations

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        code = tuple(board[0]) + tuple(board[1])
        
        def neir(i):
            if i == 0:
                return (1,3)
            elif i == 1:
                return (0,2,4)
            elif i == 2:
                return (1,5)
            elif i == 3:
                return (0,4)
            elif i == 4:
                return (1,3,5)
            else:
                return (2,4)
        
        def swap(p,i,j):
            q = []
            for k in range(len(p)):
                if k not in (i,j):
                    q.append(p[k])
                elif k == i:
                    q.append(p[j])
                else:
                    q.append(p[i])
            return tuple(q)
        
        P = permutations((0,1,2,3,4,5))
        char = {(1,2,3,4,5,0) : 0}
        new = [(1,2,3,4,5,0)]
        while new:
            sec = []
            for p in new:
                i = p.index(0)
                for j in neir(i):
                    q = swap(p,i,j)
                    if q not in char:
                        char[q] = char[p] + 1
                        sec.append(q)
            if code in char:
                return char[code]
            new = sec
        return -1
        
# 25min.
