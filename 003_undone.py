#найти сумму элементов кучи, находящихся в данном диапозоне

# Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
# Output: 32

'''
class TreeNode:
    def __init__(self, x, root):
        self.place = x
        self.val = root[x]
        self.root = root
    
    def left(self):
        return(TreeNode(2*self.place+1, root))

    def right(self):
        return(TreeNode(2*self.place+2, root))    


def rangeSumBST(root: TreeNode, L: int, R: int):
    s = 0
    N = TreeNode(0, root)
    if N.val < L:
        return(rangeSumBST(N.left(),L,R))
    elif N.val > R:
        return(rangeSumBST(N.right(),L,R))
    else:
        s = s+N.val+rangeSumBST(N.left(),L,R)+rangeSumBST(N.right(),L,R)
    return(s)

'''
class TreeNode:
    def __init__(self, x):
        self.place = x
        self.val = root[x]
    
    def left(self):
        return(TreeNode(2*self.place+1))

    def right(self):
        return(TreeNode(2*self.place+2))    

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int):
        s = 0
        N = TreeNode(0)
        if N.val < L:
            return(rangeSumBST(N.left(),L,R))
        elif N.val > R:
            return(rangeSumBST(N.right(),L,R))
        else:
            s = s+N.val+rangeSumBST(N.left(),L,R)+rangeSumBST(N.right(),L,R)
        return(s)

root = [10,5,15,3,7,12,18]
L = 7
R = 15



print(rangeSumBST(root,L,R))
