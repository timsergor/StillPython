# 390. Elimination Game. Medium. 44%.

# There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.

# Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.

# We keep repeating the steps again, alternating left to right and right to left, until a single number remains.

# Find the last number that remains starting with a list of length n.

class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        def f(n):
            if n < 3:
                return n
            else:
                return n - n % 2 - 2 * (f(n // 2) - 1)
        
        return f(n)
