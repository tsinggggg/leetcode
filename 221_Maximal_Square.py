class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        if len(matrix) == 0:
            return 0
        
        r,c = len(matrix), len(matrix[0])
        l = min(r, c)
        mat = [[[0] * c for _ in range(r)] for _ in range(l)]
        
        for ind1 in range(r):
            for ind2 in range(c):
                for ind3 in range(l):
                    s = ind3 + 1
                    if s == 1:
                        mat[ind3][ind1][ind2] = int(matrix[ind1][ind2] == "1")
                    elif ind1 + s > r or ind2 + s > c:
                        mat[ind3][ind1][ind2] = 0
                    elif mat[ind3 - 1][ind1][ind2] == 0:
                        mat[ind3][ind1][ind2] = 0
                    else:
                        temp_set = set(matrix[ind1 + s - 1][ind2 : (ind2 + s)] + 
                                       [x[ind2 + s - 1] for x in matrix[ind1 : (ind1 + s)]]
                                      )
                        if '1' in temp_set and '0' not in temp_set:
                            mat[ind3][ind1][ind2] = 1
                            
        temp_max = 0
        for ind3 in range(l):
            if sum([x for y in mat[ind3] for x in y ]) > 0:
                temp_max = (ind3 + 1) ** 2

        return temp_max

        
