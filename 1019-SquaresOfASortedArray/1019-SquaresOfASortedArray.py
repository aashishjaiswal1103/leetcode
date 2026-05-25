# Last updated: 26/05/2026, 00:49:26
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i]*=nums[i]
        new_list = sorted(nums)
        return new_list