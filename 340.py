# 725. Split Linked List in Parts. Medium. 50%.

# Given a (singly) linked list with head node root, write a function to split the linked list into k consecutive linked list "parts".

# The length of each part should be as equal as possible: no two parts should have a size differing by more than 1. This may lead to some parts being null.

# The parts should be in order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal parts occurring later.

# Return a List of ListNode's representing the linked list parts that are formed.

# Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        l = 0
        node = root
        while node:
            l += 1
            node = node.next
        answer = []
        for i in range(k):
            if root:
                answer.append(root)
                for j in range(l // k - 1):
                    root = root.next
                if i + 1 <= l % k and (l // k > 0) and root:
                    root = root.next
                if root:
                    pre = root
                    root = root.next
                    pre.next = None
            else:
                answer.append(None)
        return answer
