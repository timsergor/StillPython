# 223. Rectangle Area. Medium. 36.5%.

# Find the total area covered by two rectilinear rectangles in a 2D plane.

# Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        if E >= C or G <= A or H <= B or D <= F:
            return ((C - A) * (D - B)) + ((G - E) * (H -F))
        else:
            return ((C - A) * (D - B)) + ((G - E) * (H -F)) - (min(C,G) - max(A,E)) * (min(D,H) - max(B,F))
           
# ~6-7min.
