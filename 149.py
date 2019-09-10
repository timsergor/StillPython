# 392. Is Subsequence. Easy. 47.5%.

# Given a string s and a string t, check if s is subsequence of t.

# You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        bag = {}
        bag2 = {}
        for l in range(len(t)):
            if l % 2 == 0:
                for m in bag:
                    if t[l] == s[m + 1]:
                        bag2[m + 1] = True
                    bag2[m] = True
                if t[l] == s[0]:
                    bag2[0] = True
                if len(s) - 1 in bag2:
                    return True
            else:  
                for m in bag2:
                    if t[l] == s[m + 1]:
                        bag[m + 1] = True
                    bag[m] = True
                if t[l] == s[0]:
                    bag[0] = True
                if len(s) - 1 in bag:
                    return True
        return False
        
# 25min
