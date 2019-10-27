# 264. Ugly Number II. Medium. 37.8%.

# Write a program to find the n-th ugly number.

# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        parse = {2:True,3:True,5:True}
        char = {1:True}
        x = 1
        while len(char) < n:
            x = 2200000000
            for c in parse:
                if c < x:
                    x = c
            char[x] = True
            parse.pop(x)
            parse[x * 2] = True
            parse[x * 3] = True
            parse[x * 5] = True
        return x
