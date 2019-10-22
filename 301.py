# 162. Find Peak Element. Medium. 42%.

# A peak element is an element that is greater than its neighbors.

# Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

# You may imagine that nums[-1] = nums[n] = -∞.

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def solution(nums):
            print(nums)
            if len(nums) == 1:
                return 0
            if len(nums) == 2:
                if nums[0] > nums[1]:
                    return 0
                else:
                    return 1
            if nums[len(nums) // 2] < nums[len(nums) // 2 - 1]:
                return solution(nums[:len(nums) // 2])
            elif nums[len(nums) // 2] < nums[len(nums) // 2 + 1]:
                return len(nums) // 2 + 1 + solution(nums[len(nums) // 2 + 1:])
            else:
                return len(nums) // 2
        return solution(nums)

# 11min.
