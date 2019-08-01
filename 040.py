#844. Backspace String Compare. Easy. 46.5%.

#Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def aftermath(s):
            t = []
            ignore = 0
            for i in range(len(s)):
                if s[len(s) - 1 - i] == "#":
                    ignore += 1
                elif ignore > 0:
                    ignore -= 1
                else:
                    t.append(s[len(s) - 1 - i])
            t.reverse()
            return("".join(t))
        
        return(aftermath(S) == aftermath(T))
        
# ~5 min
