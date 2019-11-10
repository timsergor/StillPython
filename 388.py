# 1255. Maximum Score Words Formed by Letters. Hard. RIGHT AFTER CONTEST... 71.6%.

# Given a list of words, list of  single letters (might be repeating) and score of every character.

# Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).

# It is not necessary to use all characters in letters and each letter can only be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def code(word):
            local = {}
            for s in word:
                x = ord(s) - ord("a")
                if x not in local:
                    local[x] = 1
                else:
                    local[x] += 1
            cd = []
            for c in range(26):
                if c in local:
                    cd.append(local[c])
                else:
                    cd.append(0)
            return cd
        
        codes = {}
        for word in words:
            codes[word] = code(word)
        
        glob = {}
        for l in letters:
            x = ord(l) - ord("a")
            if x not in glob:
                glob[x] = 1
            else:
                glob[x] += 1
        dis = []
        for c in range(26):
            if c in glob:
                dis.append(glob[c])
            else:
                dis.append(0)
        
        scheme = []
        for word in words:
            Flag = True
            for j in range(26):
                if codes[word][j] > dis[j]:
                    Flag = False
                    break
            if Flag:
                scheme.append(codes[word])
                for i in range(len(scheme) - 1):
                    Flag = True
                    new = []
                    for j in range(26):
                        new.append(codes[word][j] + scheme[i][j])
                        if new[-1] > dis[j]:
                            Flag = False
                            break
                    if Flag:
                        scheme.append(new)
        
        def cnt(s):
            x = 0
            for i in range(26):
                x += s[i] * score[i]
            return x
        
        answer = 0
        for s in scheme:
            answer = max(answer, cnt(s))
        return answer
