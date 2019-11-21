# 342. Power of Four. Easy. 40.9%.

# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num > 1:
            if num % 4:
                return False
            else:
                num = num // 4
        return num == 1
