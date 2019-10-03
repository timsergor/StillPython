# 206. Reverse Linked List. Easy. 57.1%.

# Reverse a singly linked list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        front = head.next
        mid = front
        head.next = None
        while front.next:
            front = front.next
            mid.next = head
            head = mid
            mid = front
        mid.next = head
        return mid
