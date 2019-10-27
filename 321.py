# 263. Ugly Number. Easy. 41%.

# Write a program to check whether a given number is an ugly number.

# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

class Solution:
    def isUgly(self, num: int) -> bool:
        if num < 1:
            return False
        while not num % 2:
            num //= 2
        while not num % 3:
            num //= 3
        while not num % 5:
            num //= 5
        if num == 1:
            return True
        return False
