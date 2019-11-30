# 5113. Remove Interval. Medium. Contest.

# Given a sorted list of disjoint intervals, each interval intervals[i] = [a, b] represents the set of real numbers x such that a <= x < b.

# We remove the intersections between any interval in intervals and the interval toBeRemoved.

# Return a sorted list of intervals after all such removals.

class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        answer = []
        t = 0
        while t < len(intervals) and intervals[t][1] <= toBeRemoved[0]:
            answer.append(intervals[t])
            t += 1
        if t < len(intervals) and intervals[t][0] < toBeRemoved[0]:
            answer.append([intervals[t][0], toBeRemoved[0]])
            if t < len(intervals) and intervals[t][1] > toBeRemoved[1]:
                answer.append([toBeRemoved[1], intervals[t][1]])
            t += 1
        while t < len(intervals) and intervals[t][1] <= toBeRemoved[1]:
            t += 1
        if t < len(intervals) and intervals[t][1] > toBeRemoved[1] and intervals[t][0] < toBeRemoved[1]:
            answer.append([toBeRemoved[1], intervals[t][1]])
            t += 1
        while t < len(intervals):
            answer.append(intervals[t])
            t += 1
        return answer
