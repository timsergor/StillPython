#Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

class Solution:
    def shortestToChar(self, S: str, C: str):
        M = [10000]*len(S)
        last = -10000
        i = 0
        while i < len(S):
            if S[i] != C:
                M[i] = i - last
                i += 1    
            else:
                last = i
                while i > -1:
                    if M[i] > (last-i):
                        M[i] = last-i
                        i -= 1
                    else:
                        i = last + 1
                        break 
                if i == -1:        
                    i = last + 1        
        if last > -1:
            for i in range(last,len(S)):
                M[i] = i - last
        return(M) 
