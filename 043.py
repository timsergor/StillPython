#1041. Robot Bounded In Circle. 44.5%

#On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:
#"G": go straight 1 unit;
#"L": turn 90 degrees to the left;
#"R": turn 90 degress to the right.
#The robot performs the instructions given in order, and repeats them forever.
#Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        vector = [0,0]
        direction = 0
        for i in range(len(instructions)):
            if instructions[i] == "G":
                if direction == 0:
                    vector[1] += 1
                elif direction == 1:
                    vector[0] += 1
                elif direction == 2:
                    vector[1] -= 1
                elif direction == 3:
                    vector[0] -= 1
            elif instructions[i] == "L":
                direction = (direction - 1) % 4
            else:
                direction = (direction + 1) % 4
        if vector == [0,0]:
            return(True)
        else:
            if direction:
                return(True)
            else:
                return(False)
