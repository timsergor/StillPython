# 932. Beautiful Array. Medium. 54.5%.

# For some fixed N, an array A is beautiful if it is a permutation of the integers 1, 2, ..., N, such that:

# For every i < j, there is no k with i < k < j such that A[k] * 2 = A[i] + A[j].

# Given N, return any beautiful array A.  (It is guaranteed that one exists.)

class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        def solution(k):
            if k < 3:
                return list(range(1,k + 1))
            else:
                even = solution(k // 2)
                odd = solution((k + 1) // 2)
                for i in range(len(even)):
                    even[i] *= 2
                for i in range(len(odd)):
                    odd[i] = odd[i] * 2 - 1
                answer = []
                return even + odd
        
        return solution(N)
