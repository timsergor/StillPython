#89. Gray Code. Medium. 46.5%.

#The gray code is a binary numeral system where two successive values differ in only one bit.
#Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return([0])
        
        def solution(n):
            if n == 1:
                return([0,1])
            else:
                M1 = solution(n - 1)
                M2 = []
                for i in range(len(M1)):
                    M2.append(len(M1) + M1[-1 - i])
                M1.extend(M2)
                return(M1)
        
        return(solution(n))
