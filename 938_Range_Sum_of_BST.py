# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        ret = 0
        l = [root]
        while l:
            curr = l.pop(0)
            if curr is None:
                continue
            if curr.val >= L and curr.val <= R:
                ret += curr.val
            l.append(curr.left)
            l.append(curr.right)
        return ret
        
