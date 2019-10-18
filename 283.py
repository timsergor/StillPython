# 767. Reorganize String. Medium. 44.3%.

# Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

# If possible, output any possible result.  If not possible, return the empty string.

class Solution:
    def reorganizeString(self, S: str) -> str:
        char = {}
        for i in range(len(S)):
            if S[i] not in char:
                char[S[i]] = 1
            else:
                char[S[i]] += 1
                
        m = 0
        for c in char:
            if char[c] > m:
                m = char[c]        
        
        if m >= len(S) / 2 + 1 or len(S) == 0:
            return ""
        
        map = []
        for c in char:
            map.append([c,char[c]])
            
        def myKey(p):
            return p[1]
        
        map.sort(key = myKey)
        pre = []
        while len(pre) < len(S):
            if not pre or map[-1][0] != pre[-1]:
                pre.append(map[-1][0])
                map[-1][1] -= 1
                if map[-1][1] == 0:
                    map.pop()
            else:
                pre.append(map[-2][0])
                map[-2][1] -= 1
                if map[-2][1] == 0:
                    map.pop(-2)
            map.sort(key = myKey)
            
        return "".join(pre) 
