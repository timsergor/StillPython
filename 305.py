# 825. Friends Of Appropriate Ages. Medium. 39.3%.

# Some people will make friend requests. The list of their ages is given and ages[i] is the age of the ith person. 

# Person A will NOT friend request person B (B != A) if any of the following conditions are true:

# age[B] <= 0.5 * age[A] + 7
# age[B] > age[A]
# age[B] > 100 && age[A] < 100
# Otherwise, A will friend request B.

# Note that if A requests B, B does not necessarily request A.  Also, people will not friend request themselves.

# How many total friend requests are made?

class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        char = {}
        for i in range(len(ages)):
            if ages[i] not in char:
                char[ages[i]] = 1
            else:
                char[ages[i]] += 1
        answer = 0
        for c in char:
            for d in char:
                if d > 0.5 * c + 7 and d <= c:
                    if c != d:
                        answer += char[c] * char[d]
                    else:
                        answer += char[c] * (char[c] - 1)
        return answer
