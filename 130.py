# 1037. Valid Boomerang. Easy. 37.4%.
# A boomerang is a set of 3 points that are all distinct and not in a straight line.
# Given a list of three points in the plane, return whether these points are a boomerang.

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        def line(x,y):
            if x[0] == y[0]:
                return "inf"
            return (y[1] - x[1])/(y[0] - x[0])
        
        if line(points[0],points[1]) == line(points[0],points[2]) or points[0] == points[1] or points[0] == points[2] or points[1] == points[2]:
            return False
        return True
        
# 8min
