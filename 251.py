# 203. Remove Linked List Elements. Easy. 36.5%.

# Remove all elements from a linked list of integers that have value val.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        node = head
        pre = node
        while node:
            if node.val == val:
                if node == head:
                    head = head.next
                    node = head
                    pre = head
                else:
                    pre.next = node.next
                    node = pre.next
            else:
                pre = node
                node = node.next
        return head
        
# 3min.
