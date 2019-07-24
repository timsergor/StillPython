#894. All Possible Full Binary Trees. Medium. 71.5%

#A full binary tree is a binary tree where each node has exactly 0 or 2 children.
#Return a list of all possible full binary trees with N nodes.  Each element of the answer is the root node of one possible tree.
#Each node of each tree in the answer must have node.val = 0.
#You may return the final list of trees in any order.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N % 2 == 0:
            return([])
        All = [[],[TreeNode(0)],[]]
        if N == 1:
            return(All[1])
        else:
            for i in range(3,N+1):
                if i % 2 == 0:
                    All.append([])
                else:
                    All.append([])
                    for j in range(i):
                        Ml = All[j]
                        Mr = All[i-1-j]
                        for l in Ml:
                            for r in Mr:
                                New = TreeNode(0)
                                New.left = l
                                New.right = r
                                All[i].append(New)
            return(All[N])
   
   # 30-120 min
