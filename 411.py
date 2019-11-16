# 5108. Encode Number. Medium. Contest.

# Given a non-negative integer num, Return its encoding string.

# The encoding is done by converting the integer to a string using a secret function that you should deduce from the following table:

class Solution:
    def encode(self, num: int) -> str:
        x = 0
        d = 1
        t = 0
        while num > x:
            x += d
            d *= 2
            t += 1
        if num == x:
            return "0" * t
        d //= 2
        x -= d
        pre = ["0"] * (t - 1)
        t = 0
        num -= x
        while num:
            if num % 2:
                pre[t] = "1"
            t += 1
            num //= 2
        pre.reverse()
        return "".join(pre)
