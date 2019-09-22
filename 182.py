# 189. Rotate Array. Easy. 31.5%.

# Given an array, rotate the array to the right by k steps, where k is non-negative.

from Queue import Queue

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        Flag = True
        back = Queue()
        for i in range(len(nums)):
            if (len(nums) - k + i) % len(nums) == 0:
                Flag = False
            if Flag:
                back.put(nums[i])
                nums[i] = nums[(len(nums) - k + i) % len(nums)]
            else:
                back.put(nums[i])
                nums[i] = back.get()
                
