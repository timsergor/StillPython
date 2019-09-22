# 15. 3Sum. Medium. 24.8%.

# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:
# The solution set must not contain duplicate triplets.

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        better = []
        counter = 0
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                counter += 1
            else:
                counter = 1
            if counter <= 3:
                better.append(nums[i])
        nums = better
        char = {}
        for i in range(len(nums)):
            if nums[i] not in char:
                char[nums[i]] = [i]
            else:
                char[nums[i]].append(i)
        answer = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] < nums[j] or (nums[i] == nums[j] and i < j):
                    if - (nums[i] + nums[j]) in char and char[-(nums[i] + nums[j])][0] not in [i,j]:
                        if -(nums[i] + nums[j]) < nums[i] or (-(nums[i] + nums[j]) == nums[i]):
                            answer.append((-nums[i] - nums[j], nums[i], nums[j]))
        return list(set(answer))
