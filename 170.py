# 78. Subsets. Medium. 55.1%.

# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def solution(nums):
            if len(nums) == 0:
                return [[]]
            else:
                pre = solution(nums[0:len(nums) - 1])
                pre2 = []
                for i in range(len(pre)):
                    pre2.append(pre[i] + [nums[-1]])
                pre.extend(pre2)
                return pre
        return solution(nums)
        
# 7-10min.
