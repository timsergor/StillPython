# 740. Delete and Earn. Medium. 47.3%.

# Given an array nums of integers, you can perform operations on the array.

# In each operation, you pick any nums[i] and delete it to earn nums[i] points. After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.

# You start with 0 points. Return the maximum number of points you can earn by applying such operations.

class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        char = {}
        for i in range(len(nums)):
            if nums[i] in char:
                char[nums[i]] += 1
            else:
                char[nums[i]] = 1
        nums = []
        for c in char:
            nums.append((c, char[c]))
        
        def myKey(p):
            return p[0]
        
        nums.sort(key = myKey)
        answer = 0
        current = [0,0]
        t = 0
        for i in range(len(nums)):
            if i > 0 and nums[i][0] != nums[i - 1][0] + 1:
                answer += max(current)
                current = [nums[i][1] * nums[i][0], 0]
                t = 1
            else:
                current[t] += nums[i][1] * nums[i][0]
                if current[t] < current[1 - t]:
                    current[t] = current[1 - t]
                t = 1 - t
        answer += max(current)
        return answer
