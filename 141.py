# 21. Merge Two Sorted Lists. Easy. 48.7%.

# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            start = l1
            l1 = l1.next
        else:
            start = l2
            l2 = l2.next
        node = start
        while l1 or l2:
            if l1 == None:
                node.next = l2
                return start
            elif l2 == None:
                node.next = l1
                return start
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        return start
        
# 20min
