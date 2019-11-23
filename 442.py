# 525. Contiguous Array. 44.1%.

# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        scheme = {0:[-1]}
        t = 0
        answer = 0
        for i in range(len(nums)):
            if nums[i]:
                t += 1
            else:
                t -= 1
            if t in scheme:
                scheme[t].append(i)
            else:
                scheme[t] = [i]
            answer = max(answer, scheme[t][-1] - scheme[t][0])
        return answer
