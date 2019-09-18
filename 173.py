# 762. Prime Number of Set Bits in Binary Representation. Easy. 60.4%.

# Given two integers L and R, find the count of numbers in the range [L, R] (inclusive) having a prime number of set bits in their binary representation.

# (Recall that the number of set bits an integer has is the number of 1s present when written in binary. For example, 21 written in binary is 10101 which has 3 set bits. Also, 1 is not a prime.)

class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        def check(n):
            r = []
            while n > 0:
                r.append(n % 2)
                n //= 2
            p = sum(r)
            return p in [2,3,5,7,11,13,17,19]
        
        answer = 0
        for i in range(L,R + 1):
            if check(i):
                answer += 1
        return answer
        
# 7min.
