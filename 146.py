# 234. Palindrome Linked List. Easy.

# Given a singly linked list, determine if it is a palindrome.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        counter = 0
        if head == None:
            return True
        node = head
        while node.next:
            counter += 1
            node = node.next
        if counter == 0:
            return True
        target = (counter + 1) // 2
        midnode = head
        while target > 0:
            midnode = midnode.next
            target -= 1
        left = midnode
        if left.next:
            mid = left.next
        else:
            return left.val == head.val
        while mid.next:
                right = mid.next
                mid.next = left
                left = mid
                mid = right
        mid.next = left
        head2 = mid
        for i in range((counter + 1) // 2):
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        return True
