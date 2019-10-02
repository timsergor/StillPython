# 139. Word Break. Medium. 36.7%.
# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dyn = [True]
        for i in range(1,len(s) + 1):
            Flag = False
            for word in wordDict:
                if i - len(word) >= 0 and dyn[i - len(word)] and s[i - len(word):i] == word:
                    Flag = True
                    break
            dyn.append(Flag)
        return dyn[-1]
        
# 5-10min.
