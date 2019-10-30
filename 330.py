# 447. Number of Boomerangs

# Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

# Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        
        def dist(p,q):
            return (q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2
        
        char = {}
        
        for i in range(len(points)):
            for j in range(i):
                D = dist(points[j], points[i])
                if tuple(points[j]) not in char:
                    char[tuple(points[j])] = {}
                    char[tuple(points[j])][D] = 1
                else:
                    if D in char[tuple(points[j])]:
                        char[tuple(points[j])][D] += 1
                    else:
                        char[tuple(points[j])][D] = 1
                if tuple(points[i]) not in char:
                    char[tuple(points[i])] = {}
                    char[tuple(points[i])][D] = 1
                else:
                    if D in char[tuple(points[i])]:
                        char[tuple(points[i])][D] += 1
                    else:
                        char[tuple(points[i])][D] = 1
        answer = 0
        for c in char:
            for d in char[c]:
                answer += char[c][d] * (char[c][d] - 1)
        return answer
