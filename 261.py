# 955. Delete Columns to Make Sorted II. Medium. 32.6%.

# We are given an array A of N lowercase letter strings, all of the same length.

# Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.

# For example, if we have an array A = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after deletions is ["bef","vyz"].

# Suppose we chose a set of deletion indices D such that after deletions, the final array has its elements in lexicographic order (A[0] <= A[1] <= A[2] ... <= A[A.length - 1]).

# Return the minimum possible value of D.length.

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        def check(s,I):
            newI = []
            for i in range(len(I)):
                toApp = [[I[i][0]]]
                for j in range(len(I[i]) - 1):
                    if A[I[i][j]][s] > A[I[i][j + 1]][s]:
                        return (False, I)
                    elif A[I[i][j]][s] == A[I[i][j + 1]][s]:
                        toApp[-1].append(I[i][j + 1])
                    else:
                        toApp.append([I[i][j + 1]])
                for i in range(len(toApp) - 1, -1, -1):
                    if len(toApp[i]) == 1:
                        toApp.pop(i)
                newI.extend(toApp)
            return (True, newI)
        
        if len(A) == 0 or len(A[0]) == 0:
            return 0
        answer = 0
        I = [list(range(len(A)))]
        print(I)
        for i in range(len(A[0])):
            p = check(i,I)
            print(p)
            if p[0] == False:
                answer += 1
            else:
                I = p[1]
            if len(I) == 0:
                return answer
        return answer
