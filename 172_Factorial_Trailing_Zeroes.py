class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        power = 1
        five_power = 5
        count = 0
        while five_power<=n:
            count += n//five_power
            power += 1
            five_power *= 5
        return count
        
#         five = 0
#         record = dict()
#         for x in range(0, 1+n, 5):
#             to_add, record = helper(x, record)
#             five += to_add

#         return five


    
# def helper(x, record):
#     count = 0
#     curr = x
#     if curr%5 == 0 and curr > 0:
#         count = 1 + record.get(int(curr/5), 0)
#         record[x] = count
#     return count, record
                
