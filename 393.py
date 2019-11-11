# 216. Combination Sum III. Medium. 53.6%.

# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        dyn = Queue()
        answer = []
        t = 1
        x = []
        for i in range(1, 10):
            dyn.put([i])
        while t < k and not dyn.empty():
            x = dyn.get()
            if len(x) > t:
                t += 1
                if t == k:
                    break
            for i in range(x[-1] + 1, min(10, n + 1)):
                new = x + [i]
                s = sum(new)
                if s <= n:
                    dyn.put(new)
        if sum(x) == n and len(x) == k:
            answer.append(x)
        while not dyn.empty():
            x = dyn.get()
            if sum(x) == n and len(x) == k:
                answer.append(x)
        return answer
