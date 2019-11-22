# 436. Find Right Interval. Medium. 43.8%.

# Given a set of intervals, for each of the interval i, check if there exists an interval j whose start point is bigger than or equal to the end point of the interval i, which can be called that j is on the "right" of i.

# For any interval i, you need to store the minimum interval j's index, which means that the interval j has the minimum start point to build the "right" relationship for interval i. If the interval j doesn't exist, store -1 for the interval i. Finally, you need output the stored value of each interval as an array.

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        edges = []
        for i in range(len(intervals)):
            edges.append((intervals[i][0], i))
        
        def myKey(p):
            return p[0]
        
        edges.sort(key = myKey)
        
        answer = []
        for i in range(len(intervals)):
            l = 0
            r = len(intervals) - 1
            while r - l > 1:
                if edges[(r + l) // 2][0] < intervals[i][1]:
                    l = (r + l) // 2
                else:
                    r = (r + l) // 2
            if edges[l][0] >= intervals[i][1]:
                answer.append(edges[l][1])
            elif edges[r][0] < intervals[i][1]:
                answer.append(-1)
            else:
                answer.append(edges[r][1])
        return answer
