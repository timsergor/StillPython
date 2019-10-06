# 5216. Count Vowels Permutation. Hard. Contest.

# Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

# Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
# Each vowel 'a' may only be followed by an 'e'.
# Each vowel 'e' may only be followed by an 'a' or an 'i'.
# Each vowel 'i' may not be followed by another 'i'.
# Each vowel 'o' may only be followed by an 'i' or a 'u'.
# Each vowel 'u' may only be followed by an 'a'.
# Since the answer may be too large, return it modulo 10^9 + 7.

class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        map = [[1],[1],[1],[1],[1]]
        for i in range(n - 1):
            for j in range(0,5):
                if j == 0:
                    map[j].append(map[1][i] + map[2][i] + map[4][i])
                elif j == 1:
                    map[j].append(map[0][i] + map[2][i])
                elif j == 2:
                    map[j].append(map[1][i] + map[3][i])
                elif j == 3:
                    map[j].append(map[2][i])
                elif j == 4:
                    map[j].append(map[2][i] + map[3][i])
        return (map[0][-1] + map[1][-1] + map[2][-1] + map[3][-1] + map[4][-1]) % (10**9 + 7)
