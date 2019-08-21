#83. Remove Duplicates from Sorted List. Easy. 43.2%.
#Given a sorted linked list, delete all duplicates such that each element appear only once.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        tracer = head
        last = head
        while tracer.next:
            tracer = tracer.next
            if tracer.val != last.val:
                last.next = tracer
                last = tracer
        last.next = None
        return(head)
