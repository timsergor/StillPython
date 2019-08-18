#149. Max Points on a Line. Hard. 16.0%

#Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return(len(points))
        
        def isPointOnLine(x,y,k,b):
            return(abs(x * k + b - y) < 0.000000000001)
        
        char = {}
        char[None] = 0
        for i in range(len(points)):
            for j in range(len(points)):
                if i > j:
                    if points[i][0] == points[j][0]:
                        tg = ("inf", points[i][0])
                        if tg not in char:
                            char[tg] = 1
                        else:
                            char[tg] += 1
                    elif points[i][1] == points[j][1]:
                        tg = (0, points[i][1])
                        if tg not in char:
                            char[tg] = 1
                        else:
                            char[tg] += 1
                    else:
                        tg = ((points[i][1] - points[j][1])/(points[i][0] - points[j][0]), points[i][1] - points[i][0] * ((points[i][1] - points[j][1])/(points[i][0] - points[j][0])))
                        if tg not in char:
                            char[tg] = 1
                        else:
                            char[tg] += 1
        TheLine = None
        P = 0
        for c in char:
            if char[c] > char[TheLine]:
                TheLine = c
        if TheLine[0] == "inf":
            for i in range(len(points)):
                if points[i][0] == TheLine[1]:
                    P += 1
        else:
            for i in range(len(points)):
                if isPointOnLine(points[i][0],points[i][1],TheLine[0],TheLine[1]):
                    P += 1
        return(P)
        
# ~ 100min
