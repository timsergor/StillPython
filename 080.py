#53. Maximum Subarray. Easy. 44.3%.

#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        L = d = nums[0]
        m = min(0,nums[0])
        for i in range(1,len(nums)):
            L += nums[i]
            if L - m > d:
                d = L - m
            if L < m:
                m = L
        return(d)
