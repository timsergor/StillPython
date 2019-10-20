# 1232. Check If It Is a Straight Line. Easy. Contest.

# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        def myKey(p):
            return p[0]
        
        coordinates.sort(key = myKey)
        d = (coordinates[1][1] - coordinates[0][1], coordinates[1][0] - coordinates[0][0])
        for i in range(2, len(coordinates)):
            if d[0] * (coordinates[i][0] - coordinates[0][0]) != d[1] * (coordinates[i][1] - coordinates[0][1]):
                return False
        return True
