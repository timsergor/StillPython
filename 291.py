# 941. Valid Mountain Array. Easy. 35.2%.

# Given an array A of integers, return true if and only if it is a valid mountain array.

# Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        state = 0
        for i in range(1,len(A)):
            if state == 0:
                if A[i] > A[i - 1]:
                    state = 1
                else:
                    return False
            elif state == 1:
                if A[i] < A[i - 1]:
                    state = 2
                elif A[i] == A[i - 1]:
                    return False
            elif state == 2 and A[i] >= A[i - 1]:
                return False
        if state == 2:
            return True
        return False
