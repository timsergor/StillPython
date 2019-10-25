# 61. Rotate List. Medium. 28.2%.

# Given a linked list, rotate the list to the right by k places, where k is non-negative.

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        l = 0
        t = head
        while t:
            l += 1
            t = t.next
        k = k % l
        tracer = head
        tail = head
        while k > 0:
            tail = tail.next
            k -= 1
        while tail.next:
            tail = tail.next
            tracer = tracer.next
        tail.next = head
        newhead = tracer.next
        tracer.next = None
        return newhead
