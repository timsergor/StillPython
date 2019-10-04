# 57. Insert Interval. Hard. 31.9%.

# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

# You may assume that the intervals were initially sorted according to their start times.

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return[newInterval]
        elif len(intervals) == 1:
            if intervals[0][1] < newInterval[0]:
                return intervals + [newInterval]
            elif intervals[0][0] > newInterval[1]:
                return [newInterval] + intervals
            else:
                return [[min(newInterval[0],intervals[0][0]),max(newInterval[1],intervals[0][1])]]
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        elif newInterval[0] > intervals[-1][1]:
            return intervals + [newInterval]
        l1 = 0
        r1 = len(intervals) - 1
        while r1 - l1 > 1:
            if newInterval[0] >= intervals[(l1 + r1) // 2][0]:
                l1 = (l1 + r1) // 2
            else:
                r1 = (l1 + r1) // 2
        l2 = l1
        r2 = len(intervals) - 1
        while r2 - l2 > 1:
            if newInterval[1] >= intervals[(l2 + r2) // 2][0]:
                l2 = (l2 + r2) // 2
            else:
                r2 = (l2 + r2) // 2
        if newInterval[0] <= intervals[l1][1] and newInterval[1] < intervals[r2][0]:
            return intervals[0:l1] + [[min(intervals[l1][0],newInterval[0]),max(intervals[l2][1],newInterval[1])]] + intervals[l2 + 1: len(intervals)]
        elif newInterval[0] > intervals[l1][1] and newInterval[1] < intervals[r2][0]:
            return intervals[0:l1 + 1] + [[min(newInterval[0],intervals[l1 + 1][0]),max(intervals[l2][1],newInterval[1])]] + intervals[l2 + 1: len(intervals)]
        elif newInterval[0] <= intervals[l1][1] and newInterval[1] >= intervals[r2][0]:
            return intervals[0:l1] + [[min(intervals[l1][0],newInterval[0]), max(intervals[l2 + 1][1],newInterval[1])]] + intervals[l2 + 2: len(intervals)]
        elif newInterval[0] > intervals[l1][1] and newInterval[1] >= intervals[r2][0]:
            return intervals[0:l1 + 1] + [[min(newInterval[0],intervals[l1 + 1][0]), max(intervals[l2 + 1][1],newInterval[1])]] + intervals[l2 + 2: len(intervals)]
