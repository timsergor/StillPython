# 150. Evaluate Reverse Polish Notation. Medium. 33.6%.

# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, /. Each operand may be an integer or another expression.

# Note:

# Division between two integers should truncate toward zero.
# The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def op(s):
            return s in ["+", "-", "*", "/"]
        
        f = len(tokens) - 3
        while len(tokens) > 1:
            if f > len(tokens) - 3:
                f -= 1
            elif not(op(tokens[f]) or op(tokens[f + 1])) and op(tokens[f + 2]):
                if tokens[f + 2] == "+":
                    tokens[f] = str(int(tokens[f]) + int(tokens[f + 1]))
                    tokens.pop(f + 1)
                    tokens.pop(f + 1)
                elif tokens[f + 2] == "-":
                    tokens[f] = str(int(tokens[f]) - int(tokens[f + 1]))
                    tokens.pop(f + 1)
                    tokens.pop(f + 1)
                elif tokens[f + 2] == "*":
                    tokens[f] = str(int(tokens[f]) * int(tokens[f + 1]))
                    tokens.pop(f + 1)
                    tokens.pop(f + 1)
                elif tokens[f + 2] == "/":
                    tokens[f] = str(int(int(tokens[f]) / int(tokens[f + 1])))
                    tokens.pop(f + 1)
                    tokens.pop(f + 1)
            else:
                f -= 1
        return int(tokens[0])
