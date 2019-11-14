# 494. Target Sum. Medium. 46%.

# You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

# Find out how many ways to assign symbols to make sum of integers equal to target S.

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        dyn = {0 : 1}
        for i in range(len(nums)):
            new = {}
            for s in dyn:
                if s + nums[i] in new:
                    new[s + nums[i]] += dyn[s]
                else:
                    new[s + nums[i]] = dyn[s]
                if s - nums[i] in new:
                    new[s - nums[i]] += dyn[s]
                else:
                    new[s - nums[i]] = dyn[s]
            dyn = new
        answer = 0
        if S in dyn:
            return dyn[S]
        else:
            return 0
