# 796. Rotate String. Easy. 49.3%.

# We are given two strings, A and B.
# A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if len(A) == 0:
            return True
        for i in range(len(A)):
            if A[0:len(A) - i] == B[i:len(B)]:
                if A[len(A) - i: len(A)] == B[0:i]:
                    return True
        return False
        
 # 6min.
