# 611. Valid Triangle Number. Medium. 46.5%.

# Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        char = {}
        for n in nums:
            if n > 0:
                if n not in char:
                    char[n] = 1
                else:
                    char[n] += 1
        nums = []
        for c in char:
            nums.append((c,char[c]))
        
        def myKey(p):
            return p[0]
        
        nums.sort(key = myKey)
        answer = 0
        for i in range(2,len(nums)):
            for j in range(1,i):
                for k in range(j):
                    if nums[i][0] < nums[j][0] + nums[k][0]:
                        answer += nums[i][1] * nums[j][1] * nums[k][1]
        for i in range(1,len(nums)):
            for j in range(i):
                answer += nums[j][1] * nums[i][1] * (nums[i][1] - 1) // 2
                if nums[i][0] < 2 * nums[j][0]:
                    answer += nums[i][1] * nums[j][1] * (nums[j][1] - 1) // 2
        for i in range(len(nums)):
            answer += nums[i][1] * (nums[i][1] - 1) * (nums[i][1] - 2) // 6
        return answer
