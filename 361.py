# 1109. Corporate Flight Bookings. Medium. 49.3%.

# There are n flights, and they are labeled from 1 to n.

# We have a list of flight bookings.  The i-th booking bookings[i] = [i, j, k] means that we booked k seats from flights labeled i to j inclusive.

# Return an array answer of length n, representing the number of seats booked on each flight in order of their label.

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        answer = []
        char = {}
        for b in bookings:
            if b[0] not in char:
                char[b[0]] = b[2]
            else:
                char[b[0]] += b[2]
            if b[1] + 1 not in char:
                char[b[1] + 1] = -b[2]
            else:
                char[b[1] + 1] -= b[2]
        x = 0
        for t in range(1, n + 1):
            if t in char:
                x += char[t]
            answer.append(x)
        return answer
