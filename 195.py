# 43. Multiply Strings. Medium. 31.6%.

# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        answer = 0
        for i in range(len(num1)):
            for j in range(len(num2)):
                answer += int(num1[-1 - i]) * int(num2[-1 - j]) * 10**(i + j)
        return str(answer)
        
# 5min.
