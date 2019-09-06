# 18. 4Sum. Medium. 31.4%.
# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
# Note:
# The solution set must not contain duplicate quadruplets.

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        char = {}
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] not in char:
                        char[nums[i] + nums[j]] = [[i,j]]
                    else:
                        char[nums[i] + nums[j]].append([i,j])
        
        preanswer = {}
        for c in char:
            if target - c in char:
                for i in range(len(char[c])):
                    for j in range(len(char[target - c])):
                        if char[c][i][0] != char[target - c][j][0] and char[c][i][0] != char[target - c][j][1] and char[c][i][1] != char[target - c][j][0] and char[c][i][1] != char[target - c][j][1]:
                            tup = [nums[char[c][i][0]], nums[char[c][i][1]], nums[char[target - c][j][0]], nums[char[target - c][j][1]]]
                            tup.sort()
                            tup = tuple(tup)
                            preanswer[tup] = True
        answer = []
        for t in preanswer:
            answer.append(list(t))
        return answer
