#1104. Path In Zigzag Labelled Binary Tree. Medium. 70.5%.

#In an infinite binary tree where every node has two children, the nodes are labelled in row order.
#In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.
#Given the label of a node in this tree, return the labels in the path from the root of the tree to the node with that label.

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        path = []
        while label:
            path.append(label)
            label = label // 2
        realpath = []
        Flag = 1 - len(path) % 2
        T = 1
        while path:
            if 1 - Flag:
                realpath.append(path.pop())
            else:
                realpath.append((T * 2) - ((path.pop()) - T) - 1)
            T *= 2
            Flag = 1 - Flag
        return(realpath)
