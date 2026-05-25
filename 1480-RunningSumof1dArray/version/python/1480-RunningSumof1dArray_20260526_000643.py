# Last updated: 26/05/2026, 00:06:43
1class Solution:
2    def sortedSquares(self, nums: List[int]) -> List[int]:
3        for i in range(len(nums)):
4            nums[i]*=nums[i]
5        new_list = sorted(nums)
6        return new_list