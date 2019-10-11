# 142. Linked List Cycle II. Medium. 33.8%.

# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

# Note: Do not modify the linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        n1 = head
        n2 = head
        d = 0
        if not n2 or not n2.next:
            return None
        n2 = n2.next
        d = 1
        while n2 != n1 and n2.next:
            n2 = n2.next
            n1 = n1.next
            if not n2.next:
                return None
            n2 = n2.next
            d += 1
        if not n2.next:
            return None
        div = []
        for i in range(1,d + 1):
            if d % i == 0:
                div.append(i)
        for k in div:
            n1 = n2 = head
            for i in range(k):
                n2 = n2.next
            for i in range(1,d + 1):
                if n1 == n2:
                    return n1
                n1 = n1.next
                n2 = n2.next
