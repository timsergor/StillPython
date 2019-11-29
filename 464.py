# 812. Largest Triangle Area. Easy. 57.1%.

# You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

from math import sqrt

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(a,b,c):
            C = sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
            B = sqrt((a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2)
            A = sqrt((c[0] - b[0]) ** 2 + (c[1] - b[1]) ** 2)
            if (A + B) > C and (A + C) > B and (B + C) > A:
                return sqrt(((A + B + C) / 2) * ((A + B - C) / 2) * ((A - B + C) / 2) * ((- A + B + C) / 2))
            else:
                return 0
        
        answer = 0
        for i in range(len(points)):
            for j in range(i):
                for k in range(j):
                    answer = max(answer, area(points[i], points[j], points[k]))
        return answer
