# 485. Max Consecutive Ones. Easy. 55.8%.

# Given a binary array, find the maximum number of consecutive 1s in this array.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a = 0
        b = 0
        for i in range(len(nums)):
            if nums[i]:
                b += 1
            else:
                a = max(a,b)
                b = 0
        return max(a,b)
