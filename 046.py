#202. Happy Number. Easy. 46%.

#Write an algorithm to determine if a number is "happy".
#A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

class Solution:
    def isHappy(self, n: int) -> bool:
        def next(n):
            m = 0
            while n > 0:
                m += (n % 10)**2
                n = n // 10
            return(m)
        
        if n == 1:
            return(True)
        char = {n:True}
        while n != 1:
            n = next(n)
            if n == 1:
                return(True)
            elif n in char:
                return(False)
            else:
                char[n] = True
   # 15min
