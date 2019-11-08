# 593. Valid Square. Medium. 41.1%.

# Given the coordinates of four points in 2D space, return whether the four points could construct a square.

# The coordinate (x,y) of a point is represented by an integer array with two integers.

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def clock(v):
            return (-v[1], v[0])
        
        if p1 == p2 or p1 == p3 or p1 == p4:
            return False
        p1 = tuple(p1)
        p2 = tuple(p2)
        p3 = tuple(p3)
        p4 = tuple(p4)
        figure = set([p1,p2,p3,p4])
        side1 = [p2[0] - p1[0], p2[1] - p1[1]]
        side11 = clock(side1)
        side111 = clock(side11)
        side2 = [p3[0] - p1[0], p3[1] - p1[1]]
        side22 = clock(side2)
        side222 = clock(side22)
        side3 = [p4[0] - p1[0], p4[1] - p1[1]]
        side33 = clock(side3)
        side333 = clock(side33)
        figure1 = set([p1, p2, (p2[0] + side11[0], p2[1] + side11[1]), (p2[0] + side11[0] + side111[0], p2[1] + side11[1] + side111[1])])
        figure2 = set([p1, p3, (p3[0] + side22[0], p3[1] + side22[1]), (p3[0] + side22[0] + side222[0], p3[1] + side22[1] + side222[1])])
        figure3 = set([p1, p4, (p4[0] + side33[0], p4[1] + side33[1]), (p4[0] + side33[0] + side333[0], p4[1] + side33[1] + side333[1])])
        return figure1 == figure or figure2 == figure or figure3 == figure
