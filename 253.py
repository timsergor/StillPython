# 904. Fruit Into Baskets. 41.8%.

# In a row of trees, the i-th tree produces fruit with type tree[i].

# You start at any tree of your choice, then repeatedly perform the following steps:

# Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
# Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
# Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

# You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

# What is the total amount of fruit you can collect with this procedure?

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        if len(set(tree)) < 3:
            return len(tree)
        one = another = 0
        types = [0,0]
        answer = 0
        Flag = False
        for i in range(len(tree)):
            if Flag == False:
                if tree[i] != types[0]:
                    types[1] = tree[i]
                    another = i
                    Flag = True
            else:
                if tree[i] not in types:
                    answer = max(answer,i - one)
                    one = another
                    another = i
                    types = [tree[one],tree[another]]
                elif tree[i] != types[1]:
                    types = [types[1],types[0]]
                    another = i
        answer = max(answer,len(tree) - one)
        return answer
