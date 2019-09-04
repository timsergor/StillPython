# 970. Powerful Integers. Easy. 39.6%.
# Given two positive integers x and y, an integer is powerful if it is equal to x^i + y^j for some integers i >= 0 and j >= 0.
# Return a list of all powerful integers that have value less than or equal to bound.
# You may return the answer in any order.  In your answer, each value should occur at most once.

class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        char = {}
        a = 1
        b = 1
        if x != 1 and y != 1:
            while a <= bound:
                while a + b <= bound:
                    char[a + b] = True
                    b *= y
                b = 1
                a *= x
        elif x == 1 and y > 1:
            while b + 1 <= bound:
                char[b + 1] = True
                b *= y
        elif x > 1 and y == 1:
            while a + 1 <= bound:
                char[a + 1] = True
                a *= x
        else:
            if 2 <= bound:
                return [2]
            else:
                return []
        return list(char)
 
 # < 20min
