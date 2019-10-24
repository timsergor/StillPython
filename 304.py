# 567. Permutation in String. Medium. 39.4%.

# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s2) < len(s1):
            return False
        S1 = {}
        sum1 = 0
        for i in range(len(s1)):
            if s1[i] not in S1:
                S1[s1[i]] = 1
                sum1 += 1
            else:
                S1[s1[i]] += 1
                sum1 += 1
        S2 = {}
        sum2 = 0
        for i in range(len(s2)):
            if sum2 == sum1:
                S2[s2[i - sum1]] -= 1
                sum2 -= 1
                if S2[s2[i - sum1]] == 0:
                    S2.pop(s2[i - sum1])
            if s2[i] not in S2:
                S2[s2[i]] = 1
                sum2 += 1
            else:
                S2[s2[i]] += 1
                sum2 += 1
            if S2 == S1:
                return True
        return False
