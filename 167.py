# 462. Minimum Moves to Equal Array Elements II. Medium. 52.8%.

# Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

# You may assume the array's length is at most 10,000.

class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        mid = nums[len(nums) // 2]
        answer = 0
        for i in range(len(nums)):
            answer += abs(nums[i] - mid)
        return answer
        
# 14min.
