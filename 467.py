# 151. Reverse Words in a String. Medium. 18.6%.

# Given an input string, reverse the string word by word.

class Solution:
    def reverseWords(self, s: str) -> str:
        S = s.split()
        S.reverse()
        return " ".join(S)
