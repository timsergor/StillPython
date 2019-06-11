#There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

#The move sequence is represented by a string, and the character moves[i] represents its ith move. Valid moves are R (right), L (left), U (up), and D (down). If the robot returns to the origin after it finishes all of its moves, return true. Otherwise, return false.

class Solution:
    def judgeCircle(self, moves: str):
        a = 0
        o = 0
        for i in range(len(moves)):
            if moves[i] == "U":
                o += 1
            elif moves[i] == "L":
                a -= 1
            elif moves[i] == "R":
                a += 1
            else:
                o -= 1
        if a == 0 and o == 0:
            return(True)
        else:
            return(False)
