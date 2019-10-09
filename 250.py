# 86. Partition List

# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
# You should preserve the original relative order of the nodes in each of the two partitions.

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head or not head.next:
            return head
        Lh = l = head
        Rh = r = head
        tracer = head
        while tracer:
            if tracer.val < x:
                if l == head and head.val >= x:
                    Lh = l = tracer
                    tracer = tracer.next
                else:
                    y = tracer
                    tracer = tracer.next
                    l.next = y
                    l = y
            else:
                if r == head and head.val < x:
                    Rh = r = tracer
                    tracer = tracer.next
                else:
                    y = tracer
                    tracer = tracer.next
                    r.next = y
                    r = y
        if head and l.val < x and r.val >= x:
            l.next = Rh
            r.next = None
            return Lh
        else:
            return head
