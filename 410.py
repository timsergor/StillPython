# 451. Sort Characters By Frequency. Medium. 57.8%.

# Given a string, sort it in decreasing order based on the frequency of characters.

class Solution:
    def frequencySort(self, s: str) -> str:
        char = {}
        for i in range(len(s)):
            if s[i] in char:
                char[s[i]] += 1
            else:
                char[s[i]] = 1
        scheme = []
        for c in char:
            scheme.append((char[c], c))
        scheme.sort(reverse = True)
        pre = []
        for p in scheme:
            pre.append(p[1] * p[0])
        return "".join(pre)
