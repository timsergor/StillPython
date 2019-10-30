# 306. Additive Number. Medium. 28.8%.

# Additive number is a string whose digits can form additive sequence.

# A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

# Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

# Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3:
            return False
        pre = []
        for i in range(1,len(num) + 1):
            for j in range(1,i):
                for k in range(1,j):
                    if (num[0] != "0" or k == 1) and (num[k] != "0" or j - k == 1) and (num[j] != "0" or i - j == 1) and int(num[0:k]) + int(num[k:j]) == int(num[j:i]):
                        pre.append((k,j,i))
        
        def isIt(p):
            if p[2] - len(num) == 0:
                return True
            else:
                nxt = str(int(num[p[0]:p[1]]) + int(num[p[1]:p[2]]))
                print(nxt)
                for i in range(len(nxt)):
                    if p[2] + i < len(num) and num[p[2] + i] != nxt[i]:
                        return False
                if p[2] <= len(num):
                    return isIt((p[1],p[2],p[2] + len(nxt)))
                else:
                    return False
        
        for p in pre:
            if isIt(p):
                return True
        return False
