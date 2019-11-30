# 5112. Hexspeak. Easy. Contest.

# A decimal number can be converted to its Hexspeak representation by first converting it to an uppercase hexadecimal string, then replacing all occurrences of the digit 0 with the letter O, and the digit 1 with the letter I.  Such a representation is valid if and only if it consists only of the letters in the set {"A", "B", "C", "D", "E", "F", "I", "O"}.

# Given a string num representing a decimal integer N, return the Hexspeak representation of N if it is valid, otherwise return "ERROR".

class Solution:
    def toHexspeak(self, num: str) -> str:
        num = int(num)
        pre = []
        while num:
            pre.append(num % 16)
            num //= 16
            if pre[-1] == 0:
                pre[-1] = "O"
            elif pre[-1] == 1:
                pre[-1] = "I"
            elif pre[-1] == 1:
                pre[-1] = "I"
            elif pre[-1] == 10:
                pre[-1] = "A"
            elif pre[-1] == 11:
                pre[-1] = "B"
            elif pre[-1] == 12:
                pre[-1] = "C"
            elif pre[-1] == 13:
                pre[-1] = "D"
            elif pre[-1] == 14:
                pre[-1] = "E"
            elif pre[-1] == 15:
                pre[-1] = "F"
            else:
                return "ERROR"
        pre.reverse()
        return "".join(pre)
