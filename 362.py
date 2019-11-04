# 756. Pyramid Transition Matrix. Medium. 52.9%.

# We are stacking blocks to form a pyramid. Each block has a color which is a one letter string.

# We are allowed to place any color block C on top of two adjacent blocks of colors A and B, if and only if ABC is an allowed triple.

# We start with a bottom row of bottom, represented as a single string. We also start with a list of allowed triples allowed. Each allowed triple is represented as a string of length 3.

# Return true if we can build the pyramid all the way to the top, otherwise false.

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        pre = []
        for s in bottom:
            pre.append([s])
        char = {}
        for s in allowed:
            if s[0:2] not in char:
                char[s[0:2]] = set([s[2]])
            else:
                char[s[0:2]].add(s[2])
        dyn = []
        for i in range(len(pre) - 1):
            dyn.append(set())
            for a in pre[i]:
                for b in pre[i + 1]:
                    if a + b in char:
                        dyn[-1].update(char[a + b])
            if len(dyn[-1]) == 0:
                return False
        while len(dyn) > 1:
            pre = dyn
            dyn = []
            for i in range(len(pre) - 1):
                dyn.append(set())
                for a in pre[i]:
                    for b in pre[i + 1]:
                        if a + b in char:
                            dyn[-1].update(char[a + b])
                if len(dyn[-1]) == 0:
                    return False
        return True
