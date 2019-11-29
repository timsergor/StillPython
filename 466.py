# 1015. Smallest Integer Divisible by K. Medium. 30.3%.

# Given a positive integer K, you need find the smallest positive integer N such that N is divisible by K, and N only contains the digit 1.

# Return the length of N.  If there is no such N, return -1.

class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K == 1:
            return 1
        mosts = [1]
        nosts = [1]
        story = set((1,1))
        while True:
            m = (mosts[-1] * 10) % K
            n = (nosts[-1] + m) % K
            if n == 0:
                return len(nosts) + 1
            elif (m,n) in story:
                return -1
            else:
                mosts.append(m)
                nosts.append(n)
                story.add((m,n))       
