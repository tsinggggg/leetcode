class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        import itertools
        record = {str(i):{'col':[],
                          'row':[],
                          'block':[]} for i in range(1,10)}
        
        for i, j in itertools.product(range(9), range(9)):
            
            if board[i][j] != '.':
                
                item = board[i][j]
                
                item_dict = record[item]
                
                if i in item_dict['row']:
                    return False
                else:
                    item_dict['row'].append(i)
                    
                if j in item_dict['col']:
                    return False
                else:
                    item_dict['col'].append(j)
                
                item_block = self.get_block_id(i, j)
                if item_block in item_dict['block']:
                    return False
                else:
                    item_dict['block'].append(item_block)
        return True
        
    @staticmethod    
    def get_block_id(i,j):
        x = i//3
        y = j//3
        return (x, y)