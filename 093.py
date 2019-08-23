#841. Keys and Rooms. Medium. 61%.

#There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room. 
#Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.
#Initially, all the rooms start locked (except for room 0). 
#You can walk back and forth between rooms freely.
#Return true if and only if you can enter every room.

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        space = [0]
        char = {0:True}
        f = 0
        while f < len(space):
            l = len(space)
            for i in range(f,l):
                for j in range(len(rooms[space[i]])):
                    if rooms[space[i]][j] not in char:
                        char[rooms[space[i]][j]] = True
                        space.append(rooms[space[i]][j])
            f = l
        if len(space) == len(rooms):
            return(True)
        else:
            return(False)
