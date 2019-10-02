# 1051. Height Checker. Easy. 68.4%.

# Students are asked to stand in non-decreasing order of heights for an annual photo.

# Return the minimum number of students not standing in the right positions.  (This is the number of students that must move in order for all students to be standing in non-decreasing order of height.)

class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        H = list(heights)
        heights.sort()
        answer = 0
        for i in range(len(H)):
            if H[i] != heights[i]:
                answer += 1
        return answer
