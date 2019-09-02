# 1090. Largest Values From Labels. Medium. 57.3%.
# We have a set of items: the i-th item has value values[i] and label labels[i].
# Then, we choose a subset S of these items, such that:

|S| <= num_wanted
For every label L, the number of items in S with label L is <= use_limit.
Return the largest possible sum of the subset S.

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        def val(couple):
            return(couple[0])
            
        toOrder = []
        for i in range(len(values)):
            toOrder.append((values[i],labels[i]))
        toOrder.sort(key = val, reverse = True)
        answer = 0
        char = {}
        for i in range(len(toOrder)):
            if num_wanted == 0:
                return answer
            if toOrder[i][1] in char and char[toOrder[i][1]] == use_limit:
                pass
            else:
                answer += toOrder[i][0]
                if toOrder[i][1] not in char:
                    char[toOrder[i][1]] = 1
                else:
                    char[toOrder[i][1]] += 1
                num_wanted -= 1    
        return answer
