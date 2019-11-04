# 1175. Prime Arrangements. Easy. 50.1%.

# Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)

# (Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers both smaller than it.)

# Since the answer may be large, return the answer modulo 10^9 + 7.

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def fac(k):
            K = 1
            while k:
                K *= k
                k -= 1
            return K
        
        def isPrime(n):
            for i in range(2,n // 2 + 1):
                if n % i == 0:
                    return False
            return True
        
        p = 2
        P = 0
        while p <= n:
            if isPrime(p):
                P += 1
            p += 1
        return (fac(P) * fac(n - P)) % (10 ** 9 + 7)
