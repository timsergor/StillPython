# 231. Power of Two. Easy. 42.4%.

# Given an integer, write a function to determine if it is a power of two.

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n > 0:
            while not n % 2:
                n //= 2
            return n == 1
        return False
