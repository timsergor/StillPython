# 229. Majority Element II. Medium. 33%.

# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

# Note: The algorithm should run in linear time and in O(1) space.

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        d = len(nums) // 3 + 1
        answer = []
        i = 0
        while i < len(nums) - d + 1:
            if nums[i] == nums[i + d - 1] and (len(answer) == 0 or answer[-1] != nums[i]):
                answer.append(nums[i])
                i += d
            else:
                i += 1
        return answer
        
# 8 min.
