#925. Long Pressed Name. Easy. 44.5%.

#Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.
#You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(typed) < len(name):
            return(False)
        def code(s):
            i = 0
            c = s[i]
            Code = []
            n = 1
            i = 1
            while i < len(s):
                if s[i] == c:
                    n += 1
                    i += 1
                else:
                    Code.append([c,n])
                    c = s[i]
                    i += 1
                    n = 1
            Code.append([c,n])
            return(Code)
            
        Name = code(name)
        Typed = code(typed)
        if len(Name) != len(Typed):
            return(False)
        else:
            for i in range(len(Name)):
                if Name[i][0] != Typed[i][0] or Name[i][1] > Typed[i][1]:
                    return(False)
        return(True)
