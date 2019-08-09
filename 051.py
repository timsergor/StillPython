#720. Longest Word in Dictionary. Easy.
#Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.
#If there is no answer, return the empty string.

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key = len)
        char = {}
        l = 0
        for i in range(len(words)):
            if len(words[i]) < 2:
                char[words[i]] = True
                l = len(words[i])
            elif words[i][0:len(words[i]) - 1] in char:
                char[words[i]] = True
                l = len(words[i])

        def lex(a,b):
            for i in range(min(len(a),len(b))):
                if ord(a[i]) < ord(b[i]):
                    return(True)
                elif ord(b[i]) < ord(a[i]):
                    return(False)

        z = "z"*l
        for w in char:      
            if len(w) == l and lex(w,z):
                z = w
        return(z)
