# 524. Longest Word in Dictionary through Deleting. Medium. 46.9%.

# Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        def check(word):
            i = 0
            j = 0
            while i < len(word) and j < len(s):
                if s[j] == word[i]:
                    i += 1
                    j += 1
                else:
                    j += 1
            if i == len(word):
                return True
            return False
        
        answer = ""
        for word in d:
            if check(word):
                if len(word) > len(answer):
                    answer = word
                elif len(word) == len(answer):
                    answer = min(answer, word)
        return answer
