# 1146. Snapshot Array. Medium. 33.1%.

# Implement a SnapshotArray that supports the following interface:

# SnapshotArray(int length) initializes an array-like data structure with the given length.  Initially, each element equals 0.
# void set(index, val) sets the element at the given index to be equal to val.
# int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
# int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id

class SnapshotArray:

    def __init__(self, length: int):
        self.array = {}
        self.snaps = -1
        
    def set(self, index: int, val: int) -> None:
        if index not in self.array:
            self.array[index] = [(0,-1)]
        self.array[index].append((val,self.snaps))

    def snap(self) -> int:
        self.snaps += 1
        return self.snaps

    def get(self, index: int, snap_id: int) -> int:
        if index not in self.array:
            return 0
        l = 0
        r = len(self.array[index]) - 1
        while r - l > 1:
            if self.array[index][((r + l) // 2)][1] < snap_id:
                l = (r + l) // 2
            else:
                r = (r + l) // 2
        if self.array[index][r][1] < snap_id:
            return self.array[index][r][0]
        return self.array[index][l][0]
        
# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
