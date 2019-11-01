# 565. Array Nesting. Medium. 53.9%.

# A zero-indexed array A of length N contains all integers from 0 to N-1. Find and return the longest length of set S, where S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to the rule below.

# Suppose the first element in S starts with the selection of element A[i] of index = i, the next element in S should be A[A[i]], and then A[A[A[i]]]… By that analogy, we stop adding right before a duplicate element occurs in S.

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        char = {}
        
        def sets(i,p):
            if i not in char:
                char[i] = True
                return sets(nums[i],p + 1)
            else:
                return p
        
        answer = 0
        for i in range(len(nums)):
            if i not in char:
                answer = max(answer, sets(i,0))
        return answer
