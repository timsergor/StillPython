# 896. Monotonic Array. Easy. 56.3%.

# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

# Return true if and only if the given array A is monotonic.

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        t = 0
        for i in range(1, len(A)):
            if A[i] < A[i - 1]:
                Flag = True
                t = i
                break
            elif A[i] > A[i - 1]:
                Flag = False
                t = i
                break
        if t == 0:
            return True
        elif Flag:
            for i in range(t + 1, len(A)):
                if A[i] > A[i - 1]:
                    return False
            return True
        else:
            for i in range(t + 1, len(A)):
                if A[i] < A[i - 1]:
                    return False
            return True
