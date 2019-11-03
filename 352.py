# 1249. Minimum Remove to Make Valid Parentheses. Medium. 53%.

# Given a string s of '(' , ')' and lowercase English characters. 

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        pre = []
        i = 0
        t = 0
        while i < len(s):
            if s[i] == "(":
                t += 1
            elif s[i] == ")":
                t -= 1
            if t >= 0:
                pre.append(s[i])
            else:
                t += 1
            i += 1
        i = len(pre) - 1
        print(pre)
        while t and i >= 0:
            if i >= 0 and pre[i] == "(":
                t -= 1
                pre.pop(i)
            i -= 1
        return "".join(pre)
