# 459. Repeated Substring Pattern. Easy. 40.7%.

# Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def check(l):
            for i in range(l):
                for j in range(1, len(s) // l):
                    if s[l * j + i] != s[i]:
                        return False
            return True
        
        Flag = False
        for l in range(1, len(s) // 2 + 1):
            if len(s) % l == 0:
                Flag = check(l)
                if Flag:
                    return True
        return Flag
