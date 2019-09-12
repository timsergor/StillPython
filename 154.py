# 258. Add Digits. 54.7%.
# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        x = num % 9
        if x or num == 0:
            return x
        else:
            return 9
            
# 2-3min.
