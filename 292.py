# 939. Minimum Area Rectangle. 51.5%.

# Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.

# If there isn't any rectangle, return 0.

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        charx = {}
        rect = []
        for i in range(len(points)):
            if points[i][0] not in charx:
                charx[points[i][0]] = [points[i][1]]
            else:
                charx[points[i][0]].append(points[i][1])
        
        def findDist(M,N):
            i = j = 0
            dist = 40002
            last = -1
            while i < len(M) and j < len(N):
                while i < len(M) and j < len(N) and M[i] < N[j]:
                    i += 1
                while i < len(M) and j < len(N) and N[j] < M[i]:
                    j += 1
                if i < len(M) and j < len(N) and N[j] == M[i]:
                    if last > -1:
                        dist = min(dist, M[i] - last)
                    last = M[i]
                i += 1
            if dist <= 40000:
                return dist
            else:
                return 0                    
        
        answer = 1600000000
        for c in charx:
            charx[c].sort()
        for c in charx:
            for d in charx:
                if abs(c - d) < answer and c < d:
                    area = (d - c) * findDist(charx[c],charx[d])
                    if area > 0:
                        answer = min(answer, area)
        if answer < 1600000000:
            return answer
        else:
            return 0
