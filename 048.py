#890. Find and Replace Pattern. Medium. 71.5%

#You have a list of words and a pattern, and you want to know which words in words matches the pattern.
#A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.
#(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)
#Return a list of the words in words that match the given pattern. 
#You may return the answer in any order.

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def gettrace(s):
            trace = []
            p = 0
            char = {}
            for i in range(len(s)):
                if s[i] not in char:
                    char[s[i]] = p
                    p += 1
                    trace.append([i])
                else:
                    trace[char[s[i]]].append(i)
            return(trace)
        
        theTrace = gettrace(pattern)
        answer = []
        for i in range(len(words)):
            if gettrace(words[i]) == theTrace:
                answer.append(words[i])
        
        return(answer)
        
# 11 min.
