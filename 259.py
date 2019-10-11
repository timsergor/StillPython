# 823. Binary Trees With Factors. Medium. 33.5%.

# Given an array of unique integers, each integer is strictly greater than 1.

# We make a binary tree using these integers and each number may be used for any number of times.

# Each non-leaf node's value should be equal to the product of the values of it's children.

# How many binary trees can we make?  Return the answer modulo 10 ** 9 + 7.

class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        char = {c:1 for c in A}
        A.sort()
        for i in range(len(A)):
            for j in range(i):
                if A[i] % A[j] == 0 and A[i] // A[j] in char:
                    char[A[i]] += char[A[j]] * char[A[i] // A[j]]
        answer = 0
        for c in char:
            answer += char[c]
        return answer % (10**9 + 7)
        
< 9 min.
