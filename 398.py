# 287. Find the Duplicate Number. Medium. 51.6%.

# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def solution(l,r):
            if l >= r - 10:
                char = {}
                for i in range(len(nums)):
                    if nums[i] >= l and nums[i] <= r:
                        if nums[i] in char:
                            return nums[i]
                        else:
                            char[nums[i]] = True
            large = 0
            small = 0
            for i in range(len(nums)):
                if nums[i] >= (r + l) // 2 and nums[i] <= r:
                    large += 1
                    if large > r - ((r + l) // 2 - 1):
                        return ((r + l) // 2 , r)
                elif nums[i] >= l and nums[i] < (r + l) // 2:
                    small += 1
                    if small > (r + l) // 2 - l:
                        return (l, (r + l) // 2 - 1)
            
        t = (1, len(nums) - 1)
        while type(t) == tuple:
            t = solution(t[0],t[1])
        return t
