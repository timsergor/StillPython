# 628. Maximum Product of Three Numbers. Easy. 46.7%.

# Given an integer array, find three numbers whose product is maximum and output the maximum product.

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mn = []
        mx = []
        for i in range(len(nums)):
            if len(mn) < 2:
                mn.append(nums[i])
            elif nums[i] < max(mn):
                mn = (min(mn), nums[i])
            if len(mx) < 3:
                mx.append(nums[i])
            elif nums[i] > min(mx):
                mx.remove(min(mx))
                mx.append(nums[i])
        return max(mn[0] * mn[1] * max(mx), mx[0] * mx[1] * mx[2])
