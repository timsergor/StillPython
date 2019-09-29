# 49. Group Anagrams. 49.6%.

# Given an array of strings, group anagrams together.

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def code(word):
            char = {}
            for s in word:
                if s not in char:
                    char[s] = 1
                else:
                    char[s] += 1
            code = []
            for i in range(26):
                if chr(ord("a") + i) in char:
                    code.append(char[chr(ord("a") + i)])
                else:
                    code.append(0)
            return tuple(code)
        
        char = {}
        map = []
        t = 0
        for i in range(len(strs)):
            aCode = code(strs[i])
            map.append(aCode)
            if aCode not in char:
                char[aCode] = t
                t += 1
        answer = []
        for i in range(len(strs)):
            while len(answer) <= char[map[i]]:
                answer.append([])
            answer[char[map[i]]].append(strs[i])
        return answer
        
# 10-18min.
