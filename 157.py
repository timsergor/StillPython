# 55. Jump Game. Medium. 32.5%.

# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        player = [0,nums[0]]
        while player[0] < len(nums) - 1 and player[1] > 0:
            player[0] += 1
            player[1] = max(player[1] - 1, nums[player[0]])
        if player[0] == len(nums) - 1:
            return True
        return False
