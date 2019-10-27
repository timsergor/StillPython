# 47. Permutations II. Medium. 42.8%.

# Given a collection of numbers that might contain duplicates, return all possible unique permutations.

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        def nxt(q):
            p = list(q)
            t = -1
            for i in range(len(p) - 2, -1, -1):
                if p[i] < p[i + 1]:
                    t = i
                    break
            if t == -1:
                return -1
            s = t + 1
            while s < len(p) and p[s] > p[t]:
                s += 1
            s -= 1
            p[s], p[t] = p[t], p[s]
            for i in range((len(p) - t) // 2):
                p[t + 1 + i], p[-1 - i] = p[-1 - i], p[t + 1 + i]
            return p
        
        answer = [nums]
        while True:
            another = nxt(answer[-1])
            if another == -1:
                break
            answer.append(another)
        return answer
