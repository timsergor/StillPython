# 300. Longest Increasing Subsequence. Medium. 41.5%.

# Given an unsorted array of integers, find the length of longest increasing subsequence.

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        map = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i] > map[-1]:
                map.append(nums[i])
            elif nums[i] < map[0]:
                map[0] = nums[i]
            else:
                for j in range(len(map) - 1):
                    if nums[i] > map[j] and nums[i] < map[j + 1]:
                        map[j + 1] = nums[i]  
                        break
        return len(map)
        
# 9min.
