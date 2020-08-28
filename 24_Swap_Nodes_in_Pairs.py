# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        ret = ListNode()
        ret_curr = ret
        curr = head
        stack = []
        
        while curr is not None:
            stack.append(curr)
            curr = curr.next
            if curr is not None:
                stack.append(curr)
                curr = curr.next
            
            temp = stack.pop(-1)
            ret_curr.next = temp
            ret_curr = ret_curr.next
            
            if stack:
                temp = stack.pop(-1)
                ret_curr.next = temp
                ret_curr = ret_curr.next
        
        ret_curr.next = None
        
        return ret.next
                
            
            
        
        
#         curr = head
#         ret = head.next
        
#         while curr is not None and curr.next is not None:
            
#             temp = curr.next
            
#             curr.next = temp.next
            
#             temp.next = curr
            
#             curr = curr.next

#         return ret
