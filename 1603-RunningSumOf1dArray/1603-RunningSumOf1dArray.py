# Last updated: 26/05/2026, 00:49:21
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0 
        for i in range(len(nums)):
            sum= nums[i]+sum 
            nums[i]=sum
        return nums
        