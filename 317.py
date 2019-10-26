# 179. Largest Number. Medium. 26.8%.

# Given a list of non negative integers, arrange them such that they form the largest number.

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        
        def myKey(s):
            sy = s[0]
            t = 0
            for i in range(len(s) - 1, -1, -1):
                if s[i] == sy:
                    t += 1
                else:
                    break
            return s + s[0] * (15 - len(s)) + sy * t + str(30 - len(s))
            
        nums.sort(key = myKey, reverse = True)
        print(nums)
        pre = "".join(nums)
        if pre[0] == "0":
            return "0"
        else:
            return pre
