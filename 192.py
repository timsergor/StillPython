# 56. Merge Intervals. Medium. 36.7%.

# Given a collection of intervals, merge all overlapping intervals.

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        def mykey(inter):
            return inter[1]
        
        intervals.sort(key = mykey)
        for i in range(len(intervals) - 1, 0, -1):
            if intervals[i - 1][1] >= intervals[i][0]:
                intervals[i - 1][1] = intervals[i][1]
                if intervals[i - 1][0] > intervals[i][0]:
                    intervals[i - 1][0] = intervals[i][0]
                intervals.pop(i)
        return intervals
