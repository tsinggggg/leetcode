class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        arr_len = len(arr)
        ind = 0
        while ind < arr_len:
            if arr[ind] == 0:
                arr.insert(ind, 0)
                ind += 2
                arr.pop(-1)
            else:
                ind += 1
