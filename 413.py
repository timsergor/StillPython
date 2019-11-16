# 5110. Synonymous Sentences. Medium. Contest.

# Given a list of pairs of equivalent words synonyms and a sentence text, Return all possible synonymous sentences sorted lexicographically.

from math import prod

class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        char = {}
        for s in synonyms:
            if s[0] in char:
                char[s[0]].add(s[1])
                for c in char[s[0]]:
                    if c != s[1]:
                        char[c].add(s[1])
            else:
                if s[1] in char:
                    char[s[0]] = char[s[1]].union(set([s[0], s[1]]))
                else:
                    char[s[0]] = set([s[0], s[1]])
            if s[1] in char:
                char[s[1]].add(s[0])
                for c in char[s[1]]:
                    if c != s[0]:
                        char[c].add(s[0])
            else:
                if s[0] in char:
                    char[s[1]] = char[s[0]].union(set([s[0], s[1]]))
                else:
                    char[s[1]] = set([s[0], s[1]])
        scheme = text.split()
        for c in char:
            L = list(char[c])
            L.sort()
            char[c] = L
        var = []
        for i in range(len(scheme)):
            if scheme[i] in char:
                var.append(len(char[scheme[i]]))
            else:
                var.append(1)
                char[scheme[i]] = [scheme[i]]
        answer = []
        counts = [0] * len(var)
        for i in range(prod(var)):
            new = []
            for j in range(len(counts)):
                new.append(char[scheme[j]][counts[j]])
            answer.append(" ".join(new))
            counts[-1] += 1
            for j in range(len(counts) - 1, -1, -1):
                if counts[j] == var[j]:
                    counts[j] = 0
                    counts[j - 1] += 1
            if counts[0] == var[0]:
                break
        return answer
        
