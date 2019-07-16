# 693. Binary Number with Alternating Bits. Easy, 58.1%.
# Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 3:
            return(True)
        else:
            a = n % 2
            n = (n - a) / 2
            while n > 0:
                b = n % 2
                if a == b:
                    return(False)
                n = (n - b) / 2
                a, b = b, a
            return(True)
            
 # 10 min
