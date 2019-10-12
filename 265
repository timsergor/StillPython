# 39. Combination Sum. Medium. 51.2%.
# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
# The same repeated number may be chosen from candidates unlimited number of times.
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dyn = [[[]]]
        for i in range(target):
            dyn.append([])
            for c in candidates:
                if i + 1 - c >= 0:
                    for swath in dyn[i + 1 - c]:
                        if len(swath) == 0 or swath[-1] <= c:
                            dyn[-1].append(swath + [c])
        return dyn[-1]
        
# <9min.
