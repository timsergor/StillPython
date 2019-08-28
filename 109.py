#515. Find Largest Value in Each Tree Row. Medium. 58.4%.

#You need to find the largest value in each row of a binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        def solution(Node):
            if Node == None:
                return []
            else:
                M = [Node.val]
                Ml = solution(Node.left)
                Mr = solution(Node.right)
                for i in range(max(len(Ml),len(Mr))):
                    if i < len(Ml) and i < len(Mr):
                        M.append(max(Ml[i],Mr[i]))
                    elif i >= len(Ml):
                        M.append(Mr[i])
                    else:
                        M.append(Ml[i])
                return(M)
        
        return(solution(root))
        
# 7min.
