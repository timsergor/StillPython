# 219. Contains Duplicate II. Easy. 35.9%.

# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        char = {}
        for i in range(len(nums)):
            if i <= k:
                if nums[i] in char and char[nums[i]]:
                    return True
                char[nums[i]] = True
            else:
                char[nums[i - k - 1]] = False
                if nums[i] in char and char[nums[i]]:
                    return True
                char[nums[i]] = True
        return False
