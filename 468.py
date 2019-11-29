# 154. Find Minimum in Rotated Sorted Array II. Hard.

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

# Find the minimum element.

# The array may contain duplicates.

class Solution:
    def findMin(self, nums: List[int]) -> int:
        def solution(M):
            if M[0] < M[-1]:
                return M[0]
            if len(M) < 10:
                return min(M)
            if M[len(M) // 2] > M[0]:
                return solution(M[len(M) // 2 + 1 :])
            if M[len(M) // 2] < M[-1]:
                return solution(M[1 : len(M) // 2 + 1])
            if M[0] == M[-1] and M[0] == M[len(M) // 2]:
                return min(solution(M[:len(M) // 2]), solution(M[len(M) // 2:]))
            elif M[0] == M[len(M) // 2]:
                return solution(M[len(M) // 2 + 1 :])
            else:
                return solution(M[:len(M) // 2 + 1])
        
        return solution(nums)
