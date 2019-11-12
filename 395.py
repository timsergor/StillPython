# 1027. Longest Arithmetic Sequence. Medium. 52.2%.

# Given an array A of integers, return the length of the longest arithmetic subsequence in A.

# Recall that a subsequence of A is a list A[i_1], A[i_2], ..., A[i_k] with 0 <= i_1 < i_2 < ... < i_k <= A.length - 1, and that a sequence B is arithmetic if B[i+1] - B[i] are all the same value (for 0 <= i < B.length - 1).

class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        scheme = [{}]
        dist = {}
        answer = 0
        for i in range(1, len(A)):
            scheme.append({})
            for j in range(i):
                if A[i] - A[j] not in scheme[j]:
                    scheme[i][A[i] - A[j]] = 2
                else:
                    scheme[i][A[i] - A[j]] = scheme[j][A[i] - A[j]] + 1
                answer = max(answer, scheme[i][A[i] - A[j]])
        return answer
