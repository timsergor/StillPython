# 556. Next Greater Element III. Medium. 30.6%.

# Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 12:
            return -1
        digits = []
        while n:
            digits.append(n % 10)
            n //= 10
        m = -1
        for i in range(1, len(digits)):
            if digits[i] < digits[i - 1]:
                m = i
                break
        if m == -1:
            return -1
        l = m - 1
        while l >= 0 and digits[l] > digits[m]:
            l -= 1
        l += 1
        digits[l], digits[m] = digits[m], digits[l]
        L = digits[:m]
        L.sort(reverse = True)
        digits = L + digits[m:]
        digits.reverse()
        answer = 0
        t = 0
        while digits:
            answer += digits.pop() * 10 ** t
            t += 1
        if answer < 2 ** 31:
            return answer
        else:
            return -1
