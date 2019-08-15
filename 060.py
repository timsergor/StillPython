#419. Battleships in a Board. Medium. 66.3%
#Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:
#You receive a valid board, made of only battleships or empty slots.
#Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
#At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def up(board,i,j):
            if i == 0:
                return(False)
            elif board[i-1][j] == "X":
                return(True)
            return(False)
        
        def left(board,i,j):
            if j == 0:
                return(False)
            elif board[i][j-1] == "X":
                return(True)
            return(False)
            
        ships = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X" and not left(board,i,j) and not up(board,i,j):
                    ships += 1
        return(ships)
