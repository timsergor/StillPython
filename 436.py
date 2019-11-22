# 983. Minimum Cost For Tickets. Medium. 57.9%.

# In a country popular for train travel, you have planned some train travelling one year in advance.  The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

# Train tickets are sold in 3 different ways:

# a 1-day pass is sold for costs[0] dollars;
# a 7-day pass is sold for costs[1] dollars;
# a 30-day pass is sold for costs[2] dollars.
# The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

# Return the minimum number of dollars you need to travel every day in the given list of days.

class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        dyn = [min(costs)]
        for i in range(1,len(days)):
            t = 1
            x = dyn[-1] + min(costs)
            t = i - 1
            while t >= 0 and days[i] - days[t] < 7:
                t -= 1
            if t >= 0:
                x = min(x, dyn[t] + costs[1])
            else:
                x = min(x, costs[1])
            while t >= 0 and days[i] - days[t] < 30:
                t -= 1
            if t >= 0:
                x = min(x, dyn[t] + costs[2])
            else:
                x = min(x, costs[2])
            dyn.append(x)
        return dyn[-1]
