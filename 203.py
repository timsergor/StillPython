# 917. Reverse Only Letters. Easy. 56.3%.

# Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        pre = []
        for i in range(len(S)):
            pre.append(S[i])
        t = len(S) - 1
        u = 0
        while u < len(S):
            if (ord(S[u]) >= ord("a") and ord(S[u]) <= ord("z")) or (ord(S[u]) >= ord("A") and ord(S[u]) <= ord("Z")):
                while not((ord(S[t]) >= ord("a") and ord(S[t]) <= ord("z")) or (ord(S[t]) >= ord("A") and ord(S[t]) <= ord("Z"))):
                    t -= 1
                pre[u] = S[t]
                t -= 1
            u += 1
        return "".join(pre)

# 10-20min.
