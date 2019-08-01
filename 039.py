#1018. Binary Prefix Divisible By 5. Easy. 46.7%

#Given an array A of 0s and 1s, consider N_i: the i-th subarray from A[0] to A[i] interpreted as a binary number (from most-significant-bit to least-significant-bit.)
#Return a list of booleans answer, where answer[i] is true if and only if N_i is divisible by 5.

class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        B = []
        x = 0
        for i in range(len(A)):
            x = x * 2 + A[i]
            B.append(x % 5 == 0)
        return(B)
  
  # < 5 min
