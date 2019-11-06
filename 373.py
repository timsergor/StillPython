# 1138. Alphabet Board Path. Medium. 44.7%.

# On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].

# Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"].

# We may make the following moves:

# 'U' moves our position up one row, if the position exists on the board;
# 'D' moves our position down one row, if the position exists on the board;
# 'L' moves our position left one column, if the position exists on the board;
# 'R' moves our position right one column, if the position exists on the board;
# '!' adds the character board[r][c] at our current position (r, c) to the answer.
# (Here, the only positions that exist on the board are positions with letters on them.)

# Return a sequence of moves that makes our answer equal to target in the minimum number of moves.  You may return any path that does so.



class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        char = {}
        for i in range(26):
            char[chr(ord("a") + i)] = (i // 5, i % 5)
        pre = []
        
        def path(a,b):
            if char[a][0] == char[b][0]:
                if char[a][1] < char[b][1]:
                    for i in range(char[b][1] - char[a][1]):
                        pre.append("R")
                else:
                    for i in range(char[a][1] - char[b][1]):
                        pre.append("L")
            elif char[a][0] > char[b][0]:
                for i in range(char[a][0] - char[b][0]):
                    pre.append("U")
                if char[a][1] < char[b][1]:
                    for i in range(char[b][1] - char[a][1]):
                        pre.append("R")
                else:
                    for i in range(char[a][1] - char[b][1]):
                        pre.append("L")
            else:
                if char[a][1] < char[b][1]:
                    for i in range(char[b][1] - char[a][1]):
                        pre.append("R")
                else:
                    for i in range(char[a][1] - char[b][1]):
                        pre.append("L")
                for i in range(char[b][0] - char[a][0]):
                    pre.append("D")
            pre.append("!")
        
        path("a", target[0])
        for i in range(len(target) - 1):
            path(target[i], target[i + 1])
        return "".join(pre)
