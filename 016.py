#Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

#1
class Solution:
    def reverseWords(self, s: str):
        def reverseWord(u):
            v = ""
            for i in range(len(u)):
                v = v + u[len(u)-1-i]
            return(v)    
        S = s.split()
        t = ""
        for i in range(len(S)):
            if i == 0:
                t = reverseWord(S[i])
            else:
                t = t + " " + reverseWord(S[i])
        return(t)        

#2
class Solution:
    def reverseWords(self, s: str):
        i = 0
        Flag = True
        c = 0
        t = ""
        while i < len(s):
            if s[i] != " " and Flag == True:
                i += 1
            elif s[i] == " " and Flag == True:
                if len(t) > 0:
                    u = " "  
                else:
                    u = ""
                Flag = False
                c = i
                i -= 1
            elif i == -1 or (s[i] == " " and Flag == False):
                t = t + u
                i = c + 1
                Flag = True    
            elif s[i] != " " and Flag == False:
                u = u + s[i]
                i -= 1
        if len(t) > 0:
            u = " "  
        else:
            u = ""          
        i -= 1
        while i > -1 and s[i] != " ":         
            u = u + s[i]
            i -= 1 
        t = t + u       
        return(t)            
