#Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.
#We repeatedly make duplicate removals on S until we no longer can.
#Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

class Solution:
    def removeDuplicates(self, S: str):
        T = ""
        filter = []
        for i in range(len(S)):
            filter.append(i)
        if len(S) < 2:
            return(S)   
        i = 0
        while i < len(filter)-1:
            if S[filter[i]] != S[filter[i+1]]:
                i += 1
            else:
                filter.pop(i)
                filter.pop(i)
                if i > 0:
                    i -= 1
        for i in filter:
            T = T + S[i]            
        return(T)
        
