# 1266. Minimum Time Visiting All Points. Easy. Contest.

# On a plane there are n points with integer coordinates points[i] = [xi, yi]. Your task is to find the minimum time in seconds to visit all points.

# You can move according to the next rules:

# In one second always you can either move vertically, horizontally by one unit or diagonally (it means to move one unit vertically and one unit horizontally in one second).
# You have to visit the points in the same order as they appear in the array.

class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def dist(p,q):
            return max(abs(p[0] - q[0]), abs(p[1] - q[1]))
        
        answer = 0
        for i in range(1, len(points)):
            answer += dist(points[i], points[i - 1])
        
        return answer
