# 345. Reverse Vowels of a String. Easy. 42.1%.

# Write a function that takes a string as input and reverse only the vowels of a string.

class Solution:
    def reverseVowels(self, s: str) -> str:
        def isVowel(s):
            if s == "a" or s == "e" or s == "i" or s == "u" or s == "o" or s == "A" or s == "E" or s == "I" or s == "U" or s == "O":
                return(True)
            return(False)
        
        vowels = []
        for i in range(len(s)):
            if isVowel(s[i]):
                vowels.append(s[i])
        vowels.reverse()
        preanswer = []
        v = 0
        for i in range(len(s)):
            if isVowel(s[i]):
                preanswer.append(vowels[v])
                v += 1
            else:
                preanswer.append(s[i])
        return("".join(preanswer))
        
# 10min
