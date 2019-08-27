#724. Find Pivot Index. Easy.

#Given an array of integers nums, write a method that returns the "pivot" index of this array.
#We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.
#If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return(-1)
        S = sum(nums)
        lS = 0
        for i in range(len(nums)):
            if lS * 2 + nums[i] == S:
                return(i)
            lS += nums[i]
        return(-1)
        
# 5min

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return(-1)
        rS = sum(nums) - nums[0]
        lS = 0
        for i in range(len(nums)):
            if lS == rS:
                return(i)
            lS += nums[i]
            if i < len(nums) - 1:
                rS -= nums[i+1]
        return(-1)
        
