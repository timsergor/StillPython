# 1259. Handshakes That Don't Cross. Hard. 50.2%.

# You are given an even number of people num_people that stand around a circle and each person shakes hands with someone else, so that there are num_people / 2 handshakes total.

# Return the number of ways these handshakes could occur such that none of the handshakes cross.

# Since this number could be very big, return the answer mod 10^9 + 7.

class Solution:
    def numberOfWays(self, num_people: int) -> int:
        dyn = [1, 1, 2, 5]
        if num_people < 7:
            return dyn[num_people // 2]
        for i in range(num_people // 2 - 3):
            new = 0
            for j in range(len(dyn)):
                new += dyn[j] * dyn[len(dyn) - 1 - j]
            dyn.append(new % (10 ** 9 + 7))
        return dyn[-1]
