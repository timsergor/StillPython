# 328. Odd Even Linked List. Medium. 50.5%.

# Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd = head
        if head:
            head2 = even = head.next
        while odd and even:
            mem1 = even.next
            if mem1:
                odd.next = mem1
                odd = mem1
                mem2 = mem1.next
                if mem2:
                    even.next = mem2
                    even = mem2
                else:
                    odd.next = head2
                    even.next = None
                    return head
            else:
                odd.next = head2
                even.next = None
                return head
        return head
        
# 25min.
