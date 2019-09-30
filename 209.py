# 396. Rotate Function. Medium. 35.5%.

# Given an array of integers A and let n to be its length.
# Assume Bk to be an array obtained by rotating the array A k positions clock-wise, we define a "rotation function" F on A as follow:
# F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].
# Calculate the maximum value of F(0), F(1), ..., F(n-1).

class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        S = sum(A)
        F0 = 0
        for i in range(len(A)):
            F0 += i*A[i]
        F = [F0]
        for i in range(1,len(A)):
            F.append(F[-1] + S - A[- i] * len(A))
        return max(F)
