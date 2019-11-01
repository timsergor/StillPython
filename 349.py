# 947. Most Stones Removed with Same Row or Column. Medium. 54.8%.

# On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.

# Now, a move consists of removing a stone that shares a column or row with another stone on the grid.

# What is the largest possible number of moves we can make?

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        x = {}
        y = {}
        t = 1
        for p in stones:
            if p[0] not in x and p[1] not in y:
                x[p[0]] = t
                y[p[1]] = t
                t += 1
            elif p[0] not in x and p[1] in y:
                x[p[0]] = y[p[1]]
            elif p[0] in x and p[1] not in y:
                y[p[1]] = x[p[0]]
            else:
                if x[p[0]] != y[p[1]]:
                    a = max(x[p[0]], y[p[1]])
                    b = min(x[p[0]], y[p[1]])
                    for c in x:
                        if x[c] == a:
                            x[c] = b
                    for c in y:
                        if y[c] == a:
                            y[c] = b
        return len(stones) - len(set(x.values()))
