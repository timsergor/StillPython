# 357. Count Numbers with Unique Digits. 47.6%.

# Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10**n.

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        dyn = [1]
        t = 9
        for i in range(n):
            dyn.append(dyn[-1] * t)
            if i:
                t -= 1
        return sum(dyn)
