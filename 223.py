# 387. First Unique Character in a String. Easy. 50.7%.

# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char = {}
        for i in range(len(s)):
            if s[i] not in char:
                char[s[i]] = i
            else:
                char[s[i]] = -1
        for i in range(len(s)):
            if char[s[i]] >= 0:
                return char[s[i]]
        return -1

# 3-4min.
