# 82. Remove Duplicates from Sorted List II. Medium. 34.2%.

# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        pre = head
        tracer = head
        Flag = "*"
        while tracer.next:
            if tracer.next.val == tracer.val or tracer.val == Flag:
                Flag = tracer.val
                if tracer == head:
                    head = head.next
                    tracer = head
                    pre = head
                else:
                    pre.next = tracer.next
                    tracer = tracer.next
            else:
                Flag = tracer.val
                if tracer != head:
                    pre = tracer
                tracer = tracer.next
        if Flag == tracer.val:
            if tracer == head:
                return None
            pre.next = None
            return head   
        return head
