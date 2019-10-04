# 539. Minimum Time Difference. Medium. 49.2%.

# Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.

class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        timePoints.sort()
        
        def time(t,u):
            return (int(u[3:5]) - int(t[3:5])) + (int(u[0:2]) - int(t[0:2])) * 60
        
        answer = time("00:00", timePoints[0]) + time(timePoints[-1], "24:00")
        for i in range(len(timePoints) - 1):
            answer = min(answer, time(timePoints[i],timePoints[i + 1]))
        return answer
