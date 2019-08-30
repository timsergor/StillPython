#739. Daily Temperatures. Medium. 60.5%.
#Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.
#For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
#Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        calendar = []
        char = {i:0 for i in range(30,101)}
        for i in range(len(T)):
            if char[T[-1 - i]] == 0:
                calendar.append(0)
            else:
                calendar.append(char[T[-1 - i]] - (len(T) - i - 1))
            for c in char:
                if c < T[-1 - i]:
                    char[c] = len(T) - i - 1
        calendar.reverse()
        return(calendar)
        
# 12min.
