# 474. Ones and Zeroes. Medium. 41%.

# In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.
# For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, there is an array with strings consisting of only 0s and 1s.
# Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.
# Note:
# The given numbers of 0s and 1s will both not exceed 100
# The size of given string array won't exceed 600.

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        char = {(0,0) : 0}
        for i in range(len(strs)):
            a = b = 0
            for j in range(len(strs[i])):
                if strs[i][j] == "0":
                    a += 1
                else:
                    b += 1
            if a <= m and b <= n:
                new = {}
                for c in char:
                    if c[0] + a <= m and c[1] + b <= n:
                        p = (c[0] + a, c[1] + b)
                        if p not in char:
                            new[p] = char[c] + 1
                        else:
                            new[p] = max(char[p], char[c] + 1)
                for c in new:
                    char[c] = new[c]               
        answer = 0
        for c in char:
            answer = max(answer, char[c])
        return answer
