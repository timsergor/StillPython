#969. Pancake Sorting. Medium. 62.1%.

#Given an array A, we can perform a pancake flip: We choose some positive integer k <= A.length, then reverse the order of the first k elements of A.  We want to perform zero or more pancake flips (doing them one after another in succession) to sort the array A.
#Return the k-values corresponding to a sequence of pancake flips that sort A.  Any valid answer that sorts the array within 10 * A.length flips will be judged as correct.

class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        def rev(M,n):
            N = []
            for i in range(len(M)):
                if i < n:
                    N.append(M[n - 1 - i])
                else:
                    N.append(M[i])
            return(N)
        
        solution = []
        for i in range(len(A)):
            if A[-1 -i] != len(A) - i:
                x = A.index(len(A) - i)
                solution.append(x + 1)
                solution.append(len(A) - i)
                A = rev(A,x + 1)
                A = rev(A,len(A) - i)
        return(solution)
