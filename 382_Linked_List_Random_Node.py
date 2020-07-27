# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.len = 0
        self.head = head
        curr = head
        while curr is not None:
            self.len += 1
            curr = curr.next
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        import random
        rand = random.randint(0, self.len-1)
        
        curr = self.head
        
        for i in range(rand):
            curr = curr.next
            
        return curr.val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
