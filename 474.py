# 1275. Find Winner on a Tic Tac Toe Game. Easy. 56.3%.

# Tic-tac-toe is played by two players A and B on a 3 x 3 grid.

# Here are the rules of Tic-Tac-Toe:

# Players take turns placing characters into empty squares (" ").
# The first player A always places "X" characters, while the second player B always places "O" characters.
# "X" and "O" characters are always placed into empty squares, never on filled ones.
# The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
# The game also ends if all squares are non-empty.
# No more moves can be played if the game is over.
# Given an array moves where each element is another array of size 2 corresponding to the row and column of the grid where they mark their respective character in the order in which A and B play.

# Return the winner of the game if it exists (A or B), in case the game ends in a draw return "Draw", if there are still movements to play return "Pending".

# You can assume that moves is valid (It follows the rules of Tic-Tac-Toe), the grid is initially empty and A will play first.

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        X = {}
        Y = {}
        for i in range(len(moves)):
            if i % 2:
                if moves[i][0] + moves[i][1] == 2:
                    if 1 in Y:
                        Y[1] += 1
                    else:
                        Y[1] = 1
                if moves[i][0] - moves[i][1] == 0:
                    if 2 in Y:
                        Y[2] += 1
                    else:
                        Y[2] = 1
                if (0, moves[i][0]) in Y:
                    Y[(0, moves[i][0])] += 1
                else:
                    Y[(0, moves[i][0])] = 1
                if (1, moves[i][1]) in Y:
                    Y[(1, moves[i][1])] += 1
                else:
                    Y[(1, moves[i][1])] = 1
            else:
                if moves[i][0] + moves[i][1] == 2:
                    if 1 in X:
                        X[1] += 1
                    else:
                        X[1] = 1
                if moves[i][0] - moves[i][1] == 0:
                    if 2 in X:
                        X[2] += 1
                    else:
                        X[2] = 1
                if (0, moves[i][0]) in X:
                    X[(0, moves[i][0])] += 1
                else:
                    X[(0, moves[i][0])] = 1
                if (1, moves[i][1]) in X:
                    X[(1, moves[i][1])] += 1
                else:
                    X[(1, moves[i][1])] = 1
        for c in X:
            if X[c] == 3:
                return "A"
        for c in Y:
            if Y[c] == 3:
                return "B"
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"
