# 836. Rectangle Overlap. Easy. 47.4%.

# A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the coordinates of its bottom-left corner, and (x2, y2) are the coordinates of its top-right corner.

# Two rectangles overlap if the area of their intersection is positive.  To be clear, two rectangles that only touch at the corner or edges do not overlap.

# Given two (axis-aligned) rectangles, return whether they overlap.

class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        return not ((rec2[2] <= rec1[0]) or rec2[3] <= rec1[1] or rec2[0] >= rec1[2] or rec2[1] >= rec1[3])
