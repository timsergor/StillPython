# 731. My Calendar II. Medium. 46.4%.

# Implement a MyCalendarTwo class to store your events. A new event can be added if adding the event will not cause a triple booking.

# Your class will have one method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

# A triple booking happens when three events have some non-empty intersection (ie., there is some time that is common to all 3 events.)

# For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.

# Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)

class MyCalendarTwo:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        def intersect(I,J):
            if I[0] >= J[1] or J[0] >= I[1]:
                return []
            else:
                return [max(I[0], J[0]), min(I[1],J[1])]
            
        I = [start, end]
        sec = []
        for J in self.events:
            new = intersect(I, J)
            if new:
                for K in sec:
                    if intersect(new, K):
                        return False
                sec.append(new)
        self.events.append(I)
        return True       


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
