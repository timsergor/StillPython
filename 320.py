# 1237. Find Positive Integer Solution for a Given Equation. Easy. 61.9%.

# Given a function  f(x, y) and a value z, return all positive integer pairs x and y where f(x,y) == z.

# The function is constantly increasing, i.e.:

# f(x, y) < f(x + 1, y)
# f(x, y) < f(x, y + 1)

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""
class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        t = 0
        x = 1
        y = 1
        lastx = 1001
        answer = []
        while y < 1001:
            t = customfunction.f(x,y)
            if t >= z:
                if t == z:
                    answer.append([x,y])
                if x == 1:
                    break
                lastx = x
                x = 1
                y += 1
            elif x == lastx:
                x = 1
                y += 1
            else:
                x += 1
        return answer
