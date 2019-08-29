# 38. Count and Say. Easy. 41.5%.
#The count-and-say sequence is the sequence of integers with the first five terms as following:
#1.     1
#2.     11
#3.     21
#4.     1211
#5.     111221
#1 is read off as "one 1" or 11.
#11 is read off as "two 1s" or 21.
#21 is read off as "one 2, then one 1" or 1211.
#Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
#Note: Each term of the sequence of integers will be represented as a string.

class Solution:
    def countAndSay(self, n: int) -> str:
        def solution(n):
            if n == 1:
                return("1")
            else:
                s = solution(n - 1)
                nexts = []
                for i in range(len(s)):
                    if i == 0 or s[i] != s[i -1]:
                        if i:
                            nexts.append(str(t))
                            nexts.append(c)
                        c = s[i]
                        t = 0
                    if s[i] == c:
                        t += 1
                nexts.append(str(t))
                nexts.append(c)
                return("".join(nexts))
        return(solution(n))
        
# 12min
