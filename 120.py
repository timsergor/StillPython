# 260. Single Number III. Medium. 

#Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        char = {}
        for i in range(len(nums)):
            if nums[i] not in char:
                char[nums[i]] = True
            else:
                char[nums[i]] = False
        answer = []
        for c in char:
            if char[c]:
                answer.append(c)
        return answer
        
# 4 min.
