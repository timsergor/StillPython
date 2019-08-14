#70. Climbing Stairs. Easy. 44.8%
#You are climbing a stair case. It takes n steps to reach to the top.
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#Note: Given n will be a positive integer.

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return(n)
        else:
            a = 2
            b = 3
            n -= 3
            while n:
                c = a + b
                a = b
                b = c
                n -= 1
            return(c)
  
  # < 8min
