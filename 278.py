# 895. Maximum Frequency Stack. Hard. 57.9%.

# Implement FreqStack, a class which simulates the operation of a stack-like data structure.

# FreqStack has two functions:

# push(int x), which pushes an integer x onto the stack.
# pop(), which removes and returns the most frequent element in the stack.
# If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.

class FreqStack:

    def __init__(self):
        self.stack = []
        self.els = {}

    def push(self, x: int) -> None:
        if x not in self.els:
            self.els[x] = 1
        else:
            self.els[x] += 1
        while len(self.stack) < self.els[x]:
            self.stack.append([])
        self.stack[self.els[x] - 1].append(x)

    def pop(self) -> int:
        x = self.stack[-1].pop()
        self.els[x] -= 1
        if len(self.stack[-1]) == 0:
            self.stack.pop()
        return x

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
