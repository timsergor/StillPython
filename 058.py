#674. Longest Continuous Increasing Subsequence. Easy. 44.7%.

#Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return(0)
        else:
            a = 1
            b = 1
            for i in range(1,len(nums)):
                if nums[i] > nums[i - 1]:
                    b += 1
                else:
                    a = max(a,b)
                    b = 1
            return(max(a,b))
            
# 3 min
