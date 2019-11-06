# 752. Open the Lock. Medium. 47.9%.

# You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

# The lock initially starts at '0000', a string representing the state of the 4 wheels.

# You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

# Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        char = {"0000" : 0}
        now = ["0000"]
        t = 0
        dead = {d : True for d in deadends}
        if "0000" in dead:
            return -1
        
        def nxt(code):
            for i in range(4):
                yield (code[:i] + str((int(code[i]) + 1) % 10) + code[i + 1:])
                yield (code[:i] + str((int(code[i]) - 1) % 10) + code[i + 1:])
        
        while now:
            t += 1
            new = []
            for code in now:
                for s in nxt(code):
                    if s not in char and s not in deadends:
                        char[s] = t
                        new.append(s)
                        if s == target:
                            return t
            now = new
        return -1
