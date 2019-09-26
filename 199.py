# 334. Increasing Triplet Subsequence. Medium. 39.6%.

# Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

# Formally the function should:
# Return true if there exists i, j, k
# such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
# Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        first = 0
        second = -1
        for i in range(1 ,len(nums)):
            if second > -1 and nums[i] > nums[second]:
                return True
            if nums[i] < nums[first]:
                first = i
            elif nums[i] > nums[first] and (second == -1 or nums[second] > nums[i]):
                second = i
        return False
