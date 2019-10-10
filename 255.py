# 984. String Without AAA or BBB. Medium. 34.8%.

# Given two integers A and B, return any string S such that:

# S has length A + B and contains exactly A 'a' letters, and exactly B 'b' letters;
# The substring 'aaa' does not occur in S;
# The substring 'bbb' does not occur in S.

class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        if A > B:
            if A <= 2 * B:
                return "aab" * (A - B) + "ab" * (2 * B - A)
            else:
                return "aab" * B + "a" * (A - 2 * B)
        elif B > A:
            if B <= 2 * A:
                return "bba" * (B - A) + "ba" * (2 * A - B)
            else:
                return "bba" * A + "b" * (B - 2 * A)
        else:
            return "ab" * A
