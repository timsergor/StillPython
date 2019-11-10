# 881. Boats to Save People. 44.9%.

# The i-th person has weight people[i], and each boat can carry a maximum weight of limit.

# Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.

# Return the minimum number of boats to carry every given person.  (It is guaranteed each person can be carried by a boat.)

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        answer = 0
        l = 0
        r = len(people) - 1
        while r >= l:
            if l == r:
                return answer + 1
            if people[r] + people[l] > limit:
                r -= 1
            else:
                r -= 1
                l += 1
            answer += 1
        return answer
