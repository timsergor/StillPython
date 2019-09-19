# 130. Surrounded Regions. Medium. 24%.

# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return []
        def capture(point, S1, S2):
            if board[point[0]][point[1]] == S1:
                board[point[0]][point[1]] = S2
                for i in range(-1,2):
                    for j in range(-1,2):
                        if abs(i + j) == 1 and point[0] + i >= 0 and point[0] + i < len(board) and point[1] + j >= 0 and point[1] + j < len(board[0]):
                            capture((point[0] + i, point[1] + j), S1, S2)
        
        for i in range(len(board)):
            capture([i,0],"O","I")
            capture([i,len(board[0]) - 1],"O","I")
        for i in range(1,len(board[0]) - 1):
            capture([0,i],"O","I")
            capture([len(board) - 1,i],"O","I")
            
        for i in range(1,len(board) - 1):
            for j in range(1,len(board[0]) - 1):
                capture([i,j],"O","X")
        
        for i in range(len(board)):
            capture([i,0],"I","O")
            capture([i,len(board[0]) - 1],"I","O")
        for i in range(1,len(board[0]) - 1):
            capture([0,i],"I","O")
            capture([len(board) - 1,i],"I","O")
        return board
