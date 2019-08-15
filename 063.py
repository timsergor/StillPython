#885. Spiral Matrix III. Medium. 65.4%

#On a 2 dimensional grid with R rows and C columns, we start at (r0, c0) facing east.
#Here, the north-west corner of the grid is at the first row and column, and the south-east corner of the grid is at the last row and column.
#Now, we walk in a clockwise spiral shape to visit every position in this grid. 
#Whenever we would move outside the boundary of the grid, we continue our walk outside the grid (but may return to the grid boundary later.) 
#Eventually, we reach all R * C spaces of the grid.
#Return a list of coordinates representing the positions of the grid in the order they were visited.

class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        Step = 1
        D = 0
        coord = [r0,c0]
        
        def MoveForward(coord,D):
            if D == 0:
                coord[1] += 1
            elif D == 1:
                coord[0] += 1
            elif D == 2:
                coord[1] -= 1
            else:
                coord[0] -= 1
            return(coord)
        
        Output = []
        while len(Output) < R * C:
            for i in range(Step):
                if coord[0] >= 0 and coord[0] < R and coord[1] >= 0 and coord[1] < C:
                    Output.append(list(coord))
                coord = MoveForward(coord,D)
            D = (D + 1) % 4
            for i in range(Step):
                if coord[0] >= 0 and coord[0] < R and coord[1] >= 0 and coord[1] < C:
                    Output.append(list(coord))
                coord = MoveForward(coord,D)
            D = (D + 1) % 4
            Step += 1
        return(Output)
