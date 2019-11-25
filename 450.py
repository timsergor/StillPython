# 1052. Grumpy Bookstore Owner. Medium. 53.3%.

# Today, the bookstore owner has a store open for customers.length minutes.  Every minute, some number of customers (customers[i]) enter the store, and all those customers leave after the end of that minute.

# On some minutes, the bookstore owner is grumpy.  If the bookstore owner is grumpy on the i-th minute, grumpy[i] = 1, otherwise grumpy[i] = 0.  When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise they are satisfied.

# The bookstore owner knows a secret technique to keep themselves not grumpy for X minutes straight, but can only use it once.

# Return the maximum number of customers that can be satisfied throughout the day.

class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        answer = 0
        Y = 0
        profit = 0
        tail = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                answer += customers[i]
            else:
                while tail < i - X + 1:
                    if grumpy[tail]:
                        Y -=  customers[tail]
                    tail += 1
                if grumpy[i]:
                    Y += customers[i]
                profit = max(profit, Y)
        return answer + profit
