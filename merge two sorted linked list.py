# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
#         cur_node_1=l1
#         cur_node_2=l2
        
#         if cur_node_1 is None:
#             return l2
#         elif cur_node_2 is None:
#             return l1
#         else:
#             if cur_node_1.val<=cur_node_2.val:
#                 new_list=ListNode(cur_node_1.val)
#                 cur_node_1=l1.next
#             else:
#                 new_list=ListNode(cur_node_2.val)
#                 cur_node_2=l2.next
        
#         cur=new_list
        
#         while cur_node_1 is not None or cur_node_2 is not None:
            
#             if cur_node_1 is not None and cur_node_2 is not None:
                
#                 if cur_node_1.val<=cur_node_2.val:
#                     cur.next=ListNode(cur_node_1.val)
#                     cur=cur.next
#                     cur_node_1=cur_node_1.next
                    
#                 else:
#                     cur.next=ListNode(cur_node_2.val)
#                     cur=cur.next
#                     cur_node_2=cur_node_2.next
#             elif cur_node_1 is None:
#                     cur.next=ListNode(cur_node_2.val)
#                     cur=cur.next
#                     cur_node_2=cur_node_2.next   
#             elif cur_node_2 is None:
#                     cur.next=ListNode(cur_node_1.val)
#                     cur=cur.next
#                     cur_node_1=cur_node_1.next  
        
#         return new_list


        if l1 is None:
            return l2
        if l2 is None:
            return l1

        helper=ListNode(0)
        cur=helper

        while l1 is not None and l2 is not None:

            if l1.val<=l2.val:
                cur.next=ListNode(l1.val)
                cur=cur.next
                l1=l1.next
            else:
                cur.next=ListNode(l2.val)
                cur=cur.next
                l2=l2.next

        if l1 is None:
            cur.next=l2
            
        else:
            cur.next=l1

        return helper.next
            