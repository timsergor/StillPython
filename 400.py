# 670. Maximum Swap. Medium. 41.2%.

# Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = [0]
        while num:
            digits[-1] += num % 10
            num //= 10
            if num:
                digits.append(0)
        digits.reverse()
        
        def solution(digits, k):
            m = k
            for i in range(k + 1, len(digits)):
                if digits[i] >= digits[m]:
                    m = i
            if m < len(digits):
                if digits[m] == digits[k]:
                    return solution(digits, k + 1)
                else:
                    digits[k], digits[m] = digits[m], digits[k]
                    return digits
            else:
                return digits
        
        digits = solution(digits, 0)
        answer = 0
        d = 1
        while digits:
            answer += digits.pop() * d
            d *= 10
        return answer
