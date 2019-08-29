#1143. Longest Common Subsequence. Medium. 58.3%.

#Given two strings text1 and text2, return the length of their longest common subsequence.
#A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text2) > len(text1):
            text1, text2 = text2, text1
        map = []
        for i in range(len(text1)):
            map.append([])
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    if i*j == 0:
                        map[-1].append(1)
                    else:
                        map[-1].append(map[i - 1][j - 1] + 1)
                else:
                    if i+j == 0:
                        map[-1].append(0)
                    elif i == 0:
                        map[-1].append(map[0][j - 1])
                    elif j == 0:
                        map[-1].append(map[i - 1][j])
                    else:
                        map[-1].append(max(map[i][j - 1],map[i - 1][j]))
        return(map[-1][-1])
