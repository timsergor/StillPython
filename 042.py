#1. Two Sum. Easy. 

#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums2 = list(nums)
        for i in range(len(nums)):
            nums2[i] -= target
        for i in range(len(nums)):
            if (nums2[i]*(-1) in nums) and (i != nums.index(nums2[i]*(-1))):
                return(nums.index(nums2[i]*(-1)),i)
