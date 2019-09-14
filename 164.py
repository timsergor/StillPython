# 75. Sort Colors. Medium. 43.2%.
# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
# Note: You are not suppose to use the library's sort function for this problem.

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        colours = [0,0,0]
        for i in range(len(nums)):
            colours[nums[i]] += 1
        for i in range(len(nums)):
            if colours[0]:
                nums[i] = 0
                colours[0] -= 1
            elif colours[1]:
                nums[i] = 1
                colours[1] -= 1
            else:
                nums[i] = 2
        return nums

# 5-6 min.
