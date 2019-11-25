# 592. Fraction Addition and Subtraction. Medium. 47.7%.

# Given a string representing an expression of fraction addition and subtraction, you need to return the calculation result in string format. The final result should be irreducible fraction. If your final result is an integer, say 2, you need to change it to the format of fraction that has denominator 1. So in this case, 2 should be converted to 2/1.

class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        fractions = []
        signes = []
        l = 0
        r = 0
        while l < len(expression):
            if expression[l] in ["+", "-"]:
                l += 1
            else:
                r = l + 1
                while r < len(expression) and expression[r] not in ["+", "-"]:
                    r += 1
                if l == 0 or expression[l - 1] == "+":
                    signes.append("+")
                else:
                    signes.append("-")
                fractions.append(expression[l:r].split("/"))
                fractions[-1][0] = int(fractions[-1][0])
                fractions[-1][1] = int(fractions[-1][1])
                l = r + 1
        
        def nod(a,b):
            a, b = max(a, b), min(a, b)
            while a % b:
                a = a % b
                a, b = b, a
            return b
            
        def nok(a,b):
            return a * b // nod(a, b)
        
        den = 1
        for i in range(len(fractions)):
            den = nok(den, fractions[i][1])
        num = 0
        for i in range(len(fractions)):
            if signes[i] == "+":
                num += fractions[i][0] * (den // fractions[i][1])
            else:
                num -= fractions[i][0] * (den // fractions[i][1])
        if num == 0:
            return "0/1"
        c = (nod(abs(num), den))
        num //= c
        den //= c
        return str(num) + "/" + str(den)
