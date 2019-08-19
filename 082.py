58. Length of Last Word. Easy. 32.3%.
#Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
#If the last word does not exist, return 0.
#Note: A word is defined as a character sequence consists of non-space characters only.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        current = 0
        Flag = True
        for i in range(len(s)):
            if s[i] != " " and Flag:
                current += 1
            elif s[i] != " ":
                current = 1
                Flag = True
            else:
                Flag = False
        return(current)
