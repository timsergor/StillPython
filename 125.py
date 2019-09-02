# 20. Valid Parentheses. Easy. 37.`%.

#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An input string is valid if:
#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Note that an empty string is also considered valid.

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append("(")
            elif s[i] == "[":
                stack.append("[")
            elif s[i] == "{":
                stack.append("{")
            elif s[i] == ")":
                if len(stack) and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif s[i] == "]":
                if len(stack) and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            elif s[i] == "}":
                if len(stack) and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True
