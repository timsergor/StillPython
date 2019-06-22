#We have an array A of integers, and an array queries of queries.
#For the i-th query val = queries[i][0], index = queries[i][1], we add val to A[index].  Then, the answer to the i-th query is the sum of the even values of A.
#(Here, the given index = queries[i][1] is a 0-based index, and each query permanently modifies the array A.)
#Return the answer to all queries.  Your answer array should have answer[i] as the answer to the i-th query.

class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]):
        s = 0
        С = []
        for i in range(len(A)):
            if A[i] % 2 == 0:
                s += A[i]
        for i in range(len(queries)):
            if A[queries[i][1]] % 2 == 0:
                s -= A[queries[i][1]]
            A[queries[i][1]] += queries[i][0]
            if A[queries[i][1]] % 2 == 0:
                s += A[queries[i][1]]
            С.append(s)        
        return(С)    
