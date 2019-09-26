# 69. Sqrt(x). Easy. 32.1%.

# Implement int sqrt(int x).

# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        d = 1
        prex = 1
        while prex < x:
            d += 2
            prex += d
        if prex == x:
            return (d + 1) // 2
        else:
            return (d - 1) // 2
