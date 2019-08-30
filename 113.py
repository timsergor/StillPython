849. Maximize Distance to Closest Person. Easy. 41.5%.

#In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 
#There is at least one empty seat, and at least one person sitting.
#Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 
#Return that maximum distance to closest person.

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        space = 1
        newspace = 0
        for i in range(len(seats)):
            
            if seats[i] == 0:
                newspace += 1
            else:
                space = max(space, newspace)
                newspace = 0
        space = (max(space, newspace) + 1) // 2
        leftspace = rightspace = 0
        for i in range(len(seats)):
            if seats[i] == 0:
                leftspace += 1
            else:
                break
        for i in range(len(seats)):
            if seats[-1 - i] == 0:
                rightspace += 1
            else:
                break
        return(max(space, leftspace, rightspace))
