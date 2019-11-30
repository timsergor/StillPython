# 1273. Delete Tree Nodes. Medium. 53.6%.

# A tree rooted at node 0 is given as follows:

# The number of nodes is nodes;
# The value of the i-th node is value[i];
# The parent of the i-th node is parent[i].
# Remove every subtree whose sum of values of nodes is zero.

# After doing so, return the number of nodes remaining in the tree.

class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        sums = {}
        children = {0 : set()}
        for i in range(1, nodes):
            if i not in children:
                children[i] = set()
            if parent[i] not in children:
                children[parent[i]] = set()
            children[parent[i]].add(i)
        for c in children:
            if len(children[c]) == 0:
                sums[c] = value[c]
        
        def check(i):
            if i in sums:
                return sums[i]
            else:
                S = value[i]
                for c in children[i]:
                    S += check(c)
                sums[i] = S
                return S
        
        good = set(range(nodes))
        bad = set()
        
        def extinct(i):
            if i not in bad and i in good:
                good.remove(i)
                for c in children[i]:
                    extinct(c)
        
        for i in range(nodes):
            if check(i) == 0:
                extinct(i)
        return len(good)
