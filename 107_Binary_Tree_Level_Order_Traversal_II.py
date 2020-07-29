# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        ret = []
        curr = [root]
        while curr:
            next_layer = []
            curr_layer_val = []
            for x in curr:
                curr_layer_val.append(x.val)
                
                if x.left is not None:
                    next_layer.append(x.left)
                    
                    
                if x.right is not None:
                    next_layer.append(x.right)
                
            curr = next_layer
            ret.insert(0, curr_layer_val)
        
        return ret
