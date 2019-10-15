# 481. Magical String. Medium. 46.7%.

# A magical string S consists of only '1' and '2' and obeys the following rules:

# The string S is magical because concatenating the number of contiguous occurrences of characters '1' and '2' generates the string S itself.

# The first few elements of string S is the following: S = "1221121221221121122……"

# If we group the consecutive '1's and '2's in S, it will be:

# 1 22 11 2 1 22 1 22 11 2 11 22 ......

# and the occurrences of '1's or '2's in each group are:

# 1 2 2 1 1 2 1 2 2 1 2 2 ......

# You can see that the occurrence sequence above is the S itself.

# Given an integer N as input, return the number of '1's in the first N number in the magical string S.

# Note: N will not exceed 100,000.

class Solution:
    def magicalString(self, n: int) -> int:
        answer = 0
        s = "1221121221221121122"
        if n < 20:
            for t in range(n):
                if s[t] == "1":
                    answer += 1
            return answer
        S = list(s)
        t = 12
        answer = 9
        while len(S) < n:
            x = 3 - int(S[-1])
            for i in range(int(S[t])):
                S.append(str(x))
                if x == 1:
                    answer += 1
            t += 1
        if len(S) == n:
            return answer
        else:
            return answer - int(S[-1] == "1")
