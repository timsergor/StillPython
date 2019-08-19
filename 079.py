#415. Add Strings. Easy.
#Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

#Note:
#The length of both num1 and num2 is < 5100.
#Both num1 and num2 contains only digits 0-9.
#Both num1 and num2 does not contain any leading zero.
#You must not use any built-in BigInteger library or convert the inputs to integer directly.

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        mem = 0
        preanswer = []
        for i in range(max(len(num1),len(num2)) + 1):
            if i < len(num1):
                n1 = int(num1[len(num1) - 1 - i])
            else:
                n1 = 0
            if i < len(num2):
                n2 = int(num2[len(num2) - 1 - i])
            else:
                n2 = 0
            n = n1 + n2 + mem
            preanswer.append(str(n % 10))
            mem = n // 10
        while preanswer[len(preanswer) - 1] == "0" and len(preanswer) > 1:
            preanswer.pop()
        preanswer.reverse()
        answer = "".join(preanswer)
        return(answer)

# 20min
