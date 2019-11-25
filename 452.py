# 1003. Check If Word Is Valid After Substitutions. Medium. 53.3%.

# We are given that the string "abc" is valid.

# From any valid string V, we may split V into two pieces X and Y such that X + Y (X concatenated with Y) is equal to V.  (X or Y may be empty.)  Then, X + "abc" + Y is also valid.

# If for example S = "abc", then examples of valid strings are: "abc", "aabcbc", "abcabc", "abcabcababcc".  Examples of invalid strings are: "abccba", "ab", "cababc", "bac".

# Return true if and only if the given string S is valid.

class Solution(object):
    def isValid(self, S):
        """
        :type S: str
        :rtype: bool
        """
        scheme = []
        if len(S) % 3:
            return False
        for i in range(len(S)):
            if S[i] == "a":
                scheme.append(0)
            elif S[i] == "b":
                if scheme and scheme[-1] == 0:
                    scheme[-1] += 1
                else:
                    return False
            else:
                if scheme and scheme[-1] == 1:
                    scheme.pop()
                else:
                    return False
        return len(scheme) == 0
