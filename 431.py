# 238. Product of Array Except Self. Medium. 57.5%.

# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sumn = list(nums)
        for i in range(1,len(nums)):
            nums[i] *= nums[i - 1]
            sumn[-1 - i] *= sumn[-i]
        x = nums[0]
        nums[0] = sumn[1]
        for i in range(1, len(nums) - 1):
            y = nums[i]
            nums[i] = x * sumn[i + 1]
            x = y
        nums[-1] = x
        return nums
