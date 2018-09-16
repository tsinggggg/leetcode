class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import itertools
        return [list(x) for x in itertools.permutations(nums)]