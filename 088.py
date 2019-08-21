#931. Minimum Falling Path Sum. Medium. 59.1%.

#Given a square array of integers A, we want the minimum sum of a falling path through A.
#A falling path starts at any element in the first row, and chooses one element from each row.  The next row's choice must be in a column that is different from the previous row's column by at most one.

class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        step = A[len(A) - 1]
        for i in range(1,len(A)):
            prestep = step
            step = []
            for j in range(len(A)):
                if j > 0 and j < len(A) - 1:
                    step.append(min(prestep[j - 1], prestep[j], prestep[j + 1]) + A[len(A) - 1 - i][j])
                elif j == 0:
                    step.append(min(prestep[j], prestep[j + 1]) + A[len(A) - 1 - i][j])
                else:
                    step.append(min(prestep[j - 1], prestep[j]) + A[len(A) - 1 - i][j])
        return(min(step))
        
# 12min
