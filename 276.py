# 838. Push Dominoes. 45.5%.

# There are N dominoes in a line, and we place each domino vertically upright.
# In the beginning, we simultaneously push some of the dominoes either to the left or to the right.
# After each second, each domino that is falling to the left pushes the adjacent domino on the left.
# Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.
# When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.
# For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.
# Given a string "S" representing the initial state. S[i] = 'L', if the i-th domino has been pushed to the left; S[i] = 'R', if the i-th domino has been pushed to the right; S[i] = '.', if the i-th domino has not been pushed.
# Return a string representing the final state. 

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        t = 0
                
        def observeR(t):
            l = 1
            t += 1
            while t < len(dominoes) and dominoes[t] == ".":
                l += 1
                t += 1
            if t == len(dominoes) or dominoes[t] == "R":
                return ["R"] * l
            else:
                if l % 2:
                    return ["R"] * ((l + 1) // 2) + ["L"] * ((l + 1) // 2)
                else:
                    return ["R"] * (l // 2) + ["."] + ["L"] * (l // 2)                    
        
        pre = []
        while t < len(dominoes):
            if dominoes[t] == ".":
                t += 1
            elif dominoes[t] == "L":
                pre.extend(["L"] * (t + 1 - len(pre)))
                t = len(pre)
            else:
                pre.extend(["."] * (t - len(pre)))
                pre.extend(observeR(t))
                t = len(pre)
        if t > len(pre):
            pre.extend(["."] * (t - len(pre)))
        return "".join(pre)
