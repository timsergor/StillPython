# 554. Brick Wall. Medium. 48.4%.

# There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the same height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.

# The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right.

# If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.

# You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        char = {}
        for i in range(len(wall)):
            for j in range(1,len(wall[i])):
                wall[i][j] += wall[i][j - 1]
                if wall[i][j - 1] not in char:
                    char[wall[i][j - 1]] = 1
                else:
                    char[wall[i][j - 1]] += 1
        answer = 0
        tis = 0
        for c in char:
            if char[c] > tis:
                tis = char[c]
        return len(wall) - tis
