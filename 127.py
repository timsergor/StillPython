#1094. Car Pooling. Medium. 57.6%.

#You are driving a vehicle that has capacity empty seats initially available for passengers.  The vehicle only drives east (ie. it cannot turn around and drive west.)
#Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.  The locations are given as the number of kilometers due east from your vehicle's initial location.
#Return true if and only if it is possible to pick up and drop off all passengers for all the given trips. 

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        start = {}
        end = {}
        for i in range(len(trips)):
            if trips[i][1] not in start:
                start[trips[i][1]] = trips[i][0]
            else:
                start[trips[i][1]] += trips[i][0]
            if trips[i][2] not in end:
                end[trips[i][2]] = trips[i][0]
            else:
                end[trips[i][2]] += trips[i][0]
        for c in start:
            if c not in end:
                end[c] = 0
        for c in end:
            if c not in start:
                start[c] = 0
        for c in start:
            X = 0
            for d in start:
                if d <= c:
                    X += (start[d] - end[d])
            if X > capacity:
                return False
        return True
