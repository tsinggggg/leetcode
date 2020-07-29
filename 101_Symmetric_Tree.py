# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if root is None:
            return True
        
        current = [root]
        while current:
            next_layer = []
            val = []
            for x in current:
                if x.left is not None:
                    
                    next_layer.append(x.left)
                    val.append(x.left.val)
                else:
                    
                    val.append(None)
                    
                if x.right is not None:
                    next_layer.append(x.right)
                    val.append(x.right.val)
                else:
                    val.append(None)


            if not val == list(reversed(val)):
                return False
                
            current = next_layer
                
        return True
                    
                
    
    
        
