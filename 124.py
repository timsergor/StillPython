# 859. Buddy Strings. Easy. 27.8%.

# Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        mismatches = []
        for i in range(len(A)):
            if A[i] != B[i]:
                mismatches.append((A[i],B[i]))
        if len(mismatches) not in [0,2]:
            return False
        elif len(mismatches) == 2:
            if mismatches[0][0] == mismatches[1][1] and mismatches[0][1] == mismatches[1][0]:
                return True
            else:
                return False
        else:
            char = {}
            for i in range(len(A)):
                if A[i] not in char:
                    char[A[i]] = True
                else:
                    return True
            return False
