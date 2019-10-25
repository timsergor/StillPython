# 833. Find And Replace in String. 48%.

# To some string S, we will perform some replacement operations that replace groups of letters with new ones (not necessarily the same size).

# Each replacement operation has 3 parameters: a starting index i, a source word x and a target word y.  The rule is that if x starts at position i in the original string S, then we will replace that occurrence of x with y.  If not, we do nothing.

# For example, if we have S = "abcd" and we have some replacement operation i = 2, x = "cd", y = "ffff", then because "cd" starts at position 2 in the original string S, we will replace it with "ffff".

# Using another example on S = "abcd", if we have both the replacement operation i = 0, x = "ab", y = "eee", as well as another replacement operation i = 2, x = "ec", y = "ffff", this second operation does nothing because in the original string S[2] = 'c', which doesn't match x[0] = 'e'.

# All these operations occur simultaneously.  It's guaranteed that there won't be any overlap in replacement: for example, S = "abc", indexes = [0, 1], sources = ["ab","bc"] is not a valid test case.

class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        scheme = []
        for i in range(len(indexes)):
            scheme.append((indexes[i], sources[i], targets[i]))
        
        def myKey(p):
            return p[0]
        
        scheme.sort(key = myKey)
        
        def check(i, s):
            for j in range(len(s)):
                if S[i + j] != s[j]:
                    return False
            return True
        
        t = 0
        pre = []
        for i in range(len(scheme)):
            if check(scheme[i][0], scheme[i][1]):
                pre.append(S[t:scheme[i][0]])
                pre.append(scheme[i][2])
                t = scheme[i][0] + len(scheme[i][1])
        pre.append(S[t:len(S)])
        return "".join(pre)
