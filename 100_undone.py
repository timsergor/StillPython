#558. Quad Tree Intersection. Easy. 41.8%.

#A quadtree is a tree data in which each internal node has exactly four children: topLeft, topRight, bottomLeft and bottomRight. Quad trees are often used to partition a two-dimensional space by recursively subdividing it into four quadrants or regions.

#We want to store True/False information in our quad tree. The quad tree is used to represent a N * N boolean grid. For each node, it will be subdivided into four children nodes until the values in the region it represents are all the same. Each node has another two boolean attributes : isLeaf and val. isLeaf is true if and only if the node is a leaf node. The val attribute for a leaf node contains the value of the region it represents.

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        theNode = Node()
        def solution(Node1, Node2):
            if Node1.isLeaf:
                if Node1.val == True:
                    return(Node1)
                else:
                    return(Node2)
            elif Node2.isLeaf:
                if Node2.val == True:
                    return(Node2)
                else:
                    return(Node1)
            else:
                orNode = Node()
                orNode.isLeaf = False
                orNode.topLeft = solution(Node1.topLeft, Node2.topLeft)
                orNode.topRight = solution(Node1.topRight, Node2.topRight)
                orNode.bottomLeft = solution(Node1.bottomLeft, Node2.bottomLeft)
                orNode.bottomRight = solution(Node1.bottomRight, Node2.bottomRight)
                return(orNode)
        
        def reduction(aNode):
            if aNode.isLeaf:
                return(aNode)
            elif aNode.topLeft.isLeaf and aNode.topRight.isLeaf and aNode.bottomLeft.isLeaf and aNode.bottomRight.isLeaf:
                if aNode.topLeft.val and aNode.topRight.val and aNode.bottomLeft.val and aNode.bottomRight.val:
                    return(Node(True, True))
                elif not (aNode.topLeft.val or aNode.topRight.val or aNode.bottomLeft.val or aNode.bottomRight.val):
                    return(Node(False,True))
                else:
                    return(aNode)
            else:
                return(reduction(Node(None,False,reduction(aNode.topLeft),reduction(aNode.topRight),reduction(aNode.bottomLeft),reduction(aNode.bottomRight))))
        
        preanswer = solution(quadTree1,quadTree2)
        return(reduction(preanswer))
