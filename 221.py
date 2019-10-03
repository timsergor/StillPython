# 13. Roman to Integer. Easy. 53.4%.

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        S = list(s)
        answer = 0
        while S:
            if S[-1] == "I":
                answer += 1
                S.pop()
            elif S[-1] == "X":
                if len(S) > 1 and S[-2] == "I":
                    answer += 9
                    S.pop()
                else:
                    answer += 10
                S.pop()
            elif S[-1] == "C":
                if len(S) > 1 and S[-2] == "X":
                    answer += 90
                    S.pop()
                else:
                    answer += 100
                S.pop()
            elif S[-1] == "M":
                if len(S) > 1 and S[-2] == "C":
                    answer += 900
                    S.pop()
                else:
                    answer += 1000
                S.pop()
            elif S[-1] == "V":
                if len(S) > 1 and S[-2] == "I":
                    answer += 4
                    S.pop()
                else:
                    answer += 5
                S.pop()
            elif S[-1] == "L":
                if len(S) > 1 and S[-2] == "X":
                    answer += 40
                    S.pop()
                else:
                    answer += 50
                S.pop()
            elif S[-1] == "D":
                if len(S) > 1 and S[-2] == "C":
                    answer += 400
                    S.pop()
                else:
                    answer += 500
                S.pop()
        return answer
