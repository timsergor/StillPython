# 160. Intersection of Two Linked Lists. Easy. 36.1%.

# Write a program to find the node at which the intersection of two singly linked lists begins.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        char = {}
        while headA and headB:
            if headA not in char:
                char[headA] = True
                headA = headA.next
            else:
                return headA
            if headB not in char:
                char[headB] = True
                headB = headB.next
            else:
                return headB
        while headA:
            if headA not in char:
                char[headA] = True
                headA = headA.next
            else:
                return headA
        while headB:
            if headB not in char:
                char[headB] = True
                headB = headB.next
            else:
                return headB
                
    # 5-6min
