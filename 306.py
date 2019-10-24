# 92. Reverse Linked List II. Medium. 36.4%.

# Reverse a linked list from position m to n. Do it in one-pass.

# Note: 1 ≤ m ≤ n ≤ length of list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if n == m:
            return head
        t = 1
        tracer = head
        while t < m:
            pre = tracer
            tracer = tracer.next
            t += 1
        edge = tracer
        node = tracer.next
        t += 1
        while t < n:
            node2 = node.next
            node.next = tracer
            tracer = node
            node = node2
            t += 1
        edge.next = node.next
        node.next = tracer
        if m > 1:
            pre.next = node
        if m > 1:
            return head
        else:
            return node
