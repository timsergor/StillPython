# 289. Game of Life. Medium. 48.5%.

# According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def neir(p):
            for i in range(-1,2):
                for j in range(-1,2):
                    if p[0] + i >= 0 and p[0] + i < len(board) and p[1] + j >= 0 and p[1] + j < len(board[0]) and abs(i) + abs(j) != 0:
                        yield (p[0] + i,p[1] + j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                t = 0
                for q in neir((i,j)):
                    t += board[q[0]][q[1]] % 2
                if board[i][j] == 0 and t == 3:
                    board[i][j] = 2
                elif board[i][j] == 1 and t not in [2,3]:
                    board[i][j] = 3
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 1
                if board[i][j] == 3:
                    board[i][j] = 0
