# 77. Combinations. Medium. 50.4%.

# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0:
            return [[]]
        answer = []
        for i in range(k, n + 1):
            answer.append([i])
        while len(answer[0]) < k:
            pre = []
            for t in answer:
                for i in range(k - len(t), t[-1]):
                    pre.append(t + [i])
            answer = pre
        return answer
