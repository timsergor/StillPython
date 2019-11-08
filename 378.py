# 795. Number of Subarrays with Bounded Maximum. Medium. 44.4%.

# We are given an array A of positive integers, and two positive integers L and R (L <= R).

# Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that subarray is at least L and at most R.

class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        good = -1
        bad = -1
        answer = 0
        for i in range(len(A)):
            if A[i] <= R:
                if A[i] >= L:
                    good = i               
                if good > bad:
                    answer += good - bad
            else:
                bad = i
        return answer
