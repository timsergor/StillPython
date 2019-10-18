# 735. Asteroid Collision. Medium. 39.3%.

# We are given an array asteroids of integers representing asteroids in a row.

# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        i = len(asteroids) - 1
        while i > -1:
            if asteroids[i] > 0 and i < len(asteroids) - 1 and asteroids[i + 1] < 0:
                if abs(asteroids[i]) > abs(asteroids[i + 1]):
                    asteroids.pop(i + 1)
                elif abs(asteroids[i]) < abs(asteroids[i + 1]):
                    asteroids.pop(i)
                    i -= 1
                else:
                    asteroids.pop(i)
                    asteroids.pop(i)
                    i -= 1
            else:
                i -= 1
        return asteroids
