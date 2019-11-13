# 1014. Best Sightseeing Pair. Medium. 51%.

# Given an array A of positive integers, A[i] represents the value of the i-th sightseeing spot, and two sightseeing spots i and j have distance j - i between them.

# The score of a pair (i < j) of sightseeing spots is (A[i] + A[j] + i - j) : the sum of the values of the sightseeing spots, minus the distance between them.

# Return the maximum score of a pair of sightseeing spots.

class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        answer = 0
        back = A[0] - 1
        for i in range(1,len(A)):
            answer = max(answer, A[i] + back)
            back = max(back - 1,A[i] - 1)
        return answer
