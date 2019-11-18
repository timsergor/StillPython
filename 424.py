# 978. Longest Turbulent Subarray. Medium. 45.9%.

# A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if:

# For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
# OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.
# That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

# Return the length of a maximum size turbulent subarray of A.

class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        x = A[0]
        for i in range(1, len(A)):
            y = A[i]
            if y > x:
                A[i] = 1
            elif y < x:
                A[i] = -1
            else:
                A[i] = 0
            x = y
        A[0] = 0
        print(A)
        if len(A) == 1:
            return 1
        else:
            answer = 1
            t = 0
            for i in range(len(A)):
                if A[i] == 0:
                    t = 1
                elif A[i] == A[i - 1]:
                    t = 2
                else:
                    t += 1
                answer = max(t, answer)
        return answer
