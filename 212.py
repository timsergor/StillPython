# 147. Insertion Sort List. Medium. 38.5%.

# Sort a linked list using insertion sort.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        for i in range(1,length):
            node = head
            for j in range(i):
                pre = node
                node = node.next
            if node.val < head.val:
                pre.next = node.next
                node.next = head
                head = node
            else:
                nodel = head
                noder = head.next
                while noder.val <= node.val and noder != node:
                    nodel = noder
                    noder = noder.next
                if noder != node:
                    pre.next = node.next
                    nodel.next = node
                    node.next = noder
        return head
