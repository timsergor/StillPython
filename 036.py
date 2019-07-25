# 198. House Robber. Easy. 41.2%.

#You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def result(nums):
            M = []
            if len(nums) == 0:
                return(0)
            if len(nums) == 1:
                return(nums[0])
            elif len(nums) == 2:
                return(max(nums))
            else:
                M.append(nums[0])
                M.append(max(nums[0],nums[1]))
                for i in range(2,len(nums)):
                    M.append(max(M[i-1],M[i-2] + nums[i]))
                return(M[len(M)-1])
        return(result(nums))
        
# 32 min
