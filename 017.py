#Given a non-empty, singly linked list with head node head, return a middle node of linked list.
#If there are two middle nodes, return the second middle node.
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode):
        M = []
        while head.next:
            M.append(head)
            head = head.next
        M.append(head)    
        return(M[len(M)//2])  
