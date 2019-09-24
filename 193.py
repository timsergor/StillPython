# 172. Factorial Trailing Zeroes. Easy. 37.6%.

# Given an integer n, return the number of trailing zeroes in n!.

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        answer = 0
        d = 5
        while d <= n:
            answer += n // d
            d *= 5
        return answer
        
# 5min.
