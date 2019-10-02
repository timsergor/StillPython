# 90. Subsets II. Medium. 43.9%.

# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def solution(nums):
            if len(nums) == 0:
                return [[]]
            else:
                A = solution(nums[0:len(nums) - 1])
                B = []
                for el in A:
                    B.append(el)
                    B.append(el + [nums[-1]])
                return B
        
        nums.sort()
        B = solution(nums)
        S = [tuple(el) for el in B]
        preanswer = set(S)
        answer = [list(el) for el in preanswer]
        return answer
