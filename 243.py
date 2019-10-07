# 143. Reorder List. Medium. 32.6%.

# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

# You may not modify the values in the list's nodes, only nodes itself may be changed.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        
        def reverse(node):
            if not node or not node.next:
                return node
            pre = None
            current = node
            while current:
                nxt = current.next
                current.next = pre
                pre = current
                current = nxt
            return pre
        
        length = 0
        tracer = head
        while tracer:
            length += 1
            tracer = tracer.next
        m = (length + 1) // 2
        mid = head
        while m:
            pre = mid
            mid = mid.next
            m -= 1
        
        mid = reverse(mid)
        pre.next = None
        
        def Merge(head1,head2):
            if not head2:
                return head1
            if not head1.next:
                head1.next = head2
                return head1
            else:
                sec1 = head1.next
                head1.next = head2
                sec2 = head2.next
                third = Merge(sec1,sec2)
                head2.next = third
                return head1
        
        head = Merge(head,mid)
        return head
