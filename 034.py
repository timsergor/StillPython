#888. Fair Candy Swap

#Alice and Bob have candy bars of different sizes: A[i] is the size of the i-th bar of candy that Alice has, and B[j] is the size of the j-th bar of candy that Bob has.
#Since they are friends, they would like to exchange one candy bar each so that after the exchange, they both have the same total amount of candy.  (The total amount of candy a person has is the sum of the sizes of candy bars they have.)
#Return an integer array ans where ans[0] is the size of the candy bar that Alice must exchange, and ans[1] is the size of the candy bar that Bob must exchange.
#If there are multiple answers, you may return any one of them.  It is guaranteed an answer exists.

class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        d = sum(B) - sum(A)
        A.sort()
        B.sort()
        i = 0
        j = 0
        while (2 * (B[j] - A[i])) != d:
            if 2 * (B[j] - A[i]) > d:
                i += 1
            else:
                j += 1
        return(A[i],B[j])
        
# 10-15 min, n*logn

class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        d = sum(B) - sum(A)
        for i in range(len(B)):
            B[i] = (B[i] - (d / 2))
        setB = set(B)
        for x in A:
            if x in setB:
                return(x, d/2 + x)
                
 # n
