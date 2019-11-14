# 561. Array Partition I. Easy. 70.4%.

# Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        answer = 0
        for i in range(len(nums) // 2):
            answer += nums[i * 2]
        return answer
