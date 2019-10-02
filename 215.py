# 19. Remove Nth Node From End of List. Medium. 34.6%.

# Given a linked list, remove the n-th node from the end of list and return its head.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        machine = [head,head,head]
        while n > 0:
            machine[2] = machine[2].next
            n -= 1
        if machine[2] == None:
            return head.next
        machine[1] = machine[1].next
        machine[2] = machine[2].next
        while machine[2]:
            machine[0] = machine[0].next
            machine[1] = machine[1].next
            machine[2] = machine[2].next
        machine[0].next = machine[1].next
        return head
