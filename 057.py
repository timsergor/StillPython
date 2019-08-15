#119. Pascal's Triangle II. Easy. 44.7%.

#Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
#Note that the row index starts from 0.

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def solution(rowIndex):
            if rowIndex == 0:
                return([1])
            else:
                M = solution(rowIndex-1)
                N = [1]
                for i in range(len(M) - 1):
                    N.append(M[i] + M[i+1])
                N.append(1)
            return(N)
        
        return(solution(rowIndex))
        
 # < 5min
