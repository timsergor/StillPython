#989. Add to Array-Form of Integer. Easy. 44.1%.

#For a non-negative integer X, the array-form of X is an array of its digits in left to right order.  For example, if X = 1231, then the array form is [1,2,3,1].
#Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.

class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        a = 0
        for i in range(len(A)):
            a += A[i]
            a *= 10
        b = ((a // 10) + K)
        B = []
        while b > 0:
            B.append(b % 10)
            b //= 10
        B.reverse()
        if len(B) == 0:
            B.append(0)
        return(B)
