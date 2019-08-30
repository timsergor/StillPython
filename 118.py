# 946. Validate Stack Sequences. Medium.
#Given two sequences pushed and popped with distinct values, return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if len(pushed) != len(popped):
            return(False)
        stack = []
        pushed.reverse()
        popped.reverse()
        for i in range(len(pushed) + len(popped)):
            if not pushed:
                if stack and popped[-1] == stack[-1]:
                    popped.pop()
                    stack.pop()
                else:
                    return False
            else:
                if popped and stack and popped[-1] == stack[-1]:
                    popped.pop()
                    stack.pop()
                else:
                    stack.append(pushed.pop())
        return True
