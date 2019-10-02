# 91. Decode Ways. Medium. 23%.
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#'A' -> 1
#'B' -> 2
#...
#'Z' -> 26
#Given a non-empty string containing only digits, determine the total number of ways to decode it.

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dyn = [1,1]
        if len(s) == 0:
            return 1
        if s[0] == "0":
            return 0
        for i in range(1, len(s)):
            if (s[i - 1] == "1" and s[i] != "0") or (s[i - 1] == "2" and s[i] in ["1","2","3","4","5","6"]):
                dyn.append(dyn[-1] + dyn[-2])
            elif s[i] == "0":
                if s[i - 1] not in ["1","2"]:
                    return 0
                else:
                    dyn.append(dyn[-2])
            else:
                dyn.append(dyn[-1])
        return dyn[-1]
