# 24. Swap Nodes in Pairs. Medium. 48.5%.

# Given a linked list, swap every two adjacent nodes and return its head.

# You may not modify the values in the list's nodes, only nodes itself may be changed.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        second = head.next
        head.next = second.next
        second.next = head
        realhead = second
        pre = head
        head = head.next
        while head:
            if head.next:
                second = head.next
                pre.next = second
                head.next = second.next
                second.next = head
                pre = head
                head = head.next
            else:
                break
        return realhead
