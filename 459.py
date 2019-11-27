# 497. Random Point in Non-overlapping Rectangles. Medium. 36.9%.

# Given a list of non-overlapping axis-aligned rectangles rects, write a function pick which randomly and uniformily picks an integer point in the space covered by the rectangles.

# Note:

# An integer point is a point that has integer coordinates. 
# A point on the perimeter of a rectangle is included in the space covered by the rectangles. 
# ith rectangle = rects[i] = [x1,y1,x2,y2], where [x1, y1] are the integer coordinates of the bottom-left corner, and [x2, y2] are the integer coordinates of the top-right corner.
# length and width of each rectangle does not exceed 2000.
# 1 <= rects.length <= 100
# pick return a point as an array of integer coordinates [p_x, p_y]
# pick is called at most 10000 times.

from random import randint

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.scheme = [0]
        self.rects = rects
        for i in range(len(rects)):
            self.scheme.append(self.scheme[-1] + (rects[i][2] - rects[i][0] + 1) * (rects[i][3] - rects[i][1] + 1))
        print(self.scheme)

    def pick(self) -> List[int]:
        t = randint(1, self.scheme[-1])
        l = 0
        r = len(self.scheme) - 1
        while r - l > 1:
            if self.scheme[(r + l) // 2] >= t:
                r = (r + l) // 2
            else:
                l = (r + l) // 2
        t -= self.scheme[l]
        return [self.rects[l][0] + (t - 1) % (self.rects[l][2] - self.rects[l][0] + 1), self.rects[l][1] + (t - 1) // (self.rects[l][2] - self.rects[l][0] + 1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
