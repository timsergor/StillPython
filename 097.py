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
