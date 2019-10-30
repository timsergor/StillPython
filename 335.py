# 279. Perfect Squares. Medium. 43.3%.

# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

class Solution:
    def numSquares(self, n: int) -> int:
        d = 1
        l = 1
        squares = set()
        while d <= n:
            if d == n:
                return 1
            squares.add(d)
            d += l * 2 + 1
            l += 1
        pre = set(squares)
        dyn = set()
        t = 2
        while True:
            for c in pre:
                for d in squares:
                    if c + d == n:
                        return t
                    elif c + d < n:
                        dyn.add(c + d)
            pre = dyn
            dyn = set()
            t += 1
