# 1222. Queens That Can Attack the King. Medium. Contest.

# Given an array of integer coordinates queens that represents the positions of the Black Queens, and a pair of coordinates king that represent the position of the White King, return the coordinates of all the queens (in any order) that can attack the King.

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        def canHit(q,k):
            if q[0] == k[0]:
                for i in range(abs(k[1] - q[1]) - 1):
                    if [q[0],min(k[1], q[1]) + i + 1] in queens:
                        return False
                return True
            elif q[1] == k[1]:
                for i in range(abs(k[0] - q[0]) - 1):
                    if [min(q[0], k[0]) + i + 1, q[1]] in queens:
                        return False
                return True
            elif q[0] + q[1] == k[0] + k[1]:
                if q[0] < k[0]:
                    p = q
                else:
                    p = k
                for i in range(abs(k[1] - q[1]) - 1):
                    if [p[0] + i + 1, p[1] - i - 1] in queens:
                        return False
                return True
            elif q[0] - q[1] == k[0] - k[1]:
                if q[0] < k[0]:
                    p = q
                else:
                    p = k
                for i in range(abs(k[1] - q[1]) - 1):
                    if [p[0] + i + 1, p[1] + i + 1] in queens:
                        return False
                return True
            
        answer = []
        for q in queens:
            if canHit(q,king):
                answer.append(q)
        return answer
        
# 20-25min
