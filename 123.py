# 7. Reverse Integer. Easy. 25.5%.

# Given a 32-bit signed integer, reverse digits of an integer.

class Solution:
    def reverse(self, x: int) -> int:
        def solution(x):
            digits = []
            while x > 0:
                digits.append(x % 10)
                x //= 10
            degree = 1
            answer = 0
            while digits:
                answer += digits.pop() * degree
                degree *= 10
            return answer
        
        if x >= 0:
            y = solution(x)
            if y >= 2**31:
                return 0
            else:
                return y
        else:
            y = -solution(-x)
            if abs(y) >= 2**31:
                return 0
            else:
                return y

# 10min.
