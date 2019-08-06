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
