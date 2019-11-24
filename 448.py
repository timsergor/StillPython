# 990. Satisfiability of Equality Equations. Medium. 41.8%.

# Given an array equations of strings that represent relationships between variables, each string equations[i] has length 4 and takes one of two different forms: "a==b" or "a!=b".  Here, a and b are lowercase letters (not necessarily different) that represent one-letter variable names.

# Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.

class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        def myKey(q):
            return q[1]
        
        equations.sort(key = myKey, reverse = True)
        eq = {}
        for q in equations:
            if q[1] == "=":
                if q[0] in eq and q[-1] in eq:
                    S = eq[q[0]].union(eq[q[-1]])
                    for el in S:
                        eq[el] = S
                elif q[0] in eq:
                    S = eq[q[0]].union(set([q[-1]]))
                    for el in S:
                        eq[el] = S
                elif q[-1] in eq:
                    S = eq[q[-1]].union(set([q[0]]))
                    for el in S:
                        eq[el] = S
                else:
                    S = set([q[0], q[-1]])
                    eq[q[0]] = S
                    eq[q[-1]] = S
            else:
                if (q[-1] in eq and q[0] in eq[q[-1]]) or q[0] == q[-1]:
                    return False
        return True
