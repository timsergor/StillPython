# 853. Car Fleet. Medium. 41.4%.

# N cars are going to the same destination along a one lane road.  The destination is target miles away.

# Each car i has a constant speed speed[i] (in miles per hour), and initial position position[i] miles towards the target along the road.

# A car can never pass another car ahead of it, but it can catch up to it, and drive bumper to bumper at the same speed.

# The distance between these two cars is ignored - they are assumed to have the same position.

# A car fleet is some non-empty set of cars driving at the same position and same speed.  Note that a single car is also a car fleet.

# If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

# How many car fleets will arrive at the destination?

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position:
            return 0
        cars = position
        for i in range(len(cars)):
            cars[i] = (target - cars[i], speed[i])
        
        def myKey(c):
            return c[0]
        
        cars.sort(key = myKey, reverse = True)
        t = cars[-1][0] / cars[-1][1]
        answer = 1
        cars.pop()
        for i in range(len(cars)):
            while cars and cars[-1][0] / cars[-1][1] <= t:
                cars.pop()
            if cars:
                t = cars[-1][0] / cars[-1][1]
                answer += 1
                cars.pop()
        return answer
