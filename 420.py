# 643. Maximum Average Subarray I. Easy. 40.5%.

# Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        answer = "#"
        current = 0
        for i in range(len(nums)):
            current += nums[i] / k
            if i >= k - 1:
                if i >= k:
                    current -= nums[i - k] / k
                if answer == "#":
                    answer = current
                else:
                    answer = max(answer, current)
        return answer
