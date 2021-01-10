# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        
        if head.next is None:
            return head
        
        second = self.reverseList(head.next)
        curr = second
        
        while curr.next is not None:
            curr = curr.next
            
        curr.next = head
        head.next = None
        
        return second
        
