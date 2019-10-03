# 1001. Grid Illumination. Hard. 34.7%.

# On a N x N grid of cells, each cell (x, y) with 0 <= x < N and 0 <= y < N has a lamp.
# Initially, some number of lamps are on.  lamps[i] tells us the location of the i-th lamp that is on.  Each lamp that is on illuminates every square on its x-axis, y-axis, and both diagonals (similar to a Queen in chess).
# For the i-th query queries[i] = (x, y), the answer to the query is 1 if the cell (x, y) is illuminated, else 0.
# After each query (x, y) [in the order given by queries], we turn off any lamps that are at cell (x, y) or are adjacent 8-directionally (ie., share a corner or edge with cell (x, y).)
# Return an array of answers.  Each value answer[i] should be equal to the answer of the i-th query queries[i].

class Solution(object):
    def gridIllumination(self, N, lamps, queries):
        """
        :type N: int
        :type lamps: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        lamps = {tuple(l):True for l in lamps}
        lightenCode = {}
        for l in lamps:
            if (l[0],0) not in lightenCode:
                lightenCode[(l[0],0)] = [l]
            else:
                lightenCode[(l[0],0)].append(l)
            if (l[0] + l[1],1)  not in lightenCode:
                lightenCode[(l[0] + l[1],1)] = [l]
            else:
                lightenCode[(l[0] + l[1],1)].append(l)
            if (l[1],2) not in lightenCode:
                lightenCode[(l[1],2)] = [l]
            else:
                lightenCode[(l[1],2)].append(l)
            if (l[0] - l[1],3) not in lightenCode:
                lightenCode[(l[0] - l[1],3)] = [l]
            else:
                lightenCode[(l[0] - l[1],3)].append(l)
        
        def isLighten(p):
            return ((p[0],0) in lightenCode and len(lightenCode[(p[0],0)]) > 0) or ((p[0] + p[1],1) in lightenCode  and len(lightenCode[(p[0] + p[1],1)]) > 0) or ((p[1],2) in lightenCode and len(lightenCode[(p[1],2)]) > 0) or ((p[0] - p[1],3) in lightenCode and len(lightenCode[(p[0] - p[1],3)]) > 0)
        
        def neir(p):
            for i in range(-1,2):
                for j in range(-1,2):
                    yield (p[0] + i, p[1] + j)
        
        answer = []
        for p in queries:
            if isLighten(p):
                answer.append(1)
                for q in neir(p):
                    if q in lamps:
                        lamps.pop(q)
                        lightenCode[(q[0],0)].remove(q)
                        lightenCode[(q[0] + q[1],1)].remove(q)
                        lightenCode[(q[1],2)].remove(q)
                        lightenCode[(q[0] - q[1],3)].remove(q)
            else:
                answer.append(0)
        return answer
