# 775. Global and Local Inversions. Medium. 40.1%.

# We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.

# The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].

# The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].

# Return true if and only if the number of global inversions is equal to the number of local inversions.

class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        i = 0
        while i < len(A) - 1:
            if A[i] == A[i + 1] + 1:
                A[i], A[i + 1] = A[i + 1], A[i]
                i += 2
            else:
                i += 1
        for i in range(len(A)):
            if i != A[i]:
                return False
        return True
