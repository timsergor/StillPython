# 79. Word Search. Medium. 32.4%.

# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def check(point, word, back):
            if point in back or board[point[0]][point[1]] != word[0]:
                return False
            if board[point[0]][point[1]] == word[0]:
                if len(word) == 1:
                    return True
                else:
                    for i in range(-1,2):
                        for j in range (-1,2):
                            if abs(i + j) == 1 and point[0] + i >= 0 and point[1] + j >= 0 and point[0] + i < len(board) and point[1] + j < len(board[0]):
                                Flag = check([point[0] + i,point[1] + j], word[1:len(word)], back + [point])
                                if Flag:
                                    return True
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                Flag = check([i,j], word, [])
                if Flag:
                    return True
        return False
        
# 15min.
