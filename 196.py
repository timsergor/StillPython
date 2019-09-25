# 209. Minimum Size Subarray Sum. Medium. 35.7%.

# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        l = r = 0
        S = nums[0]
        while S < s:
            r += 1
            if r < len(nums):
                S += nums[r]
            else:
                return 0
        while r < len(nums):
            while S - nums[l] >= s:
                S -= nums[l]
                l += 1
            if r == len(nums) - 1:
                return r - l + 1
            else:
                S -= nums[l]
                l += 1
                r += 1
                S += nums[r]
