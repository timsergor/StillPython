# 516. Longest Palindromic Subsequence. Medium. 49.2%.

# Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        pre = [1] * len(s)
        dyn = []
        for i in range(1,len(s)):
            if s[i] == s[i - 1]:
                dyn.append(2)
            else:
                dyn.append(1)
        for i in range(2,len(s)):
            new = []
            for j in range(i,len(s)):
                if s[j] == s[j - i]:
                    new.append(pre[j - i + 1] + 2)
                else:
                    new.append(max(dyn[j - i], dyn[j - i + 1]))
            pre = dyn
            dyn = new
        return dyn[0]
