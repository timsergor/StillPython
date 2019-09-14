# 424. Longest Repeating Character Replacement. Medium. 44.7%.

# Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.
# In one operation, you can choose any character of the string and change it to any other uppercase English character.
# Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def check(char, k, s):
            m = 0
            for c in char:
                if char[c] > m:
                    m = char[c]
            if s - m > k:
                return False
            return True
        
        if len(s) < 2:
            return len(s)
        l = 0
        r = 1
        char = {s[0]: 1}
        answer = [l,r]
        while r <= len(s):
            if check(char, k, r - l):
                answer = [l,r]
                if r == len(s):
                    break
                if s[r] not in char:
                    char[s[r]] = 1
                else:
                    char[s[r]] += 1
                r += 1
            else:
                if r == len(s):
                    break
                char[s[l]] -= 1
                l += 1
                if s[r] not in char:
                    char[s[r]] = 1
                else:
                    char[s[r]] += 1
                r += 1
        return answer[1] - answer[0]
