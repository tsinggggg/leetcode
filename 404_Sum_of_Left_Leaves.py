# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        if root is None:
            return 0
        
        l = [root]
        ret = 0
        
        while l:
            curr = l.pop(0)
            if curr.left is not None:
                l.append(curr.left)
                if curr.left.left is None and curr.left.right is None:
                    ret += curr.left.val
            if curr.right is not None:
                l.append(curr.right)
                
        return ret
                
        
