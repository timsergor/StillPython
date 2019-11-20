# 826. Most Profit Assigning Work. Medium. 37.2%.

# We have jobs: difficulty[i] is the difficulty of the ith job, and profit[i] is the profit of the ith job. 

# Now we have some workers. worker[i] is the ability of the ith worker, which means that this worker can only complete a job with difficulty at most worker[i]. 

# Every worker can be assigned at most one job, but one job can be completed multiple times.

# For example, if 3 people attempt the same job that pays $1, then the total profit will be $3.  If a worker cannot complete any job, his profit is $0.

# What is the most profit we can make?

class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        jobs = [[difficulty[i], profit[i]] for i in range(len(profit))]
        
        def myKey(p):
            return p[0]
        
        jobs.sort(key = myKey)
        s = jobs[0][1]
        for i in range(len(jobs)):
            if s > jobs[i][1]:
                jobs[i][1] = s
            else:
                s = jobs[i][1]
        
        def optimize(w):
            l = 0
            r = len(jobs) - 1
            while r - l > 1:
                if jobs[(r + l) // 2][0] > w:
                    r = (r + l) // 2
                else:
                    l = (r + l) // 2
            if jobs[r][0] <= w:
                return jobs[r][1]
            elif jobs[l][0] <= w:
                return jobs[l][1]
            else:
                return 0
        
        answer = 0
        for w in worker:
            answer += optimize(w)
        return answer
