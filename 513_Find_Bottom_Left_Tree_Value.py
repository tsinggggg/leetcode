# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        
        
        depth = 0
        
        record = dict()
        record[0] = [root]
        l = [(root,0)]
        
        while l:
            curr, d = l.pop(0)
            

            if curr.left is not None:
                l.append((curr.left,d+1))
                
                if d+1 not in record:
                    record[d+1] = [curr.left]
                else:
                    record[d+1].append(curr.left)
                    
                
            if curr.right is not None:
                l.append((curr.right, d+1))
                         
                if (d+1) not in record:
                    record[d+1] = [curr.right]
                else:
                    record[d+1].append(curr.right)
              
        depth = max(record.keys())             
        return record[depth][0].val
        
        
        
