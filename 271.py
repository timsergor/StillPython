# 1224. Maximum Equal Frequency. Hard.

# Given an array nums of positive integers, return the longest possible length of an array prefix of nums, such that it is possible to remove exactly one element from this prefix so that every number that has appeared in it will have the same number of occurrences.

# If after removing one element there are no remaining elements, it's still considered that every appeared number has the same number of ocurrences (0).

class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        char = {}
        ch = {}
        def check():
            k = list(ch.keys())
            if k == [1] or list(ch.values()) == [1]:
                return True
            if len(ch) != 2:
                return False
            return ((abs(k[1] - k[0]) == 1) and (ch[max(k)] == 1)) or (1 in k and ch[1] == 1)
            
        for i in range(len(nums)):
            if nums[i] not in char:
                char[nums[i]] = 1
            else:
                char[nums[i]] += 1
            if char[nums[i]] - 1 in ch:
                ch[char[nums[i]] - 1] -= 1
                if ch[char[nums[i]] -1 ] == 0:
                    ch.pop(char[nums[i]] - 1)
            if char[nums[i]] not in ch:
                ch[char[nums[i]]] = 1
            else:
                ch[char[nums[i]]] += 1
            if check():
                answer = i + 1
        return answer
        
# ~20-25min.
