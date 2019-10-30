# 981. Time Based Key-Value Store

# Create a timebased key-value store class TimeMap, that supports two operations.

# 1. set(string key, string value, int timestamp)

# Stores the key and value, along with the given timestamp.
# 2. get(string key, int timestamp)

# Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
# If there are multiple such values, it returns the one with the largest timestamp_prev.
# If there are no values, it returns the empty string ("").

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.book = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.book:
            self.book[key].append((timestamp, value))
        else:
            self.book[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.book:
            l = 0
            r = len(self.book[key]) - 1
            while r - l > 1:
                if self.book[key][(r + l) // 2][0] > timestamp:
                    r = (r + l) // 2
                else:
                    l = (r + l) // 2
            if self.book[key][r][0] <= timestamp:
                return self.book[key][r][1]
            elif self.book[key][l][0] <= timestamp:
                return self.book[key][l][1]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
