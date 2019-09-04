# 2. Add Two Numbers. Medium. 31.7%.

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        source = ListNode((l1.val + l2.val) % 10)
        if l1.val + l2.val >= 10:
            mem = 1
        else:
            mem = 0
        node = source
        while l1.next and l2.next:
            node.next = ListNode(0)
            node = node.next
            l1 = l1.next
            l2 = l2.next
            node.val = (mem + l1.val + l2.val) % 10
            if l1.val + l2.val + mem >= 10:
                mem = 1
            else:
                mem = 0
        while l1.next:
            node.next = ListNode(0)
            node = node.next
            l1 = l1.next
            node.val = (mem + l1.val) % 10
            if l1.val + mem >= 10:
                mem = 1
            else:
                mem = 0
        while l2.next:
            node.next = ListNode(0)
            node = node.next
            l2 = l2.next
            node.val = (mem + l2.val) % 10
            if l2.val + mem >= 10:
                mem = 1
            else:
                mem = 0
        if mem == 1:
            node.next = ListNode(1)
        return source

# 20min
