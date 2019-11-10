# 1253. Reconstruct a 2-Row Binary Matrix. Medium. Contest.

# Given the following details of a matrix with n columns and 2 rows :

# The matrix is a binary matrix, which means each element in the matrix can be 0 or 1.
# The sum of elements of the 0-th(upper) row is given as upper.
# The sum of elements of the 1-st(lower) row is given as lower.
# The sum of elements in the i-th column(0-indexed) is colsum[i], where colsum is given as an integer array with length n.
# Your task is to reconstruct the matrix with upper, lower and colsum.

# Return it as a 2-D integer array.

# If there are more than one valid solution, any of them will be accepted.

# If no valid solution exists, return an empty 2-D array.

class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        answer = [[],[]]
        for i in range(len(colsum)):
            if colsum[i] == 2:
                answer[0].append(1)
                answer[1].append(1)
                upper -= 1
                lower -= 1
            elif colsum[i] == 0:
                answer[0].append(0)
                answer[1].append(0)
            else:
                if upper >= lower:
                    answer[0].append(1)
                    answer[1].append(0)
                    upper -= 1
                else:
                    answer[0].append(0)
                    answer[1].append(1)
                    lower -= 1
            if upper == -1 or lower == -1:
                return []
        if upper == 0 and lower == 0:
            return answer
        else:
            return []
