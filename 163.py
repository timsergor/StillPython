# 816. Ambiguous Coordinates. Medium. 44.8%.
# We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)".  Then, we removed all commas, decimal points, and spaces, and ended up with the string S.  Return a list of strings representing all possibilities for what our original coordinates could have been.
# Our original representation never had extraneous zeroes, so we never started with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", or any other number that can be represented with less digits.  Also, a decimal point within a number never occurs without at least one digit occuring before it, so we never started with numbers like ".1".
# The final answer list can be returned in any order.  Also note that all coordinates in the final answer have exactly one space between them (occurring after the comma.)

class Solution(object):
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        def check(s):
            if int(s[0]) and int(s[-1]):
                return 1
            elif int(s[-1]):
                return 2
            elif int(s[0]):
                return 3
            else:
                return 0
        
        answer = []
        for i in range(len(S) - 3):
            A = []
            B = []
            if i == 0:
                A.append(S[1])
            else:
                key = check(S[1:i + 2])
                if key == 3:
                    A.append(S[1:i + 2])
                if key == 2:
                    A.append(S[1] + "." + S[2:i + 2])
                if key == 1:
                    A.append(S[1:i + 2])
                    for j in range(i):
                        A.append(S[1:2 + j] + "." + S[2 + j: i + 2])
            if i == len(S) - 4:
                B.append(S[-2])
            else:
                key = check(S[i + 2: len(S) - 1])
                if key == 3:
                    B.append(S[i + 2: len(S) - 1])
                if key == 2:
                    B.append(S[i + 2] + "." + S[i + 3:len(S) - 1])
                if key == 1:
                    B.append(S[i + 2: len(S) - 1])
                    for j in range(len(S) - i - 4):
                        B.append(S[i + 2:i + 3 + j] + "." + S[i + 3 + j: len(S) - 1])
            for a in range(len(A)):
                for b in range(len(B)):
                    answer.append("(" + A[a] + ", " + B[b] + ")")
        return answer
