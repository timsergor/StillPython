# 368. Largest Divisible Subset. Medium. 35.5%.

# Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

# Si % Sj = 0 or Sj % Si = 0.

# If there are multiple solutions, return any subset is fine.

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        nums.sort()
        dev = {n:[1,[]] for n in nums}
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dev[nums[j]][0] + 1 > dev[nums[i]][0]:
                        dev[nums[i]] = [dev[nums[j]][0] + 1,dev[nums[j]][1] + [nums[j]]]
        a = 0
        great = 0
        print(dev)
        for c in dev:
            if dev[c][0] > a:
                a = dev[c][0]
                great = c
        return dev[great][1] + [great]
