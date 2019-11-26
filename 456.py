# 688. Knight Probability in Chessboard. Medium. 46.4%.

# On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).
# A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

# Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.
# The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.

class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        pre = 0
        
        def step(p):
            for i in range(-2, 3, 4):
                for j in range(-1, 2, 2):
                    for k in range(2):
                        if k:
                            yield (p[0] + i, p[1] + j)
                        else:
                            yield (p[0] + j, p[1] + i)
        
        now = {(r,c) : 1}
        for t in range(K):
            new = {}
            for p in now:
                for q in step(p):
                    if q[0] < 0 or q[0] >= N or q[1] < 0 or q[1] >= N:
                        pre += now[p] / 8
                    else:
                        if q in new:
                            new[q] += now[p] / 8
                        else:
                            new[q] = now[p] / 8
            now = new
        return 1 - pre
