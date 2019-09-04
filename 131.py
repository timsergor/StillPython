# 67. Add Binary. Easy. 40.3%.

# Given two binary strings, return their sum (also a binary string).
# The input strings are both non-empty and contains only characters 1 or 0.

class Solution(object):        
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def xor(x,y,z):
            if (x * y * z == 1) or (x + y + z == 1):
                return 1
            else:
                return 0
        
        pre = []
        mem = 0
        for i in range(max(len(a),len(b))):
            if len(a) -1 - i < 0:
                A = 0
            else:
                A = int(a[len(a) -1 - i])
            if len(b) -1 - i < 0:
                B = 0
            else:
                B = int(b[len(b) -1 - i])
            pre.append(str(xor(A,B,mem)))
            if A + B + mem > 1:
                mem = 1
            else:
                mem = 0
        if mem == 1:
            pre.append(str(mem))
        pre.reverse()
        return("".join(pre))

# < 25min
