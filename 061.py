#537. Complex Number Multiplication. Medium. 65.9%
#Given two strings representing two complex numbers.
#You need to return a string representing their multiplication. Note i^2 = -1 according to the definition.

class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        def couple(s):
            Z = s.split("+")
            Z[0] = int(Z[0])
            Z[1] = int(Z[1][0:len(Z[1]) - 1])
            return(Z)
            
        a = couple(a)
        b = couple(b)
        x = a[0]*b[0] - a[1]*b[1]
        y = a[1]*b[0] + a[0]*b[1]
        return(str(x) + "+" + str(y) + "i")
