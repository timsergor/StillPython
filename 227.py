# 149. Max Points on a Line. Hard. 16.2%.

# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """        
        def nok(a,b):
            a, b = max(a, b), min(a, b)
            while (a % b) != 0:
                a -= (a // b) * b
                a, b = b, a
            return b
    
        def line(p,q):
            if p == q:
                return None
            if p[0] == q[0]:
                return ((0,1),(p[0],0))
            if p[1] == q[1]:
                return ((1,0),(0,q[0]))
            if p[0] > q[0]:
                p, q = q, p
            k = ((q[1] - p[1]) // nok(q[0] - p[0], abs(q[1] - p[1])), (q[0] - p[0]) // nok(q[0] - p[0],abs(q[1] - p[1])))
            b = list(p)
            if p[1] <= 0:
                d = abs(p[1]) // k[0]
                b[0] += d * k[1]
                b[1] += d * k[0]
            else:
                d = p[1] // k[0]
                if p[1] % k[0] == 0:
                    b[1] = 0
                    b[0] -= d * k[1]
                else:
                    b[0] -= (d + 1) * k[1]
                    b[1] -= (d + 1) * k[0]                
            return (k,tuple(b))

        char = {}
        for p in points:
            if tuple(p) in char:
                char[tuple(p)] += 1
            else:
                char[tuple(p)] = 1

        if len(char) < 2:
            if len(char):
                return char[tuple(points[0])]
            else:
                return 0
        
        lines = {}
        for a in char:
            for b in char:
                l = line(a,b)
                if l != None and l not in lines:
                    lines[l] = 0

        def isOnLine(l,p):
            k = l[0]
            b = l[1]
            if k == (0,1):
                return p[0] == b[0]
            elif k == (1,0):
                return p[1] == b[1]
            else:
                return p == b or (p[0] - b[0]) * k[0] == (p[1] - b[1]) * k[1]

        for l in lines:
            for p in char:
                if isOnLine(l,p):   
                    lines[l] += char[p]
        answer = 0
        for l in lines:
            if lines[l] > answer:
                answer = lines[l]
        return answer
