# 541. Reverse String II. Easy. 45.8%
# Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original

class Solution:
    def reverseStr(self, s: str, k: int):
        i = 0
        pre = []
        while i < len(s):
            if (i % (2*k) == 0):
                i += k
                for j in range(k):
                    if i - j - 1 < len(s):
                        pre.append(s[i - j - 1])
            else:
                pre.append(s[i])
                i += 1
        return("".join(pre))
