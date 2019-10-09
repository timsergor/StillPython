# 397. Integer Replacement. Medium. 31.9%.

# Given a positive integer n and you can do operations as follow:

# If n is even, replace n with n/2.
# If n is odd, you can replace n with either n + 1 or n - 1.
# What is the minimum number of replacements needed for n to become 1?

class Solution:
    def integerReplacement(self, n: int) -> int:
        def solve(n):
            if n == 1:
                return 0
            elif n % 2 == 0:
                return solve(n // 2) + 1
            else:
                return min(solve(n - 1),solve(n + 1)) + 1
            
        return solve(n)
