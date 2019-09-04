# 12. Integer to Roman

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        pre = []
        while num >= 1000:
            pre.append("M")
            num -= 1000
        if num >= 900:
            pre.append("CM")
            num -= 900
        elif num >= 400 and num < 500:
            pre.append("CD")
            num -= 400
        elif num >= 500:
            pre.append("D")
            num -= 500
        while num >= 100:
            pre.append("C")
            num -= 100
        if num >= 90:
            pre.append("XC")
            num -= 90
        elif num >= 40 and num < 50:
            pre.append("XL")
            num -= 40
        elif num >= 50:
            pre.append("L")
            num -= 50
        while num >= 10:
            pre.append("X")
            num -= 10
        if num >= 9:
            pre.append("IX")
            num -= 9
        elif num == 4:
            pre.append("IV")
            num -= 4
        elif num >= 5:
            pre.append("V")
            num -= 5
        while num >= 1:
            pre.append("I")
            num -= 1
        return("".join(pre))
        
# 9 min.
