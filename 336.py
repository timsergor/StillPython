# 5. Longest Palindromic Substring. Medium. 28.2%.

# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ln = 0
        answer = ""
        for i in range(len(s)):
            p = 1
            while i - p >= 0 and i + p < len(s):
                if s[i - p] != s[i + p]:
                    break
                p += 1
            if ln < 2 * p - 1:
                ln = 2 * p - 1
                answer = s[i - p + 1:i + p]
        for i in range(len(s) - 1):
            p = 0
            while i - p >= 0 and i + 1 + p < len(s):
                if s[i - p] != s[i + 1 + p]:
                    break
                p += 1
            if ln < 2 * p:
                ln = 2 * p
                answer = s[i - p + 1:i + p + 1]
        return answer
