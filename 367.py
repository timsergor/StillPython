# 34. Find First and Last Position of Element in Sorted Array. Medium. 34.5%.

# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        m = -1
        while r - l > 1:
            if nums[(l + r) // 2] < target:
                l = (l + r) // 2
            elif nums[(l + r) // 2] > target:
                r = (l + r) // 2
            else:
                m = (l + r) // 2
                break
        if nums and l != r and m == -1:
            if nums[l] == target:
                m = l
            elif nums[r] == target:
                m = r
        if m == -1:
            if len(nums) <= 2:
                answer = []
                for i in range(len(nums)):
                    if nums[i] == target:
                        answer.append(i)
                if answer:
                    if len(answer) == 1:
                        answer = answer + answer
                    return answer
            return [-1,-1]
        l = 0
        R = m
        while R - l > 1:
            if nums[(l + R) // 2] < target:
                l = (l + R) // 2
            elif nums[(l + R) // 2] == target:
                R = (l + R) // 2
        if nums[l] < target:
            l = R
        L = m
        r = len(nums) - 1
        while r - L > 1:
            if nums[(L + r) // 2] == target:
                L = (L + r) // 2
            elif nums[(L + r) // 2] > target:
                r = (L + r) // 2
        if nums[r] > target:
            r = L
        return [l,r]
