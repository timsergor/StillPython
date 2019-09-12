# 3. Longest Substring Without Repeating Characters. Medium. 28.8%.

# Given a string, find the length of the longest substring without repeating characters.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        def isIt(s):
            char = {}
            for i in range(len(s)):
                if s[i] not in char:
                    char[s[i]] = True
                else:
                    return(False)
            return True
        
        answer = 0
        for i in range(len(s)):
            if isIt(s[i - answer:i + 1]):
                answer += 1
        return answer
