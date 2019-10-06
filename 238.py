# 5214. Longest Arithmetic Subsequence of Given Difference. Easy. Contest.

# Given an integer array arr and an integer difference, return the length of the longest subsequence in arr which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.

class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        map = {}
        answer = 0
        for i in range(len(arr)):
            if arr[i] - difference in map:
                map[arr[i]] = map[arr[i] - difference] + 1
            else:
                map[arr[i]] = 1
            if map[arr[i]] > answer:
                    answer = map[arr[i]]
        return answer
