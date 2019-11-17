# 1262. Greatest Sum Divisible by Three. Medium. Contest.

# Given an array nums of integers, we need to find the maximum possible sum of elements of the array such that it is divisible by three.

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        h1 = []
        h2 = []
        s = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                s += nums[i] 
                if nums[i] % 3 == 1:
                    if len(h1) < 2:
                        h1.append(nums[i])
                    elif nums[i] <= max(h1):
                        h1.remove(max(h1))
                        h1.append(nums[i])
                elif nums[i] % 3 == 2:
                    if len(h2) < 2:
                        h2.append(nums[i])
                    elif nums[i] <= max(h2):
                        h2.remove(max(h2))
                        h2.append(nums[i])
        if s % 3 == 0:
            return s
        elif s % 3 == 1:
            pre = []
            if h1:
                pre.append(s - min(h1))
            if len(h2) == 2:
                pre.append(s - sum(h2))
            if pre:
                return max(pre)
            else:
                return 0
        else:
            pre = []
            if h2:
                pre.append(s - min(h2))
            if len(h1) == 2:
                pre.append(s - sum(h1))
            if pre:
                return max(pre)
            else:
                return 0
