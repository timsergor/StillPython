# 441. Arranging Coins. Easy. 38.8%.

# You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

# Given n, find the total number of full staircase rows that can be formed.

# n is a non-negative integer and fits within the range of a 32-bit signed integer.

class Solution:
    def arrangeCoins(self, n: int) -> int:
        t = 1
        while n > 0:
            n -= t
            t += 1
        if n == 0:
            return t - 1
        else:
            return t - 2
