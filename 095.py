#405. Convert a Number to Hexadecimal. Easy. 42.3%.

#All letters in hexadecimal (a-f) must be in lowercase.
#The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
#The given number is guaranteed to fit within the range of a 32-bit signed integer.
#You must not use any method provided by the library which converts/formats the number to hex directly.

class Solution:
    def toHex(self, num: int) -> str:
        def hex(n):
            if n < 10:
                return(str(n))
            elif n == 10:
                return("a")
            elif n == 11:
                return("b")
            elif n == 12:
                return("c")
            elif n == 13:
                return("d")
            elif n == 14:
                return("e")
            else:
                return("f")
            
        if abs(num) == 0:
            return(str(0))
        
        def solution(num):
            pre = []
            while num > 0:
                ost = num % 16
                pre.append(hex(ost))
                num //= 16
            pre.reverse()
            return("".join(pre))
        
        if num > 0:
            return(solution(num))
        else:
            return(solution(num + 16**8))
